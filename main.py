import numpy as np
from video_camera import VideoCamera

if __name__ == "__main__":
  
  video_camera = VideoCamera()
  print('created video camera')

  # while True:
  #   frame = video_camera.get_frame()

  video_camera.run()
