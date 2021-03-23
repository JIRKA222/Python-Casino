import random as rnd
import console_format
from colorama import Fore, Back, Style
from colorama import init
init()


def intro():
    console_format.clear()

    print("You are play coin flip advanced™. Yay")
    print("\t[A]:   Yes")
    print("\t[ANY]: No")

def betting_info():
    print("The amount of monis you win is determined by the amount of coin flips predicted:")
    print("\t1  Flips: 2x    monis.")
    print("\t2  Flips: 4x    monis.")
    print("\t3  Flips: 8x    monis.")
    print("\t4  Flips: 16x   monis.")
    print("\t5  Flips: 32x   monis.")
    print("\t6  Flips: 64x   monis.")
    print("\t7  Flips: 128x  monis.")
    print("\t8  Flips: 256x  monis.")
    print("\t9  Flips: 512x  monis.")
    print("\t10 Flips: 1024x monis.")


def win_screen(amount):
    print(Fore.GREEN, end="")
    print(f"You won {amount} monis.")
    console_format.format_reset()


def lose_screen(amount):
    print(Fore.RED, end="")
    print(f"You lost {amount} monis.")
    console_format.format_reset()


def int_into_bool_array(binary_str):
    prediction_array = []
    for i in binary_str:
        if i == "1":
            prediction_array.append(True)
        elif i == "0":
            prediction_array.append(False)
    return prediction_array


def get_dice_roll(number_of_throws):
    dice_roll_array = []

    for i in range(number_of_throws):
        dice_roll_array.append(rnd.choice([True, False]))

    return dice_roll_array


def cc_main(player_name, player_money):
    you_won = True
    betted_money = 0
    num_of_turns = 0
    prediction = []
    dice_roll = []

    intro()
    if console_format.is_proceed_menu() == False:
        return 0
    console_format.clear()

    betted_money = console_format.input_number(
        f"How much many monis do you want to bet? (You have {player_money} monis): ", 5, player_money)

    console_format.clear()

    prediction = int_into_bool_array(input(
        "Enter ur prediction. 1 for heads and 0 for tails. (example: 01001): "))
    num_of_turns = len(prediction)
    dice_roll = get_dice_roll(num_of_turns)

    for i in range(0, num_of_turns):
        console_format.clear()

        if prediction[i] == True:
            print("You prediction: heads. ", end="")
        else:
            print("Your prediction: tails ", end="")

        input()

        console_format.print_loading_bar(10, 0.1)
        if prediction[i] == dice_roll[i]:
            print(Fore.GREEN, end="")
            if dice_roll[i] == True:
                print("It's heads. ")
            else:
                print("It's tails. ")

            input()

            console_format.clear()
            console_format.format_reset()
        else:
            print(Fore.RED, end="")
            if dice_roll[i] == True:
                print("It's heads. ")
            else:
                print("It's tails. ")
            
            input()

            console_format.clear()
            console_format.format_reset()

            you_won = False
            break

    if you_won == True:
        win_screen()
        input()
        return betted_money
    else:
        lose_screen()
        input()
        return -betted_money
