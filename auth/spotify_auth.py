from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
from config.settings import settings

def get_spotify_client():
    scope = "playlist-read-private playlist-modify-private playlist-modify-public"
    auth_manager = SpotifyOAuth(
        client_id=settings.SPOTIFY_CLIENT_ID,
        client_secret=settings.SPOTIFY_CLIENT_SECRET,
        redirect_uri=settings.SPOTIFY_REDIRECT_URI,
        scope=scope,
        show_dialog=True
    )
    return Spotify(auth_manager=auth_manager)
