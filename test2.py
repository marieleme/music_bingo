from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageEnhance

width=854
height=480
opacity=0.8
text='copyright'
filename = 'result.png'
black = (0,0,0)
white = (255,255,255)
transparent = (0,0,0,0)

font = ImageFont.truetype('verdana.ttf',25)
wm = Image.new('RGBA',(width,height),transparent)
im = Image.new('RGBA',(width,height),transparent) # Change this line too.

draw = ImageDraw.Draw(wm)
w,h = draw.textsize(text, font)
draw.text(((width-w)/2,(height-h)/2),text,black,font)

en = ImageEnhance.Brightness(wm)
#en.putalpha(mask)
mask = en.enhance(1-opacity)
im.paste(wm,(25,25),mask)

im.save(filename)

