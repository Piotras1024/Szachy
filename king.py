from figure import Figure


class King(Figure):
    def __init__(self, board, color):
        super().__init__(board, "K", color)

    def can_move(self, x_from, y_from, x_to, y_to):
        try:
            if x_from - 1 == x_to and y_from - 1 == y_to:
                return True
            elif x_from - 1 == x_to and y_from == y_to:
                return True
            elif x_from - 1 == x_to and y_from + 1 == y_to:
                return True
            elif x_from == x_to and y_from - 1 == y_to:
                return True
            elif x_from == x_to and y_from + 1 == y_to:
                return True
            elif x_from + 1 == x_to and y_from - 1 == y_to:
                return True
            elif x_from + 1 == x_to and y_from == y_to:
                return True
            elif x_from + 1 == x_to and y_from + 1 == y_to:
                return True
            else:
                return False
        except IndexError:
            print("błędny ruch, queen poza boardem")
            return False