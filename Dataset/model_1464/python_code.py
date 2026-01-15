from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class graph_Node:

    def __init__(self, name: str, graph_Node: "graph_Graph" = None, Node: "graph_Node" = None, predecessors: set["graph_Node"] = None, Node5: "graph_Node" = None, successors: set["graph_Node"] = None):
        self.name = name
        self.graph_Node = graph_Node
        self.Node = Node
        self.predecessors = predecessors if predecessors is not None else set()
        self.Node5 = Node5
        self.successors = successors if successors is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def successors(self):
        return self.__successors

    @successors.setter
    def successors(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Node__successors", None)
        self.__successors = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Node5"):
                    opp_val = getattr(item, "Node5", None)
                    
                    if opp_val == self:
                        setattr(item, "Node5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Node5"):
                    opp_val = getattr(item, "Node5", None)
                    
                    setattr(item, "Node5", self)
                    

    @property
    def Node5(self):
        return self.__Node5

    @Node5.setter
    def Node5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Node__Node5", None)
        self.__Node5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "successors"):
                opp_val = getattr(old_value, "successors", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "successors"):
                opp_val = getattr(value, "successors", None)
                if opp_val is None:
                    setattr(value, "successors", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Node(self):
        return self.__Node

    @Node.setter
    def Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Node__Node", None)
        self.__Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "predecessors"):
                opp_val = getattr(old_value, "predecessors", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "predecessors"):
                opp_val = getattr(value, "predecessors", None)
                if opp_val is None:
                    setattr(value, "predecessors", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def predecessors(self):
        return self.__predecessors

    @predecessors.setter
    def predecessors(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Node__predecessors", None)
        self.__predecessors = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Node"):
                    opp_val = getattr(item, "Node", None)
                    
                    if opp_val == self:
                        setattr(item, "Node", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Node"):
                    opp_val = getattr(item, "Node", None)
                    
                    setattr(item, "Node", self)
                    

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

class graph_Graph:

    pass