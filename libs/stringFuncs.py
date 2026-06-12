from sys     import exit   as SYSEXIT
from globals import colors as Gcolors

# преобразование
def cutColors(string:str):  # вырезает из строки все цвета
  # можно использовать для правильного подсчёта длины строки
  for clr in Gcolors.values(): string = string.replace(clr['rpl'],'')
  return string

# защита от запуска модуля
if __name__ == '__main__':
  print("This is module, please don't execute.")
  SYSEXIT()
