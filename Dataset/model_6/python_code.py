from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class petrinet_Arc:

    pass
class petrinet_Node(ABC):

    def __init__(self, name: str, petrinet_Node: "petrinet_Petrinet" = None, target: set["petrinet_Arc"] = None, source: set["petrinet_Arc"] = None, Node: "petrinet_Arc" = None, Node8: "petrinet_Arc" = None):
        self.name = name
        self.petrinet_Node = petrinet_Node
        self.target = target if target is not None else set()
        self.source = source if source is not None else set()
        self.Node = Node
        self.Node8 = Node8
        
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
        old_value = getattr(self, f"_petrinet_Node__source", None)
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
    def petrinet_Node(self):
        return self.__petrinet_Node

    @petrinet_Node.setter
    def petrinet_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Node__petrinet_Node", None)
        self.__petrinet_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet_Petrinet"):
                opp_val = getattr(old_value, "petrinet_Petrinet", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_Petrinet"):
                opp_val = getattr(value, "petrinet_Petrinet", None)
                if opp_val is None:
                    setattr(value, "petrinet_Petrinet", set([self]))
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
    def Node(self):
        return self.__Node

    @Node.setter
    def Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Node__Node", None)
        self.__Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "incomming"):
                opp_val = getattr(old_value, "incomming", None)
                if opp_val == self:
                    setattr(old_value, "incomming", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "incomming"):
                opp_val = getattr(value, "incomming", None)
                setattr(value, "incomming", self)

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
                    

class petrinet_Petrinet:

    pass
class Node:

    pass
class petrinet_Place(Node):

    def __init__(self, tokenNb: int):
        self.tokenNb = tokenNb
        
    @property
    def tokenNb(self) -> int:
        return self.__tokenNb

    @tokenNb.setter
    def tokenNb(self, tokenNb: int):
        self.__tokenNb = tokenNb

class petrinet_Transition(Node):

    pass