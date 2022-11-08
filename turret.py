from figure import Figure


class Turret(Figure):
    def __init__(self, board, color):
        super().__init__(board, "T", color)

    def can_move(self, x_from, y_from, x_to, y_to):
        try:
            if x_from == x_to and y_from != y_to:
                for i in range(1, abs(y_to - y_from)):
                    if self.board.board[y_from + (i * self.direction(y_from, y_to))][x_from].figure is not None:
                        return False
                return True
            elif y_from == y_to and x_from != x_to:
                for i in range(1, abs(x_to - x_from)):
                    if self.board.board[y_from][x_from + (i * self.direction(x_from, x_to))].figure is not None:
                        return False
                return True
            else:
                return False
        except IndexError:
            print("błędny ruch, wieża poza bordem")
            return False
