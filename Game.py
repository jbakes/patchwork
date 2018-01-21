import Board
import Env
from copy import deepcopy


def make():
    return Env.Env()


class Game(object):
    
    def __init__(self, p1, p2):
        self.player_one = p1
        self.player_two = p2
        self.board = Board.Board()
        self.active_player = self.player_one
        self.inactive_player = self.player_two
        self.last_piece_played = None
        self.chatter = True

    def reset(self):
        self.player_one.reset()
        self.player_two.reset()
        self.active_player = self.player_one
        self.inactive_player = self.player_two
        self.board.reset()
    
    def game_over(self):
        return ( self.player_one.get_time_left() <= 0 and self.player_two.get_time_left() <= 0 ) 
    
    def alternate_turn(self):
        self.active_player, self.inactive_player = self.inactive_player, self.active_player
        if self.chatter:
            print('\nChange player: {}'.format(self.active_player.name))
    
    def get_market_piece(self, choice_ix):
        piece = self.board.market[choice_ix]
        return piece

    def is_player_active(self, player_name):
        return self.active_player.name == player_name

    def is_legal(self, choice_ix):
        # Check if the player can afford it
        piece = self.get_market_piece(choice_ix)
        if self.active_player.buttons >= piece.cost_buttons and self.active_player.empty_spaces >= piece.squares:
            return True
        else:
            return False
    
    def get_available_moves(self):
        legal_moves = [-1]
        for i in range(3):
            if self.is_legal(i):
                legal_moves.append(i)
        return legal_moves

    def earns_income(self, time_cost):
        """check if player crossed income"""
        for i in self.board.board_income:
            if self.active_player.location - time_cost < i < self.active_player.location:
                return True
        return False
        
    def earns_patch(self, time_cost):
        """check if player collects a patch"""
        for i in self.board.board_patches:
            if self.active_player.location - time_cost < i < self.active_player.location:
                self.board.board_patches.remove(i)
                return True
        return False

    def add_piece(self, piece):
        """Adds a piece to the player's quilt and updates the states
        """
        self.active_player.income += piece.buttons
        self.active_player.buttons -= piece.cost_buttons
        self.active_player.location += piece.cost_time
        self.active_player.empty_spaces -= piece.squares
        self.active_player.pieces_added.append(piece)

    def pass_turn(self, time):
        """Adjusts the player after a pass
        """
        self.active_player.buttons += time
        self.active_player.location += time

    def receive_income(self):
        """Gives the player his income"""
        self.active_player.buttons += self.active_player.income
    
    def make_move(self, choice_ix):
            if choice_ix == 3:
                self.board.print_whole_market()
            elif choice_ix == -1:
                self.select_pass()
            elif choice_ix >= 0 and self.is_legal(choice_ix):
                self.select_piece(choice_ix)
            else:
                print('illegal choice!')
                print('{} attempted to choose {}, but he only had {} buttons.'.format(self.active_player.name, self.get_market_piece(choice_ix).name, self.active_player.buttons))
                return 'ERROR'


    def select_piece(self, choice_ix):
        """Checks to see if the player receives an income or a patch and then adds a piece to the player's quilt
        player: the player adding the piece
        piece: the piece to be added to the quilt
        
        returns nothing.
        """
        piece = self.get_market_piece(choice_ix)
        self.last_piece_played = piece.name
        if self.chatter:
            print('{} adds the {} piece to his board.'.format(self.active_player.name, piece.name))
        self.add_piece(piece)
        self.board.remove_piece_from_market(choice_ix)

        if self.earns_income(piece.cost_time):
            self.receive_income()
        if self.earns_patch(piece.cost_time):
            if self.chatter:
                print( '{} is given a patch'.format(self.active_player.name) )
            self.add_piece(self.board.PATCH )
            self.active_player.pieces_added.append(self.board.PATCH)

        # check if turn changes
        if self.active_player.location > self.inactive_player.location:
            self.alternate_turn()
        return

    def select_pass(self):
        """Checks to see if the player receives an income or a patch and then moves the player as many passes as they need
        player: the player adding the piece
        other_player: the player who is being caught up to
        
        returns nothing.
        """
        self.last_piece_played = 'pass'

        if self.chatter:
            print('{} chooses to pass.'.format(self.active_player.name))
        pass_distance = min(self.board.LENGTH - 1, self.inactive_player.location) - self.active_player.location + 1
        self.pass_turn(pass_distance)
        if self.earns_income(pass_distance):
            self.receive_income()
        if self.earns_patch(pass_distance):
            if self.chatter:
                print( '{} is given a patch'.format(self.active_player.name))
            self.add_piece(self.board.PATCH)
            self.active_player.pieces_added.append(self.board.PATCH)

        # always change turns on a pass
        self.alternate_turn()
        return
    
    def run_game(self):
        turn = 0

        while not self.game_over():
            turn += 1
            print('\nTurn: {}'.format(turn))
            self.active_player.get_sm_status()
            self.inactive_player.get_sm_status()
            self.board.print_market(n=6)
            choice_ix = self.active_player.choose_move(deepcopy(self))
            self.make_move(choice_ix)

        print('+++++++++++++')
        print( '{} scored {}. {} scored {}'.format( self.player_one.name, self.player_one.get_score(), self.player_two.name, self.player_two.get_score() ))
        print( '{} wins by {}'.format( self.player_one.name, self.player_one.get_score() - self.player_two.get_score() ))





