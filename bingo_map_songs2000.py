##### HUSK Å KJØR I PYTHON3 #####
import random
import config as cf
from PIL import Image, ImageDraw, ImageFont, ImageEnhance

"""
Add random integer to grid for n = 5 x 5
Integer will represent song from list. 
"""
def create_grid(n, amount_songs):
    allnum = random.sample(range(amount_songs), 25)
    return [[allnum.pop() for x in range(n)] for _ in range(n)]


"""
Open txt file, and return string with song and artist
"""
def open_playlist_file():
    with open("formated_playlist.txt", "r") as f:
        song_list = f.readlines()
    return song_list

"""
Returns amount of songs in playlist
"""
def count_songs_in_playlist():
    with open("formated_playlist.txt", "r") as f:
        amount_songs = sum(1 for _ in f)
    return amount_songs

"""
Find song with the equivalent number between song_list and grid
"""
def find_song(i, song_list):
    for song in song_list:
        songinfo = song.split(":")
        if i == int(songinfo[0]):
            return (songinfo[1],songinfo[2])
                 
"""
Replace grid number with tuple of song and artist
"""
def map_song_to_grid():
    song_list = open_playlist_file()
    amount_songs = count_songs_in_playlist()
    grid = create_grid(5, amount_songs)

    return [[find_song(x, song_list) for x in row] for row in grid]


"""
Change song and artist tuple to pretty strings
"""
def beautify(song_tuple, max_width):
    str1 = song_tuple[0]
    str2 = song_tuple[1]

    if(len(song_tuple[0]) > max_width):
        str1 = str1[:max_width] + "- \n" + str1[max_width:]

    if(len(song_tuple[1]) > max_width):
        str2 = str2[:max_width] + "- \n" + str2[max_width:]

    return '"' + str(str1) + '"' +"\n"+str(str2)

def draw_image_from_colour_grid(colour_grid, name):

    width = 1800
    string_width = 21 #23
    font_width = 25
    height = 1500
    opacity = 0.5
    transparent = (0, 0, 0, 0)
    white = (255,255,255)
    black = (0,0,0)
    font = ImageFont.truetype('font/Oswald-Regular.ttf', font_width)
    bingo_name = 'BINGO/bingo_sheet' + str(name) + '.pdf'

    wm = Image.new('RGBA',(width,height),transparent)
    im = Image.new('RGBA',(width,height),transparent)

    draw = ImageDraw.Draw(wm)

    for i, row in enumerate(colour_grid):
        for j, song in enumerate(row):
            some = beautify(song, string_width)
            draw.text((i*265, j*260), some, black, font)


    draw.text((1340, 1470), str(name), black, font)

    en = ImageEnhance.Brightness(wm)
    mask = en.enhance(1-opacity)

    # im.paste(wm, (25,25), mask)
    # im.save('bingo.png', 'PNG')

    #sheet2-1
    ima = Image.open('test_sheet.png')

    ima.paste(wm, (180,690), mask)

    ima.save(bingo_name, 'PDF')
    

if __name__ == '__main__':
    for i in range(cf.AMOUNT_SHEETS):
        colour_grid = map_song_to_grid()
        draw_image_from_colour_grid(colour_grid, i)
