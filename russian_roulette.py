import console_format
import random as rnd

from colorama import init
init()
from colorama import Fore, Back, Style


# __________Russian Roulette__________

def win_screen(win_list, win_status, player_money):
    console_format.clear()
    print(Fore.GREEN +
          f"As you stand next to a pile of {len(win_list) - 1} bodies, you begin wonder: What am I gonna do with this money?")
    console_format.format_reset()
    console_format.print_money(player_money)
    print_competetor_status(win_list, win_status)


def lose_screen(lost_list, lost_status, player_money):
    console_format.clear()
    print(Fore.RED + "In an unfortunate turn of events, you seem to have created a new opening in your skull.")
    console_format.format_reset()
    print_competetor_status(lost_list, lost_status)

    input()
    quit()


def print_competetor_status(competetor_list, competetor_status):
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


def create_magazine(num_competetors_load, status_of_competetors_load):
    magazine = []
    ammo_pos = 0
    while True:
        ammo_pos = rnd.randint(0, len(num_competetors_load) - 1)
        if status_of_competetors_load[ammo_pos] == True:
            break
    return ammo_pos


def debug(magazine_debug, current_competetors_debug, current_status_of_competetors_debug):
    print(f"Magazine: {magazine_debug}")
    print(f"Current competetors: {current_competetors_debug}")
    print(f"Current status: {current_status_of_competetors_debug}")


def print_intro():
    print("You are playing russian roulette.")
    print("Each round a loaded gun with one bullet is passed among the players and fired.")
    print("You always bet all your belongings.")
    print("The survivor inherits all property of the deceased.")
    print()
    print("Are you certain it is in your best interest to proceed?")
    print("\t[A]:   Yes")
    print("\t[ANY]: No")