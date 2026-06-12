from   os      import path  as osPath
from   sys     import exit  as SYSEXIT
import globalFuncs          as GF
from   globals import files as Gfiles
from   output  import progress

# shared class
class File():
  def __init__(self,dir:str,file:str,write:bool):
    self.name      = file
    self.path      = osPath.join(dir ,file)
    self.writePath = osPath.join('./',file)
    self.write     = write

# per-file classes
class Championships(File): pass
class Tracks       (File): pass

# functions for multiple files
def readAll():
  def _preCheck(dir:str):
    def _error     (errObj:dict,final:bool):
      progress.status(False)
      GF.error(**errObj)

    def _checkFiles(files :dict,key  :str):
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

    progress.stage('preCheck')
    if not osPath.isdir(dir): _error({'key':'argIsNotDir'},False)
    files = {'read':{},'write':{}}
    for key,obj in Gfiles.items():
      fileObj = File(dir,**obj)
      files['read'][key] = fileObj
      if obj['write']: files['write'][key] = fileObj
    _checkFiles(files,'read')
    _checkFiles(files,'write')
    progress.status(True)
    return files['read']
  dir = GF.getArg()
  _preCheck(dir)
def checkFile(path:str):  # проверяет наличие файла
  return osPath.isfile(path)

# защита от запуска модуля
if __name__ == '__main__':
  print("This is module, please don't execute.")
  SYSEXIT()
