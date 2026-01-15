from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class SettingsType(Enum):
    GRAPH = "GRAPH"
    NODE = "NODE"
    EDGE = "EDGE"


############################################
# Definition of Classes
############################################

class dot_AttributedItem(ABC):

    pass
class dot_StringToStringMapEntry:

    def __init__(self, key: str, value: str, dot_StringToStringMapEntry: "dot_AttributedItem" = None):
        self.key = key
        self.value = value
        self.dot_StringToStringMapEntry = dot_StringToStringMapEntry
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def dot_StringToStringMapEntry(self):
        return self.__dot_StringToStringMapEntry

    @dot_StringToStringMapEntry.setter
    def dot_StringToStringMapEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dot_StringToStringMapEntry__dot_StringToStringMapEntry", None)
        self.__dot_StringToStringMapEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dot_AttributedItem"):
                opp_val = getattr(old_value, "dot_AttributedItem", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dot_AttributedItem"):
                opp_val = getattr(value, "dot_AttributedItem", None)
                if opp_val is None:
                    setattr(value, "dot_AttributedItem", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dot_Identifiable(ABC):

    def __init__(self, id: str):
        self.id = id
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

class Node:

    pass
class dot_InnerNode(Node):

    pass
class dot_RecordNode(Node):

    pass
class AttributedItem:

    pass
class dot_Statement(ABC):

    pass
class Statement:

    pass
class dot_Settings(AttributedItem, Statement):

    def __init__(self, type: str):
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class dot_Assignment(Statement):

    def __init__(self, key: str, value: str):
        self.key = key
        self.value = value
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class dot_Edge(AttributedItem, Statement):

    pass
class Identifiable:

    pass
class dot_Node(AttributedItem, Identifiable, Statement):

    pass
class dot_Graph(Identifiable, Statement):

    pass