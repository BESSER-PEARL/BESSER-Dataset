from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class graph_Mark:

    def __init__(self, time: str, Mark: "graph_Graph" = None, Mark6: "graph_Node" = None, mark: "graph_Node" = None, marks: "graph_Graph" = None):
        self.time = time
        self.Mark = Mark
        self.Mark6 = Mark6
        self.mark = mark
        self.marks = marks
        
    @property
    def time(self) -> str:
        return self.__time

    @time.setter
    def time(self, time: str):
        self.__time = time

    @property
    def Mark6(self):
        return self.__Mark6

    @Mark6.setter
    def Mark6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Mark__Mark6", None)
        self.__Mark6 = value
        
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
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Mark__marks", None)
        self.__marks = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Graph17"):
                opp_val = getattr(old_value, "Graph17", None)
                if opp_val == self:
                    setattr(old_value, "Graph17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Graph17"):
                opp_val = getattr(value, "Graph17", None)
                setattr(value, "Graph17", self)

    @property
    def Mark(self):
        return self.__Mark

    @Mark.setter
    def Mark(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Mark__Mark", None)
        self.__Mark = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph4"):
                opp_val = getattr(old_value, "graph4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph4"):
                opp_val = getattr(value, "graph4", None)
                if opp_val is None:
                    setattr(value, "graph4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mark(self):
        return self.__mark

    @mark.setter
    def mark(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Mark__mark", None)
        self.__mark = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Node15"):
                opp_val = getattr(old_value, "Node15", None)
                if opp_val == self:
                    setattr(old_value, "Node15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Node15"):
                opp_val = getattr(value, "Node15", None)
                setattr(value, "Node15", self)

class graph_Edge:

    def __init__(self, name: str, Edge: "graph_Graph" = None, graph_Edge: "graph_Node" = None, graph_Edge10: "graph_Node" = None, edges: "graph_Graph" = None):
        self.name = name
        self.Edge = Edge
        self.graph_Edge = graph_Edge
        self.graph_Edge10 = graph_Edge10
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
            if hasattr(old_value, "Graph13"):
                opp_val = getattr(old_value, "Graph13", None)
                if opp_val == self:
                    setattr(old_value, "Graph13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Graph13"):
                opp_val = getattr(value, "Graph13", None)
                setattr(value, "Graph13", self)

    @property
    def graph_Edge10(self):
        return self.__graph_Edge10

    @graph_Edge10.setter
    def graph_Edge10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Edge__graph_Edge10", None)
        self.__graph_Edge10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_Node11"):
                opp_val = getattr(old_value, "graph_Node11", None)
                if opp_val == self:
                    setattr(old_value, "graph_Node11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_Node11"):
                opp_val = getattr(value, "graph_Node11", None)
                setattr(value, "graph_Node11", self)

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

class graph_Node:

    def __init__(self, name: str, Node: "graph_Graph" = None, node: "graph_Mark" = None, nodes: "graph_Graph" = None, graph_Node: "graph_Edge" = None, graph_Node11: "graph_Edge" = None, Node15: "graph_Mark" = None):
        self.name = name
        self.Node = Node
        self.node = node
        self.nodes = nodes
        self.graph_Node = graph_Node
        self.graph_Node11 = graph_Node11
        self.Node15 = Node15
        
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

    @property
    def graph_Node11(self):
        return self.__graph_Node11

    @graph_Node11.setter
    def graph_Node11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Node__graph_Node11", None)
        self.__graph_Node11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_Edge10"):
                opp_val = getattr(old_value, "graph_Edge10", None)
                if opp_val == self:
                    setattr(old_value, "graph_Edge10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_Edge10"):
                opp_val = getattr(value, "graph_Edge10", None)
                setattr(value, "graph_Edge10", self)

    @property
    def node(self):
        return self.__node

    @node.setter
    def node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Node__node", None)
        self.__node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Mark6"):
                opp_val = getattr(old_value, "Mark6", None)
                if opp_val == self:
                    setattr(old_value, "Mark6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Mark6"):
                opp_val = getattr(value, "Mark6", None)
                setattr(value, "Mark6", self)

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
    def Node15(self):
        return self.__Node15

    @Node15.setter
    def Node15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Node__Node15", None)
        self.__Node15 = value
        
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

class graph_Graph:

    def __init__(self, name: str, graph: set["graph_Node"] = None, graph2: set["graph_Edge"] = None, graph4: set["graph_Mark"] = None, Graph: "graph_Node" = None, Graph13: "graph_Edge" = None, Graph17: "graph_Mark" = None):
        self.name = name
        self.graph = graph if graph is not None else set()
        self.graph2 = graph2 if graph2 is not None else set()
        self.graph4 = graph4 if graph4 is not None else set()
        self.Graph = Graph
        self.Graph13 = Graph13
        self.Graph17 = Graph17
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Graph(self):
        return self.__Graph

    @Graph.setter
    def Graph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Graph__Graph", None)
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
    def graph2(self):
        return self.__graph2

    @graph2.setter
    def graph2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Graph__graph2", None)
        self.__graph2 = value if value is not None else set()
        
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
    def Graph17(self):
        return self.__Graph17

    @Graph17.setter
    def Graph17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Graph__Graph17", None)
        self.__Graph17 = value
        
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
    def Graph13(self):
        return self.__Graph13

    @Graph13.setter
    def Graph13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Graph__Graph13", None)
        self.__Graph13 = value
        
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
    def graph4(self):
        return self.__graph4

    @graph4.setter
    def graph4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Graph__graph4", None)
        self.__graph4 = value if value is not None else set()
        
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
    def graph(self):
        return self.__graph

    @graph.setter
    def graph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_Graph__graph", None)
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
                    
