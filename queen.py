from figure import Figure


class Queen(Figure):
    def __init__(self, board, color):
        super().__init__(board, "Q", color)             #czemu samo podpowiada wpisanie Quen do środka itp?

    def can_move(self, x_from, y_from, x_to, y_to):
        try:
            dir_y = self.direction(y_from, y_to)
            dir_x = self.direction(x_from, x_to)
            if x_from - x_to == y_from - y_to:
                for i in range(1, abs(x_from - x_to)):
                    if self.board.board[y_from + i * dir_y][x_from + i * dir_x].figure is not None:
                        return False
                return True
            elif (x_from - x_to) * (-1) == y_from - y_to:
                for i in range(1, abs(x_from - x_to)):
                    if self.board.board[y_from + i * dir_y][x_from + i * dir_x].figure is not None:
                        return False
                return True
            elif x_from == x_to and y_from != y_to:
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
            print("błędny ruch, queen poza boardem")
            return False
