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

def sort(src,dest,dir_list):
    years = []
    im = ""

    to_from = {}
    FAILURES = 0

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
        dest_dir = os.path.join(dest,name)
        final_dest = os.path.join(dest_dir,MONTHS[month])

        # print(src,final_dest)

        if not os.path.exists(final_dest):
            os.makedirs(final_dest)

        # print("MOVING:",os.path.join(src,x),"to",os.path.join(final_dest,x))
        to_from[os.path.join(src,x)] = os.path.join(final_dest,x)
        # shutil.move(os.path.join(src,x),os.path.join(final_dest,x))
    for k,v in to_from.items():
        move(k,v)


def unsort(src,dst,files={},dirs={}):
    buffer = os.listdir(src)
    dirs = []
    for x in buffer:
        if os.path.isfile(os.path.join(src,x)):
            move(os.path.join(src,x),os.path.join(dst,x))
        else:
            dirs.append(os.path.join(src,x))
            unsort(os.path.join(src,x),dst)
    for x in dirs:
        try:
            os.rmdir(x)
        except:
            print("FAILED TO REMOVE:",x)


def move(src,dst):
    try:
        shutil.move(src,dst)
    except:
        print("FAILED TO MOVE:",src, "->",dst)
