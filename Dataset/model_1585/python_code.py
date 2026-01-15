from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Node:

    pass
class petrinet_Transition(Node):

    pass
class petrinet_Arc:

    pass
class petrinet_Token:

    pass
class petrinet_Place(Node):

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
                    

class petrinet_Petrinet:

    def __init__(self, name: str, petrinet_Petrinet: set["petrinet_Node"] = None, petrinet_Petrinet2: set["petrinet_Arc"] = None):
        self.name = name
        self.petrinet_Petrinet = petrinet_Petrinet if petrinet_Petrinet is not None else set()
        self.petrinet_Petrinet2 = petrinet_Petrinet2 if petrinet_Petrinet2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def petrinet_Petrinet2(self):
        return self.__petrinet_Petrinet2

    @petrinet_Petrinet2.setter
    def petrinet_Petrinet2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Petrinet__petrinet_Petrinet2", None)
        self.__petrinet_Petrinet2 = value if value is not None else set()
        
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
    def petrinet_Petrinet(self):
        return self.__petrinet_Petrinet

    @petrinet_Petrinet.setter
    def petrinet_Petrinet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Petrinet__petrinet_Petrinet", None)
        self.__petrinet_Petrinet = value if value is not None else set()
        
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
                    
