import datetime
import os
import sys
import getopt
import time
import toml


__VERSION__ = "1.3.0"
__AUTHOR__ = "Nicholas Toothaker"

no_arg = "ERROR: No arguments given"
versionMSG = "Version " + __VERSION__ + " by " + __AUTHOR__

options = "a:hs:l:v"
long_options = ["Help", "Sort", "List"]

### Class 

class Pysorter:

    source_dir = ""
    dest_dir = ""
    dest_structure = {}
    dir_contents = []

    def __init__(self,**kwargs):
        self.source_dir = kwargs['source_dir']
        self.dest_dir = kwargs['dest_dir']
        self.dest_structure = {}
        self.dir_contents = self.get_list()
    
    def get_list(self):
        res = []
        for root, dirs, files in os.walk(self.source_dir, topdown=False):
            for name in files:
                res.append(name)
        return res
    
    def target_architecture(self):
        years = []
        months = ["January", "February", "March", 
                  "April", "May", "June", 
                  "July", "August", "September", 
                  "October", "November", "December"]
        res = {}

        # print("Contents:",self.dir_contents)

        for x in self.dir_contents:            
            t = os.stat(os.path.join(self.source_dir,x)).st_mtime
            month = datetime.datetime.fromtimestamp(t).strftime("%m")
            year = datetime.datetime.fromtimestamp(t).strftime("%y")
            # print("\t",month,"/",year,"\n")
            if year not in years:
                years.append(year)
                name = "20" + year
                res[name] = months
        print(res)










arglist = sys.argv[1:]

sys.argv.pop(0)
print(sys.argv)

if len(arglist) < 1:
    print(no_arg)
    raise SystemExit

try: 
    arguments, values = getopt.getopt(arglist, options, long_options)
    for currentArgument, currentValue in arguments:
        if currentArgument in ("-s", "--sort"):
            print("Sort")
        elif currentArgument in ("-l","--list"):
            print("List")
            sorter = Pysorter(source_dir=arglist[1], dest_dir=None)
            print(sorter.source_dir)
            print(sorter.dir_contents)
        elif currentArgument in ("-a"):
            print("Creating Architecture...")
            sorter = Pysorter(source_dir=arglist[1], dest_dir=None)
            sorter.target_architecture()
            print("Has run")
        elif currentArgument in ("-h", "--Help"):
            path = os.path.join(os.path.dirname(__file__), ".help.txt")
            f = open(path,"r")
            for line in f:
                print(line, end="")
        elif currentArgument in ("-v","--version"):
            print(versionMSG)
        else:
            print("Default Launching")
except getopt.error as err:
    print(str(err))