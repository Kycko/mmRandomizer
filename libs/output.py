from   sys import exit as SYSEXIT
import globals         as G
import strings         as S

# для использования в этом модуле оригинального принта
origPrint = print

# обычный print(), но с расцветкой
def print     (obj):
  # obj может быть ЛИБО строкой, ЛИБО списком[]
  # список[] = список ключей из S.msg{}
  if type(obj) == list:
    final = S.msg
    for key in obj: final = final[key]
  else: final = obj

  for clr in G.colors.values():
    final = final.replace(clr['rpl'],clr['code'])

  origPrint(final)
def error     (key:str,extra=[]):
  # key = ключ из S.msg['errors']; extra = список доп. строк
  print(S.separator)
  print(['errors',key])
  for string in extra: print(string)

# защита от запуска модуля
if __name__ == '__main__':
  print("This is module, please don't execute.")
  SYSEXIT()
