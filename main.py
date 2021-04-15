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


# __________Not So Global Vars__________

player_name = "Player"
player_money = 500
entered_name = False


# __________Main Game Parts Things__________

def main(player_money, player_name, entered_name):
    console_format.clear()
    console_format.format_reset()
    intro()
    if entered_name == False:
        player_name, entered_name = name_menu(player_name, entered_name)
        intro()
    console_format.print_money(player_money)

    if player_money <= 0:
        print("You have been kicked out the casino, because you are broke.")
        input()
        quit()
    player_money += pick_game(player_name, player_money)

    return player_money, player_name, entered_name


def intro():
    print(Fore.YELLOW, end="")
    print(console_format.casino_ascii_art)
    print(Fore.WHITE)


def pick_game(player_name, player_money):
    returned_money = 0

    print("Select a game:")
    print("\t[A]: Russian roulette™")
    print("\t[B]: Coin flip advanced™")
    print("\t[ANY]: Exit")
    game_choice_input = input()

    if game_choice_input == "A" or game_choice_input == "a":
        returned_money += russian_roulette.rr_main(player_name, player_money)
    elif game_choice_input == "B" or game_choice_input == "b":
        returned_money += coin_flip.cc_main(player_name, player_money)
    else:
        quit()
    console_format.clear()
    return returned_money


def name_menu(player_name, entered_name):
    player_name = input("What's your name: ")
    entered_name = True
    console_format.clear()

    return player_name, entered_name


while True:
    player_money, player_name, entered_name = main(
        player_money, player_name, entered_name)
