import cv2
import numpy as np
from math import*
import random
##########################################################################

##########################################################################

class Model(object):
	"""Model of fruit"""

class rectangle(object):
	"""create a class of rectangle"""

	def __init__(self, upperleft, height, length, direction, speed, color):
		colorlist = [(255,0,0),(255,255,0),(255,0,255),(0,255,0),(0,0,255),(0,255,255)]
		if color == "green":
			self.color = (0,255,0)
		if color == "red":
			self.color = (0,0,255)
		if color == "blue":
			self.color = (255,0,0)
		if color == "co":
			self.color = (255,255,0)
		if color == "yellow":
			self.color = (0,255,255)
		if color == "purple":
			self.color = (255,0,255)

		self.x = upperleft[0]
		self.y = upperleft[1]
		self.height = height
		self.length = length
		self.direction = direction
		self.speed = speed
		self.g = 0
		self.exist = True
		


	def draw(self):
		
		n=0
		if self.exist:
			for i in range(self.x,self.x+self.length):
			    for j in range(self.y,self.y+self.height):
			        if res[i,j][0]>50 and res[i,j][0]<255:
			            if res[i,j][1]>0 and res[i,j][1]<255:
			                if res[i,j][2]>0 and res[i,j][2]<255:
			                    n+=1

			if n>=self.length * self.height/4:
			    self.exist = False
			else:
			    for i in range(self.x,self.x+self.length):
			        for j in range(self.y,self.y+self.height):
			            res[i,j]=self.color
			            flip[i,(639-j)]=self.color

	def move(self):
	    """move the rectangle"""
	    if self.exist:
		    Gravity = 1.5
		    self.g+=1
		    xn = 0
		    yn = 0
		    xn += sin(self.direction*pi/180)*27 - self.g * Gravity
		    yn = yn + cos(self.direction*pi/180)*27 
		    self.x -= int(xn + 0.5)
		    self.y -= int(yn + 0.5)

##########################################################################

class Windows(object):
	"""Windows of fruit"""


##########################################################################

class Controls(object):
	"""Controls of fruit"""

##########################################################################


def main():
	""" Parts that runs the code"""

cap = cv2.VideoCapture(0)

R1 = rectangle((380,10),100,50,130,0,"red")
R2 = rectangle((380,500),50,100,70,0,"co")
R3 = rectangle((380,200),50,100,83,0,"green")

while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([75,75,50])
    upper_blue = np.array([130,200,255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    flip = cv2.flip(frame,180)

    blur = cv2.GaussianBlur(res,(5,5),0)

    R1.draw()
    R1.move()

    R2.draw()
    R2.move()

    R3.draw()
    R3.move()

    cv2.imshow('frame',flip)
    #cv2.imshow('mask',mask)
    #cv2.imshow('res',blur)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()

##########################################################################		
if __name__ == "__main__":
    main()
