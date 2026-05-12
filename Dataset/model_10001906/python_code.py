from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Card:

    def __init__(self, value: int, suit: int, color: bool, deck1: "Deck" = None):
        self.value = value
        self.suit = suit
        self.color = color
        self.deck1 = deck1
        
        pass
    @property
    def value(self):
        return self.__value
    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self, color: bool):
        self.__color = color

    @property
    def suit(self):
        return self.__suit
    @suit.setter
    def suit(self, suit: int):
        self.__suit = suit

    @property
    def deck1(self):
        return self.__deck1
    @deck1.setter
    def deck1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Card__deck1", None)
        self.__deck1 = value
        
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

    def __init__(self, deck: str, card0: "Card" = None):
        self.deck = deck
        self.card0 = card0
        
        pass
    @property
    def deck(self):
        return self.__deck
    @deck.setter
    def deck(self, deck: str):
        self.__deck = deck

    @property
    def card0(self):
        return self.__card0
    @card0.setter
    def card0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Deck__card0", None)
        self.__card0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "deck1"):
                opp_val = getattr(old_value, "deck1", None)
                if opp_val == self:
                    setattr(old_value, "deck1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "deck1"):
                opp_val = getattr(value, "deck1", None)
                setattr(value, "deck1", self)

