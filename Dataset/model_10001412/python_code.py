from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Cards:

    def __init__(self, string: str, int: str, int1: str, bool: str, deck1: "Deck" = None):
        self.string = string
        self.int = int
        self.int1 = int1
        self.bool = bool
        self.deck1 = deck1
        
        pass
    @property
    def int(self):
        return self.__int
    @int.setter
    def int(self, int: str):
        self.__int = int

    @property
    def bool(self):
        return self.__bool
    @bool.setter
    def bool(self, bool: str):
        self.__bool = bool

    @property
    def int1(self):
        return self.__int1
    @int1.setter
    def int1(self, int1: str):
        self.__int1 = int1

    @property
    def string(self):
        return self.__string
    @string.setter
    def string(self, string: str):
        self.__string = string

    @property
    def deck1(self):
        return self.__deck1
    @deck1.setter
    def deck1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cards__deck1", None)
        self.__deck1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cards0"):
                opp_val = getattr(old_value, "cards0", None)
                if opp_val == self:
                    setattr(old_value, "cards0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cards0"):
                opp_val = getattr(value, "cards0", None)
                setattr(value, "cards0", self)



class Deck:

    def __init__(self, int: str, cards0: "Cards" = None):
        self.int = int
        self.cards0 = cards0
        
        pass
    @property
    def int(self):
        return self.__int
    @int.setter
    def int(self, int: str):
        self.__int = int

    @property
    def cards0(self):
        return self.__cards0
    @cards0.setter
    def cards0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Deck__cards0", None)
        self.__cards0 = value
        
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



class Player:

    def __init__(self, int: str, int1: str, Deck: str, Card: str):
        self.int = int
        self.int1 = int1
        self.Deck = Deck
        self.Card = Card
        
        pass
    @property
    def int(self):
        return self.__int
    @int.setter
    def int(self, int: str):
        self.__int = int

    @property
    def int1(self):
        return self.__int1
    @int1.setter
    def int1(self, int1: str):
        self.__int1 = int1

    @property
    def Deck(self):
        return self.__Deck
    @Deck.setter
    def Deck(self, Deck: str):
        self.__Deck = Deck

    @property
    def Card(self):
        return self.__Card
    @Card.setter
    def Card(self, Card: str):
        self.__Card = Card



class Account:

    def __init__(self, int: str, string: str, int1: str):
        self.int = int
        self.string = string
        self.int1 = int1
        
        pass
    @property
    def int1(self):
        return self.__int1
    @int1.setter
    def int1(self, int1: str):
        self.__int1 = int1

    @property
    def int(self):
        return self.__int
    @int.setter
    def int(self, int: str):
        self.__int = int

    @property
    def string(self):
        return self.__string
    @string.setter
    def string(self, string: str):
        self.__string = string



class InputValidation:

    pass


class Blackjack:

    pass


class Main:

    pass
