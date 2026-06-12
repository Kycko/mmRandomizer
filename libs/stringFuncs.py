from   sys import exit as SYSEXIT
import globals         as G
import strings         as S

# для использования в этом модуле оригинального принта
origPrint = print

# обычный print(), но с расцветкой
def print(keys:list): # keys = список[] ключей из S.msg{}
  final = S.msg
  for key in keys: final = final[key]
  for clr,code in G.colors.items():
    final = final.replace('$'+clr+'$',code)
  origPrint(final)

# защита от запуска модуля
if __name__ == '__main__':
  origPrint("This is module, please don't execute.")
  SYSEXIT()
