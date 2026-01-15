from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Node:

    pass
class petrinet_Transition(Node):

    pass
class petrinet_Place(Node):

    def __init__(self, capacity: int, tokens: int):
        self.capacity = capacity
        self.tokens = tokens
        
    @property
    def capacity(self) -> int:
        return self.__capacity

    @capacity.setter
    def capacity(self, capacity: int):
        self.__capacity = capacity

    @property
    def tokens(self) -> int:
        return self.__tokens

    @tokens.setter
    def tokens(self, tokens: int):
        self.__tokens = tokens

class petrinet_PetriNet:

    pass
class petrinet_Arc:

    def __init__(self, weight: int, petrinet_Arc: "petrinet_PetriNet" = None, petrinet_Arc7: "petrinet_Node" = None, petrinet_Arc4: "petrinet_Node" = None):
        self.weight = weight
        self.petrinet_Arc = petrinet_Arc
        self.petrinet_Arc7 = petrinet_Arc7
        self.petrinet_Arc4 = petrinet_Arc4
        
    @property
    def weight(self) -> int:
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight

    @property
    def petrinet_Arc7(self):
        return self.__petrinet_Arc7

    @petrinet_Arc7.setter
    def petrinet_Arc7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Arc__petrinet_Arc7", None)
        self.__petrinet_Arc7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet_Node8"):
                opp_val = getattr(old_value, "petrinet_Node8", None)
                if opp_val == self:
                    setattr(old_value, "petrinet_Node8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_Node8"):
                opp_val = getattr(value, "petrinet_Node8", None)
                setattr(value, "petrinet_Node8", self)

    @property
    def petrinet_Arc(self):
        return self.__petrinet_Arc

    @petrinet_Arc.setter
    def petrinet_Arc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Arc__petrinet_Arc", None)
        self.__petrinet_Arc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet_PetriNet2"):
                opp_val = getattr(old_value, "petrinet_PetriNet2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_PetriNet2"):
                opp_val = getattr(value, "petrinet_PetriNet2", None)
                if opp_val is None:
                    setattr(value, "petrinet_PetriNet2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def petrinet_Arc4(self):
        return self.__petrinet_Arc4

    @petrinet_Arc4.setter
    def petrinet_Arc4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Arc__petrinet_Arc4", None)
        self.__petrinet_Arc4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet_Node5"):
                opp_val = getattr(old_value, "petrinet_Node5", None)
                if opp_val == self:
                    setattr(old_value, "petrinet_Node5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_Node5"):
                opp_val = getattr(value, "petrinet_Node5", None)
                setattr(value, "petrinet_Node5", self)

class petrinet_Node(ABC):

    def __init__(self, name: str, petrinet_Node: "petrinet_PetriNet" = None, petrinet_Node5: "petrinet_Arc" = None, petrinet_Node8: "petrinet_Arc" = None):
        self.name = name
        self.petrinet_Node = petrinet_Node
        self.petrinet_Node5 = petrinet_Node5
        self.petrinet_Node8 = petrinet_Node8
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def petrinet_Node8(self):
        return self.__petrinet_Node8

    @petrinet_Node8.setter
    def petrinet_Node8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Node__petrinet_Node8", None)
        self.__petrinet_Node8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet_Arc7"):
                opp_val = getattr(old_value, "petrinet_Arc7", None)
                if opp_val == self:
                    setattr(old_value, "petrinet_Arc7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_Arc7"):
                opp_val = getattr(value, "petrinet_Arc7", None)
                setattr(value, "petrinet_Arc7", self)

    @property
    def petrinet_Node(self):
        return self.__petrinet_Node

    @petrinet_Node.setter
    def petrinet_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Node__petrinet_Node", None)
        self.__petrinet_Node = value
        
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

    @property
    def petrinet_Node5(self):
        return self.__petrinet_Node5

    @petrinet_Node5.setter
    def petrinet_Node5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Node__petrinet_Node5", None)
        self.__petrinet_Node5 = value
        
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
