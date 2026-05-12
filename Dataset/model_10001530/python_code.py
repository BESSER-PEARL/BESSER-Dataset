from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Game:

    def __init__(self, mainDeck: Deck, completedCards: Deck, cardsOnTable: Card):
        self.mainDeck = mainDeck
        self.completedCards = completedCards
        self.cardsOnTable = cardsOnTable
        
        pass
    @property
    def cardsOnTable(self):
        return self.__cardsOnTable
    @cardsOnTable.setter
    def cardsOnTable(self, cardsOnTable: Card):
        self.__cardsOnTable = cardsOnTable

    @property
    def mainDeck(self):
        return self.__mainDeck
    @mainDeck.setter
    def mainDeck(self, mainDeck: Deck):
        self.__mainDeck = mainDeck

    @property
    def completedCards(self):
        return self.__completedCards
    @completedCards.setter
    def completedCards(self, completedCards: Deck):
        self.__completedCards = completedCards



class Deck:

    def __init__(self, cards: Card):
        self.cards = cards
        
        pass
    @property
    def cards(self):
        return self.__cards
    @cards.setter
    def cards(self, cards: Card):
        self.__cards = cards



class Card:

    def __init__(self, value: int):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value
    @value.setter
    def value(self, value: int):
        self.__value = value

