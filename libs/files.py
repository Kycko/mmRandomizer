from   os      import path  as osPath
from   sys     import exit  as SYSEXIT
import globalFuncs          as GF
import globals              as G
from   output  import progress

# shared class
class File():
  def __init__(self,dir:str,file:str,write:bool):
    self.name      = file
    self.path      = osPath.join(dir ,file)
    self.writePath = osPath.join('./',file)
    self.write     = write
  def read    (self):
    def _parse():
      self.lines = []
      self.titles = self.raw[0].split(',')
      for line in self.raw[1:]:
        final    = {}
        splitted = line.split(',')
        for i in range(len(splitted)): final[self.titles[i]] = splitted[i]
        self.lines.append(final)
    with  open(self.path,'r',encoding='utf-8') as f:
      self.raw = [line.strip() for line in f]
    _parse()

# per-file classes
class Championships(File):
  def read(self):
    super().read()
    self.db = {}
    for line in self.lines:
      self.db[line['Acronym']] = {'startWeek':int(line['Season Start']),
                                  'endWeek'  :int(line['Season End'])}
    # DEBUG
    # for champ,data in self.db.items():
    #   print(champ.ljust(5) + ' : ' + str(data))
class Tracks       (File):
  def read(self):
    def _roster():
      def _add (country:str,ID:str,region:str):
        # region = eu/ap/int
        rg = self.roster[region]
        if country not in rg.keys(): rg[country] = []
        rg[country].append(ID)
      # roster format = eu:{Italy:[3,5,7],Germany:...}
      self.roster = {'eu' :{},  # Europe
                     'ap' :{},  # Asia-Pacific (= non-Europe)
                     'int':{}}  # for International championships
      self.byID   = {}          # {ID:country,...}

      for track in self.lines:
        country = track['Country']
        ID      = track['Circuit ID']
        self.byID[ID] = country

        for reg in (G.regions[country],'int'):
          _add(country,ID,reg)
    super().read()
    _roster()

    # DEBUG
    # for r,reg in self.roster.items():
    #   print('----- ' + r)
    #   for country,tracks in reg.items():
    #     print('   ' + country + ' : ' + str(tracks))

# functions for multiple files
def readAll():
  def _preCheck(dir  :str ):
    def _error     (errObj:dict,final:bool):
      progress.status(False)
      GF.error(**errObj)
    def _getClass  (key   :str):
      match key:
        case 'champ' : return Championships
        case 'tracks': return Tracks
        case _       : return File
    def _checkFiles(files :dict,key  :str):
      res = []
      for file in files[key].values():
        path  = file.path if key == 'read' else file.writePath
        found = checkFile(path)
        chk1  =     found and key == 'write'
        chk2  = not found and key == 'read'
        if chk1 or chk2: res.append(file)
      if res:
        fList = ['   '+file.name for file in res]
        if key == 'read': errKey = 'noFilesToRead'
        else            : errKey = 'rmFilesToRun'
        _error({'key':errKey,'extra':fList},
               key == 'write')

    progress.stage('preCheck')
    if not osPath.isdir(dir): _error({'key':'argIsNotDir'},False)
    files = {'read':{},'write':{}}
    for key,obj in G.files.items():
      fileObj = _getClass(key)(dir,**obj)
      files['read'][key] = fileObj
      if obj['write']: files['write'][key] = fileObj
    _checkFiles(files,'read')
    _checkFiles(files,'write')
    progress.status(True)
    return files['read']
  files = _preCheck(GF.getArg())
  progress.stage('read')
  for file in files.values(): file.read()
  progress.status(True)
  return files
def checkFile(path:str):  # проверяет наличие файла
  return osPath.isfile(path)

# защита от запуска модуля
if __name__ == '__main__':
  print("This is module, please don't execute.")
  SYSEXIT()
