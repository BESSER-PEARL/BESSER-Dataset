from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Suit(Enum):
    pass

############################################
# Definition of Classes
############################################










class Deck:

    pass


class CardTester:

    pass


class Card:

    def __init__(self, suit: str, pointValue: int, rank: str):
        self.suit = suit
        self.pointValue = pointValue
        self.rank = rank
        
        pass
    @property
    def suit(self):
        return self.__suit
    @suit.setter
    def suit(self, suit: str):
        self.__suit = suit

    @property
    def pointValue(self):
        return self.__pointValue
    @pointValue.setter
    def pointValue(self, pointValue: int):
        self.__pointValue = pointValue

    @property
    def rank(self):
        return self.__rank
    @rank.setter
    def rank(self, rank: str):
        self.__rank = rank

