import cv
import cv2
import numpy as np
from matplotlib import pyplot as plt

cv.NamedWindow("window", cv.CV_WINDOW_AUTOSIZE)
camera_index = 0
capture = cv.CaptureFromCAM(camera_index)

def repeat():
    global capture #declare as globals since we are assigning to them now
    global camera_index
    frame = cv.QueryFrame(capture)
    cv.ShowImage("window", frame)
    # print type(frame)
    edges = cv2.Canny(frame,100,200)
    plt.imshow(frame)
    c = cv.WaitKey(10)
    if(c=="n"): #in "n" key is pressed while the popup window is in focus
        camera_index += 1 #try the next camera index
        capture = cv.CaptureFromCAM(camera_index)
        if not capture: #if the next camera index didn't work, reset to 0.
            camera_index = 0
            capture = cv.CaptureFromCAM(camera_index)

while True:
    repeat()
    if cv.WaitKey(10) == 27:
        break

