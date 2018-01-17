import Game
import Player
import gym.spaces as spaces

action_space = spaces.Discrete(4)
observation_space = spaces.Dict({
    "active_b": spaces.Discrete(256), 
    "active_i": spaces.Discrete(256), 
    "active_e": spaces.Discrete(81), 
    "active_l": spaces.Discrete(256),
    "inactive_b": spaces.Discrete(256),
    "inactive_i": spaces.Discrete(256),
    "inactive_e": spaces.Discrete(81),
    "inactive_l": spaces.Discrete(256)
})


class Env(object):
    def __init__(self):
        self.playerState1 = Player.HumanPlayer()
        self.playerState1.name = "Player 1"
        self.playerState2 = Player.HumanPlayer()
        self.playerState2.name = "Player 2"
        self.game = Game.Game(self.playerState1, self.playerState2)
        self.game.active_player = self.playerState1
        self.game.inactive_player = self.playerState2

    def step(self, action):
        obs, reward, done, info = None, None, False, None
        score_init = self.game.active_player.get_score()

        if action == 4:
            return 'Complete'
        elif action == -1:
            self.game.make_pass()
        elif action >= 0 and self.game.is_legal(action):
            self.game.make_move(action)
        else:
            print('illegal choice!')
            print('{} attempted to choose {}, but he only had {} buttons.'.format(
                self.game.active_player.name,
                self.game.get_market_piece(action).name,
                self.game.active_player.buttons))
            return 'ERROR'
        self.game.active_player, self.game.inactive_player = self.game.inactive_player, self.game.active_player

        obs_dict = {}
        for k, v in self.game.active_player.get_status_map().items():
            obs_dict["active_{}".format(k)] = v
        for k, v in self.game.inactive_player.get_status_map().items():
            obs_dict["inactive_{}".format(k)] = v
        obs = spaces.Dict(obs_dict)
        
        reward = self.game.active_player.get_score() - score_init
        done = self.game.game_over()

        return obs, reward, done, info


