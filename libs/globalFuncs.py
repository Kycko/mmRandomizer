import sys
from   output import error as Oerror

def error (key:str,extra=[]):
  # key = ключ из S.msg['errors']; extra = список доп. строк
  Oerror(key,extra); sys.exit(1)
def getArg():
  try   : return sys.argv[1]
  except: error('addArg')

# защита от запуска модуля
if __name__ == '__main__':
  print("This is module, please don't execute.")
  sys.exit()
