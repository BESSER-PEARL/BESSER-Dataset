from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class LeafSize(Enum):
    small = "small"
    medium = "medium"
    big = "big"


############################################
# Definition of Classes
############################################

class TreeElement:

    pass
class MMTree_Node(TreeElement):

    pass
class MMTree_Leaf(TreeElement):

    def __init__(self, size: str):
        self.size = size
        
    @property
    def size(self) -> str:
        return self.__size

    @size.setter
    def size(self, size: str):
        self.__size = size

class MMTree_TreeElement(ABC):

    def __init__(self, name: str, MMTree_TreeElement: "MMTree_Node" = None):
        self.name = name
        self.MMTree_TreeElement = MMTree_TreeElement
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def MMTree_TreeElement(self):
        return self.__MMTree_TreeElement

    @MMTree_TreeElement.setter
    def MMTree_TreeElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MMTree_TreeElement__MMTree_TreeElement", None)
        self.__MMTree_TreeElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MMTree_Node"):
                opp_val = getattr(old_value, "MMTree_Node", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MMTree_Node"):
                opp_val = getattr(value, "MMTree_Node", None)
                if opp_val is None:
                    setattr(value, "MMTree_Node", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
