from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class graph_Edge:

    pass
class graph_Vertex:

    def __init__(self, label: str, weigth: int, graph_Vertex: "graph_Graph" = None, graph_Vertex8: "graph_Edge" = None, graph_Vertex5: "graph_Edge" = None):
        self.label = label
        self.weigth = weigth
        self.graph_Vertex = graph_Vertex
        self.graph_Vertex8 = graph_Vertex8
        self.graph_Vertex5 = graph_Vertex5
        
    @property
    def weigth(self) -> int:
        return self.__weigth

    @weigth.setter
    def weigth(self, weigth: int):
        self.__weigth = weigth

    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def graph_Vertex5(self):
        return self.__graph_Vertex5

    @graph_Vertex5.setter
    def graph_Vertex5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Vertex__graph_Vertex5", None)
        self.__graph_Vertex5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_Edge4"):
                opp_val = getattr(old_value, "graph_Edge4", None)
                if opp_val == self:
                    setattr(old_value, "graph_Edge4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_Edge4"):
                opp_val = getattr(value, "graph_Edge4", None)
                setattr(value, "graph_Edge4", self)

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
    def graph_Vertex8(self):
        return self.__graph_Vertex8

    @graph_Vertex8.setter
    def graph_Vertex8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Vertex__graph_Vertex8", None)
        self.__graph_Vertex8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_Edge7"):
                opp_val = getattr(old_value, "graph_Edge7", None)
                if opp_val == self:
                    setattr(old_value, "graph_Edge7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_Edge7"):
                opp_val = getattr(value, "graph_Edge7", None)
                setattr(value, "graph_Edge7", self)

class graph_Graph:

    pass