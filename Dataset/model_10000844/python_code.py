from __future__ import annotations
from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Operation(Enum):
    pass
class Kind(Enum):
    pass

############################################
# Definition of Classes
############################################










class Card:

    def __init__(self, operation: str, kind: Kind, deck1: "Deck" = None, player5: "Player" = None):
        self.operation = operation
        self.kind = kind
        self.deck1 = deck1
        self.player5 = player5
        
        pass
    @property
    def kind(self):
        return self.__kind
    @kind.setter
    def kind(self, kind: Kind):
        self.__kind = kind

    @property
    def operation(self):
        return self.__operation
    @operation.setter
    def operation(self, operation: str):
        self.__operation = operation

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

    @property
    def player5(self):
        return self.__player5
    @player5.setter
    def player5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Card__player5", None)
        self.__player5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cards4"):
                opp_val = getattr(old_value, "cards4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cards4"):
                opp_val = getattr(value, "cards4", None)
                if opp_val is None:
                    setattr(value, "cards4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Player(ABC):

    pass


class Deck:

    pass
