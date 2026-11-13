import requests


# app_id = 1091500


def get_game_data(app_id):
    #get_info
    url = "https://store.steampowered.com/api/appdetails"

    params = {
        "appids": app_id,
        "cc": "us",
        "l": "english"
    }

    response = requests.get(url, params=params, timeout=15)
    data = response.json()
    print(response.status_code)

    #organize information
    game_data = data[str(app_id)]["data"]

    game_info = {
        "name": game_data["name"],
        "app_id": app_id,
        "developer": game_data["developers"][0],
        "release_date": game_data["release_date"]["date"],
        "price": game_data["price_overview"]["final_formatted"],
        "genre": game_data["genres"][0]["description"],
    }
    return game_info

game = get_game_data(1091500)
print(game)



#
# print(game_data["name"])
# print(game_data["developers"])
# print(game_data["release_date"]["date"])
# print(game_data["price_overview"]["final_formatted"])
# print(game_data["genres"][0]["description"])
