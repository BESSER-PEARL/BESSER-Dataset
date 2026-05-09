from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class graph_Vertex:

    def __init__(self, hotSpot: bool):
        self.hotSpot = hotSpot
        
        pass
    @property
    def hotSpot(self):
        return self.__hotSpot

    @hotSpot.setter
    def hotSpot(self, hotSpot: bool):
        self.__hotSpot = hotSpot


    def getIncomingEdgeFrom(self, graph_vertex_p):
        # TODO: Implement getIncomingEdgeFrom method
        pass

    def hasForIncomingAdjacent(self, graph_vertex_p) :
        # TODO: Implement hasForIncomingAdjacent method
        pass

    def hasForAdjacent(self, graph_vertex_p) :
        # TODO: Implement hasForAdjacent method
        pass

    def getOutgoingEdgeTo(self, graph_vertex_p):
        # TODO: Implement getOutgoingEdgeTo method
        pass

    def hasForOutgoingAdjacent(self, graph_vertex_p) :
        # TODO: Implement hasForOutgoingAdjacent method
        pass

    def getEdgeTo(self, graph_vertex_p):
        # TODO: Implement getEdgeTo method
        pass

class graph_Edge:

    def __init__(self, critical: bool):
        self.critical = critical
        
        pass
    @property
    def critical(self):
        return self.__critical

    @critical.setter
    def critical(self, critical: bool):
        self.__critical = critical


    def update(self, graph_targetVertex_p, graph_criticalEdge_p, graph_sourceVertex_p):
        # TODO: Implement update method
        pass

class graph_GraphElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class graph_Graph:

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    def addNamedAdjacent(self, graph_critical_p, graph_edgeContent_p, graph_target_p, graph_edgeName_p, graph_source_p):
        # TODO: Implement addNamedAdjacent method
        pass

    def addAdjacent(self, graph_target_p, graph_critical_p, graph_edgeContent_p, graph_source_p):
        # TODO: Implement addAdjacent method
        pass

    def addVertex(self, graph_vertex_p):
        # TODO: Implement addVertex method
        pass

    def addEdge(self, graph_edge_p):
        # TODO: Implement addEdge method
        pass
