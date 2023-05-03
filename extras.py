import time
import sys

<<<<<<< HEAD
def typewriter(write):
    """
    Creates a typewriter effect for output.
    Code for the typewriter effect was found here:
    https://replit.com/talk/learn/Typewriter-effect-Python/139897
    """
    for i in write:
        sys.stdout.write(i)
        sys.stdout.flush()
=======
def typewriter(string):
    """
    Creates a typewriter effect for output.
    Code for the typewriter effect was found here:
    https://stackoverflow.com/questions/42940747/python-simple-typewriter-effect
    """
    for char in string:
        print(char, end='', flush=True)
>>>>>>> ebf92c8 (Define typewriter function in extras.py)
        time.sleep(.05)