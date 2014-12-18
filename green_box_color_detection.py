import cv2
import numpy as np

cap = cv2.VideoCapture(0)
n = 0
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
    if n == 0:
	    for i in range(100):
	    	for j in range (100):
	    		res[i,j]=(0,255,0)

    # blur = cv2.blur(res,(5,5))
    blur = cv2.GaussianBlur(res,(5,5),0)
    blue = res[100, 80]
    # x = 479, y = 639
    track = []
    print blue
    track.append(blue)
    if blue[0]>0 and blue[1]>0 and blue[2]>0:
    	n = 1
    	a = len(track)-1
    	if track[a][0]>0 and track[a][1]>0 and track[a][2]>0:
    		for i in range(100):
    			for j in range (100):
    				res[i,j]=(255,0,0)
    		print "it's blue"
    else:
    	n = 0
    # cv2.imshow('frame',frame)
    # cv2.imshow('mask',mask)
    # cv2.imshow('res',res)
    cv2.imshow('blur',blur)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()