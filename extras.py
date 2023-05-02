import time
import sys

def typewriter(write):
    """
    Creates a typewriter effect for output.
    Code for the typewriter effect was found here:
    https://replit.com/talk/learn/Typewriter-effect-Python/139897
    """
    for i in write:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(.05)