from colorama import Fore, Back, Style
import console_format
import random as rnd

from colorama import init
init()

# __________Russian Roulette__________


def win_screen(win_list, win_status, money_amount):
    console_format.clear()
    print(Fore.GREEN +
          f"As you stand next to a pile of {len(win_list) - 1} bodies, you begin wonder: What am I gonna do with this money?")
    console_format.format_reset()
    print(f"You earned {money_amount} monis.")
    print_competetor_status(win_list, win_status)


def lose_screen(lost_list, lost_status, money_amount):
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
    console_format.clear()

    print("You are playing russian roulette™.")
    print("Each round a loaded gun with one bullet is passed among the players and fired.")
    print("You always bet all your belongings.")
    print("The survivor inherits all property of the deceased.")
    print()
    print("Are you certain it is in your best interest to proceed?")
    print("\t[A]:   Yes")
    print("\t[ANY]: No")


def rr_main(player_name, player_money):
    print_intro()
    if console_format.is_proceed_menu() == False:
        return 0

    current_competetors = []
    current_status_of_competetors = []
    current_num_competetors = 0
    you_won = False

    current_num_competetors = console_format.input_number(
        "How many people do you wish to compete with? (5 is reccomended): ", 1, 40)
    current_max_num_competetors = current_num_competetors

    prize_pool = 0

    for a in range(current_num_competetors):
        current_competetors.append(rnd.choice(console_format.russian_names))
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
        magazine = create_magazine(
            current_competetors, current_status_of_competetors)
        while i <= current_max_num_competetors:
            if current_status_of_competetors[i] == True:
                print_competetor_status(
                    current_competetors, current_status_of_competetors)
                print()
                print(f"{current_competetors[i]}'s turn.", end="")
                input()
                console_format.print_loading_bar(10, 0.1)
                if i == magazine:
                    current_status_of_competetors[i] = False
                    current_num_competetors -= 1

                    console_format.clear()
                    print_competetor_status(
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
        win_screen(
            current_competetors, current_status_of_competetors, prize_pool)

    else:
        lose_screen(
            current_competetors, current_status_of_competetors, prize_pool)
        prize_pool = 0

    input("Press enter to return to the main menu...")
    return prize_pool
