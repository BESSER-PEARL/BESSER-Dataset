from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class ElementType:

    pass
class graph_ElementType(ABC):

    def __init__(self, name: str, elementType: "graph_Graph" = None, ElementType: "graph_Graph" = None):
        self.name = name
        self.elementType = elementType
        self.ElementType = ElementType
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def elementType(self):
        return self.__elementType

    @elementType.setter
    def elementType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_ElementType__elementType", None)
        self.__elementType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Graph10"):
                opp_val = getattr(old_value, "Graph10", None)
                if opp_val == self:
                    setattr(old_value, "Graph10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Graph10"):
                opp_val = getattr(value, "Graph10", None)
                setattr(value, "Graph10", self)

    @property
    def ElementType(self):
        return self.__ElementType

    @ElementType.setter
    def ElementType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_ElementType__ElementType", None)
        self.__ElementType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph13"):
                opp_val = getattr(old_value, "graph13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph13"):
                opp_val = getattr(value, "graph13", None)
                if opp_val is None:
                    setattr(value, "graph13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class graph_Graph:

    def __init__(self, name: str, Graph: "graph_Element" = None, Graph10: "graph_ElementType" = None, graph: set["graph_Element"] = None, graph13: set["graph_ElementType"] = None):
        self.name = name
        self.Graph = Graph
        self.Graph10 = Graph10
        self.graph = graph if graph is not None else set()
        self.graph13 = graph13 if graph13 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Graph10(self):
        return self.__Graph10

    @Graph10.setter
    def Graph10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Graph__Graph10", None)
        self.__Graph10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "elementType"):
                opp_val = getattr(old_value, "elementType", None)
                if opp_val == self:
                    setattr(old_value, "elementType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "elementType"):
                opp_val = getattr(value, "elementType", None)
                setattr(value, "elementType", self)

    @property
    def graph(self):
        return self.__graph

    @graph.setter
    def graph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Graph__graph", None)
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
                    

    @property
    def Graph(self):
        return self.__Graph

    @Graph.setter
    def Graph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Graph__Graph", None)
        self.__Graph = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "element"):
                opp_val = getattr(old_value, "element", None)
                if opp_val == self:
                    setattr(old_value, "element", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "element"):
                opp_val = getattr(value, "element", None)
                setattr(value, "element", self)

    @property
    def graph13(self):
        return self.__graph13

    @graph13.setter
    def graph13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Graph__graph13", None)
        self.__graph13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ElementType"):
                    opp_val = getattr(item, "ElementType", None)
                    
                    if opp_val == self:
                        setattr(item, "ElementType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ElementType"):
                    opp_val = getattr(item, "ElementType", None)
                    
                    setattr(item, "ElementType", self)
                    

class graph_Element(ABC):

    pass
class graph_EdgeType(ElementType):

    pass
class graph_NodeType(ElementType):

    pass
class Element:

    pass
class graph_Edge(Element):

    pass
class graph_Node(Element):

    def __init__(self, label: str, target: set["graph_Edge"] = None, source: set["graph_Edge"] = None, graph_Node: "graph_NodeType" = None, Node: "graph_Edge" = None, Node6: "graph_Edge" = None):
        self.label = label
        self.target = target if target is not None else set()
        self.source = source if source is not None else set()
        self.graph_Node = graph_Node
        self.Node = Node
        self.Node6 = Node6
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def graph_Node(self):
        return self.__graph_Node

    @graph_Node.setter
    def graph_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Node__graph_Node", None)
        self.__graph_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_NodeType"):
                opp_val = getattr(old_value, "graph_NodeType", None)
                if opp_val == self:
                    setattr(old_value, "graph_NodeType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_NodeType"):
                opp_val = getattr(value, "graph_NodeType", None)
                setattr(value, "graph_NodeType", self)

    @property
    def Node6(self):
        return self.__Node6

    @Node6.setter
    def Node6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Node__Node6", None)
        self.__Node6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outgoing"):
                opp_val = getattr(old_value, "outgoing", None)
                if opp_val == self:
                    setattr(old_value, "outgoing", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outgoing"):
                opp_val = getattr(value, "outgoing", None)
                setattr(value, "outgoing", self)

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Node__target", None)
        self.__target = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Edge"):
                    opp_val = getattr(item, "Edge", None)
                    
                    if opp_val == self:
                        setattr(item, "Edge", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Edge"):
                    opp_val = getattr(item, "Edge", None)
                    
                    setattr(item, "Edge", self)
                    

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Node__source", None)
        self.__source = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Edge2"):
                    opp_val = getattr(item, "Edge2", None)
                    
                    if opp_val == self:
                        setattr(item, "Edge2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Edge2"):
                    opp_val = getattr(item, "Edge2", None)
                    
                    setattr(item, "Edge2", self)
                    

    @property
    def Node(self):
        return self.__Node

    @Node.setter
    def Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Node__Node", None)
        self.__Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "incoming"):
                opp_val = getattr(old_value, "incoming", None)
                if opp_val == self:
                    setattr(old_value, "incoming", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "incoming"):
                opp_val = getattr(value, "incoming", None)
                setattr(value, "incoming", self)
