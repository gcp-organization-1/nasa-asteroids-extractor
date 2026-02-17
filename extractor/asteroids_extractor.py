import requests
from config.settings import settings


class AsteroidsExtractor:
    def __init__(self, start_date: str, end_date: str):
        self.start_date = start_date
        self.end_date = end_date

    def get_asteroids_data(self):
        url =  f"{settings.API_BASE_URL}start_date={self.start_date}&end_date={self.end_date}&api_key={settings.API_KEY}"

        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        print(data)
        return data

