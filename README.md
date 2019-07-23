# chord_gesture

playing music chords with hand gestures.

modules
1. record_video.py
    -- records a video using the default camera (macbook camera for MacBooks) and saves it to a .avi file.
    -- takes filename as argument and saves the video inside ../data/ directory with the given name

2. video_parser.py
    -- locates the hand within the video
    -- applies image processing