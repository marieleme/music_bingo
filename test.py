while playlists:
    for i, playlist in enumerate(playlists['items']):
        with open("something.txt", "a") as file:
            file.write("%4d %s %s \n" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
    if playlists['next']:
        playlists = sp.next(playlists)
    else:
        playlists = None
