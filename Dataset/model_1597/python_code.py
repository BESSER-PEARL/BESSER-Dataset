from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Node:

    pass
class Petrinet_Place(Node):

    pass
class Petrinet_Transition(Node):

    def __init__(self, maxDelay: float, minDelay: float, Petrinet_Transition: "Petrinet_OutputArc" = None, Petrinet_Transition5: "Petrinet_InputArc" = None):
        self.maxDelay = maxDelay
        self.minDelay = minDelay
        self.Petrinet_Transition = Petrinet_Transition
        self.Petrinet_Transition5 = Petrinet_Transition5
        
    @property
    def maxDelay(self) -> float:
        return self.__maxDelay

    @maxDelay.setter
    def maxDelay(self, maxDelay: float):
        self.__maxDelay = maxDelay

    @property
    def minDelay(self) -> float:
        return self.__minDelay

    @minDelay.setter
    def minDelay(self, minDelay: float):
        self.__minDelay = minDelay

    @property
    def Petrinet_Transition5(self):
        return self.__Petrinet_Transition5

    @Petrinet_Transition5.setter
    def Petrinet_Transition5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Petrinet_Transition__Petrinet_Transition5", None)
        self.__Petrinet_Transition5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Petrinet_InputArc"):
                opp_val = getattr(old_value, "Petrinet_InputArc", None)
                if opp_val == self:
                    setattr(old_value, "Petrinet_InputArc", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Petrinet_InputArc"):
                opp_val = getattr(value, "Petrinet_InputArc", None)
                setattr(value, "Petrinet_InputArc", self)

    @property
    def Petrinet_Transition(self):
        return self.__Petrinet_Transition

    @Petrinet_Transition.setter
    def Petrinet_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Petrinet_Transition__Petrinet_Transition", None)
        self.__Petrinet_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Petrinet_OutputArc"):
                opp_val = getattr(old_value, "Petrinet_OutputArc", None)
                if opp_val == self:
                    setattr(old_value, "Petrinet_OutputArc", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Petrinet_OutputArc"):
                opp_val = getattr(value, "Petrinet_OutputArc", None)
                setattr(value, "Petrinet_OutputArc", self)

class Arc:

    pass
class Petrinet_InputArc(Arc):

    pass
class Petrinet_OutputArc(Arc):

    pass
class Petrinet_Petrinet:

    pass
class Petrinet_Element(ABC):

    def __init__(self, name: str, Petrinet_Element: "Petrinet_Petrinet" = None):
        self.name = name
        self.Petrinet_Element = Petrinet_Element
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Petrinet_Element(self):
        return self.__Petrinet_Element

    @Petrinet_Element.setter
    def Petrinet_Element(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Petrinet_Element__Petrinet_Element", None)
        self.__Petrinet_Element = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Petrinet_Petrinet"):
                opp_val = getattr(old_value, "Petrinet_Petrinet", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Petrinet_Petrinet"):
                opp_val = getattr(value, "Petrinet_Petrinet", None)
                if opp_val is None:
                    setattr(value, "Petrinet_Petrinet", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Element:

    pass
class Petrinet_Arc(Element):

    pass
class Petrinet_Node(Element):

    pass