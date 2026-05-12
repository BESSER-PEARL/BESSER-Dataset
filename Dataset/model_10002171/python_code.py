from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Value(Enum):
    pass
class CardSuit(Enum):
    pass
class Suit(Enum):
    pass

############################################
# Definition of Classes
############################################










class Card:

    def __init__(self, _CardSuit: int, toString: str, Value: int):
        self._CardSuit = _CardSuit
        self.toString = toString
        self.Value = Value
        
        pass
    @property
    def _CardSuit(self):
        return self.___CardSuit
    @_CardSuit.setter
    def _CardSuit(self, _CardSuit: int):
        self.___CardSuit = _CardSuit

    @property
    def toString(self):
        return self.__toString
    @toString.setter
    def toString(self, toString: str):
        self.__toString = toString

    @property
    def Value(self):
        return self.__Value
    @Value.setter
    def Value(self, Value: int):
        self.__Value = Value



class Deck:

    def __init__(self, ArrayList: str):
        self.ArrayList = ArrayList
        
        pass
    @property
    def ArrayList(self):
        return self.__ArrayList
    @ArrayList.setter
    def ArrayList(self, ArrayList: str):
        self.__ArrayList = ArrayList



class BlackjackGameSimulator:

    pass
