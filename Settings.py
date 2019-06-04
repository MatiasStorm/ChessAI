
# Colors:
BLACK = (0,0,0)
WHITE = (255, 255, 255)
DARKGREY = (30, 30, 30)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
DARKRED = (170, 0, 0)
SADDLEBROWN = (139,69,19)
BURLYWOOD = (222,184,135)
MAHOGANY = (93, 45, 5)
YELLOW = (200, 200, 0)
ORANGE = (200, 100, 0)

## Game settings:
WIDTH = 650
HEIGHT = 650
TITLE = "Chess"
FPS = 40
LEFT = 1
RIGHT = 3
STARTING_PIECE_MATRIX = [["bR", "bH", "bB", "bK", "bQ", "bB", "bH", "bR"],
                         ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
                         ["..", "..", "..", "..", "..", "..", "..", ".."],
                         ["..", "..", "..", "..", "..", "..", "..", ".."],
                         ["..", "..", "..", "..", "..", "..", "..", ".."],
                         ["..", "..", "..", "..", "..", "..", "..", ".."],
                         ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
                         ["wR", "wH", "wB", "wK", "wQ", "wB", "wH", "wR"]]
IMAGE_FOLDER = "C:\\Users\\mat-4\\Desktop\\Atom projects\\Python Projects\\ML & AI\\Search\\ChessAI\\Images"
IMAGE_FILE_DICT = {"bR":IMAGE_FOLDER + "\\b_rock.PNG",  "bH":IMAGE_FOLDER + "\\b_knight.PNG",
                    "bB":IMAGE_FOLDER + "\\b_bishop.PNG","bQ":IMAGE_FOLDER + "\\b_queen.PNG", 
                    "bK":IMAGE_FOLDER + "\\b_king.PNG",  "bP":IMAGE_FOLDER + "\\b_pawn.PNG",
                    "wR":IMAGE_FOLDER + "\\w_rock.PNG",  "wH":IMAGE_FOLDER + "\\w_knight.PNG",
                    "wB":IMAGE_FOLDER + "\\w_bishop.PNG","wQ":IMAGE_FOLDER + "\\w_queen.PNG", 
                    "wK":IMAGE_FOLDER + "\\w_king.PNG",  "wP":IMAGE_FOLDER + "\\w_pawn.PNG"}
CHAR_TO_STR = {'K':"King", 'B': "Bishop", "Q":"Queen", "R":"Rock", "P":"Pawn", "H": "Knight"}


# Board Settings:
TILESIZE = 75
MARGIN = 25
BOARD_COLORS = [BURLYWOOD, SADDLEBROWN]
BOARD_CHARS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

## ChessEngine settings:
buttom_K_pos_factor = [[-3, -4, -4, -5, -5, -4, -4, -3],
                 [-3, -4, -4, -5, -5, -4, -4, -3],
                 [-3, -4, -4, -5, -5, -4, -4, -3],
                 [-3, -4, -4, -5, -5, -4, -4, -3],
                 [-2, -3, -3, -4, -4, -3, -3, -2],
                 [-1, -2, -2, -2, -2, -2, -2, -1],
                 [2, 2, 0, 0, 0, 0, 2, 2],
                 [2, 3, 1, 0, 0, 1, 3, 2]]
buttom_Q_pos_factor = [[-2, -1, -1, -0.5, -0.5, -1, -1, -2],
                 [-1, 0, 0, 0, 0, 0, 0, -1],
                 [-1, 0, 0.5, 0.5, 0.5, 0.5, 0, -1],
                 [-0.5, 0, 0.5, 0.5, 0.5, 0.5, 0, -0.5],
                 [0, 0, 0.5, 0.5, 0.5, 0.5, 0, -0.5],
                 [-1, 0.5, 0.5, 0.5, 0.5, 0.5, 0, -1],
                 [-1, 0, 0.5, 0, 0, 0, 0, -1],
                 [-2, -1, -1, -0.5, -0.5, -1, -1, -2]]
buttom_R_pos_factor = [[0, 0, 0, 0, 0, 0, 0, 0],
                 [0.5, 1, 1, 1, 1, 1, 1, 0.5],
                 [-0.5, 0, 0, 0, 0, 0, 0, -0.5],
                 [-0.5, 0, 0, 0, 0, 0, 0, -0.5],
                 [-0.5, 0, 0, 0, 0, 0, 0, -0.5],
                 [-0.5, 0, 0, 0, 0, 0, 0, -0.5],
                 [-0.5, 0, 0, 0, 0, 0, 0, -0.5],
                 [0, 0, 0, 0.5, 0.5, 0, 0, 0]]
buttom_B_pos_factor = [[-2, -1, -1, -1, -1, -1, -1,-2],
                 [-1, 0, 0, 0, 0, 0, 0, -1],
                 [-1, 0, 0.5, 1, 1, 0.5, 0, -1],
                 [-1, 0.5, 0.5, 1, 1, 0.5, 0.5, -1],
                 [-1, 0, 1, 1, 1, 1, 0, -1],
                 [-1, 1, 1, 1, 1, 1, 1, -1],
                 [-1, 0.5, 0, 0, 0, 0, 0.5, -1],
                 [-2, -1, -1, -1, -1, -1, -1,-2]]
buttom_H_pos_factor = [[-5, -4, -3, -3, -3, -3, -4, -5],
                        [-4, -2, 0, 0, 0, 0, -2, -4],
                        [-3, 0, 1, 1.5, 1.5, 1, 0, -3],
                        [-3, 0.5, 1.5, 2, 2, 1.5, 0.5, -3],
                        [-3, 0, 1.5, 2, 2, 1.5, 0, -3],
                        [-3, 0.5, 1, 1.5, 1.5, 1 ,0.5, -3],
                        [-4, -2, 0, 0.5, 0.5, 0, -2, -4],
                        [-5, -4, -3, -3, -3, -3, -4, -5]]
buttom_P_pos_factor =[[0, 0, 0, 0, 0, 0, 0, 0],
                [5, 5, 5, 5, 5, 5, 5, 5],
                [1, 1, 2, 3, 3, 2, 1, 1,],
                [0.5, 0.5, 1, 2.5, 2.5, 1, 0.5, 0.5],
                [0, 0, 0, 2, 2, 0, 0, 0],
                [0.5, -0.5, -1, 0, 0, -1, 0.5, 0.5],
                [0.5, 1, 1, -2, -2, 1, 1, 0.5],
                [0, 0, 0, 0, 0, 0, 0, 0]]
POSITION_FACTOR = {'P':buttom_P_pos_factor, 'Q':buttom_Q_pos_factor, 'K':buttom_K_pos_factor,
                   'R':buttom_R_pos_factor, 'B':buttom_B_pos_factor, 'H':buttom_H_pos_factor}

## TextField Setting:
TF_WIDTH = 600
TF_HEIGHT = HEIGHT










