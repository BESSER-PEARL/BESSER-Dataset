from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class graph_Edge:

    def __init__(self, name: str, Edge: "graph_Graph" = None, graph_Edge: "graph_Node" = None, graph_Edge6: "graph_Node" = None, edges: "graph_Graph" = None):
        self.name = name
        self.Edge = Edge
        self.graph_Edge = graph_Edge
        self.graph_Edge6 = graph_Edge6
        self.edges = edges
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def graph_Edge6(self):
        return self.__graph_Edge6

    @graph_Edge6.setter
    def graph_Edge6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Edge__graph_Edge6", None)
        self.__graph_Edge6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_Node7"):
                opp_val = getattr(old_value, "graph_Node7", None)
                if opp_val == self:
                    setattr(old_value, "graph_Node7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_Node7"):
                opp_val = getattr(value, "graph_Node7", None)
                setattr(value, "graph_Node7", self)

    @property
    def edges(self):
        return self.__edges

    @edges.setter
    def edges(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Edge__edges", None)
        self.__edges = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Graph9"):
                opp_val = getattr(old_value, "Graph9", None)
                if opp_val == self:
                    setattr(old_value, "Graph9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Graph9"):
                opp_val = getattr(value, "Graph9", None)
                setattr(value, "Graph9", self)

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
            if hasattr(old_value, "graph_Node"):
                opp_val = getattr(old_value, "graph_Node", None)
                if opp_val == self:
                    setattr(old_value, "graph_Node", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_Node"):
                opp_val = getattr(value, "graph_Node", None)
                setattr(value, "graph_Node", self)

    @property
    def Edge(self):
        return self.__Edge

    @Edge.setter
    def Edge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Edge__Edge", None)
        self.__Edge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph2"):
                opp_val = getattr(old_value, "graph2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph2"):
                opp_val = getattr(value, "graph2", None)
                if opp_val is None:
                    setattr(value, "graph2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class graph_Node:

    def __init__(self, name: str, Node: "graph_Graph" = None, nodes: "graph_Graph" = None, graph_Node: "graph_Edge" = None, graph_Node7: "graph_Edge" = None):
        self.name = name
        self.Node = Node
        self.nodes = nodes
        self.graph_Node = graph_Node
        self.graph_Node7 = graph_Node7
        
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
            if hasattr(old_value, "graph_Edge"):
                opp_val = getattr(old_value, "graph_Edge", None)
                if opp_val == self:
                    setattr(old_value, "graph_Edge", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_Edge"):
                opp_val = getattr(value, "graph_Edge", None)
                setattr(value, "graph_Edge", self)

    @property
    def nodes(self):
        return self.__nodes

    @nodes.setter
    def nodes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Node__nodes", None)
        self.__nodes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Graph"):
                opp_val = getattr(old_value, "Graph", None)
                if opp_val == self:
                    setattr(old_value, "Graph", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Graph"):
                opp_val = getattr(value, "Graph", None)
                setattr(value, "Graph", self)

    @property
    def graph_Node7(self):
        return self.__graph_Node7

    @graph_Node7.setter
    def graph_Node7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Node__graph_Node7", None)
        self.__graph_Node7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_Edge6"):
                opp_val = getattr(old_value, "graph_Edge6", None)
                if opp_val == self:
                    setattr(old_value, "graph_Edge6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_Edge6"):
                opp_val = getattr(value, "graph_Edge6", None)
                setattr(value, "graph_Edge6", self)

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
            if hasattr(old_value, "graph"):
                opp_val = getattr(old_value, "graph", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph"):
                opp_val = getattr(value, "graph", None)
                if opp_val is None:
                    setattr(value, "graph", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class graph_Graph:

    pass