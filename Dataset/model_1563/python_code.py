from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class graph_Edge:

    def __init__(self, critical: bool):
        self.critical = critical
        
    @property
    def critical(self) -> bool:
        return self.__critical

    @critical.setter
    def critical(self, critical: bool):
        self.__critical = critical

    def update(self, targetVertex_p: str, sourceVertex_p: str):
        # TODO: Implement update method
        pass

    def update(self, sourceVertex_p: str, criticalEdge_p: bool, edgeName_p: str, targetVertex_p: str):
        # TODO: Implement update method
        pass

    def update(self, sourceVertex_p: str, criticalEdge_p: bool, targetVertex_p: str):
        # TODO: Implement update method
        pass

    def update(self, criticalEdge_p: bool, sourceVertex_p: str, targetVertex_p: str, edgeName_p: str, edgeContent_p: str):
        # TODO: Implement update method
        pass

class graph_Vertex:

    def __init__(self, hotSpot: bool):
        self.hotSpot = hotSpot
        
    @property
    def hotSpot(self) -> bool:
        return self.__hotSpot

    @hotSpot.setter
    def hotSpot(self, hotSpot: bool):
        self.__hotSpot = hotSpot

    def hasForOutgoingAdjacent(self, vertex_p: str) -> bool:
        # TODO: Implement hasForOutgoingAdjacent method
        pass

    def hasForIncomingAdjacent(self, vertex_p: str) -> bool:
        # TODO: Implement hasForIncomingAdjacent method
        pass

    def getOutgoingEdgeTo(self, vertex_p: str):
        # TODO: Implement getOutgoingEdgeTo method
        pass

    def getEdgeTo(self, vertex_p: str):
        # TODO: Implement getEdgeTo method
        pass

    def getIncomingEdgeFrom(self, vertex_p: str):
        # TODO: Implement getIncomingEdgeFrom method
        pass

    def hasForAdjacent(self, vertex_p: str) -> bool:
        # TODO: Implement hasForAdjacent method
        pass

class graph_GraphElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class graph_Graph:

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    def addAdjacent(self, source_p: str, edgeContent_p: str, critical_p: bool, target_p: str):
        # TODO: Implement addAdjacent method
        pass

    def addVertex(self, vertex_p: str):
        # TODO: Implement addVertex method
        pass

    def addNamedAdjacent(self, edgeName: str, edgeContent: str, source: str, target: str):
        # TODO: Implement addNamedAdjacent method
        pass

    def addEdge(self, edge_p: str):
        # TODO: Implement addEdge method
        pass

    def addAdjacent(self, source_p: str, target_p: str, edgeContent_p: str):
        # TODO: Implement addAdjacent method
        pass

    def addNamedAdjacent(self, edgeContent_p: str, edgeName_p: str, source_p: str, target_p: str, critical_p: bool):
        # TODO: Implement addNamedAdjacent method
        pass
