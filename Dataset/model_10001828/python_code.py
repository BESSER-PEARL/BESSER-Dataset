from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Enumeration(Enum):
    pass

############################################
# Definition of Classes
############################################










class Cards:

    def __init__(self, Suit: str, Character: str, deck5: "Deck" = None):
        self.Suit = Suit
        self.Character = Character
        self.deck5 = deck5
        
        pass
    @property
    def Character(self):
        return self.__Character
    @Character.setter
    def Character(self, Character: str):
        self.__Character = Character

    @property
    def Suit(self):
        return self.__Suit
    @Suit.setter
    def Suit(self, Suit: str):
        self.__Suit = Suit

    @property
    def deck5(self):
        return self.__deck5
    @deck5.setter
    def deck5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cards__deck5", None)
        self.__deck5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cards4"):
                opp_val = getattr(old_value, "cards4", None)
                if opp_val == self:
                    setattr(old_value, "cards4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cards4"):
                opp_val = getattr(value, "cards4", None)
                setattr(value, "cards4", self)



class Deck:

    def __init__(self, attribute: str, elevens3: "Elevens" = None, cards4: "Cards" = None):
        self.attribute = attribute
        self.elevens3 = elevens3
        self.cards4 = cards4
        
        pass
    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def elevens3(self):
        return self.__elevens3
    @elevens3.setter
    def elevens3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Deck__elevens3", None)
        self.__elevens3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "deck2"):
                opp_val = getattr(old_value, "deck2", None)
                if opp_val == self:
                    setattr(old_value, "deck2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "deck2"):
                opp_val = getattr(value, "deck2", None)
                setattr(value, "deck2", self)

    @property
    def cards4(self):
        return self.__cards4
    @cards4.setter
    def cards4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Deck__cards4", None)
        self.__cards4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "deck5"):
                opp_val = getattr(old_value, "deck5", None)
                if opp_val == self:
                    setattr(old_value, "deck5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "deck5"):
                opp_val = getattr(value, "deck5", None)
                setattr(value, "deck5", self)



class Player:

    def __init__(self, wins: int, losses: int, winRate: str, elevens1: "Elevens" = None):
        self.wins = wins
        self.losses = losses
        self.winRate = winRate
        self.elevens1 = elevens1
        
        pass
    @property
    def wins(self):
        return self.__wins
    @wins.setter
    def wins(self, wins: int):
        self.__wins = wins

    @property
    def losses(self):
        return self.__losses
    @losses.setter
    def losses(self, losses: int):
        self.__losses = losses

    @property
    def winRate(self):
        return self.__winRate
    @winRate.setter
    def winRate(self, winRate: str):
        self.__winRate = winRate

    @property
    def elevens1(self):
        return self.__elevens1
    @elevens1.setter
    def elevens1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Player__elevens1", None)
        self.__elevens1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "player0"):
                opp_val = getattr(old_value, "player0", None)
                if opp_val == self:
                    setattr(old_value, "player0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "player0"):
                opp_val = getattr(value, "player0", None)
                setattr(value, "player0", self)



class Elevens:

    def __init__(self, _attr: Player, player0: "Player" = None, deck2: "Deck" = None):
        self._attr = _attr
        self.player0 = player0
        self.deck2 = deck2
        
        pass
    @property
    def _attr(self):
        return self.___attr
    @_attr.setter
    def _attr(self, _attr: Player):
        self.___attr = _attr

    @property
    def deck2(self):
        return self.__deck2
    @deck2.setter
    def deck2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elevens__deck2", None)
        self.__deck2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "elevens3"):
                opp_val = getattr(old_value, "elevens3", None)
                if opp_val == self:
                    setattr(old_value, "elevens3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "elevens3"):
                opp_val = getattr(value, "elevens3", None)
                setattr(value, "elevens3", self)

    @property
    def player0(self):
        return self.__player0
    @player0.setter
    def player0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elevens__player0", None)
        self.__player0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "elevens1"):
                opp_val = getattr(old_value, "elevens1", None)
                if opp_val == self:
                    setattr(old_value, "elevens1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "elevens1"):
                opp_val = getattr(value, "elevens1", None)
                setattr(value, "elevens1", self)

