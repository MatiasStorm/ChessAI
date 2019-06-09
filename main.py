import pygame as pg
import sys
from Settings import *
from BoardCanvas import BoardCanvas
from math import floor
from ChessEngine import ChessEngine
from ChessAI import ChessAI
from TextPanel import TextPanel

vector = pg.math.Vector2

class Game():
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH + TF_WIDTH, HEIGHT), pg.SRCALPHA, 32)
        self.clock = pg.time.Clock()
        pg.display.set_caption(TITLE)
        icon = pg.image.load(IMAGE_FILE_DICT["wR"])
        pg.display.set_icon(icon)
        self.load_data()
        self.engine = ChessEngine()
        self.AI = ChessAI(4)
        
    def load_data(self):
        self.image_dict = {}
        for name in IMAGE_FILE_DICT:
            image = pg.image.load(IMAGE_FILE_DICT[name])
            image = pg.transform.scale(image, (TILESIZE, TILESIZE))
            self.image_dict[name] = image

    def new(self):
        self.piece_matrix = [x[:] for x in STARTING_PIECE_MATRIX]
        self.start_pos = ()
        self.board_canvas = BoardCanvas(self)
        self.screen.fill(MAHOGANY)
        self.board_canvas.draw()
        self.text_panel = TextPanel()
        self.checked = ""
        self.computer_turn = False
    
    def run(self):
        self.running = True
        while self.running:
            self.clock.tick(FPS)
            if self.computer_turn:
                self.handle_computer_turn()
            self.events()
            self.draw()
    
    def handle_computer_turn(self):
        move = self.AI.search(self.piece_matrix, -sys.maxsize, sys.maxsize)
        piece = self.piece_matrix[move[0][0]][move[0][1]]
        self.move_piece(move[0], move[1], 'C')
        text = "Computer moved " + CHAR_TO_STR[piece[1]] +" to " + BOARD_CANVAS_CHARS[move[1][1]] +  str(7 - move[1][0] + 1) + ". Score: " + str(move[2]) + ". Nodes: " + str(move[3][0]) + " CutOffs: " + str(move[3][1])
        self.text_panel.write(text)
    
    def animate_movement(self, start_tile, end_tile, piece):
        current_pos = vector(start_tile[1] * TILESIZE + MARGIN, start_tile[0] * TILESIZE + MARGIN)
        end_pos = vector(end_tile[1] * TILESIZE + MARGIN, end_tile[0] * TILESIZE + MARGIN)
        direction = end_pos - current_pos
        direction = direction.normalize() * 8
        image = self.image_dict[piece]
        while (end_pos.x - 10 > current_pos.x or current_pos.x > end_pos.x + 10) or (end_pos.y - 10 > current_pos.y or current_pos.y > end_pos.y + 10):
            dt = self.clock.tick(FPS)
            self.events()
            self.draw()
            self.screen.blit(image, (current_pos.x, current_pos.y))
            pg.display.update()
            current_pos += direction
                
    
    def move_piece(self, start_tile, end_tile, mover):
        if self.engine.is_move_allowed(self.piece_matrix, start_tile, end_tile):
            piece = self.piece_matrix[start_tile[0]][start_tile[1]]
            self.piece_matrix[start_tile[0]][start_tile[1]] = ".."
            self.animate_movement(start_tile, end_tile, piece)
            self.piece_matrix[end_tile[0]][end_tile[1]] = piece
            self.checked = ""
            self.computer_turn = not self.computer_turn
            if mover == "P":
                text = "Player moved " + CHAR_TO_STR[piece[1]] +" to " + BOARD_CANVAS_CHARS[end_tile[1]] +  str(7 - end_tile[0] + 1)
                self.text_panel.write(text)
                self.check_mate('b')
            else:
                self.check_mate('w')
                
                
    def quit(self):
        self.running = False
        pg.quit()
        sys.exit()
    
    def check_mate(self, color):
        if self.engine.check(self.piece_matrix, color):
            if self.engine.check_mate(self.piece_matrix, color):
                self.text_panel.write("Check-mate!", RED if color == 'w' else GREEN)
                self.GO_screen(color)
            else:
                self.text_panel.write("Check!", RED if color == 'w' else GREEN)
                self.checked = color
    
    def get_mouse_pos_rc(self): # Returns the mouse positions tranlated into rows and columns of the board
        pos = pg.mouse.get_pos()
        col = floor((pos[0] - MARGIN) / TILESIZE)
        row = floor((pos[1] - MARGIN) / TILESIZE)
        return (row, col)
        
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                if event.key == pg.K_r:
                    self.running = False;
            
            elif event.type == pg.MOUSEBUTTONDOWN and event.button == LEFT:
                mouse_pos = pg.mouse.get_pos()
                if mouse_pos[0] > MARGIN and mouse_pos[0] < WIDTH - MARGIN and mouse_pos[1] > MARGIN and mouse_pos[1] < HEIGHT - MARGIN and not self.computer_turn:
                    if self.start_pos:
                        self.move_piece(self.start_pos, self.get_mouse_pos_rc(), 'P')
                        self.start_pos = ()
                    else:
                        self.start_pos = self.get_mouse_pos_rc()
                        if "w" not in self.piece_matrix[self.start_pos[0]][self.start_pos[1]]:
                            self.start_pos = ()
            elif event.type == pg.MOUSEBUTTONDOWN and event.button == RIGHT:
                self.start_pos = ()

            
    def draw(self):
        self.screen.fill(MAHOGANY)
        self.board_canvas.draw()
        # Drawing pieces:
        for row_index, row in enumerate(self.piece_matrix):
            for col_index, piece in enumerate(row):
                if piece in self.image_dict.keys():
                    image = self.image_dict[piece] # Load Image
                     # Scale image to tilesize
                    y = MARGIN + TILESIZE * row_index
                    x = MARGIN + TILESIZE * col_index
                    self.screen.blit(image, (x, y))
                    if piece == self.checked + "K":
                        pg.draw.rect(self.screen, DARKRED, pg.Rect(x, y, TILESIZE, TILESIZE), 4)
        
        if self.start_pos: ## if start position is defined, mark it and show allowed moves
            mark_surface = pg.Surface((TILESIZE, TILESIZE))
            mark_surface.set_alpha(80)
            mark_surface.fill(ORANGE)
            y = MARGIN + TILESIZE * self.start_pos[0]
            x = MARGIN + TILESIZE * self.start_pos[1]
            self.screen.blit(mark_surface, (x, y))
            self.show_allowed_moves(self.start_pos)
        
        if self.is_mouse_over_piece() and not self.computer_turn:
            self.show_allowed_moves(self.get_mouse_pos_rc())
        
        # Text field:
        self.screen.blit(self.text_panel.surface, (WIDTH, MARGIN))
        
        pg.display.update()
    
    def is_mouse_over_piece(self):
        mouse_pos = self.get_mouse_pos_rc()
        for r in range(len(self.piece_matrix)):
            for c in range(len(self.piece_matrix[0])):
                if (r, c) == mouse_pos and (r, c) != self.start_pos and 'w' in self.piece_matrix[r][c]:
                    return True
        return False
        
    def show_allowed_moves(self, pos):
        moves = self.engine.get_allowed_moves(self.piece_matrix, pos)
        if moves:
            for move in moves["M"]:
                mark_surface = pg.Surface((TILESIZE, TILESIZE))
                mark_surface.set_alpha(150)
                y = MARGIN + TILESIZE * move[0]
                x = MARGIN + TILESIZE * move[1]
                self.screen.blit(mark_surface, (x, y))
    
    def GO_screen(self, color):
        self.running = False
        self.draw()
        font = pg.font.SysFont("consolas", 40)
        text = "The computer won, press a key to play again."
        if color == 'b':
            text = "Congratulation you won, press a key to play again."
        text_surface = font.render(text, True, WHITE)
        self.screen.blit(text_surface, (WIDTH/8, HEIGHT/3))
        pg.display.update()
        self.wait_for_key()
    
    def wait_for_key(self):
        pg.event.wait()
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.quit()
                if event.type == pg.KEYUP:
                    waiting = False
        
if __name__ == "__main__":
    game = Game()
    while True:
        game.new()
        game.run()
    pg.quit()



