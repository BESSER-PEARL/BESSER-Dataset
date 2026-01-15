from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class petrinet_NetworkSystem:

    pass
class Node:

    pass
class petrinet_Place(Node):

    pass
class petrinet_Transition(Node):

    def __init__(self, maxDelay: float, minDelay: float, petrinet_Transition: "petrinet_OutputArc" = None, petrinet_Transition10: "petrinet_InputArc" = None):
        self.maxDelay = maxDelay
        self.minDelay = minDelay
        self.petrinet_Transition = petrinet_Transition
        self.petrinet_Transition10 = petrinet_Transition10
        
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

    @property
    def petrinet_Transition10(self):
        return self.__petrinet_Transition10

    @petrinet_Transition10.setter
    def petrinet_Transition10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Transition__petrinet_Transition10", None)
        self.__petrinet_Transition10 = value
        
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

class Arc:

    pass
class petrinet_InputArc(Arc):

    pass
class petrinet_OutputArc(Arc):

    pass
class petrinet_PetriNet:

    def __init__(self, name: str, petrinet_PetriNet2: "petrinet_Arc" = None, petrinet_PetriNet: set["petrinet_Element"] = None, petrinet_PetriNet5: "petrinet_Arc" = None, petrinet_PetriNet15: "petrinet_NetworkSystem" = None):
        self.name = name
        self.petrinet_PetriNet2 = petrinet_PetriNet2
        self.petrinet_PetriNet = petrinet_PetriNet if petrinet_PetriNet is not None else set()
        self.petrinet_PetriNet5 = petrinet_PetriNet5
        self.petrinet_PetriNet15 = petrinet_PetriNet15
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def petrinet_PetriNet15(self):
        return self.__petrinet_PetriNet15

    @petrinet_PetriNet15.setter
    def petrinet_PetriNet15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_PetriNet__petrinet_PetriNet15", None)
        self.__petrinet_PetriNet15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet_NetworkSystem"):
                opp_val = getattr(old_value, "petrinet_NetworkSystem", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_NetworkSystem"):
                opp_val = getattr(value, "petrinet_NetworkSystem", None)
                if opp_val is None:
                    setattr(value, "petrinet_NetworkSystem", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def petrinet_PetriNet2(self):
        return self.__petrinet_PetriNet2

    @petrinet_PetriNet2.setter
    def petrinet_PetriNet2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_PetriNet__petrinet_PetriNet2", None)
        self.__petrinet_PetriNet2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet_Arc"):
                opp_val = getattr(old_value, "petrinet_Arc", None)
                if opp_val == self:
                    setattr(old_value, "petrinet_Arc", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_Arc"):
                opp_val = getattr(value, "petrinet_Arc", None)
                setattr(value, "petrinet_Arc", self)

    @property
    def petrinet_PetriNet(self):
        return self.__petrinet_PetriNet

    @petrinet_PetriNet.setter
    def petrinet_PetriNet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_PetriNet__petrinet_PetriNet", None)
        self.__petrinet_PetriNet = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "petrinet_Element"):
                    opp_val = getattr(item, "petrinet_Element", None)
                    
                    if opp_val == self:
                        setattr(item, "petrinet_Element", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petrinet_Element"):
                    opp_val = getattr(item, "petrinet_Element", None)
                    
                    setattr(item, "petrinet_Element", self)
                    

    @property
    def petrinet_PetriNet5(self):
        return self.__petrinet_PetriNet5

    @petrinet_PetriNet5.setter
    def petrinet_PetriNet5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_PetriNet__petrinet_PetriNet5", None)
        self.__petrinet_PetriNet5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet_Arc4"):
                opp_val = getattr(old_value, "petrinet_Arc4", None)
                if opp_val == self:
                    setattr(old_value, "petrinet_Arc4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_Arc4"):
                opp_val = getattr(value, "petrinet_Arc4", None)
                setattr(value, "petrinet_Arc4", self)

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

class Element:

    pass
class petrinet_Arc(Element):

    pass
class petrinet_Node(Element):

    pass