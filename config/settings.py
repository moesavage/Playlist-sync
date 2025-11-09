import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
    SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
    SPOTIFY_REDIRECT_URI = os.getenv("SPOTIFY_REDIRECT_URI")

    YOUTUBE_CLIENT_SECRET_FILE = os.getenv("YOUTUBE_CLIENT_SECRET_FILE")

    APPLE_TEAM_ID = os.getenv("APPLE_TEAM_ID")
    APPLE_KEY_ID = os.getenv("APPLE_KEY_ID")
    APPLE_PRIVATE_KEY_PATH = os.getenv("APPLE_PRIVATE_KEY_PATH")

settings = Settings()
