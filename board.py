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
            print(f"{i} |" + f"|".join(map(lambda x: "_", self.board[y])) + "|" + f" {i}")
            i = i + 1
        print("   " + " ".join(abcd))
