from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class graph_Pattern_Matching_Master_Project_Entry:

    def __init__(self, key: str, value: str, graph_Pattern_Matching_Master_Project_Entry: "graph_Pattern_Matching_Master_Project_Vertex" = None, graph_Pattern_Matching_Master_Project_Entry14: "graph_Pattern_Matching_Master_Project_Edge" = None):
        self.key = key
        self.value = value
        self.graph_Pattern_Matching_Master_Project_Entry = graph_Pattern_Matching_Master_Project_Entry
        self.graph_Pattern_Matching_Master_Project_Entry14 = graph_Pattern_Matching_Master_Project_Entry14
        
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

    @property
    def graph_Pattern_Matching_Master_Project_Entry(self):
        return self.__graph_Pattern_Matching_Master_Project_Entry

    @graph_Pattern_Matching_Master_Project_Entry.setter
    def graph_Pattern_Matching_Master_Project_Entry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Pattern_Matching_Master_Project_Entry__graph_Pattern_Matching_Master_Project_Entry", None)
        self.__graph_Pattern_Matching_Master_Project_Entry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_Pattern_Matching_Master_Project_Vertex"):
                opp_val = getattr(old_value, "graph_Pattern_Matching_Master_Project_Vertex", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_Pattern_Matching_Master_Project_Vertex"):
                opp_val = getattr(value, "graph_Pattern_Matching_Master_Project_Vertex", None)
                if opp_val is None:
                    setattr(value, "graph_Pattern_Matching_Master_Project_Vertex", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def graph_Pattern_Matching_Master_Project_Entry14(self):
        return self.__graph_Pattern_Matching_Master_Project_Entry14

    @graph_Pattern_Matching_Master_Project_Entry14.setter
    def graph_Pattern_Matching_Master_Project_Entry14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Pattern_Matching_Master_Project_Entry__graph_Pattern_Matching_Master_Project_Entry14", None)
        self.__graph_Pattern_Matching_Master_Project_Entry14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_Pattern_Matching_Master_Project_Edge13"):
                opp_val = getattr(old_value, "graph_Pattern_Matching_Master_Project_Edge13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_Pattern_Matching_Master_Project_Edge13"):
                opp_val = getattr(value, "graph_Pattern_Matching_Master_Project_Edge13", None)
                if opp_val is None:
                    setattr(value, "graph_Pattern_Matching_Master_Project_Edge13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class graph_Pattern_Matching_Master_Project_Vertex:

    def __init__(self, name: str, Vertex: "graph_Pattern_Matching_Master_Project_Graph" = None, vertices: "graph_Pattern_Matching_Master_Project_Graph" = None, graph_Pattern_Matching_Master_Project_Vertex: set["graph_Pattern_Matching_Master_Project_Entry"] = None, graph_Pattern_Matching_Master_Project_Vertex8: "graph_Pattern_Matching_Master_Project_Edge" = None, graph_Pattern_Matching_Master_Project_Vertex11: "graph_Pattern_Matching_Master_Project_Edge" = None):
        self.name = name
        self.Vertex = Vertex
        self.vertices = vertices
        self.graph_Pattern_Matching_Master_Project_Vertex = graph_Pattern_Matching_Master_Project_Vertex if graph_Pattern_Matching_Master_Project_Vertex is not None else set()
        self.graph_Pattern_Matching_Master_Project_Vertex8 = graph_Pattern_Matching_Master_Project_Vertex8
        self.graph_Pattern_Matching_Master_Project_Vertex11 = graph_Pattern_Matching_Master_Project_Vertex11
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def graph_Pattern_Matching_Master_Project_Vertex8(self):
        return self.__graph_Pattern_Matching_Master_Project_Vertex8

    @graph_Pattern_Matching_Master_Project_Vertex8.setter
    def graph_Pattern_Matching_Master_Project_Vertex8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Pattern_Matching_Master_Project_Vertex__graph_Pattern_Matching_Master_Project_Vertex8", None)
        self.__graph_Pattern_Matching_Master_Project_Vertex8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_Pattern_Matching_Master_Project_Edge"):
                opp_val = getattr(old_value, "graph_Pattern_Matching_Master_Project_Edge", None)
                if opp_val == self:
                    setattr(old_value, "graph_Pattern_Matching_Master_Project_Edge", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_Pattern_Matching_Master_Project_Edge"):
                opp_val = getattr(value, "graph_Pattern_Matching_Master_Project_Edge", None)
                setattr(value, "graph_Pattern_Matching_Master_Project_Edge", self)

    @property
    def graph_Pattern_Matching_Master_Project_Vertex(self):
        return self.__graph_Pattern_Matching_Master_Project_Vertex

    @graph_Pattern_Matching_Master_Project_Vertex.setter
    def graph_Pattern_Matching_Master_Project_Vertex(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Pattern_Matching_Master_Project_Vertex__graph_Pattern_Matching_Master_Project_Vertex", None)
        self.__graph_Pattern_Matching_Master_Project_Vertex = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "graph_Pattern_Matching_Master_Project_Entry"):
                    opp_val = getattr(item, "graph_Pattern_Matching_Master_Project_Entry", None)
                    
                    if opp_val == self:
                        setattr(item, "graph_Pattern_Matching_Master_Project_Entry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graph_Pattern_Matching_Master_Project_Entry"):
                    opp_val = getattr(item, "graph_Pattern_Matching_Master_Project_Entry", None)
                    
                    setattr(item, "graph_Pattern_Matching_Master_Project_Entry", self)
                    

    @property
    def Vertex(self):
        return self.__Vertex

    @Vertex.setter
    def Vertex(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Pattern_Matching_Master_Project_Vertex__Vertex", None)
        self.__Vertex = value
        
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
    def vertices(self):
        return self.__vertices

    @vertices.setter
    def vertices(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Pattern_Matching_Master_Project_Vertex__vertices", None)
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
    def graph_Pattern_Matching_Master_Project_Vertex11(self):
        return self.__graph_Pattern_Matching_Master_Project_Vertex11

    @graph_Pattern_Matching_Master_Project_Vertex11.setter
    def graph_Pattern_Matching_Master_Project_Vertex11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Pattern_Matching_Master_Project_Vertex__graph_Pattern_Matching_Master_Project_Vertex11", None)
        self.__graph_Pattern_Matching_Master_Project_Vertex11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_Pattern_Matching_Master_Project_Edge10"):
                opp_val = getattr(old_value, "graph_Pattern_Matching_Master_Project_Edge10", None)
                if opp_val == self:
                    setattr(old_value, "graph_Pattern_Matching_Master_Project_Edge10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_Pattern_Matching_Master_Project_Edge10"):
                opp_val = getattr(value, "graph_Pattern_Matching_Master_Project_Edge10", None)
                setattr(value, "graph_Pattern_Matching_Master_Project_Edge10", self)

class graph_Pattern_Matching_Master_Project_Edge:

    def __init__(self, label: str, Edge: "graph_Pattern_Matching_Master_Project_Graph" = None, edges: "graph_Pattern_Matching_Master_Project_Graph" = None, graph_Pattern_Matching_Master_Project_Edge: "graph_Pattern_Matching_Master_Project_Vertex" = None, graph_Pattern_Matching_Master_Project_Edge10: "graph_Pattern_Matching_Master_Project_Vertex" = None, graph_Pattern_Matching_Master_Project_Edge13: set["graph_Pattern_Matching_Master_Project_Entry"] = None):
        self.label = label
        self.Edge = Edge
        self.edges = edges
        self.graph_Pattern_Matching_Master_Project_Edge = graph_Pattern_Matching_Master_Project_Edge
        self.graph_Pattern_Matching_Master_Project_Edge10 = graph_Pattern_Matching_Master_Project_Edge10
        self.graph_Pattern_Matching_Master_Project_Edge13 = graph_Pattern_Matching_Master_Project_Edge13 if graph_Pattern_Matching_Master_Project_Edge13 is not None else set()
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def edges(self):
        return self.__edges

    @edges.setter
    def edges(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Pattern_Matching_Master_Project_Edge__edges", None)
        self.__edges = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Graph6"):
                opp_val = getattr(old_value, "Graph6", None)
                if opp_val == self:
                    setattr(old_value, "Graph6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Graph6"):
                opp_val = getattr(value, "Graph6", None)
                setattr(value, "Graph6", self)

    @property
    def graph_Pattern_Matching_Master_Project_Edge10(self):
        return self.__graph_Pattern_Matching_Master_Project_Edge10

    @graph_Pattern_Matching_Master_Project_Edge10.setter
    def graph_Pattern_Matching_Master_Project_Edge10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Pattern_Matching_Master_Project_Edge__graph_Pattern_Matching_Master_Project_Edge10", None)
        self.__graph_Pattern_Matching_Master_Project_Edge10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_Pattern_Matching_Master_Project_Vertex11"):
                opp_val = getattr(old_value, "graph_Pattern_Matching_Master_Project_Vertex11", None)
                if opp_val == self:
                    setattr(old_value, "graph_Pattern_Matching_Master_Project_Vertex11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_Pattern_Matching_Master_Project_Vertex11"):
                opp_val = getattr(value, "graph_Pattern_Matching_Master_Project_Vertex11", None)
                setattr(value, "graph_Pattern_Matching_Master_Project_Vertex11", self)

    @property
    def Edge(self):
        return self.__Edge

    @Edge.setter
    def Edge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Pattern_Matching_Master_Project_Edge__Edge", None)
        self.__Edge = value
        
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
    def graph_Pattern_Matching_Master_Project_Edge13(self):
        return self.__graph_Pattern_Matching_Master_Project_Edge13

    @graph_Pattern_Matching_Master_Project_Edge13.setter
    def graph_Pattern_Matching_Master_Project_Edge13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Pattern_Matching_Master_Project_Edge__graph_Pattern_Matching_Master_Project_Edge13", None)
        self.__graph_Pattern_Matching_Master_Project_Edge13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "graph_Pattern_Matching_Master_Project_Entry14"):
                    opp_val = getattr(item, "graph_Pattern_Matching_Master_Project_Entry14", None)
                    
                    if opp_val == self:
                        setattr(item, "graph_Pattern_Matching_Master_Project_Entry14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graph_Pattern_Matching_Master_Project_Entry14"):
                    opp_val = getattr(item, "graph_Pattern_Matching_Master_Project_Entry14", None)
                    
                    setattr(item, "graph_Pattern_Matching_Master_Project_Entry14", self)
                    

    @property
    def graph_Pattern_Matching_Master_Project_Edge(self):
        return self.__graph_Pattern_Matching_Master_Project_Edge

    @graph_Pattern_Matching_Master_Project_Edge.setter
    def graph_Pattern_Matching_Master_Project_Edge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Pattern_Matching_Master_Project_Edge__graph_Pattern_Matching_Master_Project_Edge", None)
        self.__graph_Pattern_Matching_Master_Project_Edge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_Pattern_Matching_Master_Project_Vertex8"):
                opp_val = getattr(old_value, "graph_Pattern_Matching_Master_Project_Vertex8", None)
                if opp_val == self:
                    setattr(old_value, "graph_Pattern_Matching_Master_Project_Vertex8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_Pattern_Matching_Master_Project_Vertex8"):
                opp_val = getattr(value, "graph_Pattern_Matching_Master_Project_Vertex8", None)
                setattr(value, "graph_Pattern_Matching_Master_Project_Vertex8", self)

class graph_Pattern_Matching_Master_Project_Graph:

    def __init__(self, name: str, direct: bool, graph: set["graph_Pattern_Matching_Master_Project_Edge"] = None, graph2: set["graph_Pattern_Matching_Master_Project_Vertex"] = None, Graph: "graph_Pattern_Matching_Master_Project_Vertex" = None, Graph6: "graph_Pattern_Matching_Master_Project_Edge" = None):
        self.name = name
        self.direct = direct
        self.graph = graph if graph is not None else set()
        self.graph2 = graph2 if graph2 is not None else set()
        self.Graph = Graph
        self.Graph6 = Graph6
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def direct(self) -> bool:
        return self.__direct

    @direct.setter
    def direct(self, direct: bool):
        self.__direct = direct

    @property
    def graph2(self):
        return self.__graph2

    @graph2.setter
    def graph2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Pattern_Matching_Master_Project_Graph__graph2", None)
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
                    

    @property
    def graph(self):
        return self.__graph

    @graph.setter
    def graph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Pattern_Matching_Master_Project_Graph__graph", None)
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
    def Graph6(self):
        return self.__Graph6

    @Graph6.setter
    def Graph6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Pattern_Matching_Master_Project_Graph__Graph6", None)
        self.__Graph6 = value
        
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
    def Graph(self):
        return self.__Graph

    @Graph.setter
    def Graph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Pattern_Matching_Master_Project_Graph__Graph", None)
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

    def isConnected(self) -> bool:
        # TODO: Implement isConnected method
        pass
