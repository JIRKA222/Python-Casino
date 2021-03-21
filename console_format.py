import time

from colorama import init
init()
from colorama import Fore, Back, Style


# __________Console Formating__________

def clear():
    print('\x1b[2J', end="")


def format_setup():
    print(Style.BRIGHT, end="")


def format_reset():
    print(Style.RESET_ALL, end="")
    print(Style.BRIGHT, end="")


def input_number(input_message, min_value):
    input_number_returned = 0

    while True:
        try:
            input_number_returned = int(input(input_message))
        except:
            clear()
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


def library_info():
    print(Fore.MAGENTA +
          "You need to install colorama (https://pypi.org/project/colorama/)", end="")
    input()
    format_reset()
    clear()


def print_money(amount):
    print(f"You have {amount} monis.")


def input_number(input_message, min_value):
    input_number_returned = 0

    while True:
        try:
            input_number_returned = int(input(input_message))
        except:
            clear()
            print("Please enter an integer.")
        else:
            if input_number_returned >= min_value:
                return input_number_returned
            else:
                
                clear()
                print(f"Please enter an integer greater than {min_value - 1}.")


def is_proceed_menu():
    entered_char = input()
    clear()
    if entered_char == "A" or entered_char == "a":
        return True
    else:
        return False
