from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class graph_Edge:

    pass
class graph_Vertice:

    def __init__(self, label: str, graph_Vertice: "graph_Graph" = None, graph_Vertice5: "graph_Edge" = None, graph_Vertice8: "graph_Edge" = None):
        self.label = label
        self.graph_Vertice = graph_Vertice
        self.graph_Vertice5 = graph_Vertice5
        self.graph_Vertice8 = graph_Vertice8
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def graph_Vertice(self):
        return self.__graph_Vertice

    @graph_Vertice.setter
    def graph_Vertice(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Vertice__graph_Vertice", None)
        self.__graph_Vertice = value
        
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
    def graph_Vertice5(self):
        return self.__graph_Vertice5

    @graph_Vertice5.setter
    def graph_Vertice5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Vertice__graph_Vertice5", None)
        self.__graph_Vertice5 = value
        
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
    def graph_Vertice8(self):
        return self.__graph_Vertice8

    @graph_Vertice8.setter
    def graph_Vertice8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Vertice__graph_Vertice8", None)
        self.__graph_Vertice8 = value
        
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