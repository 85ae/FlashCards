"""
This module contains a flashcard folder manager.
"""

from .io import from_file, to_file
from .flashcard import FlashCard

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
        self.path = path