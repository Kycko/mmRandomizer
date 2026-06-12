from sys import exit as SYSEXIT

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

# защита от запуска модуля
if __name__ == '__main__':
  print  ("This is module, please don't execute.")
  SYSEXIT()
