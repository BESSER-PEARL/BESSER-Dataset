from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Suit(Enum):
    pass
class Rank(Enum):
    pass

############################################
# Definition of Classes
############################################










class Card:

    def __init__(self, suit: str, rank: str):
        self.suit = suit
        self.rank = rank
        
        pass
    @property
    def rank(self):
        return self.__rank
    @rank.setter
    def rank(self, rank: str):
        self.__rank = rank

    @property
    def suit(self):
        return self.__suit
    @suit.setter
    def suit(self, suit: str):
        self.__suit = suit



class Deck:

    def __init__(self, cards: str):
        self.cards = cards
        
        pass
    @property
    def cards(self):
        return self.__cards
    @cards.setter
    def cards(self, cards: str):
        self.__cards = cards



class Blackjack:

    pass
