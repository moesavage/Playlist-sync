from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from config.settings import settings

def get_youtube_client():
    scopes = ["https://www.googleapis.com/auth/youtube"]
    flow = InstalledAppFlow.from_client_secrets_file(settings.YOUTUBE_CLIENT_SECRET_FILE, scopes)
    creds = flow.run_local_server(port=8080)
    yt =  build("youtube", "v3", credentials=creds)
    return yt
