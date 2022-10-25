class Figure:
    def __init__(self, board, sign, color):
        self.sign = sign
        self.color = color
        self.board = board

    def move(self, move_str):
        self.board.board[move_str[2]][move_str[3]].figure = self.board.board[move_str[0]][move_str[1]].figure
        self.board.board[move_str[0]][move_str[1]].figure = None
        return self.board.board[2][3].figure

    def string(self):
        if self.color == "w":
            return self.sign
        elif self.color == "b":
            return self.sign.lower()
        raise NotImplementedError
