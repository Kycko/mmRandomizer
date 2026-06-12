from sys import exit as SYSEXIT

separator = '-'*25

msg = {
  'errors':{
    'addArg'       :'$red$Добавьте путь к каталогу, в котором лежат ОРИГИНАЛЬНЫЕ файлы базы данных.$rst$',
    'argIsNotDir'  :'$red$Это не каталог$rst$',
    'noFilesToRead':'$red$Эти файлы не найдены в указанном каталоге$rst$:',
    'rmFilesToRun' :'$red$Для запуска уберите эти файлы из текущего каталога$rst$:'
    }
  }

# защита от запуска модуля
if __name__ == '__main__':
  print("This is module, please don't execute.")
  SYSEXIT()
