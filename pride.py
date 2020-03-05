#!/bin/python3

import sys
import math as m

# Escape codes
black = "\033[30m"
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m"
magenta = "\033[35m"
cyan = "\033[36m"
white = "\033[0m"

bright_black = "\033[30;1m"
bright_red = "\033[31;1m"
bright_green = "\033[32;1m"
bright_yellow = "\033[33;1m"
bright_blue = "\033[34;1m"
bright_magenta = "\033[35;1m"
bright_cyan = "\033[36;1m"
bright_white = "\033[37;1m"
reset = "\033[0m"

def cprint(c,s):
    print(c+s+reset)

# Could do with some color styling, some sort of rainbow fade would be neat.
def optprint():
    print("Options: \n")
    for x in options:
        print(x)

options = ["Lesbian", "Gay", "Bi", "Trans", "Intersex", "Asexual", "Pan"]

w = 45
h = 15

if len(sys.argv) < 2:
    optprint()
    exit()

if len(sys.argv) > 3:
    w = int(sys.argv[2])
    h = int(sys.argv[3])

sel = sys.argv[1].lower()

if sel not in {opt.lower() for opt in options}:
    optprint()
    exit()

if sel == "lesbian":
    for y in range(h):
        if (float(y) / float(h - 1)) <= 0.2:
            cprint(red, "█" * w)
        elif (float(y) / float(h - 1)) <= 0.4:
            cprint(bright_red, "█" * w)
        elif (float(y) / float(h - 1)) <= 0.6:
            cprint(white, "█" * w)
        elif (float(y) / float(h - 1)) <= 0.8:
            cprint(bright_magenta, "█" * w)
        else: 
            cprint(magenta, "█" * w)

elif sel == "gay":
    for y in range(h):
        if (float(y) / float(h - 1)) <= 1.0/6.0:
            cprint(red, "█" * w)
        elif (float(y) / float(h - 1)) <= 2.0/6.0:
            cprint(bright_red, "█" * w)
        elif (float(y) / float(h - 1)) <= 3.0/6.0:
            cprint(yellow, "█" * w)
        elif (float(y) / float(h - 1)) <= 4.0/6.0:
            cprint(bright_green, "█" * w)
        elif (float(y) / float(h - 1)) <= 5.0/6.0:
            cprint(blue, "█" * w)
        else: 
            cprint(magenta, "█" * w)

elif sel == "bi":
    for y in range(h):
        if (float(y) / float(h - 1)) <= 0.4:
            cprint(bright_magenta, "█" * w)
        elif (float(y) / float(h - 1)) <= 0.6:
            cprint(magenta, "█" * w)
        else: 
            cprint(blue, "█" * w)

elif sel == "trans":
    for y in range(h):
        if (float(y) / float(h - 1)) <= 0.2 or (float(y) / float(h - 1)) >= 0.8:
            cprint(bright_cyan, "█" * w)
        elif (float(y) / float(h - 1)) <= 0.4 or (float(y) / float(h - 1)) >= 0.6:
            cprint(bright_magenta, "█" * w)
        else: 
            cprint(white, "█" * w)

elif sel == "intersex":

    rad = w / 15

    for y in range(h):
        for x in range(w):
            dist = m.floor(m.sqrt( ((y - ((h-1)/2)) ** 2) + ((x - ((w-1)/2)) ** 2 )))
            if dist > rad and dist < rad * 2:
                print(magenta +"█" + reset, end="")
            else:
                print(yellow + "█" + reset, end="")
        print("")

elif sel == "asexual":
    for y in range(h):
        if (float(y) / float(h - 1)) <= 0.25:
            cprint(black, "█" * w)
        elif (float(y) / float(h - 1)) <= 0.5:
            cprint(bright_black, "█" * w)
        elif (float(y) / float(h - 1)) <= 0.75:
            cprint(white, "█" * w)
        else: 
            cprint(magenta, "█" * w)

elif sel == "pan":
    for y in range(h):
        if (float(y) / float(h - 1)) <= 1.0/3.0:
            cprint(bright_magenta, "█" * w)
        elif (float(y) / float(h - 1)) <= 2.0/3.0:
            cprint(bright_yellow, "█" * w)
        else: 
            cprint(bright_cyan, "█" * w)
