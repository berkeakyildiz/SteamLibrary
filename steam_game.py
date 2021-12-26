import json

import requests


class SteamGame:
    def __init__(self, game_id, name, hours_played):
        self.game_id = game_id
        self.name = name
        self.hours_played = float(hours_played)

    def __repr__(self):
        return 'Steam Game ID: ' + self.game_id + ' Game Name: ' + self.name + ' ' + str(self.hours_played) + ' hours played'
