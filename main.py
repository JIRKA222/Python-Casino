#!/usr/local/bin/python
# latin-1a
import os
import sys

import pip
import random as rnd
import time

import console_format
import russian_roulette


from colorama import init
init()
from colorama import Fore, Back, Style

if not 'pip' in sys.modules.keys():
    print("You need to install pip (https://pypi.org/project/pip/)")
    input()
    quit()

if not 'colorama' in sys.modules.keys():
    pip.main(['install', 'colorama'])


# __________Global Vars__________

player_name = "Player"
player_money = 500
casino_ascii_art = "   __            _          \n  / / _   _  ___| | ___   _ \n / / | | | |/ __| |/ / | | |\n/ /__| |_| | (__|   <| |_| |\n\____/\__,_|\___|_|\_\\__, |\n                      |___/ \n __________                 \n|___ /___  |                \n  |_ \  / /                 \n ___) |/ /                  \n|____//_/"
russian_names = ["Sofia", "Anastasia", "Victoria", "Ksenia", "Arina", "Elizaveta", "Adelina", "Irina", "Yelena", "Polina", "Daria", "Natalia", "Svetlana", "Vera", "Nadezhda", "Galina", "Lyubov", "Aleksandra", "Maria", "Anna", "Angelina", "Marina", "Yekaterina", "Ludmila",
                 "Tatiana", "Artyom", "Aleksandr", "Roman", "Yevgeny", "Ivan", "Maksim", "Denis", "Alexey", "Dmitry", "Danyl", "Sergey", "Nikolai", "Konstantin", "Nikita", "Mikhail", "Boris", "Victor", "Gennady", "Vyacheslav", "Vladimir", "Andrey", "Anatoly", "Ilya", "Kirill", "Oleg"]
entered_name = False
#debug_mode = False


# __________Main Game Parts Things__________

def main():
    global entered_name

    console_format.clear()
    console_format.format_setup()
    intro()
    # debug_mode_menu()
    if entered_name == False:
        name_menu()
    console_format.print_money(player_money)
    pick_game()


def intro():
    # console_format.library_info()
    print(Fore.YELLOW, end="")
    print(casino_ascii_art)
    print(Fore.WHITE)


def pick_game():
    print("Select a game:")
    print("\t[A]: Russian roulette")
    print("\t[B]: Na to neklikej")
    print("\t[ANY]: Exit")
    game_choice_input = input()

    if game_choice_input == "A" or game_choice_input == "a":
        console_format.clear()
        rr_main()
    else:
        quit()


def return_menu():
    input("Press enter to return to the main menu...")


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


#__________Russian Roulette__________

def rr_main():
    russian_roulette.print_intro()
    if console_format.is_proceed_menu() == False:
        return

    global player_name
    global player_money
    
    current_competetors = []
    current_status_of_competetors = []
    current_num_competetors = 0
    you_won = False

    current_num_competetors = console_format.input_number(
        "How many people do you wish to compete with? (5 is reccomended): ", 1)
    current_max_num_competetors = current_num_competetors

    prize_pool = 0

    for a in range(current_num_competetors):
        current_competetors.append(rnd.choice(russian_names))
        current_status_of_competetors.append(True)
        prize_pool += rnd.randint(100, 1000)
    current_competetors.append(player_name)
    current_status_of_competetors.append(True)
    print(f"You can win {prize_pool} monis.")
    print(
        f"The odds of you surviving could be {round((1 / len(current_competetors) * 100), 2)}%.")
    console_format.format_reset()
    input()

    while True:
        console_format.clear()
        i = 0
        magazine = 0
        magazine = russian_roulette.create_magazine(
            current_competetors, current_status_of_competetors)
        while i <= current_max_num_competetors:
            if current_status_of_competetors[i] == True:
                russian_roulette.print_competetor_status(
                    current_competetors, current_status_of_competetors)
                print()
                print(f"{current_competetors[i]}'s turn.", end="")
                input()
                console_format.print_loading_bar(10, 0.1)
                if i == magazine:
                    current_status_of_competetors[i] = False
                    current_num_competetors -= 1

                    console_format.clear()
                    russian_roulette.print_competetor_status(
                        current_competetors, current_status_of_competetors)
                    print()
                    print(Fore.LIGHTRED_EX + f"Bang!!!")
                    print(Fore.WHITE, end="")
                    break
                else:
                    print(f"The gun didn't fire.")
                input()
            console_format.clear()
            i += 1
        input()
        
        if current_num_competetors == 0 and current_status_of_competetors[len(current_competetors) - 1] == True:
            you_won = True
            break
        elif current_status_of_competetors[len(current_competetors) - 1] == False:
            you_won = False
            break
    if you_won == True:
        player_money += prize_pool
        russian_roulette.win_screen(current_competetors, current_status_of_competetors, player_money)
        return_menu()
    else:
        player_money = 0
        russian_roulette.lose_screen(current_competetors, current_status_of_competetors, player_money)

while True:
    main()
