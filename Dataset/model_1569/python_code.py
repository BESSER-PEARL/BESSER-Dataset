from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class graphdom_Edge:

    def __init__(self, guid: str, weight: int, marked: bool, graphdom_Edge: "graphdom_Graph" = None, Edge: "graphdom_Node" = None, connectedEdges: set["graphdom_Node"] = None):
        self.guid = guid
        self.weight = weight
        self.marked = marked
        self.graphdom_Edge = graphdom_Edge
        self.Edge = Edge
        self.connectedEdges = connectedEdges if connectedEdges is not None else set()
        
    @property
    def marked(self) -> bool:
        return self.__marked

    @marked.setter
    def marked(self, marked: bool):
        self.__marked = marked

    @property
    def weight(self) -> int:
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight

    @property
    def guid(self) -> str:
        return self.__guid

    @guid.setter
    def guid(self, guid: str):
        self.__guid = guid

    @property
    def graphdom_Edge(self):
        return self.__graphdom_Edge

    @graphdom_Edge.setter
    def graphdom_Edge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphdom_Edge__graphdom_Edge", None)
        self.__graphdom_Edge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphdom_Graph2"):
                opp_val = getattr(old_value, "graphdom_Graph2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphdom_Graph2"):
                opp_val = getattr(value, "graphdom_Graph2", None)
                if opp_val is None:
                    setattr(value, "graphdom_Graph2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Edge(self):
        return self.__Edge

    @Edge.setter
    def Edge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphdom_Edge__Edge", None)
        self.__Edge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connectedNodes"):
                opp_val = getattr(old_value, "connectedNodes", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connectedNodes"):
                opp_val = getattr(value, "connectedNodes", None)
                if opp_val is None:
                    setattr(value, "connectedNodes", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def connectedEdges(self):
        return self.__connectedEdges

    @connectedEdges.setter
    def connectedEdges(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphdom_Edge__connectedEdges", None)
        self.__connectedEdges = value if value is not None else set()
        
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
                    

    def flip(self) -> bool:
        # TODO: Implement flip method
        pass

class graphdom_Node:

    def __init__(self, nodeName: str, color: str, dominating: bool, grade: str, guid: str, xCoord: int, yCoord: int, dominated: bool, graphdom_Node: "graphdom_Graph" = None, connectedNodes: set["graphdom_Edge"] = None, Node: "graphdom_Edge" = None):
        self.nodeName = nodeName
        self.color = color
        self.dominating = dominating
        self.grade = grade
        self.guid = guid
        self.xCoord = xCoord
        self.yCoord = yCoord
        self.dominated = dominated
        self.graphdom_Node = graphdom_Node
        self.connectedNodes = connectedNodes if connectedNodes is not None else set()
        self.Node = Node
        
    @property
    def dominated(self) -> bool:
        return self.__dominated

    @dominated.setter
    def dominated(self, dominated: bool):
        self.__dominated = dominated

    @property
    def grade(self) -> str:
        return self.__grade

    @grade.setter
    def grade(self, grade: str):
        self.__grade = grade

    @property
    def nodeName(self) -> str:
        return self.__nodeName

    @nodeName.setter
    def nodeName(self, nodeName: str):
        self.__nodeName = nodeName

    @property
    def dominating(self) -> bool:
        return self.__dominating

    @dominating.setter
    def dominating(self, dominating: bool):
        self.__dominating = dominating

    @property
    def xCoord(self) -> int:
        return self.__xCoord

    @xCoord.setter
    def xCoord(self, xCoord: int):
        self.__xCoord = xCoord

    @property
    def guid(self) -> str:
        return self.__guid

    @guid.setter
    def guid(self, guid: str):
        self.__guid = guid

    @property
    def yCoord(self) -> int:
        return self.__yCoord

    @yCoord.setter
    def yCoord(self, yCoord: int):
        self.__yCoord = yCoord

    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

    @property
    def connectedNodes(self):
        return self.__connectedNodes

    @connectedNodes.setter
    def connectedNodes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphdom_Node__connectedNodes", None)
        self.__connectedNodes = value if value is not None else set()
        
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
    def graphdom_Node(self):
        return self.__graphdom_Node

    @graphdom_Node.setter
    def graphdom_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphdom_Node__graphdom_Node", None)
        self.__graphdom_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphdom_Graph"):
                opp_val = getattr(old_value, "graphdom_Graph", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphdom_Graph"):
                opp_val = getattr(value, "graphdom_Graph", None)
                if opp_val is None:
                    setattr(value, "graphdom_Graph", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Node(self):
        return self.__Node

    @Node.setter
    def Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphdom_Node__Node", None)
        self.__Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connectedEdges"):
                opp_val = getattr(old_value, "connectedEdges", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connectedEdges"):
                opp_val = getattr(value, "connectedEdges", None)
                if opp_val is None:
                    setattr(value, "connectedEdges", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def getAdjacentNodes(self) -> str:
        # TODO: Implement getAdjacentNodes method
        pass

class graphdom_Graph:

    def __init__(self, graphName: str, graphdom_Graph: set["graphdom_Node"] = None, graphdom_Graph2: set["graphdom_Edge"] = None):
        self.graphName = graphName
        self.graphdom_Graph = graphdom_Graph if graphdom_Graph is not None else set()
        self.graphdom_Graph2 = graphdom_Graph2 if graphdom_Graph2 is not None else set()
        
    @property
    def graphName(self) -> str:
        return self.__graphName

    @graphName.setter
    def graphName(self, graphName: str):
        self.__graphName = graphName

    @property
    def graphdom_Graph(self):
        return self.__graphdom_Graph

    @graphdom_Graph.setter
    def graphdom_Graph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphdom_Graph__graphdom_Graph", None)
        self.__graphdom_Graph = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "graphdom_Node"):
                    opp_val = getattr(item, "graphdom_Node", None)
                    
                    if opp_val == self:
                        setattr(item, "graphdom_Node", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graphdom_Node"):
                    opp_val = getattr(item, "graphdom_Node", None)
                    
                    setattr(item, "graphdom_Node", self)
                    

    @property
    def graphdom_Graph2(self):
        return self.__graphdom_Graph2

    @graphdom_Graph2.setter
    def graphdom_Graph2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphdom_Graph__graphdom_Graph2", None)
        self.__graphdom_Graph2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "graphdom_Edge"):
                    opp_val = getattr(item, "graphdom_Edge", None)
                    
                    if opp_val == self:
                        setattr(item, "graphdom_Edge", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graphdom_Edge"):
                    opp_val = getattr(item, "graphdom_Edge", None)
                    
                    setattr(item, "graphdom_Edge", self)
                    

    def checkNodesDomination(self):
        # TODO: Implement checkNodesDomination method
        pass

    def isIndependentlyDominated(self) -> bool:
        # TODO: Implement isIndependentlyDominated method
        pass

    def findNodeById(self, id: str) -> str:
        # TODO: Implement findNodeById method
        pass

    def getNextNodeId(self) -> int:
        # TODO: Implement getNextNodeId method
        pass

    def isTotallyDominated(self) -> bool:
        # TODO: Implement isTotallyDominated method
        pass

    def isConnectedDomination(self) -> bool:
        # TODO: Implement isConnectedDomination method
        pass

    def removeNode(self, node: str):
        # TODO: Implement removeNode method
        pass

    def getDominatingSet(self) -> str:
        # TODO: Implement getDominatingSet method
        pass

    def isDominated(self) -> bool:
        # TODO: Implement isDominated method
        pass

    def unmarkAllNodes(self):
        # TODO: Implement unmarkAllNodes method
        pass
