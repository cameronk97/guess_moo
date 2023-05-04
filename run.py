import random

import colorama
from colorama import Fore, Style

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
    typewriter(f"LET'S SEE IF I CAN GUESS THE FARM ANIMAL YOU'RE THINKING OF\n")
    input(f"{colorama.Fore.CYAN}PRESS ENTER TO START\n>>> ")

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
                game(animals_list)
                break
            elif chosen_option == "c":
                exit_game()
            else:
                raise ValueError(f"{colorama.Fore.MAGENTA}{colorama.Style.BRIGHT}Invalid input: Please enter 'a', 'b' or 'c'\n")
        except ValueError as error:
            print(error)

def display_game_info(game_info):
    """
    Print game information
    Direct users back to the main menu
    """
    print(f"{colorama.Fore.BLUE}{colorama.Style.BRIGHT}{game_info}\n")
    back_to_main = input(f"{colorama.Fore.MAGENTA}{colorama.Style.BRIGHT}Press enter to go back\n>>> ")

def introduction():
    """
    Introduce the game and prompt users to input their name
    Raise and catch ValueError if no characters or non-alphabetic characters are input for username
    """
    typewriter(f"\nHi! I'm a farm animal expert.\n")
    typewriter(f"I will try to guess the farm animal you're thinking of in 20 questions or less.\n")
    while True:
        try:
            username = input(f"{colorama.Fore.GREEN}What's your name?\n>>> ").capitalize().strip()
            if len(username) == 0:
                raise ValueError(f"{colorama.Fore.MAGENTA}{colorama.Style.BRIGHT}Invalid name: Please enter at least one character.\n")
            elif username.isalpha() != True:
                raise ValueError(f"{colorama.Fore.MAGENTA}{colorama.Style.BRIGHT}Invalid name: Please try again using alphabetic characters.\n")
            else:
                break
        except ValueError as error:
            print(error)

    while True:
        try:
            start_game_input = input(f"{colorama.Fore.BLUE}{colorama.Style.BRIGHT}Welcome {username}! Please think of a farm animal.\nPress enter when you're ready for the first question.\n>>> ")
            if len(start_game_input) == 0:
                break
            else:
                raise ValueError(f"{colorama.Fore.MAGENTA}{colorama.Style.BRIGHT}Invalid input: Please try again.\n")
        except ValueError as error:
            print(error)

def exit_game():
    """
    Exits the program
    """
    print(f"{colorama.Fore.MAGENTA}{colorama.Style.BRIGHT}Now exiting the game...\n")
    print(f"{colorama.Fore.CYAN}Hope to see you again soon!\n")
    sys.exit()

def random_trait(possible_animals, asked_traits):
    """
    Return a random trait from the dictionary keys for the first animal in the list of possible_animals
    that isn't "animal" or "probability" and hasn't already been asked
    """
    return random.choice([key for key in possible_animals[0].keys() if key != "animal" 
	                    and key != "probability" and key not in asked_traits])

def rank_animals(possible_animals, key="probability"):
    """
    Return the list of possible_animals sorted by probability from highest to lowest
    """
    return sorted(possible_animals, key=lambda x: x["probability"], reverse=True)

def compare_animals(possible_animals, asked_traits, animal1, animal2):
    """
    Declare a variable named likely_animals containing the top 3 most probable animals
    Loop through likely_animals keys for the first animal in likely_animals
    compare values for keys that aren't "animal" or "probability" and aren't in the list of asked_traits
    until differing boolean values are found for a trait
    Then assign the key found to a variable named trait and return
    """
    likely_animals = rank_animals(possible_animals, "probability")[:3]
    for key in likely_animals[0].keys():
        if key != "animal" and key != "probability" and key not in asked_traits:
            if likely_animals[animal1][key] != likely_animals[animal2][key]:
                trait = key
                return trait

# Choose the trait for the next question
def generate_question(possible_animals, asked_traits):
    """
    Return a random trait that hasn't already been asked for the first question.
    For subsequent questions return a trait based on a difference found in the most probable animals.
    Otherwise return another random trait to be used in the question.
    """
    trait = None
    # If this is the first question
    if len(asked_traits) == 0:
        # choose a random trait that isn't in asked_traits
        trait = random_trait(possible_animals, asked_traits)
        return trait
    elif len(asked_traits) > 0:
        for animal1, animal2 in [(0, 1), (0, 2), (1, 2)]:
            trait = compare_animals(possible_animals, asked_traits, animal1, animal2)
            if trait:
                return trait
    if not trait:
        return random_trait(possible_animals, asked_traits)

def ask_question(asked_traits, possible_animals):
    """
    Ask a question using generated trait
    Add asked traits to the list of asked_traits
    Validate player answers
    Convert player answers to boolean values
    """
    while True:
        trait = generate_question(possible_animals, asked_traits)
        player_answer = input(f"{colorama.Fore.CYAN}Does the animal you're thinking of {trait}? (Yes/No/I don't know)\n>>> ")
        asked_traits.append(trait)
        player_answer = player_answer.lower()
        if player_answer in VALID_ANSWERS:
            # convert player answer to boolean
            if player_answer in VALID_ANSWERS[0:2]:
                player_answer = True
                update_animal_probability(possible_animals, trait, player_answer)
                return player_answer
            elif player_answer in VALID_ANSWERS[2:4]:
                player_answer = False
                update_animal_probability(possible_animals, trait, player_answer)
                return player_answer
            elif player_answer in VALID_ANSWERS[-3:]:
                player_answer = None
                return player_answer
        else:
            print(f'{colorama.Fore.MAGENTA}{colorama.Style.BRIGHT}Invalid input: Please answer "Yes", "No" or "I don\'t know"\n')

def update_animal_probability(possible_animals, trait, player_answer):
    """
    Loop through every animal in the list of possible_animals
    and update each animal probability based on the player_answer
    Increment each matching value by 1
    and decrement each value that doesn't match by 1
    """
    for animal in possible_animals:
        if animal[trait] == player_answer:
            animal["probability"] += 1
        elif animal[trait] != player_answer:
            animal["probability"] -= 1

def make_guess(possible_animals, question_number):
    """
    Make a guess based on the most probable animal and ask the user if the guess is correct
    Print whether the animal was guessed correctly or not and how many questions were asked
    """
    # Sort the possible animals by probability
    ranked_animals = rank_animals(possible_animals, key="probability")
    while True:
        try:
            final_player_answer = input(f"{colorama.Fore.BLUE}Is the animal you're thinking of {ranked_animals[0]['animal']}? (yes/no)\n>>> ")
            if final_player_answer.lower() == "yes" or final_player_answer.lower() == "y":
                print(f"{colorama.Fore.GREEN}I knew it.\nGuessed in {question_number} questions.\nThanks for playing!\n")
                break
            elif final_player_answer.lower() == "no" or final_player_answer.lower() == "n":
                print(f"{colorama.Fore.MAGENTA}{colorama.Style.BRIGHT}Sorry, I couldn't guess the farm animal you were thinking of.\nI guess I still have a lot to learn.\n")
                break
            else:
                raise ValueError(f'{colorama.Fore.MAGENTA}{colorama.Style.BRIGHT}Invalid input: Please answer "Yes" or "No"\n')
        except ValueError as error:
            print(error)
    game_over(game_over_options)

def game(animals_list, key="probability"):
    """
    Start the game loop
    """
    # Initialize the list of asked traits
    asked_traits = []
    # Creates a copy of the animals list that can be manipulated for the duration of the game
    possible_animals = animals_list.copy()
    for animal in possible_animals:
        animal["probability"] = 1
    # Loop through 20 questions
    for i in range(20):
        question_number = i + 1
        print(f"\n{colorama.Fore.GREEN}QUESTION {question_number}:")
        while True:
            player_answer = ask_question(asked_traits, possible_animals)
            if player_answer in [True, False, None]:
                break
        # checks
        if any(animal["probability"] > 12 for animal in possible_animals):
            make_guess(possible_animals, question_number)
            break
        if any(animal["probability"] < -10 for animal in possible_animals):
            possible_animals = [animal for animal in possible_animals if animal["probability"] >= -10]
        if len(possible_animals) == 1:
            make_guess(possible_animals, question_number)
    else:
        make_guess(possible_animals, question_number)

def main():
    """
    Displays the start screen
    and main menu
    """
    start_screen(WELCOME_LOGO)
    display_main_menu(main_menu, game_info)

def game_over(game_over_options):
    """
    When a game ends, give the player 3 choices:
    * start a new game
    * return to main menu
    * exit the program
    """
    while True:
        try:
            game_over_input = input(f"{colorama.Fore.GREEN}{game_over_options}\n>>> ").lower()
            if game_over_input == "a":
                input(f"{colorama.Fore.BLUE}{colorama.Style.BRIGHT}Please think of a farm animal.\nPress enter when you're ready for the first question.\n>>> ")
                game(animals_list)
            elif game_over_input == "b":
                display_main_menu(main_menu, game_info)
            elif game_over_input == "c":
                exit_game()
            else:
                raise ValueError(f"{colorama.Fore.MAGENTA}{colorama.Style.BRIGHT}Invalid input: Please enter 'a', 'b' or 'c'\n")
        except ValueError as error:
            print(error)

main()