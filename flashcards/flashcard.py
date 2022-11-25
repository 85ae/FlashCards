"""
This module defines the FlashCard class.
This is probably the only module you'll import.
"""

class FlashCard:
    """This class represents a flashcard"""

    def __init__(self, question: str = "Question", answer: str = "Answer"):
        """The main constructor."""
        self.question = question
        self.answer = answer

    def __init__(self, other: FlashCard):
        self(other.question, other.answer)

    def __init__(self, card: tuple):
        """
        Another constructor.
        @param card must be a tuple under the form ("question", "answer")
        """
        (self.question, self.answer) = card

    def __init__(self, card: dict):
        """
        Another constructor.
        @param card must be a dictionary with 2 keys: "question" and "answer".
        """
        self(card['question'], card['answer'])

    @property
    def question(self) -> str: # test
        """Get the 'question' property"""
        return self._question

    @question.setter
    def question(self, question: str = "Question"):
        """Set the 'question' property"""
        self._question = question

    @property
    def answer(self) -> str:
        """Get the 'answer' property"""
        return self._answer

    @answer.setter
    def answer(self, answer: str = "Answer"):
        """Set the 'answer' property"""
        self._answer = answer

    def ask(self) -> bool:
        """Ask to the user what is the corresponding answer to a question"""
        print(self.question)
        if input("Your answer :").casefold() == self.answer.casefold():
            print("All right !")
            return True

    def to_str(self) -> str:
        return "Question: " + self.question + "\nAnswer: " + self.answer

    def to_tuple(self) -> tuple:
        """
        Returns a tuple under the form ("question", "answer").
        """
        return (self.question, self.answer)

    def to_dict(self) -> dict:
        """
        Returns a dictionary with 2 keys:
         - "question"
         - "answer"
        """
        return {
            "question": self.question,
            "answer": self.answer
        }
