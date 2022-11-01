from board import Board
from pawn import Pawn
from player import Player


class Game:
    def __init__(self):
        self.board = Board()

    def run(self):
        player = Player("1")
        for x in range(8):
            self.board.board[1][x].figure = Pawn(self.board, "w")
            self.board.board[6][x].figure = Pawn(self.board, "b")
        self.board.print()

        while not self.board.end_game():
            print(f"Teraz Tura >> {player.player} << gracza")
            move_str = input("Podaj Ruch A2B3")
            x_from, y_from, x_to, y_to, send = player.get_input(move_str)
            if send:
                if self.board.board[y_from][x_from].figure is not None:
                    print("can_move >> ", self.board.board[y_from][x_from].figure.can_move(x_to, y_to, x_from, y_from))
                    if self.board.board[y_from][x_from].figure.can_move(x_to, y_to, x_from, y_from):
                        print("move accepted")
                        if self.board.move(x_from, y_from, x_to, y_to):
                            print("ruch poszedł")
                            self.board.print()
                            player.change_player()
                            send = False
