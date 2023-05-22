import time
import sys
import os


def typewriter(string):
    """
    Creates a typewriter effect for output.
    Code for the typewriter effect was found here:
    https://stackoverflow.com/questions/42940747/python-simple-typewriter-effect
    """
    for char in string:
        print(char, end='', flush=True)
        time.sleep(.05)


def clear():
    """
    Clears the mock terminal screen
    The code for this function was found here:
    https://www.geeksforgeeks.org/clear-screen-python/
    """
    if os.name == "nt":
        _ = os.system('cls')
    else:
        _ = os.system('clear')
