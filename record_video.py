#!/usr/bin/python

import sys
import cv2

def recordVideo(output_file_name):
  # Create a VideoCapture object
  cap = cv2.VideoCapture(0)
  
  # Check if camera opened successfully
  if (cap.isOpened() == False): 
    print("Unable to read camera feed")
  
  # use resolution of the captured image
  frame_width = int(cap.get(3))
  frame_height = int(cap.get(4))
  
  # Define the codec and create VideoWriter object.The output is stored in 'outpy.avi' file.
  out = cv2.VideoWriter('outpy.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))
  
  while(True):
    ret, frame = cap.read()
  
    if ret == True: 
      # gray out the video
      gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
      out.write(gray)
  
      # Display the resulting frame    
      cv2.imshow('frame',frame)
  
      # Press Q on keyboard to stop recording
      if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
    # Break the loop
    else:
      break 
  
  # When everything done, release the video capture and video write objects
  cap.release()
  out.release()
  
  # Closes all the frames
  cv2.destroyAllWindows()

if __name__ == "__main__":
  args = sys.argv[1:]
  output_file_name = args[0]
  recordVideo(output_file_name)
