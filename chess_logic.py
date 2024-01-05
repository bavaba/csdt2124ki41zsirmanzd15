import chess


class ChessGame:
    def __init__(self):
        self.board = chess.Board()

    def make_move(self, move):
        try:
            chess_move = self.board.parse_san(move)
            self.board.push(chess_move)
            return True
        except ValueError:
            return False

    def is_game_over(self):
        return self.board.is_game_over()
