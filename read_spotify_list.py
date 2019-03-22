from spotipy.oauth2 import SpotifyClientCredentials
import spotipy 
import spotipy.util as util
import json


client_credentials_manager = SpotifyClientCredentials(client_id='***REMOVED***', client_secret='***REMOVED***')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

uri = 'spotify:user:spotify:playlist:37i9dQZF1DXauOWFg72pbl'
username = uri.split(':')[2]
playlist_id = uri.split(':')[4]

def show_tracks(results):
    for i, item in enumerate(results['items']):
        track = item['track']
        with open("something.txt", "a") as file:
            file.write("%d:%s:%s \n" % (i, track['name'], track['artists'][0]['name']))


playlists = sp.user_playlists(username)

results = sp.user_playlist(username, playlist_id, fields="tracks,next")
tracks = results['tracks']
show_tracks(tracks)



