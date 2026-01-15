from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Node:

    pass
class kiamaas_Num(Node):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class kiamaas_Plus(Node):

    pass
class kiamaas_Node(ABC):

    def __init__(self, height: int, deep: int, kiamaas_Node: "kiamaas_Top" = None, kiamaas_Node2: "kiamaas_Plus" = None, kiamaas_Node5: "kiamaas_Plus" = None):
        self.height = height
        self.deep = deep
        self.kiamaas_Node = kiamaas_Node
        self.kiamaas_Node2 = kiamaas_Node2
        self.kiamaas_Node5 = kiamaas_Node5
        
    @property
    def deep(self) -> int:
        return self.__deep

    @deep.setter
    def deep(self, deep: int):
        self.__deep = deep

    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, height: int):
        self.__height = height

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

    @property
    def kiamaas_Node5(self):
        return self.__kiamaas_Node5

    @kiamaas_Node5.setter
    def kiamaas_Node5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kiamaas_Node__kiamaas_Node5", None)
        self.__kiamaas_Node5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kiamaas_Plus4"):
                opp_val = getattr(old_value, "kiamaas_Plus4", None)
                if opp_val == self:
                    setattr(old_value, "kiamaas_Plus4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kiamaas_Plus4"):
                opp_val = getattr(value, "kiamaas_Plus4", None)
                setattr(value, "kiamaas_Plus4", self)

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
            if hasattr(old_value, "kiamaas_Plus"):
                opp_val = getattr(old_value, "kiamaas_Plus", None)
                if opp_val == self:
                    setattr(old_value, "kiamaas_Plus", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kiamaas_Plus"):
                opp_val = getattr(value, "kiamaas_Plus", None)
                setattr(value, "kiamaas_Plus", self)

class kiamaas_Top:

    pass