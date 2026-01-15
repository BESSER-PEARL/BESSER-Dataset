from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class graph_Edge:

    def __init__(self, label: str, graph_Edge: "graph_GraphModel" = None, graph_Edge4: "graph_Node" = None, graph_Edge7: "graph_Node" = None):
        self.label = label
        self.graph_Edge = graph_Edge
        self.graph_Edge4 = graph_Edge4
        self.graph_Edge7 = graph_Edge7
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

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
    def graph_Edge(self):
        return self.__graph_Edge

    @graph_Edge.setter
    def graph_Edge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Edge__graph_Edge", None)
        self.__graph_Edge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_GraphModel2"):
                opp_val = getattr(old_value, "graph_GraphModel2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_GraphModel2"):
                opp_val = getattr(value, "graph_GraphModel2", None)
                if opp_val is None:
                    setattr(value, "graph_GraphModel2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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

    def __init__(self, value: str, graph_Node: "graph_GraphModel" = None, graph_Node5: "graph_Edge" = None, graph_Node8: "graph_Edge" = None):
        self.value = value
        self.graph_Node = graph_Node
        self.graph_Node5 = graph_Node5
        self.graph_Node8 = graph_Node8
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

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
            if hasattr(old_value, "graph_GraphModel"):
                opp_val = getattr(old_value, "graph_GraphModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_GraphModel"):
                opp_val = getattr(value, "graph_GraphModel", None)
                if opp_val is None:
                    setattr(value, "graph_GraphModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class graph_GraphModel:

    pass