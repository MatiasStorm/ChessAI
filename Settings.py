
# Colors:
BLACK = (0,0,0)
WHITE = (255, 255, 255)
DARKGREY = (30, 30, 30)
LIGHTGREY = (225, 225, 225)
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
STARTING_PIECE_MATRIX = [["..", "..", "..", "..", "..", "..", "..", ".."],
                         ["wP", "wP", "wP", "..", "..", "..", "..", ".."],
                         ["..", "..", "..", "..", "..", "..", "bK", ".."],
                         ["..", "..", "..", "..", "..", "..", "..", ".."],
                         ["..", "..", "..", "..", "..", "..", "..", ".."],
                         ["..", "..", "..", "..", "..", "..", "..", ".."],
                         ["..", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
                         ["wR", "wH", "wB", "wK", "wQ", "wB", "wH", "wR"]]
# STARTING_PIECE_MATRIX = [["bR", "bH", "bB", "bK", "bQ", "bB", "bH", "bR"],
#                          ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
#                          ["..", "..", "..", "..", "..", "..", "..", ".."],
#                          ["..", "..", "..", "..", "..", "..", "..", ".."],
#                          ["..", "..", "..", "..", "..", "..", "..", ".."],
#                          ["..", "..", "..", "..", "..", "..", "..", ".."],
#                          ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
#                          ["wR", "wH", "wB", "wK", "wQ", "wB", "wH", "wR"]]

IMAGE_FOLDER = "Images"
IMAGE_FILE_DICT = {"bR":IMAGE_FOLDER + "/b_rock.png",  "bH":IMAGE_FOLDER + "/b_knight.png",
                    "bB":IMAGE_FOLDER + "/b_bishop.png","bQ":IMAGE_FOLDER + "/b_queen.png",
                    "bK":IMAGE_FOLDER + "/b_king.png",  "bP":IMAGE_FOLDER + "/b_pawn.png",
                    "wR":IMAGE_FOLDER + "/w_rock.png",  "wH":IMAGE_FOLDER + "/w_knight.png",
                    "wB":IMAGE_FOLDER + "/w_bishop.png","wQ":IMAGE_FOLDER + "/w_queen.png",
                    "wK":IMAGE_FOLDER + "/w_king.png",  "wP":IMAGE_FOLDER + "/w_pawn.png"}
# IMAGE_FILE_DICT = {"bR":IMAGE_FOLDER + "\\b_rock.PNG",  "bH":IMAGE_FOLDER + "\\b_knight.PNG",
#                     "bB":IMAGE_FOLDER + "\\b_bishop.PNG","bQ":IMAGE_FOLDER + "\\b_queen.PNG",
#                     "bK":IMAGE_FOLDER + "\\b_king.PNG",  "bP":IMAGE_FOLDER + "\\b_pawn.PNG",
#                     "wR":IMAGE_FOLDER + "\\w_rock.PNG",  "wH":IMAGE_FOLDER + "\\w_knight.PNG",
#                     "wB":IMAGE_FOLDER + "\\w_bishop.PNG","wQ":IMAGE_FOLDER + "\\w_queen.PNG",
#                     "wK":IMAGE_FOLDER + "\\w_king.PNG",  "wP":IMAGE_FOLDER + "\\w_pawn.PNG"}
CHAR_TO_STR = {'K':"King", 'B': "Bishop", "Q":"Queen", "R":"Rock", "P":"Pawn", "H": "Knight"}


# BoardCanvas Settings:
TILESIZE = 75
MARGIN = 25
BOARD_CANVAS_COLORS = [BURLYWOOD, SADDLEBROWN]
BOARD_CANVAS_CHARS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

## TextField Setting:
TF_WIDTH = 600
TF_HEIGHT = HEIGHT

# AI settings:
MAX_SEARCH_DEPTH = 5
