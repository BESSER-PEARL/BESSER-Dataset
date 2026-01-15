from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class petrinet_Arc:

    pass
class petrinet_Node(ABC):

    def __init__(self, name: str, target: set["petrinet_Arc"] = None, petrinet_Node5: set["petrinet_Arc"] = None, petrinet_Node9: "petrinet_Arc" = None, Node: "petrinet_Arc" = None, petrinet_Node: "petrinet_Petrinet" = None):
        self.name = name
        self.target = target if target is not None else set()
        self.petrinet_Node5 = petrinet_Node5 if petrinet_Node5 is not None else set()
        self.petrinet_Node9 = petrinet_Node9
        self.Node = Node
        self.petrinet_Node = petrinet_Node
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def petrinet_Node5(self):
        return self.__petrinet_Node5

    @petrinet_Node5.setter
    def petrinet_Node5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Node__petrinet_Node5", None)
        self.__petrinet_Node5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "petrinet_Arc6"):
                    opp_val = getattr(item, "petrinet_Arc6", None)
                    
                    if opp_val == self:
                        setattr(item, "petrinet_Arc6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "petrinet_Arc6"):
                    opp_val = getattr(item, "petrinet_Arc6", None)
                    
                    setattr(item, "petrinet_Arc6", self)
                    

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
    def petrinet_Node9(self):
        return self.__petrinet_Node9

    @petrinet_Node9.setter
    def petrinet_Node9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_petrinet_Node__petrinet_Node9", None)
        self.__petrinet_Node9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "petrinet_Arc8"):
                opp_val = getattr(old_value, "petrinet_Arc8", None)
                if opp_val == self:
                    setattr(old_value, "petrinet_Arc8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "petrinet_Arc8"):
                opp_val = getattr(value, "petrinet_Arc8", None)
                setattr(value, "petrinet_Arc8", self)

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
            if hasattr(old_value, "in"):
                opp_val = getattr(old_value, "in", None)
                if opp_val == self:
                    setattr(old_value, "in", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "in"):
                opp_val = getattr(value, "in", None)
                setattr(value, "in", self)

class petrinet_Petrinet:

    def __init__(self, name: str, petrinet_Petrinet2: set["petrinet_Arc"] = None, petrinet_Petrinet: set["petrinet_Node"] = None):
        self.name = name
        self.petrinet_Petrinet2 = petrinet_Petrinet2 if petrinet_Petrinet2 is not None else set()
        self.petrinet_Petrinet = petrinet_Petrinet if petrinet_Petrinet is not None else set()
        
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
                    

class petrinet_Token:

    pass
class Node:

    pass
class petrinet_Place(Node):

    pass
class petrinet_Transition(Node):

    pass