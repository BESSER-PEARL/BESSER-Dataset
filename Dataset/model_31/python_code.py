from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class ArcKind(Enum):
    normal = "normal"
    readArc = "readArc"


############################################
# Definition of Classes
############################################

class Node:

    pass
class iritptn_Transition(Node):

    def __init__(self, tMax: int, tMin: int):
        self.tMax = tMax
        self.tMin = tMin
        
    @property
    def tMax(self) -> int:
        return self.__tMax

    @tMax.setter
    def tMax(self, tMax: int):
        self.__tMax = tMax

    @property
    def tMin(self) -> int:
        return self.__tMin

    @tMin.setter
    def tMin(self, tMin: int):
        self.__tMin = tMin

class iritptn_Place(Node):

    def __init__(self, marking: int):
        self.marking = marking
        
    @property
    def marking(self) -> int:
        return self.__marking

    @marking.setter
    def marking(self, marking: int):
        self.__marking = marking

class iritptn_Arc:

    def __init__(self, weight: int, kind: str, Arc6: "iritptn_Node" = None, ingoings: "iritptn_Node" = None, arc: "iritptn_PetriNet" = None, Arc: "iritptn_PetriNet" = None, Arc4: "iritptn_Node" = None, outgoings: "iritptn_Node" = None):
        self.weight = weight
        self.kind = kind
        self.Arc6 = Arc6
        self.ingoings = ingoings
        self.arc = arc
        self.Arc = Arc
        self.Arc4 = Arc4
        self.outgoings = outgoings
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def weight(self) -> int:
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight

    @property
    def Arc6(self):
        return self.__Arc6

    @Arc6.setter
    def Arc6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iritptn_Arc__Arc6", None)
        self.__Arc6 = value
        
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
    def arc(self):
        return self.__arc

    @arc.setter
    def arc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iritptn_Arc__arc", None)
        self.__arc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNet11"):
                opp_val = getattr(old_value, "PetriNet11", None)
                if opp_val == self:
                    setattr(old_value, "PetriNet11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNet11"):
                opp_val = getattr(value, "PetriNet11", None)
                setattr(value, "PetriNet11", self)

    @property
    def outgoings(self):
        return self.__outgoings

    @outgoings.setter
    def outgoings(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iritptn_Arc__outgoings", None)
        self.__outgoings = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Node13"):
                opp_val = getattr(old_value, "Node13", None)
                if opp_val == self:
                    setattr(old_value, "Node13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Node13"):
                opp_val = getattr(value, "Node13", None)
                setattr(value, "Node13", self)

    @property
    def Arc4(self):
        return self.__Arc4

    @Arc4.setter
    def Arc4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iritptn_Arc__Arc4", None)
        self.__Arc4 = value
        
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
    def Arc(self):
        return self.__Arc

    @Arc.setter
    def Arc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iritptn_Arc__Arc", None)
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
    def ingoings(self):
        return self.__ingoings

    @ingoings.setter
    def ingoings(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iritptn_Arc__ingoings", None)
        self.__ingoings = value
        
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

class iritptn_Node:

    def __init__(self, name: str, Node: "iritptn_PetriNet" = None, source: set["iritptn_Arc"] = None, nodes: "iritptn_PetriNet" = None, Node9: "iritptn_Arc" = None, target: set["iritptn_Arc"] = None, Node13: "iritptn_Arc" = None):
        self.name = name
        self.Node = Node
        self.source = source if source is not None else set()
        self.nodes = nodes
        self.Node9 = Node9
        self.target = target if target is not None else set()
        self.Node13 = Node13
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iritptn_Node__source", None)
        self.__source = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Arc6"):
                    opp_val = getattr(item, "Arc6", None)
                    
                    if opp_val == self:
                        setattr(item, "Arc6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Arc6"):
                    opp_val = getattr(item, "Arc6", None)
                    
                    setattr(item, "Arc6", self)
                    

    @property
    def Node13(self):
        return self.__Node13

    @Node13.setter
    def Node13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iritptn_Node__Node13", None)
        self.__Node13 = value
        
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
    def Node9(self):
        return self.__Node9

    @Node9.setter
    def Node9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iritptn_Node__Node9", None)
        self.__Node9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ingoings"):
                opp_val = getattr(old_value, "ingoings", None)
                if opp_val == self:
                    setattr(old_value, "ingoings", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ingoings"):
                opp_val = getattr(value, "ingoings", None)
                setattr(value, "ingoings", self)

    @property
    def Node(self):
        return self.__Node

    @Node.setter
    def Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iritptn_Node__Node", None)
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
    def nodes(self):
        return self.__nodes

    @nodes.setter
    def nodes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iritptn_Node__nodes", None)
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
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iritptn_Node__target", None)
        self.__target = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Arc4"):
                    opp_val = getattr(item, "Arc4", None)
                    
                    if opp_val == self:
                        setattr(item, "Arc4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Arc4"):
                    opp_val = getattr(item, "Arc4", None)
                    
                    setattr(item, "Arc4", self)
                    

class iritptn_PetriNet:

    def __init__(self, name: str, net: set["iritptn_Node"] = None, PetriNet: "iritptn_Node" = None, PetriNet11: "iritptn_Arc" = None, net2: set["iritptn_Arc"] = None):
        self.name = name
        self.net = net if net is not None else set()
        self.PetriNet = PetriNet
        self.PetriNet11 = PetriNet11
        self.net2 = net2 if net2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def net(self):
        return self.__net

    @net.setter
    def net(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iritptn_PetriNet__net", None)
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
    def net2(self):
        return self.__net2

    @net2.setter
    def net2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iritptn_PetriNet__net2", None)
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
    def PetriNet11(self):
        return self.__PetriNet11

    @PetriNet11.setter
    def PetriNet11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iritptn_PetriNet__PetriNet11", None)
        self.__PetriNet11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arc"):
                opp_val = getattr(old_value, "arc", None)
                if opp_val == self:
                    setattr(old_value, "arc", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arc"):
                opp_val = getattr(value, "arc", None)
                setattr(value, "arc", self)

    @property
    def PetriNet(self):
        return self.__PetriNet

    @PetriNet.setter
    def PetriNet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iritptn_PetriNet__PetriNet", None)
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
