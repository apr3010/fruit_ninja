import pygame as pyg
from pygame.locals import *
import test2
from buttons import Button
import buttons
import welcome_page
import sys

def score_main(score):
    # Set size of screen
    x = 620
    y = 700
    
    pyg.init()
    screen = pyg.display.set_mode((x, y))
    pyg.display.set_caption('Fruit Ninja')

    # Place background image
    background_img = pyg.image.load("fruit_ninja.jpeg").convert()
    screen.blit(background_img, [0,0])
    pyg.display.flip()

    # Sets the text to display score
    font = pyg.font.Font(None, 80)
    text = font.render("Your final score is %s" %(score), 1, (255, 255, 255))
    
    if score>=100:
        screen.blit(text, (20, 350))
    elif score>=10 and score<100:
        screen.blit(text, (35, 350))
    else:
        screen.blit(text, (47, 350))

    # Makes two buttons: one to play game again and one to quit the game
    again_button = buttons.Button()
    again = again_button.create_button(screen,(205,133,63), 0, 480, 620, 80, 0, "Play More",(255,255,255))
    again_pos = again.get_rect()       
    screen.blit(again,again_pos)

    quit_button = buttons.Button()
    quitting = quit_button.create_button(screen,(205,133,63), 0, 600, 620, 80, 0, "Quit Game",(255,255,255))
    quit_pos = quitting.get_rect()
    screen.blit(quitting,quit_pos)
    pyg.display.flip()
    
    # Sets all the transition conditions: changing screens, closing windows, etc.
    while True:
        pyg.init()
        for event in pyg.event.get():
            if event.type == QUIT:
                pyg.quit()
                sys.exit(0)
                return
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pyg.quit()
                    sys.exit(0)
                    return
            elif event.type == MOUSEBUTTONDOWN:
                mouse_pos = pyg.mouse.get_pos()
                if again_button.pressed(mouse_pos):
                    pyg.quit()
                    test2.test_main()
                    return
                elif quit_button.pressed(mouse_pos):
                    pyg.quit()
                    sys.exit(0)
                    return
        pyg.display.flip()
                    
if __name__ == '__main__':
    score_main(score)
