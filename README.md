# chord_gesture

playing music chords with hand gestures.

modules
1. record_video.py
    - records a video using the default camera (macbook camera for MacBooks) and saves it to a .avi file.
    - takes filename as argument and saves the video inside ../data/ directory with the given name

2. video_to_imgs.py
    - generate images from the recorded videos
    - you can pass in a filename to target single video
    - if filename is not passed in as an argument, it will iterate the image generation procedure for all images under '../data/videos/'

3. dataframe_generator.py
    - create CSVs from the /data/imgs/ to use pandas' dataframe in the ML_core.py

4. ML_core.py
    - brain of the application
    - build a CNN model and train it against the generated data from 'video_to_imgs' module.
    - save model weights to a file