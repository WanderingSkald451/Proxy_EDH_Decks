import sys
from PIL import Image

from src.classes.deck import Deck


def create_print_sheets(deck_name: str):
    d = Deck(deck_name)
