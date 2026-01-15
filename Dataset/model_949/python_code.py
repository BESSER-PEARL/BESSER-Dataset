from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Graph_Edge:

    pass
class Graph_Node:

    def __init__(self, name: str, Graph_Node: "Graph_Graph" = None, source: set["Graph_Edge"] = None, target: set["Graph_Edge"] = None, Node: "Graph_Edge" = None, Node6: "Graph_Edge" = None):
        self.name = name
        self.Graph_Node = Graph_Node
        self.source = source if source is not None else set()
        self.target = target if target is not None else set()
        self.Node = Node
        self.Node6 = Node6
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Node6(self):
        return self.__Node6

    @Node6.setter
    def Node6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Graph_Node__Node6", None)
        self.__Node6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "incoming"):
                opp_val = getattr(old_value, "incoming", None)
                if opp_val == self:
                    setattr(old_value, "incoming", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "incoming"):
                opp_val = getattr(value, "incoming", None)
                setattr(value, "incoming", self)

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Graph_Node__target", None)
        self.__target = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Edge3"):
                    opp_val = getattr(item, "Edge3", None)
                    
                    if opp_val == self:
                        setattr(item, "Edge3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Edge3"):
                    opp_val = getattr(item, "Edge3", None)
                    
                    setattr(item, "Edge3", self)
                    

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Graph_Node__source", None)
        self.__source = value if value is not None else set()
        
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
    def Graph_Node(self):
        return self.__Graph_Node

    @Graph_Node.setter
    def Graph_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Graph_Node__Graph_Node", None)
        self.__Graph_Node = value
        
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

    @property
    def Node(self):
        return self.__Node

    @Node.setter
    def Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Graph_Node__Node", None)
        self.__Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outgoing"):
                opp_val = getattr(old_value, "outgoing", None)
                if opp_val == self:
                    setattr(old_value, "outgoing", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outgoing"):
                opp_val = getattr(value, "outgoing", None)
                setattr(value, "outgoing", self)

class Graph_Graph:

    pass