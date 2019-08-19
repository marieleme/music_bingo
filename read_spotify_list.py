from spotipy.oauth2 import SpotifyClientCredentials
import spotipy 
import spotipy.util as util
import json


client_credentials_manager = SpotifyClientCredentials(client_id='b7ddf409ea2447e2b51d3a9013fdc65e', client_secret='bed965d091b341b8846cca8a0f34db5d')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# spotify:user:1111932445:playlist:0EamcIJwK2nZWS6iKcNwZ5

uri = 'spotify:playlist:7Im8oz8h3jkrOqMPIcZTpb'
username = 'spotify'
playlist_id = uri.split(':')[2]

def show_tracks(results):
    for i, item in enumerate(results['items']):
        track = item['track']
        with open("something.txt", "a") as file:
            string = ("%d:%s:%s \n" % (i, track['name'], track['artists'][0]['name'])).encode('utf-8')
            file.write(string)


playlists = sp.user_playlists(username)

results = sp.user_playlist(username, playlist_id, fields="tracks,next")
tracks = results['tracks']
show_tracks(tracks)



