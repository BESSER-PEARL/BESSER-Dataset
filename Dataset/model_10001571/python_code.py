from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Cards_Suit(Enum):
    pass
class Cards_Rank(Enum):
    pass

############################################
# Definition of Classes
############################################










class Cards_Deck_Interface:

    pass


class Cards_StarndardDeck:

    def __init__(self, rand: str, cards: Cards_Card, card0: "Cards_Card" = None):
        self.rand = rand
        self.cards = cards
        self.card0 = card0
        
        pass
    @property
    def cards(self):
        return self.__cards
    @cards.setter
    def cards(self, cards: Cards_Card):
        self.__cards = cards

    @property
    def rand(self):
        return self.__rand
    @rand.setter
    def rand(self, rand: str):
        self.__rand = rand

    @property
    def card0(self):
        return self.__card0
    @card0.setter
    def card0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cards_StarndardDeck__card0", None)
        self.__card0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "starndardDeck1"):
                opp_val = getattr(old_value, "starndardDeck1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "starndardDeck1"):
                opp_val = getattr(value, "starndardDeck1", None)
                if opp_val is None:
                    setattr(value, "starndardDeck1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Cards_Card:

    def __init__(self, rank: Cards_Rank, suit: Cards_Suit, starndardDeck1: set["Cards_StarndardDeck"] = None):
        self.rank = rank
        self.suit = suit
        self.starndardDeck1 = starndardDeck1 if starndardDeck1 is not None else set()
        
        pass
    @property
    def rank(self):
        return self.__rank
    @rank.setter
    def rank(self, rank: Cards_Rank):
        self.__rank = rank

    @property
    def suit(self):
        return self.__suit
    @suit.setter
    def suit(self, suit: Cards_Suit):
        self.__suit = suit

    @property
    def starndardDeck1(self):
        return self.__starndardDeck1
    @starndardDeck1.setter
    def starndardDeck1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cards_Card__starndardDeck1", None)
        self.__starndardDeck1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "card0"):
                    opp_val = getattr(item, "card0", None)
                    
                    if opp_val == self:
                        setattr(item, "card0", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "card0"):
                    opp_val = getattr(item, "card0", None)
                    
                    setattr(item, "card0", self)
                    

