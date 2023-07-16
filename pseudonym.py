import datetime
import os
import shutil
from statistics import mean
import sys
import getopt
from PIL import Image


__VERSION__ = "1.3.0"
__AUTHOR__ = "Nicholas Toothaker"
__PATH__ = os.path.dirname(os.path.abspath(__file__))

MONTHS = {  "01":"January","02":"February","03":"March",
            "04":"April","05":"May","06":"June",
            "07":"July","08":"August","09":"September",
            "10":"October","11":"November","12":"December"}

FAILURES = 0

BLACKLIST = ['97TH', 'REGIMENTAL', 'STRING', 'BAND', '-']
GRAYLIST = ['THE', 'A', 'AN','OF','ON','AND','TO']
   
    

class Pseudoname():
    
    source_dir = ""
    dest_dir = ""
    dest_structure = {}
    dir_contents = []

    def __init__(self,source=__PATH__,destination=__PATH__):
        self.source_dir = source
        self.dest_dir = destination
        self.dest_structure = {}
        self.dir_contents = self.get_list()
    
    def get_list(self):
        # buffer = []
        output = []
        buffer = os.listdir(self.source_dir)
        file_count = 0
        for x in buffer:
            if os.path.isfile(os.path.join(self.source_dir,x)):
                output.append(x)
                file_count += 1
        print("Source Directory contains ",file_count,"files.")
        return output
    
    def rename(self):
        for x in self.dir_contents:
            title = ""
            # print(x)
            parsed_x = x.split()
            for i in range(len(parsed_x)-1):
                if parsed_x[i].upper() not in GRAYLIST:
                    parsed_x[i] = parsed_x[i].capitalize()
                if parsed_x[i].upper() not in BLACKLIST and parsed_x[i].find("-") != -1:
                    split = parsed_x[i].split("-") # may change to try to split by each element of blacklist to make config file easier
                    parsed_x.remove(parsed_x[i])
                    for x in split:
                        parsed_x.insert(i,x)
            parsed_x = self.remove(parsed_x)
            for e in parsed_x:
                title += e + " "
            # print(title)
    
    def remove(self,list):
        blacklist = BLACKLIST.copy()
        for i in range(len(list)-1):
            i = 0
            # print(list[i])
            # list[i] = list[i].capitalize()
            for y in blacklist:
                if list[i].upper() == y:
                    blacklist.remove(y)
                    del list[i]
                    break
                else:
                    mp = self.reasonable_match(list[i],y)
                    if mp >= 98 and mp <= 101:
                        print(list[i],y)
                        blacklist.remove(y)
                        print("Removing:",list[i],"-",mp,"match with",y)
                        del list[i]
        return list

    def reasonable_match(self,key,remove):
        i = 0
        match_percent =  0
        total_percent = 0
        key = key.upper()
        percent_list = []
        length_percent = len(key) / len(remove)
        shortest = len(key)
        longest = len(remove)
        for x in remove:
            all_not_alpha = 0
            if x.isalpha():
                all_not_alpha += 1
        if all_not_alpha == 0:
            return 0.0
        if len(remove) < shortest:
            shortest = len(remove)
            longest = len(key)
        else:
            print(remove.ljust(longest, '*'))
            print(key,remove)
            for i in range(longest):
                if key[i] == remove[i]:
                    match_percent += 1
                    print(match_percent)
        match_percent = match_percent / longest
        percent_list.append(match_percent)
        percent_list.append(length_percent)
        total_percent = round(mean(percent_list)*100,2)
        return total_percent

        



# fs = Pseudoname()
# fs.reasonable_match("regimentall","REGIMENTAL")

        
        
            