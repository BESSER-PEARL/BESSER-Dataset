from __future__ import annotations
from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Kind(Enum):
    pass

############################################
# Definition of Classes
############################################










class Card:

    def __init__(self, suit: str, kind: Kind, player1: "Player" = None):
        self.suit = suit
        self.kind = kind
        self.player1 = player1
        
        pass
    @property
    def kind(self):
        return self.__kind
    @kind.setter
    def kind(self, kind: Kind):
        self.__kind = kind

    @property
    def suit(self):
        return self.__suit
    @suit.setter
    def suit(self, suit: str):
        self.__suit = suit

    @property
    def player1(self):
        return self.__player1
    @player1.setter
    def player1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Card__player1", None)
        self.__player1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cards0"):
                opp_val = getattr(old_value, "cards0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cards0"):
                opp_val = getattr(value, "cards0", None)
                if opp_val is None:
                    setattr(value, "cards0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Player(ABC):

    def __init__(self, name: str, cards0: set["Card"] = None, game3: "Game" = None):
        self.name = name
        self.cards0 = cards0 if cards0 is not None else set()
        self.game3 = game3
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cards0(self):
        return self.__cards0
    @cards0.setter
    def cards0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Player__cards0", None)
        self.__cards0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "player1"):
                    opp_val = getattr(item, "player1", None)
                    
                    if opp_val == self:
                        setattr(item, "player1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "player1"):
                    opp_val = getattr(item, "player1", None)
                    
                    setattr(item, "player1", self)
                    

    @property
    def game3(self):
        return self.__game3
    @game3.setter
    def game3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Player__game3", None)
        self.__game3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "player2"):
                opp_val = getattr(old_value, "player2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "player2"):
                opp_val = getattr(value, "player2", None)
                if opp_val is None:
                    setattr(value, "player2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Game(ABC):

    def __init__(self, name: str, player2: set["Player"] = None):
        self.name = name
        self.player2 = player2 if player2 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def player2(self):
        return self.__player2
    @player2.setter
    def player2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Game__player2", None)
        self.__player2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "game3"):
                    opp_val = getattr(item, "game3", None)
                    
                    if opp_val == self:
                        setattr(item, "game3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "game3"):
                    opp_val = getattr(item, "game3", None)
                    
                    setattr(item, "game3", self)
                    

