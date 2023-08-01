import datetime
import os
import shutil
import sys
import argparse
import time
from PIL import Image

import sorter
import pseudonym

execution_start = time.time()

__VERSION__ = "1.3.0"
__AUTHOR__ = "Nicholas Toothaker"
__PATH__ = os.path.dirname(os.path.abspath(__file__))

NO_ARG = "ERROR: No arguments given"
MONTHS = {  "01":"January","02":"February","03":"March",
            "04":"April","05":"May","06":"June",
            "07":"July","08":"August","09":"September",
            "10":"October","11":"November","12":"December"}

parser = argparse.ArgumentParser(
                    prog='Pyfile',
                    description='Sorts image files by year and month.',
                    epilog='By Nicholas Toothaker')

parser.add_argument('-s','--sort', action='store_true')
parser.add_argument('-u','--unsort', action='store_true')
parser.add_argument('-r','--rename', action='store_true')
parser.add_argument('-v','--version', action='store_true')
parser.add_argument('--source',dest='source',default=__PATH__)
parser.add_argument('--destination',dest='destination',default=__PATH__)
args = parser.parse_args()

if args.source and not args.destination:
    args.destination = args.source
elif not args.source and args.destination:
    args.source = args.destination 


### MAIN


if args.sort:
    sorter = sorter.Sorter(args.source,args.destination)
    sorter.sort()
elif args.unsort:
    sorter = sorter.Sorter(args.source,args.destination)
    sorter.unsort()
elif args.rename:
    sorter = pseudonym.Pseudoname(args.source,args.destination)
    sorter.rename()
elif args.version:
    print("Pyfile ",__VERSION__)
else:
    print(NO_ARG)

# print program execution time
print("--- Program Execution Time: %.2f seconds ---" % (time.time() - execution_start))