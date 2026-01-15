from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Gaussian2ForcingDiseaseModel:

    pass
class forcing_Gaussian3ForcingDiseaseModel(Gaussian2ForcingDiseaseModel):

    def __init__(self, sigma2_3: float, transmissionRate2: float, transmissionRate3: float, modulationFloor_2: float):
        self.sigma2_3 = sigma2_3
        self.transmissionRate2 = transmissionRate2
        self.transmissionRate3 = transmissionRate3
        self.modulationFloor_2 = modulationFloor_2
        
    @property
    def transmissionRate3(self) -> float:
        return self.__transmissionRate3

    @transmissionRate3.setter
    def transmissionRate3(self, transmissionRate3: float):
        self.__transmissionRate3 = transmissionRate3

    @property
    def transmissionRate2(self) -> float:
        return self.__transmissionRate2

    @transmissionRate2.setter
    def transmissionRate2(self, transmissionRate2: float):
        self.__transmissionRate2 = transmissionRate2

    @property
    def sigma2_3(self) -> float:
        return self.__sigma2_3

    @sigma2_3.setter
    def sigma2_3(self, sigma2_3: float):
        self.__sigma2_3 = sigma2_3

    @property
    def modulationFloor_2(self) -> float:
        return self.__modulationFloor_2

    @modulationFloor_2.setter
    def modulationFloor_2(self, modulationFloor_2: float):
        self.__modulationFloor_2 = modulationFloor_2

class StochasticSIRDiseaseModel:

    pass
class forcing_Gaussian2ForcingDiseaseModel(StochasticSIRDiseaseModel):

    def __init__(self, modulationPeriod: float, modulationPhaseShift: float, modulationFloor: float, sigma2_2: float, sigma2: float, att1: float, att2: float, att3: float, att4: float):
        self.modulationPeriod = modulationPeriod
        self.modulationPhaseShift = modulationPhaseShift
        self.modulationFloor = modulationFloor
        self.sigma2_2 = sigma2_2
        self.sigma2 = sigma2
        self.att1 = att1
        self.att2 = att2
        self.att3 = att3
        self.att4 = att4
        
    @property
    def att4(self) -> float:
        return self.__att4

    @att4.setter
    def att4(self, att4: float):
        self.__att4 = att4

    @property
    def modulationPhaseShift(self) -> float:
        return self.__modulationPhaseShift

    @modulationPhaseShift.setter
    def modulationPhaseShift(self, modulationPhaseShift: float):
        self.__modulationPhaseShift = modulationPhaseShift

    @property
    def att1(self) -> float:
        return self.__att1

    @att1.setter
    def att1(self, att1: float):
        self.__att1 = att1

    @property
    def sigma2(self) -> float:
        return self.__sigma2

    @sigma2.setter
    def sigma2(self, sigma2: float):
        self.__sigma2 = sigma2

    @property
    def att3(self) -> float:
        return self.__att3

    @att3.setter
    def att3(self, att3: float):
        self.__att3 = att3

    @property
    def sigma2_2(self) -> float:
        return self.__sigma2_2

    @sigma2_2.setter
    def sigma2_2(self, sigma2_2: float):
        self.__sigma2_2 = sigma2_2

    @property
    def modulationPeriod(self) -> float:
        return self.__modulationPeriod

    @modulationPeriod.setter
    def modulationPeriod(self, modulationPeriod: float):
        self.__modulationPeriod = modulationPeriod

    @property
    def att2(self) -> float:
        return self.__att2

    @att2.setter
    def att2(self, att2: float):
        self.__att2 = att2

    @property
    def modulationFloor(self) -> float:
        return self.__modulationFloor

    @modulationFloor.setter
    def modulationFloor(self, modulationFloor: float):
        self.__modulationFloor = modulationFloor

class forcing_GaussianForcingDiseaseModel(StochasticSIRDiseaseModel):

    def __init__(self, sigma2: float, modulationPeriod: float, modulationPhaseShift: float, modulationFloor: float):
        self.sigma2 = sigma2
        self.modulationPeriod = modulationPeriod
        self.modulationPhaseShift = modulationPhaseShift
        self.modulationFloor = modulationFloor
        
    @property
    def sigma2(self) -> float:
        return self.__sigma2

    @sigma2.setter
    def sigma2(self, sigma2: float):
        self.__sigma2 = sigma2

    @property
    def modulationFloor(self) -> float:
        return self.__modulationFloor

    @modulationFloor.setter
    def modulationFloor(self, modulationFloor: float):
        self.__modulationFloor = modulationFloor

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

class forcing_ForcingDiseaseModel(StochasticSIRDiseaseModel):

    def __init__(self, seasonalModulationExponent: float, modulationPeriod: float, modulationPhaseShift: float, seasonalModulationFloor: float):
        self.seasonalModulationExponent = seasonalModulationExponent
        self.modulationPeriod = modulationPeriod
        self.modulationPhaseShift = modulationPhaseShift
        self.seasonalModulationFloor = seasonalModulationFloor
        
    @property
    def modulationPeriod(self) -> float:
        return self.__modulationPeriod

    @modulationPeriod.setter
    def modulationPeriod(self, modulationPeriod: float):
        self.__modulationPeriod = modulationPeriod

    @property
    def seasonalModulationExponent(self) -> float:
        return self.__seasonalModulationExponent

    @seasonalModulationExponent.setter
    def seasonalModulationExponent(self, seasonalModulationExponent: float):
        self.__seasonalModulationExponent = seasonalModulationExponent

    @property
    def seasonalModulationFloor(self) -> float:
        return self.__seasonalModulationFloor

    @seasonalModulationFloor.setter
    def seasonalModulationFloor(self, seasonalModulationFloor: float):
        self.__seasonalModulationFloor = seasonalModulationFloor

    @property
    def modulationPhaseShift(self) -> float:
        return self.__modulationPhaseShift

    @modulationPhaseShift.setter
    def modulationPhaseShift(self, modulationPhaseShift: float):
        self.__modulationPhaseShift = modulationPhaseShift
