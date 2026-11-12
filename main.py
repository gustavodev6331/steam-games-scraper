import requests


app_id = 1091500

url = "https://store.steampowered.com/api/appdetails"

params = {
    "appids": app_id,
    "cc": "us",
    "l": "english"
}

response = requests.get(url, params=params, timeout=15)

print(response.status_code)

data = response.json()

print(data)
