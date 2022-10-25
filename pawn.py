from figure import Figure


class Pawn(Figure):
    def __init__(self, board, color):
        super().__init__(board, "P", color)

    def can_move(self, x_to, y_to):
        #todo
        return True
