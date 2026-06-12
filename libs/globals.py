from sys import exit as SYSEXIT

# максимальная длина сообщений, показывающих прогресс (stages)
stageLen = 35

# эти базовые вещи должны быть здесь, в globals
# write = True для файлов, которые будем изменять
#   остальные просто читаем для получения доп. данных
files = {'champ' :{'file':'Championships.txt','write':True},
         'tracks':{'file':'Locations.txt'    ,'write':False}}

colors = {'blk':{'code':'\033[30m'},  # black
          'red':{'code':'\033[31m'},  # red
          'grn':{'code':'\033[32m'},  # green
          'ylw':{'code':'\033[33m'},  # yellow
          'blu':{'code':'\033[34m'},  # blue
          'mag':{'code':'\033[35m'},  # magenta
          'cya':{'code':'\033[36m'},  # cyan
          'wht':{'code':'\033[37m'},  # white
          'udl':{'code':'\033[4m' },  # underline
          'bld':{'code':'\033[1m' },  # bold
          'rst':{'code':'\033[0m' }}  # reset all colors
for clr,sub in colors.items(): sub['rpl'] = '$'+clr+'$'
# красный bold выглядит лучше
colors['red']['code'] = colors['bld']['code'] + colors['red']['code']

# eu = Europe / ap = Asia-Pasific (= non-Europe)
regions = {'Australia'         :'ap',
           'Belgium'           :'eu',
           'Brazil'            :'ap',
           'Canada'            :'ap',
           'China'             :'ap',
           'Germany'           :'eu',
           'Italy'             :'eu',
           'Japan'             :'ap',
           'Portugal'          :'eu',
           'Qatar'             :'ap',
           'RussianFederation' :'eu',
           'Singapore'         :'ap',
           'SouthAfrica'       :'ap',
           'UK'                :'eu',
           'UnitedArabEmirates':'ap',
           'UnitedStates'      :'ap'}

# 'doubles' defines if the championship can have the same country twice
# IEC-B == IEC-A
champs = {'WMC'  :{'roster':'int','doubles':False},
          'APS'  :{'roster':'ap' ,'doubles':True },
          'ERS'  :{'roster':'eu' ,'doubles':True },
          'IGTC' :{'roster':'int','doubles':False},
          'GTCS' :{'roster':'int','doubles':True },
          'IEC-A':{'roster':'int','doubles':False}}

# защита от запуска модуля
if __name__ == '__main__':
  print  ("This is module, please don't execute.")
  SYSEXIT()
