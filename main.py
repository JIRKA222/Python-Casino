#!/usr/local/bin/python
# latin-1a
from colorama import Fore, Back, Style
import os
import sys

import pip
import random as rnd
import time

import console_format
import russian_roulette
import coin_flip

from colorama import init
init()

if not 'pip' in sys.modules.keys():
    print("You need to install pip (https://pypi.org/project/pip/)")
    input()
    quit()

if not 'colorama' in sys.modules.keys():
    pip.main(['install', 'colorama'])


# __________Global Vars__________

player_name = "Player"
player_money = 500
entered_name = False


# __________Main Game Parts Things__________

def main():
    global entered_name

    console_format.clear()
    console_format.format_setup()
    intro()
    if entered_name == False:
        name_menu()
        intro()
    console_format.print_money(player_money)
    pick_game()


def intro():
    print(Fore.YELLOW, end="")
    print(console_format.casino_ascii_art)
    print(Fore.WHITE)


def pick_game():
    global player_money

    print("Select a game:")
    print("\t[A]: Russian roulette™")
    print("\t[B]: Coin flip advanced™ (W.I.P.)")
    print("\t[ANY]: Exit")
    game_choice_input = input()

    if game_choice_input == "A" or game_choice_input == "a":
        player_money += russian_roulette.rr_main(player_name, player_money)
    elif game_choice_input == "B" or game_choice_input == "b":
        player_money += coin_flip.cc_main(player_name, player_money)
    else:
        quit()
    console_format.clear()


def debug_mode_menu():
    print("Do you wish to enable debug mode?")
    print("\t[A]: Yes")
    print("\t[B]: No")
    entered_char = input()
    if entered_char == "A" or entered_char == "a":
        debug_mode = True
    console_format.clear()


def name_menu():
    global player_name
    global entered_name

    player_name = input("What's your name: ")
    entered_name = True
    console_format.clear()


while True:
    main()
