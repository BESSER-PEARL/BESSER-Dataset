from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class poker_GameRun:

    pass


class poker_Game:

    def __init__(self, hand_size: int, tryagain: int):
        self.hand_size = hand_size
        self.tryagain = tryagain
        
        pass
    @property
    def tryagain(self):
        return self.__tryagain
    @tryagain.setter
    def tryagain(self, tryagain: int):
        self.__tryagain = tryagain

    @property
    def hand_size(self):
        return self.__hand_size
    @hand_size.setter
    def hand_size(self, hand_size: int):
        self.__hand_size = hand_size



class Card:

    pass


class Comparable_Interface:

    pass


class player_Deck:

    def __init__(self, deck_size: int, hand_size: int, numberofShuffles: int, remainofDeck: int):
        self.deck_size = deck_size
        self.hand_size = hand_size
        self.numberofShuffles = numberofShuffles
        self.remainofDeck = remainofDeck
        
        pass
    @property
    def remainofDeck(self):
        return self.__remainofDeck
    @remainofDeck.setter
    def remainofDeck(self, remainofDeck: int):
        self.__remainofDeck = remainofDeck

    @property
    def deck_size(self):
        return self.__deck_size
    @deck_size.setter
    def deck_size(self, deck_size: int):
        self.__deck_size = deck_size

    @property
    def hand_size(self):
        return self.__hand_size
    @hand_size.setter
    def hand_size(self, hand_size: int):
        self.__hand_size = hand_size

    @property
    def numberofShuffles(self):
        return self.__numberofShuffles
    @numberofShuffles.setter
    def numberofShuffles(self, numberofShuffles: int):
        self.__numberofShuffles = numberofShuffles



class player_Player:

    pass


class card_Card:

    def __init__(self, suit: int, rank: int):
        self.suit = suit
        self.rank = rank
        
        pass
    @property
    def suit(self):
        return self.__suit
    @suit.setter
    def suit(self, suit: int):
        self.__suit = suit

    @property
    def rank(self):
        return self.__rank
    @rank.setter
    def rank(self, rank: int):
        self.__rank = rank

