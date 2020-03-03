from PIL import Image
import os
import time
import sys

def resize(path):
    image = path
    # opens image and assigns it to new variable to preserve original
    originImg = Image.open(image, 'r')
    tempImg = originImg

    # resize with thumbnail caps the size at 100 pixels wide or long and resizes the image propotianally
    tempImg.thumbnail((100, 100), Image.LANCZOS)
    width, height = tempImg.size

    # This resize squishes the picture a bit to minimize elongation
    # This along with the skipline variable cuts out elongation whithout distorting the picture too much
    tempImg = tempImg.resize((width, height - 10), )
    print(tempImg.size)

    return tempImg

def convert(path, color):
    image = resize(path)
    width, height = image.size
    # create a list out or pixel rgb values
    pix_val = list(image.getdata())
    x = 0
    skipLine = False

    # initialize the picture string.
    picture = "'"

    # for every single pixel we will observe the R value (red) and determine how dark that pixel is.
    # Then assign an approprite ascii character.
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
                #picture = picture + random.choice("QWERTYUIOPASDFGHJKLZXCVBNM") // this prints random letters
            else:
                picture = picture + " "
        else:
            picture = picture + ""

        # This portion deals with the skip line variable.
        # It skips printing every other line to reduce enlongation of an image.
        # Elongation is due to the fact that a pixel is smaller than a character.
        x += 1
        if x % width == 0 and x != 0:
            if not skipLine:
                picture = picture + "\n"
            skipLine = not skipLine

    # close picture string
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


# loop function
# this turnes a still into a spining animation
def spin(path):
    loading = [" "," "," "," "," "," "," "," "," "," "," "," "," "]

    # open the image using its path
    image = resize(path)

    # creates new path in the animations and loops folders
    folderName = path.split("/")
    folderName = folderName[1].split(".")
    aniPath = "animations/" + folderName[0] + "/"
    loopPath = "loops/" + folderName[0] + "/"
    os.system("mkdir " + aniPath)
    os.system("mkdir " + loopPath)

    # create a new image so we dont ruin the original
    wreckedImg = image

    # rotate picture 30 degrees 12 times to get a full circle
    # x is set to 1 in order to follow naming conventions for animations
    x = 1
    while x <= 13:
        #create file name to follow convention
        filename = str(x) + '.' + folderName[1]
        newImg = wreckedImg.rotate(30, resample=Image.BILINEAR, expand=False)
        newImg.save(aniPath + filename)
        newImg.save(loopPath + filename)
        wreckedImg = newImg
        loading[x - 1] = '#'
        x += 1
        sys.stdout.write(f'\r{loading}')

    animation(aniPath,False)



# spin("pictures/ghostBusters.jpeg")