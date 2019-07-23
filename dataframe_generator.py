import os
import numpy as np

PATH_TO_IMG_FOLDERS = '../data/imgs/'
FILE_TO_IGNORE = {'.DS_Store'}

def sortByImageNumber(x):
  return int((x.split('.')[0]).split('-')[1])

def filterIgnored(path):
  z = [x for x in os.listdir(path) if x not in FILE_TO_IGNORE]
  return z

def dataframeGenerator():
  img_folders = filterIgnored(PATH_TO_IMG_FOLDERS)

  for folder in sorted(img_folders):
    image_class = folder
    imgs = filterIgnored(PATH_TO_IMG_FOLDERS + image_class)

    for img in sorted(imgs, key=sortByImageNumber):
      print('image!', img)

if __name__ == "__main__":
  dataframeGenerator()