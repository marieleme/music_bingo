import random


from PIL import Image, ImageDraw, ImageFont, ImageEnhance

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

def draw_image_from_colour_grid(colour_grid):
    width = 1000
    height = 800
    opacity = 0.8
    transparent = (0, 0, 0, 0)
    white = (255,255,255)
    black = (0,0,0)
    font = ImageFont.truetype('Oswald-Regular.ttf',15)

    wm = Image.new('RGBA',(width,height),transparent)
    im = Image.new('RGBA',(width,height),transparent)

    draw = ImageDraw.Draw(wm)

    for i, row in enumerate(colour_grid):
        for j, song in enumerate(row):
            some = beautify(song, 25)
            draw.text((i*200, j*150), some, black, font)


    en = ImageEnhance.Brightness(wm)
    mask = en.enhance(1-opacity)

    im.paste(wm, (25,25), mask)
    im.save('bingo.png', 'PNG')
    
    #make_white_pixles_transparent('bingo.jpg')

    #paste_grid_to_sheet('sheet.png', 'img2.png')

"""
def make_white_pixles_transparent(image):

    img = Image.open(image)
    img = img.convert("RGBA")
    datas = img.getdata()   

    newData = []
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)

    img.putdata(newData)
    img.save("img2.png", "PNG")
"""
"""
def paste_grid_to_sheet(sheet, image):

    #Image on which we want to paste 
    img1 = Image.open(sheet)  
    
    if img1.mode!='RGBA':
        alpha = Image.new('L', img1.size, 255)
        img1.putalpha(alpha)

    #Relative Path 
    #Image which we want to paste 
    img2 = Image.open(image)  
    #img1.paste(img2, (50, 50)) 
        
    #Saved in the same relative location 
    #img1.save("bingo_sheet.png", "PNG") 
    #Image.alpha_composite(img1, img2).save("test3.png")
"""


if __name__ == '__main__':
    value_grid = create_grid(5)
    colour_grid = map_song_to_grid(value_grid)
    draw_image_from_colour_grid(colour_grid)