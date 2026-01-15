from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class graph1_Graph:

    pass
class graph1_Edge:

    pass
class graph1_Node:

    def __init__(self, name: str, graph1_Node: "graph1_Edge" = None, graph1_Node3: "graph1_Edge" = None, graph1_Node5: "graph1_Graph" = None):
        self.name = name
        self.graph1_Node = graph1_Node
        self.graph1_Node3 = graph1_Node3
        self.graph1_Node5 = graph1_Node5
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def graph1_Node3(self):
        return self.__graph1_Node3

    @graph1_Node3.setter
    def graph1_Node3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph1_Node__graph1_Node3", None)
        self.__graph1_Node3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph1_Edge2"):
                opp_val = getattr(old_value, "graph1_Edge2", None)
                if opp_val == self:
                    setattr(old_value, "graph1_Edge2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph1_Edge2"):
                opp_val = getattr(value, "graph1_Edge2", None)
                setattr(value, "graph1_Edge2", self)

    @property
    def graph1_Node(self):
        return self.__graph1_Node

    @graph1_Node.setter
    def graph1_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph1_Node__graph1_Node", None)
        self.__graph1_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph1_Edge"):
                opp_val = getattr(old_value, "graph1_Edge", None)
                if opp_val == self:
                    setattr(old_value, "graph1_Edge", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph1_Edge"):
                opp_val = getattr(value, "graph1_Edge", None)
                setattr(value, "graph1_Edge", self)

    @property
    def graph1_Node5(self):
        return self.__graph1_Node5

    @graph1_Node5.setter
    def graph1_Node5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph1_Node__graph1_Node5", None)
        self.__graph1_Node5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph1_Graph"):
                opp_val = getattr(old_value, "graph1_Graph", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph1_Graph"):
                opp_val = getattr(value, "graph1_Graph", None)
                if opp_val is None:
                    setattr(value, "graph1_Graph", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
