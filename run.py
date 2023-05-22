import os
import sys
import random

import colorama
from colorama import Fore, Style

from game_art import *
from extras import typewriter, clear
from animals import animals_list

colorama.init(autoreset=True)

VALID_ANSWERS = ["yes", "y", "no", "n", "i don't know", "idk", "i dont know"]


def start_screen(WELCOME_LOGO):
    """
    Prints the game logo,
    which is provided as a parameter.
    Prints a welcome message with a typewriter effect.
    Prompts players to press enter to start.
    Clears the mock terminal screen.
    """
    print(f"{Fore.GREEN}{Style.NORMAL}{WELCOME_LOGO}\n")
    typewriter(f"LET'S SEE IF I CAN READ YOUR MIND\n")
    input(f"{colorama.Fore.CYAN}PRESS ENTER TO START\n>>> ")
    clear()


def display_main_menu(VALID_ANSWERS, main_menu):
    """
    Display main game menu with 3 options for users:
        a) GAME INFO
        b) PLAY GAME
        c) EXIT
    Raise and catch ValueError if the user input is not 'a', 'b' or 'c'
    """
    while True:
        try:
            chosen_option = input(f"{Fore.GREEN}{Style.NORMAL}"
                                  f"{main_menu}\n>>> ").lower()
            if chosen_option == "a":
                display_game_info(game_info)
                continue
            elif chosen_option == "b":
                introduction()
                game(VALID_ANSWERS, animals_list)
                break
            elif chosen_option == "c":
                exit_game()
            else:
                raise ValueError(f"{Fore.MAGENTA}{Style.BRIGHT}"
                                 f"Invalid input: Please enter"
                                 f" 'a', 'b' or 'c'\n")
        except ValueError as error:
            print(error)


def display_game_info(game_info):
    """
    Print game information
    Direct users back to the main menu
    Clear the mock terminal
    """
    clear()
    print(f"{Fore.BLUE}{Style.BRIGHT}{game_info}\n")
    input(f"{Fore.MAGENTA}{Style.BRIGHT}"
          f"Press enter to go back\n>>> ")
    clear()


def introduction():
    """
    Introduce the game and prompt users to input their name
    Raise and catch ValueError if no characters
    or non-alphabetic characters are input for username
    """
    typewriter(f"\nHi! I'm a farm animal expert.\n")
    typewriter(f"I will try to guess the farm animal you're"
               f" thinking of in 20 questions or less.\n\n")
    while True:
        try:
            username = input(f"{Fore.GREEN}{Style.NORMAL}"
                             f"What's your name?\n>>> ").capitalize().strip()
            if len(username) == 0:
                raise ValueError(f"{Fore.MAGENTA}{Style.BRIGHT}"
                                 f"Invalid name: "
                                 f"Please enter at least one character.\n")
            elif username.isalpha() != True:
                raise ValueError(f"{Fore.MAGENTA}{Style.BRIGHT}"
                                 f"Invalid name: Please try again "
                                 f"using alphabetic characters.\n")
            else:
                break
        except ValueError as error:
            print(error)

    while True:
        try:
            start_game_input = input(f"{Fore.BLUE}{Style.BRIGHT}\n"
                                     f"Welcome {username}!\n"
                                     f"Please think of a farm animal."
                                     f"\nPress enter when you're ready"
                                     f" for the first question.\n>>> ")
            if len(start_game_input) == 0:
                break
            else:
                raise ValueError(f"{Fore.MAGENTA}{Style.BRIGHT}"
                                 f"Invalid input: Please try again.\n")
        except ValueError as error:
            print(error)


def exit_game():
    """
    Exits the program
    """
    print(f"{Fore.MAGENTA}{Style.BRIGHT}Now exiting the game...\n")
    print(f"{Fore.CYAN}{Style.NORMAL}Hope to see you again soon!\n")
    sys.exit()


def random_trait(possible_animals, asked_traits):
    """
    Return a random trait from the dictionary keys
    for the first animal in the list of possible_animals
    that isn't "animal" or "probability" and hasn't already been asked
    """
    return random.choice([key for key in possible_animals[0].keys() 
                        if key != "animal" and key != "probability" 
                        and key not in asked_traits])


def rank_animals(possible_animals, key="probability"):
    """
    Return the list of possible_animals
    sorted by probability from highest to lowest
    """
    return sorted(possible_animals, key=lambda x: x["probability"], reverse=True)


def compare_animals(possible_animals, asked_traits, animal1, animal2):
    """
    Declare a variable named likely_animals
    containing the top 3 most probable animals
    Loop through likely_animals keys for the first animal in likely_animals
    compare values for keys that aren't "animal" or "probability"
    and aren't in the list of asked_traits
    until differing boolean values are found for a trait
    Then assign the key found to a variable named trait and return
    """
    likely_animals = rank_animals(possible_animals, "probability")[:3]
    for key in likely_animals[0].keys():
        if key != "animal" and key != "probability" and key not in asked_traits:
            if likely_animals[animal1][key] != likely_animals[animal2][key]:
                trait = key
                return trait


def generate_question(possible_animals, asked_traits):
    """
    Return a random trait that hasn't already been asked for the first question.
    For subsequent questions return a trait based on
    a difference found in the most probable animals.
    Otherwise return another random trait to be used in the question.
    """
    trait = None
    if len(asked_traits) == 0:
        trait = random_trait(possible_animals, asked_traits)
        return trait
    elif len(asked_traits) > 0:
        for animal1, animal2 in [(0, 1), (0, 2), (1, 2)]:
            trait = compare_animals(possible_animals, asked_traits, animal1, animal2)
            if trait:
                return trait
    if not trait:
        return random_trait(possible_animals, asked_traits)


def ask_question(VALID_ANSWERS, asked_traits, possible_animals):
    """
    Ask a question using generated trait
    Add asked traits to the list of asked_traits
    Validate player answers
    Convert player answers to boolean values
    """
    while True:
        trait = generate_question(possible_animals, asked_traits)
        player_answer = input(f"{Fore.CYAN}{Style.NORMAL}"
                              f"Does the animal you're thinking of {trait}?"
                              f" (Yes/No/I don't know)\n>>> ")
        player_answer = player_answer.lower()
        if player_answer in VALID_ANSWERS:
            if player_answer in VALID_ANSWERS[0:2]:
                player_answer = True
                asked_traits.append(trait)
                update_animal_probability(possible_animals, trait, player_answer)
                return player_answer
            elif player_answer in VALID_ANSWERS[2:4]:
                player_answer = False
                asked_traits.append(trait)
                update_animal_probability(possible_animals, trait, player_answer)
                return player_answer
            elif player_answer in VALID_ANSWERS[-3:]:
                player_answer = None
                asked_traits.append(trait)
                return player_answer
        else:
            print(f'{Fore.MAGENTA}{Style.BRIGHT}'
                  f'Invalid input: Please answer "Yes", "No" or "I don\'t know"\n')


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


def make_guess(possible_animals, question_number, VALID_ANSWERS):
    """
    Make a guess based on the most probable animal
    and ask the user if the guess is correct
    Print whether the animal was guessed correctly or not
    and how many questions were asked
    """
    ranked_animals = rank_animals(possible_animals, key="probability")
    while True:
        try:
            final_player_answer = input(f"{Fore.BLUE}{Style.BRIGHT}"
                                        f"\nIs the animal you're thinking of "
                                        f"{ranked_animals[0]['animal']}?"
                                        f" (yes/no)\n>>> ").lower()
            if final_player_answer == "yes" or final_player_answer == "y":
                print(f"{Fore.CYAN}\nI knew it."
                      f"\nGuessed in {question_number} questions."
                      f"\nThanks for playing!\n")
                break
            elif final_player_answer == "no" or final_player_answer == "n":
                print(f"{Fore.MAGENTA}{Style.BRIGHT}\n"
                      f"Sorry, I couldn't guess the farm animal"
                      f" you were thinking of.\n"
                      f"I guess I still have a lot to learn.\n")
                break
            else:
                raise ValueError(f'{Fore.MAGENTA}{Style.BRIGHT}'
                                 f'Invalid input: '
                                 f'Please answer "Yes" or "No"\n')
        except ValueError as error:
            print(error)
    game_over(game_over_options, VALID_ANSWERS)


def game(VALID_ANSWERS, animals_list, key="probability"):
    """
    Start the game loop
    """
    asked_traits = []
    possible_animals = animals_list.copy()
    for animal in possible_animals:
        animal["probability"] = 1
    clear()
    for i in range(20):
        print("\n" + BORDER)
        question_number = i + 1
        print(f"\n{Fore.GREEN}{Style.BRIGHT}QUESTION {question_number}:")
        while True:
            player_answer = ask_question(VALID_ANSWERS,
                                         asked_traits, possible_animals)
            if player_answer in [True, False, None]:
                break
        if any(animal["probability"] > 12 for animal in possible_animals):
            print("\n" + BORDER)
            make_guess(possible_animals, question_number, VALID_ANSWERS)
            break
        if any(animal["probability"] < -10 for animal in possible_animals):
            possible_animals = [animal for animal in possible_animals
                                if animal["probability"] >= -10]
        if len(possible_animals) == 1:
            print("\n" + BORDER)
            make_guess(possible_animals, question_number, VALID_ANSWERS)
    else:
        print("\n" + BORDER)
        make_guess(possible_animals, question_number, VALID_ANSWERS)


def main(VALID_ANSWERS):
    """
    Displays the start screen
    and main menu
    """
    start_screen(WELCOME_LOGO)
    display_main_menu(VALID_ANSWERS, main_menu)


def game_over(game_over_options, VALID_ANSWERS):
    """
    When a game ends, give the player 3 choices:
        * PLAY AGAIN
        * GAME INFO
        * EXIT
    """
    while True:
        try:
            game_over_input = input(f"{Fore.GREEN}{Style.NORMAL}"
                                    f"{game_over_options}\n>>> ").lower()
            if game_over_input == "a":
                clear()
                input(f"{Fore.BLUE}{Style.BRIGHT}"
                      f"Please think of a farm animal.\n"
                      f"Press enter when you're ready "
                      f"for the first question.\n>>> ")
                game(VALID_ANSWERS, animals_list)
            elif game_over_input == "b":
                display_game_info(game_info)
            elif game_over_input == "c":
                exit_game()
            else:
                raise ValueError(f"{Fore.MAGENTA}{Style.BRIGHT}"
                                 f"Invalid input: "
                                 f"Please enter 'a', 'b' or 'c'\n")
        except ValueError as error:
            print(error)


main(VALID_ANSWERS)