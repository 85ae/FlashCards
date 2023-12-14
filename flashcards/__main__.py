"""
 +============+
 | FlashCards |
 +============+

The main file.
"""

from flashcards.flashcard import FlashCard
from flashcards.io import to_html, Printing

fc = FlashCard("???", "Oui")
print(to_html(fc.to_tuple(), Printing.ASK_ANSWER))
