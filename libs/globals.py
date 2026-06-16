from   sys import exit  as SYSEXIT
import globalsGenerator as gen

######### максимальная длина сообщений, показывающих прогресс (stages)
stageLen = 48

# эти базовые вещи должны быть здесь, в globals
# write = True для файлов, которые будем изменять
#   остальные просто читаем для получения доп. данных
# ПРИ ДОБАВЛЕНИИ ФАЙЛОВ ОБЯЗАТЕЛЬНО ДОБАВИТЬ В F.readAll()._preCheck()._getClass()
files = {'carParts':{'file':'Default Parts.txt','write':True},
         'champ'   :{'file':'Championships.txt','write':True},
         'chassis' :{'file':'Chassis.txt'      ,'write':True},
         'rules'   :{'file':'Rule Changes.txt' ,'write':False},
         'tracks'  :{'file':'Locations.txt'    ,'write':False}}

######### цвета
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

######### страны/регионы
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

# чемпионаты
champList = [abbr for abbr in gen.champs.keys()]

# защита от запуска модуля
if __name__ == '__main__':
  print  ("This is module, please don't execute.")
  SYSEXIT()
