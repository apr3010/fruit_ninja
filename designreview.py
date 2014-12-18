import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([50,0,0])
    upper_blue = np.array([255,255,255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)



    n=0
    for i in range(100):
       for j in range(100):
          if res[i,j][0]>50 and res[i,j][0]<255:
             if res[i,j][1]>0 and res[i,j][1]<255:
                if res[i,j][2]>0 and res[i,j][2]<255:
                   n+=1
    if n>=2500:
        for i in range(100):
            for j in range(100):
                res[i,j]=[255,0,0]
                frame[i,j]=[255,0,0]

    else:
        for i in range(100):
            for j in range(100):
                res[i,j]=[0,255,0]
                frame[i,j]=[0,255,0]

    blur = cv2.GaussianBlur(res,(5,5),0)




    cv2.imshow('frame',frame)
    #cv2.imshow('mask',mask)
    #cv2.imshow('res',blur)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()