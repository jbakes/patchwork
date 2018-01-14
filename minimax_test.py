import Player

class JoelBot(Player.Player):
    def __init__(self, name='JoelBot'):
        Player.Player.__init__(self, name)

    
    def choose_move(self, game):
    	return -1

    def evaluate(self, game):
    	if self.name = game.player_one.name:
			return game.player_one.get_score() - game.player_two.get_score()
		else:
			return game.player_two.get_score() - game.player_one.get_score()

    def min_play(self, game):
		if game.game_over():
			return self.evaluate(game)
		return min(scores) # you are here



#    def get_min_max(me_player, other_player, game, depth):
#   	if depth == 0:
  		return (me_player.get_score() - other_player.get_score(), [-1]) # get_estimated_score? get_pass_score?
		# else:
		# 	if game.whose_turn() == me_player:
		# 		max_score = -1000
		# 		for i in game.get_options(me_player):
		# 			score, move_list = get_min_max(me_player, other_player, game.make_move(player, i, depth - 1))
		# 			if score > max_score:
		# 				max_score= score
		# 				max_move = i

		# 		return (max_score, max_move) #This doesn't return like below

#This is slick::
#'http://giocc.com/concise-implementation-of-minimax-through-higher-order-functions.html'


"""
The idea here is that get_min_max returns something like:
( best_score, 
	[
		( move_1, player_name ),
		( move_2, player_name ),
		...
		( move_depth, player_name )
	]
)

This is so that I can keep track of the move list even though I probably don't actually need this.
"""
'''
TODO:
	game.whose_turn()
	game.get_options(me_player)
	game.make_move(player, i)
'''