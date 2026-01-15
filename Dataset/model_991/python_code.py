from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class EdgeType(Enum):
    TREE_EDGE = "TREE_EDGE"
    BACKWARD_EDGE = "BACKWARD_EDGE"
    FORWARD_EDGE = "FORWARD_EDGE"
    CROSS_EDGE = "CROSS_EDGE"


############################################
# Definition of Classes
############################################

class dfs_DFSGraph:

    pass
class dfs_Edge:

    def __init__(self, type: str, Edge6: "dfs_Node" = None, edges: "dfs_DFSGraph" = None, outgoing: "dfs_Node" = None, dfs_Edge: "dfs_EObject" = None, incoming: "dfs_Node" = None, Edge15: "dfs_DFSGraph" = None, Edge: "dfs_Node" = None):
        self.type = type
        self.Edge6 = Edge6
        self.edges = edges
        self.outgoing = outgoing
        self.dfs_Edge = dfs_Edge
        self.incoming = incoming
        self.Edge15 = Edge15
        self.Edge = Edge
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def Edge15(self):
        return self.__Edge15

    @Edge15.setter
    def Edge15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dfs_Edge__Edge15", None)
        self.__Edge15 = value
        
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
    def dfs_Edge(self):
        return self.__dfs_Edge

    @dfs_Edge.setter
    def dfs_Edge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dfs_Edge__dfs_Edge", None)
        self.__dfs_Edge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dfs_EObject11"):
                opp_val = getattr(old_value, "dfs_EObject11", None)
                if opp_val == self:
                    setattr(old_value, "dfs_EObject11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dfs_EObject11"):
                opp_val = getattr(value, "dfs_EObject11", None)
                setattr(value, "dfs_EObject11", self)

    @property
    def Edge(self):
        return self.__Edge

    @Edge.setter
    def Edge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dfs_Edge__Edge", None)
        self.__Edge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "target"):
                opp_val = getattr(old_value, "target", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "target"):
                opp_val = getattr(value, "target", None)
                if opp_val is None:
                    setattr(value, "target", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def edges(self):
        return self.__edges

    @edges.setter
    def edges(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dfs_Edge__edges", None)
        self.__edges = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DFSGraph8"):
                opp_val = getattr(old_value, "DFSGraph8", None)
                if opp_val == self:
                    setattr(old_value, "DFSGraph8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DFSGraph8"):
                opp_val = getattr(value, "DFSGraph8", None)
                setattr(value, "DFSGraph8", self)

    @property
    def outgoing(self):
        return self.__outgoing

    @outgoing.setter
    def outgoing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dfs_Edge__outgoing", None)
        self.__outgoing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Node"):
                opp_val = getattr(old_value, "Node", None)
                if opp_val == self:
                    setattr(old_value, "Node", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Node"):
                opp_val = getattr(value, "Node", None)
                setattr(value, "Node", self)

    @property
    def incoming(self):
        return self.__incoming

    @incoming.setter
    def incoming(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dfs_Edge__incoming", None)
        self.__incoming = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Node13"):
                opp_val = getattr(old_value, "Node13", None)
                if opp_val == self:
                    setattr(old_value, "Node13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Node13"):
                opp_val = getattr(value, "Node13", None)
                setattr(value, "Node13", self)

    @property
    def Edge6(self):
        return self.__Edge6

    @Edge6.setter
    def Edge6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dfs_Edge__Edge6", None)
        self.__Edge6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "source"):
                opp_val = getattr(old_value, "source", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "source"):
                opp_val = getattr(value, "source", None)
                if opp_val is None:
                    setattr(value, "source", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dfs_Node:

    def __init__(self, postTraversal: int, preTraversal: int, nodes: "dfs_DFSGraph" = None, dfs_Node: "dfs_EObject" = None, source: set["dfs_Edge"] = None, Node: "dfs_Edge" = None, Node13: "dfs_Edge" = None, target: set["dfs_Edge"] = None, Node18: "dfs_DFSGraph" = None):
        self.postTraversal = postTraversal
        self.preTraversal = preTraversal
        self.nodes = nodes
        self.dfs_Node = dfs_Node
        self.source = source if source is not None else set()
        self.Node = Node
        self.Node13 = Node13
        self.target = target if target is not None else set()
        self.Node18 = Node18
        
    @property
    def postTraversal(self) -> int:
        return self.__postTraversal

    @postTraversal.setter
    def postTraversal(self, postTraversal: int):
        self.__postTraversal = postTraversal

    @property
    def preTraversal(self) -> int:
        return self.__preTraversal

    @preTraversal.setter
    def preTraversal(self, preTraversal: int):
        self.__preTraversal = preTraversal

    @property
    def Node13(self):
        return self.__Node13

    @Node13.setter
    def Node13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dfs_Node__Node13", None)
        self.__Node13 = value
        
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
        old_value = getattr(self, f"_dfs_Node__target", None)
        self.__target = value if value is not None else set()
        
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
    def Node18(self):
        return self.__Node18

    @Node18.setter
    def Node18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dfs_Node__Node18", None)
        self.__Node18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph17"):
                opp_val = getattr(old_value, "graph17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph17"):
                opp_val = getattr(value, "graph17", None)
                if opp_val is None:
                    setattr(value, "graph17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def nodes(self):
        return self.__nodes

    @nodes.setter
    def nodes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dfs_Node__nodes", None)
        self.__nodes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DFSGraph"):
                opp_val = getattr(old_value, "DFSGraph", None)
                if opp_val == self:
                    setattr(old_value, "DFSGraph", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DFSGraph"):
                opp_val = getattr(value, "DFSGraph", None)
                setattr(value, "DFSGraph", self)

    @property
    def dfs_Node(self):
        return self.__dfs_Node

    @dfs_Node.setter
    def dfs_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dfs_Node__dfs_Node", None)
        self.__dfs_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dfs_EObject"):
                opp_val = getattr(old_value, "dfs_EObject", None)
                if opp_val == self:
                    setattr(old_value, "dfs_EObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dfs_EObject"):
                opp_val = getattr(value, "dfs_EObject", None)
                setattr(value, "dfs_EObject", self)

    @property
    def Node(self):
        return self.__Node

    @Node.setter
    def Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dfs_Node__Node", None)
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
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dfs_Node__source", None)
        self.__source = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Edge6"):
                    opp_val = getattr(item, "Edge6", None)
                    
                    if opp_val == self:
                        setattr(item, "Edge6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Edge6"):
                    opp_val = getattr(item, "Edge6", None)
                    
                    setattr(item, "Edge6", self)
                    

class EdgeProcessor:

    pass
class dfs_DepthFirstSearch(EdgeProcessor):

    def __init__(self, postTraversalCounter: int, preTraversalCounter: int):
        self.postTraversalCounter = postTraversalCounter
        self.preTraversalCounter = preTraversalCounter
        
    @property
    def postTraversalCounter(self) -> int:
        return self.__postTraversalCounter

    @postTraversalCounter.setter
    def postTraversalCounter(self, postTraversalCounter: int):
        self.__postTraversalCounter = postTraversalCounter

    @property
    def preTraversalCounter(self) -> int:
        return self.__preTraversalCounter

    @preTraversalCounter.setter
    def preTraversalCounter(self, preTraversalCounter: int):
        self.__preTraversalCounter = preTraversalCounter

    def processEdge(self, edge: str) -> str:
        # TODO: Implement processEdge method
        pass

    def processNode(self, node: str) -> str:
        # TODO: Implement processNode method
        pass

    def incrementPreTraversalCounter(self) -> int:
        # TODO: Implement incrementPreTraversalCounter method
        pass

    def incrementPostTraversalCounter(self) -> int:
        # TODO: Implement incrementPostTraversalCounter method
        pass

class dfs_EObject:

    pass
class dfs_EdgeProcessor(ABC):

    def __init__(self, dfs_EdgeProcessor: "dfs_EdgeProcessor" = None, dfs_EdgeProcessor0: "dfs_EdgeProcessor" = None):
        self.dfs_EdgeProcessor = dfs_EdgeProcessor
        self.dfs_EdgeProcessor0 = dfs_EdgeProcessor0
        
    @property
    def dfs_EdgeProcessor(self):
        return self.__dfs_EdgeProcessor

    @dfs_EdgeProcessor.setter
    def dfs_EdgeProcessor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dfs_EdgeProcessor__dfs_EdgeProcessor", None)
        self.__dfs_EdgeProcessor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dfs_EdgeProcessor0"):
                opp_val = getattr(old_value, "dfs_EdgeProcessor0", None)
                if opp_val == self:
                    setattr(old_value, "dfs_EdgeProcessor0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dfs_EdgeProcessor0"):
                opp_val = getattr(value, "dfs_EdgeProcessor0", None)
                setattr(value, "dfs_EdgeProcessor0", self)

    @property
    def dfs_EdgeProcessor0(self):
        return self.__dfs_EdgeProcessor0

    @dfs_EdgeProcessor0.setter
    def dfs_EdgeProcessor0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dfs_EdgeProcessor__dfs_EdgeProcessor0", None)
        self.__dfs_EdgeProcessor0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dfs_EdgeProcessor"):
                opp_val = getattr(old_value, "dfs_EdgeProcessor", None)
                if opp_val == self:
                    setattr(old_value, "dfs_EdgeProcessor", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dfs_EdgeProcessor"):
                opp_val = getattr(value, "dfs_EdgeProcessor", None)
                setattr(value, "dfs_EdgeProcessor", self)

    def processNode(self, node: str) -> str:
        # TODO: Implement processNode method
        pass

    def processEdge(self, edge: str) -> str:
        # TODO: Implement processEdge method
        pass
