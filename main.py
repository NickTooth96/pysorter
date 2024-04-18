import datetime
import os
import shutil
import subprocess
import sys
import argparse
import time
from PIL import Image

import src.sorter as sorter
import src.pseudonym as pseudonym
import src.build_list as build_list

execution_start = time.time()

__VERSION__ = "1.4.0"
__AUTHOR__ = "Nicholas Toothaker"
__PATH__ = os.getcwd()

sys.path.append(os.path.join(__PATH__,"src"))

NO_ARG = "\nERROR: No Valid Argument\nType 'pyfile.py --help' for valid arguments\n"
SOURCE_HELP = "Source directory to sort or rename. Defaults to root directory of module."
DEST_HELP = """Destination directory for sorted files. Not used for Psudonym. Defaults to root directory of module."
If source is given with no destination then destination is set to source."""
MONTHS = {  "01":"January","02":"February","03":"March",
            "04":"April","05":"May","06":"June",
            "07":"July","08":"August","09":"September",
            "10":"October","11":"November","12":"December"}

parser = argparse.ArgumentParser(
                    prog='Pyfile',
                    description='Sorts image files by year and month.',
                    epilog='By Nicholas Toothaker')

parser.add_argument('-d','--do_this', action='store_true')

# add -l, --list with required argument to select between all and image only
parser.add_argument('-l','--list', metavar=['all','image'], nargs=1)


parser.add_argument('-s','--sort', metavar=['in-place','to-dst'], nargs=1)
parser.add_argument('-u','--unsort', action='store_true')
parser.add_argument('-r','--rename', action='store_true')
parser.add_argument('-v','--version', action='store_true')
parser.add_argument('--src',dest='source', help=SOURCE_HELP)
parser.add_argument('--dst',dest='destination', help=DEST_HELP)
args = parser.parse_args()

if args.source and not args.destination:
    args.destination = args.source
elif not args.source and args.destination:
    args.source = args.destination 


### MAIN


# for arg in vars(args):
#     print(arg, getattr(args, arg))
    
if args.source:
    src = args.source
else:
    src = __PATH__
if args.destination:
    dest = args.destination
else:
    dest = args.source

dir_list = build_list.get_list(src)
im_list = build_list.remove_non_image(dir_list,src)

# subprocess.call("clear", shell=True)
if args.list:

    if args.list[0] == "image":
        build_list.display_image(im_list,src)
    elif args.list[0] == "all":
        d_list = build_list.get_list(src)
        build_list.display(d_list,src)

elif args.sort:
    if args.sort[0] == "in-place":
        sorter.sort(src,src,im_list)
    elif args.sort[0] == "to-dst":
        sorter.sort(src,dest,im_list)

elif args.unsort:
    sorter.unsort(src,dest)
elif args.rename:
    sorter = pseudonym.Pseudoname(args.source,args.destination)
    sorter.rename()
elif args.version:
    print("pyfile ",__VERSION__)
elif args.do_this:        
    build_list.display(im_list,src)
else:
    print(NO_ARG)

# print program execution time
print("--- Program Execution Time: %.2f seconds ---" % (time.time() - execution_start))