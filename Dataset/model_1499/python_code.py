from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class PetriNets_Token:

    pass
class Node:

    pass
class PetriNets_Place(Node):

    def __init__(self, capacity: int, PetriNets_Place: set["PetriNets_Token"] = None):
        self.capacity = capacity
        self.PetriNets_Place = PetriNets_Place if PetriNets_Place is not None else set()
        
    @property
    def capacity(self) -> int:
        return self.__capacity

    @capacity.setter
    def capacity(self, capacity: int):
        self.__capacity = capacity

    @property
    def PetriNets_Place(self):
        return self.__PetriNets_Place

    @PetriNets_Place.setter
    def PetriNets_Place(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNets_Place__PetriNets_Place", None)
        self.__PetriNets_Place = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PetriNets_Token"):
                    opp_val = getattr(item, "PetriNets_Token", None)
                    
                    if opp_val == self:
                        setattr(item, "PetriNets_Token", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PetriNets_Token"):
                    opp_val = getattr(item, "PetriNets_Token", None)
                    
                    setattr(item, "PetriNets_Token", self)
                    

class PetriNets_Transition(Node):

    pass
class Object:

    pass
class PetriNets_Arc(Object):

    pass
class PetriNets_Node(Object):

    def __init__(self, name: str, target: set["PetriNets_Arc"] = None, source: set["PetriNets_Arc"] = None, Node: "PetriNets_Arc" = None, Node6: "PetriNets_Arc" = None):
        self.name = name
        self.target = target if target is not None else set()
        self.source = source if source is not None else set()
        self.Node = Node
        self.Node6 = Node6
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNets_Node__target", None)
        self.__target = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Arc"):
                    opp_val = getattr(item, "Arc", None)
                    
                    if opp_val == self:
                        setattr(item, "Arc", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Arc"):
                    opp_val = getattr(item, "Arc", None)
                    
                    setattr(item, "Arc", self)
                    

    @property
    def Node6(self):
        return self.__Node6

    @Node6.setter
    def Node6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNets_Node__Node6", None)
        self.__Node6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "in"):
                opp_val = getattr(old_value, "in", None)
                if opp_val == self:
                    setattr(old_value, "in", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "in"):
                opp_val = getattr(value, "in", None)
                setattr(value, "in", self)

    @property
    def Node(self):
        return self.__Node

    @Node.setter
    def Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNets_Node__Node", None)
        self.__Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "out"):
                opp_val = getattr(old_value, "out", None)
                if opp_val == self:
                    setattr(old_value, "out", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "out"):
                opp_val = getattr(value, "out", None)
                setattr(value, "out", self)

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNets_Node__source", None)
        self.__source = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Arc3"):
                    opp_val = getattr(item, "Arc3", None)
                    
                    if opp_val == self:
                        setattr(item, "Arc3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Arc3"):
                    opp_val = getattr(item, "Arc3", None)
                    
                    setattr(item, "Arc3", self)
                    

class PetriNets_PetriNet:

    pass
class PetriNets_Object(ABC):

    pass