
from enum import Enum
import random
from dataclasses import dataclass

#this class etablishes the cards and also starts the main game
class CardsDeck:
    def make_deck():
        spades = {"A♠" : 11, "2♠" : 2, "3♠" : 3, "4♠" : 4, "5♠": 5,"6♠" : 6, "7♠" : 7, "8♠" : 8, "9♠" : 9, "10♠" : 10,"J♠" : 10,"Q♠" : 10, "K♠" : 10}

        hearts = {"A♥" : 11, "2♥" : 2, "3♥" : 3, "4♥" : 4, "5♥": 5,"6♥" : 6, "7♥" : 7, "8♥" : 8, "9♥" : 9, "10♥" : 10,"J♥" : 10,"Q♥" : 10, "K♥" : 10}

        jacks = {"A♣" : 11, "2♣" : 2, "3♣" : 3, "4♣" : 4, "5♣": 5,"6♣" : 6, "7♣" : 7, "8♣" : 8, "9♣" : 9, "10♣" : 10,"J♣" : 10,"Q♣" : 10, "K♣" : 10}

        diamond = {"A♦" : 11, "2♦" : 2, "3♦" : 3, "4♦" : 4, "5♦": 5,"6♦" : 6, "7♦" : 7, "8♦" : 8, "9♦" : 9, "10♦" : 10,"J♦" : 10,"Q♦" : 10, "K♦" : 10}

        deck_test = {**spades, **hearts, **jacks, **diamond}
        return deck_test

#this will serve as a refernece thingy


