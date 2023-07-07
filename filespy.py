import datetime
import os
from inspect import currentframe, getframeinfo
import sys

from PIL import Image

failures = 0
success = False

fp = os.path.dirname(os.path.abspath(__file__))
print(fp)
fpath = os.path.join(fp,'target')
print(fpath)
for x in os.listdir(fpath):
    if os.path.isfile(os.path.join(fpath,x)):
        try:
            im = Image.open(os.path.join(fpath,x))
            exif = im.getexif()
            t = exif[306]  
            success = True      
        except:
            t = os.stat(os.path.join(fpath,x)).st_mtime
            success = False
        if success:
            try:
                buffer = datetime.datetime.strptime(t,'%Y:%m:%d %H:%M:%S')            
                t = datetime.datetime.timestamp(buffer)                
            except:
                t = t
            # print(final)
        try:
            month = datetime.datetime.fromtimestamp(t).strftime("%m")
            year = datetime.datetime.fromtimestamp(t).strftime("%y")
            name = "20" + year  
            print(month,name)
        except:
            print(t)
        # print("END",t)

