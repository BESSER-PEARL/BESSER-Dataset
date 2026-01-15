from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class EdgeViewType(Enum):
    solidline = "solidline"
    dashline = "dashline"
class Shape(Enum):
    round = "round"
    square = "square"
class Color(Enum):
    red = "red"
    blue = "blue"


############################################
# Definition of Classes
############################################

class nodesAndEdges_ShapedNode_toString:

    pass
class nodesAndEdges_Edge_toString:

    pass
class nodesAndEdges_Edge:

    def __init__(self, name: str, type: str):
        self.name = name
        self.type = type
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class nodesAndEdges_ColoredNode_toString:

    pass
class nodesAndEdges_Node_toString:

    pass
class nodesAndEdges_Node:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class Node:

    pass
class nodesAndEdges_ShapedNode(Node):

    def __init__(self, size: float, shape: str):
        self.size = size
        self.shape = shape
        
    @property
    def shape(self) -> str:
        return self.__shape

    @shape.setter
    def shape(self, shape: str):
        self.__shape = shape

    @property
    def size(self) -> float:
        return self.__size

    @size.setter
    def size(self, size: float):
        self.__size = size

    def toString(self) -> str:
        # TODO: Implement toString method
        pass

class nodesAndEdges_ColoredNode(Node):

    def __init__(self, color: str):
        self.color = color
        
    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

    def toString(self) -> str:
        # TODO: Implement toString method
        pass
