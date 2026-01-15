from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class graph_Edge:

    def __init__(self, name: str, graph_Edge: "graph_Graph" = None, graph_Edge4: "graph_Node" = None, graph_Edge7: "graph_Node" = None):
        self.name = name
        self.graph_Edge = graph_Edge
        self.graph_Edge4 = graph_Edge4
        self.graph_Edge7 = graph_Edge7
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def graph_Edge(self):
        return self.__graph_Edge

    @graph_Edge.setter
    def graph_Edge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Edge__graph_Edge", None)
        self.__graph_Edge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_Graph2"):
                opp_val = getattr(old_value, "graph_Graph2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_Graph2"):
                opp_val = getattr(value, "graph_Graph2", None)
                if opp_val is None:
                    setattr(value, "graph_Graph2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def graph_Edge4(self):
        return self.__graph_Edge4

    @graph_Edge4.setter
    def graph_Edge4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Edge__graph_Edge4", None)
        self.__graph_Edge4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_Node5"):
                opp_val = getattr(old_value, "graph_Node5", None)
                if opp_val == self:
                    setattr(old_value, "graph_Node5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_Node5"):
                opp_val = getattr(value, "graph_Node5", None)
                setattr(value, "graph_Node5", self)

    @property
    def graph_Edge7(self):
        return self.__graph_Edge7

    @graph_Edge7.setter
    def graph_Edge7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Edge__graph_Edge7", None)
        self.__graph_Edge7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_Node8"):
                opp_val = getattr(old_value, "graph_Node8", None)
                if opp_val == self:
                    setattr(old_value, "graph_Node8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_Node8"):
                opp_val = getattr(value, "graph_Node8", None)
                setattr(value, "graph_Node8", self)

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

    def __init__(self, name: str, graph_Graph: set["graph_Node"] = None, graph_Graph2: set["graph_Edge"] = None):
        self.name = name
        self.graph_Graph = graph_Graph if graph_Graph is not None else set()
        self.graph_Graph2 = graph_Graph2 if graph_Graph2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def graph_Graph(self):
        return self.__graph_Graph

    @graph_Graph.setter
    def graph_Graph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Graph__graph_Graph", None)
        self.__graph_Graph = value if value is not None else set()
        
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
    def graph_Graph2(self):
        return self.__graph_Graph2

    @graph_Graph2.setter
    def graph_Graph2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Graph__graph_Graph2", None)
        self.__graph_Graph2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "graph_Edge"):
                    opp_val = getattr(item, "graph_Edge", None)
                    
                    if opp_val == self:
                        setattr(item, "graph_Edge", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graph_Edge"):
                    opp_val = getattr(item, "graph_Edge", None)
                    
                    setattr(item, "graph_Edge", self)
                    
