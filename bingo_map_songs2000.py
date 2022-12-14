##### HUSK Å KJØR I PYTHON3 #####
from genericpath import exists
import random
import config as cf
from tqdm import tqdm
from PIL import Image, ImageDraw, ImageFont, ImageEnhance
from os import mkdir, path, remove
from fitz import fitz, Rect

"""
Add random integer to grid for n = 5 x 5
Integer will represent song from list. 
"""
def create_grid(n, amount_songs):
    allnum = random.sample(range(amount_songs), 25)
    return [[allnum.pop() for x in range(n)] for _ in range(n)]

"""
Creates temporary bingo sheets folder
"""
def make_dir():
    if path.exists(cf.BINGO_FOLDER):
        return
    mkdir(cf.BINGO_FOLDER)

"""
Open txt file, and return string with song and artist
"""
def open_playlist_file():
    with open(cf.PLAYLIST, "r") as f:
        song_list = f.readlines()
    return song_list

"""
Returns amount of songs in playlist
"""
def count_songs_in_playlist():
    with open(cf.PLAYLIST, "r") as f:
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

"""
Create bingo sheet 
"""
def draw_image_from_colour_grid(colour_grid, name):

    width = 1800
    string_width = 21 #23
    font_width = 25
    height = 1500
    opacity = 0.5
    transparent = (0, 0, 0, 0)
    white = (255,255,255)
    black = (0,0,0)
    font = ImageFont.truetype(cf.FONT, font_width)
    bingo_sheet = cf.BINGO_FOLDER + cf.SHEET_NAME + str(name) + cf.PDF

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

    # Opens the template sheet
    ima = Image.open(cf.TMP_SHEET)

    ima.paste(wm, (180,690), mask)

    ima.save(bingo_sheet, 'PDF')

    # Adds logo if specified
    if cf.LOGO:
        add_logo(bingo_sheet)


""" 
Adds to logos to the given PDF 
"""
def add_logo(pdf_name):
    
    pdf = fitz.open(pdf_name)

    # opens logo specified in cf file
    img = open(cf.LOGO, "rb").read()
    
    page_width = 1654

    logo_dim = cf.LOGO_DIM
    logo_x = cf.LOGO_X
    logo_y = cf.LOGO_Y

    # Define area which the logo should cover
    left_logo = Rect(logo_x, logo_y, logo_x+logo_dim, logo_y+logo_dim)    
    right_logo = Rect(page_width-logo_dim-logo_x, logo_y, page_width-logo_x, logo_dim+logo_y) # Mirrors the x-coordinates

    # Insert logo to left and right side of image
    pdf[0].insert_image(left_logo, stream=img)
    pdf[0].insert_image(right_logo, stream=img)    
    pdf.saveIncr()

if __name__ == '__main__':
    make_dir()
    for i in tqdm(range(cf.AMOUNT_SHEETS)):
        colour_grid = map_song_to_grid()
        draw_image_from_colour_grid(colour_grid, i)
