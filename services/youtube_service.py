# services/youtube_service.py


def create_playlist(yt, title, description='Synced playlist'):
    body = {
        'snippet': {'title': title, 'description': description},
        'status': {'privacyStatus': 'private'}
    }
    res = yt.playlists().insert(part='snippet,status', body=body).execute()
    return res['id']




def add_video_to_playlist(yt, playlist_id, video_id):
    body = {
        'snippet': {
            'playlistId': playlist_id,
            'resourceId': {'kind': 'youtube#video', 'videoId': video_id}
        }
    }
    yt.playlistItems().insert(part='snippet', body=body).execute()




def search_video_id(yt, query, max_results=5):
    res = yt.search().list(q=query, part='id,snippet', type='video', maxResults=max_results).execute()
    items = res.get('items', [])
    if not items:
        return None
    # choose first by default; you can improve selection using duration/title similarity
    return items[0]['id']['videoId']






















# def create_playlist(yt, title, description="Synced playlist"):
#     body = {"snippet": {"title": title, "description": description}, "status": {"privacyStatus": "private"}}
#     return yt.playlists().insert(part="snippet,status", body=body).execute()["id"]

# def add_video_to_playlist(yt, playlist_id, video_id):
#     body = {"snippet": {"playlistId": playlist_id, "resourceId": {"kind": "youtube#video", "videoId": video_id}}}
#     yt.playlistItems().insert(part="snippet", body=body).execute()

# def search_video(yt, query):
#     res = yt.search().list(q=query, part="id,snippet", type="video", maxResults=1).execute()
#     items = res.get("items", [])
#     return items[0]["id"]["videoId"] if items else None
