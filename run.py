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