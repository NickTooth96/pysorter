import json
from PIL import Image
import io
import os



def merge_exif(im_path, ex_path, debug=False):
    # open image and extract exif data
    imWithEXIF = Image.open(im_path)
    original_exif = imWithEXIF.getexif()
    # imWithEXIF.info['exif']

    # read exif data from json file and get time image taken
    with open(ex_path, 'r') as f:
        exif_data = f.read()
    try:
        exif_data = eval(exif_data)
    except:
        exif_data = json.loads(exif_data)
    create_time = exif_data['photoTakenTime']['timestamp']

    # update exif data with time image taken
    original_exif[306] = create_time
    imWithEXIF.save(im_path, exif=original_exif)

    check = Image.open(im_path)
    mod_exif = check.getexif()
    return mod_exif

def find_pairs(path=os.getcwd(), debug=False):
    pairs = {}
    good_pairs = {}
    bad_pairs = {}
    for file in os.listdir(path):
        ext = file.split('.')[-1]
        if ext in im_exts:
            pairs[file] = f"{file}.json" if os.path.exists(f"{file}.json") else None
    for k,v in pairs.items():
        if v:
            good_pairs[k] = v
        else:
            bad_pairs[k] = v
    return good_pairs, bad_pairs, len(good_pairs.items()), len(bad_pairs.items())


## Variables

im_exts = ['jpg', 'jpeg', 'png', 'tiff', 'tif', 'gif', 'bmp', 'webp']

## Main

pair_info = find_pairs()
print(pair_info[2], pair_info[3])

pairs = pair_info[0]

for k,v in pairs.items():
    # print(f"Processing {k} with {v}")
    merge_exif(k,v)
    # print(f"Processed {k}")