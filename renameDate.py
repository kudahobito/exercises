#! python3
# renameDates.py - Renames filenames with American MM-DD-YYYY date format
# to European DD-MM-YYYY.

import re, os, shutil

# Create a regex that matches files with the American date format.
datePattern = re.compile(r'''(
(.*?)                       # all text before the date
((0|1)?\d)-                 # one or two digits for the month
((0|1|2|3)?\d)-             # one or two digits for the day
((19|20)\d\d)               # four digits for the year
(.*?)$                       # all text after the date
)''', re.VERBOSE)

#list all the filestin the current working directory
dirList = os.listdir('.')

ame_date_file = ''
american_date_format_file = ''

for foldName in dirList:
    #produce a list containing a tuple of the match objects
    mo=datePattern.findall(foldName)
    if len(mo) == 0:
        continue

    else:
        #retrieve the dateparts
        dayPart = mo[0][4]
        monthPart = mo[0][2]
        yearPart = mo[0][6]
        beforePart = mo[0][1]
        afterPart = mo[0][8]
        # fullDate e.g = '01-30-1995'
        fullDate = mo[0][0]

        #the original file name in american date format mm-dd-yyyy e.g = 'sd03-12-2019', '06-11-2000sometexthere'
        ame_date_file = beforePart,fullDate,afterPart

        american_date_format_file = beforePart+monthPart+'-'+ dayPart +'-'+ yearPart+afterPart
        european_date_format_file = beforePart+dayPart+'-'+ monthPart +'-'+ yearPart+afterPart

        # Get the full, absolute file paths.
        absWorkingDir = os.path.abspath('.')
        american_date_format_file = os.path.join(absWorkingDir, american_date_format_file)
        european_date_format_file = os.path.join(absWorkingDir, european_date_format_file)

        # Rename the files.
        print('Renaming "%s" to "%s"...' % (american_date_format_file, european_date_format_file))
        #this code will rename all the matched files
        #shutil.move('american_date_format_file',european_date_format_file)  #uncomment when think everything is ok
