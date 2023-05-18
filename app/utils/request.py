import requests


def RequestGetApi(API_URL: str, params):
    response = requests.get(API_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None
