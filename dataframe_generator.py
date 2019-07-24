import os
import sys
import numpy as np
import pandas as pd

PATH_TO_IMG_FOLDERS = '../data/imgs/'
PATH_TO_DATAFRAME_FOLDER = '../data/dataframes/'
FILE_TO_IGNORE = {'.DS_Store'}

def sortByImageNumber(x):
  return int((x.split('.')[0]).split('-')[1])

def filterIgnored(path):
  z = [x for x in os.listdir(path) if x not in FILE_TO_IGNORE]
  return z

def dataframeGenerator(filename):
  filename_to_class = []

  img_folders = filterIgnored(PATH_TO_IMG_FOLDERS)

  for folder in sorted(img_folders):
    image_class = folder
    imgs = filterIgnored(PATH_TO_IMG_FOLDERS + image_class)

    for img in sorted(imgs, key=sortByImageNumber):
      gesture_class = img.split('.')[0].split('-')[0]
      filename_to_class.append([img, gesture_class])
  
  # create pandas dataframe that will be exported as a csv file
  img_data_df = pd.DataFrame(columns=['filename', 'class'], data=filename_to_class)

  # wrtie to a csv file
  img_data_df.to_csv(PATH_TO_DATAFRAME_FOLDER + filename, encoding='utf-8', index=False)
  print('created csv file named {filename}'.format(filename=filename))      

if __name__ == "__main__":
  args = sys.argv

  if len(args) > 1:
    filename = args[1]
  else:
    filename = 'filename_to_class.csv'

  dataframeGenerator(filename)