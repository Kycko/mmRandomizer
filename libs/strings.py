from sys     import exit as SYSEXIT
from globals import stageLen

separator = '-' * stageLen

status = {True:'$grn$OK$rst$',False:'$red$FAILED$rst$'}

msg = {
  'errors':{
    'addArg'       :"$red$Add the path to the directory with ORIGINAL game's database files.$rst$",
    'argIsNotDir'  :'$red$This path is not a directory$rst$',
    'noFilesToRead':'$red$These files were not found in the defined directory$rst$:',
    'rmFilesToRun' :'$red$(Re)move these files from the current directory to launch$rst$:',
    'teamsCount'   :'$red$You have defined the wrong number of teams for WMC + APC + ERS$rst$',
    'teamsCount30' :'$red$Should be 30 in total$rst$',
    'teamsCount12' :'$red$No one championship can have more than 12 teams$rst$'
    },
  'info'  :{
    'final'        :['$grn$Finished SUCCESSFULLY$rst$',
                     'Files created:']
    },
  'stages':{  # ttl = title
    'ttlPre'       :'$ylw$------- Prepare$rst$',
    'preCheck'     :'Pre-checks',
    'read'         :'Reading the game database',

    'ttlGen'       :'$ylw$------- Generation & other changes$rst$',
    'genTracks'    :'Generating the calendars',
    'genRules'     :'Generating the championships rules',
    'moveTeams'    :'Changing the number of teams per championship',

    'ttlFin'       :'$ylw$------- Finalize$rst$',
    'write'        :'Writing the resulting files'
    }
  }

# защита от запуска модуля
if __name__ == '__main__':
  print("This is module, please don't execute.")
  SYSEXIT()
