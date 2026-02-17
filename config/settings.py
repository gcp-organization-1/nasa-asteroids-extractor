

from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    API_KEY = os.getenv("NASA_API_KEY")
    API_BASE_URL = os.getenv("NASA_BASE_URL")

settings = Settings()