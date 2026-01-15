from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class graph_GraphElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class graph_Graph:

    def __init__(self, name: str, graph_Graph: set["graph_Node"] = None, graph_Graph2: set["graph_Edge"] = None):
        self.name = name
        self.graph_Graph = graph_Graph if graph_Graph is not None else set()
        self.graph_Graph2 = graph_Graph2 if graph_Graph2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def graph_Graph(self):
        return self.__graph_Graph

    @graph_Graph.setter
    def graph_Graph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Graph__graph_Graph", None)
        self.__graph_Graph = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "graph_Node"):
                    opp_val = getattr(item, "graph_Node", None)
                    
                    if opp_val == self:
                        setattr(item, "graph_Node", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graph_Node"):
                    opp_val = getattr(item, "graph_Node", None)
                    
                    setattr(item, "graph_Node", self)
                    

    @property
    def graph_Graph2(self):
        return self.__graph_Graph2

    @graph_Graph2.setter
    def graph_Graph2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Graph__graph_Graph2", None)
        self.__graph_Graph2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "graph_Edge"):
                    opp_val = getattr(item, "graph_Edge", None)
                    
                    if opp_val == self:
                        setattr(item, "graph_Edge", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graph_Edge"):
                    opp_val = getattr(item, "graph_Edge", None)
                    
                    setattr(item, "graph_Edge", self)
                    

class GraphElement:

    pass
class graph_Edge(GraphElement):

    pass
class graph_Node(GraphElement):

    pass