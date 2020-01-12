import pygame as pg
from Settings import *


class BoardCanvas():
    def __init__(self, game):
        self.game = game
        self.font_size = 25
        self.font = pg.font.SysFont("timesnewroman", self.font_size)
    
    def draw(self):
        index = 0
        for y in range(0, 8):
            for x in range(0, 8):
                pg.draw.rect(self.game.screen, BOARD_CANVAS_COLORS[index], pg.Rect(x * TILESIZE + MARGIN, y * TILESIZE + MARGIN, TILESIZE, TILESIZE))
                index = (index + 1) %2
            index = (index + 1) %2
        # draw numbers on y-axis
        for i in range(1, 9):
            text = self.font.render(str(i), True, BLACK)
            self.game.screen.blit(text, (MARGIN - (self.font_size * 0.8), (7 - (i-1))*TILESIZE + MARGIN * 2))
            self.game.screen.blit(text, (WIDTH - (MARGIN - self.font_size * 0.3), (7 - (i-1))*TILESIZE + MARGIN * 2))
        # Draw char on x-axis
        for char, index in zip(BOARD_CANVAS_CHARS, range(8)):
            text = self.font.render(char, True, BLACK)
            self.game.screen.blit(text, (index * TILESIZE + MARGIN * 2, MARGIN - (self.font_size )))
            self.game.screen.blit(text, (index * TILESIZE + MARGIN * 2, HEIGHT - (MARGIN)))
            
