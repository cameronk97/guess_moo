import random

import colorama
from colorama import Fore

from game_art import *
from extras import typewriter
from animals import animals_list

colorama.init(autoreset=True)

VALID_ANSWERS = ["yes", "y", "no", "n", "i don't know", "idk", "i dont know"]

def start_screen(WELCOME_LOGO):
    """
    Print game logo
    imported locally from game_art.py
    and welcome message with typewriter effect
    prompt player to press enter to start
    """
    print(f"{colorama.Fore.GREEN}{WELCOME_LOGO}\n")
    typewriter(f"{colorama.Fore.CYAN}LET'S SEE IF I CAN GUESS THE FARM ANIMAL YOU'RE THINKING OF\n")
    input(f"{colorama.Fore.WHITE}PRESS ENTER TO START\n>>> ")

def display_main_menu(main_menu, game_info):
    #not sure if i need game-info as a parameter here
    """
    Display main game menu with 3 options for users:
        a) Game Information
        b) Play Game
        c) Exit the program
    Raise and catch ValueError if the user input is not 'a', 'b' or 'c'
    """
    while True:
        try:
            chosen_option = input(f"{colorama.Fore.GREEN}{main_menu}\n>>> ").lower()
            if chosen_option == "a":
                display_game_info(game_info)
                continue
            elif chosen_option == "b":
                introduction()
                game(animals)
                break
            elif chosen_option == "c":
                exit_game()
            else:
                raise ValueError(f"{colorama.Fore.MAGENTA}Invalid input: Please enter 'a', 'b' or 'c'\n")
        except ValueError as error:
            print(error)

def display_game_info(game_info):
    """
    Print game information
    Direct users back to the main menu
    """
    print(f"{colorama.Fore.BLUE}{game_info}\n")
    back_to_main = input(f"{colorama.Fore.MAGENTA}Press enter to go back\n>>> ")

def introduction():
    print(f"{colorama.Fore.CYAN}Hi! I'm a farm animal expert.\n")
    print(f"{colorama.Fore.CYAN}I will try to guess the farm animal you're thinking of in 20 questions or less.\n")
    while True:
        try:
            username = input(f"{colorama.Fore.GREEN}What's your name?\n>>> ").capitalize().strip()
            if len(username) == 0:
                raise ValueError(f"{colorama.Fore.MAGENTA}Invalid name: Please enter at least one character.\n")
            elif username.isalpha() != True:
                raise ValueError(f"{colorama.Fore.MAGENTA}Invalid name: Please try again using alphabetic characters.\n")
            else:
                break
        except ValueError as error:
            print(error)

def exit_game():
    """
    Exits the program
    """
    print(f"{colorama.Fore.MAGENTA}Now exiting the game...\n")
    print(f"{colorama.Fore.CYAN}Hope to see you again soon!\n")
    sys.exit()