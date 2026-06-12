import random
from   copy    import deepcopy
from   os      import path as osPath
from   sys     import exit as SYSEXIT
import globalFuncs         as GF
import globals             as G
import output              as O
import strings             as S

# shared class
class File():
  def __init__(self,dir:str,file:str,write:bool):
    self.name       = file
    self.path       = osPath.join(dir ,file)
    self.writePath  = osPath.join('./',file)
    self.finalWrite = write # будем ли записывать итоги
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
  def write   (self):
    def _write(lines:list):
      with open(self.writePath,'w',encoding='utf-8') as f:
        for line in lines: f.write(f'{line}\n')
    final = [','.join(self.titles)]
    for line in self.lines:
      joined = ','.join(list(line.values()))
      final.append(joined)
    _write(final)

# per-file classes
class Championships(File):
  def read     (self):
    super().read()
    self.db = {}
    for line in self.lines:
      self.db[line['Acronym']] = {'startWeek':int(line['Season Start']),
                                  'endWeek'  :int(line['Season End'])}
    # DEBUG
    # for champ,data in self.db.items():
    #   print(champ.ljust(5) + ' : ' + str(data))
  def genTracks(self,db:Tracks):
    def _getCounts ():
      # IEC-B MUST have the same tracks
      final = {'WMC'  :16,
               'ERS'  :random.randint(8,11),
               'GTCS' :random.randint(8,11),
               'IEC-A':random.randint(8,10)}
      # APS
      add = random.randint(1,2) if final['ERS'] < 10 else 1
      final['APS'] = final['ERS'] + add
      # IGTC
      add = random.randint(1,3) if final['GTCS'] < 11 else 2
      final['IGTC'] = final['GTCS'] + add
      return final
    def _crossCheck(countryByID:dict,tracks:dict):
      # check if the same countries used at the same time
      def _check(countryByID:dict,tracks:dict):
        def _collect(countryByID:dict,tracks:dict):
          final = {}  # {week:countries[]}
          for champ,trackList in tracks.items():
            racesCount = len(trackList)
            startWeek  = self.db[champ]['startWeek']
            endWeek    = self.db[champ]['endWeek']
            for index,ID in enumerate(trackList):
              country = countryByID[ID]
              week    = startWeek
              if racesCount > 1:
                week += round((index / (racesCount-1)) * (endWeek-startWeek))
              if week not in final: final[week] = []
              final[week].append(country)
          return final
        year = _collect(countryByID,tracks)
        for week,countries in year.items():
          # don't allow doubles in one week
          if len(countries) != len(set(countries)): return False
          # don't allow doubles in two weeks
          next = week + 1
          if     next    in year.keys():
            for  country in countries:
              if country in year[next]: return False
        return True
      if not tracks: return False
      return _check(countryByID,tracks)
    def _getTracks (dbroster:dict,champ:str,count:int):
      def _getAllowed(main:list,added:list,halfnum:int):
        # main  = страны главного ростера; added = countries
        def _trim(added:list,half:int):
          # обрезает added для проверки стран
          # не допускает одну страну в рамках одной половины сезона
          # + чтобы между гонками в одной стране было минимум две других
          lenAdded = len(added)
          if   lenAdded < half  : trim = 0
          elif lenAdded > half+1: trim = half
          else                  : trim = lenAdded-2
          return added[trim:]
        final = []
        for  country in main:
          if country not in _trim(added,halfnum): final.append(country)
        return final
      final     = []
      countries = []
      halfnum   = round(count/2)
      doubles   = G.champs[champ]['doubles']
      roster    = deepcopy(dbroster[G.champs[champ]['roster']])

      for i in range(count):
        allowed = _getAllowed(list(roster.keys()),countries,halfnum)
        country = random.choice   (allowed)
        index   = random.randrange(len(roster[country]))
        ID      = roster[country].pop(index)
        if not doubles or not roster[country] or country in countries:
          roster.pop(country)
        countries.append(country)
        final    .append(ID)
      return final
    def _save      (tracks  :dict):
      for line in self.lines:
        line['Locations'] = ';'.join(tracks[line['Acronym']])
    def _debug     (champ   :str,tracks:dict):
      msg  = champ.ljust(5)
      msg += ' {' + str(len(tracks[champ])).ljust(2) + '} '
      msg += str(tracks[champ])
      print(msg)

    O.progress.stage('genTracks')
    tracks  = {}  # to pass through the first 'while'
    rCounts = _getCounts()  # don't reroll it in each while loop
    while not _crossCheck(db.byID,tracks):
      # print(); print('-------------------------') # DEBUG
      tracks = {}
      for champ,count in rCounts.items():
        tracks[champ] = _getTracks(db.roster,champ,count)
        # _debug(champ,tracks)
    tracks['IEC-B'] = tracks['IEC-A'] # должны быть одинаковы!!
    _save(tracks)
    O.progress.status(True)
    # for champ in G.champs.keys(): _debug(champ,tracks)  # DEBUG
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
def checkFile(path:str):  # проверяет наличие файла
  return osPath.isfile(path)
def readAll  ():
  def _preCheck(dir:str):
    def _error     (errObj:dict,final:bool):
      O.progress.status(False)
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

    O.progress.stage('preCheck')
    if not osPath.isdir(dir): _error({'key':'argIsNotDir'},False)
    files = {'read':{},'write':{}}
    for key,obj in G.files.items():
      fileObj = _getClass(key)(dir,**obj)
      files['read'][key] = fileObj
      if obj['write']: files['write'][key] = fileObj
    _checkFiles(files,'read')
    _checkFiles(files,'write')
    O.progress.status(True)
    return files['read']
  files = _preCheck(GF.getArg())
  O.progress.stage('read')
  for file in files.values(): file.read()
  O.progress.status(True)
  return files
def writeAll (files:dict):
  def _print (created:list):
    O.print()
    O.print(S.separator)
    for msg  in S.msg['info']['final']: O.print(msg)
    for file in created               : O.print('   ' + file)

  O.progress.stage('write')
  created = []
  for  file in files.values():
    if file.finalWrite: file.write(); created.append(file.name)
  O.progress.status(True)
  _print(created)

# защита от запуска модуля
if __name__ == '__main__':
  print("This is module, please don't execute.")
  SYSEXIT()
