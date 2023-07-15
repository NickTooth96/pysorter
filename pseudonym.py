import datetime
import os
import shutil
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
        # print(self.source_dir)
        for x in self.dir_contents:
            # print(type(x))
            x = x.split()
            self.remove(x)
            # print(type(x),x)
    
    def remove(self,list):
        out = list
        print("\nProcessing:",list)
        for e in list:
            i = 0
            print("\tHERE")
            for i in range(len(BLACKLIST)):
                print("CHECKING:",e,i,BLACKLIST[i])
                if e.upper() == BLACKLIST[i]:
                    print("\tMATCH FOUND:",e,BLACKLIST[i])
                    out.remove(e)
                    # print("!!! ABOUT TO BREAK !!!",i)
                    # break
                else:
                    i += 1
            print(list)
        print("FINAL:",list)
            






            # print("\tChecking [",e.upper(),"] against ",BLACKLIST)
            # element = e
            # e = e.upper()
            # # print(element)
            # for word in BLACKLIST:
            #     word = word.upper()
            #     # print(">>>",word)
            #     if e.upper() == word.upper():
            #         print("\tMATCH FOUND",e,word)
            #         # list.remove(element)
            #         print("\t\t\t",out)
            #         out.remove(word)
            #     print(list)






            # if e.upper() in BLACKLIST:
            #     print("\t\t",e.upper())
            #     list.remove(e)
            #     print("\t\t\tRemoving:",e)
            # else:
            #     print("\t\t[",e.upper(),"] not found in",BLACKLIST)
        print("\nProcessed:",out)
