import os
import argparse
import time

import src.sorter as sorter
import src.pseudonym as pseudonym
import src.build_list as build_list

execution_start = time.time()

__VERSION__ = "1.4.0"
__AUTHOR__ = "Nicholas Toothaker"
__PATH__ = os.getcwd()

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
parser.add_argument('-l','--list', action='store_true')
parser.add_argument('-s','--sort', action='store_true')
parser.add_argument('-u','--unsort', action='store_true')
parser.add_argument('-r','--rename', action='store_true')
parser.add_argument('-v','--version', action='store_true')
parser.add_argument('--type', choices=['image','all','directory'], default=['all'], nargs=1)
parser.add_argument('--mode', choices=['auto','manual','debug'], default=['auto'], nargs=1)
parser.add_argument('--verbose', action='store_true')
parser.add_argument('--src',dest='source', help=SOURCE_HELP)
parser.add_argument('--dst',dest='destination', help=DEST_HELP)
args = parser.parse_args()
 
args.mode = args.mode[0] if args.mode else None
args.type = args.type[0] if args.type else None

### MAIN

_mode = args.mode if args.mode else "auto"
_type = args.type if args.type else "all"
_debug = True if _mode == 'debug' or args.verbose else False
_src = args.source if args.source else __PATH__
_dst = args.destination if args.destination else _src

[print(f"{x}: {vars(args)[x]}") for x in vars(args)] if _debug else None
print(f"\nSource: {_src}\nDestination: {_dst}\nMode: {_mode}\nType: {_type}\nDebug: {_debug}\n") if _debug else None


dlist = build_list.get_list(_src)
im_list = build_list.remove_non_image(dlist,_src)

# subprocess.call("clear", shell=True)
if args.list:
    build_list.make_list(dlist,_src,_type,_debug)
elif args.sort:
    sorter.sort(_src,_dst,im_list,_debug)
elif args.unsort:
    sorter.unsort(_src,_dst,debug=_debug)
elif args.rename:
    sorter = pseudonym.Pseudoname(_src,_dst)
    sorter.rename()
elif args.version:
    print("pyfile ",__VERSION__)
elif args.do_this:        
    build_list.display(im_list,_src)
else:
    print(NO_ARG)

# print program execution time
print("--- Program Execution Time: %.2f seconds ---" % (time.time() - execution_start))