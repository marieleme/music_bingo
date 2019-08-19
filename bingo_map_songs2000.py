import random
from PIL import Image, ImageDraw, ImageFont, ImageEnhance


"""
Add random integer to grind for n = 5 x 5
Random integer will represent song from list. 
"""
def create_grid(n):
    
    allnum = random.sample(range(35), 25)

    return [[allnum.pop() for x in range(n)] for _ in range(n)]

    

"""
Open txt file, and return string with song and artist
"""
def open_playlist_file():
    f = open("something.txt", "r")
    song_list = f.readlines()
    f.close()  
    return song_list

def find_song(i, song_list):
    for song in song_list:
        songinfo = song.decode('utf-8').split(":")
        if i == int(songinfo[0]):
            return (songinfo[1],songinfo[2])
                 
"""
Replace grind number with tuple of song and artist
"""
def map_song_to_grid(value_grid):
    song_list = open_playlist_file()

    return [[find_song(x, song_list) for x in row] for row in value_grid]


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

    return ('"' + str(str1) + '"' +"\n"+str(str2)).encode('utf-8')

def draw_image_from_colour_grid(colour_grid, name):

    width = 1800
    string_width = 23
    font_width = 25
    height = 1500
    opacity = 0.5
    transparent = (0, 0, 0, 0)
    white = (255,255,255)
    black = (0,0,0)
    font = ImageFont.truetype('Oswald-Regular.ttf', font_width)
    bingo_name = 'BINGO/bingo_sheet' + str(name) + '.pdf'

    wm = Image.new('RGBA',(width,height),transparent)
    im = Image.new('RGBA',(width,height),transparent)

    draw = ImageDraw.Draw(wm)

    for i, row in enumerate(colour_grid):
        for j, song in enumerate(row):
            some = beautify(song, string_width)
            draw.text((i*265, j*260), some, black, font)


    draw.text((2350, 3450), str(name), black, font)

    en = ImageEnhance.Brightness(wm)
    mask = en.enhance(1-opacity)

    im.paste(wm, (25,25), mask)
    im.save('bingo.png', 'PNG')

    #sheet2-1
    ima = Image.open('sheet2-1.png')

    ima.paste(wm, (180,690), mask)

    ima.save(bingo_name, 'PDF')
    

if __name__ == '__main__':
    #300 ark bingo 19
    for i in range(1):
        value_grid = create_grid(5)
        colour_grid = map_song_to_grid(value_grid)
        draw_image_from_colour_grid(colour_grid, i)
