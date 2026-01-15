from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class graph_Graph:

    pass
class graph_Edge:

    pass
class graph_Node:

    def __init__(self, name: str, graph_Node: "graph_Graph" = None, graph_Node5: "graph_Edge" = None, graph_Node8: "graph_Edge" = None):
        self.name = name
        self.graph_Node = graph_Node
        self.graph_Node5 = graph_Node5
        self.graph_Node8 = graph_Node8
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
    def graph_Node5(self):
        return self.__graph_Node5

    @graph_Node5.setter
    def graph_Node5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Node__graph_Node5", None)
        self.__graph_Node5 = value
        
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
    def graph_Node8(self):
        return self.__graph_Node8

    @graph_Node8.setter
    def graph_Node8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Node__graph_Node8", None)
        self.__graph_Node8 = value
        
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
