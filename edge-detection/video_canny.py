import cv2 
import numpy as np
import time 

# cap = cv2.VideoCapture('duckiebot_lane_tracking_mono.mp4') #Load video
cap = cv2.VideoCapture(0) #Capture livestream video content from camera 0 

while(1):
    # Take each frame 
    _, frame = cap.read() 

    # Process with Canny Edge detection in openCV
    edges = cv2.Canny(frame,100,200)

    cv2.imshow('canny edge detection',edges)

    time.sleep(0.02) 

    k = cv2.waitKey(5) & 0xFF
    if k == 27: 
        break
cv2.destroyAllWindows() 
#release the frame 
cap.release() 
