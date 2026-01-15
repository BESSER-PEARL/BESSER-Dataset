from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Node:

    pass
class petrinet_Place(Node):

    pass
class petrinet_Transition(Node):

    def __init__(self, maxDelay: float, minDelay: float, petrinet_Transition: "petrinet_OutputArc" = None, petrinet_Transition5: "petrinet_InputArc" = None):
        self.maxDelay = maxDelay
        self.minDelay = minDelay
        self.petrinet_Transition = petrinet_Transition
        self.petrinet_Transition5 = petrinet_Transition5
        
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

    @property
    def petrinet_Transition5(self):
        return self.__petrinet_Transition5

    @petrinet_Transition5.setter
    def petrinet_Transition5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Transition__petrinet_Transition5", None)
        self.__petrinet_Transition5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet_InputArc"):
                opp_val = getattr(old_value, "petrinet_InputArc", None)
                if opp_val == self:
                    setattr(old_value, "petrinet_InputArc", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_InputArc"):
                opp_val = getattr(value, "petrinet_InputArc", None)
                setattr(value, "petrinet_InputArc", self)

    @property
    def petrinet_Transition(self):
        return self.__petrinet_Transition

    @petrinet_Transition.setter
    def petrinet_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Transition__petrinet_Transition", None)
        self.__petrinet_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet_OutputArc"):
                opp_val = getattr(old_value, "petrinet_OutputArc", None)
                if opp_val == self:
                    setattr(old_value, "petrinet_OutputArc", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_OutputArc"):
                opp_val = getattr(value, "petrinet_OutputArc", None)
                setattr(value, "petrinet_OutputArc", self)

class Arc:

    pass
class petrinet_InputArc(Arc):

    pass
class petrinet_OutputArc(Arc):

    pass
class Element:

    pass
class petrinet_Arc(Element):

    pass
class petrinet_Node(Element):

    pass
class petrinet_PetriNet:

    pass
class petrinet_Element(ABC):

    def __init__(self, name: str, petrinet_Element: "petrinet_PetriNet" = None):
        self.name = name
        self.petrinet_Element = petrinet_Element
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def petrinet_Element(self):
        return self.__petrinet_Element

    @petrinet_Element.setter
    def petrinet_Element(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Element__petrinet_Element", None)
        self.__petrinet_Element = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet_PetriNet"):
                opp_val = getattr(old_value, "petrinet_PetriNet", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_PetriNet"):
                opp_val = getattr(value, "petrinet_PetriNet", None)
                if opp_val is None:
                    setattr(value, "petrinet_PetriNet", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
