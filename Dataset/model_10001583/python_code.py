from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Class:

    pass


class GoFish:

    pass


class Rules:

    def __init__(self, attribute: str, currentRules: bool):
        self.attribute = attribute
        self.currentRules = currentRules
        
        pass
    @property
    def currentRules(self):
        return self.__currentRules
    @currentRules.setter
    def currentRules(self, currentRules: bool):
        self.__currentRules = currentRules

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute



class Game:

    pass


class Computer:

    pass


class b:

    pass


class Player:

    def __init__(self, hand: str, name: str):
        self.hand = hand
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def hand(self):
        return self.__hand
    @hand.setter
    def hand(self, hand: str):
        self.__hand = hand



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



class Card:

    def __init__(self, color: str, suit: str, number: int):
        self.color = color
        self.suit = suit
        self.number = number
        
        pass
    @property
    def number(self):
        return self.__number
    @number.setter
    def number(self, number: int):
        self.__number = number

    @property
    def suit(self):
        return self.__suit
    @suit.setter
    def suit(self, suit: str):
        self.__suit = suit

    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self, color: str):
        self.__color = color

