from   sys import exit as SYSEXIT
from   os  import path as osPath
import globalFuncs     as GF

def readAll():
  dir = GF.getArg()
  if not osPath.isdir(dir): GF.error('argIsNotDir')

# защита от запуска модуля
if __name__ == '__main__':
  print("This is module, please don't execute.")
  SYSEXIT()
