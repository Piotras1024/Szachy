from board import Board
from pawn import Pawn
class Game():
    def __init__(self):
        self.board = Board()

    def run(self):
        self.board.board[1][1].set_figure(Pawn(self.board, "w"))
        self.board.board[3][1].set_figure(Pawn(self.board, "b"))
        self.board.print()

