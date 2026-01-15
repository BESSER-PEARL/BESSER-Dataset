from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Edge:

    pass
class uppaalSMC_ChanceEdge(Edge):

    def __init__(self, weight: int):
        self.weight = weight
        
    @property
    def weight(self) -> int:
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight

class Location:

    pass
class uppaalSMC_ExponentialLocation(Location):

    pass
class uppaalSMC_ChanceNode(Location):

    pass
class Type:

    pass
class uppaalSMC_DoubleType(Type):

    pass
class NTA:

    pass
class uppaalSMC_NSTA(NTA):

    pass
class Expression:

    pass