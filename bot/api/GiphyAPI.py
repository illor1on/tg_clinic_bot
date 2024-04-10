import requests
from config import GiphyAPIToken


# Функция get запроса к Giphy
def get_gif(gif_id):
    payload = {
                "api_key": GiphyAPIToken,
                "rating": "g",
            }
    request_url = f"https://api.giphy.com/v1/gifs/{gif_id}"
    gif = requests.get(request_url, payload).json()['data']['images']['original']['url']
    return gif
