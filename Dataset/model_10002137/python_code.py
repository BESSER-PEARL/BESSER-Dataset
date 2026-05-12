from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Poker_PokerRank(Enum):
    pass

############################################
# Definition of Classes
############################################










class Poker_PokerGame:

    def __init__(self, numPlayers: int, Round: int):
        self.numPlayers = numPlayers
        self.Round = Round
        
        pass
    @property
    def Round(self):
        return self.__Round
    @Round.setter
    def Round(self, Round: int):
        self.__Round = Round

    @property
    def numPlayers(self):
        return self.__numPlayers
    @numPlayers.setter
    def numPlayers(self, numPlayers: int):
        self.__numPlayers = numPlayers



class Cards_Deck:

    def __init__(self, cardsInDeck: str):
        self.cardsInDeck = cardsInDeck
        
        pass
    @property
    def cardsInDeck(self):
        return self.__cardsInDeck
    @cardsInDeck.setter
    def cardsInDeck(self, cardsInDeck: str):
        self.__cardsInDeck = cardsInDeck



class Cards_Card:

    def __init__(self, rank: int):
        self.rank = rank
        
        pass
    @property
    def rank(self):
        return self.__rank
    @rank.setter
    def rank(self, rank: int):
        self.__rank = rank



class Poker_Hand:

    def __init__(self, numCards: int, cardsInHand: str, Fold: bool, handIterator: Poker_HandIterator, Hand_HandIterator_00: "Poker_HandIterator" = None):
        self.numCards = numCards
        self.cardsInHand = cardsInHand
        self.Fold = Fold
        self.handIterator = handIterator
        self.Hand_HandIterator_00 = Hand_HandIterator_00
        
        pass
    @property
    def numCards(self):
        return self.__numCards
    @numCards.setter
    def numCards(self, numCards: int):
        self.__numCards = numCards

    @property
    def cardsInHand(self):
        return self.__cardsInHand
    @cardsInHand.setter
    def cardsInHand(self, cardsInHand: str):
        self.__cardsInHand = cardsInHand

    @property
    def Fold(self):
        return self.__Fold
    @Fold.setter
    def Fold(self, Fold: bool):
        self.__Fold = Fold

    @property
    def handIterator(self):
        return self.__handIterator
    @handIterator.setter
    def handIterator(self, handIterator: Poker_HandIterator):
        self.__handIterator = handIterator

    @property
    def Hand_HandIterator_00(self):
        return self.__Hand_HandIterator_00
    @Hand_HandIterator_00.setter
    def Hand_HandIterator_00(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Poker_Hand__Hand_HandIterator_00", None)
        self.__Hand_HandIterator_00 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "handIterator1"):
                opp_val = getattr(old_value, "handIterator1", None)
                if opp_val == self:
                    setattr(old_value, "handIterator1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "handIterator1"):
                opp_val = getattr(value, "handIterator1", None)
                setattr(value, "handIterator1", self)



class Poker_HandIterator:

    pass


class Poker_Iterator_Interface:

    pass


class Poker_Computer:

    pass


class Poker_Human:

    pass


class Poker_Player:

    def __init__(self, currentMoney: int, currentBet: int, hand: Poker_Hand):
        self.currentMoney = currentMoney
        self.currentBet = currentBet
        self.hand = hand
        
        pass
    @property
    def hand(self):
        return self.__hand
    @hand.setter
    def hand(self, hand: Poker_Hand):
        self.__hand = hand

    @property
    def currentBet(self):
        return self.__currentBet
    @currentBet.setter
    def currentBet(self, currentBet: int):
        self.__currentBet = currentBet

    @property
    def currentMoney(self):
        return self.__currentMoney
    @currentMoney.setter
    def currentMoney(self, currentMoney: int):
        self.__currentMoney = currentMoney

