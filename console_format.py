# __________Console Formating__________
from colorama import Fore, Back, Style
from colorama import init
init()

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

def library_info():
    print(Fore.MAGENTA + "You need to install colorama (https://pypi.org/project/colorama/)", end = "")
    input()
    format_reset()
    clear()
