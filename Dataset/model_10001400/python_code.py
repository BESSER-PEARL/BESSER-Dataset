from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Class2:

    pass


class Class:

    pass


class blackjackCard:

    pass


class Deck:

    def __init__(self, deck: str):
        self.deck = deck
        
        pass
    @property
    def deck(self):
        return self.__deck
    @deck.setter
    def deck(self, deck: str):
        self.__deck = deck



class Blackjack:

    pass


class blackjackHand:

    pass


class Hand:

    pass


class Card:

    def __init__(self, suit: int, face: int):
        self.suit = suit
        self.face = face
        
        pass
    @property
    def face(self):
        return self.__face
    @face.setter
    def face(self, face: int):
        self.__face = face

    @property
    def suit(self):
        return self.__suit
    @suit.setter
    def suit(self, suit: int):
        self.__suit = suit

