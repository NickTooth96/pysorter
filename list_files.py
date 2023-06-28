# !/usr/bin/python

import os 
import sys


import pandas as pd

# if len(sys.argv) > 2:
#     sys.argv.pop(0)
#     buffer = ""
#     for x in sys.argv:
#         buffer += x
#     sys.argv.insert(buffer, 0)
sys.argv.pop(0)
print(sys.argv)

file_path = sys.argv[0]

for root, dirs, files in os.walk(file_path, topdown=False):
   for name in files:
      print(os.path.join(name))
#    for name in dirs:
#       print(os.path.join(root, name))