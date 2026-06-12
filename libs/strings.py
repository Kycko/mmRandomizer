from sys     import exit as SYSEXIT
from globals import stageLen

separator = '-' * stageLen

status = {True:'$grn$OK$rst$',False:'$red$FAILED$rst$'}

msg = {
  'errors':{
    'addArg'       :'$red$Добавьте путь к каталогу, в котором лежат ОРИГИНАЛЬНЫЕ файлы базы данных.$rst$',
    'argIsNotDir'  :'$red$Это не каталог$rst$',
    'noFilesToRead':'$red$Эти файлы не найдены в указанном каталоге$rst$:',
    'rmFilesToRun' :'$red$Для запуска уберите эти файлы из текущего каталога$rst$:'
    },
  'stages':{
    'preCheck'     :'Предварительные проверки',
    'read'         :'Читаем базу игры'
    }
  }

# защита от запуска модуля
if __name__ == '__main__':
  print("This is module, please don't execute.")
  SYSEXIT()
