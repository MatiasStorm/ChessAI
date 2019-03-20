class ChessEngine():
    def __init__(self, white_pos = "BUTTOM", black_pos = "TOP"):
        self.white_pos = white_pos
        self.black_pos = black_pos
        self.get_moves_dict = {"P":self.__get_pawn_moves, "H":self.__get_knight_moves, "B":self.__get_bishop_moves,
                               "R":self.__get_rock_moves, "Q":self.__get_queen_moves, "K":self.__get_king_moves}

    def __get_pawn_moves(self, board, pos, color):
        moves = []
        if color == "w":
            if pos[0] - 1 >= 0:
                if board[pos[0] - 1][pos[1]] == "":
                    moves.append((pos[0] - 1, pos[1]))
            if self.white_pos == "BUTTOM" and pos[0] == 6 and board[pos[0] - 2][pos[1]] == "": # If pawn is at start position it can move to places.
                moves.append((pos[0] - 2, pos[1]))
        
        elif color == "b":
            if pos[0] + 1 <= 7:
                if board[pos[0] + 1][pos[1]] == "":
                    moves.append((pos[0] + 1, pos[1]))
            if self.black_pos == "TOP" and pos[0] == 1 and board[pos[0] + 2][pos[1]] == "": 
                moves.append((pos[0] + 2, pos[1]))
        return moves
    
    def __get_knight_moves(self, board, pos, color):
        steps =[[1, 2], [-1, 2], [2, -1], [2, 1], [1, -2], [-1, -2], [-2, 1], [-2, -1]]
        moves = []
        for step in steps:
            row = pos[0] + step[0]
            col = pos[1] + step[1]
            if 0 <= row <= 7 and 0 <= col <= 7 and color not in board[row][col]:
                moves.append((row, col))
        return moves
    
    def __get_directed_moves(self, board, pos, color, row_change, col_change):
        """
        Return all allowed moves in the direction specified by row_change and col_change, from pos.
        The first occurence of a piece of a different color on the directed path is also added to the allowed moves.
        """
        moves = []
        row, col = pos
        row += row_change
        col += col_change
        if 7 < row or row < 0 or col < 0 or col > 7:
            return moves
        while 0 <= row <= 7 and 0 <= col <= 7 and board[row][col] == "":
            moves.append((row, col))
            row += row_change
            col += col_change
        if 7 < row or row < 0 or col < 0 or col > 7:
            return moves
            
        if board[row][col][0] != color:
            moves.append((row, col))
        return moves
        
    def __get_bishop_moves(self, board, pos, color):
        moves = []
        moves += self.__get_directed_moves(board, pos, color, -1, -1) # NE
        moves += self.__get_directed_moves(board, pos, color, -1, 1) # NW
        moves += self.__get_directed_moves(board, pos, color, 1, -1) # SE
        moves += self.__get_directed_moves(board, pos, color, 1, 1) # SW
        return moves
    
    def __get_rock_moves(self, board, pos, color):
        moves = []
        moves += self.__get_directed_moves(board, pos, color, -1, 0) # N
        moves += self.__get_directed_moves(board, pos, color, 1, 0) # S
        moves += self.__get_directed_moves(board, pos, color, 0, -1) # E
        moves += self.__get_directed_moves(board, pos, color, 0, 1) # W
        return moves
    
    def __get_queen_moves(self, board, pos, color):
        moves = []
        moves += self.__get_rock_moves(board, pos, color) # All rock-like moves
        moves += self.__get_bishop_moves(board, pos, color) # All bishop-like moves
        return moves
    
    def __get_king_moves(self, board, pos, color):
        moves = []
        for r in range(-1, 2):
            for c in range(-1, 2):
                row = pos[0] + r
                col = pos[1] + c
                if (row, col) != pos and 0 <= row <= 7 and 0 <= col <= 7:
                    if board[row][col] == "":
                        moves.append((row, col))
                    elif board[row][col][0] != color:
                        moves.append((row, col))
        return moves
    
    def is_move_allowed(self, board, start_pos, end_pos):
        return end_pos in self.get_allowed_moves(board, start_pos)
        

    def get_allowed_moves(self, board, pos):
        piece = board[pos[0]][pos[1]]
        if piece != "":
            return self.get_moves_dict[piece[1]](board, pos, piece[0])
    
    def game_over(self, board):
        pass

# b = [["bR", "bH", "bB", "bQ", "bK", "bB", "bH", "bR"],
#      ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
#      ["", "", "", "", "", "", "", ""],
#      ["", "", "", "", "bB", "", "", ""],
#      ["", "", "", "", "", "", "", ""],
#      ["", "", "", "", "", "", "", ""],
#      ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
#      ["wR", "wH", "wB", "wQ", "wK", "wB", "wH", "wR"]]
# e = ChessEngine()
# e.get_allowed_moves(b, (3, 4))
 






