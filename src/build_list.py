import sys
import os
import datetime

from PIL import Image

__PATH__ = os.getcwd()
IGNORE = ['ini','info']
__file__ = "build_list"


def get_list(src=os.getcwd(), debug=False):
    """returns list of all files in directory

    Args:
        src (_type_): _description_

    Returns:
        list: list of all files in current directory (dest)
    """
    print(f"RUNNING {__file__}.{sys._getframe().f_code.co_name} in DEBUG mode") if debug else None
    buffer = []
    output = []
    try:
        buffer = os.listdir(src)
    except Exception as e:
        print(f"ERROR: {e}")
        return output
    for x in buffer:
        ext = x.split(".")[-1]
        if os.path.isfile(os.path.join(src,x)) and ext not in IGNORE:
            output.append(x)
    return output

def dir_list(src=os.getcwd(), debug=False):
    """returns list of all directories in directory

    Args:
        src (_type_): _description_

    Returns:
        list: list of all directories in current directory (dest)
    """
    print(f"RUNNING {__file__}.{sys._getframe().f_code.co_name} in DEBUG mode") if debug else None
    buffer = []
    output = []
    try:
        buffer = os.listdir(src)
    except Exception as e:
        print(f"ERROR: {e}")
        return output
    for x in buffer:
        if os.path.isdir(os.path.join(src,x)):
            output.append(x)
    return output

def remove_non_image(dir_list,source_dir,debug=False):
    output = []
    for file in dir_list:
        try:
            Image.open(os.path.join(source_dir,file))
            output.append(file)
        except:
            pass
    return output

def display_image(list,source_dir, debug=False):
    length = len(str(len(list))) + 1
    for file in list:
        im = Image.open(os.path.join(source_dir,file))
        exif = im.getexif()
        try:
            t = exif[306]
        except:
            t = os.stat(os.path.join(source_dir,file)).st_mtime 
        idex = str(int(list.index(file))).rjust(length,"0")
        try: 
            date = datetime.datetime.fromtimestamp(t)
        except:
            date = t + " <- NOT USEFUL"

        print(idex,shorten(file,25),date)
        
def display(list,source_dir=os.getcwd(),debug=False):
    print(f"RUNNING {__file__}.{sys._getframe().f_code.co_name} in DEBUG mode") if debug else None
    length = len(str(len(list))) + 1
    for file in list:
        idex = str(int(list.index(file))).rjust(length,"0")
        print(idex,shorten(file,25))

def shorten(str_in,length):
    out = ""    
    if len(str_in) <= length:
        out = str_in.ljust(length - 1, " ")
    else:
        length = int(length/2)
        first_half = str_in[0:length - 3]
        last_half = str_in[len(str_in) - length:len(str_in)]
        out = first_half + "..." + last_half 
    return out

def make_list(in_list,source_dir,_type,debug=False):
    print(f"RUNNING {__file__}.{sys._getframe().f_code.co_name} in DEBUG mode\nShowing Type: {_type}\n--- LISTING {source_dir} ---") if debug else None
    
    if _type == "all" :
        display(in_list,debug=debug)
    elif _type == "directory":
        d_list = dir_list(source_dir,debug=debug)
        display(d_list,debug=debug)
    elif _type == "image":
        im_list = remove_non_image(in_list,source_dir,debug=debug)
        display_image(im_list,source_dir,debug=debug)
    else:
        print("ERROR: Invalid type")
        return False
    return True