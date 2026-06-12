from sys import exit as SYSEXIT

msg = {
  'errors':{
    'addArg'     :'$red$Добавьте путь к каталогу, в котором лежат ОРИГИНАЛЬНЫЕ файлы базы данных.$rst$',
    'argIsNotDir':'$red$Это не каталог$rst$',
    }
  }

# защита от запуска модуля
if __name__ == '__main__':
  print("This is module, please don't execute.")
  SYSEXIT()
