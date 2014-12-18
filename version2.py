import cv2
import numpy as np
from math import*
import random
import time
##########################################################################
def generate():
    colorlist = ["green","red","yellow","blue","co","purple"]
    list_local = []
    type_local = random.randint(1,3)

    if type_local == 1:
        upperleft = (380,random.randint(440,538))
        height = random.randint(20,60)
        length = random.randint(20,60)
        direction = random.randint(60,80)
        speed = 20
        color = random.choice(colorlist)

    if type_local == 2:
        upperleft = (380,random.randint(270,440))
        height = random.randint(20,60)
        length = random.randint(20,60)
        direction = random.randint(70,110)
        speed = 23
        color = random.choice(colorlist)

    if type_local == 3:
        upperleft = (380,random.randint(100,270))
        height = random.randint(20,60)
        length = random.randint(20,60)
        direction = random.randint(100,120)
        speed = 21
        color = random.choice(colorlist)

    list_local.append(upperleft)
    list_local.append(height)
    list_local.append(length)
    list_local.append(direction)
    list_local.append(speed)
    list_local.append(color)

    return list_local
##########################################################################



class Model(object):
    """Model of fruit"""

class rectangle(object):
    """create a class of rectangle"""

    def __init__(self, upperleft, height, length, direction, speed, color):
        
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
        self.flag = True        


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
                global score
                score += 1
            else:
                for i in range(self.x,self.x+self.length):
                    for j in range(self.y,self.y+self.height):
                        res[i,j] = self.color
                        flip[i,(639-j)] = self.color

    def move(self):
        """move the rectangle"""
        if self.exist:
            Gravity = 1.1
            self.g+=1
            xn = 0
            yn = 0
            xn += sin(self.direction*pi/180)*self.speed - self.g * Gravity
            yn = yn + cos(self.direction*pi/180)*self.speed
            self.x -= int(xn + 0.5)
            self.y -= int(yn + 0.5)
        if self.x > 420 or self.y < 10 or self.y > 580:
            self.exist = False

    def regenerate(self):
        if (not self.exist) and self.flag:
            self.flag = False
            global rect_count
            rect_count -= 1
            




##########################################################################

class View(object):
    """Windows of fruit"""


##########################################################################

class Controls(object):
    """Controls of fruit"""
    def __init__(self):
        self.list = []


##########################################################################


def main():
    """ Parts that runs the code"""
global score
score = 0
cap = cv2.VideoCapture(0)
global rect_count
rect_count = 0

R = rectangle((380,234),50,50,100,27,"green")

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
    global score
    cv2.putText(flip, "Score %s" %(score), (5, 30), cv2.FONT_HERSHEY_TRIPLEX, 1.0, (0,0,0),thickness=4, lineType=cv2.CV_AA)

    blur = cv2.GaussianBlur(res,(5,5),0)

    if rect_count == 0:
        number = random.randint(1,4)
        if number == 1:
            a = generate()
            R1 = rectangle(a[0], a[1], a[2], a[3], a[4], a[5])
            rect_count += 1
        if number == 2:
            a = generate()
            R1 = rectangle(a[0], a[1], a[2], a[3], a[4], a[5])
            b = generate()
            R2 = rectangle(b[0], b[1], b[2], b[3], b[4], b[5])
            rect_count += 2
        if number == 3:
            a = generate()
            R1 = rectangle(a[0], a[1], a[2], a[3], a[4], a[5])
            b = generate()
            R2 = rectangle(b[0], b[1], b[2], b[3], b[4], b[5])
            c = generate()
            R3 = rectangle(c[0], c[1], c[2], c[3], c[4], c[5])
            rect_count += 3
        if number == 4:
            a = generate()
            R1 = rectangle(a[0], a[1], a[2], a[3], a[4], a[5])
            b = generate()
            R2 = rectangle(b[0], b[1], b[2], b[3], b[4], b[5])
            c = generate()
            R3 = rectangle(c[0], c[1], c[2], c[3], c[4], c[5])
            d = generate()
            R4 = rectangle(d[0], d[1], d[2], d[3], d[4], d[5])
            rect_count += 4
    else:
        if number == 1:
            R1.draw()
            R1.move()
            R1.regenerate()
        if number == 2:
            R1.draw()
            R1.move()
            R1.regenerate()
            R2.draw()
            R2.move()
            R2.regenerate()
        if number == 3:
            R1.draw()
            R1.move()
            R1.regenerate()
            R2.draw()
            R2.move()
            R2.regenerate()
            R3.draw()
            R3.move()
            R3.regenerate()
        if number == 4:
            R1.draw()
            R1.move()
            R1.regenerate()
            R2.draw()
            R2.move()
            R2.regenerate()
            R3.draw()
            R3.move()
            R3.regenerate()
            R4.draw()
            R4.move()
            R4.regenerate()

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