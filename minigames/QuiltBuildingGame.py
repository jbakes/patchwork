QUILT_LENGTH = 9

quilt_coordinates = zip(range(QUILT_LENGTH), range(QUILT_LENGTH))


def empty_quilt():
    quilt = {}
    for quilt_coord_x in range(QUILT_LENGTH):
        for quilt_coord_y in range(QUILT_LENGTH):
            quilt = {(quilt_coord_x, quilt_coord_y): 0}
    return quilt

def initial_market():
    pieces = get_pieces()
    return pieces


def get_pieces():
    pieces = []
    pieces.append(Piece('cross', {(0, 1): 1}))


class Piece(object):
    def __init__(name, shape, self):
        self.name = name
        self.shape = shape

    def squares(self):
        return len(self.shape.keys())



class QuiltBuildingMiniGameEnv:
    """In the Quilt Building Mini-Game (for 1 player, ages 4 and up), the player receives one piece at
        a time, randomly, from the market and must place it in their grid, or forfeit the piece.
        The game is over when the market is empty.  The player is penalized one point for each uncovered square.
    """
    player_quilt = empty_quilt()
    market = initial_market()

    def init(self):
        return self.game

    def step(self):
        return self.game


def make():
    quilt_env = None
    return quilt_env

