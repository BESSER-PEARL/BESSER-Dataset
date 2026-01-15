from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class petrinet_Token:

    pass
class petrinet_Petrinet:

    def __init__(self, name: str, Petrinet5: "petrinet_Node" = None, petrinet: set["petrinet_Node"] = None, petrinet12: set["petrinet_Arc"] = None, Petrinet: "petrinet_Arc" = None):
        self.name = name
        self.Petrinet5 = Petrinet5
        self.petrinet = petrinet if petrinet is not None else set()
        self.petrinet12 = petrinet12 if petrinet12 is not None else set()
        self.Petrinet = Petrinet
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Petrinet5(self):
        return self.__Petrinet5

    @Petrinet5.setter
    def Petrinet5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Petrinet__Petrinet5", None)
        self.__Petrinet5 = value
        
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

    @property
    def petrinet12(self):
        return self.__petrinet12

    @petrinet12.setter
    def petrinet12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Petrinet__petrinet12", None)
        self.__petrinet12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Arc13"):
                    opp_val = getattr(item, "Arc13", None)
                    
                    if opp_val == self:
                        setattr(item, "Arc13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Arc13"):
                    opp_val = getattr(item, "Arc13", None)
                    
                    setattr(item, "Arc13", self)
                    

    @property
    def Petrinet(self):
        return self.__Petrinet

    @Petrinet.setter
    def Petrinet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Petrinet__Petrinet", None)
        self.__Petrinet = value
        
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
    def petrinet(self):
        return self.__petrinet

    @petrinet.setter
    def petrinet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Petrinet__petrinet", None)
        self.__petrinet = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Node10"):
                    opp_val = getattr(item, "Node10", None)
                    
                    if opp_val == self:
                        setattr(item, "Node10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Node10"):
                    opp_val = getattr(item, "Node10", None)
                    
                    setattr(item, "Node10", self)
                    

class petrinet_Node(ABC):

    def __init__(self, name: str, nodes: "petrinet_Petrinet" = None, target: set["petrinet_Arc"] = None, source: set["petrinet_Arc"] = None, Node10: "petrinet_Petrinet" = None, Node: "petrinet_Arc" = None, Node2: "petrinet_Arc" = None):
        self.name = name
        self.nodes = nodes
        self.target = target if target is not None else set()
        self.source = source if source is not None else set()
        self.Node10 = Node10
        self.Node = Node
        self.Node2 = Node2
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Node10(self):
        return self.__Node10

    @Node10.setter
    def Node10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Node__Node10", None)
        self.__Node10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet"):
                opp_val = getattr(old_value, "petrinet", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet"):
                opp_val = getattr(value, "petrinet", None)
                if opp_val is None:
                    setattr(value, "petrinet", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "Petrinet5"):
                opp_val = getattr(old_value, "Petrinet5", None)
                if opp_val == self:
                    setattr(old_value, "Petrinet5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Petrinet5"):
                opp_val = getattr(value, "Petrinet5", None)
                setattr(value, "Petrinet5", self)

    @property
    def Node2(self):
        return self.__Node2

    @Node2.setter
    def Node2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Node__Node2", None)
        self.__Node2 = value
        
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
        old_value = getattr(self, f"_petrinet_Node__Node", None)
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
        old_value = getattr(self, f"_petrinet_Node__source", None)
        self.__source = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Arc8"):
                    opp_val = getattr(item, "Arc8", None)
                    
                    if opp_val == self:
                        setattr(item, "Arc8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Arc8"):
                    opp_val = getattr(item, "Arc8", None)
                    
                    setattr(item, "Arc8", self)
                    

class petrinet_Arc:

    pass
class Node:

    pass
class petrinet_Transition(Node):

    pass
class petrinet_Place(Node):

    pass