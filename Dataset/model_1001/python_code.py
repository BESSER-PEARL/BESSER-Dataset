from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class EdgeType(Enum):
    directed = "directed"
    undirected = "undirected"
class AttrType(Enum):
    double = "double"
    string = "string"
    integer = "integer"
    boolean = "boolean"
class ElemType(Enum):
    edge = "edge"
    node = "node"
    graph = "graph"


############################################
# Definition of Classes
############################################

class Element:

    pass
class GraphML_Graph(Element):

    def __init__(self, edgeDefault: str, graph: set["Element"] = None, Element: "GraphML_Graph" = None):
        self.edgeDefault = edgeDefault
        self.graph = graph if graph is not None else set()
        
        pass
    @property
    def edgeDefault(self):
        return self.__edgeDefault

    @edgeDefault.setter
    def edgeDefault(self, edgeDefault: str):
        self.__edgeDefault = edgeDefault


    @property
    def graph(self):
        return self.__graph

    @graph.setter
    def graph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GraphML_Graph__graph", None)
        self.__graph = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Element"):
                    opp_val = getattr(item, "Element", None)
                    
                    if opp_val == self:
                        setattr(item, "Element", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Element"):
                    opp_val = getattr(item, "Element", None)
                    
                    setattr(item, "Element", self)
                    

class GraphML_Key(Element):

    def __init__(self, for_: str, attrName: str, type: str, defValue: str, Element: "GraphML_Graph" = None):
        self.for_ = for_
        self.attrName = attrName
        self.type = type
        self.defValue = defValue
        
        pass
    @property
    def for_(self):
        return self.__for_

    @for_.setter
    def for_(self, for_: str):
        self.__for_ = for_


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def defValue(self):
        return self.__defValue

    @defValue.setter
    def defValue(self, defValue: str):
        self.__defValue = defValue


    @property
    def attrName(self):
        return self.__attrName

    @attrName.setter
    def attrName(self, attrName: str):
        self.__attrName = attrName


class Data:

    pass
class Edge:

    pass
class GraphML_Node(Element):

    pass
class EndPoint:

    pass
class GraphML_HyperEdge(Element):

    pass
class Port:

    pass
class Node:

    pass
class GraphML_Edge(Element):

    def __init__(self, directed: str, sourceOf: "Node" = None, targetOf: "Node" = None, GraphML_Edge: "Port" = None, GraphML_Edge12: "Port" = None, Element: "GraphML_Graph" = None):
        self.directed = directed
        self.sourceOf = sourceOf
        self.targetOf = targetOf
        self.GraphML_Edge = GraphML_Edge
        self.GraphML_Edge12 = GraphML_Edge12
        
        pass
    @property
    def directed(self):
        return self.__directed

    @directed.setter
    def directed(self, directed: str):
        self.__directed = directed


    @property
    def sourceOf(self):
        return self.__sourceOf

    @sourceOf.setter
    def sourceOf(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GraphML_Edge__sourceOf", None)
        self.__sourceOf = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Node"):
                opp_val = getattr(old_value, "Node", None)
                if opp_val == self:
                    setattr(old_value, "Node", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Node"):
                opp_val = getattr(value, "Node", None)
                setattr(value, "Node", self)

    @property
    def GraphML_Edge12(self):
        return self.__GraphML_Edge12

    @GraphML_Edge12.setter
    def GraphML_Edge12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GraphML_Edge__GraphML_Edge12", None)
        self.__GraphML_Edge12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Port13"):
                opp_val = getattr(old_value, "Port13", None)
                if opp_val == self:
                    setattr(old_value, "Port13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Port13"):
                opp_val = getattr(value, "Port13", None)
                setattr(value, "Port13", self)

    @property
    def targetOf(self):
        return self.__targetOf

    @targetOf.setter
    def targetOf(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GraphML_Edge__targetOf", None)
        self.__targetOf = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Node9"):
                opp_val = getattr(old_value, "Node9", None)
                if opp_val == self:
                    setattr(old_value, "Node9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Node9"):
                opp_val = getattr(value, "Node9", None)
                setattr(value, "Node9", self)

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

class Graph:

    pass
class Key:

    pass
class LocatedElement:

    pass
class GraphML_Element(LocatedElement):

    def __init__(self, id: str, GraphML_Element: set["Data"] = None, contents: "Graph" = None):
        self.id = id
        self.GraphML_Element = GraphML_Element if GraphML_Element is not None else set()
        self.contents = contents
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def contents(self):
        return self.__contents

    @contents.setter
    def contents(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GraphML_Element__contents", None)
        self.__contents = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Graph5"):
                opp_val = getattr(old_value, "Graph5", None)
                if opp_val == self:
                    setattr(old_value, "Graph5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Graph5"):
                opp_val = getattr(value, "Graph5", None)
                setattr(value, "Graph5", self)

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
                    

class GraphML_EndPoint(LocatedElement):

    pass
class GraphML_Data(LocatedElement):

    def __init__(self, key: str, value: str):
        self.key = key
        self.value = value
        
        pass
    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key


    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class GraphML_Port(LocatedElement):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class GraphML_Root(LocatedElement):

    pass
class GraphML_LocatedElement(ABC):

    def __init__(self, location: str, commentsBefore: str, commentsAfter: str):
        self.location = location
        self.commentsBefore = commentsBefore
        self.commentsAfter = commentsAfter
        
        pass
    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location


    @property
    def commentsAfter(self):
        return self.__commentsAfter

    @commentsAfter.setter
    def commentsAfter(self, commentsAfter: str):
        self.__commentsAfter = commentsAfter


    @property
    def commentsBefore(self):
        return self.__commentsBefore

    @commentsBefore.setter
    def commentsBefore(self, commentsBefore: str):
        self.__commentsBefore = commentsBefore

