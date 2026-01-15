from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class LatticeGraphGenerator:

    pass
class graphgenerators_PlateCarreeGlobeGraphGenerator(LatticeGraphGenerator):

    def __init__(self, angularStep: int, radius: float):
        self.angularStep = angularStep
        self.radius = radius
        
    @property
    def angularStep(self) -> int:
        return self.__angularStep

    @angularStep.setter
    def angularStep(self, angularStep: int):
        self.__angularStep = angularStep

    @property
    def radius(self) -> float:
        return self.__radius

    @radius.setter
    def radius(self, radius: float):
        self.__radius = radius

class graphgenerators_SquareLatticeGraphGenerator(LatticeGraphGenerator):

    def __init__(self, xSize: int, ySize: int, area: float):
        self.xSize = xSize
        self.ySize = ySize
        self.area = area
        
    @property
    def area(self) -> float:
        return self.__area

    @area.setter
    def area(self, area: float):
        self.__area = area

    @property
    def xSize(self) -> int:
        return self.__xSize

    @xSize.setter
    def xSize(self, xSize: int):
        self.__xSize = xSize

    @property
    def ySize(self) -> int:
        return self.__ySize

    @ySize.setter
    def ySize(self, ySize: int):
        self.__ySize = ySize

class GraphGenerator:

    pass
class graphgenerators_MigrationEdgeGraphGenerator(GraphGenerator):

    def __init__(self, migrationRate: float, population: str, location: str):
        self.migrationRate = migrationRate
        self.population = population
        self.location = location
        
    @property
    def migrationRate(self) -> float:
        return self.__migrationRate

    @migrationRate.setter
    def migrationRate(self, migrationRate: float):
        self.__migrationRate = migrationRate

    @property
    def population(self) -> str:
        return self.__population

    @population.setter
    def population(self, population: str):
        self.__population = population

    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

class graphgenerators_PajekNetGraphGenerator(GraphGenerator):

    def __init__(self, dataFile_net: str, area: float, zoomFactor: int, colArea: int):
        self.dataFile_net = dataFile_net
        self.area = area
        self.zoomFactor = zoomFactor
        self.colArea = colArea
        
    @property
    def dataFile_net(self) -> str:
        return self.__dataFile_net

    @dataFile_net.setter
    def dataFile_net(self, dataFile_net: str):
        self.__dataFile_net = dataFile_net

    @property
    def colArea(self) -> int:
        return self.__colArea

    @colArea.setter
    def colArea(self, colArea: int):
        self.__colArea = colArea

    @property
    def zoomFactor(self) -> int:
        return self.__zoomFactor

    @zoomFactor.setter
    def zoomFactor(self, zoomFactor: int):
        self.__zoomFactor = zoomFactor

    @property
    def area(self) -> float:
        return self.__area

    @area.setter
    def area(self, area: float):
        self.__area = area

class graphgenerators_LatticeGraphGenerator(GraphGenerator):

    def __init__(self, useNearestNeighbors: bool, useNextNearestNeighbors: bool, periodicBoundaries: bool):
        self.useNearestNeighbors = useNearestNeighbors
        self.useNextNearestNeighbors = useNextNearestNeighbors
        self.periodicBoundaries = periodicBoundaries
        
    @property
    def useNextNearestNeighbors(self) -> bool:
        return self.__useNextNearestNeighbors

    @useNextNearestNeighbors.setter
    def useNextNearestNeighbors(self, useNextNearestNeighbors: bool):
        self.__useNextNearestNeighbors = useNextNearestNeighbors

    @property
    def periodicBoundaries(self) -> bool:
        return self.__periodicBoundaries

    @periodicBoundaries.setter
    def periodicBoundaries(self, periodicBoundaries: bool):
        self.__periodicBoundaries = periodicBoundaries

    @property
    def useNearestNeighbors(self) -> bool:
        return self.__useNearestNeighbors

    @useNearestNeighbors.setter
    def useNearestNeighbors(self, useNearestNeighbors: bool):
        self.__useNearestNeighbors = useNearestNeighbors

class Identifiable:

    pass
class graphgenerators_GraphGenerator(Identifiable):

    def __init__(self):
        
    def getGraph(self) -> str:
        # TODO: Implement getGraph method
        pass
