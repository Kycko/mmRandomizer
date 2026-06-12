import sys
import stringFuncs as SF

def error (key:str):  # key = ключ из S.msg['errors']
  SF.print(['errors',key]); sys.exit(1)
def getArg():
  try   : return sys.argv[1]
  except: error('addArg')

# защита от запуска модуля
if __name__ == '__main__':
  print("This is module, please don't execute.")
  sys.exit()
