import requests
from config import YandexAPIToken
from io import BytesIO
from PIL import Image


def get_map_image():
    payload = {
        "ll": "37.613189,55.704250",
        "pt": "37.613189,55.704250,pm2rdm",
        "spn": "0.0074,0.0074",
        "l": "map",
        "apikey": YandexAPIToken
    }

    request_url = "https://static-maps.yandex.ru/1.x"

    response = requests.get(request_url, payload)

    image = Image.open(BytesIO(response.content))
    image.save("src/map.png")

