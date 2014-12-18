# -*- coding: utf-8 -*-
import pygame as pyg
import welcome_page
import buttons
import test2

from pygame.locals import *

def rules_main():
    # Set screen size and initialize pygame and font
    pyg.init()
    pyg.font.init()
    screen = pyg.display.set_mode((620, 1000))
    
    # Apply background image
    background_image = pyg.image.load("background.jpeg")
    background_image = pyg.transform.scale(background_image,(620, 1000))
    pyg.display.set_icon(background_image)
    pyg.display.set_caption("Fruit Ninja Rules")
    screen.blit(background_image,[0,0])
    pyg.display.flip()
    
    # Places a darker transluscent rectangle to read text on screen
    trans = pyg.Surface((620,1000))
    trans.set_alpha(75) # 0 = transparent, 255 = opaque
    trans.fill((0,0,0))
    screen.blit(trans,(0,0))

    # Create main menu and play buttons
    main_button = buttons.Button()
    main = main_button.create_button(background_image,(205,133,63), 0, 0, 150, 80, 0, "Main",(255,255,255))
    main_pos = main.get_rect()    
    screen.blit(main,main_pos)
    pyg.display.flip()

    playing_button = buttons.Button()
    playing = playing_button.create_button(background_image,(205,133,63), 470, 765, 150, 80, 0, "Play",(255,255,255))
    playing_pos = playing.get_rect()    
    screen.blit(playing,playing_pos)
    pyg.display.flip()
    
    # Sets the default font
    default_font = pyg.font.Font(None, 60)
    
    # Sets up words on screen
    skipline = (None,0)
    text_height = 100
    rules_list = [('1. Wear the blue gloves',1),('provided.',1),skipline,
              ('2. Wave your hands on',1),('all the shapes that pop',1),('up to "cut" all the fruit.',1), skipline,
              ('3. Try to cut as much',1),('fruit within the timed',1),('limit of a minute.',1)]
    
    # Runs through list to display on screen
    for i in range(len(rules_list)):
        objective = default_font.render(rules_list[i][0], 1, (255,255,255))
        objective_pos = objective.get_rect()
        text_height += 50
        objective_pos.top = text_height
        objective_pos.left = 100 # Keep position consistent
        screen.blit(objective, objective_pos)
    pyg.display.flip()
    
    # Sets transition conditions (quitting, pressing buttons, etc.)
    while True:
        for event in pyg.event.get():
            if event.type == QUIT:
                pyg.quit()
                return
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pyg.quit()
                    return
            elif event.type == MOUSEBUTTONDOWN:
                mouse_pos = pyg.mouse.get_pos()
                if main_button.pressed(mouse_pos):
                    welcome_page.welcome_main()
                    return
                elif playing_button.pressed(mouse_pos):
                    pyg.quit()
                    test2.test_main()
                    return

if __name__ == '__main__':
    pyg.init()
    rules_main()