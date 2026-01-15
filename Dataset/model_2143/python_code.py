from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class graph_Vertex:

    def __init__(self, internalId: str, graph_Vertex: "graph_Graph" = None, graph_Vertex3: "graph_Graph" = None, graph_Vertex6: "graph_Vertex" = None, graph_Vertex4: set["graph_Vertex"] = None):
        self.internalId = internalId
        self.graph_Vertex = graph_Vertex
        self.graph_Vertex3 = graph_Vertex3
        self.graph_Vertex6 = graph_Vertex6
        self.graph_Vertex4 = graph_Vertex4 if graph_Vertex4 is not None else set()
        
    @property
    def internalId(self) -> str:
        return self.__internalId

    @internalId.setter
    def internalId(self, internalId: str):
        self.__internalId = internalId

    @property
    def graph_Vertex(self):
        return self.__graph_Vertex

    @graph_Vertex.setter
    def graph_Vertex(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Vertex__graph_Vertex", None)
        self.__graph_Vertex = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_Graph"):
                opp_val = getattr(old_value, "graph_Graph", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_Graph"):
                opp_val = getattr(value, "graph_Graph", None)
                if opp_val is None:
                    setattr(value, "graph_Graph", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def graph_Vertex3(self):
        return self.__graph_Vertex3

    @graph_Vertex3.setter
    def graph_Vertex3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Vertex__graph_Vertex3", None)
        self.__graph_Vertex3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_Graph2"):
                opp_val = getattr(old_value, "graph_Graph2", None)
                if opp_val == self:
                    setattr(old_value, "graph_Graph2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_Graph2"):
                opp_val = getattr(value, "graph_Graph2", None)
                setattr(value, "graph_Graph2", self)

    @property
    def graph_Vertex6(self):
        return self.__graph_Vertex6

    @graph_Vertex6.setter
    def graph_Vertex6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Vertex__graph_Vertex6", None)
        self.__graph_Vertex6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_Vertex4"):
                opp_val = getattr(old_value, "graph_Vertex4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_Vertex4"):
                opp_val = getattr(value, "graph_Vertex4", None)
                if opp_val is None:
                    setattr(value, "graph_Vertex4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def graph_Vertex4(self):
        return self.__graph_Vertex4

    @graph_Vertex4.setter
    def graph_Vertex4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Vertex__graph_Vertex4", None)
        self.__graph_Vertex4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "graph_Vertex6"):
                    opp_val = getattr(item, "graph_Vertex6", None)
                    
                    if opp_val == self:
                        setattr(item, "graph_Vertex6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graph_Vertex6"):
                    opp_val = getattr(item, "graph_Vertex6", None)
                    
                    setattr(item, "graph_Vertex6", self)
                    

class graph_Graph:

    def __init__(self, graphName: str, graph_Graph: set["graph_Vertex"] = None, graph_Graph2: "graph_Vertex" = None):
        self.graphName = graphName
        self.graph_Graph = graph_Graph if graph_Graph is not None else set()
        self.graph_Graph2 = graph_Graph2
        
    @property
    def graphName(self) -> str:
        return self.__graphName

    @graphName.setter
    def graphName(self, graphName: str):
        self.__graphName = graphName

    @property
    def graph_Graph2(self):
        return self.__graph_Graph2

    @graph_Graph2.setter
    def graph_Graph2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Graph__graph_Graph2", None)
        self.__graph_Graph2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_Vertex3"):
                opp_val = getattr(old_value, "graph_Vertex3", None)
                if opp_val == self:
                    setattr(old_value, "graph_Vertex3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_Vertex3"):
                opp_val = getattr(value, "graph_Vertex3", None)
                setattr(value, "graph_Vertex3", self)

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
                if hasattr(item, "graph_Vertex"):
                    opp_val = getattr(item, "graph_Vertex", None)
                    
                    if opp_val == self:
                        setattr(item, "graph_Vertex", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graph_Vertex"):
                    opp_val = getattr(item, "graph_Vertex", None)
                    
                    setattr(item, "graph_Vertex", self)
                    
