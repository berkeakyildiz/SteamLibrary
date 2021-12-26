from steam_game import SteamGame


class GameHelper:
    def create_new_steam_game(self, game_id, name, hours_played):
        new_game = SteamGame(game_id, name, hours_played)
        return new_game

