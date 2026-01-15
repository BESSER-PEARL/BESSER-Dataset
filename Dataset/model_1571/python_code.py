from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Graph_Edges:

    def __init__(self, name: str, edge: set["Graph_Vertices"] = None, Graph_Edges: "Graph_Graph" = None, Edges: "Graph_Vertices" = None):
        self.name = name
        self.edge = edge if edge is not None else set()
        self.Graph_Edges = Graph_Edges
        self.Edges = Edges
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Edges(self):
        return self.__Edges

    @Edges.setter
    def Edges(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Graph_Edges__Edges", None)
        self.__Edges = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vertice"):
                opp_val = getattr(old_value, "vertice", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vertice"):
                opp_val = getattr(value, "vertice", None)
                if opp_val is None:
                    setattr(value, "vertice", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Graph_Edges(self):
        return self.__Graph_Edges

    @Graph_Edges.setter
    def Graph_Edges(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Graph_Edges__Graph_Edges", None)
        self.__Graph_Edges = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Graph_Graph2"):
                opp_val = getattr(old_value, "Graph_Graph2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Graph_Graph2"):
                opp_val = getattr(value, "Graph_Graph2", None)
                if opp_val is None:
                    setattr(value, "Graph_Graph2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def edge(self):
        return self.__edge

    @edge.setter
    def edge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Graph_Edges__edge", None)
        self.__edge = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Vertices"):
                    opp_val = getattr(item, "Vertices", None)
                    
                    if opp_val == self:
                        setattr(item, "Vertices", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Vertices"):
                    opp_val = getattr(item, "Vertices", None)
                    
                    setattr(item, "Vertices", self)
                    

class Graph_Vertices:

    def __init__(self, name: str, Graph_Vertices: "Graph_Graph" = None, vertice: set["Graph_Edges"] = None, Vertices: "Graph_Edges" = None):
        self.name = name
        self.Graph_Vertices = Graph_Vertices
        self.vertice = vertice if vertice is not None else set()
        self.Vertices = Vertices
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Vertices(self):
        return self.__Vertices

    @Vertices.setter
    def Vertices(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Graph_Vertices__Vertices", None)
        self.__Vertices = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edge"):
                opp_val = getattr(old_value, "edge", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edge"):
                opp_val = getattr(value, "edge", None)
                if opp_val is None:
                    setattr(value, "edge", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def vertice(self):
        return self.__vertice

    @vertice.setter
    def vertice(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Graph_Vertices__vertice", None)
        self.__vertice = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Edges"):
                    opp_val = getattr(item, "Edges", None)
                    
                    if opp_val == self:
                        setattr(item, "Edges", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Edges"):
                    opp_val = getattr(item, "Edges", None)
                    
                    setattr(item, "Edges", self)
                    

    @property
    def Graph_Vertices(self):
        return self.__Graph_Vertices

    @Graph_Vertices.setter
    def Graph_Vertices(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Graph_Vertices__Graph_Vertices", None)
        self.__Graph_Vertices = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Graph_Graph"):
                opp_val = getattr(old_value, "Graph_Graph", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Graph_Graph"):
                opp_val = getattr(value, "Graph_Graph", None)
                if opp_val is None:
                    setattr(value, "Graph_Graph", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Graph_Graph:

    pass