"""
Plays sound effect sword.mp3 in same file as code
"""

import pygame
import os
import sys
import time


pygame.mixer.init()
throw = pygame.mixer.Sound('sword.wav')

def main():
    throw.play()
    time.sleep(1)

if __name__ == '__main__':
    main()