from sys import exit as SYSEXIT

# эти базовые вещи должны быть здесь, в globals
# write = True для файлов, которые будем изменять
#   остальные просто читаем для получения доп. данных
files = {'champ' :{'file':'Championships.txt','write':True},
         'tracks':{'file':'Locations.txt'    ,'write':False}}

colors = {'blk':'\033[30m', # black
          'red':'\033[31m', # red
          'grn':'\033[32m', # green
          'ylw':'\033[33m', # yellow
          'blu':'\033[34m', # blue
          'mag':'\033[35m', # magenta
          'cya':'\033[36m', # cyan
          'wht':'\033[37m', # white
          'udl':'\033[4m',  # underline
          'bld':'\033[1m',  # bold
          'rst':'\033[0m'}  # reset all colors

# защита от запуска модуля
if __name__ == '__main__':
  print  ("This is module, please don't execute.")
  SYSEXIT()
