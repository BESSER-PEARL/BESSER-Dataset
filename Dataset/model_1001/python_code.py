from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ElemType(Enum):
    edge = "edge"
    node = "node"
    graph = "graph"
class AttrType(Enum):
    double = "double"
    string = "string"
    integer = "integer"
    boolean = "boolean"
class EdgeType(Enum):
    directed = "directed"
    undirected = "undirected"


############################################
# Definition of Classes
############################################

class Edge:

    pass
class EndPoint:

    pass
class Port:

    pass
class Node:

    pass
class Element:

    pass
class GraphML_HyperEdge(Element):

    pass
class GraphML_Node(Element):

    pass
class GraphML_Graph(Element):

    def __init__(self, edgeDefault: str, 06: set["Element"] = None, #7: "GraphML_Graph"):
        self.edgeDefault = edgeDefault
        self.06 = 06 if 06 is not None else set()
        
    @property
    def edgeDefault(self) -> str:
        return self.__edgeDefault

    @edgeDefault.setter
    def edgeDefault(self, edgeDefault: str):
        self.__edgeDefault = edgeDefault

    @property
    def 06(self):
        return self.__06

    @06.setter
    def 06(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GraphML_Graph__06", None)
        self.__06 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#7"):
                    opp_val = getattr(item, "#7", None)
                    
                    if opp_val == self:
                        setattr(item, "#7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#7"):
                    opp_val = getattr(item, "#7", None)
                    
                    setattr(item, "#7", self)
                    

class GraphML_Edge(Element):

    def __init__(self, directed: str, 09: "Node" = None, 012: "Node" = None, GraphML_Edge: "Port" = None, GraphML_Edge16: "Port" = None, #7: "GraphML_Graph"):
        self.directed = directed
        self.09 = 09
        self.012 = 012
        self.GraphML_Edge = GraphML_Edge
        self.GraphML_Edge16 = GraphML_Edge16
        
    @property
    def directed(self) -> str:
        return self.__directed

    @directed.setter
    def directed(self, directed: str):
        self.__directed = directed

    @property
    def GraphML_Edge16(self):
        return self.__GraphML_Edge16

    @GraphML_Edge16.setter
    def GraphML_Edge16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GraphML_Edge__GraphML_Edge16", None)
        self.__GraphML_Edge16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Port17"):
                opp_val = getattr(old_value, "Port17", None)
                if opp_val == self:
                    setattr(old_value, "Port17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Port17"):
                opp_val = getattr(value, "Port17", None)
                setattr(value, "Port17", self)

    @property
    def 012(self):
        return self.__012

    @012.setter
    def 012(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GraphML_Edge__012", None)
        self.__012 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#13"):
                opp_val = getattr(old_value, "#13", None)
                if opp_val == self:
                    setattr(old_value, "#13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#13"):
                opp_val = getattr(value, "#13", None)
                setattr(value, "#13", self)

    @property
    def 09(self):
        return self.__09

    @09.setter
    def 09(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GraphML_Edge__09", None)
        self.__09 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#10"):
                opp_val = getattr(old_value, "#10", None)
                if opp_val == self:
                    setattr(old_value, "#10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#10"):
                opp_val = getattr(value, "#10", None)
                setattr(value, "#10", self)

    @property
    def GraphML_Edge(self):
        return self.__GraphML_Edge

    @GraphML_Edge.setter
    def GraphML_Edge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GraphML_Edge__GraphML_Edge", None)
        self.__GraphML_Edge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Port"):
                opp_val = getattr(old_value, "Port", None)
                if opp_val == self:
                    setattr(old_value, "Port", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Port"):
                opp_val = getattr(value, "Port", None)
                setattr(value, "Port", self)

class GraphML_Key(Element):

    def __init__(self, for: str, attrName: str, type: str, defValue: str, #7: "GraphML_Graph"):
        self.for = for
        self.attrName = attrName
        self.type = type
        self.defValue = defValue
        
    @property
    def attrName(self) -> str:
        return self.__attrName

    @attrName.setter
    def attrName(self, attrName: str):
        self.__attrName = attrName

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def for(self) -> str:
        return self.__for

    @for.setter
    def for(self, for: str):
        self.__for = for

    @property
    def defValue(self) -> str:
        return self.__defValue

    @defValue.setter
    def defValue(self, defValue: str):
        self.__defValue = defValue

class Graph:

    pass
class Key:

    pass
class LocatedElement:

    pass
class GraphML_EndPoint(LocatedElement):

    pass
class GraphML_Port(LocatedElement):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class GraphML_Element(LocatedElement):

    def __init__(self, id: str, GraphML_Element: set["Data"] = None, 0: "Graph" = None):
        self.id = id
        self.GraphML_Element = GraphML_Element if GraphML_Element is not None else set()
        self.0 = 0
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def 0(self):
        return self.__0

    @0.setter
    def 0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GraphML_Element__0", None)
        self.__0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#"):
                opp_val = getattr(old_value, "#", None)
                if opp_val == self:
                    setattr(old_value, "#", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#"):
                opp_val = getattr(value, "#", None)
                setattr(value, "#", self)

    @property
    def GraphML_Element(self):
        return self.__GraphML_Element

    @GraphML_Element.setter
    def GraphML_Element(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GraphML_Element__GraphML_Element", None)
        self.__GraphML_Element = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Data"):
                    opp_val = getattr(item, "Data", None)
                    
                    if opp_val == self:
                        setattr(item, "Data", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Data"):
                    opp_val = getattr(item, "Data", None)
                    
                    setattr(item, "Data", self)
                    

class GraphML_Data(LocatedElement):

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

class GraphML_Root(LocatedElement):

    pass
class GraphML_LocatedElement(ABC):

    def __init__(self, location: str, commentsBefore: str, commentsAfter: str):
        self.location = location
        self.commentsBefore = commentsBefore
        self.commentsAfter = commentsAfter
        
    @property
    def commentsBefore(self) -> str:
        return self.__commentsBefore

    @commentsBefore.setter
    def commentsBefore(self, commentsBefore: str):
        self.__commentsBefore = commentsBefore

    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def commentsAfter(self) -> str:
        return self.__commentsAfter

    @commentsAfter.setter
    def commentsAfter(self, commentsAfter: str):
        self.__commentsAfter = commentsAfter

class Data:

    pass