# Call This Class Now:
from library_fetcher import SteamLibraryFetcher

your_id = '76561198119274839'

make_object = SteamLibraryFetcher()
all_games = make_object.get_steam_library(your_id)

print("Steam ID : ", your_id, "\n")

all_games.sort(key=lambda x: x.hours_played, reverse=True)
for game in all_games:
    print(game)

