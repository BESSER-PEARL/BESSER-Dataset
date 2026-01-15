from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class PetriNets_Token:

    pass
class Arc:

    pass
class PetriNets_PTArc(Arc):

    pass
class PetriNets_TPArc(Arc):

    pass
class Node:

    pass
class PetriNets_Transition(Node):

    pass
class PetriNets_Place(Node):

    def __init__(self, tokens: int, PetriNets_Place: "PetriNets_Transition" = None, PetriNets_Place5: "PetriNets_Transition" = None, PetriNets_Place11: "PetriNets_TPArc" = None, PetriNets_Place16: "PetriNets_PTArc" = None):
        self.tokens = tokens
        self.PetriNets_Place = PetriNets_Place
        self.PetriNets_Place5 = PetriNets_Place5
        self.PetriNets_Place11 = PetriNets_Place11
        self.PetriNets_Place16 = PetriNets_Place16
        
    @property
    def tokens(self) -> int:
        return self.__tokens

    @tokens.setter
    def tokens(self, tokens: int):
        self.__tokens = tokens

    @property
    def PetriNets_Place(self):
        return self.__PetriNets_Place

    @PetriNets_Place.setter
    def PetriNets_Place(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNets_Place__PetriNets_Place", None)
        self.__PetriNets_Place = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNets_Transition"):
                opp_val = getattr(old_value, "PetriNets_Transition", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNets_Transition"):
                opp_val = getattr(value, "PetriNets_Transition", None)
                if opp_val is None:
                    setattr(value, "PetriNets_Transition", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def PetriNets_Place16(self):
        return self.__PetriNets_Place16

    @PetriNets_Place16.setter
    def PetriNets_Place16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNets_Place__PetriNets_Place16", None)
        self.__PetriNets_Place16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNets_PTArc15"):
                opp_val = getattr(old_value, "PetriNets_PTArc15", None)
                if opp_val == self:
                    setattr(old_value, "PetriNets_PTArc15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNets_PTArc15"):
                opp_val = getattr(value, "PetriNets_PTArc15", None)
                setattr(value, "PetriNets_PTArc15", self)

    @property
    def PetriNets_Place5(self):
        return self.__PetriNets_Place5

    @PetriNets_Place5.setter
    def PetriNets_Place5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNets_Place__PetriNets_Place5", None)
        self.__PetriNets_Place5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNets_Transition4"):
                opp_val = getattr(old_value, "PetriNets_Transition4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNets_Transition4"):
                opp_val = getattr(value, "PetriNets_Transition4", None)
                if opp_val is None:
                    setattr(value, "PetriNets_Transition4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def PetriNets_Place11(self):
        return self.__PetriNets_Place11

    @PetriNets_Place11.setter
    def PetriNets_Place11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNets_Place__PetriNets_Place11", None)
        self.__PetriNets_Place11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNets_TPArc10"):
                opp_val = getattr(old_value, "PetriNets_TPArc10", None)
                if opp_val == self:
                    setattr(old_value, "PetriNets_TPArc10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNets_TPArc10"):
                opp_val = getattr(value, "PetriNets_TPArc10", None)
                setattr(value, "PetriNets_TPArc10", self)

class PetriNets_Arc(ABC):

    def __init__(self, weight: int, PetriNets_Arc: "PetriNets_PetriNet" = None):
        self.weight = weight
        self.PetriNets_Arc = PetriNets_Arc
        
    @property
    def weight(self) -> int:
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight

    @property
    def PetriNets_Arc(self):
        return self.__PetriNets_Arc

    @PetriNets_Arc.setter
    def PetriNets_Arc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNets_Arc__PetriNets_Arc", None)
        self.__PetriNets_Arc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNets_PetriNet"):
                opp_val = getattr(old_value, "PetriNets_PetriNet", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNets_PetriNet"):
                opp_val = getattr(value, "PetriNets_PetriNet", None)
                if opp_val is None:
                    setattr(value, "PetriNets_PetriNet", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class PetriNets_Node(ABC):

    def __init__(self, name: str, Node: "PetriNets_PetriNet" = None, nodes: "PetriNets_PetriNet" = None):
        self.name = name
        self.Node = Node
        self.nodes = nodes
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
        old_value = getattr(self, f"_PetriNets_Node__nodes", None)
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

class PetriNets_PetriNet:

    def __init__(self, bound: int, net: set["PetriNets_Node"] = None, PetriNets_PetriNet: set["PetriNets_Arc"] = None, PetriNet: "PetriNets_Node" = None):
        self.bound = bound
        self.net = net if net is not None else set()
        self.PetriNets_PetriNet = PetriNets_PetriNet if PetriNets_PetriNet is not None else set()
        self.PetriNet = PetriNet
        
    @property
    def bound(self) -> int:
        return self.__bound

    @bound.setter
    def bound(self, bound: int):
        self.__bound = bound

    @property
    def PetriNets_PetriNet(self):
        return self.__PetriNets_PetriNet

    @PetriNets_PetriNet.setter
    def PetriNets_PetriNet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNets_PetriNet__PetriNets_PetriNet", None)
        self.__PetriNets_PetriNet = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PetriNets_Arc"):
                    opp_val = getattr(item, "PetriNets_Arc", None)
                    
                    if opp_val == self:
                        setattr(item, "PetriNets_Arc", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PetriNets_Arc"):
                    opp_val = getattr(item, "PetriNets_Arc", None)
                    
                    setattr(item, "PetriNets_Arc", self)
                    

    @property
    def net(self):
        return self.__net

    @net.setter
    def net(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PetriNets_PetriNet__net", None)
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
        old_value = getattr(self, f"_PetriNets_PetriNet__PetriNet", None)
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
