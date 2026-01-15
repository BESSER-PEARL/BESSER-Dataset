from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Arc:

    pass
class PetriNet_TPArc(Arc):

    pass
class PetriNet_PTArc(Arc):

    pass
class PetriNet_Arc(ABC):

    def __init__(self, name: str, weight: int, PetriNet_Arc: "PetriNet_PetriNet" = None):
        self.name = name
        self.weight = weight
        self.PetriNet_Arc = PetriNet_Arc
        
    @property
    def weight(self) -> int:
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def PetriNet_Arc(self):
        return self.__PetriNet_Arc

    @PetriNet_Arc.setter
    def PetriNet_Arc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_Arc__PetriNet_Arc", None)
        self.__PetriNet_Arc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNet_PetriNet2"):
                opp_val = getattr(old_value, "PetriNet_PetriNet2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNet_PetriNet2"):
                opp_val = getattr(value, "PetriNet_PetriNet2", None)
                if opp_val is None:
                    setattr(value, "PetriNet_PetriNet2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class PetriNet_Node(ABC):

    def __init__(self, name: str, PetriNet_Node: "PetriNet_PetriNet" = None):
        self.name = name
        self.PetriNet_Node = PetriNet_Node
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def PetriNet_Node(self):
        return self.__PetriNet_Node

    @PetriNet_Node.setter
    def PetriNet_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_Node__PetriNet_Node", None)
        self.__PetriNet_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNet_PetriNet"):
                opp_val = getattr(old_value, "PetriNet_PetriNet", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNet_PetriNet"):
                opp_val = getattr(value, "PetriNet_PetriNet", None)
                if opp_val is None:
                    setattr(value, "PetriNet_PetriNet", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class PetriNet_PetriNet:

    pass
class Node:

    pass
class PetriNet_Transition(Node):

    pass
class PetriNet_Place(Node):

    def __init__(self, marking: int, PetriNet_Place: "PetriNet_PTArc" = None, PetriNet_Place10: "PetriNet_TPArc" = None):
        self.marking = marking
        self.PetriNet_Place = PetriNet_Place
        self.PetriNet_Place10 = PetriNet_Place10
        
    @property
    def marking(self) -> int:
        return self.__marking

    @marking.setter
    def marking(self, marking: int):
        self.__marking = marking

    @property
    def PetriNet_Place10(self):
        return self.__PetriNet_Place10

    @PetriNet_Place10.setter
    def PetriNet_Place10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_Place__PetriNet_Place10", None)
        self.__PetriNet_Place10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNet_TPArc9"):
                opp_val = getattr(old_value, "PetriNet_TPArc9", None)
                if opp_val == self:
                    setattr(old_value, "PetriNet_TPArc9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNet_TPArc9"):
                opp_val = getattr(value, "PetriNet_TPArc9", None)
                setattr(value, "PetriNet_TPArc9", self)

    @property
    def PetriNet_Place(self):
        return self.__PetriNet_Place

    @PetriNet_Place.setter
    def PetriNet_Place(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_Place__PetriNet_Place", None)
        self.__PetriNet_Place = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNet_PTArc"):
                opp_val = getattr(old_value, "PetriNet_PTArc", None)
                if opp_val == self:
                    setattr(old_value, "PetriNet_PTArc", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNet_PTArc"):
                opp_val = getattr(value, "PetriNet_PTArc", None)
                setattr(value, "PetriNet_PTArc", self)
