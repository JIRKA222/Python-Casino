#!/usr/local/bin/python
# latin-1a
import os
import sys

import random as rnd
import time

import console_format

from colorama import Fore, Back, Style
from colorama import init

# __________Global Vars__________
player_name = "Player"
player_money = 500
casino_ascii_art = " _    _      _                            _          _   _           \n| |  | |    | |                          | |        | | | |          \n| |  | | ___| | ___ ___  _ __ ___   ___  | |_ ___   | |_| |__   ___  \n| |/\| |/ _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \  | __| '_ \ / _ \ \n\  /\  /  __/ | (_| (_) | | | | | |  __/ | || (_) | | |_| | | |  __/ \n \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/   \__|_| |_|\___| \n                                                                     \n                                                                     \n _     _   _ _____  _   ____   __  _____ _____                       \n| |   | | | /  __ \| | / /\ \ / / |____ |  _  |                      \n| |   | | | | /  \/| |/ /  \ V /      / /\ V /                       \n| |   | | | | |    |    \   \ /       \ \/ _ \                       \n| |___| |_| | \__/\| |\  \  | |   .___/ / |_| |                      \n\_____/\___/ \____/\_| \_/  \_/   \____/\_____/                      "
russian_names = ["Sofia", "Anastasia", "Victoria", "Ksenia", "Arina", "Elizaveta", "Adelina", "Irina", "Yelena", "Polina", "Daria", "Natalia", "Svetlana", "Vera", "Nadezhda", "Galina", "Lyubov", "Aleksandra", "Maria", "Anna", "Angelina", "Marina", "Yekaterina", "Ludmila",
                 "Tatiana", "Artyom", "Aleksandr", "Roman", "Yevgeny", "Ivan", "Maksim", "Denis", "Alexey", "Dmitry", "Danyl", "Sergey", "Nikolai", "Konstantin", "Nikita", "Mikhail", "Boris", "Victor", "Gennady", "Vyacheslav", "Vladimir", "Andrey", "Anatoly", "Ilya", "Kirill", "Oleg"]
entered_name = False
#debug_mode = False

# __________Main Game Parts Things__________


def main():
    global entered_name

    console_format.clear()
    console_format.format_setup()
    print("(You need colorama (https://pypi.org/project/colorama/))")
    intro()
    # debug_mode_menu()
    if entered_name == False:
        name_menu()
    pick_game()


def intro():
    print(casino_ascii_art)
    print()
    print_money()


def pick_game():
    print("Select a game:")
    print("\t[A]: Russian rulette�")
    print("\t[B]: Na to neklikej")
    print("\t[C]: Exit")
    game_choice_input = input()

    if game_choice_input == "A" or game_choice_input == "a":
        console_format.clear()
        rr_intro()
    elif game_choice_input != "C" and game_choice_input != "c":
        main()


def return_menu():
    input("Press enter to return to the main menu...")
    main()


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

# __________Misc__________


def input_number(input_message, min_value):
    input_number_returned = 0

    while True:
        try:
            input_number_returned = int(input(input_message))
        except:
            console_format.clear()
            print("Please enter a number.")
        else:
            if input_number_returned >= min_value:
                return input_number_returned
            else:
                print(f"Please enter a number greater than {min_value - 1}.")


def print_loading_bar(length, delay_between_steps):
    i = 0
    while i <= length:
        print("#", end="")
        time.sleep(delay_between_steps)
        i += 1
    print()


def print_money():
    print(f"You have {player_money} moneys.")

# __________Russian Rullete__________


def rr_win_screen(win_list, win_status):
    console_format.clear()
    print(Fore.GREEN +
          f"As you stand next to a pile of {len(win_list)} bodies, you begin wonder: What am I gonna do with this money?")
    console_format.format_reset()
    print_money()
    rr_print_competetor_status(win_list, win_status)


def rr_lose_screen(lost_list, lost_status):
    console_format.clear()
    print(Fore.RED + "In an unfortunate turn of events, you seem to have created a new opening in your skull.")
    console_format.format_reset()
    rr_print_competetor_status(lost_list, lost_status)


def rr_print_competetor_status(competetor_list, competetor_status):
    i = 0
    print("Status of competitors: ")
    while i < len(competetor_list):
        if len(competetor_list[i]) >= 8:
            print(competetor_list[i], end="\t")
        else:
            print(competetor_list[i], end="\t\t")

        if competetor_status[i] == True:
            print(Fore.GREEN + "ALIVE")
            print(Fore.WHITE, end="")
        else:
            print(Fore.RED + "DEAD")
            print(Fore.WHITE, end="")
        i += 1


def rr_load_magazine(num_competetors_load, status_of_competetors_load):
    magazine = []
    ammo_pos = 0
    while True:
        ammo_pos = rnd.randint(0, len(num_competetors_load) - 1)
        if status_of_competetors_load[ammo_pos] == True:
            break
    return ammo_pos


def rr_debug(magazine_debug, current_competetors_debug, current_status_of_competetors_debug):
    print(f"Mafazine: {magazine_debug}")
    print(f"Current competetors: {current_competetors_debug}")
    print(f"Current status: {current_status_of_competetors_debug}")


def rr_intro():
    print("You are playing russian rulette�.")
    print("Each round a loaded gun with one bullet is passed among the players and fired.")
    print("You always bet all your belongings.")
    print("The survivor inherits all property of the diceased.")
    print()
    print("Are you certain it is in your best interest to proceed?")
    print("\t[A]:   Yes")
    print("\t[Any]: No")

    entered_char = input()
    console_format.clear()
    if entered_char == "A" or entered_char == "a":
        rr_main()
    else:
        return_menu()


def rr_main():
    current_competetors = []
    current_status_of_competetors = []
    current_num_competetors = 0
    you_won = False

    global player_name
    global player_money

    current_num_competetors = input_number(
        "How many people do you wish to compete with? (5 is reccomended): ", 1)
    current_max_num_competetors = current_num_competetors

    prize_pool = 0

    for a in range(current_num_competetors):
        current_competetors.append(rnd.choice(russian_names))
        current_status_of_competetors.append(True)
        prize_pool += rnd.randint(100, 1000)
    current_competetors.append(player_name)
    current_status_of_competetors.append(True)
    print(f"You can win {prize_pool} moneys.")
    print(
        f"The odds of you surviving are not {round((1 / len(current_competetors) * 100), 2)}%.")
    input()

    while True:
        console_format.clear()
        i = 0
        magazine = 0
        magazine = rr_load_magazine(
            current_competetors, current_status_of_competetors)

        while i <= current_max_num_competetors:
            if current_status_of_competetors[i] == True:
                rr_print_competetor_status(
                    current_competetors, current_status_of_competetors)
                print()
                print(f"{current_competetors[i]}'s turn.", end="")
                input()
                print_loading_bar(10, 0.1)
                if i == magazine:
                    current_status_of_competetors[i] = False
                    current_num_competetors -= 1

                    console_format.clear()
                    rr_print_competetor_status(
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
        rr_win_screen(current_competetors, current_status_of_competetors)
        return_menu()
    else:
        player_money = 0
        rr_lose_screen(current_competetors, current_status_of_competetors)


main()
