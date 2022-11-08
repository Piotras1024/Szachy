from figure import Figure


class Pawn(Figure):
    def __init__(self, board, color):
        self.direction = 1 if color == 'w' else -1
        super().__init__(board, "P", color)

    def can_move(self, x_from, y_from, x_to, y_to):
        try:
            # Jesli tam gdzie chcemy sie ruszyc jest puste
            if self.board.board[y_to][x_to].figure is None:
                # i ruszamy sie o jedno pole w dobrym kierunku
                if x_to == x_from:
                    if y_to == y_from + self.direction:
                        return True
                    # lub o dwa pola w dobrym kierunku. Sprawdzamy jeszcze pole posrednie czy nie ma tam pionka.
                    elif y_to == y_from + 2 * self.direction and self.board.board[y_from + self.direction][x_to].figure is None:
                        return True
            elif self.board.board[y_to][x_to].figure.color != self.color:
                if y_to == y_from + self.direction and x_to in (x_from - 1, x_from + 1):
                    return True
            return False
        except IndexError:
            print("błędny ruch, pion poza boardem")
            return False











            # else:
            #     if self.string() == "P":
            #         if x_to == x_from:
            #             if y_to == y_from + 1:
            #                 return True
            #     elif self.string() == "p":
            #         if x_to == x_from:
            #             if y_to == y_from - 1:
            #                 return True
            #     else:
            #         return False
        # else:
        #     print("x to y to jest puste ? y from musi byc 3 lub 6, wtedy o 2 pole moze sie pion ruszyć, reszta to o 1 pole")
        #     return False
