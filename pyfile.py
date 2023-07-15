import datetime
import os
import shutil
import sys
import getopt
import time
from PIL import Image

import sorter
import pseudonym

execution_start = time.time()


__VERSION__ = "1.3.0"
__AUTHOR__ = "Nicholas Toothaker"
__PATH__ = os.path.dirname(os.path.abspath(__file__))

MONTHS = {  "01":"January","02":"February","03":"March",
            "04":"April","05":"May","06":"June",
            "07":"July","08":"August","09":"September",
            "10":"October","11":"November","12":"December"}

FAILURES = 0

no_arg = "ERROR: No arguments given"
versionMSG = "Version " + __VERSION__ + " by " + __AUTHOR__

### MAIN

try:
    optlist, args = getopt.getopt(sys.argv[1:], 'sup', ['origin=', 'destination=','sort', 'unsort', 'pseudonym'])
except getopt.GetoptError as err:
    # print help information and exit:
    print("This is a fail")
    print(err)  # will print something like "option -a not recognized"
    sys.exit(2)

for o, a in optlist:
    if o in ("-o","--origin"):
        origin = a
    elif o in ("-d","--destination"):
        destination = a
    elif o in ("-s","--sort"):
        run = o
    elif o in ("-u","--unsort"):
        run = o
    elif o in ("-p","--pseudonym"):
        run = o
    else:
        assert False, "unhandled option"

if run in ("-s","--sort"):
    fs = sorter.Sorter(origin,destination)
    fs.sort()
elif run in ("-u","--unsort"):
    fs = sorter.Sorter(origin,destination)
    fs.unsort()
elif run in ("-p","--rename"):
    fs = pseudonym.Pseudoname(origin)
    fs.rename()
else:
    assert False, "unhandled option"


### Print Execution Time

print("--- Program Execution Time: %.2f seconds ---" % (time.time() - execution_start))