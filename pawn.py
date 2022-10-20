from figure import Figure


class Pawn(Figure):
    def __init__(self, board, color):
        super().__init__(board, "P", color)
