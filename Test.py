from Main import get_spotify_credentials

sp = get_spotify_credentials()
playlist_url = "https://open.spotify.com/playlist/7s6IbdKa71ET8L7XHjkHaF?si=f0db8c1fe84b4b01"
results = sp.playlist_items(playlist_url)
tracks = results['items']

print(f"DEBUG: Number of items found: {len(tracks)}")

for i, item in enumerate(tracks):
    print(f"--- Item {i} Raw Keys: {list(item.keys())} ---")
    if 'track' in item:
        print(f"Track Name: {item['track'].get('name')}")
    else:
        print("No 'track' key found in this item.")
    
    # Let's see what the item actually is if it's skipping
    print(f"Full Item Content: {item}")