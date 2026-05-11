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
        
        pass
    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius: float):
        self.__radius = radius


    @property
    def angularStep(self):
        return self.__angularStep

    @angularStep.setter
    def angularStep(self, angularStep: int):
        self.__angularStep = angularStep


class graphgenerators_SquareLatticeGraphGenerator(LatticeGraphGenerator):

    def __init__(self, xSize: int, ySize: int, area: float):
        self.xSize = xSize
        self.ySize = ySize
        self.area = area
        
        pass
    @property
    def area(self):
        return self.__area

    @area.setter
    def area(self, area: float):
        self.__area = area


    @property
    def ySize(self):
        return self.__ySize

    @ySize.setter
    def ySize(self, ySize: int):
        self.__ySize = ySize


    @property
    def xSize(self):
        return self.__xSize

    @xSize.setter
    def xSize(self, xSize: int):
        self.__xSize = xSize


class GraphGenerator:

    pass
class graphgenerators_MigrationEdgeGraphGenerator(GraphGenerator):

    def __init__(self, location: str, migrationRate: float, population: str):
        self.location = location
        self.migrationRate = migrationRate
        self.population = population
        
        pass
    @property
    def population(self):
        return self.__population

    @population.setter
    def population(self, population: str):
        self.__population = population


    @property
    def migrationRate(self):
        return self.__migrationRate

    @migrationRate.setter
    def migrationRate(self, migrationRate: float):
        self.__migrationRate = migrationRate


    @property
    def location(self):
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
        
        pass
    @property
    def area(self):
        return self.__area

    @area.setter
    def area(self, area: float):
        self.__area = area


    @property
    def colArea(self):
        return self.__colArea

    @colArea.setter
    def colArea(self, colArea: int):
        self.__colArea = colArea


    @property
    def zoomFactor(self):
        return self.__zoomFactor

    @zoomFactor.setter
    def zoomFactor(self, zoomFactor: int):
        self.__zoomFactor = zoomFactor


    @property
    def dataFile_net(self):
        return self.__dataFile_net

    @dataFile_net.setter
    def dataFile_net(self, dataFile_net: str):
        self.__dataFile_net = dataFile_net


class graphgenerators_LatticeGraphGenerator(GraphGenerator):

    def __init__(self, useNearestNeighbors: bool, useNextNearestNeighbors: bool, periodicBoundaries: bool):
        self.useNearestNeighbors = useNearestNeighbors
        self.useNextNearestNeighbors = useNextNearestNeighbors
        self.periodicBoundaries = periodicBoundaries
        
        pass
    @property
    def periodicBoundaries(self):
        return self.__periodicBoundaries

    @periodicBoundaries.setter
    def periodicBoundaries(self, periodicBoundaries: bool):
        self.__periodicBoundaries = periodicBoundaries


    @property
    def useNextNearestNeighbors(self):
        return self.__useNextNearestNeighbors

    @useNextNearestNeighbors.setter
    def useNextNearestNeighbors(self, useNextNearestNeighbors: bool):
        self.__useNextNearestNeighbors = useNextNearestNeighbors


    @property
    def useNearestNeighbors(self):
        return self.__useNearestNeighbors

    @useNearestNeighbors.setter
    def useNearestNeighbors(self, useNearestNeighbors: bool):
        self.__useNearestNeighbors = useNearestNeighbors


class Identifiable:

    pass
class graphgenerators_GraphGenerator(Identifiable):

    def __init__(self):
        
        pass
    def getGraph(self) :
        # TODO: Implement getGraph method
        pass
