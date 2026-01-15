from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class GraphMM_Edge:

    pass
class GraphMM_Node:

    def __init__(self, name: str, type: str, size: float, GraphMM_Node: "GraphMM_Edge" = None, GraphMM_Node3: "GraphMM_Edge" = None):
        self.name = name
        self.type = type
        self.size = size
        self.GraphMM_Node = GraphMM_Node
        self.GraphMM_Node3 = GraphMM_Node3
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def size(self) -> float:
        return self.__size

    @size.setter
    def size(self, size: float):
        self.__size = size

    @property
    def GraphMM_Node3(self):
        return self.__GraphMM_Node3

    @GraphMM_Node3.setter
    def GraphMM_Node3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GraphMM_Node__GraphMM_Node3", None)
        self.__GraphMM_Node3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GraphMM_Edge2"):
                opp_val = getattr(old_value, "GraphMM_Edge2", None)
                if opp_val == self:
                    setattr(old_value, "GraphMM_Edge2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GraphMM_Edge2"):
                opp_val = getattr(value, "GraphMM_Edge2", None)
                setattr(value, "GraphMM_Edge2", self)

    @property
    def GraphMM_Node(self):
        return self.__GraphMM_Node

    @GraphMM_Node.setter
    def GraphMM_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GraphMM_Node__GraphMM_Node", None)
        self.__GraphMM_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GraphMM_Edge"):
                opp_val = getattr(old_value, "GraphMM_Edge", None)
                if opp_val == self:
                    setattr(old_value, "GraphMM_Edge", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GraphMM_Edge"):
                opp_val = getattr(value, "GraphMM_Edge", None)
                setattr(value, "GraphMM_Edge", self)
