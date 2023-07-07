import datetime
import os
import shutil
import sys
import getopt
import time
# import toml
from PIL import Image


__VERSION__ = "1.3.0"
__AUTHOR__ = "Nicholas Toothaker"

MONTHS = {  "01":"January","02":"February","03":"March",
            "04":"April","05":"May","06":"June",
            "07":"July","08":"August","09":"September",
            "10":"October","11":"November","12":"December"}

FAILURES = 0

no_arg = "ERROR: No arguments given"
versionMSG = "Version " + __VERSION__ + " by " + __AUTHOR__

options = "u:hs:l:v"
long_options = ["Help", "Sort", "List"]

### Class 

class Pysorter:

    source_dir = ""
    dest_dir = ""
    dest_structure = {}
    dir_contents = []

    def __init__(self,**kwargs):
        try:self.source_dir = kwargs['source_dir']
        except: pass        
        try:self.dest_dir = kwargs['dest_dir']
        except: pass
        self.dest_structure = {}
        try:self.dir_contents = self.get_list()
        except: pass
    
    def get_list(self):
        buffer = []
        output = []
        buffer = os.listdir(self.source_dir)
        for x in buffer:
            if os.path.isfile(os.path.join(self.source_dir,x)):
                output.append(x)
        return output
    
    def sort(self):
        years = []

        # print("Contents:",self.dir_contents)

        for x in self.dir_contents: 

            try:
                im = Image.open(os.path.join(self.source_dir,x))
                exif = im.getexif()
                t = exif[306]
                

                try:
                    im = Image.open(os.path.join(self.source_dir,x))
                    exif = im.getexif()
                    t = exif[306]  
                    success = True      
                except:
                    success = False
                if success:
                    try:
                        buffer = datetime.datetime.strptime(t,'%Y:%m:%d %H:%M:%S')            
                        t = datetime.datetime.timestamp(buffer)                
                    except:
                        t = t 
                        FAILURES += 1        
            except:
                t = os.stat(os.path.join(self.source_dir,x)).st_mtime

            month = datetime.datetime.fromtimestamp(t).strftime("%m")
            year = datetime.datetime.fromtimestamp(t).strftime("%y")
            name = "20" + year    
            dest = os.path.join(self.dest_dir,name)
            if os.path.exists(dest):
                final_dest = os.path.join(dest,MONTHS[month])
                if os.path.exists(final_dest):
                    shutil.move(os.path.join(self.source_dir,x),final_dest)
                else:
                    os.makedirs(os.path.join(dest,MONTHS[month]))
                    shutil.move(os.path.join(self.source_dir,x),final_dest)
            else:
                os.makedirs(os.path.join(dest,MONTHS[month]))
                shutil.move(os.path.join(self.source_dir,x),os.path.join(dest,MONTHS[month]))

    def unsort(self):
        file_count = 0
        buffer = os.listdir(self.source_dir)
       
        for x in buffer:   
            path_0 = os.path.join(self.source_dir,x)          
            if os.path.isdir(path_0) and "20" in x:
                buffer = os.listdir(path_0)   

                for x in buffer: 
                    path_1 = os.path.join(path_0,x) 
                    if os.path.isdir(path_1) and x in MONTHS.values():
                        buffer = os.listdir(path_1) 

                        for x in buffer:
                            path_2 = os.path.join(path_1,x)
                            if os.path.isfile(path_2):
                                file_count += 1
                                shutil.move(path_2,self.source_dir)
                                
                            else:
                                print("NONFILE FOUND")
                # print(path_0)
                shutil.rmtree(path_0)

            
                








### MAIN

arglist = sys.argv[1:]

sys.argv.pop(0)
# print(sys.argv)

if len(arglist) < 1:
    # print(no_arg)
    raise SystemExit

try: 
    arguments, values = getopt.getopt(arglist, options, long_options)
    for currentArgument, currentValue in arguments:
        if currentArgument in ("-s", "--sort"):
            sorter = Pysorter(source_dir=arglist[1], dest_dir=arglist[2])
            sorter.sort()
            print("Has run",FAILURES)
        elif currentArgument in ("-l","--list"):
            print("List")
            sorter = Pysorter(source_dir=arglist[1], dest_dir=None)
            print(sorter.source_dir)
            print(sorter.dir_contents)
        elif currentArgument in ("-u","unsort"):
            sorter = Pysorter(source_dir=arglist[1])
            sorter.unsort()
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