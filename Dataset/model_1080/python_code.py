from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Node:

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

class PetriNet_Transition(Node):

    pass
class PetriNet_Arc:

    def __init__(self, weight: int, PetriNet_Arc: "PetriNet_PetriNet" = None, Arc: "PetriNet_Node" = None, Arc5: "PetriNet_Node" = None, outgoing: "PetriNet_Node" = None, ingoing: "PetriNet_Node" = None):
        self.weight = weight
        self.PetriNet_Arc = PetriNet_Arc
        self.Arc = Arc
        self.Arc5 = Arc5
        self.outgoing = outgoing
        self.ingoing = ingoing
        
    @property
    def weight(self) -> int:
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight

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

    @property
    def ingoing(self):
        return self.__ingoing

    @ingoing.setter
    def ingoing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_Arc__ingoing", None)
        self.__ingoing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Node8"):
                opp_val = getattr(old_value, "Node8", None)
                if opp_val == self:
                    setattr(old_value, "Node8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Node8"):
                opp_val = getattr(value, "Node8", None)
                setattr(value, "Node8", self)

    @property
    def outgoing(self):
        return self.__outgoing

    @outgoing.setter
    def outgoing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_Arc__outgoing", None)
        self.__outgoing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Node"):
                opp_val = getattr(old_value, "Node", None)
                if opp_val == self:
                    setattr(old_value, "Node", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Node"):
                opp_val = getattr(value, "Node", None)
                setattr(value, "Node", self)

    @property
    def Arc(self):
        return self.__Arc

    @Arc.setter
    def Arc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_Arc__Arc", None)
        self.__Arc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "source"):
                opp_val = getattr(old_value, "source", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "source"):
                opp_val = getattr(value, "source", None)
                if opp_val is None:
                    setattr(value, "source", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Arc5(self):
        return self.__Arc5

    @Arc5.setter
    def Arc5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_Arc__Arc5", None)
        self.__Arc5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "target"):
                opp_val = getattr(old_value, "target", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "target"):
                opp_val = getattr(value, "target", None)
                if opp_val is None:
                    setattr(value, "target", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class PetriNet_Node(ABC):

    def __init__(self, name: str, PetriNet_Node: "PetriNet_PetriNet" = None, source: set["PetriNet_Arc"] = None, target: set["PetriNet_Arc"] = None, Node: "PetriNet_Arc" = None, Node8: "PetriNet_Arc" = None):
        self.name = name
        self.PetriNet_Node = PetriNet_Node
        self.source = source if source is not None else set()
        self.target = target if target is not None else set()
        self.Node = Node
        self.Node8 = Node8
        
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

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_Node__target", None)
        self.__target = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Arc5"):
                    opp_val = getattr(item, "Arc5", None)
                    
                    if opp_val == self:
                        setattr(item, "Arc5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Arc5"):
                    opp_val = getattr(item, "Arc5", None)
                    
                    setattr(item, "Arc5", self)
                    

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_Node__source", None)
        self.__source = value if value is not None else set()
        
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
    def Node(self):
        return self.__Node

    @Node.setter
    def Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_Node__Node", None)
        self.__Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outgoing"):
                opp_val = getattr(old_value, "outgoing", None)
                if opp_val == self:
                    setattr(old_value, "outgoing", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outgoing"):
                opp_val = getattr(value, "outgoing", None)
                setattr(value, "outgoing", self)

    @property
    def Node8(self):
        return self.__Node8

    @Node8.setter
    def Node8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_Node__Node8", None)
        self.__Node8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ingoing"):
                opp_val = getattr(old_value, "ingoing", None)
                if opp_val == self:
                    setattr(old_value, "ingoing", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ingoing"):
                opp_val = getattr(value, "ingoing", None)
                setattr(value, "ingoing", self)

class PetriNet_PetriNet:

    def __init__(self, name: str, PetriNet_PetriNet: set["PetriNet_Node"] = None, PetriNet_PetriNet2: set["PetriNet_Arc"] = None):
        self.name = name
        self.PetriNet_PetriNet = PetriNet_PetriNet if PetriNet_PetriNet is not None else set()
        self.PetriNet_PetriNet2 = PetriNet_PetriNet2 if PetriNet_PetriNet2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def PetriNet_PetriNet(self):
        return self.__PetriNet_PetriNet

    @PetriNet_PetriNet.setter
    def PetriNet_PetriNet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_PetriNet__PetriNet_PetriNet", None)
        self.__PetriNet_PetriNet = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PetriNet_Node"):
                    opp_val = getattr(item, "PetriNet_Node", None)
                    
                    if opp_val == self:
                        setattr(item, "PetriNet_Node", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PetriNet_Node"):
                    opp_val = getattr(item, "PetriNet_Node", None)
                    
                    setattr(item, "PetriNet_Node", self)
                    

    @property
    def PetriNet_PetriNet2(self):
        return self.__PetriNet_PetriNet2

    @PetriNet_PetriNet2.setter
    def PetriNet_PetriNet2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_PetriNet__PetriNet_PetriNet2", None)
        self.__PetriNet_PetriNet2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PetriNet_Arc"):
                    opp_val = getattr(item, "PetriNet_Arc", None)
                    
                    if opp_val == self:
                        setattr(item, "PetriNet_Arc", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PetriNet_Arc"):
                    opp_val = getattr(item, "PetriNet_Arc", None)
                    
                    setattr(item, "PetriNet_Arc", self)
                    
