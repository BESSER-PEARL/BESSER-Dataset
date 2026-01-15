from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Compass(Enum):
    NORTH = "NORTH"
    NORTH_EAST = "NORTH_EAST"
    EAST = "EAST"
    SOUTH_EAST = "SOUTH_EAST"
    SOUTH = "SOUTH"
    SOUTH_WEST = "SOUTH_WEST"
    WEST = "WEST"
    NORTH_WEST = "NORTH_WEST"
    CENTER = "CENTER"
    APPROPRIATE = "APPROPRIATE"


############################################
# Definition of Classes
############################################

class Attribute:

    pass
class dot_Identifiable(ABC):

    def __init__(self, id: str):
        self.id = id
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

class AbstractGraph:

    pass
class dot_Connectable(ABC):

    pass
class dot_StrictIdentifiable(ABC):

    def __init__(self, id: str):
        self.id = id
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

class dot_Statement(ABC):

    pass
class StrictIdentifiable:

    pass
class Connectable:

    pass
class dot_Attributable(ABC):

    def __init__(self, dot_Attributable: "dot_AttributeList" = None):
        self.dot_Attributable = dot_Attributable
        
    @property
    def dot_Attributable(self):
        return self.__dot_Attributable

    @dot_Attributable.setter
    def dot_Attributable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dot_Attributable__dot_Attributable", None)
        self.__dot_Attributable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dot_AttributeList"):
                opp_val = getattr(old_value, "dot_AttributeList", None)
                if opp_val == self:
                    setattr(old_value, "dot_AttributeList", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dot_AttributeList"):
                opp_val = getattr(value, "dot_AttributeList", None)
                setattr(value, "dot_AttributeList", self)

    def getAllALists(self) -> str:
        # TODO: Implement getAllALists method
        pass

class Statement:

    pass
class dot_Commentable(ABC):

    def __init__(self, comments: str):
        self.comments = comments
        
    @property
    def comments(self) -> str:
        return self.__comments

    @comments.setter
    def comments(self, comments: str):
        self.__comments = comments

class Attributable:

    pass
class dot_NodeStatement(Statement, Attributable, Attribute):

    pass
class Commentable:

    pass
class dot_AssignmentStatement(Statement, Commentable):

    def __init__(self, left: str, right: str):
        self.left = left
        self.right = right
        
    @property
    def left(self) -> str:
        return self.__left

    @left.setter
    def left(self, left: str):
        self.__left = left

    @property
    def right(self) -> str:
        return self.__right

    @right.setter
    def right(self, right: str):
        self.__right = right

class dot_Attribute(Commentable):

    def __init__(self, value: str, key: str, dot_Attribute: "dot_AList" = None):
        self.value = value
        self.key = key
        self.dot_Attribute = dot_Attribute
        
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
    def dot_Attribute(self):
        return self.__dot_Attribute

    @dot_Attribute.setter
    def dot_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dot_Attribute__dot_Attribute", None)
        self.__dot_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dot_AList"):
                opp_val = getattr(old_value, "dot_AList", None)
                if opp_val == self:
                    setattr(old_value, "dot_AList", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dot_AList"):
                opp_val = getattr(value, "dot_AList", None)
                setattr(value, "dot_AList", self)

class dot_Graph(Commentable, AbstractGraph):

    def __init__(self, type: str, strict: str):
        self.type = type
        self.strict = strict
        
    @property
    def strict(self) -> str:
        return self.__strict

    @strict.setter
    def strict(self, strict: str):
        self.__strict = strict

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    def getAllStatements(self) -> Statement:
        # TODO: Implement getAllStatements method
        pass

class dot_EdgeStatement(Statement, Attributable, Commentable):

    pass
class dot_Target(Commentable):

    def __init__(self, operation: str, dot_Target: "dot_EdgeStatement" = None, dot_Target25: "dot_Target" = None, dot_Target23: "dot_Target" = None, dot_Target27: "dot_Connectable" = None):
        self.operation = operation
        self.dot_Target = dot_Target
        self.dot_Target25 = dot_Target25
        self.dot_Target23 = dot_Target23
        self.dot_Target27 = dot_Target27
        
    @property
    def operation(self) -> str:
        return self.__operation

    @operation.setter
    def operation(self, operation: str):
        self.__operation = operation

    @property
    def dot_Target27(self):
        return self.__dot_Target27

    @dot_Target27.setter
    def dot_Target27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dot_Target__dot_Target27", None)
        self.__dot_Target27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dot_Connectable28"):
                opp_val = getattr(old_value, "dot_Connectable28", None)
                if opp_val == self:
                    setattr(old_value, "dot_Connectable28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dot_Connectable28"):
                opp_val = getattr(value, "dot_Connectable28", None)
                setattr(value, "dot_Connectable28", self)

    @property
    def dot_Target(self):
        return self.__dot_Target

    @dot_Target.setter
    def dot_Target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dot_Target__dot_Target", None)
        self.__dot_Target = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dot_EdgeStatement14"):
                opp_val = getattr(old_value, "dot_EdgeStatement14", None)
                if opp_val == self:
                    setattr(old_value, "dot_EdgeStatement14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dot_EdgeStatement14"):
                opp_val = getattr(value, "dot_EdgeStatement14", None)
                setattr(value, "dot_EdgeStatement14", self)

    @property
    def dot_Target25(self):
        return self.__dot_Target25

    @dot_Target25.setter
    def dot_Target25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dot_Target__dot_Target25", None)
        self.__dot_Target25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dot_Target23"):
                opp_val = getattr(old_value, "dot_Target23", None)
                if opp_val == self:
                    setattr(old_value, "dot_Target23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dot_Target23"):
                opp_val = getattr(value, "dot_Target23", None)
                setattr(value, "dot_Target23", self)

    @property
    def dot_Target23(self):
        return self.__dot_Target23

    @dot_Target23.setter
    def dot_Target23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dot_Target__dot_Target23", None)
        self.__dot_Target23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dot_Target25"):
                opp_val = getattr(old_value, "dot_Target25", None)
                if opp_val == self:
                    setattr(old_value, "dot_Target25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dot_Target25"):
                opp_val = getattr(value, "dot_Target25", None)
                setattr(value, "dot_Target25", self)

class dot_AttributeList(Commentable):

    pass
class dot_Subgraph(Commentable, Connectable, AbstractGraph):

    def __init__(self, type: str):
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class dot_AttributeStatement(Statement, Attributable, Commentable):

    def __init__(self, context: str):
        self.context = context
        
    @property
    def context(self) -> str:
        return self.__context

    @context.setter
    def context(self, context: str):
        self.__context = context

class dot_NodeID(StrictIdentifiable, Connectable, Commentable):

    pass
class dot_AList(Commentable):

    def __init__(self, dot_AList8: "dot_AttributeList" = None, dot_AList: "dot_Attribute" = None, dot_AList4: "dot_AList" = None, dot_AList2: "dot_AList" = None):
        self.dot_AList8 = dot_AList8
        self.dot_AList = dot_AList
        self.dot_AList4 = dot_AList4
        self.dot_AList2 = dot_AList2
        
    @property
    def dot_AList2(self):
        return self.__dot_AList2

    @dot_AList2.setter
    def dot_AList2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dot_AList__dot_AList2", None)
        self.__dot_AList2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dot_AList4"):
                opp_val = getattr(old_value, "dot_AList4", None)
                if opp_val == self:
                    setattr(old_value, "dot_AList4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dot_AList4"):
                opp_val = getattr(value, "dot_AList4", None)
                setattr(value, "dot_AList4", self)

    @property
    def dot_AList(self):
        return self.__dot_AList

    @dot_AList.setter
    def dot_AList(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dot_AList__dot_AList", None)
        self.__dot_AList = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dot_Attribute"):
                opp_val = getattr(old_value, "dot_Attribute", None)
                if opp_val == self:
                    setattr(old_value, "dot_Attribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dot_Attribute"):
                opp_val = getattr(value, "dot_Attribute", None)
                setattr(value, "dot_Attribute", self)

    @property
    def dot_AList8(self):
        return self.__dot_AList8

    @dot_AList8.setter
    def dot_AList8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dot_AList__dot_AList8", None)
        self.__dot_AList8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dot_AttributeList7"):
                opp_val = getattr(old_value, "dot_AttributeList7", None)
                if opp_val == self:
                    setattr(old_value, "dot_AttributeList7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dot_AttributeList7"):
                opp_val = getattr(value, "dot_AttributeList7", None)
                setattr(value, "dot_AttributeList7", self)

    @property
    def dot_AList4(self):
        return self.__dot_AList4

    @dot_AList4.setter
    def dot_AList4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dot_AList__dot_AList4", None)
        self.__dot_AList4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dot_AList2"):
                opp_val = getattr(old_value, "dot_AList2", None)
                if opp_val == self:
                    setattr(old_value, "dot_AList2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dot_AList2"):
                opp_val = getattr(value, "dot_AList2", None)
                setattr(value, "dot_AList2", self)

    def getAllAttributes(self) -> str:
        # TODO: Implement getAllAttributes method
        pass

class dot_StatementList(Commentable):

    pass
class Identifiable:

    pass
class dot_Port(Commentable, Identifiable):

    def __init__(self, compass: str, dot_Port: "dot_NodeID" = None):
        self.compass = compass
        self.dot_Port = dot_Port
        
    @property
    def compass(self) -> str:
        return self.__compass

    @compass.setter
    def compass(self, compass: str):
        self.__compass = compass

    @property
    def dot_Port(self):
        return self.__dot_Port

    @dot_Port.setter
    def dot_Port(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dot_Port__dot_Port", None)
        self.__dot_Port = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dot_NodeID17"):
                opp_val = getattr(old_value, "dot_NodeID17", None)
                if opp_val == self:
                    setattr(old_value, "dot_NodeID17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dot_NodeID17"):
                opp_val = getattr(value, "dot_NodeID17", None)
                setattr(value, "dot_NodeID17", self)

class dot_AbstractGraph(Identifiable):

    pass