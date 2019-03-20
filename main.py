import pygame as pg
import sys
from Settings import *
from Board import Board
from math import floor
from ChessEngine import ChessEngine

class Game():
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT), pg.SRCALPHA, 32)
        self.clock = pg.time.Clock()
        pg.display.set_caption(TITLE)
        self.load_data()
        self.engine = ChessEngine()
        
    def load_data(self):
        self.image_dict = {}
        for name in IMAGE_FILE_DICT:
            image = pg.image.load(IMAGE_FILE_DICT[name])
            image = pg.transform.scale(image, (TILESIZE, TILESIZE))
            self.image_dict[name] = image

    def new(self):
        self.piece_matrix = STARTING_PIECE_MATRIX
        self.start_pos = ()
        self.board = Board(self)
        self.screen.fill(DARKGREY)
        self.board.draw()
    
    def run(self):
        self.running = True
        while self.running:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.draw()
            
    def quit(self):
        self.running = False
        pg.quit()
        sys.exit()
    
    def get_mouse_pos_rc(self): # Returns the mouse positions tranlated into row and column of the board
        pos = pg.mouse.get_pos()
        col = floor((pos[0] - MARGIN) / TILESIZE)
        row = floor((pos[1] - MARGIN) / TILESIZE)
        return (row, col)
        
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            elif event.type == pg.MOUSEBUTTONDOWN and event.button == LEFT:
                mouse_pos = pg.mouse.get_pos()
                if mouse_pos[0] > MARGIN and mouse_pos[0] < WIDTH - MARGIN and mouse_pos[1] > MARGIN and mouse_pos[1] < HEIGHT - MARGIN:
                    if self.start_pos:
                        self.move_piece(self.start_pos, self.get_mouse_pos_rc())
                        self.start_pos = ()
                    else:
                        self.start_pos = self.get_mouse_pos_rc()
                        if "w" not in self.piece_matrix[self.start_pos[0]][self.start_pos[1]]:
                            self.start_pos = ()
            elif event.type == pg.MOUSEBUTTONDOWN and event.button == RIGHT:
                self.start_pos = ()

    def move_piece(self, start_pos, end_pos):
        if self.engine.is_move_allowed(self.piece_matrix, start_pos, end_pos): # Only move piece if the move is allowed
            moving_piece = self.piece_matrix[start_pos[0]][start_pos[1]]
            self.piece_matrix[start_pos[0]][start_pos[1]] = ""
            self.piece_matrix[end_pos[0]][end_pos[1]] = moving_piece
        
    def draw(self):
        self.board.draw()
        
        # Drawing pieces:
        for row_index, row in enumerate(self.piece_matrix):
            for col_index, piece in enumerate(row):
                if piece in self.image_dict.keys():
                    image = self.image_dict[piece] # Load Image
                     # Scale image to tilesize
                    y = MARGIN + TILESIZE * row_index
                    x = MARGIN + TILESIZE * col_index
                    self.screen.blit(image, (x, y))
        
        if self.start_pos: ## if start position is defined, mark it and show allowed moves
            mark_surface = pg.Surface((TILESIZE, TILESIZE))
            mark_surface.set_alpha(175)
            mark_surface.fill(BLACK)
            y = MARGIN + TILESIZE * self.start_pos[0]
            x = MARGIN + TILESIZE * self.start_pos[1]
            self.screen.blit(mark_surface, (x, y))
            self.show_allowed_moves()
            
        pg.display.update()
        
    def show_allowed_moves(self):
        moves = self.engine.get_allowed_moves(self.piece_matrix, self.start_pos)
        for move in moves:
            mark_surface = pg.Surface((TILESIZE, TILESIZE))
            mark_surface.set_alpha(100)
            mark_surface.fill(GREEN)
            y = MARGIN + TILESIZE * move[0]
            x = MARGIN + TILESIZE * move[1]
            self.screen.blit(mark_surface, (x, y))

if __name__ == "__main__":
    game = Game()
    while True:
        game.new()
        game.run()
    pg.quit()

























































