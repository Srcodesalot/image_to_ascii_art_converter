# image_to_ascii_art_converter Version 2
Welcome to Image to ascii art converter or IAAC!
I built this bad boy just for fun.
Its a cool way to start working in your terminal a little more cause thats where its meant to run.
So, what it does is this. 
It takes in images, perferebly black and white however it doesnt have to be, and turns them into ascii art.
For those of you who dont know what that is just google it and itll make alot of sense. 
Not only does it have the option to create an image but also animations and loops!
To get more into how to make animations and loops read those sections below!

to just jump right in there are only a couple of things youll need to get started.

NOTE! this project uses the lolcat extention to print cool colors its super easy to just brew install. If you do not want to get the extention then simply change the l and la variables in engine.py to "" instead of " | lolcat". You will also have to take out the lolcat option in the bottom of the computer_graphics.py file.

now that thats out of the way:
first pull, then spin up a venv for in its directory, pip install the requirments.txt file. Then you can add a file (its best if its black and white) to the pictures folder and you should be good to go!

# Animations and loops 
so not to much to cover here but ill try and be thorough. Animations works just as they do in real life. so the terminal prints out pictures in a sequence to create the illusion of movment. that being said this is what you have to do to make your own:
1) make a folder inside of the "animations" folder
2)make a sequence of photos that mimic motion (perferably in Black and white) for this i used photos shop because you can make each frame on a new layer then export all the frames.
3) save those as a png, jpg or jpeg in the created folder 
4) THIS IS THE IMPORTSNT PART! animations have to be name "x.jpg" x being the frame number so your first frame should always    be "1.jpg" (whatever extention it doesnt have to be jpg it could be one of the other two aswell) for the Programming junkies it starts ar 1 not 0 !

in order to create a loop you do the same thing but put the foler you create in the loops folder.
path examples 
animation/yourAnimation
loop/yourLoop

# Important notes!
1. I built this on a mac so im not to sure if there are and breaking differences on Windows.
2. READ THE NAMING CONVEIONS OR YOUR ANIMATIONS WONT WORK 
3. This was made to use lolcat so please get it or remove those bits in the code
4. Play ariund with contrast and exposure for better quality ascii images.
6. Version notes are in the pull requests
5. Have some dang fun!


# Naming Conventions 
files must be jpg png or Jpeg unless youve made changes to the code.
animations are name "x.png" or jpg or jpeg x being the frame number 
your first frame should always be "1.jpg" or whatever extention your using 

As of March 2020 I am activly working on this so feel free to point anything out !
