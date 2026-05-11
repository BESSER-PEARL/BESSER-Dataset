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

class gv_StrictIdentifiable(ABC):

    def __init__(self, id: str):
        self.id = id
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


class gv_Statement(ABC):

    pass
class StrictIdentifiable:

    pass
class Connectable:

    pass
class gv_Commentable(ABC):

    def __init__(self, comments: str):
        self.comments = comments
        
        pass
    @property
    def comments(self):
        return self.__comments

    @comments.setter
    def comments(self, comments: str):
        self.__comments = comments


class Attribute:

    pass
class gv_Identifiable(ABC):

    def __init__(self, id: str):
        self.id = id
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


class AbstractGraph:

    pass
class Attributable:

    pass
class gv_Connectable(ABC):

    pass
class Commentable:

    pass
class gv_Target(Commentable):

    def __init__(self, operation: str, gv_Target: "gv_EdgeStatement" = None, gv_Target27: "gv_Target" = None, gv_Target25: "gv_Target" = None, gv_Target29: "gv_Connectable" = None):
        self.operation = operation
        self.gv_Target = gv_Target
        self.gv_Target27 = gv_Target27
        self.gv_Target25 = gv_Target25
        self.gv_Target29 = gv_Target29
        
        pass
    @property
    def operation(self):
        return self.__operation

    @operation.setter
    def operation(self, operation: str):
        self.__operation = operation


    @property
    def gv_Target25(self):
        return self.__gv_Target25

    @gv_Target25.setter
    def gv_Target25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gv_Target__gv_Target25", None)
        self.__gv_Target25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gv_Target27"):
                opp_val = getattr(old_value, "gv_Target27", None)
                if opp_val == self:
                    setattr(old_value, "gv_Target27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gv_Target27"):
                opp_val = getattr(value, "gv_Target27", None)
                setattr(value, "gv_Target27", self)

    @property
    def gv_Target27(self):
        return self.__gv_Target27

    @gv_Target27.setter
    def gv_Target27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gv_Target__gv_Target27", None)
        self.__gv_Target27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gv_Target25"):
                opp_val = getattr(old_value, "gv_Target25", None)
                if opp_val == self:
                    setattr(old_value, "gv_Target25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gv_Target25"):
                opp_val = getattr(value, "gv_Target25", None)
                setattr(value, "gv_Target25", self)

    @property
    def gv_Target29(self):
        return self.__gv_Target29

    @gv_Target29.setter
    def gv_Target29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gv_Target__gv_Target29", None)
        self.__gv_Target29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gv_Connectable30"):
                opp_val = getattr(old_value, "gv_Connectable30", None)
                if opp_val == self:
                    setattr(old_value, "gv_Connectable30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gv_Connectable30"):
                opp_val = getattr(value, "gv_Connectable30", None)
                setattr(value, "gv_Connectable30", self)

    @property
    def gv_Target(self):
        return self.__gv_Target

    @gv_Target.setter
    def gv_Target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gv_Target__gv_Target", None)
        self.__gv_Target = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gv_EdgeStatement16"):
                opp_val = getattr(old_value, "gv_EdgeStatement16", None)
                if opp_val == self:
                    setattr(old_value, "gv_EdgeStatement16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gv_EdgeStatement16"):
                opp_val = getattr(value, "gv_EdgeStatement16", None)
                setattr(value, "gv_EdgeStatement16", self)

class gv_Subgraph(Connectable, Commentable, AbstractGraph):

    def __init__(self, type: str):
        self.type = type
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


class gv_NodeID(StrictIdentifiable, Commentable, Connectable):

    pass
class gv_Attribute(Commentable):

    def __init__(self, key: str, value: str, gv_Attribute: "gv_AList" = None):
        self.key = key
        self.value = value
        self.gv_Attribute = gv_Attribute
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key


    @property
    def gv_Attribute(self):
        return self.__gv_Attribute

    @gv_Attribute.setter
    def gv_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gv_Attribute__gv_Attribute", None)
        self.__gv_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gv_AList"):
                opp_val = getattr(old_value, "gv_AList", None)
                if opp_val == self:
                    setattr(old_value, "gv_AList", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gv_AList"):
                opp_val = getattr(value, "gv_AList", None)
                setattr(value, "gv_AList", self)

class gv_Graph(Commentable, AbstractGraph):

    def __init__(self, type: str, strict: str):
        self.type = type
        self.strict = strict
        
        pass
    @property
    def strict(self):
        return self.__strict

    @strict.setter
    def strict(self, strict: str):
        self.__strict = strict


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


class gv_AList(Commentable):

    pass
class gv_StatementList(Commentable):

    pass
class Identifiable:

    pass
class gv_Port(Commentable, Identifiable):

    def __init__(self, compass: str, gv_Port: "gv_NodeID" = None):
        self.compass = compass
        self.gv_Port = gv_Port
        
        pass
    @property
    def compass(self):
        return self.__compass

    @compass.setter
    def compass(self, compass: str):
        self.__compass = compass


    @property
    def gv_Port(self):
        return self.__gv_Port

    @gv_Port.setter
    def gv_Port(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gv_Port__gv_Port", None)
        self.__gv_Port = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gv_NodeID19"):
                opp_val = getattr(old_value, "gv_NodeID19", None)
                if opp_val == self:
                    setattr(old_value, "gv_NodeID19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gv_NodeID19"):
                opp_val = getattr(value, "gv_NodeID19", None)
                setattr(value, "gv_NodeID19", self)

class gv_AbstractGraph(Identifiable):

    pass
class gv_AttributeList(Commentable):

    pass
class gv_Attributable(ABC):

    pass
class Statement:

    pass
class gv_NodeStatement(Statement, Attribute, Attributable):

    pass
class gv_EdgeStatement(Statement, Commentable, Attributable):

    pass
class gv_AttributeStatement(Statement, Commentable):

    def __init__(self, context: str, gv_AttributeStatement: "gv_AttributeList" = None):
        self.context = context
        self.gv_AttributeStatement = gv_AttributeStatement
        
        pass
    @property
    def context(self):
        return self.__context

    @context.setter
    def context(self, context: str):
        self.__context = context


    @property
    def gv_AttributeStatement(self):
        return self.__gv_AttributeStatement

    @gv_AttributeStatement.setter
    def gv_AttributeStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gv_AttributeStatement__gv_AttributeStatement", None)
        self.__gv_AttributeStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gv_AttributeList13"):
                opp_val = getattr(old_value, "gv_AttributeList13", None)
                if opp_val == self:
                    setattr(old_value, "gv_AttributeList13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gv_AttributeList13"):
                opp_val = getattr(value, "gv_AttributeList13", None)
                setattr(value, "gv_AttributeList13", self)

class gv_AssignmentStatement(Statement, Commentable):

    def __init__(self, left: str, right: str):
        self.left = left
        self.right = right
        
        pass
    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, right: str):
        self.__right = right


    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, left: str):
        self.__left = left

