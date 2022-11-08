from figure import Figure

class Bishop(Figure):
    def __init__(self, board, color):
        super().__init__(board, "B", color)

    def can_move(self, x_from, y_from, x_to, y_to):
        try:
            dir_y = self.direction(y_from, y_to)
            dir_x = self.direction(x_from, x_to)
            if x_from - x_to == y_from - y_to:
                for i in range(1, abs(x_from-x_to)):
                    if self.board.board[y_from + i * dir_y][x_from + i * dir_x].figure is not None:
                        return False
                return True
            elif (x_from - x_to) * (-1) == y_from - y_to:
                for i in range(1, abs(x_from-x_to)):
                    if self.board.board[y_from + i * dir_y][x_from + i * dir_x].figure is not None:
                        return False
                return True
            else:
                return False
        except IndexError:
            print("błędny ruch, bishop poza boardem")
            return False
