from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Suit1(Enum):
    pass
class CardNumber(Enum):
    pass
class Suit(Enum):
    pass

############################################
# Definition of Classes
############################################










class Program:

    pass


class GameManager:

    pass


class Dealer:

    def __init__(self, cardDeck: Deck):
        self.cardDeck = cardDeck
        
        pass
    @property
    def cardDeck(self):
        return self.__cardDeck
    @cardDeck.setter
    def cardDeck(self, cardDeck: Deck):
        self.__cardDeck = cardDeck



class Player:

    def __init__(self, CardsInHand: Card, isSoft: bool):
        self.CardsInHand = CardsInHand
        self.isSoft = isSoft
        
        pass
    @property
    def CardsInHand(self):
        return self.__CardsInHand
    @CardsInHand.setter
    def CardsInHand(self, CardsInHand: Card):
        self.__CardsInHand = CardsInHand

    @property
    def isSoft(self):
        return self.__isSoft
    @isSoft.setter
    def isSoft(self, isSoft: bool):
        self.__isSoft = isSoft



class Deck:

    def __init__(self, List_card_: Card):
        self.List_card_ = List_card_
        
        pass
    @property
    def List_card_(self):
        return self.__List_card_
    @List_card_.setter
    def List_card_(self, List_card_: Card):
        self.__List_card_ = List_card_



class Card:

    def __init__(self, _CardNumber: int, _CardValue: int, _Suit: int):
        self._CardNumber = _CardNumber
        self._CardValue = _CardValue
        self._Suit = _Suit
        
        pass
    @property
    def _Suit(self):
        return self.___Suit
    @_Suit.setter
    def _Suit(self, _Suit: int):
        self.___Suit = _Suit

    @property
    def _CardValue(self):
        return self.___CardValue
    @_CardValue.setter
    def _CardValue(self, _CardValue: int):
        self.___CardValue = _CardValue

    @property
    def _CardNumber(self):
        return self.___CardNumber
    @_CardNumber.setter
    def _CardNumber(self, _CardNumber: int):
        self.___CardNumber = _CardNumber

