from board import Board
from pawn import Pawn
from player import Player
from turret import Turret


class Game:
    def __init__(self):
        self.board = Board()

    def run(self):
        player = Player("1")
        for x in range(8):
            self.board.board[1][x].figure = Pawn(self.board, "w")
            self.board.board[6][x].figure = Pawn(self.board, "b")
        self.board.print()
        x_from, y_from, x_to, y_to = player.get_input()
        self.board.move(x_from, y_from, x_to, y_to)
        self.board.print()
