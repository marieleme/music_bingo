from spotipy.oauth2 import SpotifyClientCredentials
import spotipy 
import spotipy.util as util
import json
import config as cf

client_credentials_manager = SpotifyClientCredentials(client_id = cf.CLIENT_ID, client_secret = cf.CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)


uri = cf.PLAYLIST_URI
username = 'spotify'
playlist_id = uri.split(':')[2]


def show_tracks(results):
    for i, item in enumerate(results['items']):
        track = item['track']
        with open(cf.PLAYLIST, "ab") as file:
            string = ("%d:%s:%s \n" % (i, track['name'], track['artists'][0]['name'])).encode('utf-8')
            file.write(string)



playlists = sp.user_playlists(username)
results = sp.user_playlist(username, playlist_id, fields="tracks,next")

tracks = results['tracks']
show_tracks(tracks)



