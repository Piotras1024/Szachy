class Player:
    def __init__(self, player="1"):
        self.player = player

    def change_player(self):
        if self.player == "1":
            self.player = "2"
            return self.player
        self.player = "1"
        return self.player

    @staticmethod
    def get_input():
        abcd = ["A", "B", "C", "D", "E", "F", "G", "H"]
        digits = [abcd.index(digit) for digit in abcd]
        send = True
        while send:
            move_str = input("podaj A2, B3")
            if len(move_str) != 4:
                print("too long or too short answer AB23 ;)")
                continue

            x_from = move_str[0]
            y_from = move_str[1]
            x_to = move_str[2]
            y_to = move_str[3]
            if not y_from.isnumeric():
                print(f"Wrong Y FROM, second letter")
                continue
            if not y_to.isnumeric():
                print(f"Wrong Y TO, LAST LETTER (4)  [{ y_to}]")
                continue
            if not x_from.upper() in abcd:
                print(f"wrong X FROM, first letter  [{x_from}]")
                continue
            if not x_to.upper() in abcd:
                print(f"wrong X TO, second letter  [{x_to}]")
                continue
            if not int(move_str[1]) in digits:
                print(f"wrong Y FROM, third letter  [{y_from}]")
                continue

            send = False
            x_from = int(abcd.index(x_from.upper()))
            y_from = int(y_from) - 1
            x_to = int(abcd.index(x_to.upper()))
            y_to = int(y_to) - 1
            return x_from, y_from, x_to, y_to
