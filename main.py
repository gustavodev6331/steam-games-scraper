import requests
import csv

games = []

def get_game_data(app_id):
    #get_info
    url = "https://store.steampowered.com/api/appdetails"

    params = {
        "appids": app_id,
        "cc": "us",
        "l": "english"
    }

    response = requests.get(url, params=params, timeout=15)
    response.raise_for_status()
    data = response.json()

    #organize information
    game_data = data[str(app_id)]["data"]
    price_data = game_data.get("price_overview")
    price = price_data["final_formatted"] if price_data else "Free"
    # print(game_data.keys())

    game_info = {
        "name": game_data["name"],
        "app_id": app_id,
        "price": price,
        "release_date": game_data["release_date"]["date"],
        "developer": game_data["developers"][0],
        "genre": game_data["genres"][0]["description"],
    }
    games.append(game_info)
    return game_info

app_ids = [1091500, 730, 570]

for app_id in app_ids:
    get_game_data(app_id)

with open ('steam_games.csv', 'w', newline='' , encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=games[0].keys())

    writer.writeheader()
    writer.writerows(games)




