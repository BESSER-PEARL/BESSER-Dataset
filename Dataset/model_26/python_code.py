from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ArcKind(Enum):
    normal = "normal"
    read_arc = "read_arc"
    inhibitor = "inhibitor"


############################################
# Definition of Classes
############################################

class Node:

    pass
class PetriNet_Transition(Node):

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

class PetriNet_Arc:

    def __init__(self, weight: int, kind: str, Arc: "PetriNet_PetriNet" = None, Arc5: "PetriNet_Node" = None, Arc7: "PetriNet_Node" = None, incomings: "PetriNet_Node" = None, outgoings: "PetriNet_Node" = None, arcs: "PetriNet_PetriNet" = None):
        self.weight = weight
        self.kind = kind
        self.Arc = Arc
        self.Arc5 = Arc5
        self.Arc7 = Arc7
        self.incomings = incomings
        self.outgoings = outgoings
        self.arcs = arcs
        
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
    def arcs(self):
        return self.__arcs

    @arcs.setter
    def arcs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_Arc__arcs", None)
        self.__arcs = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNet13"):
                opp_val = getattr(old_value, "PetriNet13", None)
                if opp_val == self:
                    setattr(old_value, "PetriNet13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNet13"):
                opp_val = getattr(value, "PetriNet13", None)
                setattr(value, "PetriNet13", self)

    @property
    def incomings(self):
        return self.__incomings

    @incomings.setter
    def incomings(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_Arc__incomings", None)
        self.__incomings = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Node9"):
                opp_val = getattr(old_value, "Node9", None)
                if opp_val == self:
                    setattr(old_value, "Node9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Node9"):
                opp_val = getattr(value, "Node9", None)
                setattr(value, "Node9", self)

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
            if hasattr(old_value, "net2"):
                opp_val = getattr(old_value, "net2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "net2"):
                opp_val = getattr(value, "net2", None)
                if opp_val is None:
                    setattr(value, "net2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Arc7(self):
        return self.__Arc7

    @Arc7.setter
    def Arc7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_Arc__Arc7", None)
        self.__Arc7 = value
        
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

    @property
    def outgoings(self):
        return self.__outgoings

    @outgoings.setter
    def outgoings(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_Arc__outgoings", None)
        self.__outgoings = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Node11"):
                opp_val = getattr(old_value, "Node11", None)
                if opp_val == self:
                    setattr(old_value, "Node11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Node11"):
                opp_val = getattr(value, "Node11", None)
                setattr(value, "Node11", self)

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

class PetriNet_Node(ABC):

    def __init__(self, name: str, Node: "PetriNet_PetriNet" = None, nodes: "PetriNet_PetriNet" = None, source: set["PetriNet_Arc"] = None, target: set["PetriNet_Arc"] = None, Node9: "PetriNet_Arc" = None, Node11: "PetriNet_Arc" = None):
        self.name = name
        self.Node = Node
        self.nodes = nodes
        self.source = source if source is not None else set()
        self.target = target if target is not None else set()
        self.Node9 = Node9
        self.Node11 = Node11
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def nodes(self):
        return self.__nodes

    @nodes.setter
    def nodes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_Node__nodes", None)
        self.__nodes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNet"):
                opp_val = getattr(old_value, "PetriNet", None)
                if opp_val == self:
                    setattr(old_value, "PetriNet", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNet"):
                opp_val = getattr(value, "PetriNet", None)
                setattr(value, "PetriNet", self)

    @property
    def Node9(self):
        return self.__Node9

    @Node9.setter
    def Node9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_Node__Node9", None)
        self.__Node9 = value
        
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
    def Node(self):
        return self.__Node

    @Node.setter
    def Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_Node__Node", None)
        self.__Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "net"):
                opp_val = getattr(old_value, "net", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "net"):
                opp_val = getattr(value, "net", None)
                if opp_val is None:
                    setattr(value, "net", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
                if hasattr(item, "Arc7"):
                    opp_val = getattr(item, "Arc7", None)
                    
                    if opp_val == self:
                        setattr(item, "Arc7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Arc7"):
                    opp_val = getattr(item, "Arc7", None)
                    
                    setattr(item, "Arc7", self)
                    

    @property
    def Node11(self):
        return self.__Node11

    @Node11.setter
    def Node11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_Node__Node11", None)
        self.__Node11 = value
        
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

class PetriNet_PetriNet:

    def __init__(self, name: str, net: set["PetriNet_Node"] = None, net2: set["PetriNet_Arc"] = None, PetriNet: "PetriNet_Node" = None, PetriNet13: "PetriNet_Arc" = None):
        self.name = name
        self.net = net if net is not None else set()
        self.net2 = net2 if net2 is not None else set()
        self.PetriNet = PetriNet
        self.PetriNet13 = PetriNet13
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def PetriNet13(self):
        return self.__PetriNet13

    @PetriNet13.setter
    def PetriNet13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_PetriNet__PetriNet13", None)
        self.__PetriNet13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arcs"):
                opp_val = getattr(old_value, "arcs", None)
                if opp_val == self:
                    setattr(old_value, "arcs", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arcs"):
                opp_val = getattr(value, "arcs", None)
                setattr(value, "arcs", self)

    @property
    def net2(self):
        return self.__net2

    @net2.setter
    def net2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_PetriNet__net2", None)
        self.__net2 = value if value is not None else set()
        
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
    def net(self):
        return self.__net

    @net.setter
    def net(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_PetriNet__net", None)
        self.__net = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Node"):
                    opp_val = getattr(item, "Node", None)
                    
                    if opp_val == self:
                        setattr(item, "Node", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Node"):
                    opp_val = getattr(item, "Node", None)
                    
                    setattr(item, "Node", self)
                    

    @property
    def PetriNet(self):
        return self.__PetriNet

    @PetriNet.setter
    def PetriNet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNet_PetriNet__PetriNet", None)
        self.__PetriNet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nodes"):
                opp_val = getattr(old_value, "nodes", None)
                if opp_val == self:
                    setattr(old_value, "nodes", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nodes"):
                opp_val = getattr(value, "nodes", None)
                setattr(value, "nodes", self)

class PetriNet_Place(Node):

    def __init__(self, marking: int):
        self.marking = marking
        
    @property
    def marking(self) -> int:
        return self.__marking

    @marking.setter
    def marking(self, marking: int):
        self.__marking = marking
