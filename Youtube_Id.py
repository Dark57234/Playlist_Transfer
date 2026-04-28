import yt_dlp

def find_youtube_id(track_name, artist):
    query = f"{track_name} {artist} official audio"
    ydl_opts = {'quiet': True, 'skip_download': True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(f"ytsearch1:{query}", download=False)
            return info['entries'][0]["id"]
        except:
            return None
        
if __name__ == "__main__":
    track_name = "Fabienk"
    artist = "Angine de Poitrine"

    youtube_id = find_youtube_id(track_name, artist)
    print(f"Youtube ID for {track_name} by {artist}: {youtube_id} ")