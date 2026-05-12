from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class CardCollection:

    def __init__(self, collection: str, card0: "Card" = None):
        self.collection = collection
        self.card0 = card0
        
        pass
    @property
    def collection(self):
        return self.__collection
    @collection.setter
    def collection(self, collection: str):
        self.__collection = collection

    @property
    def card0(self):
        return self.__card0
    @card0.setter
    def card0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CardCollection__card0", None)
        self.__card0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cardCollection1"):
                opp_val = getattr(old_value, "cardCollection1", None)
                if opp_val == self:
                    setattr(old_value, "cardCollection1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cardCollection1"):
                opp_val = getattr(value, "cardCollection1", None)
                setattr(value, "cardCollection1", self)



class EndCardPile:

    pass


class Hand:

    pass


class Card:

    def __init__(self, Number: int, Suit: str, cardCollection1: "CardCollection" = None):
        self.Number = Number
        self.Suit = Suit
        self.cardCollection1 = cardCollection1
        
        pass
    @property
    def Suit(self):
        return self.__Suit
    @Suit.setter
    def Suit(self, Suit: str):
        self.__Suit = Suit

    @property
    def Number(self):
        return self.__Number
    @Number.setter
    def Number(self, Number: int):
        self.__Number = Number

    @property
    def cardCollection1(self):
        return self.__cardCollection1
    @cardCollection1.setter
    def cardCollection1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Card__cardCollection1", None)
        self.__cardCollection1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "card0"):
                opp_val = getattr(old_value, "card0", None)
                if opp_val == self:
                    setattr(old_value, "card0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "card0"):
                opp_val = getattr(value, "card0", None)
                setattr(value, "card0", self)



class Deck:

    pass
