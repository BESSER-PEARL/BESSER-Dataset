from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Node:

    pass
class kiamaas_Leaf(Node):

    pass
class kiamaas_Composite(Node):

    pass
class kiamaas_Node(ABC):

    def __init__(self, height: str, depth: str, kiamaas_Node: "kiamaas_Top" = None, kiamaas_Node2: "kiamaas_Composite" = None):
        self.height = height
        self.depth = depth
        self.kiamaas_Node = kiamaas_Node
        self.kiamaas_Node2 = kiamaas_Node2
        
    @property
    def depth(self) -> str:
        return self.__depth

    @depth.setter
    def depth(self, depth: str):
        self.__depth = depth

    @property
    def height(self) -> str:
        return self.__height

    @height.setter
    def height(self, height: str):
        self.__height = height

    @property
    def kiamaas_Node2(self):
        return self.__kiamaas_Node2

    @kiamaas_Node2.setter
    def kiamaas_Node2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kiamaas_Node__kiamaas_Node2", None)
        self.__kiamaas_Node2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kiamaas_Composite"):
                opp_val = getattr(old_value, "kiamaas_Composite", None)
                if opp_val == self:
                    setattr(old_value, "kiamaas_Composite", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kiamaas_Composite"):
                opp_val = getattr(value, "kiamaas_Composite", None)
                setattr(value, "kiamaas_Composite", self)

    @property
    def kiamaas_Node(self):
        return self.__kiamaas_Node

    @kiamaas_Node.setter
    def kiamaas_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kiamaas_Node__kiamaas_Node", None)
        self.__kiamaas_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kiamaas_Top"):
                opp_val = getattr(old_value, "kiamaas_Top", None)
                if opp_val == self:
                    setattr(old_value, "kiamaas_Top", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kiamaas_Top"):
                opp_val = getattr(value, "kiamaas_Top", None)
                setattr(value, "kiamaas_Top", self)

class kiamaas_Top:

    pass