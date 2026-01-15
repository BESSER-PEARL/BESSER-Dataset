from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class simplegraph_Edge:

    pass
class simplegraph_Node:

    def __init__(self, name: str, simplegraph_Node: "simplegraph_Graph" = None, source: set["simplegraph_Edge"] = None, target: set["simplegraph_Edge"] = None, Node: "simplegraph_Edge" = None, Node6: "simplegraph_Edge" = None):
        self.name = name
        self.simplegraph_Node = simplegraph_Node
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
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplegraph_Node__source", None)
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
    def Node(self):
        return self.__Node

    @Node.setter
    def Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplegraph_Node__Node", None)
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

    @property
    def Node6(self):
        return self.__Node6

    @Node6.setter
    def Node6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplegraph_Node__Node6", None)
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
        old_value = getattr(self, f"_simplegraph_Node__target", None)
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
    def simplegraph_Node(self):
        return self.__simplegraph_Node

    @simplegraph_Node.setter
    def simplegraph_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplegraph_Node__simplegraph_Node", None)
        self.__simplegraph_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplegraph_Graph"):
                opp_val = getattr(old_value, "simplegraph_Graph", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplegraph_Graph"):
                opp_val = getattr(value, "simplegraph_Graph", None)
                if opp_val is None:
                    setattr(value, "simplegraph_Graph", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class simplegraph_Graph:

    pass