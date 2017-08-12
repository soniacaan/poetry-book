from PIL import Image, ImageDraw, ImageFont



def IntelliDraw(drawer,text,font,containerWidth):
    words = text.split()  
    lines = [] # prepare a return argument
    lines.append(words) 
    finished = False
    line = 0
    while not finished:
        thistext = lines[line]
        newline = []
        innerFinished = False
        while not innerFinished:
            #print 'thistext: '+str(thistext)
            if drawer.textsize(' '.join(thistext),font)[0] > containerWidth:
                # this is the heart of the algorithm: we pop words off
the current
                # sentence until the width is ok, then in the next outer loop
                # we move on to the next sentence. 
                newline.insert(0,thistext.pop(-1))
            else:
                innerFinished = True
        if len(newline) > 0:
            lines.append(newline)
            line = line + 1
        else:
            finished = True
    tmp = []        
    for i in lines:
        tmp.append( ' '.join(i) )
    lines = tmp
    (width,height) = drawer.textsize(lines[0],font)            
    return (lines,width,height)