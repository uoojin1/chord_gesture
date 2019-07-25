import cv2
from gesture_prediction_model import GesturePredictionModel
import numpy as np

model = GesturePredictionModel()

class VideoCamera:
  
  def __init__(self):
    self.video = cv2.VideoCapture(0)
  
  def __del__(self):
    self.video.release()
  
  def get_frame(self):
    ret, frame = self.video.read()
    # display frame
    # _, jpeg = cv2.imencode('.jpg', frame)
    # return jpeg.tobtyes()

    if ret == True:
      # Display the resulting frame    
      cv2.imshow('frame', frame)

  def run(self):
    frame_number = 0
    while(True):
      ret, frame = self.video.read()

      if ret == True:
        # Display the resulting frame   
        frame = cv2.resize(frame,(299,299))
 
        cv2.imshow('frame', frame)

        if frame_number % 25 == 0:
          print('\nframe number: ', frame_number)
          model.predict_gesture(frame)
    
        # Press Q on keyboard to stop recording
        if cv2.waitKey(1) & 0xFF == ord('q'):
          break
    
      # Break the loop
      else:
        break 
      
    # When everything done, release the video capture and video write objects
    self.video.release()
    out.release()
    
    # Closes all the frames
    cv2.destroyAllWindows() 