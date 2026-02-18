import requests
from config.settings import settings


class AsteroidsExtractor:
    def __init__(self, start_date: str, end_date: str):
        self.start_date = start_date
        self.end_date = end_date

    def get_asteroids_data(self):
        url = "{base}start_date={start}&end_date={end}&api_key={key}".format(
            base=settings.API_BASE_URL,
            start=self.start_date,
            end=self.end_date,
            key=settings.API_KEY
        )
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()
        return data

