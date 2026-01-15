from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Arc:

    pass
class PN_InputArc(Arc):

    pass
class PN_OutputArc(Arc):

    pass
class Node:

    pass
class PN_Place(Node):

    pass
class PN_Transition(Node):

    def __init__(self, maxDelay: float, minDelay: float, PN_Transition: "PN_OutputArc" = None, PN_Transition8: "PN_InputArc" = None):
        self.maxDelay = maxDelay
        self.minDelay = minDelay
        self.PN_Transition = PN_Transition
        self.PN_Transition8 = PN_Transition8
        
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
    def PN_Transition(self):
        return self.__PN_Transition

    @PN_Transition.setter
    def PN_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PN_Transition__PN_Transition", None)
        self.__PN_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PN_OutputArc"):
                opp_val = getattr(old_value, "PN_OutputArc", None)
                if opp_val == self:
                    setattr(old_value, "PN_OutputArc", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PN_OutputArc"):
                opp_val = getattr(value, "PN_OutputArc", None)
                setattr(value, "PN_OutputArc", self)

    @property
    def PN_Transition8(self):
        return self.__PN_Transition8

    @PN_Transition8.setter
    def PN_Transition8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PN_Transition__PN_Transition8", None)
        self.__PN_Transition8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PN_InputArc7"):
                opp_val = getattr(old_value, "PN_InputArc7", None)
                if opp_val == self:
                    setattr(old_value, "PN_InputArc7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PN_InputArc7"):
                opp_val = getattr(value, "PN_InputArc7", None)
                setattr(value, "PN_InputArc7", self)

class NamedElement:

    pass
class PN_Arc(NamedElement):

    pass
class PN_Node(NamedElement):

    pass
class PN_NamedElement(ABC):

    def __init__(self, name: str, PN_NamedElement: "PN_PetriNet" = None):
        self.name = name
        self.PN_NamedElement = PN_NamedElement
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def PN_NamedElement(self):
        return self.__PN_NamedElement

    @PN_NamedElement.setter
    def PN_NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PN_NamedElement__PN_NamedElement", None)
        self.__PN_NamedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PN_PetriNet"):
                opp_val = getattr(old_value, "PN_PetriNet", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PN_PetriNet"):
                opp_val = getattr(value, "PN_PetriNet", None)
                if opp_val is None:
                    setattr(value, "PN_PetriNet", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class PN_PetriNet:

    def __init__(self, name: str, PN_PetriNet: set["PN_NamedElement"] = None):
        self.name = name
        self.PN_PetriNet = PN_PetriNet if PN_PetriNet is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def PN_PetriNet(self):
        return self.__PN_PetriNet

    @PN_PetriNet.setter
    def PN_PetriNet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PN_PetriNet__PN_PetriNet", None)
        self.__PN_PetriNet = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PN_NamedElement"):
                    opp_val = getattr(item, "PN_NamedElement", None)
                    
                    if opp_val == self:
                        setattr(item, "PN_NamedElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PN_NamedElement"):
                    opp_val = getattr(item, "PN_NamedElement", None)
                    
                    setattr(item, "PN_NamedElement", self)
                    
