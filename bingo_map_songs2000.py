import random


from PIL import Image, ImageDraw

COLOUR_MAP = {
    range(-10, 0): (255, 0, 0),
    range(0, 10): (0, 255, 0),
    range(10, 21): (0, 0, 255)
}


"""
Add random integer to grind for n = 5 x 5
Random integer will represent song from list. 
"""
def create_grid(n):
    return [[random.randint(0, 74) for _ in range(n)] for _ in range(n)]


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
        songinfo = song.split(":")
        if i == int(songinfo[0]):
            return (songinfo[1],songinfo[2])
                 
"""
Replace grind number with tuple of song and artist
"""
def map_song_to_grid(value_grid):
    song_list = open_playlist_file()

    return [[find_song(x, song_list) for x in row] for row in value_grid]

def beautify(song_tuple, max_width):
    str1 = song_tuple[0]
    str2 = song_tuple[1]

    if(len(song_tuple[0]) > max_width):
        str1 = str1[max_width:] + "- \n" + str1[:]

    if(len(song_tuple[1]) > max_width):
        str2 = song_tuple[1].replace(' ', '\n')

    return str(str1)+"\n"+str(str2)

def draw_image_from_colour_grid(colour_grid):
    im = Image.new('RGB', (1500, 1500), (255,255,255))
    #im.putdata([x for row in colour_grid for x in row])
    d = ImageDraw.Draw(im)

    for i, row in enumerate(colour_grid):
        for j, song in enumerate(row):
            some = beautify(song, 15)
            d.text((i*200,j*100), some, fill=(0,0,0))

    im.save('out.jpg', 'JPEG')



if __name__ == '__main__':
    value_grid = create_grid(5)
    colour_grid = map_song_to_grid(value_grid)
    draw_image_from_colour_grid(colour_grid)