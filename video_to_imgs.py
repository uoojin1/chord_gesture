import cv2
import os
import sys
import numpy as np

PATH_TO_VIDEOS = '../data/videos/'
PATH_TO_IMGS = '../data/imgs/'

def videoToImgs(filename):
  print(filename)
  
  image_class = filename.split('.')[0]
  print('image_class', image_class)

  cap = cv2.VideoCapture(PATH_TO_VIDEOS + filename)

  filenumber = 0
  framenumber = 0

  while(cap.isOpened()):
    capture_success, frame = cap.read()

    # only read the third frame to reduce the number of images collected
    framenumber += 1
    if framenumber % 3 != 0:
      # goto beginning of loop and read next frame
      continue

    output_file_name = '{image_class}/{image_class}-{filenumber}.jpg'.format(
      filenumber=filenumber,
      image_class=image_class
    )

    print('output_filename', output_file_name)

    if capture_success == True:
      cv2.imshow('frame', frame)

      cv2.imwrite(PATH_TO_IMGS + output_file_name, frame)

      # end streaming with 'q'
      # waitKey(100) means each frame is displayed for 100ms, thus 10 fps
      # it would be ideal for this value to match the recorded fps
      if cv2.waitKey(100) & 0xFF == ord('q'):
        break

    else:
      break
    
    filenumber += 1

  cap.release()
  cv2.destroyAllWindows()


if __name__ == "__main__":
  args = sys.argv
  if len(args) > 1:
    filename = args[1]
    videoToImgs(filename)
  else:
    videos = os.listdir('../data/videos')
    for video_filename in videos:
      videoToImgs(video_filename)