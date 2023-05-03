import colorama
from colorama import Fore

from extras import *

colorama.init(autoreset=True)

WELCOME_LOGO = """
                    WELCOME TO
  ____ _   _ _____ ____ ____    __  __  ___   ___  
 / ___| | | | ____/ ___/ ___|  |  \/  |/ _ \ / _ \ 
| |  _| | | |  _| \___ \___ \  | |\/| | | | | | | |
| |_| | |_| | |___ ___) |__) | | |  | | |_| | |_| |
 \____|\___/|_____|____/____/  |_|  |_|\___/ \___/ 

           THE FARM ANIMAL GUESSING GAME
""".center(51)

main_menu = """
PLEASE SELECT AN OPTION:

     a) GAME INFO
     b) PLAY GAME
     c) EXIT

""".center(24)

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

game_over_options = """
PLEASE SELECT AN OPTION:

     a) PLAY AGAIN
     b) MAIN MENU
     c) EXIT

""".center(24)