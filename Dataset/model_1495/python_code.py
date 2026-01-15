from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class PetriNet_Arc:

    def __init__(self, name: str, weight: int, PetriNet_Arc4: "PetriNet_Node" = None, PetriNet_Arc7: "PetriNet_Node" = None, PetriNet_Arc: "PetriNet_PetriNet" = None):
        self.name = name
        self.weight = weight
        self.PetriNet_Arc4 = PetriNet_Arc4
        self.PetriNet_Arc7 = PetriNet_Arc7
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
    def PetriNet_Arc4(self):
        return self.__PetriNet_Arc4

    @PetriNet_Arc4.setter
    def PetriNet_Arc4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_Arc__PetriNet_Arc4", None)
        self.__PetriNet_Arc4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNet_Node5"):
                opp_val = getattr(old_value, "PetriNet_Node5", None)
                if opp_val == self:
                    setattr(old_value, "PetriNet_Node5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNet_Node5"):
                opp_val = getattr(value, "PetriNet_Node5", None)
                setattr(value, "PetriNet_Node5", self)

    @property
    def PetriNet_Arc7(self):
        return self.__PetriNet_Arc7

    @PetriNet_Arc7.setter
    def PetriNet_Arc7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_Arc__PetriNet_Arc7", None)
        self.__PetriNet_Arc7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNet_Node8"):
                opp_val = getattr(old_value, "PetriNet_Node8", None)
                if opp_val == self:
                    setattr(old_value, "PetriNet_Node8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNet_Node8"):
                opp_val = getattr(value, "PetriNet_Node8", None)
                setattr(value, "PetriNet_Node8", self)

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

class Node:

    pass
class PetriNet_Transition(Node):

    pass
class PetriNet_Place(Node):

    def __init__(self, marking: int):
        self.marking = marking
        
    @property
    def marking(self) -> int:
        return self.__marking

    @marking.setter
    def marking(self, marking: int):
        self.__marking = marking

class PetriNet_Node(ABC):

    def __init__(self, name: str, PetriNet_Node: "PetriNet_PetriNet" = None, PetriNet_Node5: "PetriNet_Arc" = None, PetriNet_Node8: "PetriNet_Arc" = None):
        self.name = name
        self.PetriNet_Node = PetriNet_Node
        self.PetriNet_Node5 = PetriNet_Node5
        self.PetriNet_Node8 = PetriNet_Node8
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def PetriNet_Node8(self):
        return self.__PetriNet_Node8

    @PetriNet_Node8.setter
    def PetriNet_Node8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_Node__PetriNet_Node8", None)
        self.__PetriNet_Node8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNet_Arc7"):
                opp_val = getattr(old_value, "PetriNet_Arc7", None)
                if opp_val == self:
                    setattr(old_value, "PetriNet_Arc7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNet_Arc7"):
                opp_val = getattr(value, "PetriNet_Arc7", None)
                setattr(value, "PetriNet_Arc7", self)

    @property
    def PetriNet_Node5(self):
        return self.__PetriNet_Node5

    @PetriNet_Node5.setter
    def PetriNet_Node5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_Node__PetriNet_Node5", None)
        self.__PetriNet_Node5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNet_Arc4"):
                opp_val = getattr(old_value, "PetriNet_Arc4", None)
                if opp_val == self:
                    setattr(old_value, "PetriNet_Arc4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNet_Arc4"):
                opp_val = getattr(value, "PetriNet_Arc4", None)
                setattr(value, "PetriNet_Arc4", self)

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