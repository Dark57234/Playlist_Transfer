import spotipy
from spotipy.oauth2 import SpotifyOAuth
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import yt_dlp
import time
import threading

SPOTIFY_REDIRECT_URI = "https://example.com/callback"

YT_SCOPES = ['https://www.googleapis.com/auth/youtube']

def get_auth_url(client_id, client_secret):
    
    auth_manager = SpotifyOAuth(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=SPOTIFY_REDIRECT_URI,
            scope="playlist-modify-public",
            open_browser=False
    )

    return auth_manager.get_authorize_url()

def get_spotify_from_url(client_id, client_secret, response_url):
    auth_manager = SpotifyOAuth(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=SPOTIFY_REDIRECT_URI
    )
    code = auth_manager.parse_response_code(response_url)
    token_info = auth_manager.get_access_token(code, as_dict=True)
    return spotipy.Spotify(auth=token_info['access_token'])


def get_youtube_credentials(json_path):
    flow = InstalledAppFlow.from_client_secrets_file(json_path, YT_SCOPES)
    creds = flow.run_local_server(port = 0)
    return build('youtube', 'v3', credentials=creds)

def find_youtube_id(track_name, artist):
    query = f"{track_name} {artist} official audio"
    ydl_opts = {'quiet': True, 'skip_download': True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(f"ytsearch1:{query}", download=False)
            return info['entries'][0]["id"]
        except:
            return None
        
def Transfer_Process(sp_client, yt_json, playlist_url):
    sp = sp_client
    yt = get_youtube_credentials(yt_json)

    results = sp.playlist_items(playlist_url)
    spotify_title = sp.playlist(playlist_url)['name']
    tracks = results['items']

    pl_res = yt.playlists().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": spotify_title,
                "description": f"Created from Spotify playlist: {spotify_title}",
                "status": {
                    "privacyStatus": "private"
                }
            }
        
        }
    ).execute() 
    new_playlist_id = pl_res['id']

    for item in tracks:
        track = item.get('item')
        name = track['name']
        artist = track['artists'][0]['name']

        video_id = find_youtube_id(name, artist)
        if video_id:
            yt.playlistItems().insert(
                part='snippet',
                body={
                    "snippet": {
                    "playlistId": new_playlist_id,
                    "resourceId": {
                        'kind': 'youtube#video', 'videoId': video_id
                       }
                    }
                }
            ).execute()
            time.sleep(1)


