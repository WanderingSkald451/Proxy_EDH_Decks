import os
from src.classes.deck import Deck
from src.common.constants import FOLDER_ADDRESS


def fetch(deck_name: str):
    d = Deck(deck_name)
    d.download_images()


def create_sheets(deck_name: str):
    """
    Organise images in sheets, ready to be sent to the printer.
    1. Check if deck images are available
        1.a: if not, fetch them
    2. Once all the images are available, organise them into sheets.
    :param deck_name: unique identifier of the deck
    :return:
    """
    print("Working on it ...")


def proxy():


    deck_name = input("Please, enter a deck name_: ")
    while not os.path.exists(os.path.join(FOLDER_ADDRESS, deck_name)):
        deck_name = input("Deck not found\n.Please, enter a deck name_: ")

    for action in actions:
        print(f"\033[94m> {action}")
    print("---------------------------------")
    go_on: bool = True
    while go_on:

        print("\033[94m[PROXY]> \033[92mAwaiting inquiry_")
        action = input()
        if action.upper() == "BACK":
            break
        else:
            try:
                actions[action.upper()](deck_name)
            except KeyError as e:
                print("Command not found.")


actions: dict = {"FETCH": fetch,
                 "CREATE_SHEETS": create_sheets
                 }
