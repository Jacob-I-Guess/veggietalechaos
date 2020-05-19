from PIL import Image , ImageEnhance , ImageFont , ImageDraw
import random
import urllib.request
import os
x=0

num=0
while x<10:
    x+=1
    num+=1
    word_url = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
    response = urllib.request.urlopen(word_url)
    long_txt = response.read().decode()
    words = long_txt.splitlines()
    rndword = random.choice(words)
    rndfile = random.choice(os.listdir("C:\\Users\\Home\\Desktop\\pythonimg\\imagerandomhaha"))
    rndimg = rndfile
    image1= Image.open(os.path.join("C:\\Users\\Home\\Desktop\\pythonimg\\imagerandomhaha" , rndimg))
    size = width , height = image1.size
    sharp = ImageEnhance.Sharpness (image1.convert('RGB'))
    image1 = sharp.enhance(5.0)
    colour = ImageEnhance.Color (image1)
    image1 = colour.enhance(5.0)
    str1 = rndword
    font_type = ImageFont.truetype('impact.ttf',50)


    draw = ImageDraw.Draw(image1)
    draw.text(xy=(50,50),text=str1 , font = font_type , fill = 'white' ,)
    image1.save("deepfried"+str(num)+".png")
