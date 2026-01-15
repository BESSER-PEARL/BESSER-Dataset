from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class graph_G:

    pass
class Node:

    pass
class graph_Boundary(Node):

    pass
class graph_Center(Node):

    pass
class graph_Node(ABC):

    def __init__(self, id: str, graph_Node: "graph_Node" = None, graph_Node0: set["graph_Node"] = None, graph_Node4: "graph_Node" = None, graph_Node2: set["graph_Node"] = None, graph_Node6: "graph_G" = None):
        self.id = id
        self.graph_Node = graph_Node
        self.graph_Node0 = graph_Node0 if graph_Node0 is not None else set()
        self.graph_Node4 = graph_Node4
        self.graph_Node2 = graph_Node2 if graph_Node2 is not None else set()
        self.graph_Node6 = graph_Node6
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def graph_Node4(self):
        return self.__graph_Node4

    @graph_Node4.setter
    def graph_Node4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Node__graph_Node4", None)
        self.__graph_Node4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_Node2"):
                opp_val = getattr(old_value, "graph_Node2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_Node2"):
                opp_val = getattr(value, "graph_Node2", None)
                if opp_val is None:
                    setattr(value, "graph_Node2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def graph_Node0(self):
        return self.__graph_Node0

    @graph_Node0.setter
    def graph_Node0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Node__graph_Node0", None)
        self.__graph_Node0 = value if value is not None else set()
        
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
    def graph_Node(self):
        return self.__graph_Node

    @graph_Node.setter
    def graph_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Node__graph_Node", None)
        self.__graph_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_Node0"):
                opp_val = getattr(old_value, "graph_Node0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_Node0"):
                opp_val = getattr(value, "graph_Node0", None)
                if opp_val is None:
                    setattr(value, "graph_Node0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def graph_Node2(self):
        return self.__graph_Node2

    @graph_Node2.setter
    def graph_Node2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Node__graph_Node2", None)
        self.__graph_Node2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "graph_Node4"):
                    opp_val = getattr(item, "graph_Node4", None)
                    
                    if opp_val == self:
                        setattr(item, "graph_Node4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graph_Node4"):
                    opp_val = getattr(item, "graph_Node4", None)
                    
                    setattr(item, "graph_Node4", self)
                    

    @property
    def graph_Node6(self):
        return self.__graph_Node6

    @graph_Node6.setter
    def graph_Node6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Node__graph_Node6", None)
        self.__graph_Node6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_G"):
                opp_val = getattr(old_value, "graph_G", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_G"):
                opp_val = getattr(value, "graph_G", None)
                if opp_val is None:
                    setattr(value, "graph_G", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
