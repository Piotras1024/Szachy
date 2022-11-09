from field import Field


class Board:
    def __init__(self):
        self.board = self.clean_board()

    def clean_board(self):
        abcd = ["A", "B", "C", "D", "E", "F", "G", "H"]
        print(i for i in abcd)
        #self.board = [[f"[{y},{x}]" for x in abcd] for y in range(len(abcd))]
        self.board = [[Field(x, y) for x in range(8)] for y in range(8)]
        return self.board

    def print(self):
        i = 1
        abcd = ["A", "B", "C", "D", "E", "F", "G", "H"]
        print("   " + " ".join(abcd))
        for y in range(8):
            print(f"{i} |" + f"|".join(map(lambda field: field.string(), self.board[y])) + "|" + f" {i}")
            i = i + 1
        print("   " + " ".join(abcd))

    def move(self, x_from, y_from, x_to, y_to):
        # return self.board[y_from][x_from].move(x_from, y_from, x_to, y_to)
        field_from = self.board[y_from][x_from]
        field_to = self.board[y_to][x_to]
        return field_from.move(field_to)

    def string_of_figures(self):
        tab_of_figures = []
        for y in range(8):
            figures = f"|".join(map(lambda field: field.string(), self.board[y]))
            tab_of_figures.append(figures)
        string_of_figures = "|".join(tab_of_figures)
        return string_of_figures

    def end_game(self):
        if self.string_of_figures().find("k") == -1:
            return True
        elif self.string_of_figures().find("K") == -1:
            return True
        else:
            return False
