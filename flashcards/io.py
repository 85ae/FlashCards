"""
The io module.
It includes some functions to print a flashcard or load from a file.
"""

from enum import Enum, auto

class Printing(Enum):
    """
    Defines how the flashcard must be printed.
    Pass it as an argument to flashcard.printFlashCard(x, display).
      SHOW_ANSWER: show the question AND the answer.
      ASK_ANSWER: show the question then ask for the question and, if false, print the right answer.
    """
    SHOW_ANSWER = auto()
    ASK_ANSWER = auto()

def printFlashCard(flashcard: tuple[str, str], display: Printing = Printing.SHOW_ANSWER):
    """
    Print a flashcard.
    @param flashcard the flashcard to print. Must be a tuple under the form ("question", "answer"). You can obtain this tuple with the method Flashcard.to_tuple().
    @param display the printing method. See flashcard.Printing for more informations.
    If the argument 'display' isn't given or is Printing.SHOW_ANSWER, it doesn't return anything.
    If the argument 'display' is Printing.ASK_ANSWER, it returns True if the answer is correct, False else.
    @raise an exception if the argument 'display' isn't correct.
    """
    match display:
        case Printing.SHOW_ANSWER:
            print("Question: " + flashcard[0])
            print("Answer: " + flashcard[1])

        case Printing.ASK_ANSWER:
            print("Question: " + flashcard[0])
            print("Your answer: ", end='')
            answer = input()
            if flashcard[1].casefold() == answer.casefold():
                print("Right answer !")
                return True
            else:
                print("Bad answer.\nThe correct answer was:\n" + flashcard[1])
                return False

        case _:
            raise Exception("Argument 'display' is not a correct Printing object.")

def to_html(flashcard: tuple[str, str], display: Printing = Printing.SHOW_ANSWER) -> str:
    """
    Print a flashcard to HTML.
    @param flashcard the flashcard to print. Must be a tuple under the form ("question", "answer"). You can obtain this tuple with the method Flashcard.to_tuple().
    @param display the printing method. See flashcard.Printing for more informations.
    If the argument 'display' isn't given or is Printing.SHOW_ANSWER, it doesn't return anything.
    If the argument 'display' is Printing.ASK_ANSWER, it returns True if the answer is correct, False else.
    If the argument 'display' isn't correct, it raises an exception.
    """
    html = "<html><head><meta charset=\"UTF-8\" /><title>FlashCard</title></head><body><h1>FlashCard</h1><p><div>Question: " + flashcard[0] + "</div><div id=\"answer\">Answer: " + flashcard[1] + "</div>"
    match display:
        case Printing.SHOW_ANSWER:
            "Does nothing (now)"

        case Printing.ASK_ANSWER:
            html += "<script>document.getElementById('answer').hidden = true; let answer = prompt(\"Question: " + flashcard[0].replace('\"', "\\\"") + "\", \"Answer\"); if(answer != null) { if(answer.toLowerCase() == \"" + flashcard[1].replace('\"', "\\\"").lower() + "\") { alert(\"Right answer !\"); } else { alert(\"Bad answer.\") } document.getElementById('answer').hidden = false; }</script>"

        case _:
            raise Exception("Argument 'display' is not a correct Printing object.")
        
    html += "</p></body></html>"
    return html

def from_file(path: str) -> tuple[str, str]:
    """
    It loads a flashcard from a file and returns a tuple to represent it.
    You can load it then by using the FlashCard.from_card(card) function.
    Example: my_flashcard.from_card(from_file("/path/to/my.file"))
    """
    line_1 = ""
    line_2 = ""

    with open(path, "r") as file:
        line_1 = file.readline()
        line_2 = file.readline()

    return (line_1, line_2)

def to_file(card: tuple[str, str], path: str):
    """
    It loads a flashcard into a file.
    The 'card' parameter must be a tuple under the form ("question", "answer").
    You can obtain this tuple with the method Flashcard.to_tuple().
    """
    with open(path, "w") as file:
        if file:
            file.write(card[0] + '\n')
            file.write(card[1])
        else:
            raise Exception("The file " + path + " can't be opened.")