import random
import os
from   copy    import deepcopy
from   csv     import DictReader
from   sys     import exit as SYSEXIT
import globalFuncs         as GF
import globals             as G
import listFuncs           as LF
import output              as O
import stringFuncs         as SF
import strings             as S

# shared classes
class File  ():
  def __init__(self,dir:str,writePath:str,file:str,rw:str):
    self.name       = file
    self.path       = os.path.join(dir,file)
    self.writePath  = os.path.join(writePath,file)
    self.toRead     = 'r' in rw # needs reading the original DB
    self.finalWrite = 'w' in rw # will write the results
  def read    (self):
    with  open(self.path,'r',encoding='utf-8') as f:
      csv = DictReader(f)
      self.titles = csv.fieldnames
      self.lines  = [dict(line) for line in csv]
  def write   (self):
    def _write(lines:list):
      with open(self.writePath,'w',encoding='utf-8') as f:
        for line in lines: f.write(f'{line}\n')
    final = [','.join(self.titles)]
    for line in self.lines:
      joined = ','.join(list(line.values()))
      final.append(joined)
    _write(final)
class People(File):
  pass

# per-file classes
class Championships(File):
  def read     (self):
    super().read()
    self.db = {}
    for line in self.lines:
      self.db[line['Acronym']] = {'startWeek':int(line['Season Start']),
                                  'endWeek'  :int(line['Season End'])}
    # DEBUG
    # print(); print()
    # for champ,data in self.db.items():
    #   print(champ.ljust(5) + ' : ' + str(data))
    # print()
  def save     (self,type:str,data:dict):
    # это не запись в файл, это сохранение в основное хранилище
    for line in self.lines:
      if line['Acronym'] in data.keys():
        final = data[line['Acronym']]
        for i in range(len(final)): final[i] = str(final[i])
        # print(final)  # DEBUG
        line[type] = ';'.join(final)

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
      genDB     = G.gen.champs[champ]['tracks']
      final     = []
      countries = []
      halfnum   = round(count/2)
      doubles   = genDB['doubles']
      roster    = deepcopy(dbroster[genDB['roster']])

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
    self.save('Locations',tracks)
    O.progress.status(True)
    # for champ in G.gen.champs.keys(): _debug(champ,tracks)  # DEBUG
  def genRules (self,db:Rules ):  # описания в 'Rule Changes.txt'
    def _debug (final:dict):
      def _count(rules:list):
        final = []
        for  i,name in G.gen.banParts.items():
          if str(i) in rules: final.append(name)
        return final
      print(); print()
      for champ,rules in final.items():
        ####### общий список правил
        # print(champ.ljust(5) + ' : ' + str([int(val) for val in rules.values()]))
        ####### количество запретов (разработки деталей) в разбивке по чемпионатам
        parts = _count(rules)
        msg   = champ.ljust(5) + ' : '
        msg  += str(len(parts)).rjust(3)
        if parts: msg += ' ' + str(parts)
        print(msg)
      print()
    O.progress.stage('genRules')
    final = {champ:db.gen(champ) for champ in G.champList}

    champ = 'IEC-B' # он копирует большинство правил из IEC-A
    for group,val in final[champ].items():
      if val == G.gen.copySign:
        final[champ][group] = final['IEC-A'][group]

    for champ,rules in final.items(): final[champ] = list(rules.values())
    self.save('Rules',final)
    O.progress.status(True)
    # _debug(final) # внутри есть ДВА РАЗНЫХ ВАРИАНТА
  def moveTeams(self,files:dict):
    # moves the teams to get the final 12-10-8
    def _getDB ():      # collect all the teams by category
      final = {}        # {OW:[2,...,31],GT:[32,...,51]}
      for line in self.lines:
        if 'IEC' not in line['Acronym']:
          series = G.gen.champs[line['Acronym']]['series']
          if series not in final.keys(): final[series] = []
          for team in line['Teams'].split(';'): final[series].append(int(team))

      for teams in final.values(): teams.sort() # additional check
      return final
    O.progress.stage('moveTeams')
    final = {}
    teams = {}
    db    = _getDB()
    for champ,conf in G.gen.champs.items():
      if 'teams' in conf:
        final[champ] = []
        for i in range(conf['teams']):
          teamID = db[conf['series']].pop(0)
          teams[str(teamID)] = str(conf['ID'])
          final[champ].append(teamID)
    files['chassis' ].moveTeams(teams)
    files['carParts'].moveTeams()
    self.save('Teams',final)
    O.progress.status(True)

    # DEBUG
    # for champ,teams in final.items():
    #   print(champ.ljust(5) + ' : ' + str(teams))
class CarParts     (File):
  def read(self):
    super().read()
    # ↓ store the LINKS to THE SAME DICTS from self.lines here
    self.byTeam = {}  # {teamID:[dict_from_self.lines,...],...}
    self.sorter = []  # save the part types for final sorting
    for line in self.lines:
      if line['Part Type'] not in self.sorter:
        self.sorter.append(line['Part Type'])
      teamID = int(line['Team'])
      if teamID not in self.byTeam.keys(): self.byTeam[teamID] = []
      self.byTeam[teamID].append(line)
  def moveTeams(self):
    def _checkErrors(counts:list):
      chkTotal = sum(counts) != 30
      chkParts = any(part > 12 for part in counts)
      if chkTotal or chkParts:
        O.progress.status(False)
        errKey = 'teamsCount30' if chkTotal else 'teamsCount12'
        GF.error('teamsCount',[S.msg['errors'][errKey]])
    def _get        (champ :str,ID:int,cnt:int):
      if champ == 'WMC' and cnt > 9: return G.gen.newCarParts[ID]
      if champ == 'APS':
        lines = self.byTeam[cnt+12]
        for line in lines: line['Team'] = str(ID)
        return lines
      return self.byTeam[ID]
    def _sort       (lines :list):
      self.lines = []
      for    type in self.sorter:
        for  line in lines:
          if line['Part Type'] == type: self.lines.append(line)

    cChamps = ('WMC','APS','ERS')
    counts = [G.gen.champs[champ]['teams'] for champ in cChamps]
    _checkErrors(counts)
    IDs = sorted(list(self.byTeam.keys()))

    collector = []  # can reset here, we will fill it again
    for   c in range(len(cChamps)): # WMC/APC/ERS
      for i in range(counts[c]):
        collector += _get(cChamps[c],IDs.pop(0),i)
    # other championships
    for id in IDs: collector += self.byTeam[id]

    # sort to follow original database structure
    _sort(collector)

    # DEBUG
    # print(); print()
    # for line in self.lines: print(line)
    # print()
class Chassis      (File):
  def moveTeams(self,IDs:dict):
    for line in self.lines:
      if line['Team'] in IDs.keys():
        line['Championship ID'] = IDs[line['Team']]
class Rules        (File):
  def read(self):
    def _groups():
      self.groups = {}
      for rule in self.lines:
        group = rule['Rule Group']
        if group not in self.groups.keys(): self.groups[group] = []
        self.groups[group].append(rule['ID'])
    super().read()
    _groups()

    # DEBUG
    # print(); print()
    # for group,ids in self.groups.items():
    #   print('   ' + group + ' : ' + str(ids))
    # print()
  def gen (self,champ:str):
    def _run(db:dict,champ:str,groups:dict):
      def _get(group:str,IDs:list,champ:str):
        def _weights(group:str,champ:str,IDs:list):
          # подгоняет веса под порядок IDs, поэтому здесь формат ID:вес
          db = G.gen.rules
          if group in db.keys():
            if db[group][champ] == G.gen.copySign: return G.gen.copySign
            return [db[group][champ][id] for id in IDs]
        if   group ==  'RaceLength' and 'IEC' in champ: return None
        elif group in ('TimedRaces','DrivingLimit') and 'IEC' not in champ:
          return None
        elif group.startswith('Spec'):
          end  = SF.checkSubs(group,['GT','GET'],'e')
          bad1 = not end      and SF.checkSubs(champ,['GT','IEC'])
          bad2 = end == 'GT'  and 'GT'  not in champ
          bad3 = end == 'GET' and 'IEC' not in champ
          if bad1 or bad2 or bad3: return None

        w = _weights(group,champ,IDs)
        if   w == G.gen.copySign: return w
        elif w is not None  : return LF.random_byWeight(IDs,w)
      for group,IDs in groups.items():
        if group == 'HybridPower' and not _ERSenabled(db): continue
        res = _get(group,IDs,champ)
        if res is not None: db[group] = res
    def _bansCount (db:dict):
      final = 0
      for num in list(G.gen.banParts.keys()):
        if str(num) in list(db.values()): final += 1
      # print('------- COUNT: ' + str(final)) # DEBUG
      return final
    def _regenParts(db:dict,champ:str):
      # генерирует запреты на разработку заново, если проверка не пройдена
      final = {}
      for  group in db.keys():
        if group.startswith('Spec'): final[group] = self.groups[group]
      _run(db,champ,final)
      return _bansCount(db)
    def _ERSenabled(db:dict):
      ERSkey = 'EnergyRecoverySystem'
      return ERSkey in db.keys() and db[ERSkey] != '76'

    final = {}
    _run(final,champ,self.groups)

    bCount = _bansCount(final)
    while                   bCount > 3: bCount = _regenParts(final,champ)
    while 'GT' in champ and bCount > 2: bCount = _regenParts(final,champ)
    if   _ERSenabled(final) and 'HybridPower' not in final.keys():
      # дождались генерации ERS, теперь можно добавлять
      _run(final,champ,{'HybridPower':self.groups['HybridPower']})

    return final
class Tracks       (File):
  def read(self):
    def _roster():
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
          rg = self.roster[reg]
          if country not in rg.keys(): rg[country] = []
          rg[country].append(ID)
    super().read()
    _roster()

    # DEBUG
    # print(); print()
    # for r,reg in self.roster.items():
    #   print('----- ' + r)
    #   for country,tracks in reg.items():
    #     print('   ' + country + ' : ' + str(tracks))
    # print()

class Assistants(People):
  pass

# functions for multiple files
def checkFile(path:str):  # проверяет наличие файла
  return os.path.isfile(path)
def readAll  ():
  def _preCheck(dir:str):
    def _error       (errObj:dict,final:bool):
      O.progress.status(False)
      print()
      GF.error(**errObj)
    def _findWriteDir():
      for i in range(1000):
        num = str(i)
        # get the '001' format
        for l in range(3-len(num)): num = '0'+num
        dir = './' + G.writeDirPrefix + num
        os.makedirs(dir,exist_ok=True)
        if not os.listdir(dir): return dir
      errObj = {'key'  :'noDirsToWrite0',
                'extra':S.msg['errors']['noDirsToWrite1']}
      _error(errObj,False)
    def _getClass    (key   :str):
      match key:
        case 'assistants': return Assistants
        case 'carParts'  : return CarParts
        case 'champ'     : return Championships
        case 'chassis'   : return Chassis
        case 'rules'     : return Rules
        case 'tracks'    : return Tracks
        case _           : return File
    def _checkFiles  (files :dict,key  :str):
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
    if not os.path.isdir(dir): _error({'key':'argIsNotDir'},False)
    writeDir = _findWriteDir()

    files = {'all':{},'read':{},'write':{}}
    for key,obj in G.files.items():
      fileObj = _getClass(key)(dir,writeDir,**obj)
      files['all' ][key] = fileObj
      if 'r' in obj['rw']: files['read' ][key] = fileObj
      if 'w' in obj['rw']: files['write'][key] = fileObj
    _checkFiles(files,'read')
    _checkFiles(files,'write')
    O.progress.status(True)
    return files['all']
  files = _preCheck(GF.getArg())
  O.progress.stage('read')
  for file in files.values():
    if file.toRead: file.read()
  O.progress.status(True)
  return files
def writeAll (files:dict):
  def _print (created:list):
    O.print(); O.print()
    for msg  in S.msg['info']['final']: O.print(msg)
    for file in sorted(created)       : O.print('   ' + file)
  O.progress.stage('write')
  created = []
  for  file in files.values():
    if file.finalWrite: file.write(); created.append(file.writePath)
  O.progress.status(True)
  _print(created)

# защита от запуска модуля
if __name__ == '__main__':
  print("This is module, please don't execute.")
  SYSEXIT()
