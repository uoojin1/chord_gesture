import cv2
import sys
import numpy as np

PATH_TO_DATA = '../data/videos/'

def recordVideo(filename):
  # Create a VideoCapture object
  cap = cv2.VideoCapture(0)
  
  # Check if camera opened successfully
  if (cap.isOpened() == False): 
    print("Unable to read camera feed")
  
  # Default resolutions of the frame are obtained.
  frame_width = int(cap.get(3))
  frame_height = int(cap.get(4))
  
  # Define the codec and create VideoWriter object.The output is stored in 'outpy.avi' file.
  out = cv2.VideoWriter(PATH_TO_DATA + filename, cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))
  
  while(True):
    ret, frame = cap.read()

    # grayout
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if ret == True:
      # Write the frame into the file 'output.avi'
      out.write(frame)
  
      # Display the resulting frame    
      cv2.imshow('frame', frame)
  
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
  args = sys.argv
  print(args)
  recordVideo(args[1])