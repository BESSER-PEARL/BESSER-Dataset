from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class standard_IntegrationDecorator(ABC):

    def __init__(self):
        
    def isDeterministic(self) -> bool:
        # TODO: Implement isDeterministic method
        pass

class standard_IntegrationLabelValue(ABC):

    pass
class standard_IntegrationLabel(ABC):

    pass
class SIInfector:

    pass
class standard_SIRInoculator(SIInfector):

    def __init__(self, inoculatedPercentage: float, inoculatePercentage: bool):
        self.inoculatedPercentage = inoculatedPercentage
        self.inoculatePercentage = inoculatePercentage
        
    @property
    def inoculatedPercentage(self) -> float:
        return self.__inoculatedPercentage

    @inoculatedPercentage.setter
    def inoculatedPercentage(self, inoculatedPercentage: float):
        self.__inoculatedPercentage = inoculatedPercentage

    @property
    def inoculatePercentage(self) -> bool:
        return self.__inoculatePercentage

    @inoculatePercentage.setter
    def inoculatePercentage(self, inoculatePercentage: bool):
        self.__inoculatePercentage = inoculatePercentage

class StochasticDiseaseModel:

    pass
class standard_StandardStochasticDiseaseModel(StochasticDiseaseModel):

    def __init__(self, gain: float):
        self.gain = gain
        
    @property
    def gain(self) -> float:
        return self.__gain

    @gain.setter
    def gain(self, gain: float):
        self.__gain = gain

    def computeNoise(self) -> float:
        # TODO: Implement computeNoise method
        pass

class AggregatingSIDiseaseModel:

    pass
class standard_AggregatingSIRDiseaseModel(AggregatingSIDiseaseModel):

    pass
class AggregatingSIRDiseaseModel:

    pass
class standard_AggregatingSEIRDiseaseModel(AggregatingSIRDiseaseModel):

    pass
class standard_SanityChecker(ABC):

    pass
class StandardStochasticDiseaseModel:

    pass
class Infector:

    pass
class standard_StandardInfector(Infector):

    pass
class DiseaseModelState:

    pass
class standard_AggregatingDiseaseModelState(DiseaseModelState):

    pass
class standard_StandardDiseaseModelState(DiseaseModelState):

    def __init__(self, areaRatio: float):
        self.areaRatio = areaRatio
        
    @property
    def areaRatio(self) -> float:
        return self.__areaRatio

    @areaRatio.setter
    def areaRatio(self, areaRatio: float):
        self.__areaRatio = areaRatio

class DiseaseModelLabelValue:

    pass
class standard_StandardDiseaseModelLabelValue(DiseaseModelLabelValue):

    def __init__(self, s: float):
        self.s = s
        
    @property
    def s(self) -> float:
        return self.__s

    @s.setter
    def s(self, s: float):
        self.__s = s

class IntegrationLabel:

    pass
class DiseaseModelLabel:

    pass
class standard_StandardDiseaseModelLabel(DiseaseModelLabel, IntegrationLabel):

    pass
class IntegrationDecorator:

    pass
class DiseaseModel:

    pass
class standard_StochasticDiseaseModel(DiseaseModel):

    def __init__(self, seed: str, randomGenerator: str):
        self.seed = seed
        self.randomGenerator = randomGenerator
        
    @property
    def seed(self) -> str:
        return self.__seed

    @seed.setter
    def seed(self, seed: str):
        self.__seed = seed

    @property
    def randomGenerator(self) -> str:
        return self.__randomGenerator

    @randomGenerator.setter
    def randomGenerator(self, randomGenerator: str):
        self.__randomGenerator = randomGenerator

class SILabelValue:

    pass
class standard_SIRLabelValue(SILabelValue):

    def __init__(self, r: float, standard_SIRLabelValue47: "standard_SIRLabel" = None, standard_SIRLabelValue: "standard_SIRLabel" = None, standard_SIRLabelValue38: "standard_SIRLabel" = None, standard_SIRLabelValue41: "standard_SIRLabel" = None, standard_SIRLabelValue44: "standard_SIRLabel" = None):
        self.r = r
        self.standard_SIRLabelValue47 = standard_SIRLabelValue47
        self.standard_SIRLabelValue = standard_SIRLabelValue
        self.standard_SIRLabelValue38 = standard_SIRLabelValue38
        self.standard_SIRLabelValue41 = standard_SIRLabelValue41
        self.standard_SIRLabelValue44 = standard_SIRLabelValue44
        
    @property
    def r(self) -> float:
        return self.__r

    @r.setter
    def r(self, r: float):
        self.__r = r

    @property
    def standard_SIRLabelValue38(self):
        return self.__standard_SIRLabelValue38

    @standard_SIRLabelValue38.setter
    def standard_SIRLabelValue38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_standard_SIRLabelValue__standard_SIRLabelValue38", None)
        self.__standard_SIRLabelValue38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "standard_SIRLabel37"):
                opp_val = getattr(old_value, "standard_SIRLabel37", None)
                if opp_val == self:
                    setattr(old_value, "standard_SIRLabel37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "standard_SIRLabel37"):
                opp_val = getattr(value, "standard_SIRLabel37", None)
                setattr(value, "standard_SIRLabel37", self)

    @property
    def standard_SIRLabelValue44(self):
        return self.__standard_SIRLabelValue44

    @standard_SIRLabelValue44.setter
    def standard_SIRLabelValue44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_standard_SIRLabelValue__standard_SIRLabelValue44", None)
        self.__standard_SIRLabelValue44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "standard_SIRLabel43"):
                opp_val = getattr(old_value, "standard_SIRLabel43", None)
                if opp_val == self:
                    setattr(old_value, "standard_SIRLabel43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "standard_SIRLabel43"):
                opp_val = getattr(value, "standard_SIRLabel43", None)
                setattr(value, "standard_SIRLabel43", self)

    @property
    def standard_SIRLabelValue41(self):
        return self.__standard_SIRLabelValue41

    @standard_SIRLabelValue41.setter
    def standard_SIRLabelValue41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_standard_SIRLabelValue__standard_SIRLabelValue41", None)
        self.__standard_SIRLabelValue41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "standard_SIRLabel40"):
                opp_val = getattr(old_value, "standard_SIRLabel40", None)
                if opp_val == self:
                    setattr(old_value, "standard_SIRLabel40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "standard_SIRLabel40"):
                opp_val = getattr(value, "standard_SIRLabel40", None)
                setattr(value, "standard_SIRLabel40", self)

    @property
    def standard_SIRLabelValue(self):
        return self.__standard_SIRLabelValue

    @standard_SIRLabelValue.setter
    def standard_SIRLabelValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_standard_SIRLabelValue__standard_SIRLabelValue", None)
        self.__standard_SIRLabelValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "standard_SIRLabel"):
                opp_val = getattr(old_value, "standard_SIRLabel", None)
                if opp_val == self:
                    setattr(old_value, "standard_SIRLabel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "standard_SIRLabel"):
                opp_val = getattr(value, "standard_SIRLabel", None)
                setattr(value, "standard_SIRLabel", self)

    @property
    def standard_SIRLabelValue47(self):
        return self.__standard_SIRLabelValue47

    @standard_SIRLabelValue47.setter
    def standard_SIRLabelValue47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_standard_SIRLabelValue__standard_SIRLabelValue47", None)
        self.__standard_SIRLabelValue47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "standard_SIRLabel46"):
                opp_val = getattr(old_value, "standard_SIRLabel46", None)
                if opp_val == self:
                    setattr(old_value, "standard_SIRLabel46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "standard_SIRLabel46"):
                opp_val = getattr(value, "standard_SIRLabel46", None)
                setattr(value, "standard_SIRLabel46", self)

class StandardDiseaseModel:

    pass
class standard_SI(StandardDiseaseModel):

    def __init__(self, transmissionRate: float, nonLinearityCoefficient: float, recoveryRate: float, infectiousMortalityRate: float, physicallyAdjacentInfectiousProportion: float, roadNetworkInfectiousProportion: float, infectiousMortality: float, characteristicMixingDistance: float):
        self.transmissionRate = transmissionRate
        self.nonLinearityCoefficient = nonLinearityCoefficient
        self.recoveryRate = recoveryRate
        self.infectiousMortalityRate = infectiousMortalityRate
        self.physicallyAdjacentInfectiousProportion = physicallyAdjacentInfectiousProportion
        self.roadNetworkInfectiousProportion = roadNetworkInfectiousProportion
        self.infectiousMortality = infectiousMortality
        self.characteristicMixingDistance = characteristicMixingDistance
        
    @property
    def transmissionRate(self) -> float:
        return self.__transmissionRate

    @transmissionRate.setter
    def transmissionRate(self, transmissionRate: float):
        self.__transmissionRate = transmissionRate

    @property
    def nonLinearityCoefficient(self) -> float:
        return self.__nonLinearityCoefficient

    @nonLinearityCoefficient.setter
    def nonLinearityCoefficient(self, nonLinearityCoefficient: float):
        self.__nonLinearityCoefficient = nonLinearityCoefficient

    @property
    def infectiousMortalityRate(self) -> float:
        return self.__infectiousMortalityRate

    @infectiousMortalityRate.setter
    def infectiousMortalityRate(self, infectiousMortalityRate: float):
        self.__infectiousMortalityRate = infectiousMortalityRate

    @property
    def infectiousMortality(self) -> float:
        return self.__infectiousMortality

    @infectiousMortality.setter
    def infectiousMortality(self, infectiousMortality: float):
        self.__infectiousMortality = infectiousMortality

    @property
    def characteristicMixingDistance(self) -> float:
        return self.__characteristicMixingDistance

    @characteristicMixingDistance.setter
    def characteristicMixingDistance(self, characteristicMixingDistance: float):
        self.__characteristicMixingDistance = characteristicMixingDistance

    @property
    def recoveryRate(self) -> float:
        return self.__recoveryRate

    @recoveryRate.setter
    def recoveryRate(self, recoveryRate: float):
        self.__recoveryRate = recoveryRate

    @property
    def roadNetworkInfectiousProportion(self) -> float:
        return self.__roadNetworkInfectiousProportion

    @roadNetworkInfectiousProportion.setter
    def roadNetworkInfectiousProportion(self, roadNetworkInfectiousProportion: float):
        self.__roadNetworkInfectiousProportion = roadNetworkInfectiousProportion

    @property
    def physicallyAdjacentInfectiousProportion(self) -> float:
        return self.__physicallyAdjacentInfectiousProportion

    @physicallyAdjacentInfectiousProportion.setter
    def physicallyAdjacentInfectiousProportion(self, physicallyAdjacentInfectiousProportion: float):
        self.__physicallyAdjacentInfectiousProportion = physicallyAdjacentInfectiousProportion

    def getAdjustedInfectiousMortalityRate(self, timeDelta: str) -> float:
        # TODO: Implement getAdjustedInfectiousMortalityRate method
        pass

    def getAdjustedTransmissionRate(self, timeDelta: str) -> float:
        # TODO: Implement getAdjustedTransmissionRate method
        pass

    def getNormalizedEffectiveInfectious(self, diseaseLabel: StandardDiseaseModelLabel, onsiteInfectious: float, node: str) -> float:
        # TODO: Implement getNormalizedEffectiveInfectious method
        pass

    def getAdjustedRecoveryRate(self, timeDelta: str) -> float:
        # TODO: Implement getAdjustedRecoveryRate method
        pass

    def getEffectiveInfectious(self, diseaseLabel: StandardDiseaseModelLabel, onsiteInfectious: float, node: str) -> float:
        # TODO: Implement getEffectiveInfectious method
        pass

class SIRLabelValue:

    pass
class StandardDiseaseModelLabelValue:

    pass
class standard_SILabelValue(StandardDiseaseModelLabelValue):

    def __init__(self, i: float, standard_SILabelValue: "standard_SILabel" = None, standard_SILabelValue25: "standard_SILabel" = None, standard_SILabelValue28: "standard_SILabel" = None, standard_SILabelValue31: "standard_SILabel" = None, standard_SILabelValue34: "standard_SILabel" = None):
        self.i = i
        self.standard_SILabelValue = standard_SILabelValue
        self.standard_SILabelValue25 = standard_SILabelValue25
        self.standard_SILabelValue28 = standard_SILabelValue28
        self.standard_SILabelValue31 = standard_SILabelValue31
        self.standard_SILabelValue34 = standard_SILabelValue34
        
    @property
    def i(self) -> float:
        return self.__i

    @i.setter
    def i(self, i: float):
        self.__i = i

    @property
    def standard_SILabelValue34(self):
        return self.__standard_SILabelValue34

    @standard_SILabelValue34.setter
    def standard_SILabelValue34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_standard_SILabelValue__standard_SILabelValue34", None)
        self.__standard_SILabelValue34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "standard_SILabel33"):
                opp_val = getattr(old_value, "standard_SILabel33", None)
                if opp_val == self:
                    setattr(old_value, "standard_SILabel33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "standard_SILabel33"):
                opp_val = getattr(value, "standard_SILabel33", None)
                setattr(value, "standard_SILabel33", self)

    @property
    def standard_SILabelValue25(self):
        return self.__standard_SILabelValue25

    @standard_SILabelValue25.setter
    def standard_SILabelValue25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_standard_SILabelValue__standard_SILabelValue25", None)
        self.__standard_SILabelValue25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "standard_SILabel24"):
                opp_val = getattr(old_value, "standard_SILabel24", None)
                if opp_val == self:
                    setattr(old_value, "standard_SILabel24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "standard_SILabel24"):
                opp_val = getattr(value, "standard_SILabel24", None)
                setattr(value, "standard_SILabel24", self)

    @property
    def standard_SILabelValue31(self):
        return self.__standard_SILabelValue31

    @standard_SILabelValue31.setter
    def standard_SILabelValue31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_standard_SILabelValue__standard_SILabelValue31", None)
        self.__standard_SILabelValue31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "standard_SILabel30"):
                opp_val = getattr(old_value, "standard_SILabel30", None)
                if opp_val == self:
                    setattr(old_value, "standard_SILabel30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "standard_SILabel30"):
                opp_val = getattr(value, "standard_SILabel30", None)
                setattr(value, "standard_SILabel30", self)

    @property
    def standard_SILabelValue(self):
        return self.__standard_SILabelValue

    @standard_SILabelValue.setter
    def standard_SILabelValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_standard_SILabelValue__standard_SILabelValue", None)
        self.__standard_SILabelValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "standard_SILabel"):
                opp_val = getattr(old_value, "standard_SILabel", None)
                if opp_val == self:
                    setattr(old_value, "standard_SILabel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "standard_SILabel"):
                opp_val = getattr(value, "standard_SILabel", None)
                setattr(value, "standard_SILabel", self)

    @property
    def standard_SILabelValue28(self):
        return self.__standard_SILabelValue28

    @standard_SILabelValue28.setter
    def standard_SILabelValue28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_standard_SILabelValue__standard_SILabelValue28", None)
        self.__standard_SILabelValue28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "standard_SILabel27"):
                opp_val = getattr(old_value, "standard_SILabel27", None)
                if opp_val == self:
                    setattr(old_value, "standard_SILabel27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "standard_SILabel27"):
                opp_val = getattr(value, "standard_SILabel27", None)
                setattr(value, "standard_SILabel27", self)

class StandardInfector:

    pass
class standard_SIInfector(StandardInfector):

    def __init__(self, infectiousCount: float):
        self.infectiousCount = infectiousCount
        
    @property
    def infectiousCount(self) -> float:
        return self.__infectiousCount

    @infectiousCount.setter
    def infectiousCount(self, infectiousCount: float):
        self.__infectiousCount = infectiousCount

class StandardDiseaseModelState:

    pass
class standard_SIDiseaseModelState(StandardDiseaseModelState):

    pass
class IntegrationLabelValue:

    pass
class LabelValue:

    pass
class standard_DiseaseModelLabelValue(IntegrationLabelValue, LabelValue):

    def __init__(self, diseaseDeaths: float, populationCount: float, incidence: float):
        self.diseaseDeaths = diseaseDeaths
        self.populationCount = populationCount
        self.incidence = incidence
        
    @property
    def incidence(self) -> float:
        return self.__incidence

    @incidence.setter
    def incidence(self, incidence: float):
        self.__incidence = incidence

    @property
    def diseaseDeaths(self) -> float:
        return self.__diseaseDeaths

    @diseaseDeaths.setter
    def diseaseDeaths(self, diseaseDeaths: float):
        self.__diseaseDeaths = diseaseDeaths

    @property
    def populationCount(self) -> float:
        return self.__populationCount

    @populationCount.setter
    def populationCount(self, populationCount: float):
        self.__populationCount = populationCount

    def sub(self, value: str) -> str:
        # TODO: Implement sub method
        pass

    def zeroOutPopulationCount(self):
        # TODO: Implement zeroOutPopulationCount method
        pass

    def add(self, value: str) -> str:
        # TODO: Implement add method
        pass

    def scale(self, scaleFactor: float) -> str:
        # TODO: Implement scale method
        pass

    def set(self, value: str) -> str:
        # TODO: Implement set method
        pass

class standard_PopulationModelLabel:

    pass
class standard_DiseaseModelState(ABC):

    pass
class standard_SEIRLabelValue(SIRLabelValue):

    def __init__(self, e: float, standard_SEIRLabelValue: "standard_SEIRLabel" = None, standard_SEIRLabelValue12: "standard_SEIRLabel" = None, standard_SEIRLabelValue15: "standard_SEIRLabel" = None, standard_SEIRLabelValue18: "standard_SEIRLabel" = None, standard_SEIRLabelValue21: "standard_SEIRLabel" = None):
        self.e = e
        self.standard_SEIRLabelValue = standard_SEIRLabelValue
        self.standard_SEIRLabelValue12 = standard_SEIRLabelValue12
        self.standard_SEIRLabelValue15 = standard_SEIRLabelValue15
        self.standard_SEIRLabelValue18 = standard_SEIRLabelValue18
        self.standard_SEIRLabelValue21 = standard_SEIRLabelValue21
        
    @property
    def e(self) -> float:
        return self.__e

    @e.setter
    def e(self, e: float):
        self.__e = e

    @property
    def standard_SEIRLabelValue15(self):
        return self.__standard_SEIRLabelValue15

    @standard_SEIRLabelValue15.setter
    def standard_SEIRLabelValue15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_standard_SEIRLabelValue__standard_SEIRLabelValue15", None)
        self.__standard_SEIRLabelValue15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "standard_SEIRLabel14"):
                opp_val = getattr(old_value, "standard_SEIRLabel14", None)
                if opp_val == self:
                    setattr(old_value, "standard_SEIRLabel14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "standard_SEIRLabel14"):
                opp_val = getattr(value, "standard_SEIRLabel14", None)
                setattr(value, "standard_SEIRLabel14", self)

    @property
    def standard_SEIRLabelValue(self):
        return self.__standard_SEIRLabelValue

    @standard_SEIRLabelValue.setter
    def standard_SEIRLabelValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_standard_SEIRLabelValue__standard_SEIRLabelValue", None)
        self.__standard_SEIRLabelValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "standard_SEIRLabel"):
                opp_val = getattr(old_value, "standard_SEIRLabel", None)
                if opp_val == self:
                    setattr(old_value, "standard_SEIRLabel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "standard_SEIRLabel"):
                opp_val = getattr(value, "standard_SEIRLabel", None)
                setattr(value, "standard_SEIRLabel", self)

    @property
    def standard_SEIRLabelValue18(self):
        return self.__standard_SEIRLabelValue18

    @standard_SEIRLabelValue18.setter
    def standard_SEIRLabelValue18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_standard_SEIRLabelValue__standard_SEIRLabelValue18", None)
        self.__standard_SEIRLabelValue18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "standard_SEIRLabel17"):
                opp_val = getattr(old_value, "standard_SEIRLabel17", None)
                if opp_val == self:
                    setattr(old_value, "standard_SEIRLabel17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "standard_SEIRLabel17"):
                opp_val = getattr(value, "standard_SEIRLabel17", None)
                setattr(value, "standard_SEIRLabel17", self)

    @property
    def standard_SEIRLabelValue12(self):
        return self.__standard_SEIRLabelValue12

    @standard_SEIRLabelValue12.setter
    def standard_SEIRLabelValue12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_standard_SEIRLabelValue__standard_SEIRLabelValue12", None)
        self.__standard_SEIRLabelValue12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "standard_SEIRLabel11"):
                opp_val = getattr(old_value, "standard_SEIRLabel11", None)
                if opp_val == self:
                    setattr(old_value, "standard_SEIRLabel11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "standard_SEIRLabel11"):
                opp_val = getattr(value, "standard_SEIRLabel11", None)
                setattr(value, "standard_SEIRLabel11", self)

    @property
    def standard_SEIRLabelValue21(self):
        return self.__standard_SEIRLabelValue21

    @standard_SEIRLabelValue21.setter
    def standard_SEIRLabelValue21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_standard_SEIRLabelValue__standard_SEIRLabelValue21", None)
        self.__standard_SEIRLabelValue21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "standard_SEIRLabel20"):
                opp_val = getattr(old_value, "standard_SEIRLabel20", None)
                if opp_val == self:
                    setattr(old_value, "standard_SEIRLabel20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "standard_SEIRLabel20"):
                opp_val = getattr(value, "standard_SEIRLabel20", None)
                setattr(value, "standard_SEIRLabel20", self)

class StandardDiseaseModelLabel:

    pass
class standard_SILabel(StandardDiseaseModelLabel):

    pass
class standard_SIRLabel(StandardDiseaseModelLabel):

    pass
class standard_SEIRLabel(StandardDiseaseModelLabel):

    pass
class standard_StandardDiseaseModel(DiseaseModel, IntegrationDecorator):

    def __init__(self, totalPopulationCount: float, totalPopulationCountReciprocal: float, totalArea: float, referencePopulationDensity: float, standard_StandardDiseaseModel: "standard_Infector" = None):
        self.totalPopulationCount = totalPopulationCount
        self.totalPopulationCountReciprocal = totalPopulationCountReciprocal
        self.totalArea = totalArea
        self.referencePopulationDensity = referencePopulationDensity
        self.standard_StandardDiseaseModel = standard_StandardDiseaseModel
        
    @property
    def totalPopulationCount(self) -> float:
        return self.__totalPopulationCount

    @totalPopulationCount.setter
    def totalPopulationCount(self, totalPopulationCount: float):
        self.__totalPopulationCount = totalPopulationCount

    @property
    def referencePopulationDensity(self) -> float:
        return self.__referencePopulationDensity

    @referencePopulationDensity.setter
    def referencePopulationDensity(self, referencePopulationDensity: float):
        self.__referencePopulationDensity = referencePopulationDensity

    @property
    def totalPopulationCountReciprocal(self) -> float:
        return self.__totalPopulationCountReciprocal

    @totalPopulationCountReciprocal.setter
    def totalPopulationCountReciprocal(self, totalPopulationCountReciprocal: float):
        self.__totalPopulationCountReciprocal = totalPopulationCountReciprocal

    @property
    def totalArea(self) -> float:
        return self.__totalArea

    @totalArea.setter
    def totalArea(self, totalArea: float):
        self.__totalArea = totalArea

    @property
    def standard_StandardDiseaseModel(self):
        return self.__standard_StandardDiseaseModel

    @standard_StandardDiseaseModel.setter
    def standard_StandardDiseaseModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_standard_StandardDiseaseModel__standard_StandardDiseaseModel", None)
        self.__standard_StandardDiseaseModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "standard_Infector"):
                opp_val = getattr(old_value, "standard_Infector", None)
                if opp_val == self:
                    setattr(old_value, "standard_Infector", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "standard_Infector"):
                opp_val = getattr(value, "standard_Infector", None)
                setattr(value, "standard_Infector", self)

    def calculateDelta(self, timeDelta: str, time: str, labels: str):
        # TODO: Implement calculateDelta method
        pass

    def addToTotalPopulationCount(self, populationCount: float):
        # TODO: Implement addToTotalPopulationCount method
        pass

    def doModelSpecificAdjustments(self, label: StandardDiseaseModelLabelValue):
        # TODO: Implement doModelSpecificAdjustments method
        pass

    def addToTotalArea(self, area: float):
        # TODO: Implement addToTotalArea method
        pass

    def computeTotalPopulationCountReciprocal(self) -> float:
        # TODO: Implement computeTotalPopulationCountReciprocal method
        pass

class standard_PopulationLabel:

    pass
class DynamicNodeLabel:

    pass
class standard_DiseaseModelLabel(DynamicNodeLabel):

    pass
class Modifiable:

    pass
class SanityChecker:

    pass
class NodeDecorator:

    pass
class standard_Infector(NodeDecorator, Modifiable):

    def __init__(self, targetURI: str, diseaseName: str, targetISOKey: str, populationIdentifier: str, infectPercentage: bool, standard_Infector: "standard_StandardDiseaseModel" = None, standard_Infector7: set["standard_DiseaseModelLabel"] = None, standard_Infector51: "standard_InfectorInoculatorCollection" = None):
        self.targetURI = targetURI
        self.diseaseName = diseaseName
        self.targetISOKey = targetISOKey
        self.populationIdentifier = populationIdentifier
        self.infectPercentage = infectPercentage
        self.standard_Infector = standard_Infector
        self.standard_Infector7 = standard_Infector7 if standard_Infector7 is not None else set()
        self.standard_Infector51 = standard_Infector51
        
    @property
    def infectPercentage(self) -> bool:
        return self.__infectPercentage

    @infectPercentage.setter
    def infectPercentage(self, infectPercentage: bool):
        self.__infectPercentage = infectPercentage

    @property
    def diseaseName(self) -> str:
        return self.__diseaseName

    @diseaseName.setter
    def diseaseName(self, diseaseName: str):
        self.__diseaseName = diseaseName

    @property
    def targetURI(self) -> str:
        return self.__targetURI

    @targetURI.setter
    def targetURI(self, targetURI: str):
        self.__targetURI = targetURI

    @property
    def targetISOKey(self) -> str:
        return self.__targetISOKey

    @targetISOKey.setter
    def targetISOKey(self, targetISOKey: str):
        self.__targetISOKey = targetISOKey

    @property
    def populationIdentifier(self) -> str:
        return self.__populationIdentifier

    @populationIdentifier.setter
    def populationIdentifier(self, populationIdentifier: str):
        self.__populationIdentifier = populationIdentifier

    @property
    def standard_Infector51(self):
        return self.__standard_Infector51

    @standard_Infector51.setter
    def standard_Infector51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_standard_Infector__standard_Infector51", None)
        self.__standard_Infector51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "standard_InfectorInoculatorCollection"):
                opp_val = getattr(old_value, "standard_InfectorInoculatorCollection", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "standard_InfectorInoculatorCollection"):
                opp_val = getattr(value, "standard_InfectorInoculatorCollection", None)
                if opp_val is None:
                    setattr(value, "standard_InfectorInoculatorCollection", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def standard_Infector7(self):
        return self.__standard_Infector7

    @standard_Infector7.setter
    def standard_Infector7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_standard_Infector__standard_Infector7", None)
        self.__standard_Infector7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "standard_DiseaseModelLabel8"):
                    opp_val = getattr(item, "standard_DiseaseModelLabel8", None)
                    
                    if opp_val == self:
                        setattr(item, "standard_DiseaseModelLabel8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "standard_DiseaseModelLabel8"):
                    opp_val = getattr(item, "standard_DiseaseModelLabel8", None)
                    
                    setattr(item, "standard_DiseaseModelLabel8", self)
                    

    @property
    def standard_Infector(self):
        return self.__standard_Infector

    @standard_Infector.setter
    def standard_Infector(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_standard_Infector__standard_Infector", None)
        self.__standard_Infector = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "standard_StandardDiseaseModel"):
                opp_val = getattr(old_value, "standard_StandardDiseaseModel", None)
                if opp_val == self:
                    setattr(old_value, "standard_StandardDiseaseModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "standard_StandardDiseaseModel"):
                opp_val = getattr(value, "standard_StandardDiseaseModel", None)
                setattr(value, "standard_StandardDiseaseModel", self)

class standard_InfectorInoculatorCollection(NodeDecorator, Modifiable):

    def __init__(self, importFolder: str, standard_InfectorInoculatorCollection: set["standard_Infector"] = None):
        self.importFolder = importFolder
        self.standard_InfectorInoculatorCollection = standard_InfectorInoculatorCollection if standard_InfectorInoculatorCollection is not None else set()
        
    @property
    def importFolder(self) -> str:
        return self.__importFolder

    @importFolder.setter
    def importFolder(self, importFolder: str):
        self.__importFolder = importFolder

    @property
    def standard_InfectorInoculatorCollection(self):
        return self.__standard_InfectorInoculatorCollection

    @standard_InfectorInoculatorCollection.setter
    def standard_InfectorInoculatorCollection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_standard_InfectorInoculatorCollection__standard_InfectorInoculatorCollection", None)
        self.__standard_InfectorInoculatorCollection = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "standard_Infector51"):
                    opp_val = getattr(item, "standard_Infector51", None)
                    
                    if opp_val == self:
                        setattr(item, "standard_Infector51", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "standard_Infector51"):
                    opp_val = getattr(item, "standard_Infector51", None)
                    
                    setattr(item, "standard_Infector51", self)
                    

class standard_DiseaseModel(NodeDecorator, Modifiable, SanityChecker):

    def __init__(self, backgroundMortalityRate: float, populationIdentifier: str, timePeriod: str, diseaseName: str, relativeTolerance: float, finiteDifference: bool, frequencyDependent: bool, backgroundBirthRate: float):
        self.backgroundMortalityRate = backgroundMortalityRate
        self.populationIdentifier = populationIdentifier
        self.timePeriod = timePeriod
        self.diseaseName = diseaseName
        self.relativeTolerance = relativeTolerance
        self.finiteDifference = finiteDifference
        self.frequencyDependent = frequencyDependent
        self.backgroundBirthRate = backgroundBirthRate
        
    @property
    def diseaseName(self) -> str:
        return self.__diseaseName

    @diseaseName.setter
    def diseaseName(self, diseaseName: str):
        self.__diseaseName = diseaseName

    @property
    def timePeriod(self) -> str:
        return self.__timePeriod

    @timePeriod.setter
    def timePeriod(self, timePeriod: str):
        self.__timePeriod = timePeriod

    @property
    def backgroundBirthRate(self) -> float:
        return self.__backgroundBirthRate

    @backgroundBirthRate.setter
    def backgroundBirthRate(self, backgroundBirthRate: float):
        self.__backgroundBirthRate = backgroundBirthRate

    @property
    def populationIdentifier(self) -> str:
        return self.__populationIdentifier

    @populationIdentifier.setter
    def populationIdentifier(self, populationIdentifier: str):
        self.__populationIdentifier = populationIdentifier

    @property
    def finiteDifference(self) -> bool:
        return self.__finiteDifference

    @finiteDifference.setter
    def finiteDifference(self, finiteDifference: bool):
        self.__finiteDifference = finiteDifference

    @property
    def frequencyDependent(self) -> bool:
        return self.__frequencyDependent

    @frequencyDependent.setter
    def frequencyDependent(self, frequencyDependent: bool):
        self.__frequencyDependent = frequencyDependent

    @property
    def backgroundMortalityRate(self) -> float:
        return self.__backgroundMortalityRate

    @backgroundMortalityRate.setter
    def backgroundMortalityRate(self, backgroundMortalityRate: float):
        self.__backgroundMortalityRate = backgroundMortalityRate

    @property
    def relativeTolerance(self) -> float:
        return self.__relativeTolerance

    @relativeTolerance.setter
    def relativeTolerance(self, relativeTolerance: float):
        self.__relativeTolerance = relativeTolerance

    def initializeDiseaseState(self, diseaseModelLabel: str):
        # TODO: Implement initializeDiseaseState method
        pass

    def createInfector(self) -> str:
        # TODO: Implement createInfector method
        pass

    def createDiseaseModelLabelValue(self) -> str:
        # TODO: Implement createDiseaseModelLabelValue method
        pass

    def createDiseaseModelState(self) -> str:
        # TODO: Implement createDiseaseModelState method
        pass

    def initializeDiseaseState(self, diseaseModelLabel: str, diseaseModelState: str) -> str:
        # TODO: Implement initializeDiseaseState method
        pass

    def getAdjustedBackgroundBirthRate(self, timeDelta: str) -> float:
        # TODO: Implement getAdjustedBackgroundBirthRate method
        pass

    def createDiseaseModelLabel(self) -> str:
        # TODO: Implement createDiseaseModelLabel method
        pass

    def getAdjustedBackgroundMortalityRate(self, timeDelta: str) -> float:
        # TODO: Implement getAdjustedBackgroundMortalityRate method
        pass

class SIR:

    pass
class standard_StochasticSIRDiseaseModel(StandardStochasticDiseaseModel, SIR):

    pass
class standard_SEIR(SIR):

    def __init__(self, incubationRate: float):
        self.incubationRate = incubationRate
        
    @property
    def incubationRate(self) -> float:
        return self.__incubationRate

    @incubationRate.setter
    def incubationRate(self, incubationRate: float):
        self.__incubationRate = incubationRate

    def getAdjustedIncubationRate(self, timeDelta: str) -> float:
        # TODO: Implement getAdjustedIncubationRate method
        pass

class standard_StochasticPoissonSIRDiseaseModel(SIR):

    pass
class standard_DeterministicSIRDiseaseModel(SIR):

    pass
class SI:

    pass
class standard_StochasticPoissonSIDiseaseModel(SI):

    pass
class standard_SIR(SI):

    def __init__(self, immunityLossRate: float):
        self.immunityLossRate = immunityLossRate
        
    @property
    def immunityLossRate(self) -> float:
        return self.__immunityLossRate

    @immunityLossRate.setter
    def immunityLossRate(self, immunityLossRate: float):
        self.__immunityLossRate = immunityLossRate

    def getAdjustedImmunityLossRate(self, timeDelta: str) -> float:
        # TODO: Implement getAdjustedImmunityLossRate method
        pass

class standard_StochasticSIDiseaseModel(StandardStochasticDiseaseModel, SI):

    pass
class standard_AggregatingSIDiseaseModel(SI):

    pass
class standard_DeterministicSIDiseaseModel(SI):

    pass
class SEIR:

    pass
class standard_StochasticPoissonSEIRDiseaseModel(SEIR):

    pass
class standard_StochasticSEIRDiseaseModel(StandardStochasticDiseaseModel, SEIR):

    pass
class standard_DeterministicSEIRDiseaseModel(SEIR):

    pass