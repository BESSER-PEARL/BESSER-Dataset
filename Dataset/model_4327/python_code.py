from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class BinaryFunctor(Enum):
    plus = "plus"
    minus = "minus"
    multiply = "multiply"
    divide = "divide"
    custom = "custom"
class MeasurementScale(Enum):
    ordinal = "ordinal"
    nominal = "nominal"
    ratio = "ratio"
    interval = "interval"
class Accumulator(Enum):
    maximum = "maximum"
    minimum = "minimum"
    average = "average"
    standardDeviation = "standardDeviation"
    product = "product"
    custom = "custom"
    sum = "sum"
class Influence(Enum):
    positive = "positive"
    negative = "negative"
class ScaleOfMeasurement(Enum):
    nominal = "nominal"
    ordinal = "ordinal"
    interval = "interval"
    ratio = "ratio"
    custom = "custom"


############################################
# Definition of Classes
############################################

class UnitOfMeasure:

    pass
class smm_CountingUnit(UnitOfMeasure):

    pass
class smm_SmmElement(ABC):

    def __init__(self, name: str, shortDescription: str, description: str, SmmElement179: "smm_SmmRelationship" = None, smm_SmmElement: set["smm_Attribute"] = None, smm_SmmElement168: set["smm_Annotation"] = None, to: set["smm_SmmRelationship"] = None, from: set["smm_SmmRelationship"] = None, SmmElement: "smm_SmmRelationship" = None):
        self.name = name
        self.shortDescription = shortDescription
        self.description = description
        self.SmmElement179 = SmmElement179
        self.smm_SmmElement = smm_SmmElement if smm_SmmElement is not None else set()
        self.smm_SmmElement168 = smm_SmmElement168 if smm_SmmElement168 is not None else set()
        self.to = to if to is not None else set()
        self.from = from if from is not None else set()
        self.SmmElement = SmmElement
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def shortDescription(self) -> str:
        return self.__shortDescription

    @shortDescription.setter
    def shortDescription(self, shortDescription: str):
        self.__shortDescription = shortDescription

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def SmmElement179(self):
        return self.__SmmElement179

    @SmmElement179.setter
    def SmmElement179(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_SmmElement__SmmElement179", None)
        self.__SmmElement179 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outRelationships"):
                opp_val = getattr(old_value, "outRelationships", None)
                if opp_val == self:
                    setattr(old_value, "outRelationships", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outRelationships"):
                opp_val = getattr(value, "outRelationships", None)
                setattr(value, "outRelationships", self)

    @property
    def from(self):
        return self.__from

    @from.setter
    def from(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_SmmElement__from", None)
        self.__from = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SmmRelationship171"):
                    opp_val = getattr(item, "SmmRelationship171", None)
                    
                    if opp_val == self:
                        setattr(item, "SmmRelationship171", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SmmRelationship171"):
                    opp_val = getattr(item, "SmmRelationship171", None)
                    
                    setattr(item, "SmmRelationship171", self)
                    

    @property
    def to(self):
        return self.__to

    @to.setter
    def to(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_SmmElement__to", None)
        self.__to = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SmmRelationship"):
                    opp_val = getattr(item, "SmmRelationship", None)
                    
                    if opp_val == self:
                        setattr(item, "SmmRelationship", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SmmRelationship"):
                    opp_val = getattr(item, "SmmRelationship", None)
                    
                    setattr(item, "SmmRelationship", self)
                    

    @property
    def smm_SmmElement(self):
        return self.__smm_SmmElement

    @smm_SmmElement.setter
    def smm_SmmElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_SmmElement__smm_SmmElement", None)
        self.__smm_SmmElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smm_Attribute"):
                    opp_val = getattr(item, "smm_Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "smm_Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smm_Attribute"):
                    opp_val = getattr(item, "smm_Attribute", None)
                    
                    setattr(item, "smm_Attribute", self)
                    

    @property
    def smm_SmmElement168(self):
        return self.__smm_SmmElement168

    @smm_SmmElement168.setter
    def smm_SmmElement168(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_SmmElement__smm_SmmElement168", None)
        self.__smm_SmmElement168 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smm_Annotation"):
                    opp_val = getattr(item, "smm_Annotation", None)
                    
                    if opp_val == self:
                        setattr(item, "smm_Annotation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smm_Annotation"):
                    opp_val = getattr(item, "smm_Annotation", None)
                    
                    setattr(item, "smm_Annotation", self)
                    

    @property
    def SmmElement(self):
        return self.__SmmElement

    @SmmElement.setter
    def SmmElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_SmmElement__SmmElement", None)
        self.__SmmElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "inRelationships"):
                opp_val = getattr(old_value, "inRelationships", None)
                if opp_val == self:
                    setattr(old_value, "inRelationships", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "inRelationships"):
                opp_val = getattr(value, "inRelationships", None)
                setattr(value, "inRelationships", self)

class BaseMeasurementRelationship:

    pass
class smm_ScaledBaseMeasurementRelationship(BaseMeasurementRelationship):

    pass
class BaseMeasureRelationship:

    pass
class smm_ScaledBaseMeasureRelationship(BaseMeasureRelationship):

    pass
class BinaryMeasurement:

    pass
class smm_RatioMeasurement(BinaryMeasurement):

    pass
class BinaryMeasure:

    pass
class smm_RatioMeasure(BinaryMeasure):

    pass
class Interval:

    pass
class smm_RankingInterval(Interval):

    def __init__(self, value: float, RankingInterval: "smm_RankingMeasure" = None, interval: "smm_RankingMeasure" = None):
        self.value = value
        self.RankingInterval = RankingInterval
        self.interval = interval
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def RankingInterval(self):
        return self.__RankingInterval

    @RankingInterval.setter
    def RankingInterval(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_RankingInterval__RankingInterval", None)
        self.__RankingInterval = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ranking"):
                opp_val = getattr(old_value, "ranking", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ranking"):
                opp_val = getattr(value, "ranking", None)
                if opp_val is None:
                    setattr(value, "ranking", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def interval(self):
        return self.__interval

    @interval.setter
    def interval(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_RankingInterval__interval", None)
        self.__interval = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RankingMeasure"):
                opp_val = getattr(old_value, "RankingMeasure", None)
                if opp_val == self:
                    setattr(old_value, "RankingMeasure", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RankingMeasure"):
                opp_val = getattr(value, "RankingMeasure", None)
                setattr(value, "RankingMeasure", self)

class smm_GradeInterval(Interval):

    def __init__(self, symbol: str, smm_GradeInterval: "smm_GradeMeasure" = None):
        self.symbol = symbol
        self.smm_GradeInterval = smm_GradeInterval
        
    @property
    def symbol(self) -> str:
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol: str):
        self.__symbol = symbol

    @property
    def smm_GradeInterval(self):
        return self.__smm_GradeInterval

    @smm_GradeInterval.setter
    def smm_GradeInterval(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_GradeInterval__smm_GradeInterval", None)
        self.__smm_GradeInterval = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_GradeMeasure142"):
                opp_val = getattr(old_value, "smm_GradeMeasure142", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_GradeMeasure142"):
                opp_val = getattr(value, "smm_GradeMeasure142", None)
                if opp_val is None:
                    setattr(value, "smm_GradeMeasure142", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class smm_EObject:

    pass
class smm_RescaledMeasureRelationship(BaseMeasureRelationship):

    pass
class Measure:

    pass
class smm_GradeMeasure(Measure):

    pass
class smm_DimensionalMeasure(Measure):

    def __init__(self, formula: str, smm_DimensionalMeasure: set["smm_Base1MeasureRelationship"] = None, smm_DimensionalMeasure27: set["smm_BaseNMeasureRelationship"] = None, smm_DimensionalMeasure30: set["smm_Base2MeasureRelationship"] = None, smm_DimensionalMeasure33: set["smm_RankingMeasureRelationship"] = None, smm_DimensionalMeasure35: set["smm_RescaledMeasureRelationship"] = None, smm_DimensionalMeasure37: set["smm_GradeMeasureRelationship"] = None, smm_DimensionalMeasure39: "smm_UnitOfMeasure" = None):
        self.formula = formula
        self.smm_DimensionalMeasure = smm_DimensionalMeasure if smm_DimensionalMeasure is not None else set()
        self.smm_DimensionalMeasure27 = smm_DimensionalMeasure27 if smm_DimensionalMeasure27 is not None else set()
        self.smm_DimensionalMeasure30 = smm_DimensionalMeasure30 if smm_DimensionalMeasure30 is not None else set()
        self.smm_DimensionalMeasure33 = smm_DimensionalMeasure33 if smm_DimensionalMeasure33 is not None else set()
        self.smm_DimensionalMeasure35 = smm_DimensionalMeasure35 if smm_DimensionalMeasure35 is not None else set()
        self.smm_DimensionalMeasure37 = smm_DimensionalMeasure37 if smm_DimensionalMeasure37 is not None else set()
        self.smm_DimensionalMeasure39 = smm_DimensionalMeasure39
        
    @property
    def formula(self) -> str:
        return self.__formula

    @formula.setter
    def formula(self, formula: str):
        self.__formula = formula

    @property
    def smm_DimensionalMeasure27(self):
        return self.__smm_DimensionalMeasure27

    @smm_DimensionalMeasure27.setter
    def smm_DimensionalMeasure27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_DimensionalMeasure__smm_DimensionalMeasure27", None)
        self.__smm_DimensionalMeasure27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smm_BaseNMeasureRelationship28"):
                    opp_val = getattr(item, "smm_BaseNMeasureRelationship28", None)
                    
                    if opp_val == self:
                        setattr(item, "smm_BaseNMeasureRelationship28", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smm_BaseNMeasureRelationship28"):
                    opp_val = getattr(item, "smm_BaseNMeasureRelationship28", None)
                    
                    setattr(item, "smm_BaseNMeasureRelationship28", self)
                    

    @property
    def smm_DimensionalMeasure30(self):
        return self.__smm_DimensionalMeasure30

    @smm_DimensionalMeasure30.setter
    def smm_DimensionalMeasure30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_DimensionalMeasure__smm_DimensionalMeasure30", None)
        self.__smm_DimensionalMeasure30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smm_Base2MeasureRelationship31"):
                    opp_val = getattr(item, "smm_Base2MeasureRelationship31", None)
                    
                    if opp_val == self:
                        setattr(item, "smm_Base2MeasureRelationship31", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smm_Base2MeasureRelationship31"):
                    opp_val = getattr(item, "smm_Base2MeasureRelationship31", None)
                    
                    setattr(item, "smm_Base2MeasureRelationship31", self)
                    

    @property
    def smm_DimensionalMeasure(self):
        return self.__smm_DimensionalMeasure

    @smm_DimensionalMeasure.setter
    def smm_DimensionalMeasure(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_DimensionalMeasure__smm_DimensionalMeasure", None)
        self.__smm_DimensionalMeasure = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smm_Base1MeasureRelationship25"):
                    opp_val = getattr(item, "smm_Base1MeasureRelationship25", None)
                    
                    if opp_val == self:
                        setattr(item, "smm_Base1MeasureRelationship25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smm_Base1MeasureRelationship25"):
                    opp_val = getattr(item, "smm_Base1MeasureRelationship25", None)
                    
                    setattr(item, "smm_Base1MeasureRelationship25", self)
                    

    @property
    def smm_DimensionalMeasure35(self):
        return self.__smm_DimensionalMeasure35

    @smm_DimensionalMeasure35.setter
    def smm_DimensionalMeasure35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_DimensionalMeasure__smm_DimensionalMeasure35", None)
        self.__smm_DimensionalMeasure35 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smm_RescaledMeasureRelationship"):
                    opp_val = getattr(item, "smm_RescaledMeasureRelationship", None)
                    
                    if opp_val == self:
                        setattr(item, "smm_RescaledMeasureRelationship", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smm_RescaledMeasureRelationship"):
                    opp_val = getattr(item, "smm_RescaledMeasureRelationship", None)
                    
                    setattr(item, "smm_RescaledMeasureRelationship", self)
                    

    @property
    def smm_DimensionalMeasure39(self):
        return self.__smm_DimensionalMeasure39

    @smm_DimensionalMeasure39.setter
    def smm_DimensionalMeasure39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_DimensionalMeasure__smm_DimensionalMeasure39", None)
        self.__smm_DimensionalMeasure39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_UnitOfMeasure"):
                opp_val = getattr(old_value, "smm_UnitOfMeasure", None)
                if opp_val == self:
                    setattr(old_value, "smm_UnitOfMeasure", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_UnitOfMeasure"):
                opp_val = getattr(value, "smm_UnitOfMeasure", None)
                setattr(value, "smm_UnitOfMeasure", self)

    @property
    def smm_DimensionalMeasure37(self):
        return self.__smm_DimensionalMeasure37

    @smm_DimensionalMeasure37.setter
    def smm_DimensionalMeasure37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_DimensionalMeasure__smm_DimensionalMeasure37", None)
        self.__smm_DimensionalMeasure37 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smm_GradeMeasureRelationship"):
                    opp_val = getattr(item, "smm_GradeMeasureRelationship", None)
                    
                    if opp_val == self:
                        setattr(item, "smm_GradeMeasureRelationship", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smm_GradeMeasureRelationship"):
                    opp_val = getattr(item, "smm_GradeMeasureRelationship", None)
                    
                    setattr(item, "smm_GradeMeasureRelationship", self)
                    

    @property
    def smm_DimensionalMeasure33(self):
        return self.__smm_DimensionalMeasure33

    @smm_DimensionalMeasure33.setter
    def smm_DimensionalMeasure33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_DimensionalMeasure__smm_DimensionalMeasure33", None)
        self.__smm_DimensionalMeasure33 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smm_RankingMeasureRelationship"):
                    opp_val = getattr(item, "smm_RankingMeasureRelationship", None)
                    
                    if opp_val == self:
                        setattr(item, "smm_RankingMeasureRelationship", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smm_RankingMeasureRelationship"):
                    opp_val = getattr(item, "smm_RankingMeasureRelationship", None)
                    
                    setattr(item, "smm_RankingMeasureRelationship", self)
                    

class MeasurementRelationship:

    pass
class smm_RefinementMeasurementRelationship(MeasurementRelationship):

    pass
class smm_BaseMeasurementRelationship(MeasurementRelationship):

    pass
class smm_EquivalentMeasurementRelationship(MeasurementRelationship):

    pass
class MeasureRelationship:

    pass
class smm_RefinementMeasureRelationship(MeasureRelationship):

    pass
class smm_BaseMeasureRelationship(MeasureRelationship):

    pass
class smm_EquivalentMeasureRelationship(MeasureRelationship):

    pass
class smm_RescaledMeasurementRelationship(BaseMeasurementRelationship):

    pass
class Measurement:

    pass
class smm_GradeMeasurement(Measurement):

    def __init__(self, isBaseSupplied: bool, value: str, smm_GradeMeasurement: "smm_GradeMeasurementRelationship" = None, smm_GradeMeasurement61: "smm_Operation" = None):
        self.isBaseSupplied = isBaseSupplied
        self.value = value
        self.smm_GradeMeasurement = smm_GradeMeasurement
        self.smm_GradeMeasurement61 = smm_GradeMeasurement61
        
    @property
    def isBaseSupplied(self) -> bool:
        return self.__isBaseSupplied

    @isBaseSupplied.setter
    def isBaseSupplied(self, isBaseSupplied: bool):
        self.__isBaseSupplied = isBaseSupplied

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def smm_GradeMeasurement(self):
        return self.__smm_GradeMeasurement

    @smm_GradeMeasurement.setter
    def smm_GradeMeasurement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_GradeMeasurement__smm_GradeMeasurement", None)
        self.__smm_GradeMeasurement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_GradeMeasurementRelationship59"):
                opp_val = getattr(old_value, "smm_GradeMeasurementRelationship59", None)
                if opp_val == self:
                    setattr(old_value, "smm_GradeMeasurementRelationship59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_GradeMeasurementRelationship59"):
                opp_val = getattr(value, "smm_GradeMeasurementRelationship59", None)
                setattr(value, "smm_GradeMeasurementRelationship59", self)

    @property
    def smm_GradeMeasurement61(self):
        return self.__smm_GradeMeasurement61

    @smm_GradeMeasurement61.setter
    def smm_GradeMeasurement61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_GradeMeasurement__smm_GradeMeasurement61", None)
        self.__smm_GradeMeasurement61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_Operation62"):
                opp_val = getattr(old_value, "smm_Operation62", None)
                if opp_val == self:
                    setattr(old_value, "smm_Operation62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_Operation62"):
                opp_val = getattr(value, "smm_Operation62", None)
                setattr(value, "smm_Operation62", self)

class smm_DimensionalMeasurement(Measurement):

    def __init__(self, value: float, smm_DimensionalMeasurement: set["smm_Base1MeasurementRelationship"] = None, smm_DimensionalMeasurement43: set["smm_BaseNMeasurementRelationship"] = None, smm_DimensionalMeasurement46: set["smm_Base2MeasurementRelationship"] = None, smm_DimensionalMeasurement49: set["smm_GradeMeasurementRelationship"] = None, smm_DimensionalMeasurement51: set["smm_RescaledMeasurementRelationship"] = None, smm_DimensionalMeasurement53: set["smm_RankingMeasurementRelationship"] = None):
        self.value = value
        self.smm_DimensionalMeasurement = smm_DimensionalMeasurement if smm_DimensionalMeasurement is not None else set()
        self.smm_DimensionalMeasurement43 = smm_DimensionalMeasurement43 if smm_DimensionalMeasurement43 is not None else set()
        self.smm_DimensionalMeasurement46 = smm_DimensionalMeasurement46 if smm_DimensionalMeasurement46 is not None else set()
        self.smm_DimensionalMeasurement49 = smm_DimensionalMeasurement49 if smm_DimensionalMeasurement49 is not None else set()
        self.smm_DimensionalMeasurement51 = smm_DimensionalMeasurement51 if smm_DimensionalMeasurement51 is not None else set()
        self.smm_DimensionalMeasurement53 = smm_DimensionalMeasurement53 if smm_DimensionalMeasurement53 is not None else set()
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def smm_DimensionalMeasurement53(self):
        return self.__smm_DimensionalMeasurement53

    @smm_DimensionalMeasurement53.setter
    def smm_DimensionalMeasurement53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_DimensionalMeasurement__smm_DimensionalMeasurement53", None)
        self.__smm_DimensionalMeasurement53 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smm_RankingMeasurementRelationship"):
                    opp_val = getattr(item, "smm_RankingMeasurementRelationship", None)
                    
                    if opp_val == self:
                        setattr(item, "smm_RankingMeasurementRelationship", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smm_RankingMeasurementRelationship"):
                    opp_val = getattr(item, "smm_RankingMeasurementRelationship", None)
                    
                    setattr(item, "smm_RankingMeasurementRelationship", self)
                    

    @property
    def smm_DimensionalMeasurement46(self):
        return self.__smm_DimensionalMeasurement46

    @smm_DimensionalMeasurement46.setter
    def smm_DimensionalMeasurement46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_DimensionalMeasurement__smm_DimensionalMeasurement46", None)
        self.__smm_DimensionalMeasurement46 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smm_Base2MeasurementRelationship47"):
                    opp_val = getattr(item, "smm_Base2MeasurementRelationship47", None)
                    
                    if opp_val == self:
                        setattr(item, "smm_Base2MeasurementRelationship47", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smm_Base2MeasurementRelationship47"):
                    opp_val = getattr(item, "smm_Base2MeasurementRelationship47", None)
                    
                    setattr(item, "smm_Base2MeasurementRelationship47", self)
                    

    @property
    def smm_DimensionalMeasurement43(self):
        return self.__smm_DimensionalMeasurement43

    @smm_DimensionalMeasurement43.setter
    def smm_DimensionalMeasurement43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_DimensionalMeasurement__smm_DimensionalMeasurement43", None)
        self.__smm_DimensionalMeasurement43 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smm_BaseNMeasurementRelationship44"):
                    opp_val = getattr(item, "smm_BaseNMeasurementRelationship44", None)
                    
                    if opp_val == self:
                        setattr(item, "smm_BaseNMeasurementRelationship44", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smm_BaseNMeasurementRelationship44"):
                    opp_val = getattr(item, "smm_BaseNMeasurementRelationship44", None)
                    
                    setattr(item, "smm_BaseNMeasurementRelationship44", self)
                    

    @property
    def smm_DimensionalMeasurement49(self):
        return self.__smm_DimensionalMeasurement49

    @smm_DimensionalMeasurement49.setter
    def smm_DimensionalMeasurement49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_DimensionalMeasurement__smm_DimensionalMeasurement49", None)
        self.__smm_DimensionalMeasurement49 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smm_GradeMeasurementRelationship"):
                    opp_val = getattr(item, "smm_GradeMeasurementRelationship", None)
                    
                    if opp_val == self:
                        setattr(item, "smm_GradeMeasurementRelationship", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smm_GradeMeasurementRelationship"):
                    opp_val = getattr(item, "smm_GradeMeasurementRelationship", None)
                    
                    setattr(item, "smm_GradeMeasurementRelationship", self)
                    

    @property
    def smm_DimensionalMeasurement51(self):
        return self.__smm_DimensionalMeasurement51

    @smm_DimensionalMeasurement51.setter
    def smm_DimensionalMeasurement51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_DimensionalMeasurement__smm_DimensionalMeasurement51", None)
        self.__smm_DimensionalMeasurement51 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smm_RescaledMeasurementRelationship"):
                    opp_val = getattr(item, "smm_RescaledMeasurementRelationship", None)
                    
                    if opp_val == self:
                        setattr(item, "smm_RescaledMeasurementRelationship", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smm_RescaledMeasurementRelationship"):
                    opp_val = getattr(item, "smm_RescaledMeasurementRelationship", None)
                    
                    setattr(item, "smm_RescaledMeasurementRelationship", self)
                    

    @property
    def smm_DimensionalMeasurement(self):
        return self.__smm_DimensionalMeasurement

    @smm_DimensionalMeasurement.setter
    def smm_DimensionalMeasurement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_DimensionalMeasurement__smm_DimensionalMeasurement", None)
        self.__smm_DimensionalMeasurement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smm_Base1MeasurementRelationship41"):
                    opp_val = getattr(item, "smm_Base1MeasurementRelationship41", None)
                    
                    if opp_val == self:
                        setattr(item, "smm_Base1MeasurementRelationship41", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smm_Base1MeasurementRelationship41"):
                    opp_val = getattr(item, "smm_Base1MeasurementRelationship41", None)
                    
                    setattr(item, "smm_Base1MeasurementRelationship41", self)
                    

class DimensionalMeasurement:

    pass
class smm_CollectiveMeasurement(DimensionalMeasurement):

    def __init__(self, isBaseSupplied: str, smm_CollectiveMeasurement: set["smm_BaseNMeasurementRelationship"] = None, smm_CollectiveMeasurement22: "smm_Operation" = None):
        self.isBaseSupplied = isBaseSupplied
        self.smm_CollectiveMeasurement = smm_CollectiveMeasurement if smm_CollectiveMeasurement is not None else set()
        self.smm_CollectiveMeasurement22 = smm_CollectiveMeasurement22
        
    @property
    def isBaseSupplied(self) -> str:
        return self.__isBaseSupplied

    @isBaseSupplied.setter
    def isBaseSupplied(self, isBaseSupplied: str):
        self.__isBaseSupplied = isBaseSupplied

    @property
    def smm_CollectiveMeasurement(self):
        return self.__smm_CollectiveMeasurement

    @smm_CollectiveMeasurement.setter
    def smm_CollectiveMeasurement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_CollectiveMeasurement__smm_CollectiveMeasurement", None)
        self.__smm_CollectiveMeasurement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smm_BaseNMeasurementRelationship"):
                    opp_val = getattr(item, "smm_BaseNMeasurementRelationship", None)
                    
                    if opp_val == self:
                        setattr(item, "smm_BaseNMeasurementRelationship", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smm_BaseNMeasurementRelationship"):
                    opp_val = getattr(item, "smm_BaseNMeasurementRelationship", None)
                    
                    setattr(item, "smm_BaseNMeasurementRelationship", self)
                    

    @property
    def smm_CollectiveMeasurement22(self):
        return self.__smm_CollectiveMeasurement22

    @smm_CollectiveMeasurement22.setter
    def smm_CollectiveMeasurement22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_CollectiveMeasurement__smm_CollectiveMeasurement22", None)
        self.__smm_CollectiveMeasurement22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_Operation23"):
                opp_val = getattr(old_value, "smm_Operation23", None)
                if opp_val == self:
                    setattr(old_value, "smm_Operation23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_Operation23"):
                opp_val = getattr(value, "smm_Operation23", None)
                setattr(value, "smm_Operation23", self)

class smm_RescaledMeasurement(DimensionalMeasurement):

    def __init__(self, isBaseSupplied: str, smm_RescaledMeasurement: "smm_RescaledMeasurementRelationship" = None, smm_RescaledMeasurement152: "smm_Operation" = None):
        self.isBaseSupplied = isBaseSupplied
        self.smm_RescaledMeasurement = smm_RescaledMeasurement
        self.smm_RescaledMeasurement152 = smm_RescaledMeasurement152
        
    @property
    def isBaseSupplied(self) -> str:
        return self.__isBaseSupplied

    @isBaseSupplied.setter
    def isBaseSupplied(self, isBaseSupplied: str):
        self.__isBaseSupplied = isBaseSupplied

    @property
    def smm_RescaledMeasurement(self):
        return self.__smm_RescaledMeasurement

    @smm_RescaledMeasurement.setter
    def smm_RescaledMeasurement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_RescaledMeasurement__smm_RescaledMeasurement", None)
        self.__smm_RescaledMeasurement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_RescaledMeasurementRelationship150"):
                opp_val = getattr(old_value, "smm_RescaledMeasurementRelationship150", None)
                if opp_val == self:
                    setattr(old_value, "smm_RescaledMeasurementRelationship150", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_RescaledMeasurementRelationship150"):
                opp_val = getattr(value, "smm_RescaledMeasurementRelationship150", None)
                setattr(value, "smm_RescaledMeasurementRelationship150", self)

    @property
    def smm_RescaledMeasurement152(self):
        return self.__smm_RescaledMeasurement152

    @smm_RescaledMeasurement152.setter
    def smm_RescaledMeasurement152(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_RescaledMeasurement__smm_RescaledMeasurement152", None)
        self.__smm_RescaledMeasurement152 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_Operation153"):
                opp_val = getattr(old_value, "smm_Operation153", None)
                if opp_val == self:
                    setattr(old_value, "smm_Operation153", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_Operation153"):
                opp_val = getattr(value, "smm_Operation153", None)
                setattr(value, "smm_Operation153", self)

class smm_RankingMeasurement(DimensionalMeasurement):

    def __init__(self, isBaseSupplied: str, smm_RankingMeasurement: "smm_Operation" = None, smm_RankingMeasurement188: "smm_RankingMeasurementRelationship" = None):
        self.isBaseSupplied = isBaseSupplied
        self.smm_RankingMeasurement = smm_RankingMeasurement
        self.smm_RankingMeasurement188 = smm_RankingMeasurement188
        
    @property
    def isBaseSupplied(self) -> str:
        return self.__isBaseSupplied

    @isBaseSupplied.setter
    def isBaseSupplied(self, isBaseSupplied: str):
        self.__isBaseSupplied = isBaseSupplied

    @property
    def smm_RankingMeasurement(self):
        return self.__smm_RankingMeasurement

    @smm_RankingMeasurement.setter
    def smm_RankingMeasurement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_RankingMeasurement__smm_RankingMeasurement", None)
        self.__smm_RankingMeasurement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_Operation186"):
                opp_val = getattr(old_value, "smm_Operation186", None)
                if opp_val == self:
                    setattr(old_value, "smm_Operation186", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_Operation186"):
                opp_val = getattr(value, "smm_Operation186", None)
                setattr(value, "smm_Operation186", self)

    @property
    def smm_RankingMeasurement188(self):
        return self.__smm_RankingMeasurement188

    @smm_RankingMeasurement188.setter
    def smm_RankingMeasurement188(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_RankingMeasurement__smm_RankingMeasurement188", None)
        self.__smm_RankingMeasurement188 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_RankingMeasurementRelationship189"):
                opp_val = getattr(old_value, "smm_RankingMeasurementRelationship189", None)
                if opp_val == self:
                    setattr(old_value, "smm_RankingMeasurementRelationship189", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_RankingMeasurementRelationship189"):
                opp_val = getattr(value, "smm_RankingMeasurementRelationship189", None)
                setattr(value, "smm_RankingMeasurementRelationship189", self)

class smm_DirectMeasurement(DimensionalMeasurement):

    pass
class smm_NamedMeasurement(DimensionalMeasurement):

    pass
class smm_BinaryMeasurement(DimensionalMeasurement):

    def __init__(self, isBaseSupplied: str, smm_BinaryMeasurement: "smm_Base2MeasurementRelationship" = None, smm_BinaryMeasurement10: "smm_Base1MeasurementRelationship" = None, smm_BinaryMeasurement12: "smm_Operation" = None):
        self.isBaseSupplied = isBaseSupplied
        self.smm_BinaryMeasurement = smm_BinaryMeasurement
        self.smm_BinaryMeasurement10 = smm_BinaryMeasurement10
        self.smm_BinaryMeasurement12 = smm_BinaryMeasurement12
        
    @property
    def isBaseSupplied(self) -> str:
        return self.__isBaseSupplied

    @isBaseSupplied.setter
    def isBaseSupplied(self, isBaseSupplied: str):
        self.__isBaseSupplied = isBaseSupplied

    @property
    def smm_BinaryMeasurement12(self):
        return self.__smm_BinaryMeasurement12

    @smm_BinaryMeasurement12.setter
    def smm_BinaryMeasurement12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_BinaryMeasurement__smm_BinaryMeasurement12", None)
        self.__smm_BinaryMeasurement12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_Operation13"):
                opp_val = getattr(old_value, "smm_Operation13", None)
                if opp_val == self:
                    setattr(old_value, "smm_Operation13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_Operation13"):
                opp_val = getattr(value, "smm_Operation13", None)
                setattr(value, "smm_Operation13", self)

    @property
    def smm_BinaryMeasurement(self):
        return self.__smm_BinaryMeasurement

    @smm_BinaryMeasurement.setter
    def smm_BinaryMeasurement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_BinaryMeasurement__smm_BinaryMeasurement", None)
        self.__smm_BinaryMeasurement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_Base2MeasurementRelationship"):
                opp_val = getattr(old_value, "smm_Base2MeasurementRelationship", None)
                if opp_val == self:
                    setattr(old_value, "smm_Base2MeasurementRelationship", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_Base2MeasurementRelationship"):
                opp_val = getattr(value, "smm_Base2MeasurementRelationship", None)
                setattr(value, "smm_Base2MeasurementRelationship", self)

    @property
    def smm_BinaryMeasurement10(self):
        return self.__smm_BinaryMeasurement10

    @smm_BinaryMeasurement10.setter
    def smm_BinaryMeasurement10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_BinaryMeasurement__smm_BinaryMeasurement10", None)
        self.__smm_BinaryMeasurement10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_Base1MeasurementRelationship"):
                opp_val = getattr(old_value, "smm_Base1MeasurementRelationship", None)
                if opp_val == self:
                    setattr(old_value, "smm_Base1MeasurementRelationship", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_Base1MeasurementRelationship"):
                opp_val = getattr(value, "smm_Base1MeasurementRelationship", None)
                setattr(value, "smm_Base1MeasurementRelationship", self)

class DimensionalMeasure:

    pass
class smm_RescaledMeasure(DimensionalMeasure):

    def __init__(self, offset: float, multiplier: float, operationFirst: str, smm_RescaledMeasure: set["smm_RescaledMeasureRelationship"] = None, rescaledMeasure: "smm_ScaledBaseMeasureRelationship" = None, smm_RescaledMeasure147: "smm_Operation" = None, RescaledMeasure: "smm_ScaledBaseMeasureRelationship" = None):
        self.offset = offset
        self.multiplier = multiplier
        self.operationFirst = operationFirst
        self.smm_RescaledMeasure = smm_RescaledMeasure if smm_RescaledMeasure is not None else set()
        self.rescaledMeasure = rescaledMeasure
        self.smm_RescaledMeasure147 = smm_RescaledMeasure147
        self.RescaledMeasure = RescaledMeasure
        
    @property
    def multiplier(self) -> float:
        return self.__multiplier

    @multiplier.setter
    def multiplier(self, multiplier: float):
        self.__multiplier = multiplier

    @property
    def operationFirst(self) -> str:
        return self.__operationFirst

    @operationFirst.setter
    def operationFirst(self, operationFirst: str):
        self.__operationFirst = operationFirst

    @property
    def offset(self) -> float:
        return self.__offset

    @offset.setter
    def offset(self, offset: float):
        self.__offset = offset

    @property
    def smm_RescaledMeasure147(self):
        return self.__smm_RescaledMeasure147

    @smm_RescaledMeasure147.setter
    def smm_RescaledMeasure147(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_RescaledMeasure__smm_RescaledMeasure147", None)
        self.__smm_RescaledMeasure147 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_Operation148"):
                opp_val = getattr(old_value, "smm_Operation148", None)
                if opp_val == self:
                    setattr(old_value, "smm_Operation148", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_Operation148"):
                opp_val = getattr(value, "smm_Operation148", None)
                setattr(value, "smm_Operation148", self)

    @property
    def smm_RescaledMeasure(self):
        return self.__smm_RescaledMeasure

    @smm_RescaledMeasure.setter
    def smm_RescaledMeasure(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_RescaledMeasure__smm_RescaledMeasure", None)
        self.__smm_RescaledMeasure = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smm_RescaledMeasureRelationship144"):
                    opp_val = getattr(item, "smm_RescaledMeasureRelationship144", None)
                    
                    if opp_val == self:
                        setattr(item, "smm_RescaledMeasureRelationship144", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smm_RescaledMeasureRelationship144"):
                    opp_val = getattr(item, "smm_RescaledMeasureRelationship144", None)
                    
                    setattr(item, "smm_RescaledMeasureRelationship144", self)
                    

    @property
    def rescaledMeasure(self):
        return self.__rescaledMeasure

    @rescaledMeasure.setter
    def rescaledMeasure(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_RescaledMeasure__rescaledMeasure", None)
        self.__rescaledMeasure = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ScaledBaseMeasureRelationship"):
                opp_val = getattr(old_value, "ScaledBaseMeasureRelationship", None)
                if opp_val == self:
                    setattr(old_value, "ScaledBaseMeasureRelationship", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ScaledBaseMeasureRelationship"):
                opp_val = getattr(value, "ScaledBaseMeasureRelationship", None)
                setattr(value, "ScaledBaseMeasureRelationship", self)

    @property
    def RescaledMeasure(self):
        return self.__RescaledMeasure

    @RescaledMeasure.setter
    def RescaledMeasure(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_RescaledMeasure__RescaledMeasure", None)
        self.__RescaledMeasure = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rescales"):
                opp_val = getattr(old_value, "rescales", None)
                if opp_val == self:
                    setattr(old_value, "rescales", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rescales"):
                opp_val = getattr(value, "rescales", None)
                setattr(value, "rescales", self)

class smm_RankingMeasure(DimensionalMeasure):

    pass
class smm_NamedMeasure(DimensionalMeasure):

    pass
class smm_DirectMeasure(DimensionalMeasure):

    pass
class smm_BinaryMeasure(DimensionalMeasure):

    def __init__(self, functor: str, smm_BinaryMeasure: "smm_Base1MeasureRelationship" = None, smm_BinaryMeasure5: "smm_Base2MeasureRelationship" = None, smm_BinaryMeasure7: "smm_Operation" = None):
        self.functor = functor
        self.smm_BinaryMeasure = smm_BinaryMeasure
        self.smm_BinaryMeasure5 = smm_BinaryMeasure5
        self.smm_BinaryMeasure7 = smm_BinaryMeasure7
        
    @property
    def functor(self) -> str:
        return self.__functor

    @functor.setter
    def functor(self, functor: str):
        self.__functor = functor

    @property
    def smm_BinaryMeasure(self):
        return self.__smm_BinaryMeasure

    @smm_BinaryMeasure.setter
    def smm_BinaryMeasure(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_BinaryMeasure__smm_BinaryMeasure", None)
        self.__smm_BinaryMeasure = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_Base1MeasureRelationship"):
                opp_val = getattr(old_value, "smm_Base1MeasureRelationship", None)
                if opp_val == self:
                    setattr(old_value, "smm_Base1MeasureRelationship", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_Base1MeasureRelationship"):
                opp_val = getattr(value, "smm_Base1MeasureRelationship", None)
                setattr(value, "smm_Base1MeasureRelationship", self)

    @property
    def smm_BinaryMeasure7(self):
        return self.__smm_BinaryMeasure7

    @smm_BinaryMeasure7.setter
    def smm_BinaryMeasure7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_BinaryMeasure__smm_BinaryMeasure7", None)
        self.__smm_BinaryMeasure7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_Operation"):
                opp_val = getattr(old_value, "smm_Operation", None)
                if opp_val == self:
                    setattr(old_value, "smm_Operation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_Operation"):
                opp_val = getattr(value, "smm_Operation", None)
                setattr(value, "smm_Operation", self)

    @property
    def smm_BinaryMeasure5(self):
        return self.__smm_BinaryMeasure5

    @smm_BinaryMeasure5.setter
    def smm_BinaryMeasure5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_BinaryMeasure__smm_BinaryMeasure5", None)
        self.__smm_BinaryMeasure5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_Base2MeasureRelationship"):
                opp_val = getattr(old_value, "smm_Base2MeasureRelationship", None)
                if opp_val == self:
                    setattr(old_value, "smm_Base2MeasureRelationship", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_Base2MeasureRelationship"):
                opp_val = getattr(value, "smm_Base2MeasureRelationship", None)
                setattr(value, "smm_Base2MeasureRelationship", self)

class ScaledBaseMeasurementRelationship:

    pass
class smm_BaseNMeasurementRelationship(ScaledBaseMeasurementRelationship):

    pass
class smm_RankingMeasurementRelationship(ScaledBaseMeasurementRelationship):

    pass
class smm_GradeMeasurementRelationship(ScaledBaseMeasurementRelationship):

    pass
class smm_Base2MeasurementRelationship(ScaledBaseMeasurementRelationship):

    pass
class smm_Base1MeasurementRelationship(ScaledBaseMeasurementRelationship):

    pass
class ScaledBaseMeasureRelationship:

    pass
class smm_RankingMeasureRelationship(ScaledBaseMeasureRelationship):

    pass
class smm_Base2MeasureRelationship(ScaledBaseMeasureRelationship):

    pass
class smm_GradeMeasureRelationship(ScaledBaseMeasureRelationship):

    pass
class smm_BaseNMeasureRelationship(ScaledBaseMeasureRelationship):

    pass
class smm_Base1MeasureRelationship(ScaledBaseMeasureRelationship):

    pass
class smm_CollectiveMeasure(DimensionalMeasure):

    def __init__(self, accumulator: str, smm_CollectiveMeasure: set["smm_BaseNMeasureRelationship"] = None, smm_CollectiveMeasure18: "smm_Operation" = None):
        self.accumulator = accumulator
        self.smm_CollectiveMeasure = smm_CollectiveMeasure if smm_CollectiveMeasure is not None else set()
        self.smm_CollectiveMeasure18 = smm_CollectiveMeasure18
        
    @property
    def accumulator(self) -> str:
        return self.__accumulator

    @accumulator.setter
    def accumulator(self, accumulator: str):
        self.__accumulator = accumulator

    @property
    def smm_CollectiveMeasure(self):
        return self.__smm_CollectiveMeasure

    @smm_CollectiveMeasure.setter
    def smm_CollectiveMeasure(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_CollectiveMeasure__smm_CollectiveMeasure", None)
        self.__smm_CollectiveMeasure = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smm_BaseNMeasureRelationship"):
                    opp_val = getattr(item, "smm_BaseNMeasureRelationship", None)
                    
                    if opp_val == self:
                        setattr(item, "smm_BaseNMeasureRelationship", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smm_BaseNMeasureRelationship"):
                    opp_val = getattr(item, "smm_BaseNMeasureRelationship", None)
                    
                    setattr(item, "smm_BaseNMeasureRelationship", self)
                    

    @property
    def smm_CollectiveMeasure18(self):
        return self.__smm_CollectiveMeasure18

    @smm_CollectiveMeasure18.setter
    def smm_CollectiveMeasure18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_CollectiveMeasure__smm_CollectiveMeasure18", None)
        self.__smm_CollectiveMeasure18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_Operation19"):
                opp_val = getattr(old_value, "smm_Operation19", None)
                if opp_val == self:
                    setattr(old_value, "smm_Operation19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_Operation19"):
                opp_val = getattr(value, "smm_Operation19", None)
                setattr(value, "smm_Operation19", self)

class AbstractMeasureElement:

    pass
class smm_Scope(AbstractMeasureElement):

    pass
class smm_Operation(AbstractMeasureElement):

    def __init__(self, body: str, language: str, smm_Operation13: "smm_BinaryMeasurement" = None, smm_Operation19: "smm_CollectiveMeasure" = None, smm_Operation: "smm_BinaryMeasure" = None, smm_Operation55: "smm_DirectMeasure" = None, smm_Operation57: "smm_EquivalentMeasureRelationship" = None, smm_Operation23: "smm_CollectiveMeasurement" = None, smm_Operation62: "smm_GradeMeasurement" = None, smm_Operation80: "smm_Measure" = None, smm_Operation103: "smm_MeasureRelationship" = None, smm_Operation156: "smm_Scope" = None, smm_Operation159: "smm_Scope" = None, smm_Operation148: "smm_RescaledMeasure" = None, smm_Operation153: "smm_RescaledMeasurement" = None, smm_Operation186: "smm_RankingMeasurement" = None):
        self.body = body
        self.language = language
        self.smm_Operation13 = smm_Operation13
        self.smm_Operation19 = smm_Operation19
        self.smm_Operation = smm_Operation
        self.smm_Operation55 = smm_Operation55
        self.smm_Operation57 = smm_Operation57
        self.smm_Operation23 = smm_Operation23
        self.smm_Operation62 = smm_Operation62
        self.smm_Operation80 = smm_Operation80
        self.smm_Operation103 = smm_Operation103
        self.smm_Operation156 = smm_Operation156
        self.smm_Operation159 = smm_Operation159
        self.smm_Operation148 = smm_Operation148
        self.smm_Operation153 = smm_Operation153
        self.smm_Operation186 = smm_Operation186
        
    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language

    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def smm_Operation103(self):
        return self.__smm_Operation103

    @smm_Operation103.setter
    def smm_Operation103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Operation__smm_Operation103", None)
        self.__smm_Operation103 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_MeasureRelationship102"):
                opp_val = getattr(old_value, "smm_MeasureRelationship102", None)
                if opp_val == self:
                    setattr(old_value, "smm_MeasureRelationship102", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_MeasureRelationship102"):
                opp_val = getattr(value, "smm_MeasureRelationship102", None)
                setattr(value, "smm_MeasureRelationship102", self)

    @property
    def smm_Operation159(self):
        return self.__smm_Operation159

    @smm_Operation159.setter
    def smm_Operation159(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Operation__smm_Operation159", None)
        self.__smm_Operation159 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_Scope158"):
                opp_val = getattr(old_value, "smm_Scope158", None)
                if opp_val == self:
                    setattr(old_value, "smm_Scope158", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_Scope158"):
                opp_val = getattr(value, "smm_Scope158", None)
                setattr(value, "smm_Scope158", self)

    @property
    def smm_Operation13(self):
        return self.__smm_Operation13

    @smm_Operation13.setter
    def smm_Operation13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Operation__smm_Operation13", None)
        self.__smm_Operation13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_BinaryMeasurement12"):
                opp_val = getattr(old_value, "smm_BinaryMeasurement12", None)
                if opp_val == self:
                    setattr(old_value, "smm_BinaryMeasurement12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_BinaryMeasurement12"):
                opp_val = getattr(value, "smm_BinaryMeasurement12", None)
                setattr(value, "smm_BinaryMeasurement12", self)

    @property
    def smm_Operation19(self):
        return self.__smm_Operation19

    @smm_Operation19.setter
    def smm_Operation19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Operation__smm_Operation19", None)
        self.__smm_Operation19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_CollectiveMeasure18"):
                opp_val = getattr(old_value, "smm_CollectiveMeasure18", None)
                if opp_val == self:
                    setattr(old_value, "smm_CollectiveMeasure18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_CollectiveMeasure18"):
                opp_val = getattr(value, "smm_CollectiveMeasure18", None)
                setattr(value, "smm_CollectiveMeasure18", self)

    @property
    def smm_Operation(self):
        return self.__smm_Operation

    @smm_Operation.setter
    def smm_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Operation__smm_Operation", None)
        self.__smm_Operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_BinaryMeasure7"):
                opp_val = getattr(old_value, "smm_BinaryMeasure7", None)
                if opp_val == self:
                    setattr(old_value, "smm_BinaryMeasure7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_BinaryMeasure7"):
                opp_val = getattr(value, "smm_BinaryMeasure7", None)
                setattr(value, "smm_BinaryMeasure7", self)

    @property
    def smm_Operation57(self):
        return self.__smm_Operation57

    @smm_Operation57.setter
    def smm_Operation57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Operation__smm_Operation57", None)
        self.__smm_Operation57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_EquivalentMeasureRelationship"):
                opp_val = getattr(old_value, "smm_EquivalentMeasureRelationship", None)
                if opp_val == self:
                    setattr(old_value, "smm_EquivalentMeasureRelationship", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_EquivalentMeasureRelationship"):
                opp_val = getattr(value, "smm_EquivalentMeasureRelationship", None)
                setattr(value, "smm_EquivalentMeasureRelationship", self)

    @property
    def smm_Operation148(self):
        return self.__smm_Operation148

    @smm_Operation148.setter
    def smm_Operation148(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Operation__smm_Operation148", None)
        self.__smm_Operation148 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_RescaledMeasure147"):
                opp_val = getattr(old_value, "smm_RescaledMeasure147", None)
                if opp_val == self:
                    setattr(old_value, "smm_RescaledMeasure147", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_RescaledMeasure147"):
                opp_val = getattr(value, "smm_RescaledMeasure147", None)
                setattr(value, "smm_RescaledMeasure147", self)

    @property
    def smm_Operation153(self):
        return self.__smm_Operation153

    @smm_Operation153.setter
    def smm_Operation153(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Operation__smm_Operation153", None)
        self.__smm_Operation153 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_RescaledMeasurement152"):
                opp_val = getattr(old_value, "smm_RescaledMeasurement152", None)
                if opp_val == self:
                    setattr(old_value, "smm_RescaledMeasurement152", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_RescaledMeasurement152"):
                opp_val = getattr(value, "smm_RescaledMeasurement152", None)
                setattr(value, "smm_RescaledMeasurement152", self)

    @property
    def smm_Operation80(self):
        return self.__smm_Operation80

    @smm_Operation80.setter
    def smm_Operation80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Operation__smm_Operation80", None)
        self.__smm_Operation80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_Measure79"):
                opp_val = getattr(old_value, "smm_Measure79", None)
                if opp_val == self:
                    setattr(old_value, "smm_Measure79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_Measure79"):
                opp_val = getattr(value, "smm_Measure79", None)
                setattr(value, "smm_Measure79", self)

    @property
    def smm_Operation23(self):
        return self.__smm_Operation23

    @smm_Operation23.setter
    def smm_Operation23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Operation__smm_Operation23", None)
        self.__smm_Operation23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_CollectiveMeasurement22"):
                opp_val = getattr(old_value, "smm_CollectiveMeasurement22", None)
                if opp_val == self:
                    setattr(old_value, "smm_CollectiveMeasurement22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_CollectiveMeasurement22"):
                opp_val = getattr(value, "smm_CollectiveMeasurement22", None)
                setattr(value, "smm_CollectiveMeasurement22", self)

    @property
    def smm_Operation55(self):
        return self.__smm_Operation55

    @smm_Operation55.setter
    def smm_Operation55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Operation__smm_Operation55", None)
        self.__smm_Operation55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_DirectMeasure"):
                opp_val = getattr(old_value, "smm_DirectMeasure", None)
                if opp_val == self:
                    setattr(old_value, "smm_DirectMeasure", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_DirectMeasure"):
                opp_val = getattr(value, "smm_DirectMeasure", None)
                setattr(value, "smm_DirectMeasure", self)

    @property
    def smm_Operation156(self):
        return self.__smm_Operation156

    @smm_Operation156.setter
    def smm_Operation156(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Operation__smm_Operation156", None)
        self.__smm_Operation156 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_Scope155"):
                opp_val = getattr(old_value, "smm_Scope155", None)
                if opp_val == self:
                    setattr(old_value, "smm_Scope155", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_Scope155"):
                opp_val = getattr(value, "smm_Scope155", None)
                setattr(value, "smm_Scope155", self)

    @property
    def smm_Operation62(self):
        return self.__smm_Operation62

    @smm_Operation62.setter
    def smm_Operation62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Operation__smm_Operation62", None)
        self.__smm_Operation62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_GradeMeasurement61"):
                opp_val = getattr(old_value, "smm_GradeMeasurement61", None)
                if opp_val == self:
                    setattr(old_value, "smm_GradeMeasurement61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_GradeMeasurement61"):
                opp_val = getattr(value, "smm_GradeMeasurement61", None)
                setattr(value, "smm_GradeMeasurement61", self)

    @property
    def smm_Operation186(self):
        return self.__smm_Operation186

    @smm_Operation186.setter
    def smm_Operation186(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Operation__smm_Operation186", None)
        self.__smm_Operation186 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_RankingMeasurement"):
                opp_val = getattr(old_value, "smm_RankingMeasurement", None)
                if opp_val == self:
                    setattr(old_value, "smm_RankingMeasurement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_RankingMeasurement"):
                opp_val = getattr(value, "smm_RankingMeasurement", None)
                setattr(value, "smm_RankingMeasurement", self)

    def getParamStrings(self) -> str:
        # TODO: Implement getParamStrings method
        pass

class smm_Measure(AbstractMeasureElement):

    def __init__(self, source: str, measureLabelFormat: str, measurementLabelFormat: str, scale: str, customScale: str, visible: str, smm_Measure: set["smm_RefinementMeasureRelationship"] = None, smm_Measure65: set["smm_RefinementMeasureRelationship"] = None, smm_Measure68: set["smm_MeasureRelationship"] = None, smm_Measure70: set["smm_MeasureRelationship"] = None, smm_Measure73: set["smm_EquivalentMeasureRelationship"] = None, smm_Measure76: set["smm_EquivalentMeasureRelationship"] = None, smm_Measure79: "smm_Operation" = None, categoryMeasure: set["smm_MeasureCategory"] = None, smm_Measure83: "smm_Scope" = None, smm_Measure85: "smm_Characteristic" = None, smm_Measure88: set["smm_MeasureRelationship"] = None, Measure: "smm_MeasureCategory" = None, smm_Measure138: "smm_ObservedMeasure" = None):
        self.source = source
        self.measureLabelFormat = measureLabelFormat
        self.measurementLabelFormat = measurementLabelFormat
        self.scale = scale
        self.customScale = customScale
        self.visible = visible
        self.smm_Measure = smm_Measure if smm_Measure is not None else set()
        self.smm_Measure65 = smm_Measure65 if smm_Measure65 is not None else set()
        self.smm_Measure68 = smm_Measure68 if smm_Measure68 is not None else set()
        self.smm_Measure70 = smm_Measure70 if smm_Measure70 is not None else set()
        self.smm_Measure73 = smm_Measure73 if smm_Measure73 is not None else set()
        self.smm_Measure76 = smm_Measure76 if smm_Measure76 is not None else set()
        self.smm_Measure79 = smm_Measure79
        self.categoryMeasure = categoryMeasure if categoryMeasure is not None else set()
        self.smm_Measure83 = smm_Measure83
        self.smm_Measure85 = smm_Measure85
        self.smm_Measure88 = smm_Measure88 if smm_Measure88 is not None else set()
        self.Measure = Measure
        self.smm_Measure138 = smm_Measure138
        
    @property
    def measureLabelFormat(self) -> str:
        return self.__measureLabelFormat

    @measureLabelFormat.setter
    def measureLabelFormat(self, measureLabelFormat: str):
        self.__measureLabelFormat = measureLabelFormat

    @property
    def scale(self) -> str:
        return self.__scale

    @scale.setter
    def scale(self, scale: str):
        self.__scale = scale

    @property
    def source(self) -> str:
        return self.__source

    @source.setter
    def source(self, source: str):
        self.__source = source

    @property
    def customScale(self) -> str:
        return self.__customScale

    @customScale.setter
    def customScale(self, customScale: str):
        self.__customScale = customScale

    @property
    def measurementLabelFormat(self) -> str:
        return self.__measurementLabelFormat

    @measurementLabelFormat.setter
    def measurementLabelFormat(self, measurementLabelFormat: str):
        self.__measurementLabelFormat = measurementLabelFormat

    @property
    def visible(self) -> str:
        return self.__visible

    @visible.setter
    def visible(self, visible: str):
        self.__visible = visible

    @property
    def smm_Measure73(self):
        return self.__smm_Measure73

    @smm_Measure73.setter
    def smm_Measure73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measure__smm_Measure73", None)
        self.__smm_Measure73 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smm_EquivalentMeasureRelationship74"):
                    opp_val = getattr(item, "smm_EquivalentMeasureRelationship74", None)
                    
                    if opp_val == self:
                        setattr(item, "smm_EquivalentMeasureRelationship74", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smm_EquivalentMeasureRelationship74"):
                    opp_val = getattr(item, "smm_EquivalentMeasureRelationship74", None)
                    
                    setattr(item, "smm_EquivalentMeasureRelationship74", self)
                    

    @property
    def categoryMeasure(self):
        return self.__categoryMeasure

    @categoryMeasure.setter
    def categoryMeasure(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measure__categoryMeasure", None)
        self.__categoryMeasure = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MeasureCategory"):
                    opp_val = getattr(item, "MeasureCategory", None)
                    
                    if opp_val == self:
                        setattr(item, "MeasureCategory", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MeasureCategory"):
                    opp_val = getattr(item, "MeasureCategory", None)
                    
                    setattr(item, "MeasureCategory", self)
                    

    @property
    def smm_Measure76(self):
        return self.__smm_Measure76

    @smm_Measure76.setter
    def smm_Measure76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measure__smm_Measure76", None)
        self.__smm_Measure76 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smm_EquivalentMeasureRelationship77"):
                    opp_val = getattr(item, "smm_EquivalentMeasureRelationship77", None)
                    
                    if opp_val == self:
                        setattr(item, "smm_EquivalentMeasureRelationship77", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smm_EquivalentMeasureRelationship77"):
                    opp_val = getattr(item, "smm_EquivalentMeasureRelationship77", None)
                    
                    setattr(item, "smm_EquivalentMeasureRelationship77", self)
                    

    @property
    def smm_Measure85(self):
        return self.__smm_Measure85

    @smm_Measure85.setter
    def smm_Measure85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measure__smm_Measure85", None)
        self.__smm_Measure85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_Characteristic86"):
                opp_val = getattr(old_value, "smm_Characteristic86", None)
                if opp_val == self:
                    setattr(old_value, "smm_Characteristic86", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_Characteristic86"):
                opp_val = getattr(value, "smm_Characteristic86", None)
                setattr(value, "smm_Characteristic86", self)

    @property
    def smm_Measure70(self):
        return self.__smm_Measure70

    @smm_Measure70.setter
    def smm_Measure70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measure__smm_Measure70", None)
        self.__smm_Measure70 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smm_MeasureRelationship71"):
                    opp_val = getattr(item, "smm_MeasureRelationship71", None)
                    
                    if opp_val == self:
                        setattr(item, "smm_MeasureRelationship71", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smm_MeasureRelationship71"):
                    opp_val = getattr(item, "smm_MeasureRelationship71", None)
                    
                    setattr(item, "smm_MeasureRelationship71", self)
                    

    @property
    def smm_Measure83(self):
        return self.__smm_Measure83

    @smm_Measure83.setter
    def smm_Measure83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measure__smm_Measure83", None)
        self.__smm_Measure83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_Scope"):
                opp_val = getattr(old_value, "smm_Scope", None)
                if opp_val == self:
                    setattr(old_value, "smm_Scope", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_Scope"):
                opp_val = getattr(value, "smm_Scope", None)
                setattr(value, "smm_Scope", self)

    @property
    def Measure(self):
        return self.__Measure

    @Measure.setter
    def Measure(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measure__Measure", None)
        self.__Measure = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "category"):
                opp_val = getattr(old_value, "category", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "category"):
                opp_val = getattr(value, "category", None)
                if opp_val is None:
                    setattr(value, "category", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def smm_Measure(self):
        return self.__smm_Measure

    @smm_Measure.setter
    def smm_Measure(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measure__smm_Measure", None)
        self.__smm_Measure = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smm_RefinementMeasureRelationship"):
                    opp_val = getattr(item, "smm_RefinementMeasureRelationship", None)
                    
                    if opp_val == self:
                        setattr(item, "smm_RefinementMeasureRelationship", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smm_RefinementMeasureRelationship"):
                    opp_val = getattr(item, "smm_RefinementMeasureRelationship", None)
                    
                    setattr(item, "smm_RefinementMeasureRelationship", self)
                    

    @property
    def smm_Measure138(self):
        return self.__smm_Measure138

    @smm_Measure138.setter
    def smm_Measure138(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measure__smm_Measure138", None)
        self.__smm_Measure138 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_ObservedMeasure137"):
                opp_val = getattr(old_value, "smm_ObservedMeasure137", None)
                if opp_val == self:
                    setattr(old_value, "smm_ObservedMeasure137", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_ObservedMeasure137"):
                opp_val = getattr(value, "smm_ObservedMeasure137", None)
                setattr(value, "smm_ObservedMeasure137", self)

    @property
    def smm_Measure68(self):
        return self.__smm_Measure68

    @smm_Measure68.setter
    def smm_Measure68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measure__smm_Measure68", None)
        self.__smm_Measure68 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smm_MeasureRelationship"):
                    opp_val = getattr(item, "smm_MeasureRelationship", None)
                    
                    if opp_val == self:
                        setattr(item, "smm_MeasureRelationship", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smm_MeasureRelationship"):
                    opp_val = getattr(item, "smm_MeasureRelationship", None)
                    
                    setattr(item, "smm_MeasureRelationship", self)
                    

    @property
    def smm_Measure65(self):
        return self.__smm_Measure65

    @smm_Measure65.setter
    def smm_Measure65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measure__smm_Measure65", None)
        self.__smm_Measure65 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smm_RefinementMeasureRelationship66"):
                    opp_val = getattr(item, "smm_RefinementMeasureRelationship66", None)
                    
                    if opp_val == self:
                        setattr(item, "smm_RefinementMeasureRelationship66", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smm_RefinementMeasureRelationship66"):
                    opp_val = getattr(item, "smm_RefinementMeasureRelationship66", None)
                    
                    setattr(item, "smm_RefinementMeasureRelationship66", self)
                    

    @property
    def smm_Measure88(self):
        return self.__smm_Measure88

    @smm_Measure88.setter
    def smm_Measure88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measure__smm_Measure88", None)
        self.__smm_Measure88 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smm_MeasureRelationship89"):
                    opp_val = getattr(item, "smm_MeasureRelationship89", None)
                    
                    if opp_val == self:
                        setattr(item, "smm_MeasureRelationship89", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smm_MeasureRelationship89"):
                    opp_val = getattr(item, "smm_MeasureRelationship89", None)
                    
                    setattr(item, "smm_MeasureRelationship89", self)
                    

    @property
    def smm_Measure79(self):
        return self.__smm_Measure79

    @smm_Measure79.setter
    def smm_Measure79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measure__smm_Measure79", None)
        self.__smm_Measure79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_Operation80"):
                opp_val = getattr(old_value, "smm_Operation80", None)
                if opp_val == self:
                    setattr(old_value, "smm_Operation80", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_Operation80"):
                opp_val = getattr(value, "smm_Operation80", None)
                setattr(value, "smm_Operation80", self)

    def getAllArguments(self) -> str:
        # TODO: Implement getAllArguments method
        pass

    def getArguments(self) -> str:
        # TODO: Implement getArguments method
        pass

class smm_OCLOperation(AbstractMeasureElement):

    def __init__(self, body: str, context: str):
        self.body = body
        self.context = context
        
    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def context(self) -> str:
        return self.__context

    @context.setter
    def context(self, context: str):
        self.__context = context

class smm_MeasureCategory(AbstractMeasureElement):

    pass
class smm_UnitOfMeasure(AbstractMeasureElement):

    pass
class smm_Characteristic(AbstractMeasureElement):

    pass
class SmmRelationship:

    pass
class smm_MeasurementRelationship(SmmRelationship):

    pass
class smm_MeasureRelationship(SmmRelationship):

    def __init__(self, influence: str, smm_MeasureRelationship: "smm_Measure" = None, smm_MeasureRelationship71: "smm_Measure" = None, smm_MeasureRelationship89: "smm_Measure" = None, smm_MeasureRelationship102: "smm_Operation" = None):
        self.influence = influence
        self.smm_MeasureRelationship = smm_MeasureRelationship
        self.smm_MeasureRelationship71 = smm_MeasureRelationship71
        self.smm_MeasureRelationship89 = smm_MeasureRelationship89
        self.smm_MeasureRelationship102 = smm_MeasureRelationship102
        
    @property
    def influence(self) -> str:
        return self.__influence

    @influence.setter
    def influence(self, influence: str):
        self.__influence = influence

    @property
    def smm_MeasureRelationship102(self):
        return self.__smm_MeasureRelationship102

    @smm_MeasureRelationship102.setter
    def smm_MeasureRelationship102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_MeasureRelationship__smm_MeasureRelationship102", None)
        self.__smm_MeasureRelationship102 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_Operation103"):
                opp_val = getattr(old_value, "smm_Operation103", None)
                if opp_val == self:
                    setattr(old_value, "smm_Operation103", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_Operation103"):
                opp_val = getattr(value, "smm_Operation103", None)
                setattr(value, "smm_Operation103", self)

    @property
    def smm_MeasureRelationship(self):
        return self.__smm_MeasureRelationship

    @smm_MeasureRelationship.setter
    def smm_MeasureRelationship(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_MeasureRelationship__smm_MeasureRelationship", None)
        self.__smm_MeasureRelationship = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_Measure68"):
                opp_val = getattr(old_value, "smm_Measure68", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_Measure68"):
                opp_val = getattr(value, "smm_Measure68", None)
                if opp_val is None:
                    setattr(value, "smm_Measure68", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def smm_MeasureRelationship89(self):
        return self.__smm_MeasureRelationship89

    @smm_MeasureRelationship89.setter
    def smm_MeasureRelationship89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_MeasureRelationship__smm_MeasureRelationship89", None)
        self.__smm_MeasureRelationship89 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_Measure88"):
                opp_val = getattr(old_value, "smm_Measure88", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_Measure88"):
                opp_val = getattr(value, "smm_Measure88", None)
                if opp_val is None:
                    setattr(value, "smm_Measure88", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def smm_MeasureRelationship71(self):
        return self.__smm_MeasureRelationship71

    @smm_MeasureRelationship71.setter
    def smm_MeasureRelationship71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_MeasureRelationship__smm_MeasureRelationship71", None)
        self.__smm_MeasureRelationship71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_Measure70"):
                opp_val = getattr(old_value, "smm_Measure70", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_Measure70"):
                opp_val = getattr(value, "smm_Measure70", None)
                if opp_val is None:
                    setattr(value, "smm_Measure70", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class smm_CategoryRelationship(SmmRelationship):

    pass
class SmmElement:

    pass
class smm_Measurement(SmmElement):

    def __init__(self, breakValue: str, error: str, smm_Measurement: set["smm_MeasurementRelationship"] = None, smm_Measurement106: set["smm_EquivalentMeasurementRelationship"] = None, smm_Measurement108: set["smm_EquivalentMeasurementRelationship"] = None, smm_Measurement111: set["smm_MeasurementRelationship"] = None, smm_Measurement114: set["smm_MeasurementRelationship"] = None, smm_Measurement117: set["smm_RefinementMeasurementRelationship"] = None, smm_Measurement119: set["smm_RefinementMeasurementRelationship"] = None, measurements: "smm_ObservedMeasure" = None, smm_Measurement124: "smm_EObject" = None, Measurement: "smm_ObservedMeasure" = None):
        self.breakValue = breakValue
        self.error = error
        self.smm_Measurement = smm_Measurement if smm_Measurement is not None else set()
        self.smm_Measurement106 = smm_Measurement106 if smm_Measurement106 is not None else set()
        self.smm_Measurement108 = smm_Measurement108 if smm_Measurement108 is not None else set()
        self.smm_Measurement111 = smm_Measurement111 if smm_Measurement111 is not None else set()
        self.smm_Measurement114 = smm_Measurement114 if smm_Measurement114 is not None else set()
        self.smm_Measurement117 = smm_Measurement117 if smm_Measurement117 is not None else set()
        self.smm_Measurement119 = smm_Measurement119 if smm_Measurement119 is not None else set()
        self.measurements = measurements
        self.smm_Measurement124 = smm_Measurement124
        self.Measurement = Measurement
        
    @property
    def breakValue(self) -> str:
        return self.__breakValue

    @breakValue.setter
    def breakValue(self, breakValue: str):
        self.__breakValue = breakValue

    @property
    def error(self) -> str:
        return self.__error

    @error.setter
    def error(self, error: str):
        self.__error = error

    @property
    def smm_Measurement124(self):
        return self.__smm_Measurement124

    @smm_Measurement124.setter
    def smm_Measurement124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measurement__smm_Measurement124", None)
        self.__smm_Measurement124 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_EObject"):
                opp_val = getattr(old_value, "smm_EObject", None)
                if opp_val == self:
                    setattr(old_value, "smm_EObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_EObject"):
                opp_val = getattr(value, "smm_EObject", None)
                setattr(value, "smm_EObject", self)

    @property
    def smm_Measurement119(self):
        return self.__smm_Measurement119

    @smm_Measurement119.setter
    def smm_Measurement119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measurement__smm_Measurement119", None)
        self.__smm_Measurement119 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smm_RefinementMeasurementRelationship120"):
                    opp_val = getattr(item, "smm_RefinementMeasurementRelationship120", None)
                    
                    if opp_val == self:
                        setattr(item, "smm_RefinementMeasurementRelationship120", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smm_RefinementMeasurementRelationship120"):
                    opp_val = getattr(item, "smm_RefinementMeasurementRelationship120", None)
                    
                    setattr(item, "smm_RefinementMeasurementRelationship120", self)
                    

    @property
    def smm_Measurement111(self):
        return self.__smm_Measurement111

    @smm_Measurement111.setter
    def smm_Measurement111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measurement__smm_Measurement111", None)
        self.__smm_Measurement111 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smm_MeasurementRelationship112"):
                    opp_val = getattr(item, "smm_MeasurementRelationship112", None)
                    
                    if opp_val == self:
                        setattr(item, "smm_MeasurementRelationship112", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smm_MeasurementRelationship112"):
                    opp_val = getattr(item, "smm_MeasurementRelationship112", None)
                    
                    setattr(item, "smm_MeasurementRelationship112", self)
                    

    @property
    def Measurement(self):
        return self.__Measurement

    @Measurement.setter
    def Measurement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measurement__Measurement", None)
        self.__Measurement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "observedMeasure135"):
                opp_val = getattr(old_value, "observedMeasure135", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "observedMeasure135"):
                opp_val = getattr(value, "observedMeasure135", None)
                if opp_val is None:
                    setattr(value, "observedMeasure135", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def smm_Measurement106(self):
        return self.__smm_Measurement106

    @smm_Measurement106.setter
    def smm_Measurement106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measurement__smm_Measurement106", None)
        self.__smm_Measurement106 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smm_EquivalentMeasurementRelationship"):
                    opp_val = getattr(item, "smm_EquivalentMeasurementRelationship", None)
                    
                    if opp_val == self:
                        setattr(item, "smm_EquivalentMeasurementRelationship", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smm_EquivalentMeasurementRelationship"):
                    opp_val = getattr(item, "smm_EquivalentMeasurementRelationship", None)
                    
                    setattr(item, "smm_EquivalentMeasurementRelationship", self)
                    

    @property
    def smm_Measurement(self):
        return self.__smm_Measurement

    @smm_Measurement.setter
    def smm_Measurement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measurement__smm_Measurement", None)
        self.__smm_Measurement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smm_MeasurementRelationship"):
                    opp_val = getattr(item, "smm_MeasurementRelationship", None)
                    
                    if opp_val == self:
                        setattr(item, "smm_MeasurementRelationship", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smm_MeasurementRelationship"):
                    opp_val = getattr(item, "smm_MeasurementRelationship", None)
                    
                    setattr(item, "smm_MeasurementRelationship", self)
                    

    @property
    def smm_Measurement117(self):
        return self.__smm_Measurement117

    @smm_Measurement117.setter
    def smm_Measurement117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measurement__smm_Measurement117", None)
        self.__smm_Measurement117 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smm_RefinementMeasurementRelationship"):
                    opp_val = getattr(item, "smm_RefinementMeasurementRelationship", None)
                    
                    if opp_val == self:
                        setattr(item, "smm_RefinementMeasurementRelationship", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smm_RefinementMeasurementRelationship"):
                    opp_val = getattr(item, "smm_RefinementMeasurementRelationship", None)
                    
                    setattr(item, "smm_RefinementMeasurementRelationship", self)
                    

    @property
    def smm_Measurement114(self):
        return self.__smm_Measurement114

    @smm_Measurement114.setter
    def smm_Measurement114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measurement__smm_Measurement114", None)
        self.__smm_Measurement114 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smm_MeasurementRelationship115"):
                    opp_val = getattr(item, "smm_MeasurementRelationship115", None)
                    
                    if opp_val == self:
                        setattr(item, "smm_MeasurementRelationship115", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smm_MeasurementRelationship115"):
                    opp_val = getattr(item, "smm_MeasurementRelationship115", None)
                    
                    setattr(item, "smm_MeasurementRelationship115", self)
                    

    @property
    def smm_Measurement108(self):
        return self.__smm_Measurement108

    @smm_Measurement108.setter
    def smm_Measurement108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measurement__smm_Measurement108", None)
        self.__smm_Measurement108 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smm_EquivalentMeasurementRelationship109"):
                    opp_val = getattr(item, "smm_EquivalentMeasurementRelationship109", None)
                    
                    if opp_val == self:
                        setattr(item, "smm_EquivalentMeasurementRelationship109", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smm_EquivalentMeasurementRelationship109"):
                    opp_val = getattr(item, "smm_EquivalentMeasurementRelationship109", None)
                    
                    setattr(item, "smm_EquivalentMeasurementRelationship109", self)
                    

    @property
    def measurements(self):
        return self.__measurements

    @measurements.setter
    def measurements(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measurement__measurements", None)
        self.__measurements = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ObservedMeasure122"):
                opp_val = getattr(old_value, "ObservedMeasure122", None)
                if opp_val == self:
                    setattr(old_value, "ObservedMeasure122", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ObservedMeasure122"):
                opp_val = getattr(value, "ObservedMeasure122", None)
                setattr(value, "ObservedMeasure122", self)

    def getMeasureLabel(self) -> str:
        # TODO: Implement getMeasureLabel method
        pass

    def getMeasurementLabel(self) -> str:
        # TODO: Implement getMeasurementLabel method
        pass

class smm_SmmRelationship(SmmElement):

    pass
class smm_SmmModel(SmmElement):

    pass
class smm_ObservationScope(SmmElement):

    def __init__(self, scopeUri: str, smm_ObservationScope: "smm_Observation" = None):
        self.scopeUri = scopeUri
        self.smm_ObservationScope = smm_ObservationScope
        
    @property
    def scopeUri(self) -> str:
        return self.__scopeUri

    @scopeUri.setter
    def scopeUri(self, scopeUri: str):
        self.__scopeUri = scopeUri

    @property
    def smm_ObservationScope(self):
        return self.__smm_ObservationScope

    @smm_ObservationScope.setter
    def smm_ObservationScope(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_ObservationScope__smm_ObservationScope", None)
        self.__smm_ObservationScope = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_Observation"):
                opp_val = getattr(old_value, "smm_Observation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_Observation"):
                opp_val = getattr(value, "smm_Observation", None)
                if opp_val is None:
                    setattr(value, "smm_Observation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class smm_Attribute(SmmElement):

    def __init__(self, tag: str, value: str, smm_Attribute: "smm_SmmElement" = None):
        self.tag = tag
        self.value = value
        self.smm_Attribute = smm_Attribute
        
    @property
    def tag(self) -> str:
        return self.__tag

    @tag.setter
    def tag(self, tag: str):
        self.__tag = tag

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def smm_Attribute(self):
        return self.__smm_Attribute

    @smm_Attribute.setter
    def smm_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Attribute__smm_Attribute", None)
        self.__smm_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_SmmElement"):
                opp_val = getattr(old_value, "smm_SmmElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_SmmElement"):
                opp_val = getattr(value, "smm_SmmElement", None)
                if opp_val is None:
                    setattr(value, "smm_SmmElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class smm_ObservedMeasure(SmmElement):

    pass
class smm_Interval(SmmElement):

    def __init__(self, maximumOpen: str, minimum: float, minimumOpen: str, maximum: float):
        self.maximumOpen = maximumOpen
        self.minimum = minimum
        self.minimumOpen = minimumOpen
        self.maximum = maximum
        
    @property
    def maximum(self) -> float:
        return self.__maximum

    @maximum.setter
    def maximum(self, maximum: float):
        self.__maximum = maximum

    @property
    def minimumOpen(self) -> str:
        return self.__minimumOpen

    @minimumOpen.setter
    def minimumOpen(self, minimumOpen: str):
        self.__minimumOpen = minimumOpen

    @property
    def maximumOpen(self) -> str:
        return self.__maximumOpen

    @maximumOpen.setter
    def maximumOpen(self, maximumOpen: str):
        self.__maximumOpen = maximumOpen

    @property
    def minimum(self) -> float:
        return self.__minimum

    @minimum.setter
    def minimum(self, minimum: float):
        self.__minimum = minimum

class smm_Observation(SmmElement):

    def __init__(self, observer: str, tool: str, whenObserved: str, smm_Observation: set["smm_ObservationScope"] = None, smm_Observation127: set["smm_ObservedMeasure"] = None, smm_Observation129: set["smm_Argument"] = None, smm_Observation131: set["smm_AbstractMeasureElement"] = None, smm_Observation176: "smm_SmmModel" = None):
        self.observer = observer
        self.tool = tool
        self.whenObserved = whenObserved
        self.smm_Observation = smm_Observation if smm_Observation is not None else set()
        self.smm_Observation127 = smm_Observation127 if smm_Observation127 is not None else set()
        self.smm_Observation129 = smm_Observation129 if smm_Observation129 is not None else set()
        self.smm_Observation131 = smm_Observation131 if smm_Observation131 is not None else set()
        self.smm_Observation176 = smm_Observation176
        
    @property
    def whenObserved(self) -> str:
        return self.__whenObserved

    @whenObserved.setter
    def whenObserved(self, whenObserved: str):
        self.__whenObserved = whenObserved

    @property
    def tool(self) -> str:
        return self.__tool

    @tool.setter
    def tool(self, tool: str):
        self.__tool = tool

    @property
    def observer(self) -> str:
        return self.__observer

    @observer.setter
    def observer(self, observer: str):
        self.__observer = observer

    @property
    def smm_Observation127(self):
        return self.__smm_Observation127

    @smm_Observation127.setter
    def smm_Observation127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Observation__smm_Observation127", None)
        self.__smm_Observation127 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smm_ObservedMeasure"):
                    opp_val = getattr(item, "smm_ObservedMeasure", None)
                    
                    if opp_val == self:
                        setattr(item, "smm_ObservedMeasure", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smm_ObservedMeasure"):
                    opp_val = getattr(item, "smm_ObservedMeasure", None)
                    
                    setattr(item, "smm_ObservedMeasure", self)
                    

    @property
    def smm_Observation129(self):
        return self.__smm_Observation129

    @smm_Observation129.setter
    def smm_Observation129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Observation__smm_Observation129", None)
        self.__smm_Observation129 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smm_Argument"):
                    opp_val = getattr(item, "smm_Argument", None)
                    
                    if opp_val == self:
                        setattr(item, "smm_Argument", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smm_Argument"):
                    opp_val = getattr(item, "smm_Argument", None)
                    
                    setattr(item, "smm_Argument", self)
                    

    @property
    def smm_Observation176(self):
        return self.__smm_Observation176

    @smm_Observation176.setter
    def smm_Observation176(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Observation__smm_Observation176", None)
        self.__smm_Observation176 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_SmmModel175"):
                opp_val = getattr(old_value, "smm_SmmModel175", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_SmmModel175"):
                opp_val = getattr(value, "smm_SmmModel175", None)
                if opp_val is None:
                    setattr(value, "smm_SmmModel175", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def smm_Observation(self):
        return self.__smm_Observation

    @smm_Observation.setter
    def smm_Observation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Observation__smm_Observation", None)
        self.__smm_Observation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smm_ObservationScope"):
                    opp_val = getattr(item, "smm_ObservationScope", None)
                    
                    if opp_val == self:
                        setattr(item, "smm_ObservationScope", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smm_ObservationScope"):
                    opp_val = getattr(item, "smm_ObservationScope", None)
                    
                    setattr(item, "smm_ObservationScope", self)
                    

    @property
    def smm_Observation131(self):
        return self.__smm_Observation131

    @smm_Observation131.setter
    def smm_Observation131(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Observation__smm_Observation131", None)
        self.__smm_Observation131 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smm_AbstractMeasureElement132"):
                    opp_val = getattr(item, "smm_AbstractMeasureElement132", None)
                    
                    if opp_val == self:
                        setattr(item, "smm_AbstractMeasureElement132", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smm_AbstractMeasureElement132"):
                    opp_val = getattr(item, "smm_AbstractMeasureElement132", None)
                    
                    setattr(item, "smm_AbstractMeasureElement132", self)
                    

class smm_MeasureLibrary(SmmElement):

    pass
class smm_AbstractMeasureElement(SmmElement):

    pass
class smm_Argument(SmmElement):

    def __init__(self, Type: str, value: str, arguments: "smm_ObservedMeasure" = None, Argument: "smm_ObservedMeasure" = None, smm_Argument: "smm_Observation" = None):
        self.Type = Type
        self.value = value
        self.arguments = arguments
        self.Argument = Argument
        self.smm_Argument = smm_Argument
        
    @property
    def Type(self) -> str:
        return self.__Type

    @Type.setter
    def Type(self, Type: str):
        self.__Type = Type

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def smm_Argument(self):
        return self.__smm_Argument

    @smm_Argument.setter
    def smm_Argument(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Argument__smm_Argument", None)
        self.__smm_Argument = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_Observation129"):
                opp_val = getattr(old_value, "smm_Observation129", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_Observation129"):
                opp_val = getattr(value, "smm_Observation129", None)
                if opp_val is None:
                    setattr(value, "smm_Observation129", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Argument(self):
        return self.__Argument

    @Argument.setter
    def Argument(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Argument__Argument", None)
        self.__Argument = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "observedMeasure"):
                opp_val = getattr(old_value, "observedMeasure", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "observedMeasure"):
                opp_val = getattr(value, "observedMeasure", None)
                if opp_val is None:
                    setattr(value, "observedMeasure", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def arguments(self):
        return self.__arguments

    @arguments.setter
    def arguments(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Argument__arguments", None)
        self.__arguments = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ObservedMeasure"):
                opp_val = getattr(old_value, "ObservedMeasure", None)
                if opp_val == self:
                    setattr(old_value, "ObservedMeasure", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ObservedMeasure"):
                opp_val = getattr(value, "ObservedMeasure", None)
                setattr(value, "ObservedMeasure", self)

class smm_Annotation(SmmElement):

    def __init__(self, text: str, smm_Annotation: "smm_SmmElement" = None):
        self.text = text
        self.smm_Annotation = smm_Annotation
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def smm_Annotation(self):
        return self.__smm_Annotation

    @smm_Annotation.setter
    def smm_Annotation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Annotation__smm_Annotation", None)
        self.__smm_Annotation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_SmmElement168"):
                opp_val = getattr(old_value, "smm_SmmElement168", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_SmmElement168"):
                opp_val = getattr(value, "smm_SmmElement168", None)
                if opp_val is None:
                    setattr(value, "smm_SmmElement168", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
