import sys
from   os     import path  as osPath
from   output import error as Oerror

def error     (key:str,extra=[]):
  # key = ключ из S.msg['errors']; extra = список доп. строк
  Oerror(key,extra); sys.exit(1)
def getArg    ():
  try   : return sys.argv[1]
  except: error('addArg')
def checkFiles(files:list,dir=''):
  # проверяет наличие файлов в dir
  # в files можно передать полные пути, а dir не передавать
  # возвращает словарь{} с двумя списками[]: найденные и не найденные
  final = {'found':[],'notFound':[]}
  for file in files:
    chkFile = osPath.join(dir,file)
    key = 'found' if osPath.isfile(chkFile) else 'notFound'
    final[key].append(file)
  return final

# защита от запуска модуля
if __name__ == '__main__':
  print("This is module, please don't execute.")
  sys.exit()
