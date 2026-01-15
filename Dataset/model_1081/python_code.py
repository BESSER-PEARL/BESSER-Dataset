from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class petrinet_Token:

    pass
class Node:

    pass
class petrinet_Transition(Node):

    pass
class petrinet_Place(Node):

    pass
class petrinet_Arc:

    pass
class petrinet_Node(ABC):

    def __init__(self, name: str, Node: "petrinet_Petrinet" = None, Node11: "petrinet_Arc" = None, nodes: "petrinet_Petrinet" = None, Node13: "petrinet_Arc" = None, target: set["petrinet_Arc"] = None, source: set["petrinet_Arc"] = None):
        self.name = name
        self.Node = Node
        self.Node11 = Node11
        self.nodes = nodes
        self.Node13 = Node13
        self.target = target if target is not None else set()
        self.source = source if source is not None else set()
        
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
        old_value = getattr(self, f"_petrinet_Node__Node", None)
        self.__Node = value
        
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
            if hasattr(old_value, "Petrinet"):
                opp_val = getattr(old_value, "Petrinet", None)
                if opp_val == self:
                    setattr(old_value, "Petrinet", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Petrinet"):
                opp_val = getattr(value, "Petrinet", None)
                setattr(value, "Petrinet", self)

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
    def Node11(self):
        return self.__Node11

    @Node11.setter
    def Node11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Node__Node11", None)
        self.__Node11 = value
        
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
                    

class petrinet_Petrinet:

    def __init__(self, name: str, petrinet: set["petrinet_Node"] = None, petrinet2: set["petrinet_Arc"] = None, Petrinet: "petrinet_Node" = None, Petrinet15: "petrinet_Arc" = None):
        self.name = name
        self.petrinet = petrinet if petrinet is not None else set()
        self.petrinet2 = petrinet2 if petrinet2 is not None else set()
        self.Petrinet = Petrinet
        self.Petrinet15 = Petrinet15
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
    def Petrinet15(self):
        return self.__Petrinet15

    @Petrinet15.setter
    def Petrinet15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Petrinet__Petrinet15", None)
        self.__Petrinet15 = value
        
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
    def Petrinet(self):
        return self.__Petrinet

    @Petrinet.setter
    def Petrinet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Petrinet__Petrinet", None)
        self.__Petrinet = value
        
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
    def petrinet2(self):
        return self.__petrinet2

    @petrinet2.setter
    def petrinet2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Petrinet__petrinet2", None)
        self.__petrinet2 = value if value is not None else set()
        
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
                    
