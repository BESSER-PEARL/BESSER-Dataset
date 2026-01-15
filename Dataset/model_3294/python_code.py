from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class EarthSciencePopulationInitializer:

    pass
class standard_YetiPopulationInitializer(EarthSciencePopulationInitializer):

    pass
class PopulationInitializer:

    pass
class standard_EarthSciencePopulationInitializer(PopulationInitializer):

    pass
class standard_StandardPopulationInitializer(PopulationInitializer):

    def __init__(self, individuals: float, useDensity: bool):
        self.individuals = individuals
        self.useDensity = useDensity
        
    @property
    def useDensity(self) -> bool:
        return self.__useDensity

    @useDensity.setter
    def useDensity(self, useDensity: bool):
        self.__useDensity = useDensity

    @property
    def individuals(self) -> float:
        return self.__individuals

    @individuals.setter
    def individuals(self, individuals: float):
        self.__individuals = individuals

class PopulationModelLabelValue:

    pass
class LabelValue:

    pass
class standard_PopulationModelLabelValue(LabelValue):

    pass
class standard_IntegrationDecorator(ABC):

    pass
class standard_IntegrationLabelValue(ABC):

    pass
class standard_IntegrationLabel(ABC):

    pass
class IntegrationLabel:

    pass
class PopulationModelLabel:

    pass
class standard_StandardPopulationModelLabel(IntegrationLabel, PopulationModelLabel):

    pass
class standard_PopulationLabel:

    pass
class DynamicNodeLabel:

    pass
class standard_PopulationModelLabel(DynamicNodeLabel):

    def __init__(self, populationIdentifier: str, standard_PopulationModelLabel: "standard_PopulationLabel" = None):
        self.populationIdentifier = populationIdentifier
        self.standard_PopulationModelLabel = standard_PopulationModelLabel
        
    @property
    def populationIdentifier(self) -> str:
        return self.__populationIdentifier

    @populationIdentifier.setter
    def populationIdentifier(self, populationIdentifier: str):
        self.__populationIdentifier = populationIdentifier

    @property
    def standard_PopulationModelLabel(self):
        return self.__standard_PopulationModelLabel

    @standard_PopulationModelLabel.setter
    def standard_PopulationModelLabel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_standard_PopulationModelLabel__standard_PopulationModelLabel", None)
        self.__standard_PopulationModelLabel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "standard_PopulationLabel"):
                opp_val = getattr(old_value, "standard_PopulationLabel", None)
                if opp_val == self:
                    setattr(old_value, "standard_PopulationLabel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "standard_PopulationLabel"):
                opp_val = getattr(value, "standard_PopulationLabel", None)
                setattr(value, "standard_PopulationLabel", self)

class IntegrationDecorator:

    pass
class PopulationModel:

    pass
class standard_PopulationGroup:

    def __init__(self, identifier: str, fraction: float, standard_PopulationGroup: "standard_DemographicPopulationModel" = None):
        self.identifier = identifier
        self.fraction = fraction
        self.standard_PopulationGroup = standard_PopulationGroup
        
    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    @property
    def fraction(self) -> float:
        return self.__fraction

    @fraction.setter
    def fraction(self, fraction: float):
        self.__fraction = fraction

    @property
    def standard_PopulationGroup(self):
        return self.__standard_PopulationGroup

    @standard_PopulationGroup.setter
    def standard_PopulationGroup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_standard_PopulationGroup__standard_PopulationGroup", None)
        self.__standard_PopulationGroup = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "standard_DemographicPopulationModel"):
                opp_val = getattr(old_value, "standard_DemographicPopulationModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "standard_DemographicPopulationModel"):
                opp_val = getattr(value, "standard_DemographicPopulationModel", None)
                if opp_val is None:
                    setattr(value, "standard_DemographicPopulationModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class StandardPopulationModel:

    pass
class standard_DemographicPopulationModel(StandardPopulationModel):

    pass
class standard_SeasonalPopulationModel(StandardPopulationModel):

    def __init__(self, phase: float, modulationAmplitude: float, period: float, useLatitude: bool):
        self.phase = phase
        self.modulationAmplitude = modulationAmplitude
        self.period = period
        self.useLatitude = useLatitude
        
    @property
    def period(self) -> float:
        return self.__period

    @period.setter
    def period(self, period: float):
        self.__period = period

    @property
    def phase(self) -> float:
        return self.__phase

    @phase.setter
    def phase(self, phase: float):
        self.__phase = phase

    @property
    def useLatitude(self) -> bool:
        return self.__useLatitude

    @useLatitude.setter
    def useLatitude(self, useLatitude: bool):
        self.__useLatitude = useLatitude

    @property
    def modulationAmplitude(self) -> float:
        return self.__modulationAmplitude

    @modulationAmplitude.setter
    def modulationAmplitude(self, modulationAmplitude: float):
        self.__modulationAmplitude = modulationAmplitude

class standard_StochasticStandardPopulationModel(StandardPopulationModel):

    def __init__(self, gain: float):
        self.gain = gain
        
    @property
    def gain(self) -> float:
        return self.__gain

    @gain.setter
    def gain(self, gain: float):
        self.__gain = gain

class IntegrationLabelValue:

    pass
class standard_StandardPopulationModelLabelValue(PopulationModelLabelValue, IntegrationLabelValue):

    def __init__(self, count: float, incidence: float, births: float, deaths: float, density: float, standard_StandardPopulationModelLabelValue: "standard_StandardPopulationModelLabel" = None, standard_StandardPopulationModelLabelValue4: "standard_StandardPopulationModelLabel" = None, standard_StandardPopulationModelLabelValue7: "standard_StandardPopulationModelLabel" = None, standard_StandardPopulationModelLabelValue10: "standard_StandardPopulationModelLabel" = None, standard_StandardPopulationModelLabelValue13: "standard_StandardPopulationModelLabel" = None):
        self.count = count
        self.incidence = incidence
        self.births = births
        self.deaths = deaths
        self.density = density
        self.standard_StandardPopulationModelLabelValue = standard_StandardPopulationModelLabelValue
        self.standard_StandardPopulationModelLabelValue4 = standard_StandardPopulationModelLabelValue4
        self.standard_StandardPopulationModelLabelValue7 = standard_StandardPopulationModelLabelValue7
        self.standard_StandardPopulationModelLabelValue10 = standard_StandardPopulationModelLabelValue10
        self.standard_StandardPopulationModelLabelValue13 = standard_StandardPopulationModelLabelValue13
        
    @property
    def incidence(self) -> float:
        return self.__incidence

    @incidence.setter
    def incidence(self, incidence: float):
        self.__incidence = incidence

    @property
    def density(self) -> float:
        return self.__density

    @density.setter
    def density(self, density: float):
        self.__density = density

    @property
    def count(self) -> float:
        return self.__count

    @count.setter
    def count(self, count: float):
        self.__count = count

    @property
    def births(self) -> float:
        return self.__births

    @births.setter
    def births(self, births: float):
        self.__births = births

    @property
    def deaths(self) -> float:
        return self.__deaths

    @deaths.setter
    def deaths(self, deaths: float):
        self.__deaths = deaths

    @property
    def standard_StandardPopulationModelLabelValue7(self):
        return self.__standard_StandardPopulationModelLabelValue7

    @standard_StandardPopulationModelLabelValue7.setter
    def standard_StandardPopulationModelLabelValue7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_standard_StandardPopulationModelLabelValue__standard_StandardPopulationModelLabelValue7", None)
        self.__standard_StandardPopulationModelLabelValue7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "standard_StandardPopulationModelLabel6"):
                opp_val = getattr(old_value, "standard_StandardPopulationModelLabel6", None)
                if opp_val == self:
                    setattr(old_value, "standard_StandardPopulationModelLabel6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "standard_StandardPopulationModelLabel6"):
                opp_val = getattr(value, "standard_StandardPopulationModelLabel6", None)
                setattr(value, "standard_StandardPopulationModelLabel6", self)

    @property
    def standard_StandardPopulationModelLabelValue4(self):
        return self.__standard_StandardPopulationModelLabelValue4

    @standard_StandardPopulationModelLabelValue4.setter
    def standard_StandardPopulationModelLabelValue4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_standard_StandardPopulationModelLabelValue__standard_StandardPopulationModelLabelValue4", None)
        self.__standard_StandardPopulationModelLabelValue4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "standard_StandardPopulationModelLabel3"):
                opp_val = getattr(old_value, "standard_StandardPopulationModelLabel3", None)
                if opp_val == self:
                    setattr(old_value, "standard_StandardPopulationModelLabel3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "standard_StandardPopulationModelLabel3"):
                opp_val = getattr(value, "standard_StandardPopulationModelLabel3", None)
                setattr(value, "standard_StandardPopulationModelLabel3", self)

    @property
    def standard_StandardPopulationModelLabelValue10(self):
        return self.__standard_StandardPopulationModelLabelValue10

    @standard_StandardPopulationModelLabelValue10.setter
    def standard_StandardPopulationModelLabelValue10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_standard_StandardPopulationModelLabelValue__standard_StandardPopulationModelLabelValue10", None)
        self.__standard_StandardPopulationModelLabelValue10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "standard_StandardPopulationModelLabel9"):
                opp_val = getattr(old_value, "standard_StandardPopulationModelLabel9", None)
                if opp_val == self:
                    setattr(old_value, "standard_StandardPopulationModelLabel9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "standard_StandardPopulationModelLabel9"):
                opp_val = getattr(value, "standard_StandardPopulationModelLabel9", None)
                setattr(value, "standard_StandardPopulationModelLabel9", self)

    @property
    def standard_StandardPopulationModelLabelValue13(self):
        return self.__standard_StandardPopulationModelLabelValue13

    @standard_StandardPopulationModelLabelValue13.setter
    def standard_StandardPopulationModelLabelValue13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_standard_StandardPopulationModelLabelValue__standard_StandardPopulationModelLabelValue13", None)
        self.__standard_StandardPopulationModelLabelValue13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "standard_StandardPopulationModelLabel12"):
                opp_val = getattr(old_value, "standard_StandardPopulationModelLabel12", None)
                if opp_val == self:
                    setattr(old_value, "standard_StandardPopulationModelLabel12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "standard_StandardPopulationModelLabel12"):
                opp_val = getattr(value, "standard_StandardPopulationModelLabel12", None)
                setattr(value, "standard_StandardPopulationModelLabel12", self)

    @property
    def standard_StandardPopulationModelLabelValue(self):
        return self.__standard_StandardPopulationModelLabelValue

    @standard_StandardPopulationModelLabelValue.setter
    def standard_StandardPopulationModelLabelValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_standard_StandardPopulationModelLabelValue__standard_StandardPopulationModelLabelValue", None)
        self.__standard_StandardPopulationModelLabelValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "standard_StandardPopulationModelLabel"):
                opp_val = getattr(old_value, "standard_StandardPopulationModelLabel", None)
                if opp_val == self:
                    setattr(old_value, "standard_StandardPopulationModelLabel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "standard_StandardPopulationModelLabel"):
                opp_val = getattr(value, "standard_StandardPopulationModelLabel", None)
                setattr(value, "standard_StandardPopulationModelLabel", self)

    def adjustDelta(self, value: IntegrationLabelValue) -> bool:
        # TODO: Implement adjustDelta method
        pass

class standard_StandardPopulationModel(IntegrationDecorator, PopulationModel):

    def __init__(self, birthRate: float, deathRate: float, timePeriod: str):
        self.birthRate = birthRate
        self.deathRate = deathRate
        self.timePeriod = timePeriod
        
    @property
    def deathRate(self) -> float:
        return self.__deathRate

    @deathRate.setter
    def deathRate(self, deathRate: float):
        self.__deathRate = deathRate

    @property
    def timePeriod(self) -> str:
        return self.__timePeriod

    @timePeriod.setter
    def timePeriod(self, timePeriod: str):
        self.__timePeriod = timePeriod

    @property
    def birthRate(self) -> float:
        return self.__birthRate

    @birthRate.setter
    def birthRate(self, birthRate: float):
        self.__birthRate = birthRate

class Modifiable:

    pass
class NodeDecorator:

    pass
class standard_PopulationInitializer(Modifiable, NodeDecorator):

    def __init__(self, targetISOKey: str, populationIdentifier: str):
        self.targetISOKey = targetISOKey
        self.populationIdentifier = populationIdentifier
        
    @property
    def populationIdentifier(self) -> str:
        return self.__populationIdentifier

    @populationIdentifier.setter
    def populationIdentifier(self, populationIdentifier: str):
        self.__populationIdentifier = populationIdentifier

    @property
    def targetISOKey(self) -> str:
        return self.__targetISOKey

    @targetISOKey.setter
    def targetISOKey(self, targetISOKey: str):
        self.__targetISOKey = targetISOKey

class standard_PopulationModel(NodeDecorator, Modifiable):

    def __init__(self, populationIdentifier: str, name: str, targetISOKey: str):
        self.populationIdentifier = populationIdentifier
        self.name = name
        self.targetISOKey = targetISOKey
        
    @property
    def populationIdentifier(self) -> str:
        return self.__populationIdentifier

    @populationIdentifier.setter
    def populationIdentifier(self, populationIdentifier: str):
        self.__populationIdentifier = populationIdentifier

    @property
    def targetISOKey(self) -> str:
        return self.__targetISOKey

    @targetISOKey.setter
    def targetISOKey(self, targetISOKey: str):
        self.__targetISOKey = targetISOKey

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name
