class SteamGame:
    def __init__(self, game_id, name, hours_played):
        self.game_id = game_id
        self.name = name
        self.hours_played = float(hours_played)
        self.total_achievement_count = 0
        self.completed = False
        self.achievement_completed = 0

    def __repr__(self):
        return 'Steam Game ID: ' + self.game_id + ' Game Name: ' + self.name + ' ' + str(self.hours_played) + ' hours played'
