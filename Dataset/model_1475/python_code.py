from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class mgraph_MEdge:

    def __init__(self, name: str, from: "mgraph_MNode" = None, edges: "mgraph_MGraph" = None, MEdge: "mgraph_MGraph" = None, to: "mgraph_MNode" = None, MEdge11: "mgraph_MNode" = None, MEdge13: "mgraph_MNode" = None):
        self.name = name
        self.from = from
        self.edges = edges
        self.MEdge = MEdge
        self.to = to
        self.MEdge11 = MEdge11
        self.MEdge13 = MEdge13
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def from(self):
        return self.__from

    @from.setter
    def from(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mgraph_MEdge__from", None)
        self.__from = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MNode6"):
                opp_val = getattr(old_value, "MNode6", None)
                if opp_val == self:
                    setattr(old_value, "MNode6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MNode6"):
                opp_val = getattr(value, "MNode6", None)
                setattr(value, "MNode6", self)

    @property
    def MEdge13(self):
        return self.__MEdge13

    @MEdge13.setter
    def MEdge13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mgraph_MEdge__MEdge13", None)
        self.__MEdge13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "inComing"):
                opp_val = getattr(old_value, "inComing", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "inComing"):
                opp_val = getattr(value, "inComing", None)
                if opp_val is None:
                    setattr(value, "inComing", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def to(self):
        return self.__to

    @to.setter
    def to(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mgraph_MEdge__to", None)
        self.__to = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MNode4"):
                opp_val = getattr(old_value, "MNode4", None)
                if opp_val == self:
                    setattr(old_value, "MNode4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MNode4"):
                opp_val = getattr(value, "MNode4", None)
                setattr(value, "MNode4", self)

    @property
    def MEdge11(self):
        return self.__MEdge11

    @MEdge11.setter
    def MEdge11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mgraph_MEdge__MEdge11", None)
        self.__MEdge11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outGoing"):
                opp_val = getattr(old_value, "outGoing", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outGoing"):
                opp_val = getattr(value, "outGoing", None)
                if opp_val is None:
                    setattr(value, "outGoing", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def edges(self):
        return self.__edges

    @edges.setter
    def edges(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mgraph_MEdge__edges", None)
        self.__edges = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MGraph"):
                opp_val = getattr(old_value, "MGraph", None)
                if opp_val == self:
                    setattr(old_value, "MGraph", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MGraph"):
                opp_val = getattr(value, "MGraph", None)
                setattr(value, "MGraph", self)

    @property
    def MEdge(self):
        return self.__MEdge

    @MEdge.setter
    def MEdge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mgraph_MEdge__MEdge", None)
        self.__MEdge = value
        
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

class mgraph_MNode:

    def __init__(self, name: str, MNode: "mgraph_MGraph" = None, MNode6: "mgraph_MEdge" = None, nodes: "mgraph_MGraph" = None, MNode4: "mgraph_MEdge" = None, outGoing: set["mgraph_MEdge"] = None, inComing: set["mgraph_MEdge"] = None):
        self.name = name
        self.MNode = MNode
        self.MNode6 = MNode6
        self.nodes = nodes
        self.MNode4 = MNode4
        self.outGoing = outGoing if outGoing is not None else set()
        self.inComing = inComing if inComing is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def MNode6(self):
        return self.__MNode6

    @MNode6.setter
    def MNode6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mgraph_MNode__MNode6", None)
        self.__MNode6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "from"):
                opp_val = getattr(old_value, "from", None)
                if opp_val == self:
                    setattr(old_value, "from", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "from"):
                opp_val = getattr(value, "from", None)
                setattr(value, "from", self)

    @property
    def MNode(self):
        return self.__MNode

    @MNode.setter
    def MNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mgraph_MNode__MNode", None)
        self.__MNode = value
        
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
    def outGoing(self):
        return self.__outGoing

    @outGoing.setter
    def outGoing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mgraph_MNode__outGoing", None)
        self.__outGoing = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MEdge11"):
                    opp_val = getattr(item, "MEdge11", None)
                    
                    if opp_val == self:
                        setattr(item, "MEdge11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MEdge11"):
                    opp_val = getattr(item, "MEdge11", None)
                    
                    setattr(item, "MEdge11", self)
                    

    @property
    def inComing(self):
        return self.__inComing

    @inComing.setter
    def inComing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mgraph_MNode__inComing", None)
        self.__inComing = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MEdge13"):
                    opp_val = getattr(item, "MEdge13", None)
                    
                    if opp_val == self:
                        setattr(item, "MEdge13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MEdge13"):
                    opp_val = getattr(item, "MEdge13", None)
                    
                    setattr(item, "MEdge13", self)
                    

    @property
    def nodes(self):
        return self.__nodes

    @nodes.setter
    def nodes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mgraph_MNode__nodes", None)
        self.__nodes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MGraph9"):
                opp_val = getattr(old_value, "MGraph9", None)
                if opp_val == self:
                    setattr(old_value, "MGraph9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MGraph9"):
                opp_val = getattr(value, "MGraph9", None)
                setattr(value, "MGraph9", self)

    @property
    def MNode4(self):
        return self.__MNode4

    @MNode4.setter
    def MNode4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mgraph_MNode__MNode4", None)
        self.__MNode4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "to"):
                opp_val = getattr(old_value, "to", None)
                if opp_val == self:
                    setattr(old_value, "to", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "to"):
                opp_val = getattr(value, "to", None)
                setattr(value, "to", self)

class mgraph_MGraph:

    def __init__(self, name: str, graph: set["mgraph_MNode"] = None, MGraph: "mgraph_MEdge" = None, graph2: set["mgraph_MEdge"] = None, MGraph9: "mgraph_MNode" = None):
        self.name = name
        self.graph = graph if graph is not None else set()
        self.MGraph = MGraph
        self.graph2 = graph2 if graph2 is not None else set()
        self.MGraph9 = MGraph9
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def MGraph(self):
        return self.__MGraph

    @MGraph.setter
    def MGraph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mgraph_MGraph__MGraph", None)
        self.__MGraph = value
        
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
        old_value = getattr(self, f"_mgraph_MGraph__graph", None)
        self.__graph = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MNode"):
                    opp_val = getattr(item, "MNode", None)
                    
                    if opp_val == self:
                        setattr(item, "MNode", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MNode"):
                    opp_val = getattr(item, "MNode", None)
                    
                    setattr(item, "MNode", self)
                    

    @property
    def MGraph9(self):
        return self.__MGraph9

    @MGraph9.setter
    def MGraph9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mgraph_MGraph__MGraph9", None)
        self.__MGraph9 = value
        
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
        old_value = getattr(self, f"_mgraph_MGraph__graph2", None)
        self.__graph2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MEdge"):
                    opp_val = getattr(item, "MEdge", None)
                    
                    if opp_val == self:
                        setattr(item, "MEdge", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MEdge"):
                    opp_val = getattr(item, "MEdge", None)
                    
                    setattr(item, "MEdge", self)
                    
