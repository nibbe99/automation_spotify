from bs4 import BeautifulSoup
import requests
import spotipy

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get(f"https://billboard.com/charts/hot-100/{date}/")

response.raise_for_status()
soup = BeautifulSoup(response.text, 'html.parser')


all_titles = soup.find_all(name="h3", class_="a-no-trucate")

titles = [title.getText().strip() for title in all_titles]

print(titles)

YOUR_APP_CLIENT_ID = 'xxx'
YOUR_APP_CLIENT_SECRET = 'xxx'
YOUR_APP_REDIRECT_URI = 'xxx'

import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=YOUR_APP_CLIENT_ID,
                                               client_secret=YOUR_APP_CLIENT_SECRET,
                                               redirect_uri=YOUR_APP_REDIRECT_URI,
                                               scope="playlist-modify-private",
                                             ))

# user-library-read
results = sp.current_user()
USER_ID = results['id']
print(USER_ID)

uris = [sp.search(title)['tracks']['items'][0]['uri'] for title in titles]

print(uris)

PLAYLIST_ID = sp.user_playlist_create(user=USER_ID,public=False,name=f"{date} BillBoard-100")['id']

sp.user_playlist_add_tracks(playlist_id=PLAYLIST_ID,tracks=uris,user=USER_ID)