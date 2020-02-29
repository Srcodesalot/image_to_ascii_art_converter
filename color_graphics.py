from PIL import Image
import os
import time

def convert(path, color):
    image = path
    opImg = Image.open(image, 'r')
    opImg.thumbnail((100,100))
    opImg.save(image)
    print(opImg.size)
    width, height = Image.open(image).size
    pix_val = list(opImg.getdata())
    x = 0
    skipLine = False
    picture = "'"

    for pixel in pix_val:
        r, g, b = pixel
        if skipLine == False:
            if 190 <= r <= 225:
                picture = picture + " "
            elif 130 <= r <= 189:
                picture = picture + "."
            elif 70 <= r <= 129:
                picture = picture + ":"
            elif 31 <= r <= 69:
                picture = picture + "!"
            elif 16 <= r <= 30:
                picture = picture + "|"
            elif 0 <= r <= 15:
                picture = picture + "I"
            else:
                picture = picture + " "
        else:
            picture = picture + ""

        x += 1

        if x % width == 0 and x != 0:
            if not skipLine:
                picture = picture + "\n"
            skipLine = not skipLine
    picture += "'"

    if color:
        os.system('printf ' + picture + '| lolcat')
    else:
        os.system('printf ' + picture)


# Animation function
def animation(path, color):
    x=1
    for file in os.listdir(path):
        extention = ''
        if file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.png'):
            if file.endswith('.jpg'):
                extention = '.jpg'
            elif file.endswith('.jpeg'):
                extention = '.jpeg'
            else:
                extention = '.png'

            os.system('clear')
            convert(path + str(x) + extention, color)
            x += 1
            time.sleep(.05)


# loop function
def loop(path, times, color):
    x = 0
    while x < times:
        animation(path, color)
        x += 1

