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
        while not self.board.end_game():
            move_str = input("Podaj Ruch A2B3")
            x_from, y_from, x_to, y_to = player.get_input(move_str)
            # if self.board.board[y_from][x_from].figure.color == "w":
            #     if player.string() != "1":
            #         print(f"Gracz " + player.string() + "może ruszyć tylko MAŁYMI")
            #         continue
            # if self.board.board[y_from][x_from].figure.color == "b":
            #     if player.string() != "2":
            #         print(f"Gracz " + player.string() + "może ruszyć tylko DUŻYMI")
            #         continue

            self.board.move(x_from, y_from, x_to, y_to)
            self.board.print()
            player.change_player()
            print(f"gracz >>" + player.string())
