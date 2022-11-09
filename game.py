from board import Board
from pawn import Pawn
from player import Player
from turret import Turret
from bishop import Bishop
from horse import Horse
from queen import Queen
from king import King

class Game:
    def __init__(self):
        self.board = Board()

    def run(self):
        player = Player("1")
        for x in range(8):
            self.board.board[1][x].figure = Pawn(self.board, "w")
            self.board.board[6][x].figure = Pawn(self.board, "b")
        self.board.board[7][7].figure = Turret(self.board, "b")
        self.board.board[7][0].figure = Turret(self.board, "b")
        self.board.board[0][7].figure = Turret(self.board, "w")
        self.board.board[0][0].figure = Turret(self.board, "w")         #todo turret stay in bad spot, because of function win_game is in proces of build
        self.board.board[0][5].figure = Bishop(self.board, "w")
        self.board.board[0][2].figure = Bishop(self.board, "w")
        self.board.board[7][5].figure = Bishop(self.board, "b")
        self.board.board[7][2].figure = Bishop(self.board, "b")
        self.board.board[0][1].figure = Horse(self.board, "w")
        self.board.board[0][6].figure = Horse(self.board, "w")
        self.board.board[7][1].figure = Horse(self.board, "b")
        self.board.board[7][6].figure = Horse(self.board, "b")
        self.board.board[0][3].figure = Queen(self.board, "w")
        self.board.board[7][3].figure = Queen(self.board, "b")
        self.board.board[7][4].figure = King(self.board, "b")
        self.board.board[0][4].figure = King(self.board, "w")

        while not self.board.end_game():
            print(f"Teraz Tura >> {player.player} << gracza")
            self.board.print()
            move_str = input("Podaj Ruch A2B3")
            x_from, y_from, x_to, y_to, send = player.get_input(move_str)
            if self.board.board[y_from][x_from].figure is not None:
                if self.board.board[y_from][x_from].figure.can_move(x_from, y_from, x_to, y_to):
                    print("move accepted")
                    if self.board.move(x_from, y_from, x_to, y_to):
                        print("ruch poszedł")
                        player.change_player()
                    else:
                        print("move nie przeszedl")
                else:
                    print("can move nie przeszedł")
            else:
                print("Pierwsze współrzędne muszą podawać miejsce z Twoją Figurą")
        player.change_player()
        print(f" WYGRAŁ GRACZ nr {player.player}\n GRATULACJE :) ")

