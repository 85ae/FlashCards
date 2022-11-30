"""
This module defines the FlashCard class.
"""

from .io import printFlashCard, Printing
from datetime import date

class FlashCard:
    """This class represents a flashcard"""

    def __init__(self, question: str = "Question", answer: str = "Answer", last_date: date = date.today()):
        """The main constructor."""
        self.question = question
        self.answer = answer
        if last_date < date.today():
            self._last_date = last_date
        else:
            self._last_date = date.today()

    def from_card(self, card: tuple[str, str] | dict):
        """
        Construct from a tuple or a dictionary.
        If using a tuple, it must be under the form ("question", "answer").
        If you prefer use a dictionary, define two keys: 'question' and 'answer'.
        @raise An exception if card is not a tuple or a dictionary.
        """
        if isinstance(card, tuple):
            (self.question, self.answer) = card # tuple unpackaging
        elif isinstance(card, dict):
            if 'question' in card:
                self. question = card['question']
            if 'answer' in card:
                self.answer = card['answer']
        else:
            raise Exception("Argument 'card' is not a tuple or a dictionary.")

    @property
    def question(self) -> str: # test
        """Get the 'question' property"""
        return self._question

    @question.setter
    def question(self, question: str):
        """Set the 'question' property"""
        self._question = question

    @property
    def answer(self) -> str:
        """Get the 'answer' property"""
        return self._answer

    @answer.setter
    def answer(self, answer: str):
        """Set the 'answer' property"""
        self._answer = answer

    @property
    def last_date(self) -> date: # test
        """Get the 'date' property"""
        return self._last_date

    @last_date.setter
    def last_date(self, last_date: date):
        """Set the 'date' property"""
        if last_date < date.today():
            _last_date = last_date

    def isRightAnswer(self, answer: str) -> bool:
        return answer.casefold() == self.answer.casefold()

    def ask(self) -> bool:
        """Ask to the user what is the corresponding answer to a question"""
        result = printFlashCard(self.to_tuple(), Printing.ASK_ANSWER)
        if isinstance(result, bool):
            return result
        else:
            return False

    def show(self):
        """
        Show the flashcard to the user.
        """
        printFlashCard(self.to_tuple())

    def __str__(self) -> str:
        """
        Return a printable string.
        """
        return self.question + ":\n" + self.answer

    def to_tuple(self) -> tuple[str, str]:
        """
        Returns a tuple under the form ("question", "answer").
        """
        return (self.question, self.answer)

    def to_dict(self) -> dict:
        """
        Returns a dictionary with 2 keys:
         - 'question'
         - 'answer'
        """
        return {
            'question': self.question,
            'answer': self.answer
        }
