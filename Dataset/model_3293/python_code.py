from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Edge:

    pass
class edges_PopulationEdge(Edge):

    def __init__(self, populationIdentifier: str):
        self.populationIdentifier = populationIdentifier
        
        pass
    @property
    def populationIdentifier(self):
        return self.__populationIdentifier

    @populationIdentifier.setter
    def populationIdentifier(self, populationIdentifier: str):
        self.__populationIdentifier = populationIdentifier


class LabelValue:

    pass
class edges_MixingEdgeLabelValue(LabelValue):

    def __init__(self, mixingRate: float):
        self.mixingRate = mixingRate
        
        pass
    @property
    def mixingRate(self):
        return self.__mixingRate

    @mixingRate.setter
    def mixingRate(self, mixingRate: float):
        self.__mixingRate = mixingRate


class edges_MigrationEdgeLabelValue(LabelValue):

    def __init__(self, migrationRate: float):
        self.migrationRate = migrationRate
        
        pass
    @property
    def migrationRate(self):
        return self.__migrationRate

    @migrationRate.setter
    def migrationRate(self, migrationRate: float):
        self.__migrationRate = migrationRate


class EdgeLabel:

    pass
class edges_MixingEdgeLabel(EdgeLabel):

    pass
class edges_MigrationEdgeLabel(EdgeLabel):

    pass
class PopulationEdge:

    pass
class edges_MixingEdge(PopulationEdge):

    pass
class edges_MigrationEdge(PopulationEdge):

    pass