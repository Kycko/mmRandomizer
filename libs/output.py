from   sys import exit as SYSEXIT
import globals         as G
import stringFuncs     as SF
import strings         as S

# для использования в этом модуле оригинального принта
origPrint = print

# обычный print(), но с расцветкой
def print(obj='',newLine=True):
  # obj может быть ЛИБО строкой, ЛИБО списком[]
  # список[] = список ключей из S.msg{}
  # newLine = False оставляет каретку в конце этой же строки
  #   (нужно для вывода статусных сообщений, stages)
  if type(obj) == list:
    final = S.msg
    for key in obj: final = final[key]
  else: final = obj

  for clr in G.colors.values():
    final = final.replace(clr['rpl'],clr['code'])

  params = {'end'  :'\n' if newLine else '',
            'flush':not newLine}
  origPrint(final,**params)
def error(key:str,extra=[]):
  # key = ключ из S.msg['errors']; extra = список доп. строк
  print(S.separator)
  print(['errors',key])
  for string in extra: print(string)

class Progress():
  def stageTitle(self,ttlKey:str): print(['stages',ttlKey])
  def stage     (self,stgKey:str):
    def _align(txt:str):
      length = len(SF.cutColors(txt))
      for i in range(length,G.stageLen): txt += '.'
      return txt
    print(_align(S.msg['stages'][stgKey]),False)
  def status    (self,status:bool,tip=''):
    # для сокращения кода возвращаем этот же статус
    # tip = любой текст, будет выведен в скобках
    final = S.status[status]
    if tip: final += ' (' + tip + ')'
    print(final)
    return status
progress = Progress()

# защита от запуска модуля
if __name__ == '__main__':
  print("This is module, please don't execute.")
  SYSEXIT()
