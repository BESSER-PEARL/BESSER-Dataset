from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Deck:

    pass


class Card:

    def __init__(self, suit: int, value: int, JOKER: int, CLUBS: int, DIAMONDS: int, HEARTS: int, SPADES: int, ACE: int, JACK: int, QUEEN: int, KING: int):
        self.suit = suit
        self.value = value
        self.JOKER = JOKER
        self.CLUBS = CLUBS
        self.DIAMONDS = DIAMONDS
        self.HEARTS = HEARTS
        self.SPADES = SPADES
        self.ACE = ACE
        self.JACK = JACK
        self.QUEEN = QUEEN
        self.KING = KING
        
        pass
    @property
    def value(self):
        return self.__value
    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def ACE(self):
        return self.__ACE
    @ACE.setter
    def ACE(self, ACE: int):
        self.__ACE = ACE

    @property
    def JACK(self):
        return self.__JACK
    @JACK.setter
    def JACK(self, JACK: int):
        self.__JACK = JACK

    @property
    def KING(self):
        return self.__KING
    @KING.setter
    def KING(self, KING: int):
        self.__KING = KING

    @property
    def JOKER(self):
        return self.__JOKER
    @JOKER.setter
    def JOKER(self, JOKER: int):
        self.__JOKER = JOKER

    @property
    def QUEEN(self):
        return self.__QUEEN
    @QUEEN.setter
    def QUEEN(self, QUEEN: int):
        self.__QUEEN = QUEEN

    @property
    def CLUBS(self):
        return self.__CLUBS
    @CLUBS.setter
    def CLUBS(self, CLUBS: int):
        self.__CLUBS = CLUBS

    @property
    def HEARTS(self):
        return self.__HEARTS
    @HEARTS.setter
    def HEARTS(self, HEARTS: int):
        self.__HEARTS = HEARTS

    @property
    def SPADES(self):
        return self.__SPADES
    @SPADES.setter
    def SPADES(self, SPADES: int):
        self.__SPADES = SPADES

    @property
    def suit(self):
        return self.__suit
    @suit.setter
    def suit(self, suit: int):
        self.__suit = suit

    @property
    def DIAMONDS(self):
        return self.__DIAMONDS
    @DIAMONDS.setter
    def DIAMONDS(self, DIAMONDS: int):
        self.__DIAMONDS = DIAMONDS

