from figure import Figure


class Horse(Figure):
    def __init__(self, board, color):
        super().__init__(board, "H", color)

    def can_move(self, x_from, y_from, x_to, y_to):
        try:
            if x_from + 2 == x_to and y_from - 1 == y_to:
                return True
            elif x_from + 2 == x_to and y_from + 1 == y_to:
                return True
            elif x_from - 2 == x_to and y_from + 1 == y_to:
                return True
            elif x_from - 2 == x_to and y_from - 1 == y_to:
                return True
            elif x_from - 1 == x_to and y_from + 2 == y_to:
                return True
            elif x_from + 1 == x_to and y_from + 2 == y_to:
                return True
            elif x_from + 1 == x_to and y_from - 2 == y_to:
                return True
            elif x_from - 1 == x_to and y_from - 2 == y_to:
                return True
            else:
                return False
        except IndexError:
            print("index error na can move horse")
            return False
