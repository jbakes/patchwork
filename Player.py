from random import randint

class Player(object):
    """Player class"""
    name = ''
    buttons = 5
    income = 0
    empty_spaces = 81
    location = 0
    
    def __init__(self, name):
        """Player creation
        name: name of the player
        """
        self.name = name

    def reset(self):
        self.buttons = 5
        self.income = 0
        self.empty_spaces = 81
        self.location = 0

    def get_time_left(self):
        return 53 - self.location
        
    def get_status(self):
        """Prints the status of the player"""
        print( 'Player: {}'.format(self.name))
        print( '\tbuttons: {}'.format(self.buttons))
        print( '\tincome: {}'.format(self.income))
        print( '\tempty spaces: {}'.format(self.empty_spaces))
        print( '\tlocation: {}'.format(self.location))
        print( '\ttime left: {}'.format(self.get_time_left()))
        
    def get_sm_status(self):
        """Prints the status of the player"""
        print( '*** {}: b:{}, i:{}, e:{}, loc:{}'.format(self.name, self.buttons, self.income, self.empty_spaces, self.location))
        
        
    def is_me(self, game):
        if game.active_player.name == self.name:
            return True
        else:
            return False

    def choose_move(self, board):
        """Asks the player for a move"""
        return 0

    def get_score(self, chatter = False):
        """Returns the current score if the game ended now"""
        score = max(0, self.empty_spaces) * -2
        score += self.buttons
        score += self.get_time_left()
        if chatter:
            print('Points from:')
            print('\tempty_spaces: {}'.format(self.empty_spaces * -2))
            print('\tbuttons: {}'.format(self.buttons))
            print('\ttime left: {}'.format(self.get_time_left()))
        return score
    
    def get_estimated_score(self, game_state, chatter = False):
        """Should estimeate a score based on time left, income remaining, and 1x1s with passing"""
        score = self.get_score(chatter)
        
        # count incomdes left
        inc_count = 0
        for inc in game_state.board.board_income:
            if self.location < inc:
                inc_count += 1
        score += self.income * inc_count
        if chatter:
            print('\tincomes remaining: {}'.format(inc_count))
            print('\tincome amount: {}'.format(self.income))
            print('\tincome value: {}'.format(self.income * inc_count))
            print('{}: estimated score is {}'.format(self.name, score))
        return score

    def get_legal_options(self, game):
        legal_moves = [-1]
        for i in range(3):
            if game.is_legal(i):
                legal_moves.append(i)
        return legal_moves

class HumanPlayer(Player):
    def __init__(self):
        Player.__init__(self, 'Human')
    
    def choose_move(self, game):
        game.board.print_market()
        print(self.get_legal_options(game))
        return int( input() )

class MaxBot(Player):
    def __init__(self, name='MaxBot'):
        Player.__init__(self, name)
    
    def choose_move(self,game):
        options = self.get_legal_options(game)
        print('{} has {} valid moves.'.format(self.name, len(options)))
        return max( options )

class RandomPlayer(Player):
    def __init__(self, name='RandomBot'):
        Player.__init__(self, name)
    
    def choose_move(self,game):
        options = self.get_legal_options(game)
        print('{} has {} valid moves.'.format(self.name, len(options)))
        rand_option = 0
        if len(options) > 1:
            rand_option = randint(1, len(options)-1)
        return options[rand_option]

class PassBot(Player):
    def __init__(self, name='PassBot'):
        Player.__init__(self, name)

    def choose_move(self,game):
        return -1