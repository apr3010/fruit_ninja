"""
Plays sound effect sword.mp3 in same file as code
"""

import pygame
import os
import sys

if sys.version_info[:2] <= (2, 7):
    get_input = raw_input
else:
    get_input = input



pygame.mixer.init()

throw = pygame.mixer.Sound('sword.wav') #load sound

gameloop = True
while gameloop:
	print("press b to play the sword sound")
	answer = get_input("press b followed by enter (or x to exit)")
	answer = answer.lower() #force lower case
	if "b" in answer:
		throw.play()
		print("playing sword.mp3 once")
	elif "x" in answer:
		gameloop = False
	else:
		print("please press b or x you little butt")

print "bye bye"
