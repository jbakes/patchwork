import Board

class Game(object):
    
    def __init__(self, p1, p2):
        self.player_one = p1
        self.player_two = p2
        self.board = Board.Board()
        
    def reset(self):
        self.player_one.reset()
        self.player_two.reset()
        self.board.reset()
    
    def game_over(self):
        return ( self.player_one.get_time_left() <= 0 and self.player_two.get_time_left() <= 0 ) 
    
    def get_market_piece(self, choice_ix):
        piece = self.board.market[choice_ix]
        return piece

    def is_legal(self, player, choice_ix):
        # Check if the player can afford it
        piece = self.get_market_piece(choice_ix)
        if player.buttons >= piece.cost_buttons and player.empty_spaces >= piece.squares:
            return True
        else:
            return False
    
    def earns_income(self, player, time_cost):
        """check if player crossed income"""
        for i in self.board.board_income:
            if player.location - time_cost < i < player.location:
                return True
        return False
        
    def earns_patch(self, player, time_cost):
        """check if player collects a patch"""
        for i in self.board.board_patches:
            if player.location - time_cost < i < player.location:
                self.board.board_patches.remove(i)
                return True
        return False

    def add_piece(self, player, piece):
        """Adds a piece to the player's quilt and updates the states
        """
        player.income += piece.buttons
        player.buttons -= piece.cost_buttons
        player.location += piece.cost_time
        player.empty_spaces -= piece.squares

    def pass_turn(self, player, time):
        """Adjusts the player after a pass
        """
        player.buttons += time
        player.location += time

    def receive_income(self, player):
        """Gives the player his income"""
        player.buttons += player.income
    
    def make_move(self, player, choice_ix):
        '''Checks to see if the player receives an income or a patch and then adds a piece to the player's quilt
        player: the player adding the piece
        piece: the piece to be added to the quilt
        
        returns nothing.
        '''
        piece = self.get_market_piece(choice_ix)
        print('{} adds the {} piece to his board.'.format(player.name, piece.name))
        self.add_piece(player, piece)
        self.board.remove_piece_from_market(choice_ix)

        if self.earns_income(player, piece.cost_time):
            self.receive_income(player)
        if self.earns_patch(player, piece.cost_time):
            print( '{} is given a patch'.format(player.name) )
            self.add_piece(player, self.board.PATCH )
        return

    def make_pass(self, player, other_player):
        '''Checks to see if the player receives an income or a patch and then moves the player as many passes as they need
        player: the player adding the piece
        other_player: the player who is being caught up to
        
        returns nothing.
        '''
        print('{} chooses to pass.'.format(player.name) )
        pass_distance = other_player.location - player.location + 1
        self.pass_turn(player, pass_distance)
        if self.earns_income(player, pass_distance):
            self.receive_income(player)
        if self.earns_patch(player, pass_distance):
            print( '{} is given a patch'.format(player.name) )
            self.add_piece(player, self.board.PATCH )
        return
    
    def run_game(self):
        active_player = self.player_one
        inactive_player = self.player_two
        
        turn = 0

        while not self.game_over():
            while active_player.location <= inactive_player.location and not self.game_over():
                turn += 1
                print('Turn: {}'.format(turn))
                choice_ix = active_player.choose_move(self)
                if choice_ix == 4:
                    return 'Complete'
                elif choice_ix == -1:
                    self.make_pass(active_player, inactive_player)
                elif choice_ix >= 0 and self.is_legal( active_player, choice_ix ):
                    self.make_move(active_player, choice_ix)
                else:
                    print('illegal choice!')
                    print('{} attempted to choose {}, but he only had {} buttons.'.format(active_player.name, self.get_market_piece(choice_ix).name, active_player.buttons))
                    return 'ERROR'
            print('STATUS:')
            active_player.get_sm_status()
            inactive_player.get_sm_status()
            print('\n')
            active_player, inactive_player = inactive_player, active_player
        print( '{} scored {}. {} scored {}'.format( active_player.name, active_player.get_score(), inactive_player.name, inactive_player.get_score() ))






