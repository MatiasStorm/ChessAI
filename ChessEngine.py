from Settings import *


class ChessEngine():
    def __init__(self):
        self.get_moves_dict = {"P":self.__get_pawn_moves, "H":self.__get_knight_moves, "B":self.__get_bishop_moves,
                               "R":self.__get_rock_moves, "Q":self.__get_queen_moves, "K":self.__get_king_moves}
        
    def __get_pawn_moves(self, board, pos, color):
        moves_dict = {}
        moves_dict["M"] = [] # M for moves   
        moves_dict["P"] = [] # P for protect, can protect a piece so the king cannot seize it
        moves_dict["K"] = [] # K, places where the oppsite king cannot move to (only used when finding the kings allowed moves)
        
        if color == "w":
            direction = -1;
            final_row = 0;
            start_row = 6;
            opp_col = "b";
        elif color == "b":
            direction = 1;
            final_row = 7;
            start_row = 1;
            opp_col = "w";
            
        row = pos[0];
        col = pos[1];
        if 0 < row < 7: # Pawn cannot move if it is in the top or bottom of the board.
            if board[row + direction][col] == "..": # Strait ahead
                moves_dict["M"].append((row + direction, col))
            if pos[1] < 7:
                if opp_col in board[row + direction][col + 1]: # Right diagonal
                    moves_dict["M"].append((row + direction, col + 1))
                elif color in board[row + direction][col + 1]:
                    moves_dict["P"].append((row + direction, col + 1))
                else:
                    moves_dict["K"].append((row + direction, col + 1))
            if pos[1] > 0:
                if opp_col in board[row + direction][col - 1]: # Left diagonal,
                    moves_dict["M"].append((row + direction, col - 1))
                elif color in board[row - 1][col - 1]: # Left diagonal
                    moves_dict["P"].append((row + direction, col - 1))
                else:
                    moves_dict["K"].append((row + direction, col - 1))
                
        if row == start_row: # If pawn is at start position it can move two steps ahead.
            if board[row + (2 * direction)][col] == ".." and board[row + direction][col] == "..": 
                moves_dict["M"].append((row + (2 * direction), col))
                
        return moves_dict
    
    def __get_knight_moves(self, board, pos, color):
        steps =[[1, 2], [-1, 2], [2, -1], [2, 1], [1, -2], [-1, -2], [-2, 1], [-2, -1]]
        moves_dict = {}
        moves_dict["M"] = []
        moves_dict["P"] = []
        for step in steps:
            row = pos[0] + step[0]
            col = pos[1] + step[1]
            if 0 <= row <= 7 and 0 <= col <= 7 and color not in board[row][col]:
                if color not in board[row][col]:
                    moves_dict["M"].append((row, col))
                else:
                    moves_dict["P"].append((row, col))
        return moves_dict
    
    def __get_directed_moves(self, board, pos, color, row_change, col_change):
        """
            Return all allowed moves in the direction specified by row_change and col_change, from pos.
            The first occurence of a different colored piece on the directed path is also added to the allowed moves.
        """
        moves_dict = {}
        moves_dict["M"] = []
        moves_dict["P"] = []
        row, col = pos
        row += row_change
        col += col_change
        if 7 < row or row < 0 or col < 0 or col > 7:
            return moves_dict
        while 0 <= row <= 7 and 0 <= col <= 7 and board[row][col] == "..":
            moves_dict["M"].append((row, col))
            row += row_change
            col += col_change
        if 7 < row or row < 0 or col < 0 or col > 7:
            return moves_dict
        
        # Last move
        if board[row][col][0] != color:
            moves_dict["M"].append((row, col))
        elif board[row][col][0] == color:
            moves_dict["P"].append((row, col))
            
        return moves_dict
        
    def __get_bishop_moves(self, board, pos, color):
        moves_dict = {}
        moves_dict["M"] = []
        moves_dict["P"] = []
        for i in [-1, 1]:
            for j in [-1, 1]:
                diagonal_moves = self.__get_directed_moves(board, pos, color, i, j)
                moves_dict["M"] += diagonal_moves["M"]
                moves_dict["P"] += diagonal_moves["P"]
        return moves_dict
    
    def __get_rock_moves(self, board, pos, color):
        moves_dict = {}
        moves_dict["M"] = []
        moves_dict["P"] = []
        for dir in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                moves = self.__get_directed_moves(board, pos, color, dir[0], dir[1])
                moves_dict["M"] += moves["M"]
                moves_dict["P"] += moves["P"]
        return moves_dict
    
    def __get_queen_moves(self, board, pos, color):
        moves_dict = {}
        moves_dict["M"] = []
        moves_dict["P"] = []
        rock_moves = self.__get_rock_moves(board, pos, color)
        moves_dict["M"] += rock_moves["M"]
        moves_dict["P"] += rock_moves["P"]
        bishop_moves = self.__get_bishop_moves(board, pos, color)
        moves_dict["M"] += bishop_moves["M"]
        moves_dict["P"] += bishop_moves["P"]
        return moves_dict
    
    def __get_king_moves(self, board, pos, color):
        moves_dict = {}
        moves_dict["M"] = []
        moves_dict["P"] = []
        for r in range(-1, 2):
            for c in range(-1, 2):
                row = pos[0] + r
                col = pos[1] + c
                if (row, col) != pos and 0 <= row <= 7 and 0 <= col <= 7:
                    if board[row][col] == ".." and (row, col):
                        moves_dict["M"].append((row, col))
                    elif board[row][col][0] != color and (row, col):
                        moves_dict["M"].append((row, col))
                    else:
                        moves_dict["P"].append((row, col))
        if color == 'w': # Restict moves to avoid check
            for move in moves_dict["M"].copy():
                new_board = [x[:] for x in board]
                self.move(new_board, pos, move)
                if self.check(new_board, color):
                    moves_dict["M"].remove(move)
        return moves_dict
    
    def is_move_allowed(self, board, start_pos, end_pos):
        return end_pos in self.get_allowed_moves(board, start_pos)["M"]
        
    def get_allowed_moves(self, board, pos):
        """
            returns a list of tuples [(end_row, end_col),...]
        """
        piece = board[pos[0]][pos[1]]
        if piece != "..":
            color = piece[0]
            return (self.get_moves_dict[piece[1]](board, pos, color))
    
    def get_all_moves_list(self, board, color):
        """
            Returns a list of all allowed moves of the given color.
        """
        all_moves = []
        for r in range(len(board)):
            for c in range(len(board[r])):
                if color in board[r][c]:
                    pos = (r, c)
                    moves_dict = self.get_allowed_moves(board, pos)
                    if "P" in board[r][c]:
                        all_moves += moves_dict["P"]
                        all_moves += moves_dict["K"]
                    else:
                        all_moves += moves_dict["M"]
                        all_moves += moves_dict["P"]
        return all_moves
    
    def get_all_moves_dict(self, board, color):
        """
            Finds all allowed moves of the given color.
            Returns a dictonary:
                {(start_row, start_col):[(end_row1, end_col1),...],...}
                Key: The position of the piece
                Value: List of tuples (row, col) of all the allowed moves.
        """
        moves_dict = {}
        for r in range(len(board)):
            for c in range(len(board[r])):
                if color in board[r][c]:
                    pos = (r, c)
                    moves = self.get_allowed_moves(board, pos)["M"]
                    if moves: 
                        moves_dict[pos] = moves
        return moves_dict
    
    def get_king_pos(self, board, color):
        king_pos = ()
        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == color + 'K':
                    king_pos = (r, c)
                    break
        return king_pos
    
    def check(self, board, color):
        king_pos = self.get_king_pos(board, color)
        if not king_pos: return True
        opposite_color_moves = self.get_all_moves_list(board, 'b' if color == 'w' else 'w')
        if king_pos in opposite_color_moves:
            return True
        return False
    
    def check_mate(self, board, color):
        opposite_color_moves = self.get_all_moves_dict(board, color)
        for start in opposite_color_moves:
            for end in opposite_color_moves[start]:
                new_board = [x[:] for x in board]
                self.move(new_board, start, end)
                if not self.check(new_board, color):
                    return False
        return True        
    
    def board_score(self, board, color):
        score_dict = {"P":10, "B":30, "H":30, "R":50, "Q":90, "K":900}
        score = 0
        for r in range(len(board)):
            for c in range(len(board[r])):
                piece = board[r][c]
                if "w" in piece:
                    score -= score_dict[piece[1]] 
                elif 'b' in piece:
                    score += score_dict[piece[1]] 
        return score
                
    def move(self, board, start_pos, end_pos):
        piece = board[start_pos[0]][start_pos[1]]
        board[end_pos[0]][end_pos[1]] = piece
        board[start_pos[0]][start_pos[1]] = ".."

    def print_board(self, b):
        for row in b:
            print(row)
            


# Debuggin code            
# b = [["wP", "..", "bB", "bQ", "bK", "bB", "bH", "bR"],
#      ["..", "wP", "bP", "bP", "..", "bP", "bP", "bP"],
#      ["..", "wP", "..", "wP", "..", "..", "..", ".."],
#      ["..", "..", "..", "..", "..", "..", "..", ".."],
#      ["bR", "..", "..", "..", "..", "..", "..", ".."],
#      ["..", "..", "..", "..", "..", "..", "..", ".."],
#      ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
#      ["bP", "wH", "wB", "wQ", "..", "wB", "wH", "wR"]]
# e = ChessEngine()
# print(e.get_allowed_moves(b, (1,1)))
# print(e.get_allowed_moves(b, (7,0)))

