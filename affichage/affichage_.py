import os
import time

class bcolors:
    cyan = '\033[96m'
    ver = '\033[92m'
    jaune = '\033[93m'
    rouge = '\033[91m'
    ENDC = '\033[0m'

def clear_terminal():
    if os.name == 'nt':
        os.system('cls')

def print_labyrinthe (labyrinthe) :
    clear_terminal ()
    for line in labyrinthe:
        for c in line :
            if c == "#" :
                print(f"{bcolors.jaune}#{bcolors.ENDC}", end="")
            elif c == "." :
                print(f"{bcolors.cyan}.{bcolors.ENDC}", end="")
            elif c == "o" :
                print(f"{bcolors.ver}o{bcolors.ENDC}", end="")
            elif c == "*" :
                print(f"{bcolors.rouge}*{bcolors.ENDC}", end="")
        print("")
    time.sleep (0.4)
