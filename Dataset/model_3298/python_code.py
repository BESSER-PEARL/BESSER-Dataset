from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Infector:

    pass
class standard_StandardInfector(Infector):

    pass
class SIInfector:

    pass
class standard_SIRInoculator(SIInfector):

    def __init__(self, inoculatedPercentage: float, inoculatePercentage: bool):
        self.inoculatedPercentage = inoculatedPercentage
        self.inoculatePercentage = inoculatePercentage
        
        pass
    @property
    def inoculatedPercentage(self):
        return self.__inoculatedPercentage

    @inoculatedPercentage.setter
    def inoculatedPercentage(self, inoculatedPercentage: float):
        self.__inoculatedPercentage = inoculatedPercentage


    @property
    def inoculatePercentage(self):
        return self.__inoculatePercentage

    @inoculatePercentage.setter
    def inoculatePercentage(self, inoculatePercentage: bool):
        self.__inoculatePercentage = inoculatePercentage


class StochasticDiseaseModel:

    pass
class standard_StandardStochasticDiseaseModel(StochasticDiseaseModel):

    def __init__(self, gain: float):
        self.gain = gain
        
        pass
    @property
    def gain(self):
        return self.__gain

    @gain.setter
    def gain(self, gain: float):
        self.__gain = gain


    def computeNoise(self) :
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
class standard_IntegrationDecorator(ABC):

    def __init__(self):
        
        pass
    def isDeterministic(self) :
        # TODO: Implement isDeterministic method
        pass

class standard_IntegrationLabelValue(ABC):

    pass
class standard_IntegrationLabel(ABC):

    pass
class standard_SanityChecker(ABC):

    pass
class StandardStochasticDiseaseModel:

    pass
class StandardDiseaseModelLabelValue:

    pass
class DiseaseModelState:

    pass
class standard_AggregatingDiseaseModelState(DiseaseModelState):

    pass
class standard_StandardDiseaseModelState(DiseaseModelState):

    def __init__(self, areaRatio: float):
        self.areaRatio = areaRatio
        
        pass
    @property
    def areaRatio(self):
        return self.__areaRatio

    @areaRatio.setter
    def areaRatio(self, areaRatio: float):
        self.__areaRatio = areaRatio


class DiseaseModelLabelValue:

    pass
class standard_StandardDiseaseModelLabelValue(DiseaseModelLabelValue):

    def __init__(self, s: float):
        self.s = s
        
        pass
    @property
    def s(self):
        return self.__s

    @s.setter
    def s(self, s: float):
        self.__s = s


class IntegrationLabel:

    pass
class DiseaseModelLabel:

    pass
class standard_StandardDiseaseModelLabel(IntegrationLabel, DiseaseModelLabel):

    pass
class IntegrationDecorator:

    pass
class DiseaseModel:

    pass
class standard_StochasticDiseaseModel(DiseaseModel):

    def __init__(self, seed: str, randomGenerator: str):
        self.seed = seed
        self.randomGenerator = randomGenerator
        
        pass
    @property
    def randomGenerator(self):
        return self.__randomGenerator

    @randomGenerator.setter
    def randomGenerator(self, randomGenerator: str):
        self.__randomGenerator = randomGenerator


    @property
    def seed(self):
        return self.__seed

    @seed.setter
    def seed(self, seed: str):
        self.__seed = seed


class SILabelValue:

    pass
class standard_SIRLabelValue(SILabelValue):

    def __init__(self, r: float, standard_SIRLabelValue: "standard_SIRLabel" = None, standard_SIRLabelValue38: "standard_SIRLabel" = None, standard_SIRLabelValue41: "standard_SIRLabel" = None, standard_SIRLabelValue44: "standard_SIRLabel" = None, standard_SIRLabelValue47: "standard_SIRLabel" = None):
        self.r = r
        self.standard_SIRLabelValue = standard_SIRLabelValue
        self.standard_SIRLabelValue38 = standard_SIRLabelValue38
        self.standard_SIRLabelValue41 = standard_SIRLabelValue41
        self.standard_SIRLabelValue44 = standard_SIRLabelValue44
        self.standard_SIRLabelValue47 = standard_SIRLabelValue47
        
        pass
    @property
    def r(self):
        return self.__r

    @r.setter
    def r(self, r: float):
        self.__r = r


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

class standard_SILabelValue(StandardDiseaseModelLabelValue):

    def __init__(self, i: float, standard_SILabelValue: "standard_SILabel" = None, standard_SILabelValue25: "standard_SILabel" = None, standard_SILabelValue28: "standard_SILabel" = None, standard_SILabelValue31: "standard_SILabel" = None, standard_SILabelValue34: "standard_SILabel" = None):
        self.i = i
        self.standard_SILabelValue = standard_SILabelValue
        self.standard_SILabelValue25 = standard_SILabelValue25
        self.standard_SILabelValue28 = standard_SILabelValue28
        self.standard_SILabelValue31 = standard_SILabelValue31
        self.standard_SILabelValue34 = standard_SILabelValue34
        
        pass
    @property
    def i(self):
        return self.__i

    @i.setter
    def i(self, i: float):
        self.__i = i


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

class StandardInfector:

    pass
class standard_SIInfector(StandardInfector):

    def __init__(self, infectiousCount: float):
        self.infectiousCount = infectiousCount
        
        pass
    @property
    def infectiousCount(self):
        return self.__infectiousCount

    @infectiousCount.setter
    def infectiousCount(self, infectiousCount: float):
        self.__infectiousCount = infectiousCount


class StandardDiseaseModelState:

    pass
class standard_SIDiseaseModelState(StandardDiseaseModelState):

    pass
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
        
        pass
    @property
    def recoveryRate(self):
        return self.__recoveryRate

    @recoveryRate.setter
    def recoveryRate(self, recoveryRate: float):
        self.__recoveryRate = recoveryRate


    @property
    def characteristicMixingDistance(self):
        return self.__characteristicMixingDistance

    @characteristicMixingDistance.setter
    def characteristicMixingDistance(self, characteristicMixingDistance: float):
        self.__characteristicMixingDistance = characteristicMixingDistance


    @property
    def infectiousMortality(self):
        return self.__infectiousMortality

    @infectiousMortality.setter
    def infectiousMortality(self, infectiousMortality: float):
        self.__infectiousMortality = infectiousMortality


    @property
    def transmissionRate(self):
        return self.__transmissionRate

    @transmissionRate.setter
    def transmissionRate(self, transmissionRate: float):
        self.__transmissionRate = transmissionRate


    @property
    def nonLinearityCoefficient(self):
        return self.__nonLinearityCoefficient

    @nonLinearityCoefficient.setter
    def nonLinearityCoefficient(self, nonLinearityCoefficient: float):
        self.__nonLinearityCoefficient = nonLinearityCoefficient


    @property
    def roadNetworkInfectiousProportion(self):
        return self.__roadNetworkInfectiousProportion

    @roadNetworkInfectiousProportion.setter
    def roadNetworkInfectiousProportion(self, roadNetworkInfectiousProportion: float):
        self.__roadNetworkInfectiousProportion = roadNetworkInfectiousProportion


    @property
    def physicallyAdjacentInfectiousProportion(self):
        return self.__physicallyAdjacentInfectiousProportion

    @physicallyAdjacentInfectiousProportion.setter
    def physicallyAdjacentInfectiousProportion(self, physicallyAdjacentInfectiousProportion: float):
        self.__physicallyAdjacentInfectiousProportion = physicallyAdjacentInfectiousProportion


    @property
    def infectiousMortalityRate(self):
        return self.__infectiousMortalityRate

    @infectiousMortalityRate.setter
    def infectiousMortalityRate(self, infectiousMortalityRate: float):
        self.__infectiousMortalityRate = infectiousMortalityRate


    def getAdjustedTransmissionRate(self, standard_timeDelta) :
        # TODO: Implement getAdjustedTransmissionRate method
        pass

    def getEffectiveInfectious(self, standard_diseaseLabel, standard_onsiteInfectious, standard_node) :
        # TODO: Implement getEffectiveInfectious method
        pass

    def getAdjustedRecoveryRate(self, standard_timeDelta) :
        # TODO: Implement getAdjustedRecoveryRate method
        pass

    def getNormalizedEffectiveInfectious(self, standard_onsiteInfectious, standard_node, standard_diseaseLabel) :
        # TODO: Implement getNormalizedEffectiveInfectious method
        pass

    def getAdjustedInfectiousMortalityRate(self, standard_timeDelta) :
        # TODO: Implement getAdjustedInfectiousMortalityRate method
        pass

class SIRLabelValue:

    pass
class standard_PopulationModelLabel:

    pass
class standard_SEIRLabelValue(SIRLabelValue):

    def __init__(self, e: float, standard_SEIRLabelValue: "standard_SEIRLabel" = None, standard_SEIRLabelValue12: "standard_SEIRLabel" = None, standard_SEIRLabelValue15: "standard_SEIRLabel" = None, standard_SEIRLabelValue21: "standard_SEIRLabel" = None, standard_SEIRLabelValue18: "standard_SEIRLabel" = None):
        self.e = e
        self.standard_SEIRLabelValue = standard_SEIRLabelValue
        self.standard_SEIRLabelValue12 = standard_SEIRLabelValue12
        self.standard_SEIRLabelValue15 = standard_SEIRLabelValue15
        self.standard_SEIRLabelValue21 = standard_SEIRLabelValue21
        self.standard_SEIRLabelValue18 = standard_SEIRLabelValue18
        
        pass
    @property
    def e(self):
        return self.__e

    @e.setter
    def e(self, e: float):
        self.__e = e


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

class StandardDiseaseModelLabel:

    pass
class standard_SIRLabel(StandardDiseaseModelLabel):

    pass
class standard_SILabel(StandardDiseaseModelLabel):

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
        
        pass
    @property
    def totalArea(self):
        return self.__totalArea

    @totalArea.setter
    def totalArea(self, totalArea: float):
        self.__totalArea = totalArea


    @property
    def referencePopulationDensity(self):
        return self.__referencePopulationDensity

    @referencePopulationDensity.setter
    def referencePopulationDensity(self, referencePopulationDensity: float):
        self.__referencePopulationDensity = referencePopulationDensity


    @property
    def totalPopulationCountReciprocal(self):
        return self.__totalPopulationCountReciprocal

    @totalPopulationCountReciprocal.setter
    def totalPopulationCountReciprocal(self, totalPopulationCountReciprocal: float):
        self.__totalPopulationCountReciprocal = totalPopulationCountReciprocal


    @property
    def totalPopulationCount(self):
        return self.__totalPopulationCount

    @totalPopulationCount.setter
    def totalPopulationCount(self, totalPopulationCount: float):
        self.__totalPopulationCount = totalPopulationCount


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

    def computeTotalPopulationCountReciprocal(self) :
        # TODO: Implement computeTotalPopulationCountReciprocal method
        pass

    def doModelSpecificAdjustments(self, standard_label):
        # TODO: Implement doModelSpecificAdjustments method
        pass

    def addToTotalPopulationCount(self, standard_populationCount):
        # TODO: Implement addToTotalPopulationCount method
        pass

    def calculateDelta(self, standard_time, standard_timeDelta, standard_labels):
        # TODO: Implement calculateDelta method
        pass

    def addToTotalArea(self, standard_area):
        # TODO: Implement addToTotalArea method
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
        
        pass
    @property
    def incidence(self):
        return self.__incidence

    @incidence.setter
    def incidence(self, incidence: float):
        self.__incidence = incidence


    @property
    def diseaseDeaths(self):
        return self.__diseaseDeaths

    @diseaseDeaths.setter
    def diseaseDeaths(self, diseaseDeaths: float):
        self.__diseaseDeaths = diseaseDeaths


    @property
    def populationCount(self):
        return self.__populationCount

    @populationCount.setter
    def populationCount(self, populationCount: float):
        self.__populationCount = populationCount


    def add(self, standard_value) :
        # TODO: Implement add method
        pass

    def set(self, standard_value) :
        # TODO: Implement set method
        pass

    def sub(self, standard_value) :
        # TODO: Implement sub method
        pass

    def scale(self, standard_scaleFactor) :
        # TODO: Implement scale method
        pass

    def zeroOutPopulationCount(self):
        # TODO: Implement zeroOutPopulationCount method
        pass

class standard_DiseaseModelState(ABC):

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
class standard_Infector(Modifiable, NodeDecorator):

    def __init__(self, targetURI: str, diseaseName: str, targetISOKey: str, populationIdentifier: str, infectPercentage: bool, standard_Infector: "standard_StandardDiseaseModel" = None, standard_Infector7: set["standard_DiseaseModelLabel"] = None, standard_Infector51: "standard_InfectorInoculatorCollection" = None):
        self.targetURI = targetURI
        self.diseaseName = diseaseName
        self.targetISOKey = targetISOKey
        self.populationIdentifier = populationIdentifier
        self.infectPercentage = infectPercentage
        self.standard_Infector = standard_Infector
        self.standard_Infector7 = standard_Infector7 if standard_Infector7 is not None else set()
        self.standard_Infector51 = standard_Infector51
        
        pass
    @property
    def populationIdentifier(self):
        return self.__populationIdentifier

    @populationIdentifier.setter
    def populationIdentifier(self, populationIdentifier: str):
        self.__populationIdentifier = populationIdentifier


    @property
    def targetURI(self):
        return self.__targetURI

    @targetURI.setter
    def targetURI(self, targetURI: str):
        self.__targetURI = targetURI


    @property
    def diseaseName(self):
        return self.__diseaseName

    @diseaseName.setter
    def diseaseName(self, diseaseName: str):
        self.__diseaseName = diseaseName


    @property
    def infectPercentage(self):
        return self.__infectPercentage

    @infectPercentage.setter
    def infectPercentage(self, infectPercentage: bool):
        self.__infectPercentage = infectPercentage


    @property
    def targetISOKey(self):
        return self.__targetISOKey

    @targetISOKey.setter
    def targetISOKey(self, targetISOKey: str):
        self.__targetISOKey = targetISOKey


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
        
        pass
    @property
    def importFolder(self):
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
                    

class standard_DiseaseModel(SanityChecker, NodeDecorator, Modifiable):

    def __init__(self, backgroundMortalityRate: float, populationIdentifier: str, timePeriod: str, diseaseName: str, relativeTolerance: float, finiteDifference: bool, frequencyDependent: bool, backgroundBirthRate: float):
        self.backgroundMortalityRate = backgroundMortalityRate
        self.populationIdentifier = populationIdentifier
        self.timePeriod = timePeriod
        self.diseaseName = diseaseName
        self.relativeTolerance = relativeTolerance
        self.finiteDifference = finiteDifference
        self.frequencyDependent = frequencyDependent
        self.backgroundBirthRate = backgroundBirthRate
        
        pass
    @property
    def diseaseName(self):
        return self.__diseaseName

    @diseaseName.setter
    def diseaseName(self, diseaseName: str):
        self.__diseaseName = diseaseName


    @property
    def backgroundMortalityRate(self):
        return self.__backgroundMortalityRate

    @backgroundMortalityRate.setter
    def backgroundMortalityRate(self, backgroundMortalityRate: float):
        self.__backgroundMortalityRate = backgroundMortalityRate


    @property
    def relativeTolerance(self):
        return self.__relativeTolerance

    @relativeTolerance.setter
    def relativeTolerance(self, relativeTolerance: float):
        self.__relativeTolerance = relativeTolerance


    @property
    def finiteDifference(self):
        return self.__finiteDifference

    @finiteDifference.setter
    def finiteDifference(self, finiteDifference: bool):
        self.__finiteDifference = finiteDifference


    @property
    def backgroundBirthRate(self):
        return self.__backgroundBirthRate

    @backgroundBirthRate.setter
    def backgroundBirthRate(self, backgroundBirthRate: float):
        self.__backgroundBirthRate = backgroundBirthRate


    @property
    def frequencyDependent(self):
        return self.__frequencyDependent

    @frequencyDependent.setter
    def frequencyDependent(self, frequencyDependent: bool):
        self.__frequencyDependent = frequencyDependent


    @property
    def timePeriod(self):
        return self.__timePeriod

    @timePeriod.setter
    def timePeriod(self, timePeriod: str):
        self.__timePeriod = timePeriod


    @property
    def populationIdentifier(self):
        return self.__populationIdentifier

    @populationIdentifier.setter
    def populationIdentifier(self, populationIdentifier: str):
        self.__populationIdentifier = populationIdentifier


    def initializeDiseaseState(self, standard_diseaseModelLabel):
        # TODO: Implement initializeDiseaseState method
        pass

    def createDiseaseModelLabel(self) :
        # TODO: Implement createDiseaseModelLabel method
        pass

    def getAdjustedBackgroundMortalityRate(self, standard_timeDelta) :
        # TODO: Implement getAdjustedBackgroundMortalityRate method
        pass

    def createDiseaseModelLabelValue(self) :
        # TODO: Implement createDiseaseModelLabelValue method
        pass

    def getAdjustedBackgroundBirthRate(self, standard_timeDelta) :
        # TODO: Implement getAdjustedBackgroundBirthRate method
        pass

    def createInfector(self) :
        # TODO: Implement createInfector method
        pass

    def createDiseaseModelState(self) :
        # TODO: Implement createDiseaseModelState method
        pass

class SIR:

    pass
class standard_StochasticPoissonSIRDiseaseModel(SIR):

    pass
class standard_StochasticSIRDiseaseModel(SIR, StandardStochasticDiseaseModel):

    pass
class standard_SEIR(SIR):

    def __init__(self, incubationRate: float):
        self.incubationRate = incubationRate
        
        pass
    @property
    def incubationRate(self):
        return self.__incubationRate

    @incubationRate.setter
    def incubationRate(self, incubationRate: float):
        self.__incubationRate = incubationRate


    def getAdjustedIncubationRate(self, standard_timeDelta) :
        # TODO: Implement getAdjustedIncubationRate method
        pass

class standard_DeterministicSIRDiseaseModel(SIR):

    pass
class SI:

    pass
class standard_SIR(SI):

    def __init__(self, immunityLossRate: float):
        self.immunityLossRate = immunityLossRate
        
        pass
    @property
    def immunityLossRate(self):
        return self.__immunityLossRate

    @immunityLossRate.setter
    def immunityLossRate(self, immunityLossRate: float):
        self.__immunityLossRate = immunityLossRate


    def getAdjustedImmunityLossRate(self, standard_timeDelta) :
        # TODO: Implement getAdjustedImmunityLossRate method
        pass

class standard_StochasticSIDiseaseModel(SI, StandardStochasticDiseaseModel):

    pass
class standard_AggregatingSIDiseaseModel(SI):

    pass
class standard_StochasticPoissonSIDiseaseModel(SI):

    pass
class standard_DeterministicSIDiseaseModel(SI):

    pass
class SEIR:

    pass
class standard_StochasticSEIRDiseaseModel(SEIR, StandardStochasticDiseaseModel):

    pass
class standard_StochasticPoissonSEIRDiseaseModel(SEIR):

    pass
class standard_DeterministicSEIRDiseaseModel(SEIR):

    pass