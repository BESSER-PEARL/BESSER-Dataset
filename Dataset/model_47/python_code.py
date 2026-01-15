from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Arc:

    pass
class petrinet_OutputArc(Arc):

    pass
class Node:

    pass
class petrinet_Transition(Node):

    pass
class petrinet_Place(Node):

    pass
class petrinet_InputArc(Arc):

    pass
class petrinet_Element(ABC):

    pass
class petrinet_PetriNetRelationship:

    pass
class petrinet_PetriNet:

    def __init__(self, name: str, petrinet_PetriNet7: "petrinet_PetriNetRelationship" = None, petrinet_PetriNet10: "petrinet_PetriNetRelationship" = None, petrinet_PetriNet: "petrinet_System" = None, petrinet_PetriNet4: set["petrinet_Element"] = None):
        self.name = name
        self.petrinet_PetriNet7 = petrinet_PetriNet7
        self.petrinet_PetriNet10 = petrinet_PetriNet10
        self.petrinet_PetriNet = petrinet_PetriNet
        self.petrinet_PetriNet4 = petrinet_PetriNet4 if petrinet_PetriNet4 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def petrinet_PetriNet7(self):
        return self.__petrinet_PetriNet7

    @petrinet_PetriNet7.setter
    def petrinet_PetriNet7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_PetriNet__petrinet_PetriNet7", None)
        self.__petrinet_PetriNet7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet_PetriNetRelationship6"):
                opp_val = getattr(old_value, "petrinet_PetriNetRelationship6", None)
                if opp_val == self:
                    setattr(old_value, "petrinet_PetriNetRelationship6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_PetriNetRelationship6"):
                opp_val = getattr(value, "petrinet_PetriNetRelationship6", None)
                setattr(value, "petrinet_PetriNetRelationship6", self)

    @property
    def petrinet_PetriNet4(self):
        return self.__petrinet_PetriNet4

    @petrinet_PetriNet4.setter
    def petrinet_PetriNet4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_PetriNet__petrinet_PetriNet4", None)
        self.__petrinet_PetriNet4 = value if value is not None else set()
        
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
    def petrinet_PetriNet10(self):
        return self.__petrinet_PetriNet10

    @petrinet_PetriNet10.setter
    def petrinet_PetriNet10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_PetriNet__petrinet_PetriNet10", None)
        self.__petrinet_PetriNet10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet_PetriNetRelationship9"):
                opp_val = getattr(old_value, "petrinet_PetriNetRelationship9", None)
                if opp_val == self:
                    setattr(old_value, "petrinet_PetriNetRelationship9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_PetriNetRelationship9"):
                opp_val = getattr(value, "petrinet_PetriNetRelationship9", None)
                setattr(value, "petrinet_PetriNetRelationship9", self)

    @property
    def petrinet_PetriNet(self):
        return self.__petrinet_PetriNet

    @petrinet_PetriNet.setter
    def petrinet_PetriNet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_PetriNet__petrinet_PetriNet", None)
        self.__petrinet_PetriNet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet_System"):
                opp_val = getattr(old_value, "petrinet_System", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_System"):
                opp_val = getattr(value, "petrinet_System", None)
                if opp_val is None:
                    setattr(value, "petrinet_System", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Element:

    pass
class petrinet_Arc(Element):

    pass
class petrinet_Node(Element):

    def __init__(self, minDelay: float, maxDelay: float, name: str):
        self.minDelay = minDelay
        self.maxDelay = maxDelay
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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

class petrinet_System:

    pass