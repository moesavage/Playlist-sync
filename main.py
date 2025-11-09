# main.py
from auth import get_spotify_client, get_youtube_client
from services.spotify_service import get_playlist_tracks, create_playlist as sp_create_playlist
from services.youtube_service import create_playlist as yt_create_playlist, search_video_id, add_video_to_playlist
from utils.logger import get_logger
from utils.helpers import load_mappings, save_mappings


logger = get_logger('playlist_sync')




def sync_spotify_to_youtube(spotify_playlist_id, target_title=None):
    sp = get_spotify_client()
    yt = get_youtube_client()


    user = sp.current_user()
    user_id = user['id']
    logger.info(f"Spotify user: {user.get('display_name') or user_id}")


    tracks = get_playlist_tracks(sp, spotify_playlist_id)
    logger.info(f"Fetched {len(tracks)} tracks from Spotify")


    target_title = target_title or f"Synced: {spotify_playlist_id}"
    yt_playlist_id = yt_create_playlist(yt, target_title, description='Playlist synced from Spotify')
    logger.info(f"Created YouTube playlist {yt_playlist_id}")


    mappings = load_mappings()
    added = 0
    for t in tracks:
        query = f"{t.get('artist')} - {t.get('title')}"
        # try cached mapping first
        cache_key = f"spotify:{t.get('spotify_uri') or t.get('title')+'|'+t.get('artist','') }"
        video_id = mappings.get(cache_key)
        if not video_id:
            video_id = search_video_id(yt, query)
            if video_id:
                mappings[cache_key] = video_id
        if video_id:
            add_video_to_playlist(yt, yt_playlist_id, video_id)
            added += 1
            logger.info(f"Added: {t.get('title')} -> {video_id}")
        else:
            logger.warning(f"Not found on YouTube: {t.get('title')}")


    save_mappings(mappings)
    logger.info(f"Finished. Added {added}/{len(tracks)} tracks.")




if __name__ == '__main__':
    playlist_id = input('Enter Spotify playlist ID or URL: ').strip()
    # if url provided, try to parse id
    if 'playlist' in playlist_id and 'spotify' in playlist_id:
    # expect format https://open.spotify.com/playlist/{id}
        playlist_id = playlist_id.split('playlist/')[-1].split('?')[0]
    sync_spotify_to_youtube(playlist_id)
























# from auth.spotify_auth import get_spotify_client
# from auth.youtube_auth import get_youtube_client
# from services.spotify_service import get_playlist_tracks
# from services.youtube_service import create_playlist, add_video_to_playlist, search_video

# def sync_spotify_to_youtube(spotify_playlist_id):
#     sp = get_spotify_client()
#     yt = get_youtube_client()
#     user = sp.current_user()

#     print("Fetching Spotify playlist...")
#     tracks = get_playlist_tracks(sp, spotify_playlist_id)

#     print("Creating YouTube playlist...")
#     yt_playlist_id = create_playlist(yt, title="Synced from Spotify")

#     for t in tracks:
#         query = f"{t['artist']} {t['title']}"
#         video_id = search_video(yt, query)
#         if video_id:
#             add_video_to_playlist(yt, yt_playlist_id, video_id)
#             print(f"✅ Added {t['title']}")
#         else:
#             print(f"❌ Not found: {t['title']}")

# if __name__ == "__main__":
#     playlist_id = input("Enter Spotify playlist ID: ")
#     sync_spotify_to_youtube(playlist_id)
