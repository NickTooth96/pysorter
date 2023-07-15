import datetime
import os
import shutil
import sys
import getopt
import time
from PIL import Image

import sorter

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
    optlist, args = getopt.getopt(sys.argv[1:], 'su', ['origin=', 'destination=','sort', 'unsort'])
except getopt.GetoptError as err:
    # print help information and exit:
    print("This is a fail")
    print(err)  # will print something like "option -a not recognized"
    sys.exit(2)

for o, a in optlist:
    if o in ("-o","--origin"):
        origin = a
    if o in ("-d","--destination"):
        destination = a
    if o in ("-s","--sort"):
        pass
    if o in ("-u","--unsort"):
        pass

for o, a in optlist:
    print("Loop Second:",o,a)
    if o in ("-s","--sort"):
        fs = sorter.Sorter(origin,destination)
        fs.sort()
    elif o in ("-u","--unsort"):
        fs = sorter.Sorter(origin,destination)
        fs.unsort()
    elif o in ("-o","--origin"):
        pass
    elif o in ("-d","--destination"):
        pass
    else:
        assert False, "unhandled option"


### Print Execution Time

print("--- Program Execution Time: %.2f seconds ---" % (time.time() - execution_start))