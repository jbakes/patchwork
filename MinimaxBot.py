import Player
from copy import deepcopy

class MinimaxBot(Player.Player):
    def __init__(self, name='MmmBot', mm_depth=3):
        Player.Player.__init__(self, name)
        self.mm_depth = mm_depth
        print('Minimax depth set to {}'.format(self.mm_depth))
        self.solver = Minimax(self.name, self.mm_depth)

    def choose_move(self, game_state):
        move = self.solver.minimax(game_state, self.mm_depth)
        return move

class Minimax(object):
    """docstring for Minimax"""
    def __init__(self, caller_name, mm_depth):
        self.caller_name = caller_name
        self.mm_depth = mm_depth
        self.chatter = False
            
    def next_state(self, game, move):
        """Returns the next state of the game given a current state and a move.
        Keyword arguments:
        game -- the current state of the game
        move -- the move to apply
        """
        clone = deepcopy(game)
        clone.chatter = False
        clone.make_move(move)
        return clone

    def chat(self, text, how='print'):
        if self.chatter:
            if how=='print':
                print(text)

    def is_caller_active(self, game_state):
        return game_state.active_player.name == self.caller_name

    def evaluate(self, game_state):
        if self.is_caller_active(game_state):
            score = game_state.active_player.get_estimated_score(game_state, chatter=False) - game_state.inactive_player.get_estimated_score(game_state)
        else:
            score = game_state.inactive_player.get_estimated_score(game_state, chatter=False) - game_state.active_player.get_estimated_score(game_state)
        return score

    def minimax(self, game_state, depth):
        self.chat('Choice depth: {}'.format(depth))
        moves = game_state.get_available_moves()
        best_move = moves[0]
        best_score = float('-inf')
        for move in moves:
            clone = self.next_state(game_state, move)
            self.chat('My move: {}'.format(clone.last_piece_played))
            if self.is_caller_active(clone):
                score = self.max_play(clone, depth - 1)
            else:
                score = self.min_play(clone, depth - 1)
            self.chat('Move score: {}'.format(score))
            if score > best_score:
                best_move = move
                best_score = score
        print('Best score: {}'.format(best_score))
        return best_move

    def min_play(self, game_state, depth):
        if game_state.game_over() or depth <= 0:
            return self.evaluate(game_state)
        moves = game_state.get_available_moves()
        best_score = float('inf')
        for move in moves:
            clone = self.next_state(game_state, move)
            self.chat('{}Op move: {}'.format('  '*(self.mm_depth - depth), clone.last_piece_played))
            if self.is_caller_active(clone):
                score = self.max_play(clone, depth - 1)
            else:
                score = self.min_play(clone, depth - 1)
            self.chat('{}+ score: {}'.format('  '*(self.mm_depth - depth), score))
            if score < best_score:
                best_move = move
                best_score = score
        return best_score

    def max_play(self, game_state, depth):
        if game_state.game_over() or depth <= 0:
            return self.evaluate(game_state)
        moves = game_state.get_available_moves()
        best_score = float('-inf')
        for move in moves:
            clone = self.next_state(game_state, move)
            self.chat('{}My move: {}'.format('  '*(self.mm_depth - depth), clone.last_piece_played))
            if self.is_caller_active(clone):
                score = self.max_play(clone, depth - 1)
            else:
                score = self.min_play(clone, depth - 1)
            self.chat('{}+ score: {}'.format('  '*(self.mm_depth - depth), score))
            if score > best_score:
                best_move = move
                best_score = score
        return best_score

#http://giocc.com/concise-implementation-of-minimax-through-higher-order-functions.html