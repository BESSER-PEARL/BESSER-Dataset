from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class StochasticSIRDiseaseModel:

    pass
class example_ExampleDiseaseModel(StochasticSIRDiseaseModel):

    def __init__(self, seasonalModulationExponent: float, modulationPeriod: float, modulationPhaseShift: float, seasonalModulationFloor: float):
        self.seasonalModulationExponent = seasonalModulationExponent
        self.modulationPeriod = modulationPeriod
        self.modulationPhaseShift = modulationPhaseShift
        self.seasonalModulationFloor = seasonalModulationFloor
        
    @property
    def seasonalModulationExponent(self) -> float:
        return self.__seasonalModulationExponent

    @seasonalModulationExponent.setter
    def seasonalModulationExponent(self, seasonalModulationExponent: float):
        self.__seasonalModulationExponent = seasonalModulationExponent

    @property
    def modulationPhaseShift(self) -> float:
        return self.__modulationPhaseShift

    @modulationPhaseShift.setter
    def modulationPhaseShift(self, modulationPhaseShift: float):
        self.__modulationPhaseShift = modulationPhaseShift

    @property
    def modulationPeriod(self) -> float:
        return self.__modulationPeriod

    @modulationPeriod.setter
    def modulationPeriod(self, modulationPeriod: float):
        self.__modulationPeriod = modulationPeriod

    @property
    def seasonalModulationFloor(self) -> float:
        return self.__seasonalModulationFloor

    @seasonalModulationFloor.setter
    def seasonalModulationFloor(self, seasonalModulationFloor: float):
        self.__seasonalModulationFloor = seasonalModulationFloor
