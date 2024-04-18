import datetime
import os
import shutil
import sys
import getopt
from PIL import Image

__AUTHOR__ = "Nicholas Toothaker"
__PATH__ = os.getcwd()

FAILURES = 0
MONTHS = {  "01":"January","02":"February","03":"March",
            "04":"April","05":"May","06":"June",
            "07":"July","08":"August","09":"September",
            "10":"October","11":"November","12":"December"}

source_dir = ""
dest_dir = ""
dest_structure = {}
dir_contents = []

def sort(src,dest,dir_list,debug=False):
    years = []
    im = ""
    to_from = {}
    new_dir = {}

    for x in dir_list: 
        im = Image.open(os.path.join(src,x))
        exif = im.getexif()
        try:
            
            temp = exif[306]
            t = datetime.datetime.strptime(temp,"%Y:%m:%d %H:%M:%S").timestamp()
        except:
            t = os.stat(os.path.join(src,x)).st_mtime 

        month = datetime.datetime.fromtimestamp(t).strftime("%m")
        year = datetime.datetime.fromtimestamp(t).strftime("%y")
        name = "20" + year  
        month_name = f"{month} - {MONTHS[month]}"  
        dest_dir = os.path.join(dest,name)
        final_dest = os.path.join(dest_dir,month_name)

        if not os.path.exists(final_dest) and not os.path.exists(os.path.join(dest,month_name)):
            if debug:
                new_dir[final_dest] = False
            else:       
                new_dir[final_dest] = True    
                os.makedirs(final_dest)
        

        to_from[os.path.join(src,x)] = os.path.join(final_dest,x)
    if debug:
        print("--- NEW DIRECTORIES ---")
        for x in new_dir:
            print(f"CREATING New Directory:\t{x}")
        print("--- MOVING FILES ---")
    for k,v in to_from.items():
        if debug:
            print(f"MOVING: {k} \nTO:\t{v}")
        else:
            move(k,v)


def unsort(src,dst,files={},dirs=[],debug=False):

    print(f"\n !!! Running unsort() in DEBUG mode with \nSRC: {src} \nDST: {dst}\nFFILES: {files}\nDIRECTORIES: {dirs}\n") if debug else None

    buffer = os.listdir(src)
    dirs = []
    
    for x in buffer:
        if os.path.isfile(os.path.join(src,x)):
            if debug:
                print(f"MOVING: {x} \nTO:\t{os.path.join(dst,x)}")
            else:
                move(os.path.join(src,x),os.path.join(dst,x))
        else:
            dirs.append(os.path.join(src,x))
            unsort(os.path.join(src,x),dst,files,dirs,debug)

    for x in dirs:
        if debug:
            print(f"REMOVING: {x}")
        else:
            try:
                os.rmdir(x)
            except:
                print("FAILED TO REMOVE:",x)



def move(src,dst):
    try:
        shutil.move(src,dst)
    except:
        print("FAILED TO MOVE:",src, "->",dst)
