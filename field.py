
class Field:
    def __init__(self, x, y, figure=None):
        self.x = x
        self.y = y
        self.figure = figure

    def set_figure(self, figure):
        self.figure = figure
        return self.figure

    def string(self):
        if self.figure is None:
            return "_"
        return self.figure.string()

