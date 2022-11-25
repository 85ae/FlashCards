"""
The io module.
It includes some functions to print a flashcard.
It also includes a flashcard folder manager.
"""

from .flashcard import FlashCard

def print(x: FlashCard):
    print(x.to_str())