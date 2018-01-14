class Piece(object):
    name = ''
    squares = 0
    buttons = 0
    cost_buttons = 0
    cost_time = 0

    def __init__(self, name, squares, buttons, cost_buttons, cost_time):
        self.name = name
        self.squares = squares
        self.buttons = buttons
        self.cost_buttons = cost_buttons
        self.cost_time = cost_time