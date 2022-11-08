class Figure:
    def __init__(self, board, sign, color):
        self.sign = sign
        self.color = color
        self.board = board

    def can_move(self, x_from, y_from, x_to, y_to):
        raise NotImplementedError

    def string(self):
        if self.color == "w":
            return self.sign
        elif self.color == "b":
            return self.sign.lower()
        raise NotImplementedError

    @staticmethod
    def direction(figure_from=int, figure_to=int):
        ## podaje kierunek zmiany
        if figure_to - figure_from > 0:
            direction = 1
            return direction
        elif figure_to - figure_from < 0:
            direction = -1
            return direction
        else:
            return -99999
