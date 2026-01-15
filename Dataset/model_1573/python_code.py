from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class graph_Entry:

    def __init__(self, key: str, value: str, Entry: "graph_Label" = None, entries: "graph_Label" = None):
        self.key = key
        self.value = value
        self.Entry = Entry
        self.entries = entries
        
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
    def entries(self):
        return self.__entries

    @entries.setter
    def entries(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Entry__entries", None)
        self.__entries = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Label25"):
                opp_val = getattr(old_value, "Label25", None)
                if opp_val == self:
                    setattr(old_value, "Label25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Label25"):
                opp_val = getattr(value, "Label25", None)
                setattr(value, "Label25", self)

    @property
    def Entry(self):
        return self.__Entry

    @Entry.setter
    def Entry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Entry__Entry", None)
        self.__Entry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "label23"):
                opp_val = getattr(old_value, "label23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "label23"):
                opp_val = getattr(value, "label23", None)
                if opp_val is None:
                    setattr(value, "label23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class graph_Named(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class GraphElement:

    pass
class Typed:

    pass
class graph_GraphElement(Typed):

    def __init__(self, id: int):
        self.id = id
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

class graph_Vertex(GraphElement):

    pass
class graph_Edge(Typed):

    pass
class Named:

    pass
class graph_Typed(Named):

    def __init__(self, type: str):
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class graph_Label(Named):

    pass
class graph_Graph(Named):

    def __init__(self, direct: bool, graph: set["graph_Edge"] = None, graph2: set["graph_Vertex"] = None, Graph10: "graph_Edge" = None, Graph: "graph_Vertex" = None):
        self.direct = direct
        self.graph = graph if graph is not None else set()
        self.graph2 = graph2 if graph2 is not None else set()
        self.Graph10 = Graph10
        self.Graph = Graph
        
    @property
    def direct(self) -> bool:
        return self.__direct

    @direct.setter
    def direct(self, direct: bool):
        self.__direct = direct

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
    def Graph(self):
        return self.__Graph

    @Graph.setter
    def Graph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Graph__Graph", None)
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
    def graph2(self):
        return self.__graph2

    @graph2.setter
    def graph2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Graph__graph2", None)
        self.__graph2 = value if value is not None else set()
        
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
                    
