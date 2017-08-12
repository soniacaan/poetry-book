from os import listdir
from os.path import isfile, join
import random
from nltk.corpus import gutenberg
import re
import textwrap
from split_sentences import split_into_sentences
from PIL import Image, ImageDraw, ImageFont
from code_poetry import get_poetry
from xml.etree import ElementTree
from code_quotations import get_quotes
import textwrap
import sys


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

"""
Poems available on gutenberg
'blake-poems.txt'
'milton-paradise.txt'
'shakespeare-caesar.txt'
'shakespeare-hamlet.txt'
'shakespeare-macbeth.txt'
'whitman-leaves.txt'
"""

#location of photos
photo_dir = 'image-twt/'


def random_gutenberg(text_length):
    
    poems = ['shakespeare-caesar.txt']
    
    #poems = ['blake-poems.txt', 'milton-paradise.txt', 'whitman-leaves.txt', 
    #'shakespeare-caesar.txt', 'shakespeare-hamlet.txt', 'shakespeare-macbeth.txt']

    text_clean = []
    positions = []
    print("text_length ", text_length)
    #get a random gutenberg title
    i = random.randint(0, len(poems)-1)
    poem = poems[i]
    print("poem name ", poem)
    raw = gutenberg.raw(poem)

    #find all indexes for paragraphs and find title
    space_positions = [m.start() for m in re.finditer('\n \n \n', raw)]
    nospace_positions =  [m.start() for m in re.finditer('\n\n\n', raw)]
    
    #Find Title and also index paragraph start/stop
    if space_positions > nospace_positions:
        if len(space_positions) < 10:
            title = raw[:space_positions[0]]
            title = clean_gutenberg(title)
            print("space 1")
            positions = [m.start() for m in re.finditer('\n \n', raw)]
            if len(positions) < 10:
                print("2ndry loop of space makes no sense")
        else: 
            title = raw[:space_positions[0]] 
            title = clean_gutenberg(title)  
            print("space 2")
            positions.extend(space_positions)
    
    else:
        if len(nospace_positions) < 10:
            title = raw[:nospace_positions[0]]
            title = clean_gutenberg(title)
            print("space 3")
            positions = [m.start() for m in re.finditer('\n\n', raw)]
            if len(positions) < 10:
                print("2ndry loop of NO space makes no sense")
        else:
            title = raw[:nospace_positions[0]]
            title = clean_gutenberg(title)
            print("space 4")
            positions.extend(nospace_positions)


    #index all paragraphs
    #if len(positions) < 10:
     #   title = positions      
      #  next_positions = [m.start() for m in re.finditer('\n \n \n', raw)]
       # print("position space ", len(positions))
    
    #Find a paragraph position to print
    j = random.randint(1, len(positions)-3)
    print("random index j ", j)
    #print("len positions ", len(positions))
    
    text = raw[positions[j]:positions[j+1]]
    text_clean.extend(clean_gutenberg(text))

    #Only return text that fits the photo
    length=len(text_clean) 

    k = j + 1
    #print("nth of raw ", raw.index([len(positions)-1]))
    print("var text_length", text_length)
    
    while (int(length) < int(text_length)):
        print("length in loop getgut!!! ", length)
        if k >= (len(positions)-1):
            k == 1
        if k == 0:
            k = 1
        if k == j:
            sys.exit()
        else:  
            print("k index in else! ", k)
            content = raw[positions[k]:positions[k+1]]
            new_text = clean_gutenberg(content)
            text_clean.extend(new_text)
            length += len(new_text)
            k += 1
            print("length in else stat ", length)
            
    

    print("length of clean_text in get_text ", len(text_clean))

    return text_clean, title

#Clean text for, takes String only
def get_length(text):
    length = 0
    for f in text:
        length += 1

    return length




def clean_gutenberg(text):
    
    text_clean = []

    #
    text = text.split('\n')


    for t in text:
     #clean_text.append(split_into_sentences(t))
        t = t.strip('{}')
        t = t.strip('[]')
        if t == '':
            continue
        if t == ' ':
            continue
        if t == ', ':
            continue
        else:
            text_clean.append(t)

    return text_clean    
    

#Get Photo Ready
def photos_ready():
    photos = [f for f in listdir(photo_dir) if f.endswith(('.jpg', '.png', '.gif'))]
        
    return photos

def random_photo(item):
    i = random.randint(0, len(item)-1)
    photo = item[i]

    return photo

def draw_text(genre, q):
    
    #Pick text to draw
    if genre == 'classic':
        text_clean = print_gutenberg_photo()
    if genre == 'poem':
        text_clean = print_poetry(q)
    if genre == 'quote':
        text_clean = clean_quotes(q) 

    return text_clean
      
 
"""
    #set parameters for text to draw
  
    font_fname = 'Courier'
    font = ImageFont.truetype(font_fname, font_size)
    #draw.text((10, 10), "Sample Text", (255,255,255), font=font)

    
    #wrapc = 0
    #print("length of line", len(text_clean))
    if offset < (int(photo_height)):
        for line in text_clean:
            print(line)
            width, height = font.getsize(line)
            #print("TEXT HEIGHT", height)
            if width > 80:
                for f in textwrap.wrap(line, text_width):
                    #width, height = font.getsize(line)
                    #print(width)
                    draw.text((margin, offset), f, font=font)
                    #draw.text(((10 - width) / 2, y_text), line, font=font)
                    #draw.text((10, y_text), line, font=font)
                    offset += font.getsize(f)[1]
                    print("offset ", offset)
                    #y_text += height
                    #wrapc = wrapc + 1
            else:
                draw.text((margin, offset), line, font=font)
                offset += font.getsize(line)[1]
    print("offset ", offset)
    img.show()
    img.save('out.jpg', quality=90, optimize=True)
    img.close()
    #print(wrapc)
 """   

def print_gutenberg_photo():
    font_fname = 'Courier'
    margin = offset = 40
    font_size = 80
    title_size = 50
   
    #Get photo List
    photos = photos_ready()
    #Get one photo
    photo = random_photo(photos)
    photo = photo_dir + photo
    img = Image.open(photo) 
    #get size of photo
    photo_width, photo_height = img.size
    draw = ImageDraw.Draw(img)
    text_width = photo_width * 0.5
    title_width = margin + text_width
    photo_height_cutoff = photo_height * 0.9
    title_offset = photo_height * 0.9
    if title_width < (photo_width * .75):
        title_width = (photo_width * .75)
    #calculate the lenght of text to get
    text_length = (int(photo_height)/int(font_size)) 

    text_clean, title = random_gutenberg(text_length)
    #set font type, size
    font = ImageFont.truetype(font_fname, font_size)  
    font_title = ImageFont.truetype(font_fname, title_size) 
    #calculate location of start of title text
    title_margin = (photo_height * .8)
    #print("length of line", len(text_clean))
    for line in text_clean:
        width, height = font.getsize(line)
        if int(offset) < photo_height_cutoff:
            if int(width) > int(text_width):
                for f in textwrap.wrap(line, (text_width)):
                    print("F in WRAPTEXT ", f)
                   #width, height = font.getsize(line)
                    #print(width)
                    draw.text((margin, offset), f, font=font)
                    #draw.text(((10 - width) / 2, y_text), line, font=font)
                    #draw.text((10, y_text), line, font=font)
                    offset += font.getsize(f)[1]
                    print("offset TEXTWRAP", offset)
                    #y_text += height
                    #wrapc = wrapc + 1
            else:
                draw.text((margin, offset), line, font=font)
                offset += font.getsize(line)[1]
    for t in title:
                draw.text((title_margin, title_offset), t, font=font_title)
                title_height = font.getsize(t)[1]
                title_offset += title_height
    img.show()
    img.save('out.jpg', quality=90, optimize=True)
    img.close()
    #print(wrapc)
    return text_clean

def print_poetry(q):
    font_fname = 'Courier'
    margin = offset = 40
    font_size = 80
    title_size = 50
    
    #Get photo List
    photos = photos_ready()
    #Get one photo
    photo = random_photo(photos)
    photo = photo_dir + photo
    img = Image.open(photo) 
    #get size of photo
    photo_width, photo_height = img.size
    draw = ImageDraw.Draw(img)
    text_width = photo_width * 0.5
    title_width = margin + text_width
    photo_height_cutoff = photo_height * 0.9
    title_offset = photo_height * 0.9
    if title_width < (photo_width * .75):
        title_width = (photo_width * .75)
    #calculate the lenght of text to get
    text_length = (int(photo_height)/int(font_size)) 
    
    #get poetry text
    text_clean = parse_poetry(q, text_length)

    #set font type, size
    font = ImageFont.truetype(font_fname, font_size)  
    font_title = ImageFont.truetype(font_fname, title_size) 
    #calculate location of start of title text
    title_margin = (photo_height * .8)
    #print("length of line", len(text_clean))
    for line in text_clean:
        width, height = font.getsize(line)
        if int(offset) < photo_height_cutoff:
            print(" WIDTH ", width)
            print("TEXT_WIDTH", text_width)
            if int(width) > int(text_width):
                for f in textwrap.wrap(line, int(text_width)):
                    if int(font.getsize(f)[1]) > int(text_width):
                        for g in textwrap.wrap(f, int(text_width)):
                            print("G in WRAPTEXT ", g)
                   #width, height = font.getsize(line)
                    #print(width)
                            draw.text((margin, offset), g, font=font)
                    #draw.text(((10 - width) / 2, y_text), line, font=font)
                    #draw.text((10, y_text), line, font=font)
                            offset += font.getsize(g)[1]
                            print("F lenght ", font.getsize(g)[1])
                            print("offset TEXTWRAP", offset)
                    else:
                        print("F in WRAPTEXT ", f)
                   #width, height = font.getsize(line)
                    #print(width)
                        draw.text((margin, offset), f, font=font)
                    #draw.text(((10 - width) / 2, y_text), line, font=font)
                    #draw.text((10, y_text), line, font=font)
                        offset += font.getsize(f)[1]
                        print("F lenght ", font.getsize(f)[1])
                        print("offset TEXTWRAP", offset)
                    #y_text += height
                    #wrapc = wrapc + 1
            else:
                draw.text((margin, offset), line, font=font)
                offset += font.getsize(line)[1]
    
    img.show()
    img.save('out.jpg', quality=90, optimize=True)
    img.close()
    #print(wrapc)
    return text_clean

def wrap_text(text, length):
    text_clean = []

    for f in textwrap.wrap(text, int(length)):
        print
        text_clean.append(f)

    return text_clean




    #Parse Poetry.com
def parse_poetry(q, text_length):
    data = get_poetry(q)
    clean_text = []
    tree = ElementTree.fromstring(data.content)
    print("tree length", len(tree))

    length = 0

    for i in range(0,len(tree)-1): 
        print("this is i ", i)
        if int(length) < int(text_length):
            title = tree[i][0].text
            title = title.split('\n')
            title = clean_poetry(title)
            author = tree[i][1].text
            author = author.split('\n')
            author = clean_poetry(author)
            poem = tree[i][2].text.split('\n')
            poem = clean_poetry(poem)

            clean_text.extend(title)
            #clean_text.append("  ")
            clean_text.extend(author)
            clean_text.append("  ")
            clean_text.extend(poem)
            clean_text.append("  ")
            length += len(clean_text)
            print("clean_text length ", length)
            print("clean_text ", clean_text)
            i += 1
        else:
            break
    return clean_text 

def clean_poetry(text):
    text_clean = []
    
    for t in text:
     #clean_text.append(split_into_sentences(t))
        t = t.strip('[\t]+')
        t = t.strip('[\r]+')
        t = t.strip('[{[]}]+')
        if len(t) == 1:
            continue
        if t.isspace():
            continue
        if t == '':
            continue
        if t == ', ':
            continue
        else:
            text_clean.append(t)
            text_clean.append("  ")
    return text_clean

def clean_quotes(q):
    data = get_quotes(q)
    tree = ElementTree.fromstring(data.content)
    text_clean = []
    print("tree length", len(tree))

    #quote = tree[0][0].text
    #author = tree[0][1].text

    i = 0
    if i < 3:
        for t in tree:
            text_clean.append("--"+tree[i][1].text+"--")
            quote = tree[i][0].text.split('.')# FIX IT Iterate over it
            for f in quote:
                text_clean.append(f)
            text_clean.append(" ")
            
            i = i + 1

    return text_clean

