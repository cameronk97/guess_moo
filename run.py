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

def display_main_menu(main_menu):
    chosen_option = input(f"{colorama.Fore.GREEN}{main_menu}\n>>> ").lower()

def display_game_info(game_info):
    print(f"{colorama.Fore.BLUE}{game_info}\n")

def introduction():
    print(f"{colorama.Fore.CYAN}Hi! I'm a farm animal expert.\n")
    print(f"{colorama.Fore.CYAN}I will try to guess the farm animal you're thinking of in 20 questions or less.\n")

def exit_game():
    """
    Exits the program
    """
    print(f"{colorama.Fore.MAGENTA}Now exiting the game...\n")
    print(f"{colorama.Fore.CYAN}Hope to see you again soon!\n")
    sys.exit()