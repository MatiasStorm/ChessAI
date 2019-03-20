import pygame as pg
from Settings import *


class Board():
    def __init__(self, game):
        self.game = game

    def draw(self):
        index = 0
        for y in range(MARGIN, HEIGHT - MARGIN, TILESIZE):
            for x in range(MARGIN, WIDTH - MARGIN, TILESIZE):
                pg.draw.rect(self.game.screen, BOARD_COLORS[index], pg.Rect(x, y, TILESIZE, TILESIZE))
                index = (index + 1) % 2
            index = (index + 1) % 2    
                




