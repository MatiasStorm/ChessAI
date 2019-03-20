



class ChessEngine():
    def __init__(self, white_pos = "BUTTOM", black_pos = "TOP"):
        self.white_pos = white_pos
        self.black_pos = black_pos
        self.get_moves_dict = {"P":self.__get_pawn_moves}

    def __get_pawn_moves(self, board, pos, color):
        moves = []
        if color == "w":
            if pos[0] - 1 >= 0:
                if board[pos[0] - 1][pos[1]] == "":
                    moves.append((pos[0] - 1, pos[1]))
            if self.white_pos == "BUTTOM" and pos[0] == 6 and board[pos[0] - 2][pos[1]] == "":
                moves.append((pos[0] - 2, pos[1]))
        
        elif color == "b":
            if pos[0] + 1 <= 7:
                if board[pos[0] + 1][pos[1]] == "":
                    moves.append((pos[0] + 1, pos[1]))
            if self.black_pos == "TOP" and pos[0] == 1 and board[pos[0] + 2][pos[1]] == "":
                moves.append((pos[0] + 2, pos[1]))
        return moves
    
    def is_move_allowed(self, board, start_pos, end_pos):
        piece_str = board[start_pos[0]][start_pos[1]]
        color = piece_str[0]
        piece = piece_str[1]
        

    def get_allowed_moves(self, board, pos):
        piece = board[pos[0]][pos[1]]
        if piece != "":
            return self.get_moves_dict[piece[1]](board, pos, piece[0])
    
    def game_over(self, board):
        pass
    
    def p(self, t):
        print(t)


b = [["bR", "bH", "bB", "bQ", "bK", "bB", "bH", "bR"],
     ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
     ["", "", "", "", "", "", "", ""],
     ["", "", "", "", "", "", "", ""],
     ["", "", "", "", "", "", "", ""],
     ["", "", "", "", "", "", "", ""],
     ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
     ["wR", "wH", "wB", "wQ", "wK", "wB", "wH", "wR"]]
                     
e = ChessEngine()
pos = (2, 1)
print(e.get_allowed_moves(b, pos))  






