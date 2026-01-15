from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class ArcKind(Enum):
    normal = "normal"
    read_arc = "read_arc"


############################################
# Definition of Classes
############################################

class petrinet_Arc:

    def __init__(self, weight: int, kind: str, Arc: "petrinet_Node" = None, Arc5: "petrinet_Node" = None, outgoings: "petrinet_Node" = None, incomings: "petrinet_Node" = None, petrinet_Arc: "petrinet_PetriNet" = None):
        self.weight = weight
        self.kind = kind
        self.Arc = Arc
        self.Arc5 = Arc5
        self.outgoings = outgoings
        self.incomings = incomings
        self.petrinet_Arc = petrinet_Arc
        
    @property
    def weight(self) -> int:
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight

    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def outgoings(self):
        return self.__outgoings

    @outgoings.setter
    def outgoings(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Arc__outgoings", None)
        self.__outgoings = value
        
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
    def Arc5(self):
        return self.__Arc5

    @Arc5.setter
    def Arc5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Arc__Arc5", None)
        self.__Arc5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "target"):
                opp_val = getattr(old_value, "target", None)
                if opp_val == self:
                    setattr(old_value, "target", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "target"):
                opp_val = getattr(value, "target", None)
                setattr(value, "target", self)

    @property
    def Arc(self):
        return self.__Arc

    @Arc.setter
    def Arc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Arc__Arc", None)
        self.__Arc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "source"):
                opp_val = getattr(old_value, "source", None)
                if opp_val == self:
                    setattr(old_value, "source", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "source"):
                opp_val = getattr(value, "source", None)
                setattr(value, "source", self)

    @property
    def incomings(self):
        return self.__incomings

    @incomings.setter
    def incomings(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Arc__incomings", None)
        self.__incomings = value
        
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

class petrinet_Node:

    def __init__(self, name: str, source: "petrinet_Arc" = None, target: "petrinet_Arc" = None, Node: "petrinet_Arc" = None, Node8: "petrinet_Arc" = None, petrinet_Node: "petrinet_PetriNet" = None):
        self.name = name
        self.source = source
        self.target = target
        self.Node = Node
        self.Node8 = Node8
        self.petrinet_Node = petrinet_Node
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
    def Node8(self):
        return self.__Node8

    @Node8.setter
    def Node8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Node__Node8", None)
        self.__Node8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "incomings"):
                opp_val = getattr(old_value, "incomings", None)
                if opp_val == self:
                    setattr(old_value, "incomings", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "incomings"):
                opp_val = getattr(value, "incomings", None)
                setattr(value, "incomings", self)

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Node__target", None)
        self.__target = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Arc5"):
                opp_val = getattr(old_value, "Arc5", None)
                if opp_val == self:
                    setattr(old_value, "Arc5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Arc5"):
                opp_val = getattr(value, "Arc5", None)
                setattr(value, "Arc5", self)

    @property
    def Node(self):
        return self.__Node

    @Node.setter
    def Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Node__Node", None)
        self.__Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outgoings"):
                opp_val = getattr(old_value, "outgoings", None)
                if opp_val == self:
                    setattr(old_value, "outgoings", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outgoings"):
                opp_val = getattr(value, "outgoings", None)
                setattr(value, "outgoings", self)

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Node__source", None)
        self.__source = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Arc"):
                opp_val = getattr(old_value, "Arc", None)
                if opp_val == self:
                    setattr(old_value, "Arc", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Arc"):
                opp_val = getattr(value, "Arc", None)
                setattr(value, "Arc", self)

class Node:

    pass
class petrinet_Place(Node):

    def __init__(self, marking: int):
        self.marking = marking
        
    @property
    def marking(self) -> int:
        return self.__marking

    @marking.setter
    def marking(self, marking: int):
        self.__marking = marking

class petrinet_Transition(Node):

    def __init__(self, min_time: int, max_time: int):
        self.min_time = min_time
        self.max_time = max_time
        
    @property
    def max_time(self) -> int:
        return self.__max_time

    @max_time.setter
    def max_time(self, max_time: int):
        self.__max_time = max_time

    @property
    def min_time(self) -> int:
        return self.__min_time

    @min_time.setter
    def min_time(self, min_time: int):
        self.__min_time = min_time

class petrinet_PetriNet:

    def __init__(self, name: str, petrinet_PetriNet2: set["petrinet_Arc"] = None, petrinet_PetriNet: set["petrinet_Node"] = None):
        self.name = name
        self.petrinet_PetriNet2 = petrinet_PetriNet2 if petrinet_PetriNet2 is not None else set()
        self.petrinet_PetriNet = petrinet_PetriNet if petrinet_PetriNet is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def petrinet_PetriNet2(self):
        return self.__petrinet_PetriNet2

    @petrinet_PetriNet2.setter
    def petrinet_PetriNet2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_PetriNet__petrinet_PetriNet2", None)
        self.__petrinet_PetriNet2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "petrinet_Arc"):
                    opp_val = getattr(item, "petrinet_Arc", None)
                    
                    if opp_val == self:
                        setattr(item, "petrinet_Arc", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petrinet_Arc"):
                    opp_val = getattr(item, "petrinet_Arc", None)
                    
                    setattr(item, "petrinet_Arc", self)
                    

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
                if hasattr(item, "petrinet_Node"):
                    opp_val = getattr(item, "petrinet_Node", None)
                    
                    if opp_val == self:
                        setattr(item, "petrinet_Node", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petrinet_Node"):
                    opp_val = getattr(item, "petrinet_Node", None)
                    
                    setattr(item, "petrinet_Node", self)
                    
