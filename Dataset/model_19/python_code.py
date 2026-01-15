from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class petrinet2_Element(ABC):

    def __init__(self, name: str, petrinet2_Element: "petrinet2_Petrinet" = None):
        self.name = name
        self.petrinet2_Element = petrinet2_Element
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def petrinet2_Element(self):
        return self.__petrinet2_Element

    @petrinet2_Element.setter
    def petrinet2_Element(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet2_Element__petrinet2_Element", None)
        self.__petrinet2_Element = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet2_Petrinet"):
                opp_val = getattr(old_value, "petrinet2_Petrinet", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet2_Petrinet"):
                opp_val = getattr(value, "petrinet2_Petrinet", None)
                if opp_val is None:
                    setattr(value, "petrinet2_Petrinet", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class petrinet2_Petrinet:

    pass
class Node:

    pass
class petrinet2_Transition(Node):

    def __init__(self, maxDelay: float, minDelay: float):
        self.maxDelay = maxDelay
        self.minDelay = minDelay
        
    @property
    def minDelay(self) -> float:
        return self.__minDelay

    @minDelay.setter
    def minDelay(self, minDelay: float):
        self.__minDelay = minDelay

    @property
    def maxDelay(self) -> float:
        return self.__maxDelay

    @maxDelay.setter
    def maxDelay(self, maxDelay: float):
        self.__maxDelay = maxDelay

class petrinet2_Place(Node):

    pass
class Element:

    pass
class petrinet2_Arc(Element):

    pass
class petrinet2_Node(Element):

    pass