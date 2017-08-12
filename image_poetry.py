
from os import listdir
from os.path import isfile, join
import random
from nltk.corpus import gutenberg
import re
import textwrap
from split_sentences import split_into_sentences
from PIL import Image, ImageDraw, ImageFont

"""
fonts available on this machine
['Computer Modern', 'Computer Modern', 'Computer Modern', 'Computer Modern', 'Computer Modern', 
'Courier', 'Courier', 'Courier', 'Courier', 'Courier', 'Courier', 'Courier', 'Courier', 
'Helvetica', 'Helvetica', 'Helvetica', 'Helvetica', 'Helvetica', 'Helvetica', 'Helvetica', 
'Helvetica', 'Helvetica', 'Helvetica', 'Helvetica', 'Helvetica', 'Helvetica', 'Helvetica', 
'ITC Avant Garde Gothic', 'ITC Avant Garde Gothic', 'ITC Avant Garde Gothic', 
'ITC Avant Garde Gothic', 'ITC Bookman', 'ITC Bookman', 'ITC Bookman', 'ITC Bookman', 
'ITC Zapf Chancery', 'ITC Zapf Dingbats', 'New Century Schoolbook', 'New Century Schoolbook', 
'New Century Schoolbook', 'New Century Schoolbook', 'Palatino', 'Palatino', 'Palatino', 
'Palatino', 'Symbol', 'Symbol', 'Times', 'Times', 'Times', 'Times', 'Times', 'Times', 'Times', 
'Times', 'Utopia', 'Utopia', 'Utopia', 'Utopia', 'ZapfDingbats']

"""



#extensions = {".jpg", ".png", ".gif"}

#mypath = 'image-twt'




#Get Photo Ready
#def photo_ready():
 #   photos = [f for f in listdir(mypath) if f.endswith('jpg')]
  #  i = random.randint(0, len(photos)-1)
   # photo = photos[i]
    
    #return photo

    


def draw_text(self):
    raw = gutenberg.raw('whitman-leaves.txt')
    text = str(raw[:600])
    text = split_into_sentences(text)
    lines = textwrap.wrap(str(text), width=40)

    img = Image.open('image-twt/test.jpg') #MAKE CHANGE
    draw = ImageDraw.Draw(img)
    y_text = 10
    font_size = 200
    font = ImageFont.truetype(font_fname, font_size)
    #draw.text((10, 10), "Sample Text", (255,255,255), font=font)

    for line in lines:
	    width, height = font.getsize(line)
	    print(width)
	    draw.text(((10 - width) / 2, y_text), line, font=font)
	    y_text += height
    
    img.show()
    img.close()


#Get Poetry Ready
"""
Poems available on gutenberg
'blake-poems.txt'
'milton-paradise.txt'
'shakespeare-caesar.txt'
'shakespeare-hamlet.txt'
'shakespeare-macbeth.txt'
'whitman-leaves.txt'
"""
