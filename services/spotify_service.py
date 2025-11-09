# services/spotify_service.py


def get_playlist_tracks(sp, playlist_id, limit=100):
    items = []
    offset = 0
    while True:
        res = sp.playlist_items(playlist_id, limit=limit, offset=offset)
        if not res or 'items' not in res or len(res['items']) == 0:
            break
        for it in res['items']:
            t = it.get('track')
            if not t:
                continue
            items.append({
            'title': t.get('name'),
            'artists': [a.get('name') for a in t.get('artists', [])],
            'artist': ', '.join([a.get('name') for a in t.get('artists', [])]),
            'isrc': (t.get('external_ids') or {}).get('isrc'),
            'duration_ms': t.get('duration_ms'),
            'spotify_uri': t.get('uri')
            })
        offset += len(res['items'])
    return items




def create_playlist(sp, user_id, name, public=False, description='Synced playlist'):
    pl = sp.user_playlist_create(user=user_id, name=name, public=public, description=description)
    return pl['id']




def add_tracks_to_playlist(sp, playlist_id, uris):
    # Spotify max 100 add per request
    for i in range(0, len(uris), 100):
     sp.playlist_add_items(playlist_id, uris[i:i+100])

















# def get_playlist_tracks(sp, playlist_id):
#     tracks = []
#     results = sp.playlist_items(playlist_id)
#     for item in results['items']:
#         t = item['track']
#         tracks.append({
#             'title': t['name'],
#             'artist': ', '.join(a['name'] for a in t['artists']),
#             'isrc': t.get('external_ids', {}).get('isrc')
#         })
#     return tracks

# def create_playlist(sp, user_id, name):
#     playlist = sp.user_playlist_create(user=user_id, name=name, public=False)
#     return playlist['id']

# def add_tracks_to_playlist(sp, playlist_id, track_uris):
#     for i in range(0, len(track_uris), 100):
#         sp.playlist_add_items(playlist_id, track_uris[i:i+100])
