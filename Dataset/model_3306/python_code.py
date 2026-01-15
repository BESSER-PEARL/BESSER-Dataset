from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Solver:

    pass
class rk_RungeKutta(Solver):

    def __init__(self, relativeTolerance: float):
        self.relativeTolerance = relativeTolerance
        
    @property
    def relativeTolerance(self) -> float:
        return self.__relativeTolerance

    @relativeTolerance.setter
    def relativeTolerance(self, relativeTolerance: float):
        self.__relativeTolerance = relativeTolerance
