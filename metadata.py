import pandas as pd
import shutil
import os
from shutil import move

meta_ham = pd.read_csv('/metadata.csv')

keyword = "meta_ham[image_id]"

from_folder = r"c:/"
to_folder = r"c:/???"

for i in os.listdir(from_folder):
    if keyword in i:
        move(os.path.join(from_folder, i), os.path.join(to_folder, i))