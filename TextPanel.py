import pygame as pg
from Settings import *

class TextPanel():
    def __init__(self):
        self.surface = pg.Surface((TF_WIDTH - MARGIN, TF_HEIGHT - MARGIN * 2))
        self.font_size = 15
        self.y = 0
        self.font = pg.font.SysFont("consolas", self.font_size)
    
    def clear(self):
        self.surface = pg.Surface((TF_WIDTH - MARGIN, TF_HEIGHT - MARGIN * 2))
        self.y = 0
    
    def write(self, text, color=WHITE):
        if self.y >= TF_HEIGHT - self.font_size*4:
            self.clear()
        text = self.font.render(text, True, color)
        self.surface.blit(text, (0,self.y))
        self.y += self.font_size
        