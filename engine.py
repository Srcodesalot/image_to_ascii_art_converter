##
# Visual class for creating ascii art work from images.
# This class handles all user interaction and "frontend" logic.
# This file was created for the purpose of learning and having fun.
# created by Aidan Gutierrez March first 2020
##

import os
import color_graphics
import time
import sys
import random

# globals
la = " | lolcat --animate"
l = " | lolcat"
command = ""
color = True


# allows users to choose the file they want
def chooseFiles (root):
    dirDict = {}
    dirList = "'"
    x = 0
    # parse through directory
    for file in os.listdir(root):
        # # grabs all folders
        if root == 'pictures/':
            if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png"):
                # creates path to picture then adds it to dict and a string
                path = root + file
                dirDict[x] = path
                dirList += str(x) + "." + file + "\n"
                x += 1

        else:
            if file.endswith(""):
                # creates path to picture then adds it to dict and a string
                path = root + file
                dirDict[x] = path + "/"
                dirList += str(x) + "." + file + "\n"
                x += 1

    dirList += "\n\n'"
    os.system("printf " + dirList + l)
    os.system("printf 'type the number of the file you would like to see?\n'" + l)
    chosenFile = number()

    if chosenFile in dirDict:
        return dirDict[chosenFile]
    else:
        os.system("printf '\n∆˚Sorry bud, that key doesnt seem to be in the list!˚∆'" + la)
        os.system("printf '\n\n∆˚Would you like to try again? (Y/N)!˚∆'" + la)
        yn = input(">")

        # lets them try again
        if "y" in yn.casefold():
            chooseFiles(root)
            return
        else:
            return

    return


# makes sure input is a number
def number():
    userNum = -1
    isnumber = False
    while not isnumber:
        try:
         userNum = int(input(">"))
         isnumber = True
        except:
            print("sorry something went wrong :( Please make sure you are only entering numbers \n")

    return userNum


#prompt for going back to menu
#this is important so we dont clog the final product
def goBack():
    global command
    command = ""
    os.system("printf 'Commands: To return to menu > back, to exit > exit, to convert another image > again  '" + l)
    while not "back" in command.casefold() and not "exit" in command.casefold() and not "again" in command.casefold():
        command = input(">")
        if "exit" in command:
            exit(0)



def colorPicker():
    global color
    color = True
    os.system("printf 'WARNING!! Animations run GREAT in black and white but SLOW in color! \n'" + la)
    os.system("printf 'would you like to print in black and white(Y/N)'" + la)
    yn = input(">")
    if "y" in yn.casefold():
        color = False


def main():
    global command

    display()

    print("")
    while not "exit" in command.casefold():
        os.system("printf '•\n"
                  " ★ To Get a picture type pic\n"
                  "•\n"
                  " ★ To run a animation type ani\n"
                  "•\n"
                  " ★ To run a loop type loop\n"
                  "•\n"
                  " ★ To create a spining animation/loop a current picture type spin\n"
                  "•\n"
                  " ★ Finally, To exit type exit\n\n' " + la)
        command = input(">")

        if "pic" in command.casefold():
            while "back" not in command:
                root = 'pictures/'
                path = chooseFiles(root)
                colorPicker()
                color_graphics.convert(path, color)
                goBack()

        elif "ani" in command.casefold():
            while "back" not in command:
                root = 'animations/'
                path = chooseFiles(root)
                colorPicker()
                color_graphics.animation(path, color)
                goBack()

        elif "loop" in command.casefold():
            while "back" not in command:
                root = 'loops/'
                path = chooseFiles(root)
                os.system("printf 'How many times would you like your loop to run'" + la)
                times = number()
                colorPicker()
                color_graphics.loop(path, times, color)
                goBack()

        elif "spin" in command.casefold():
            while "back" not in command:
                root = 'pictures/'
                path = chooseFiles(root)
                color_graphics.spin(path)
                goBack()

        else:
            if 'exit' in command.casefold():
                os.system("printf '∆˚Whoa there bud, that doesnt seem to be a command!˚∆'" + la)


#Just for looks!
def display():
    os.system('clear')
    target = "~~ WELCOME TO GRAPHICTERM ~~"
    targetA = list(target)
    guessA = [''] * len(targetA)

    x = 0
    while guessA != targetA:
        i = 0
        guess = ''
        while i < len(guessA):
            if guessA[i] == targetA[i]:
                pointless = 0
            else:
                guessA[i] = random.choice("≈~1234567890-=qwertyuiop[]\ asdfghjkl;'zxcvbnm,./!@#$%^&*()+QWERTYUIOP{}|ASDFGHJKL:ZXCVBNM<>?")
            guess += guessA[i]
            i += 1

        sys.stdout.write(f'\r{guess}')
        sys.stdout.flush()
        time.sleep(0.006)

    os.system('clear')
    os.system("printf '~~ WELCOME TO GRAPHICTERM ~~\n' " + la)

main()