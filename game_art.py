import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)
WELCOME_LOGO = r"""
                    WELCOME TO
  ____ _   _ _____ ____ ____    __  __  ___   ___
 / ___| | | | ____/ ___/ ___|  |  \/  |/ _ \ / _ \
| |  _| | | |  _| \___ \___ \  | |\/| | | | | | | |
| |_| | |_| | |___ ___) |__) | | |  | | |_| | |_| |
 \____|\___/|_____|____/____/  |_|  |_|\___/ \___/

           THE FARM ANIMAL GUESSING GAME
"""

main_menu = """
PLEASE SELECT AN OPTION:

     a) GAME INFO
     b) PLAY GAME
     c) EXIT

"""

game_info = """
    ==================================================================
   ||                                                                ||
   ||                                                                ||
   ||                       G A M E   I N F O                        ||
   ||                     ---------------------                      ||
   ||                                                                ||
   ||                                                                ||
   ||             * The player thinks of a farm animal               ||
   ||                                                                ||
   ||                                                                ||
   ||        * The computer asks up to 20 yes or no questions        ||
   ||                                                                ||
   ||                                                                ||
   ||            * The computer attempts to guess which              ||
   ||              farm animal the player is thinking of             ||
   ||                                                                ||
   ||                                                                ||
   ||                                                                ||
    ==================================================================
"""
BORDER = (f"{Fore.MAGENTA}{Style.BRIGHT}\n"
          f"* * * * * * * * * * * * * * * * * * * * "
          f"* * * * * * * * * * * * * * * * * * * *\n")

game_over_options = """
PLEASE SELECT AN OPTION:

     a) PLAY AGAIN
     b) GAME INFO
     c) EXIT

"""
