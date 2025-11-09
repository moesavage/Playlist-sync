# auth/__init__.py
from .spotify_auth import get_spotify_client
from .youtube_auth import get_youtube_client


__all__ = ['get_spotify_client', 'get_youtube_client']