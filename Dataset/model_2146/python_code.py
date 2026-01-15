from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class DatabaseKind(Enum):
    GREMLIN = "GREMLIN"
class PrimitiveType(Enum):
    Object = "Object"
    String = "String"
    Integer = "Integer"
    Boolean = "Boolean"
    UmlToNoSQLID = "UmlToNoSQLID"


############################################
# Definition of Classes
############################################

class GraphElement:

    pass
class Element:

    pass
class graphdb_Property(Element):

    def __init__(self, key: str, type: str, properties: "graphdb_GraphElement" = None, Property: "graphdb_GraphElement" = None):
        self.key = key
        self.type = type
        self.properties = properties
        self.Property = Property
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def properties(self):
        return self.__properties

    @properties.setter
    def properties(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphdb_Property__properties", None)
        self.__properties = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GraphElement"):
                opp_val = getattr(old_value, "GraphElement", None)
                if opp_val == self:
                    setattr(old_value, "GraphElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GraphElement"):
                opp_val = getattr(value, "GraphElement", None)
                setattr(value, "GraphElement", self)

    @property
    def Property(self):
        return self.__Property

    @Property.setter
    def Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphdb_Property__Property", None)
        self.__Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owner"):
                opp_val = getattr(old_value, "owner", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner"):
                opp_val = getattr(value, "owner", None)
                if opp_val is None:
                    setattr(value, "owner", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class graphdb_GraphElement(Element):

    pass
class graphdb_Element(ABC):

    pass
class graphdb_Edge(GraphElement):

    def __init__(self, type: str, name: str, Edge: "graphdb_Graph" = None, outEdges: "graphdb_Vertex" = None, inEdges: "graphdb_Vertex" = None, edges: "graphdb_Graph" = None, Edge5: "graphdb_Vertex" = None, Edge7: "graphdb_Vertex" = None):
        self.type = type
        self.name = name
        self.Edge = Edge
        self.outEdges = outEdges
        self.inEdges = inEdges
        self.edges = edges
        self.Edge5 = Edge5
        self.Edge7 = Edge7
        
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

    @property
    def outEdges(self):
        return self.__outEdges

    @outEdges.setter
    def outEdges(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphdb_Edge__outEdges", None)
        self.__outEdges = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Vertex10"):
                opp_val = getattr(old_value, "Vertex10", None)
                if opp_val == self:
                    setattr(old_value, "Vertex10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Vertex10"):
                opp_val = getattr(value, "Vertex10", None)
                setattr(value, "Vertex10", self)

    @property
    def Edge7(self):
        return self.__Edge7

    @Edge7.setter
    def Edge7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphdb_Edge__Edge7", None)
        self.__Edge7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tail"):
                opp_val = getattr(old_value, "tail", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tail"):
                opp_val = getattr(value, "tail", None)
                if opp_val is None:
                    setattr(value, "tail", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def inEdges(self):
        return self.__inEdges

    @inEdges.setter
    def inEdges(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphdb_Edge__inEdges", None)
        self.__inEdges = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Vertex12"):
                opp_val = getattr(old_value, "Vertex12", None)
                if opp_val == self:
                    setattr(old_value, "Vertex12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Vertex12"):
                opp_val = getattr(value, "Vertex12", None)
                setattr(value, "Vertex12", self)

    @property
    def Edge(self):
        return self.__Edge

    @Edge.setter
    def Edge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphdb_Edge__Edge", None)
        self.__Edge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph2"):
                opp_val = getattr(old_value, "graph2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph2"):
                opp_val = getattr(value, "graph2", None)
                if opp_val is None:
                    setattr(value, "graph2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def edges(self):
        return self.__edges

    @edges.setter
    def edges(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphdb_Edge__edges", None)
        self.__edges = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Graph14"):
                opp_val = getattr(old_value, "Graph14", None)
                if opp_val == self:
                    setattr(old_value, "Graph14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Graph14"):
                opp_val = getattr(value, "Graph14", None)
                setattr(value, "Graph14", self)

    @property
    def Edge5(self):
        return self.__Edge5

    @Edge5.setter
    def Edge5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphdb_Edge__Edge5", None)
        self.__Edge5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "head"):
                opp_val = getattr(old_value, "head", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "head"):
                opp_val = getattr(value, "head", None)
                if opp_val is None:
                    setattr(value, "head", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class graphdb_Vertex(GraphElement):

    def __init__(self, labels: str, name: str, Vertex: "graphdb_Graph" = None, Vertex10: "graphdb_Edge" = None, Vertex12: "graphdb_Edge" = None, head: set["graphdb_Edge"] = None, tail: set["graphdb_Edge"] = None, vertices: "graphdb_Graph" = None):
        self.labels = labels
        self.name = name
        self.Vertex = Vertex
        self.Vertex10 = Vertex10
        self.Vertex12 = Vertex12
        self.head = head if head is not None else set()
        self.tail = tail if tail is not None else set()
        self.vertices = vertices
        
    @property
    def labels(self) -> str:
        return self.__labels

    @labels.setter
    def labels(self, labels: str):
        self.__labels = labels

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def tail(self):
        return self.__tail

    @tail.setter
    def tail(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphdb_Vertex__tail", None)
        self.__tail = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Edge7"):
                    opp_val = getattr(item, "Edge7", None)
                    
                    if opp_val == self:
                        setattr(item, "Edge7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Edge7"):
                    opp_val = getattr(item, "Edge7", None)
                    
                    setattr(item, "Edge7", self)
                    

    @property
    def head(self):
        return self.__head

    @head.setter
    def head(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphdb_Vertex__head", None)
        self.__head = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Edge5"):
                    opp_val = getattr(item, "Edge5", None)
                    
                    if opp_val == self:
                        setattr(item, "Edge5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Edge5"):
                    opp_val = getattr(item, "Edge5", None)
                    
                    setattr(item, "Edge5", self)
                    

    @property
    def vertices(self):
        return self.__vertices

    @vertices.setter
    def vertices(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphdb_Vertex__vertices", None)
        self.__vertices = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Graph"):
                opp_val = getattr(old_value, "Graph", None)
                if opp_val == self:
                    setattr(old_value, "Graph", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Graph"):
                opp_val = getattr(value, "Graph", None)
                setattr(value, "Graph", self)

    @property
    def Vertex(self):
        return self.__Vertex

    @Vertex.setter
    def Vertex(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphdb_Vertex__Vertex", None)
        self.__Vertex = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph"):
                opp_val = getattr(old_value, "graph", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph"):
                opp_val = getattr(value, "graph", None)
                if opp_val is None:
                    setattr(value, "graph", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Vertex12(self):
        return self.__Vertex12

    @Vertex12.setter
    def Vertex12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphdb_Vertex__Vertex12", None)
        self.__Vertex12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "inEdges"):
                opp_val = getattr(old_value, "inEdges", None)
                if opp_val == self:
                    setattr(old_value, "inEdges", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "inEdges"):
                opp_val = getattr(value, "inEdges", None)
                setattr(value, "inEdges", self)

    @property
    def Vertex10(self):
        return self.__Vertex10

    @Vertex10.setter
    def Vertex10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphdb_Vertex__Vertex10", None)
        self.__Vertex10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outEdges"):
                opp_val = getattr(old_value, "outEdges", None)
                if opp_val == self:
                    setattr(old_value, "outEdges", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outEdges"):
                opp_val = getattr(value, "outEdges", None)
                setattr(value, "outEdges", self)

class graphdb_Graph:

    def __init__(self, rawDatabase: str, graph: set["graphdb_Vertex"] = None, graph2: set["graphdb_Edge"] = None, Graph14: "graphdb_Edge" = None, Graph: "graphdb_Vertex" = None):
        self.rawDatabase = rawDatabase
        self.graph = graph if graph is not None else set()
        self.graph2 = graph2 if graph2 is not None else set()
        self.Graph14 = Graph14
        self.Graph = Graph
        
    @property
    def rawDatabase(self) -> str:
        return self.__rawDatabase

    @rawDatabase.setter
    def rawDatabase(self, rawDatabase: str):
        self.__rawDatabase = rawDatabase

    @property
    def graph2(self):
        return self.__graph2

    @graph2.setter
    def graph2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphdb_Graph__graph2", None)
        self.__graph2 = value if value is not None else set()
        
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
    def Graph14(self):
        return self.__Graph14

    @Graph14.setter
    def Graph14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphdb_Graph__Graph14", None)
        self.__Graph14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edges"):
                opp_val = getattr(old_value, "edges", None)
                if opp_val == self:
                    setattr(old_value, "edges", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edges"):
                opp_val = getattr(value, "edges", None)
                setattr(value, "edges", self)

    @property
    def graph(self):
        return self.__graph

    @graph.setter
    def graph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphdb_Graph__graph", None)
        self.__graph = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Vertex"):
                    opp_val = getattr(item, "Vertex", None)
                    
                    if opp_val == self:
                        setattr(item, "Vertex", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Vertex"):
                    opp_val = getattr(item, "Vertex", None)
                    
                    setattr(item, "Vertex", self)
                    

    @property
    def Graph(self):
        return self.__Graph

    @Graph.setter
    def Graph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphdb_Graph__Graph", None)
        self.__Graph = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vertices"):
                opp_val = getattr(old_value, "vertices", None)
                if opp_val == self:
                    setattr(old_value, "vertices", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vertices"):
                opp_val = getattr(value, "vertices", None)
                setattr(value, "vertices", self)
