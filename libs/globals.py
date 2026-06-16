from   sys import exit  as SYSEXIT
import globalsGenerator as gen

######### maximum status messages length
stageLen = 48

######### files
# this basic variables should be here, in the globals
# write = True means we will write the new file for the user
#   others are here to get all the needed data
# when adding the new file here CHECK THE DEFINED CLASS
#   in F.readAll()._preCheck()._getClass()
files = {'carParts':{'file':'Default Parts.txt','write':True},
         'champ'   :{'file':'Championships.txt','write':True},
         'chassis' :{'file':'Chassis.txt'      ,'write':True},
         'rules'   :{'file':'Rule Changes.txt' ,'write':False},
         'tracks'  :{'file':'Locations.txt'    ,'write':False}}
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
