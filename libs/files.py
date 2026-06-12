from   os.path import isdir
from   sys     import exit  as SYSEXIT
import globalFuncs          as GF
from   globals import files as Gfiles

def readAll():
  def _preCheck(dir:str):
    def _checkFiles(files:list,dir:str,resKey:str,errKey:str):
      res = GF.checkFiles(files,dir)[resKey]
      if res: GF.error(errKey,['   '+file for file in res])
    if not isdir(dir): GF.error('argIsNotDir')
    files = {'read':[],'write':[]}
    for obj in Gfiles.values():
      files['read'].append(obj['file'])
      if obj['write']: files['write'].append(obj['file'])
    _checkFiles(files['read' ],dir ,'notFound','noFilesToRead')
    _checkFiles(files['write'],'./','found'   ,'rmFilesToRun')
  dir = GF.getArg()
  _preCheck(dir)

# защита от запуска модуля
if __name__ == '__main__':
  print("This is module, please don't execute.")
  SYSEXIT()
