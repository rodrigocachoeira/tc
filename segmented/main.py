from os import listdir
from os.path import isfile, join
import os
import shutil
from PIL import Image
import sys

from utils.images import Images

if __name__ == "__main__":
    Images.path = "./all/"
    Images.segmented_path = "./xrays/"

    images = Images()
    files = [f for f in listdir(Images.path) if isfile(join(Images.path, f))]

    if images.dir_empty():
        images.copy_images(files)

    #images.resize_images()