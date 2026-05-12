from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class T3:

    pass


class Queue:

    pass


class CasinoManager:

    def __init__(self, table: Table, waitList: str):
        self.table = table
        self.waitList = waitList
        
        pass
    @property
    def table(self):
        return self.__table
    @table.setter
    def table(self, table: Table):
        self.__table = table

    @property
    def waitList(self):
        return self.__waitList
    @waitList.setter
    def waitList(self, waitList: str):
        self.__waitList = waitList



class T2:

    pass


class T1:

    pass


class Tuple:

    pass


class Player:

    pass


class T:

    pass


class Stack:

    pass


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



class Table:

    def __init__(self, deck: Deck, currPlayers: str):
        self.deck = deck
        self.currPlayers = currPlayers
        
        pass
    @property
    def currPlayers(self):
        return self.__currPlayers
    @currPlayers.setter
    def currPlayers(self, currPlayers: str):
        self.__currPlayers = currPlayers

    @property
    def deck(self):
        return self.__deck
    @deck.setter
    def deck(self, deck: Deck):
        self.__deck = deck



class Executive:

    pass


class Card:

    def __init__(self, value: int, suit: str):
        self.value = value
        self.suit = suit
        
        pass
    @property
    def suit(self):
        return self.__suit
    @suit.setter
    def suit(self, suit: str):
        self.__suit = suit

    @property
    def value(self):
        return self.__value
    @value.setter
    def value(self, value: int):
        self.__value = value

