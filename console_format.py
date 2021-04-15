from colorama import Fore, Back, Style
import time

from colorama import init
init()

# __________Fancy Variables__________

casino_ascii_art = "  _                _             ____ ______ \n | |              | |           |___ \____  |\n | |    _   _  ___| | ___   _     __) |  / / \n | |   | | | |/ __| |/ / | | |   |__ <  / /  \n | |___| |_| | (__|   <| |_| |   ___) |/ /   \n |______\__,_|\___|_|\_\\__, |  |____//_/    \n                         __/ |               \n                        |___/                "
russian_names = ["Sofia", "Anastasia", "Victoria", "Ksenia", "Arina", "Elizaveta", "Adelina", "Irina", "Yelena", "Polina", "Daria", "Natalia", "Svetlana", "Vera", "Nadezhda", "Galina", "Lyubov", "Aleksandra", "Maria", "Anna", "Angelina", "Marina", "Yekaterina", "Ludmila",
                 "Tatiana", "Artyom", "Aleksandr", "Roman", "Yevgeny", "Ivan", "Maksim", "Denis", "Alexey", "Dmitry", "Danyl", "Sergey", "Nikolai", "Konstantin", "Nikita", "Mikhail", "Boris", "Victor", "Gennady", "Vyacheslav", "Vladimir", "Andrey", "Anatoly", "Ilya", "Kirill", "Oleg"]

# __________Console Formating__________

def clear():
    print('\x1b[2J', end="")


def format_reset():
    print(Style.RESET_ALL, end="")
    #print(Style.BRIGHT, end="")


def input_number(input_message, min_value, max_value):
    input_number_returned = 0

    while True:
        try:
            input_number_returned = int(input(input_message))
        except:
            clear()
            print("Please enter a number.")
            input()
            clear()
        else:
            if input_number_returned >= min_value and input_number_returned <= max_value:
                return input_number_returned
            else:
                clear()
                print(
                    f"Please enter a number greater than {min_value - 1} and smaller than {max_value + 1}.")
                input()
                clear()


def input_binary(input_message):
    input_binary = ""
    is_aok = False

    while is_aok == False:
        is_aok = True
        input_binary = input(input_message)

        clear()
        if input_binary == "":
            print("Enter a series of 0s and 1s.")
            input()
            is_aok = False
        else:
            for i in input_binary:
                if i != "0" and i != "1":
                    
                    print("Enter a series of 0s and 1s.")
                    input()
                    is_aok = False
                    break
        clear()

    return input_binary


def print_loading_bar(length, delay_between_steps):
    i = 0
    while i <= length:
        print("#", end="")
        time.sleep(delay_between_steps)
        i += 1
    print()


def library_info():
    print(Fore.MAGENTA +
          "You need to install colorama (https://pypi.org/project/colorama/)", end="")
    input()
    format_reset()
    clear()


def print_money(amount):
    print(f"You have {amount} monis.")


def is_proceed_menu():
    entered_char = input()
    clear()
    if entered_char == "A" or entered_char == "a":
        return True
    else:
        return False

def want_to_continue(game_name):
    print(f"Do you want to continue playing {game_name}?")
    print("\t[A] Yes")
    print("\t[ANY] No")

    return is_proceed_menu()
