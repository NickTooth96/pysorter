import datetime
import os
from inspect import currentframe, getframeinfo
import sys

frameinfo = getframeinfo(currentframe())
path = sys.argv[1:]
print(path)
t = os.stat(path[0]).st_mtime
print(t)
month = datetime.datetime.fromtimestamp(t).strftime("%m")
year = datetime.datetime.fromtimestamp(t).strftime("%y")
print("\t",month,"/",year,"\n")
