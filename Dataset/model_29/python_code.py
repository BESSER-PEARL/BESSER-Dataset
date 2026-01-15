from datetime import datetime, date, time
from abc import ABC, abstractmethod

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

class Node:

    pass
class petrinet_Place(Node):

    def __init__(self, tokensCount: int):
        self.tokensCount = tokensCount
        
    @property
    def tokensCount(self) -> int:
        return self.__tokensCount

    @tokensCount.setter
    def tokensCount(self, tokensCount: int):
        self.__tokensCount = tokensCount

class petrinet_Transition(Node):

    pass
class petrinet_Network:

    def __init__(self, name: str, reseau: set["petrinet_Node"] = None, reseau2: set["petrinet_Arc"] = None, Network: "petrinet_Node" = None, Network9: "petrinet_Arc" = None):
        self.name = name
        self.reseau = reseau if reseau is not None else set()
        self.reseau2 = reseau2 if reseau2 is not None else set()
        self.Network = Network
        self.Network9 = Network9
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def reseau2(self):
        return self.__reseau2

    @reseau2.setter
    def reseau2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Network__reseau2", None)
        self.__reseau2 = value if value is not None else set()
        
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
    def reseau(self):
        return self.__reseau

    @reseau.setter
    def reseau(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Network__reseau", None)
        self.__reseau = value if value is not None else set()
        
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
    def Network9(self):
        return self.__Network9

    @Network9.setter
    def Network9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Network__Network9", None)
        self.__Network9 = value
        
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
    def Network(self):
        return self.__Network

    @Network.setter
    def Network(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Network__Network", None)
        self.__Network = value
        
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

class petrinet_Arc:

    def __init__(self, readOnly: bool, kind: str, tokensCount: int, Arc: "petrinet_Network" = None, Arc5: "petrinet_Node" = None, Arc7: "petrinet_Node" = None, arcs: "petrinet_Network" = None, successors: "petrinet_Node" = None, predecessors: "petrinet_Node" = None):
        self.readOnly = readOnly
        self.kind = kind
        self.tokensCount = tokensCount
        self.Arc = Arc
        self.Arc5 = Arc5
        self.Arc7 = Arc7
        self.arcs = arcs
        self.successors = successors
        self.predecessors = predecessors
        
    @property
    def tokensCount(self) -> int:
        return self.__tokensCount

    @tokensCount.setter
    def tokensCount(self, tokensCount: int):
        self.__tokensCount = tokensCount

    @property
    def readOnly(self) -> bool:
        return self.__readOnly

    @readOnly.setter
    def readOnly(self, readOnly: bool):
        self.__readOnly = readOnly

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
        old_value = getattr(self, f"_petrinet_Arc__arcs", None)
        self.__arcs = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Network9"):
                opp_val = getattr(old_value, "Network9", None)
                if opp_val == self:
                    setattr(old_value, "Network9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Network9"):
                opp_val = getattr(value, "Network9", None)
                setattr(value, "Network9", self)

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
    def predecessors(self):
        return self.__predecessors

    @predecessors.setter
    def predecessors(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Arc__predecessors", None)
        self.__predecessors = value
        
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
    def successors(self):
        return self.__successors

    @successors.setter
    def successors(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Arc__successors", None)
        self.__successors = value
        
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
    def Arc7(self):
        return self.__Arc7

    @Arc7.setter
    def Arc7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Arc__Arc7", None)
        self.__Arc7 = value
        
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
    def Arc(self):
        return self.__Arc

    @Arc.setter
    def Arc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Arc__Arc", None)
        self.__Arc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reseau2"):
                opp_val = getattr(old_value, "reseau2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reseau2"):
                opp_val = getattr(value, "reseau2", None)
                if opp_val is None:
                    setattr(value, "reseau2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class petrinet_Node(ABC):

    def __init__(self, name: str, Node: "petrinet_Network" = None, nodes: "petrinet_Network" = None, target: set["petrinet_Arc"] = None, source: set["petrinet_Arc"] = None, Node11: "petrinet_Arc" = None, Node13: "petrinet_Arc" = None):
        self.name = name
        self.Node = Node
        self.nodes = nodes
        self.target = target if target is not None else set()
        self.source = source if source is not None else set()
        self.Node11 = Node11
        self.Node13 = Node13
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Node13(self):
        return self.__Node13

    @Node13.setter
    def Node13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Node__Node13", None)
        self.__Node13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "predecessors"):
                opp_val = getattr(old_value, "predecessors", None)
                if opp_val == self:
                    setattr(old_value, "predecessors", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "predecessors"):
                opp_val = getattr(value, "predecessors", None)
                setattr(value, "predecessors", self)

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
            if hasattr(old_value, "reseau"):
                opp_val = getattr(old_value, "reseau", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reseau"):
                opp_val = getattr(value, "reseau", None)
                if opp_val is None:
                    setattr(value, "reseau", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Node__target", None)
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
        old_value = getattr(self, f"_petrinet_Node__source", None)
        self.__source = value if value is not None else set()
        
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
        old_value = getattr(self, f"_petrinet_Node__Node11", None)
        self.__Node11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "successors"):
                opp_val = getattr(old_value, "successors", None)
                if opp_val == self:
                    setattr(old_value, "successors", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "successors"):
                opp_val = getattr(value, "successors", None)
                setattr(value, "successors", self)

    @property
    def nodes(self):
        return self.__nodes

    @nodes.setter
    def nodes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Node__nodes", None)
        self.__nodes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Network"):
                opp_val = getattr(old_value, "Network", None)
                if opp_val == self:
                    setattr(old_value, "Network", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Network"):
                opp_val = getattr(value, "Network", None)
                setattr(value, "Network", self)
