import time
from datetime import datetime
import json

class GameState:
    def __init__(self, players=None, numbers=None, time_started=None, time_saved=None):
        self.players = players if players is not None else []
        self.numbers = numbers if numbers is not None else []
        self.time_started = time.time()
        self.time_saved = None

    @classmethod
    def fromDict(self, data):
        players = data['players']
        numbers = data['numbers']
        time_started = data['time_started']
        time_saved = data['time_saved']
        gs = self(players, numbers, time_started, time_saved)
        return gs

    def add_player(self, player):
        self.players.append(player)

    def add_number(self, number):
        self.numbers.append(number)

    def save_state(self):
        self.time_saved = time.time()
        # save game state to file, database, or elsewhere

    def __str__(self):
        return f'GameState(players={self.players}, numbers={self.numbers}, time_started={self.time_started}, time_saved={self.time_saved})'

