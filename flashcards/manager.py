"""
This module contains a flashcard folder manager.
"""

from .io import from_file, to_file
from .flashcard import FlashCard
import os
from os.path import join, abspath
from datetime import date, datetime, timedelta, MAXYEAR, MINYEAR

def is_between(x: int, inf: int = 0, sup: int = 2) -> bool:
    """
    Test if an integer ('x') is between 'int' and 'sup'.
    """
    return x < sup and x > inf

class FlashCardFolder:
    """
    This class represents a flashcard folder.
    The folder must be under this form:
      <dir>/          # The directory
        1/            # All the categories.
          01-12-2021  # The flashcard files with the format 'mm-dd-yyyy'.
          09-27-2017
        2/
        3/
        ...           # 4, 5...
        8/
    The best way to create a folder like this is to use the method defined here.
    """

    def __init__(self, path: str):
        """
        The main constructor.
        It creates a simple FlashCardFolder.
        To load or create a flashcard directory, use the functions defined below.
        """
        self.path = abspath(path)
        self.categories = [
            {
                "number": 1,
                "delay": {
                    "days": 1,
                    "months": 0
                },
                "flashcards": []
            },
            {
                "number": 2,
                "delay": {
                    "days": 2,
                    "months": 0
                },
                "flashcards": []
            },
            {
                "number": 3,
                "delay": {
                    "days": 7,
                    "months": 0
                },
                "flashcards": []
            },
            {
                "number": 4,
                "delay": {
                    "days": 14,
                    "months": 0
                },
                "flashcards": []
            },
            {
                "number": 5,
                "delay": {
                    "days": 0,
                    "months": 1
                },
                "flashcards": []
            },
            {
                "number": 6,
                "delay": {
                    "days": 0,
                    "months": 2
                },
                "flashcards": []
            },
            {
                "number": 7,
                "delay": {
                    "days": 0,
                    "months": 6
                },
                "flashcards": []
            },
            {
                "number": 8,
                "delay": {
                    "days": 0,
                    "months": 12
                },
                "flashcards": []
            }
        ]

    def load(self):
        """
        Load a folder.
        It raises an exception if the folder is not loadable.
        """
        if self.check():
            for category in self.categories:
                for flashcard_file in os.listdir(join(self.path, category['number'])):
                    flashcard = FlashCard()
                    flashcard.from_card(from_file(join(self.path, flashcard_file)))
                    flashcard.last_date = date(int(flashcard_file[6:9]), int(flashcard_file[3:4]), int(flashcard_file[0:1]))

                    category['flashcards'].append(flashcard)
        else:
            raise Exception("The folder can't be loaded.")

    def check(self) -> bool:
        """
        Check if the folder is correct.
        Return True if it's correct, False else.
        """
        categories = [str(i['number']) for i in self.categories]
        for dir in os.listdir(self.path):
            if dir in categories and os.path.isdir(join(self.path, dir)):
                categories.remove(dir)
                for file in os.listdir(join(self.path, dir)):
                    if os.path.isfile(file):
                        if len(file) >= 10 and file[0:1].isdigit() and file[2] == '-' and file[3:4].isdigit() and file[5] == '-' and file[6:9].isdigit():
                            if is_between(int(file[0:1]), 0, 13) and is_between(int(file[3:4]), 0, 31) and is_between(int(file[6:9]), MINYEAR - 1, MAXYEAR + 1):
                                pass
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                    
        if len(categories) == 0:
            return True
        else:
            return False

