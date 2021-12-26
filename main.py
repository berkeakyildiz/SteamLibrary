# Call This Class Now:
from library_fetcher import SteamLibraryFetcher

your_id = '76561198119274839'

make_object = SteamLibraryFetcher()
get_result = make_object.call_all(your_id)

if isinstance(get_result, dict):

    print("Dict Format : ", get_result, "\n")
    print("Target ID : ", your_id, "\n")

    for names, appid in get_result.items():
        print(names, appid)

else:
    print(get_result)
