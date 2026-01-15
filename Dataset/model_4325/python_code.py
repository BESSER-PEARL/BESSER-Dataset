from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class MetricAggregationOperator(Enum):
    SUM = "SUM"
    AVERAGE = "AVERAGE"
    MINIMUM = "MINIMUM"
    MAXIMUM = "MAXIMUM"
class AttributeAggregationOperator(Enum):
    NEUTRALITY = "NEUTRALITY"
    SIMULTANEITY = "SIMULTANEITY"
    REPLACEABILITY = "REPLACEABILITY"
class MetricNormalizationKind(Enum):
    BENEFIT = "BENEFIT"
    COST = "COST"


############################################
# Definition of Classes
############################################

class qualitymodel_ConfigurationProfile:

    def __init__(self, ID: int, qualitymodel_ConfigurationProfile: set["qualitymodel_Preference"] = None, qualitymodel_ConfigurationProfile9: set["qualitymodel_Metric"] = None):
        self.ID = ID
        self.qualitymodel_ConfigurationProfile = qualitymodel_ConfigurationProfile if qualitymodel_ConfigurationProfile is not None else set()
        self.qualitymodel_ConfigurationProfile9 = qualitymodel_ConfigurationProfile9 if qualitymodel_ConfigurationProfile9 is not None else set()
        
    @property
    def ID(self) -> int:
        return self.__ID

    @ID.setter
    def ID(self, ID: int):
        self.__ID = ID

    @property
    def qualitymodel_ConfigurationProfile9(self):
        return self.__qualitymodel_ConfigurationProfile9

    @qualitymodel_ConfigurationProfile9.setter
    def qualitymodel_ConfigurationProfile9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qualitymodel_ConfigurationProfile__qualitymodel_ConfigurationProfile9", None)
        self.__qualitymodel_ConfigurationProfile9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "qualitymodel_Metric10"):
                    opp_val = getattr(item, "qualitymodel_Metric10", None)
                    
                    if opp_val == self:
                        setattr(item, "qualitymodel_Metric10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "qualitymodel_Metric10"):
                    opp_val = getattr(item, "qualitymodel_Metric10", None)
                    
                    setattr(item, "qualitymodel_Metric10", self)
                    

    @property
    def qualitymodel_ConfigurationProfile(self):
        return self.__qualitymodel_ConfigurationProfile

    @qualitymodel_ConfigurationProfile.setter
    def qualitymodel_ConfigurationProfile(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qualitymodel_ConfigurationProfile__qualitymodel_ConfigurationProfile", None)
        self.__qualitymodel_ConfigurationProfile = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "qualitymodel_Preference7"):
                    opp_val = getattr(item, "qualitymodel_Preference7", None)
                    
                    if opp_val == self:
                        setattr(item, "qualitymodel_Preference7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "qualitymodel_Preference7"):
                    opp_val = getattr(item, "qualitymodel_Preference7", None)
                    
                    setattr(item, "qualitymodel_Preference7", self)
                    

class qualitymodel_Preference:

    def __init__(self, weight: float, threshold: float, qualitymodel_Preference: "qualitymodel_Attribute" = None, qualitymodel_Preference7: "qualitymodel_ConfigurationProfile" = None):
        self.weight = weight
        self.threshold = threshold
        self.qualitymodel_Preference = qualitymodel_Preference
        self.qualitymodel_Preference7 = qualitymodel_Preference7
        
    @property
    def weight(self) -> float:
        return self.__weight

    @weight.setter
    def weight(self, weight: float):
        self.__weight = weight

    @property
    def threshold(self) -> float:
        return self.__threshold

    @threshold.setter
    def threshold(self, threshold: float):
        self.__threshold = threshold

    @property
    def qualitymodel_Preference7(self):
        return self.__qualitymodel_Preference7

    @qualitymodel_Preference7.setter
    def qualitymodel_Preference7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qualitymodel_Preference__qualitymodel_Preference7", None)
        self.__qualitymodel_Preference7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qualitymodel_ConfigurationProfile"):
                opp_val = getattr(old_value, "qualitymodel_ConfigurationProfile", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qualitymodel_ConfigurationProfile"):
                opp_val = getattr(value, "qualitymodel_ConfigurationProfile", None)
                if opp_val is None:
                    setattr(value, "qualitymodel_ConfigurationProfile", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def qualitymodel_Preference(self):
        return self.__qualitymodel_Preference

    @qualitymodel_Preference.setter
    def qualitymodel_Preference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qualitymodel_Preference__qualitymodel_Preference", None)
        self.__qualitymodel_Preference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qualitymodel_Attribute5"):
                opp_val = getattr(old_value, "qualitymodel_Attribute5", None)
                if opp_val == self:
                    setattr(old_value, "qualitymodel_Attribute5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qualitymodel_Attribute5"):
                opp_val = getattr(value, "qualitymodel_Attribute5", None)
                setattr(value, "qualitymodel_Attribute5", self)

class qualitymodel_HistoricalData:

    def __init__(self, instant: str, value: float, qualitymodel_HistoricalData: "qualitymodel_Attribute" = None):
        self.instant = instant
        self.value = value
        self.qualitymodel_HistoricalData = qualitymodel_HistoricalData
        
    @property
    def instant(self) -> str:
        return self.__instant

    @instant.setter
    def instant(self, instant: str):
        self.__instant = instant

    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def qualitymodel_HistoricalData(self):
        return self.__qualitymodel_HistoricalData

    @qualitymodel_HistoricalData.setter
    def qualitymodel_HistoricalData(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qualitymodel_HistoricalData__qualitymodel_HistoricalData", None)
        self.__qualitymodel_HistoricalData = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qualitymodel_Attribute3"):
                opp_val = getattr(old_value, "qualitymodel_Attribute3", None)
                if opp_val == self:
                    setattr(old_value, "qualitymodel_Attribute3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qualitymodel_Attribute3"):
                opp_val = getattr(value, "qualitymodel_Attribute3", None)
                setattr(value, "qualitymodel_Attribute3", self)

class qualitymodel_Metric:

    def __init__(self, resourceName: str, data: str, probeName: str, descriptionName: str, qualitymodel_Metric: "qualitymodel_LeafAttribute" = None, qualitymodel_Metric10: "qualitymodel_ConfigurationProfile" = None):
        self.resourceName = resourceName
        self.data = data
        self.probeName = probeName
        self.descriptionName = descriptionName
        self.qualitymodel_Metric = qualitymodel_Metric
        self.qualitymodel_Metric10 = qualitymodel_Metric10
        
    @property
    def descriptionName(self) -> str:
        return self.__descriptionName

    @descriptionName.setter
    def descriptionName(self, descriptionName: str):
        self.__descriptionName = descriptionName

    @property
    def data(self) -> str:
        return self.__data

    @data.setter
    def data(self, data: str):
        self.__data = data

    @property
    def resourceName(self) -> str:
        return self.__resourceName

    @resourceName.setter
    def resourceName(self, resourceName: str):
        self.__resourceName = resourceName

    @property
    def probeName(self) -> str:
        return self.__probeName

    @probeName.setter
    def probeName(self, probeName: str):
        self.__probeName = probeName

    @property
    def qualitymodel_Metric(self):
        return self.__qualitymodel_Metric

    @qualitymodel_Metric.setter
    def qualitymodel_Metric(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qualitymodel_Metric__qualitymodel_Metric", None)
        self.__qualitymodel_Metric = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qualitymodel_LeafAttribute"):
                opp_val = getattr(old_value, "qualitymodel_LeafAttribute", None)
                if opp_val == self:
                    setattr(old_value, "qualitymodel_LeafAttribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qualitymodel_LeafAttribute"):
                opp_val = getattr(value, "qualitymodel_LeafAttribute", None)
                setattr(value, "qualitymodel_LeafAttribute", self)

    @property
    def qualitymodel_Metric10(self):
        return self.__qualitymodel_Metric10

    @qualitymodel_Metric10.setter
    def qualitymodel_Metric10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qualitymodel_Metric__qualitymodel_Metric10", None)
        self.__qualitymodel_Metric10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qualitymodel_ConfigurationProfile9"):
                opp_val = getattr(old_value, "qualitymodel_ConfigurationProfile9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qualitymodel_ConfigurationProfile9"):
                opp_val = getattr(value, "qualitymodel_ConfigurationProfile9", None)
                if opp_val is None:
                    setattr(value, "qualitymodel_ConfigurationProfile9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Attribute:

    pass
class qualitymodel_CompositeAttribute(Attribute):

    def __init__(self, operator: str, qualitymodel_CompositeAttribute: set["qualitymodel_Attribute"] = None):
        self.operator = operator
        self.qualitymodel_CompositeAttribute = qualitymodel_CompositeAttribute if qualitymodel_CompositeAttribute is not None else set()
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def qualitymodel_CompositeAttribute(self):
        return self.__qualitymodel_CompositeAttribute

    @qualitymodel_CompositeAttribute.setter
    def qualitymodel_CompositeAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qualitymodel_CompositeAttribute__qualitymodel_CompositeAttribute", None)
        self.__qualitymodel_CompositeAttribute = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "qualitymodel_Attribute"):
                    opp_val = getattr(item, "qualitymodel_Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "qualitymodel_Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "qualitymodel_Attribute"):
                    opp_val = getattr(item, "qualitymodel_Attribute", None)
                    
                    setattr(item, "qualitymodel_Attribute", self)
                    

    def calculateReplaceability(self, profile: str) -> float:
        # TODO: Implement calculateReplaceability method
        pass

    def calculateNeutrality(self, profile: str) -> float:
        # TODO: Implement calculateNeutrality method
        pass

    def calculateSimultaneity(self, profile: str) -> float:
        # TODO: Implement calculateSimultaneity method
        pass

class qualitymodel_Attribute(ABC):

    def __init__(self, name: str, qualitymodel_Attribute: "qualitymodel_CompositeAttribute" = None, qualitymodel_Attribute3: "qualitymodel_HistoricalData" = None, qualitymodel_Attribute5: "qualitymodel_Preference" = None):
        self.name = name
        self.qualitymodel_Attribute = qualitymodel_Attribute
        self.qualitymodel_Attribute3 = qualitymodel_Attribute3
        self.qualitymodel_Attribute5 = qualitymodel_Attribute5
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def qualitymodel_Attribute(self):
        return self.__qualitymodel_Attribute

    @qualitymodel_Attribute.setter
    def qualitymodel_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qualitymodel_Attribute__qualitymodel_Attribute", None)
        self.__qualitymodel_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qualitymodel_CompositeAttribute"):
                opp_val = getattr(old_value, "qualitymodel_CompositeAttribute", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qualitymodel_CompositeAttribute"):
                opp_val = getattr(value, "qualitymodel_CompositeAttribute", None)
                if opp_val is None:
                    setattr(value, "qualitymodel_CompositeAttribute", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def qualitymodel_Attribute3(self):
        return self.__qualitymodel_Attribute3

    @qualitymodel_Attribute3.setter
    def qualitymodel_Attribute3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qualitymodel_Attribute__qualitymodel_Attribute3", None)
        self.__qualitymodel_Attribute3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qualitymodel_HistoricalData"):
                opp_val = getattr(old_value, "qualitymodel_HistoricalData", None)
                if opp_val == self:
                    setattr(old_value, "qualitymodel_HistoricalData", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qualitymodel_HistoricalData"):
                opp_val = getattr(value, "qualitymodel_HistoricalData", None)
                setattr(value, "qualitymodel_HistoricalData", self)

    @property
    def qualitymodel_Attribute5(self):
        return self.__qualitymodel_Attribute5

    @qualitymodel_Attribute5.setter
    def qualitymodel_Attribute5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qualitymodel_Attribute__qualitymodel_Attribute5", None)
        self.__qualitymodel_Attribute5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qualitymodel_Preference"):
                opp_val = getattr(old_value, "qualitymodel_Preference", None)
                if opp_val == self:
                    setattr(old_value, "qualitymodel_Preference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qualitymodel_Preference"):
                opp_val = getattr(value, "qualitymodel_Preference", None)
                setattr(value, "qualitymodel_Preference", self)

    def calculate(self, profile: str) -> str:
        # TODO: Implement calculate method
        pass

class qualitymodel_LeafAttribute(Attribute):

    def __init__(self, normalizationMin: float, normalizationMax: float, operator: str, numSamples: int, normalizationKind: str, qualitymodel_LeafAttribute: "qualitymodel_Metric" = None):
        self.normalizationMin = normalizationMin
        self.normalizationMax = normalizationMax
        self.operator = operator
        self.numSamples = numSamples
        self.normalizationKind = normalizationKind
        self.qualitymodel_LeafAttribute = qualitymodel_LeafAttribute
        
    @property
    def numSamples(self) -> int:
        return self.__numSamples

    @numSamples.setter
    def numSamples(self, numSamples: int):
        self.__numSamples = numSamples

    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def normalizationKind(self) -> str:
        return self.__normalizationKind

    @normalizationKind.setter
    def normalizationKind(self, normalizationKind: str):
        self.__normalizationKind = normalizationKind

    @property
    def normalizationMax(self) -> float:
        return self.__normalizationMax

    @normalizationMax.setter
    def normalizationMax(self, normalizationMax: float):
        self.__normalizationMax = normalizationMax

    @property
    def normalizationMin(self) -> float:
        return self.__normalizationMin

    @normalizationMin.setter
    def normalizationMin(self, normalizationMin: float):
        self.__normalizationMin = normalizationMin

    @property
    def qualitymodel_LeafAttribute(self):
        return self.__qualitymodel_LeafAttribute

    @qualitymodel_LeafAttribute.setter
    def qualitymodel_LeafAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qualitymodel_LeafAttribute__qualitymodel_LeafAttribute", None)
        self.__qualitymodel_LeafAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qualitymodel_Metric"):
                opp_val = getattr(old_value, "qualitymodel_Metric", None)
                if opp_val == self:
                    setattr(old_value, "qualitymodel_Metric", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qualitymodel_Metric"):
                opp_val = getattr(value, "qualitymodel_Metric", None)
                setattr(value, "qualitymodel_Metric", self)

    def calculateSum(self, profile: str) -> float:
        # TODO: Implement calculateSum method
        pass

    def calculateAverage(self, profile: str) -> float:
        # TODO: Implement calculateAverage method
        pass

    def calculateMinimum(self, profile: str) -> float:
        # TODO: Implement calculateMinimum method
        pass

    def calculateMaximum(self, profile: str) -> float:
        # TODO: Implement calculateMaximum method
        pass
