from board import Board

class Game():
    def __init__(self):
        self.board = Board()

    def run(self):
        self.board.print()
