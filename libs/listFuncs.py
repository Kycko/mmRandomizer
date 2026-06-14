from sys    import exit    as SYSEXIT
from random import choices as rChoices

def random_byWeight(list:list,weights:list):
  # random сам сложит веса для подсчёта вероятностей
  return rChoices(list,weights=weights,k=1)[0]

# защита от запуска модуля
if __name__ == '__main__':
  print("This is module, please don't execute.")
  SYSEXIT()
