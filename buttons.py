"""
Class for buttons
"""

"""Button class sourced from Simon H. Larsen, http://lagusan.com/button-drawer-python-2-6/"""
import pygame as pyg


class Button:
    def create_button(self, surface, color, x, y, length, height, width, text, text_color):
        surface = self.draw_button(surface, color, length, height, x, y, width)
        surface = self.write_text(surface, text, text_color, length, height, x, y)
        self.rect = pyg.Rect(x,y, length, height)
        return surface

    def write_text(self, surface, text, text_color, length, height, x, y):
        font_size = int(length//len(text))
        myFont = pyg.font.SysFont("Calibri", font_size)
        myText = myFont.render(text, 1, text_color)
        surface.blit(myText, ((x+length/2) - myText.get_width()/2, (y+height/2) - myText.get_height()/2))
        return surface

    def draw_button(self, surface, color, length, height, x, y, width):           
        for i in range(1,10):
            s = pyg.Surface((length+(i*2),height+(i*2)))
            s.fill(color)
            alpha = (255/(i+2))
            if alpha <= 0:
                alpha = 1
            s.set_alpha(alpha)
            pyg.draw.rect(s, color, (x-i,y-i,length+i,height+i), width)
            surface.blit(s, (x-i,y-i))
        pyg.draw.rect(surface, color, (x,y,length,height), 0)
        pyg.draw.rect(surface, (190,190,190), (x,y,length,height), 1)  
        return surface
    
    def pressed(self, mouse_pos):
        if mouse_pos[0] > self.rect.topleft[0] and mouse_pos[1] > self.rect.topleft[1] and mouse_pos[0] < self.rect.bottomright[0] and mouse_pos[1] < self.rect.bottomright[1]:
            # print "Some button was pressed!"
            return True
        else: return False