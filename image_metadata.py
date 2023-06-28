import datetime
import os
from time import strptime
import time
from PIL import Image 
from PIL.ExifTags import TAGS

# print(TAGS)
img = "img_test.jpg"
file = "test.txt"

f = open(os.path.join(os.getcwd(),file))
# i = Image.open(os.path.join(os.getcwd(),"filespy",img))
# print(os.path.isdir(path))
# print(os.path.isfile(img))

# image = Image.open(img)
# print(type(image))
print(f.read())
# print(i.read())

dirlist = os.listdir(os.path.join(os.getcwd()))
print(dirlist)
for element in dirlist:
    print(os.path.getctime(element))
    t = os.path.getctime(element)
    month = datetime.datetime.fromtimestamp(t).strftime("%m")
    year = datetime.datetime.fromtimestamp(t).strftime("%y")