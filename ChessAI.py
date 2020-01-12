from ChessEngine import ChessEngine

class ChessAI():
    def __init__(self, max_depth):
        self.color = "b"
        self.max_depth = max_depth
        self.engine = ChessEngine()

    def search(self, board, alfa, beta, is_maximizer=True, depth=0, is_root=True, N_C = [0, 0]):
        """
            returns a tuple containing: (start_pos, end_pos, score, visited_nodes)
        """
        # Beta is the minimizing players value
        # alfa is the maximizing player value.
        N_C[0] += 1
        if depth >= self.max_depth:
            return self.engine.board_score(board, self.color)
        elif is_maximizer:
            moves = self.engine.get_all_moves_dict(board, self.color)
            best_score = -0.1
            for start_pos in moves:
                for end_pos in moves[start_pos]:
                    board_with_move = [row[:] for row in board]
                    self.engine.move(board_with_move, start_pos, end_pos)
                    score = self.search(board_with_move, alfa, beta, is_maximizer=False, depth=depth + 1, is_root=False, N_C=N_C)
                    alfa = max(alfa, best_score)
                    if alfa >= beta:
                        N_C[1] += 1
                        return best_score
                    if best_score == -0.1 or score > best_score:
                        best_move = end_pos
                        best_score = score
                        result = (start_pos, end_pos, best_score, N_C)
            if is_root:
                return result
            return best_score
        else:
            moves = self.engine.get_all_moves_dict(board, 'w' if self.color == 'b' else 'b')
            best_score = 99999999
            for start_pos in moves:
                for end_pos in moves[start_pos]:
                    board_with_move = [row[:] for row in board]
                    self.engine.move(board_with_move, start_pos, end_pos)
                    best_score = min(best_score, self.search(board_with_move, alfa, beta, is_maximizer=True, depth=depth + 1, is_root=False, N_C=N_C))
                    beta = min(beta, best_score)
                    if alfa >= beta:
                        N_C[1] += 1
                        return best_score
            return best_score
