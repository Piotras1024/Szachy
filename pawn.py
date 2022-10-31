from figure import Figure


class Pawn(Figure):
    def __init__(self, board, color):
        super().__init__(board, "P", color)

    def can_move(self, x_to, y_to, x_from, y_from):
        print(x_to, y_to, x_from, y_from)   # 0 , 3, 0, 1 >>A2A4
        try:
            if self.board.board[y_to][x_to].figure is None:
                if y_from == 1 or y_from == 6:
                    if self.color == "b" and x_to == x_from:
                        if y_to == y_from - 1 or y_to == y_from - 2:
                            return True
                        return False
                    if self.color == "w" and x_to == x_from:
                        if y_to == y_from + 1 or y_to == y_from + 2:
                            return True
                        return False
                    return False
                else:
                    if self.color == "b" and x_to == x_from:                    #todo
                        if y_to == y_from - 1 or y_to == y_from - 2:
                            return True
                        return False
                    if self.color == "w" and x_to == x_from:
                        if y_to == y_from + 1 or y_to == y_from + 2:
                            return True
                        return False
                    return False
            elif self.board.board[y_to+1][x_to-1].figure is not None:   #bicie malymi na ukos w lewo
                return True
            elif self.board.board[y_to+1][x_to+1].figure is not None:   #bicie malymi na ukos w prawo
                return True
            elif self.board.board[y_to-1][x_to+1].figure is not None:   #bicie duzymi na ukos w lewo
                return True
            elif self.board.board[y_to+1][x_to-1].figure is not None:   #bicie duzymi na ukos w prawo
                return True
            else:
                return False
        except IndexError:
            print("błędny ruch")
            return False











            # else:
            #     if self.string() == "P":
            #         if x_to == x_from:
            #             if y_to == y_from + 1:
            #                 return True
            #     elif self.string() == "p":
            #         if x_to == x_from:
            #             if y_to == y_from - 1:
            #                 return True
            #     else:
            #         return False
        # else:
        #     print("x to y to jest puste ? y from musi byc 3 lub 6, wtedy o 2 pole moze sie pion ruszyć, reszta to o 1 pole")
        #     return False
