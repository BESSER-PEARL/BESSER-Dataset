from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ArcKind(Enum):
    INPUT = "INPUT"
    OUTPUT = "OUTPUT"


############################################
# Definition of Classes
############################################

class Transition:

    pass
class stochasticpetrinet_ImmediateTransition(Transition):

    pass
class stochasticpetrinet_TimedTransition(Transition):

    pass
class stochasticpetrinet_Arc:

    def __init__(self, kind: str, Arc: "stochasticpetrinet_Transition" = None, arcs: "stochasticpetrinet_Transition" = None, stochasticpetrinet_Arc: "stochasticpetrinet_Place" = None):
        self.kind = kind
        self.Arc = Arc
        self.arcs = arcs
        self.stochasticpetrinet_Arc = stochasticpetrinet_Arc
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def arcs(self):
        return self.__arcs

    @arcs.setter
    def arcs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stochasticpetrinet_Arc__arcs", None)
        self.__arcs = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Transition"):
                opp_val = getattr(old_value, "Transition", None)
                if opp_val == self:
                    setattr(old_value, "Transition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Transition"):
                opp_val = getattr(value, "Transition", None)
                setattr(value, "Transition", self)

    @property
    def stochasticpetrinet_Arc(self):
        return self.__stochasticpetrinet_Arc

    @stochasticpetrinet_Arc.setter
    def stochasticpetrinet_Arc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stochasticpetrinet_Arc__stochasticpetrinet_Arc", None)
        self.__stochasticpetrinet_Arc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stochasticpetrinet_Place"):
                opp_val = getattr(old_value, "stochasticpetrinet_Place", None)
                if opp_val == self:
                    setattr(old_value, "stochasticpetrinet_Place", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stochasticpetrinet_Place"):
                opp_val = getattr(value, "stochasticpetrinet_Place", None)
                setattr(value, "stochasticpetrinet_Place", self)

    @property
    def Arc(self):
        return self.__Arc

    @Arc.setter
    def Arc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stochasticpetrinet_Arc__Arc", None)
        self.__Arc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transition"):
                opp_val = getattr(old_value, "transition", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transition"):
                opp_val = getattr(value, "transition", None)
                if opp_val is None:
                    setattr(value, "transition", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Node:

    pass
class stochasticpetrinet_Place(Node):

    def __init__(self, tokens: int, stochasticpetrinet_Place: "stochasticpetrinet_Arc" = None):
        self.tokens = tokens
        self.stochasticpetrinet_Place = stochasticpetrinet_Place
        
    @property
    def tokens(self) -> int:
        return self.__tokens

    @tokens.setter
    def tokens(self, tokens: int):
        self.__tokens = tokens

    @property
    def stochasticpetrinet_Place(self):
        return self.__stochasticpetrinet_Place

    @stochasticpetrinet_Place.setter
    def stochasticpetrinet_Place(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_stochasticpetrinet_Place__stochasticpetrinet_Place", None)
        self.__stochasticpetrinet_Place = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stochasticpetrinet_Arc"):
                opp_val = getattr(old_value, "stochasticpetrinet_Arc", None)
                if opp_val == self:
                    setattr(old_value, "stochasticpetrinet_Arc", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stochasticpetrinet_Arc"):
                opp_val = getattr(value, "stochasticpetrinet_Arc", None)
                setattr(value, "stochasticpetrinet_Arc", self)

class stochasticpetrinet_Transition(Node):

    pass
class stochasticpetrinet_Node(ABC):

    pass
class stochasticpetrinet_PetriNet:

    pass