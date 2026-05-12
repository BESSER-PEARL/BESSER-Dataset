from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Suit(Enum):
    pass
class CardValue(Enum):
    pass

############################################
# Definition of Classes
############################################







class Show_Top_Results_UseCase:

    pass


class Play_Multiple_Times_UseCase:

    pass


class Play_Once_UseCase:

    pass


class Play_for_Me_UseCase:

    pass


class Amalgamate_UseCase:

    pass


class Current_over_two_UseCase:

    pass


class Current_onto_Previous_UseCase:

    pass


class Make_Move_UseCase:

    pass


class Deal_a_Card_UseCase:

    pass


class Show_Deck_UseCase:

    pass


class Shuffle_Deck_UseCase:

    pass


class User_Actor:

    pass





class Application:

    def __init__(self, scan: str, deck: Deck):
        self.scan = scan
        self.deck = deck
        
        pass
    @property
    def deck(self):
        return self.__deck
    @deck.setter
    def deck(self, deck: Deck):
        self.__deck = deck

    @property
    def scan(self):
        return self.__scan
    @scan.setter
    def scan(self, scan: str):
        self.__scan = scan



class Card:

    def __init__(self, suit: Suit, cardValue: CardValue):
        self.suit = suit
        self.cardValue = cardValue
        
        pass
    @property
    def cardValue(self):
        return self.__cardValue
    @cardValue.setter
    def cardValue(self, cardValue: CardValue):
        self.__cardValue = cardValue

    @property
    def suit(self):
        return self.__suit
    @suit.setter
    def suit(self, suit: Suit):
        self.__suit = suit



class Deck:

    def __init__(self, _cards__: Card, scan: str):
        self._cards__ = _cards__
        self.scan = scan
        
        pass
    @property
    def scan(self):
        return self.__scan
    @scan.setter
    def scan(self, scan: str):
        self.__scan = scan

    @property
    def _cards__(self):
        return self.___cards__
    @_cards__.setter
    def _cards__(self, _cards__: Card):
        self.___cards__ = _cards__

