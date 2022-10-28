class Field:
    def __init__(self, x, y, figure=None):
        self.x = x
        self.y = y
        self.figure = figure

    def set_figure(self, figure):
        self.figure = figure
        return self.figure

    def move(self, another_field):
        if self.figure is None:
            print(f"na {self.x}, {self.y} nie ma figury")
            return False

        if not self.figure.can_move(another_field.x, another_field.x):
            print(f"Ruch nie mozliwy")
            return False

        another_field.figure = self.figure
        self.figure = None
        return True

    def string(self):
        if self.figure is None:
            return "_"
        return self.figure.string()
