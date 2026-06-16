from   sys import exit  as SYSEXIT
import globalsGenerator as gen

######### maximum status messages length
stageLen = 48

######### files
# this basic variables should be here, in the globals
# rw = r[ead] / w[rite] / rw (both)
#   write means we will create the NEW file with the generated data
#   read  means we need some data from this original DB file
#   some files we will write, but there's no need to read them
# when adding the new file here CHECK THE DEFINED CLASS
#   in F.readAll()._preCheck()._getClass()
files = {#'assistants':{'file':'Assistants.txt'   ,'rw': 'w'},
         'carParts'  :{'file':'Default Parts.txt','rw':'rw'},
         'champ'     :{'file':'Championships.txt','rw':'rw'},
         'chassis'   :{'file':'Chassis.txt'      ,'rw':'rw'},
         'rules'     :{'file':'Rule Changes.txt' ,'rw':'r' },
         'tracks'    :{'file':'Locations.txt'    ,'rw':'r' }}
# where to write the resulting files (relative to the script path)
writeDirPrefix = 'result_'

######### colors
colors = {'blk':{'code':'\033[30m'},  # black
          'red':{'code':'\033[31m'},  # red
          'grn':{'code':'\033[32m'},  # green
          'ylw':{'code':'\033[33m'},  # yellow
          'blu':{'code':'\033[34m'},  # blue
          'mag':{'code':'\033[35m'},  # magenta
          'cya':{'code':'\033[36m'},  # cyan
          'wht':{'code':'\033[37m'},  # white
          'udl':{'code':'\033[4m' },  # underline
          'bld':{'code':'\033[1m' },  # bold
          'rst':{'code':'\033[0m' }}  # reset all colors
for clr,sub in colors.items(): sub['rpl'] = '$'+clr+'$'
# red bold is better than just red
colors['red']['code'] = colors['bld']['code'] + colors['red']['code']

######### countries/regions
# eu = Europe / ap = Asia-Pasific (= non-Europe)
regions = {'Australia'         :'ap',
           'Belgium'           :'eu',
           'Brazil'            :'ap',
           'Canada'            :'ap',
           'China'             :'ap',
           'Germany'           :'eu',
           'Italy'             :'eu',
           'Japan'             :'ap',
           'Portugal'          :'eu',
           'Qatar'             :'ap',
           'RussianFederation' :'eu',
           'Singapore'         :'ap',
           'SouthAfrica'       :'ap',
           'UK'                :'eu',
           'UnitedArabEmirates':'ap',
           'UnitedStates'      :'ap'}

# championships
champList = [abbr for abbr in gen.champs.keys()]

if __name__ == '__main__':
  print  ("This is module, please don't execute.")
  SYSEXIT()
