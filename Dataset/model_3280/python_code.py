from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class sm_Node:

    def __init__(self, name: str, node: "sm_Mark" = None, nodes: "sm_Graph" = None, sm_Node: "sm_Edge" = None, Node: "sm_Graph" = None, sm_Node18: "sm_Edge" = None, Node22: "sm_Mark" = None):
        self.name = name
        self.node = node
        self.nodes = nodes
        self.sm_Node = sm_Node
        self.Node = Node
        self.sm_Node18 = sm_Node18
        self.Node22 = Node22
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Node(self):
        return self.__Node

    @Node.setter
    def Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_Node__Node", None)
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

    @property
    def node(self):
        return self.__node

    @node.setter
    def node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_Node__node", None)
        self.__node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Mark13"):
                opp_val = getattr(old_value, "Mark13", None)
                if opp_val == self:
                    setattr(old_value, "Mark13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Mark13"):
                opp_val = getattr(value, "Mark13", None)
                setattr(value, "Mark13", self)

    @property
    def nodes(self):
        return self.__nodes

    @nodes.setter
    def nodes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_Node__nodes", None)
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
    def Node22(self):
        return self.__Node22

    @Node22.setter
    def Node22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_Node__Node22", None)
        self.__Node22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mark"):
                opp_val = getattr(old_value, "mark", None)
                if opp_val == self:
                    setattr(old_value, "mark", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mark"):
                opp_val = getattr(value, "mark", None)
                setattr(value, "mark", self)

    @property
    def sm_Node18(self):
        return self.__sm_Node18

    @sm_Node18.setter
    def sm_Node18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_Node__sm_Node18", None)
        self.__sm_Node18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sm_Edge17"):
                opp_val = getattr(old_value, "sm_Edge17", None)
                if opp_val == self:
                    setattr(old_value, "sm_Edge17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sm_Edge17"):
                opp_val = getattr(value, "sm_Edge17", None)
                setattr(value, "sm_Edge17", self)

    @property
    def sm_Node(self):
        return self.__sm_Node

    @sm_Node.setter
    def sm_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_Node__sm_Node", None)
        self.__sm_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sm_Edge"):
                opp_val = getattr(old_value, "sm_Edge", None)
                if opp_val == self:
                    setattr(old_value, "sm_Edge", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sm_Edge"):
                opp_val = getattr(value, "sm_Edge", None)
                setattr(value, "sm_Edge", self)

class sm_Graph:

    def __init__(self, name: str, graph9: set["sm_Edge"] = None, graph11: set["sm_Mark"] = None, Graph: "sm_Node" = None, graph: set["sm_Node"] = None, Graph20: "sm_Edge" = None, Graph24: "sm_Mark" = None):
        self.name = name
        self.graph9 = graph9 if graph9 is not None else set()
        self.graph11 = graph11 if graph11 is not None else set()
        self.Graph = Graph
        self.graph = graph if graph is not None else set()
        self.Graph20 = Graph20
        self.Graph24 = Graph24
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def graph11(self):
        return self.__graph11

    @graph11.setter
    def graph11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_Graph__graph11", None)
        self.__graph11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Mark"):
                    opp_val = getattr(item, "Mark", None)
                    
                    if opp_val == self:
                        setattr(item, "Mark", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Mark"):
                    opp_val = getattr(item, "Mark", None)
                    
                    setattr(item, "Mark", self)
                    

    @property
    def Graph20(self):
        return self.__Graph20

    @Graph20.setter
    def Graph20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_Graph__Graph20", None)
        self.__Graph20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edges"):
                opp_val = getattr(old_value, "edges", None)
                if opp_val == self:
                    setattr(old_value, "edges", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edges"):
                opp_val = getattr(value, "edges", None)
                setattr(value, "edges", self)

    @property
    def graph(self):
        return self.__graph

    @graph.setter
    def graph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_Graph__graph", None)
        self.__graph = value if value is not None else set()
        
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
    def Graph(self):
        return self.__Graph

    @Graph.setter
    def Graph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_Graph__Graph", None)
        self.__Graph = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nodes"):
                opp_val = getattr(old_value, "nodes", None)
                if opp_val == self:
                    setattr(old_value, "nodes", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nodes"):
                opp_val = getattr(value, "nodes", None)
                setattr(value, "nodes", self)

    @property
    def Graph24(self):
        return self.__Graph24

    @Graph24.setter
    def Graph24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_Graph__Graph24", None)
        self.__Graph24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "marks"):
                opp_val = getattr(old_value, "marks", None)
                if opp_val == self:
                    setattr(old_value, "marks", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "marks"):
                opp_val = getattr(value, "marks", None)
                setattr(value, "marks", self)

    @property
    def graph9(self):
        return self.__graph9

    @graph9.setter
    def graph9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_Graph__graph9", None)
        self.__graph9 = value if value is not None else set()
        
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
                    

class sm_Mark:

    def __init__(self, time: str, Mark: "sm_Graph" = None, Mark13: "sm_Node" = None, mark: "sm_Node" = None, marks: "sm_Graph" = None):
        self.time = time
        self.Mark = Mark
        self.Mark13 = Mark13
        self.mark = mark
        self.marks = marks
        
    @property
    def time(self) -> str:
        return self.__time

    @time.setter
    def time(self, time: str):
        self.__time = time

    @property
    def Mark(self):
        return self.__Mark

    @Mark.setter
    def Mark(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_Mark__Mark", None)
        self.__Mark = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph11"):
                opp_val = getattr(old_value, "graph11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph11"):
                opp_val = getattr(value, "graph11", None)
                if opp_val is None:
                    setattr(value, "graph11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_Mark__marks", None)
        self.__marks = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Graph24"):
                opp_val = getattr(old_value, "Graph24", None)
                if opp_val == self:
                    setattr(old_value, "Graph24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Graph24"):
                opp_val = getattr(value, "Graph24", None)
                setattr(value, "Graph24", self)

    @property
    def Mark13(self):
        return self.__Mark13

    @Mark13.setter
    def Mark13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_Mark__Mark13", None)
        self.__Mark13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "node"):
                opp_val = getattr(old_value, "node", None)
                if opp_val == self:
                    setattr(old_value, "node", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "node"):
                opp_val = getattr(value, "node", None)
                setattr(value, "node", self)

    @property
    def mark(self):
        return self.__mark

    @mark.setter
    def mark(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_Mark__mark", None)
        self.__mark = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Node22"):
                opp_val = getattr(old_value, "Node22", None)
                if opp_val == self:
                    setattr(old_value, "Node22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Node22"):
                opp_val = getattr(value, "Node22", None)
                setattr(value, "Node22", self)

class sm_Edge:

    def __init__(self, name: str, Edge: "sm_Graph" = None, sm_Edge: "sm_Node" = None, sm_Edge17: "sm_Node" = None, edges: "sm_Graph" = None):
        self.name = name
        self.Edge = Edge
        self.sm_Edge = sm_Edge
        self.sm_Edge17 = sm_Edge17
        self.edges = edges
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Edge(self):
        return self.__Edge

    @Edge.setter
    def Edge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_Edge__Edge", None)
        self.__Edge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph9"):
                opp_val = getattr(old_value, "graph9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph9"):
                opp_val = getattr(value, "graph9", None)
                if opp_val is None:
                    setattr(value, "graph9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sm_Edge(self):
        return self.__sm_Edge

    @sm_Edge.setter
    def sm_Edge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_Edge__sm_Edge", None)
        self.__sm_Edge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sm_Node"):
                opp_val = getattr(old_value, "sm_Node", None)
                if opp_val == self:
                    setattr(old_value, "sm_Node", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sm_Node"):
                opp_val = getattr(value, "sm_Node", None)
                setattr(value, "sm_Node", self)

    @property
    def edges(self):
        return self.__edges

    @edges.setter
    def edges(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_Edge__edges", None)
        self.__edges = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Graph20"):
                opp_val = getattr(old_value, "Graph20", None)
                if opp_val == self:
                    setattr(old_value, "Graph20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Graph20"):
                opp_val = getattr(value, "Graph20", None)
                setattr(value, "Graph20", self)

    @property
    def sm_Edge17(self):
        return self.__sm_Edge17

    @sm_Edge17.setter
    def sm_Edge17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sm_Edge__sm_Edge17", None)
        self.__sm_Edge17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sm_Node18"):
                opp_val = getattr(old_value, "sm_Node18", None)
                if opp_val == self:
                    setattr(old_value, "sm_Node18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sm_Node18"):
                opp_val = getattr(value, "sm_Node18", None)
                setattr(value, "sm_Node18", self)

class Graph:

    pass
class sm_StateMachine(Graph):

    pass
class Mark:

    pass
class sm_Observation(Mark):

    pass
class Edge:

    pass
class sm_Transition(Edge):

    pass
class Node:

    pass
class sm_State(Node):

    pass