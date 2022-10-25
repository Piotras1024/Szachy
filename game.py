from board import Board
from pawn import Pawn
from turret import Turret


class Game:
    def __init__(self):
        self.board = Board()

    def run(self):
        self.board.board[0][0].figure = Pawn(self.board, "w")
        self.board.board[0][1].figure = Turret(self.board, "w")
        self.board.board[0][0].figure.move([0, 0, 2, 0])
        self.board.board[2][0].move([2, 0, 4, 0])
        self.board.move([4, 0, 6, 0])
        self.board.print()
