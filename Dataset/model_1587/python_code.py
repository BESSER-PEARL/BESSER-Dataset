from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Node:

    pass
class petrinet_Transition(Node):

    pass
class petrinet_petrinet:

    def __init__(self, nume: str, petrinet: set["petrinet_Arc"] = None, petrinet2: set["petrinet_Node"] = None, petrinet9: "petrinet_Arc" = None, petrinet15: "petrinet_Node" = None):
        self.nume = nume
        self.petrinet = petrinet if petrinet is not None else set()
        self.petrinet2 = petrinet2 if petrinet2 is not None else set()
        self.petrinet9 = petrinet9
        self.petrinet15 = petrinet15
        
    @property
    def nume(self) -> str:
        return self.__nume

    @nume.setter
    def nume(self, nume: str):
        self.__nume = nume

    @property
    def petrinet9(self):
        return self.__petrinet9

    @petrinet9.setter
    def petrinet9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_petrinet__petrinet9", None)
        self.__petrinet9 = value
        
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
    def petrinet2(self):
        return self.__petrinet2

    @petrinet2.setter
    def petrinet2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_petrinet__petrinet2", None)
        self.__petrinet2 = value if value is not None else set()
        
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
    def petrinet(self):
        return self.__petrinet

    @petrinet.setter
    def petrinet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_petrinet__petrinet", None)
        self.__petrinet = value if value is not None else set()
        
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
    def petrinet15(self):
        return self.__petrinet15

    @petrinet15.setter
    def petrinet15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_petrinet__petrinet15", None)
        self.__petrinet15 = value
        
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

class petrinet_Place(Node):

    pass
class petrinet_Token:

    pass
class petrinet_Node(ABC):

    def __init__(self, name: str, Node: "petrinet_petrinet" = None, Node5: "petrinet_Arc" = None, Node7: "petrinet_Arc" = None, target: set["petrinet_Arc"] = None, nodes: "petrinet_petrinet" = None, source: set["petrinet_Arc"] = None):
        self.name = name
        self.Node = Node
        self.Node5 = Node5
        self.Node7 = Node7
        self.target = target if target is not None else set()
        self.nodes = nodes
        self.source = source if source is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Node7(self):
        return self.__Node7

    @Node7.setter
    def Node7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Node__Node7", None)
        self.__Node7 = value
        
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
                if hasattr(item, "Arc11"):
                    opp_val = getattr(item, "Arc11", None)
                    
                    if opp_val == self:
                        setattr(item, "Arc11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Arc11"):
                    opp_val = getattr(item, "Arc11", None)
                    
                    setattr(item, "Arc11", self)
                    

    @property
    def Node5(self):
        return self.__Node5

    @Node5.setter
    def Node5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Node__Node5", None)
        self.__Node5 = value
        
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
    def Node(self):
        return self.__Node

    @Node.setter
    def Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Node__Node", None)
        self.__Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet2"):
                opp_val = getattr(old_value, "petrinet2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet2"):
                opp_val = getattr(value, "petrinet2", None)
                if opp_val is None:
                    setattr(value, "petrinet2", set([self]))
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
            if hasattr(old_value, "petrinet15"):
                opp_val = getattr(old_value, "petrinet15", None)
                if opp_val == self:
                    setattr(old_value, "petrinet15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet15"):
                opp_val = getattr(value, "petrinet15", None)
                setattr(value, "petrinet15", self)

class petrinet_Arc:

    pass