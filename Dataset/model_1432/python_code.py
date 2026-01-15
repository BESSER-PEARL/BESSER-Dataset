from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Graph_Edge:

    pass
class Graph_Node:

    def __init__(self, name: str, type: str, size: float, Graph_Node: "Graph_Edge" = None, Graph_Node3: "Graph_Edge" = None):
        self.name = name
        self.type = type
        self.size = size
        self.Graph_Node = Graph_Node
        self.Graph_Node3 = Graph_Node3
        
    @property
    def size(self) -> float:
        return self.__size

    @size.setter
    def size(self, size: float):
        self.__size = size

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
    def Graph_Node(self):
        return self.__Graph_Node

    @Graph_Node.setter
    def Graph_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Graph_Node__Graph_Node", None)
        self.__Graph_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Graph_Edge"):
                opp_val = getattr(old_value, "Graph_Edge", None)
                if opp_val == self:
                    setattr(old_value, "Graph_Edge", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Graph_Edge"):
                opp_val = getattr(value, "Graph_Edge", None)
                setattr(value, "Graph_Edge", self)

    @property
    def Graph_Node3(self):
        return self.__Graph_Node3

    @Graph_Node3.setter
    def Graph_Node3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Graph_Node__Graph_Node3", None)
        self.__Graph_Node3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Graph_Edge2"):
                opp_val = getattr(old_value, "Graph_Edge2", None)
                if opp_val == self:
                    setattr(old_value, "Graph_Edge2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Graph_Edge2"):
                opp_val = getattr(value, "Graph_Edge2", None)
                setattr(value, "Graph_Edge2", self)
