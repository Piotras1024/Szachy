class Figure:
    def __init__(self, board, sign, color):
        self.sign = sign
        self.color = color
        self.board = board

    def can_move(self, x_to, y_to):
        raise NotImplementedError

    def string(self):
        if self.color == "w":
            return self.sign
        elif self.color == "b":
            return self.sign.lower()
        raise NotImplementedError
