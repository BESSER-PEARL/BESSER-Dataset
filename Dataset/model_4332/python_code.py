from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Accumulator(Enum):
    sum = "sum"
    maximum = "maximum"
    minimum = "minimum"
    average = "average"


############################################
# Definition of Classes
############################################

class DirectMeasurement:

    pass
class smm_Count(DirectMeasurement):

    pass
class DimensionalMeasurement:

    pass
class smm_CollectiveMeasurement(DimensionalMeasurement):

    def __init__(self, accumulator: str, isBaseSupplied: bool, smm_CollectiveMeasurement: set["smm_DimensionalMeasurement"] = None):
        self.accumulator = accumulator
        self.isBaseSupplied = isBaseSupplied
        self.smm_CollectiveMeasurement = smm_CollectiveMeasurement if smm_CollectiveMeasurement is not None else set()
        
    @property
    def accumulator(self) -> str:
        return self.__accumulator

    @accumulator.setter
    def accumulator(self, accumulator: str):
        self.__accumulator = accumulator

    @property
    def isBaseSupplied(self) -> bool:
        return self.__isBaseSupplied

    @isBaseSupplied.setter
    def isBaseSupplied(self, isBaseSupplied: bool):
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
                if hasattr(item, "smm_DimensionalMeasurement69"):
                    opp_val = getattr(item, "smm_DimensionalMeasurement69", None)
                    
                    if opp_val == self:
                        setattr(item, "smm_DimensionalMeasurement69", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smm_DimensionalMeasurement69"):
                    opp_val = getattr(item, "smm_DimensionalMeasurement69", None)
                    
                    setattr(item, "smm_DimensionalMeasurement69", self)
                    

class smm_NamedMeasurement(DimensionalMeasurement):

    pass
class smm_ReScaledMeasurement(DimensionalMeasurement):

    def __init__(self, isBaseSupplied: bool):
        self.isBaseSupplied = isBaseSupplied
        
    @property
    def isBaseSupplied(self) -> bool:
        return self.__isBaseSupplied

    @isBaseSupplied.setter
    def isBaseSupplied(self, isBaseSupplied: bool):
        self.__isBaseSupplied = isBaseSupplied

class smm_AggregatedMeasurement(DimensionalMeasurement):

    def __init__(self, isBaseSuppled: bool, smm_AggregatedMeasurement: set["smm_DimensionalMeasurement"] = None):
        self.isBaseSuppled = isBaseSuppled
        self.smm_AggregatedMeasurement = smm_AggregatedMeasurement if smm_AggregatedMeasurement is not None else set()
        
    @property
    def isBaseSuppled(self) -> bool:
        return self.__isBaseSuppled

    @isBaseSuppled.setter
    def isBaseSuppled(self, isBaseSuppled: bool):
        self.__isBaseSuppled = isBaseSuppled

    @property
    def smm_AggregatedMeasurement(self):
        return self.__smm_AggregatedMeasurement

    @smm_AggregatedMeasurement.setter
    def smm_AggregatedMeasurement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_AggregatedMeasurement__smm_AggregatedMeasurement", None)
        self.__smm_AggregatedMeasurement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smm_DimensionalMeasurement71"):
                    opp_val = getattr(item, "smm_DimensionalMeasurement71", None)
                    
                    if opp_val == self:
                        setattr(item, "smm_DimensionalMeasurement71", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smm_DimensionalMeasurement71"):
                    opp_val = getattr(item, "smm_DimensionalMeasurement71", None)
                    
                    setattr(item, "smm_DimensionalMeasurement71", self)
                    

class smm_DirectMeasurement(DimensionalMeasurement):

    pass
class Measurement:

    pass
class smm_Grade(Measurement):

    def __init__(self, isBaseSupplied: bool, value: str, smm_Grade: "smm_DimensionalMeasurement" = None):
        self.isBaseSupplied = isBaseSupplied
        self.value = value
        self.smm_Grade = smm_Grade
        
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
    def smm_Grade(self):
        return self.__smm_Grade

    @smm_Grade.setter
    def smm_Grade(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Grade__smm_Grade", None)
        self.__smm_Grade = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_DimensionalMeasurement"):
                opp_val = getattr(old_value, "smm_DimensionalMeasurement", None)
                if opp_val == self:
                    setattr(old_value, "smm_DimensionalMeasurement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_DimensionalMeasurement"):
                opp_val = getattr(value, "smm_DimensionalMeasurement", None)
                setattr(value, "smm_DimensionalMeasurement", self)

class smm_DimensionalMeasurement(Measurement):

    def __init__(self, value: float, smm_DimensionalMeasurement: "smm_Grade" = None, smm_DimensionalMeasurement69: "smm_CollectiveMeasurement" = None, smm_DimensionalMeasurement71: "smm_AggregatedMeasurement" = None):
        self.value = value
        self.smm_DimensionalMeasurement = smm_DimensionalMeasurement
        self.smm_DimensionalMeasurement69 = smm_DimensionalMeasurement69
        self.smm_DimensionalMeasurement71 = smm_DimensionalMeasurement71
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def smm_DimensionalMeasurement69(self):
        return self.__smm_DimensionalMeasurement69

    @smm_DimensionalMeasurement69.setter
    def smm_DimensionalMeasurement69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_DimensionalMeasurement__smm_DimensionalMeasurement69", None)
        self.__smm_DimensionalMeasurement69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_CollectiveMeasurement"):
                opp_val = getattr(old_value, "smm_CollectiveMeasurement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_CollectiveMeasurement"):
                opp_val = getattr(value, "smm_CollectiveMeasurement", None)
                if opp_val is None:
                    setattr(value, "smm_CollectiveMeasurement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def smm_DimensionalMeasurement71(self):
        return self.__smm_DimensionalMeasurement71

    @smm_DimensionalMeasurement71.setter
    def smm_DimensionalMeasurement71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_DimensionalMeasurement__smm_DimensionalMeasurement71", None)
        self.__smm_DimensionalMeasurement71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_AggregatedMeasurement"):
                opp_val = getattr(old_value, "smm_AggregatedMeasurement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_AggregatedMeasurement"):
                opp_val = getattr(value, "smm_AggregatedMeasurement", None)
                if opp_val is None:
                    setattr(value, "smm_AggregatedMeasurement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def smm_DimensionalMeasurement(self):
        return self.__smm_DimensionalMeasurement

    @smm_DimensionalMeasurement.setter
    def smm_DimensionalMeasurement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_DimensionalMeasurement__smm_DimensionalMeasurement", None)
        self.__smm_DimensionalMeasurement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_Grade"):
                opp_val = getattr(old_value, "smm_Grade", None)
                if opp_val == self:
                    setattr(old_value, "smm_Grade", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_Grade"):
                opp_val = getattr(value, "smm_Grade", None)
                setattr(value, "smm_Grade", self)

class DirectMeasure:

    pass
class smm_Counting(DirectMeasure):

    pass
class BinaryMeasure:

    pass
class smm_RatioMeasure(BinaryMeasure):

    pass
class Measure:

    pass
class smm_DimensionalMeasure(Measure):

    def __init__(self, unit: str, smm_DimensionalMeasure60: "smm_BinaryMeasure" = None, smm_DimensionalMeasure62: "smm_CollectiveMeasure" = None, smm_DimensionalMeasure: "smm_BinaryMeasure" = None):
        self.unit = unit
        self.smm_DimensionalMeasure60 = smm_DimensionalMeasure60
        self.smm_DimensionalMeasure62 = smm_DimensionalMeasure62
        self.smm_DimensionalMeasure = smm_DimensionalMeasure
        
    @property
    def unit(self) -> str:
        return self.__unit

    @unit.setter
    def unit(self, unit: str):
        self.__unit = unit

    @property
    def smm_DimensionalMeasure(self):
        return self.__smm_DimensionalMeasure

    @smm_DimensionalMeasure.setter
    def smm_DimensionalMeasure(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_DimensionalMeasure__smm_DimensionalMeasure", None)
        self.__smm_DimensionalMeasure = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_BinaryMeasure"):
                opp_val = getattr(old_value, "smm_BinaryMeasure", None)
                if opp_val == self:
                    setattr(old_value, "smm_BinaryMeasure", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_BinaryMeasure"):
                opp_val = getattr(value, "smm_BinaryMeasure", None)
                setattr(value, "smm_BinaryMeasure", self)

    @property
    def smm_DimensionalMeasure62(self):
        return self.__smm_DimensionalMeasure62

    @smm_DimensionalMeasure62.setter
    def smm_DimensionalMeasure62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_DimensionalMeasure__smm_DimensionalMeasure62", None)
        self.__smm_DimensionalMeasure62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_CollectiveMeasure"):
                opp_val = getattr(old_value, "smm_CollectiveMeasure", None)
                if opp_val == self:
                    setattr(old_value, "smm_CollectiveMeasure", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_CollectiveMeasure"):
                opp_val = getattr(value, "smm_CollectiveMeasure", None)
                setattr(value, "smm_CollectiveMeasure", self)

    @property
    def smm_DimensionalMeasure60(self):
        return self.__smm_DimensionalMeasure60

    @smm_DimensionalMeasure60.setter
    def smm_DimensionalMeasure60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_DimensionalMeasure__smm_DimensionalMeasure60", None)
        self.__smm_DimensionalMeasure60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_BinaryMeasure59"):
                opp_val = getattr(old_value, "smm_BinaryMeasure59", None)
                if opp_val == self:
                    setattr(old_value, "smm_BinaryMeasure59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_BinaryMeasure59"):
                opp_val = getattr(value, "smm_BinaryMeasure59", None)
                setattr(value, "smm_BinaryMeasure59", self)

class DimensionalMeasure:

    pass
class smm_CollectiveMeasure(DimensionalMeasure):

    def __init__(self, accumulator: str, smm_CollectiveMeasure: "smm_DimensionalMeasure" = None):
        self.accumulator = accumulator
        self.smm_CollectiveMeasure = smm_CollectiveMeasure
        
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
        self.__smm_CollectiveMeasure = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_DimensionalMeasure62"):
                opp_val = getattr(old_value, "smm_DimensionalMeasure62", None)
                if opp_val == self:
                    setattr(old_value, "smm_DimensionalMeasure62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_DimensionalMeasure62"):
                opp_val = getattr(value, "smm_DimensionalMeasure62", None)
                setattr(value, "smm_DimensionalMeasure62", self)

class smm_DirectMeasure(DimensionalMeasure):

    def __init__(self, operation: str):
        self.operation = operation
        
    @property
    def operation(self) -> str:
        return self.__operation

    @operation.setter
    def operation(self, operation: str):
        self.__operation = operation

class smm_RescaledMeasure(DimensionalMeasure):

    def __init__(self, formula: str):
        self.formula = formula
        
    @property
    def formula(self) -> str:
        return self.__formula

    @formula.setter
    def formula(self, formula: str):
        self.__formula = formula

class smm_NamedMeasure(DimensionalMeasure):

    pass
class smm_BinaryMeasure(DimensionalMeasure):

    def __init__(self, functor: str, smm_BinaryMeasure59: "smm_DimensionalMeasure" = None, smm_BinaryMeasure: "smm_DimensionalMeasure" = None):
        self.functor = functor
        self.smm_BinaryMeasure59 = smm_BinaryMeasure59
        self.smm_BinaryMeasure = smm_BinaryMeasure
        
    @property
    def functor(self) -> str:
        return self.__functor

    @functor.setter
    def functor(self, functor: str):
        self.__functor = functor

    @property
    def smm_BinaryMeasure59(self):
        return self.__smm_BinaryMeasure59

    @smm_BinaryMeasure59.setter
    def smm_BinaryMeasure59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_BinaryMeasure__smm_BinaryMeasure59", None)
        self.__smm_BinaryMeasure59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_DimensionalMeasure60"):
                opp_val = getattr(old_value, "smm_DimensionalMeasure60", None)
                if opp_val == self:
                    setattr(old_value, "smm_DimensionalMeasure60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_DimensionalMeasure60"):
                opp_val = getattr(value, "smm_DimensionalMeasure60", None)
                setattr(value, "smm_DimensionalMeasure60", self)

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
            if hasattr(old_value, "smm_DimensionalMeasure"):
                opp_val = getattr(old_value, "smm_DimensionalMeasure", None)
                if opp_val == self:
                    setattr(old_value, "smm_DimensionalMeasure", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_DimensionalMeasure"):
                opp_val = getattr(value, "smm_DimensionalMeasure", None)
                setattr(value, "smm_DimensionalMeasure", self)

class smm_Ranking(Measure):

    pass
class SmmRelationship:

    pass
class smm_MeasurementRelationship(SmmRelationship):

    def __init__(self, name: str, MeasurementRelationship: "smm_Measurement" = None, MeasurementRelationship44: "smm_Measurement" = None, inMeasurement: "smm_Measurement" = None, outMeasurement: "smm_Measurement" = None):
        self.name = name
        self.MeasurementRelationship = MeasurementRelationship
        self.MeasurementRelationship44 = MeasurementRelationship44
        self.inMeasurement = inMeasurement
        self.outMeasurement = outMeasurement
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def MeasurementRelationship(self):
        return self.__MeasurementRelationship

    @MeasurementRelationship.setter
    def MeasurementRelationship(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_MeasurementRelationship__MeasurementRelationship", None)
        self.__MeasurementRelationship = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "from41"):
                opp_val = getattr(old_value, "from41", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "from41"):
                opp_val = getattr(value, "from41", None)
                if opp_val is None:
                    setattr(value, "from41", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def inMeasurement(self):
        return self.__inMeasurement

    @inMeasurement.setter
    def inMeasurement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_MeasurementRelationship__inMeasurement", None)
        self.__inMeasurement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Measurement67"):
                opp_val = getattr(old_value, "Measurement67", None)
                if opp_val == self:
                    setattr(old_value, "Measurement67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Measurement67"):
                opp_val = getattr(value, "Measurement67", None)
                setattr(value, "Measurement67", self)

    @property
    def outMeasurement(self):
        return self.__outMeasurement

    @outMeasurement.setter
    def outMeasurement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_MeasurementRelationship__outMeasurement", None)
        self.__outMeasurement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Measurement65"):
                opp_val = getattr(old_value, "Measurement65", None)
                if opp_val == self:
                    setattr(old_value, "Measurement65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Measurement65"):
                opp_val = getattr(value, "Measurement65", None)
                setattr(value, "Measurement65", self)

    @property
    def MeasurementRelationship44(self):
        return self.__MeasurementRelationship44

    @MeasurementRelationship44.setter
    def MeasurementRelationship44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_MeasurementRelationship__MeasurementRelationship44", None)
        self.__MeasurementRelationship44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "to43"):
                opp_val = getattr(old_value, "to43", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "to43"):
                opp_val = getattr(value, "to43", None)
                if opp_val is None:
                    setattr(value, "to43", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class smm_MeasureRelationship(SmmRelationship):

    pass
class smm_CategoryRelationship(SmmRelationship):

    def __init__(self, name: str, outCategory: "smm_Category" = None, inCategory: "smm_Category" = None, CategoryRelationship: "smm_Category" = None, CategoryRelationship16: "smm_Category" = None):
        self.name = name
        self.outCategory = outCategory
        self.inCategory = inCategory
        self.CategoryRelationship = CategoryRelationship
        self.CategoryRelationship16 = CategoryRelationship16
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def CategoryRelationship16(self):
        return self.__CategoryRelationship16

    @CategoryRelationship16.setter
    def CategoryRelationship16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_CategoryRelationship__CategoryRelationship16", None)
        self.__CategoryRelationship16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "to"):
                opp_val = getattr(old_value, "to", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "to"):
                opp_val = getattr(value, "to", None)
                if opp_val is None:
                    setattr(value, "to", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def outCategory(self):
        return self.__outCategory

    @outCategory.setter
    def outCategory(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_CategoryRelationship__outCategory", None)
        self.__outCategory = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Category"):
                opp_val = getattr(old_value, "Category", None)
                if opp_val == self:
                    setattr(old_value, "Category", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Category"):
                opp_val = getattr(value, "Category", None)
                setattr(value, "Category", self)

    @property
    def inCategory(self):
        return self.__inCategory

    @inCategory.setter
    def inCategory(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_CategoryRelationship__inCategory", None)
        self.__inCategory = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Category7"):
                opp_val = getattr(old_value, "Category7", None)
                if opp_val == self:
                    setattr(old_value, "Category7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Category7"):
                opp_val = getattr(value, "Category7", None)
                setattr(value, "Category7", self)

    @property
    def CategoryRelationship(self):
        return self.__CategoryRelationship

    @CategoryRelationship.setter
    def CategoryRelationship(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_CategoryRelationship__CategoryRelationship", None)
        self.__CategoryRelationship = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "from"):
                opp_val = getattr(old_value, "from", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "from"):
                opp_val = getattr(value, "from", None)
                if opp_val is None:
                    setattr(value, "from", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class SmmElement:

    pass
class smm_Measurement(SmmElement):

    def __init__(self, error: str, measurement: "smm_Measure" = None, Measurement: "smm_Measure" = None, smm_Measurement: "smm_Observation" = None, from41: set["smm_MeasurementRelationship"] = None, to43: set["smm_MeasurementRelationship"] = None, Measurement67: "smm_MeasurementRelationship" = None, Measurement65: "smm_MeasurementRelationship" = None):
        self.error = error
        self.measurement = measurement
        self.Measurement = Measurement
        self.smm_Measurement = smm_Measurement
        self.from41 = from41 if from41 is not None else set()
        self.to43 = to43 if to43 is not None else set()
        self.Measurement67 = Measurement67
        self.Measurement65 = Measurement65
        
    @property
    def error(self) -> str:
        return self.__error

    @error.setter
    def error(self, error: str):
        self.__error = error

    @property
    def measurement(self):
        return self.__measurement

    @measurement.setter
    def measurement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measurement__measurement", None)
        self.__measurement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Measure38"):
                opp_val = getattr(old_value, "Measure38", None)
                if opp_val == self:
                    setattr(old_value, "Measure38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Measure38"):
                opp_val = getattr(value, "Measure38", None)
                setattr(value, "Measure38", self)

    @property
    def to43(self):
        return self.__to43

    @to43.setter
    def to43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measurement__to43", None)
        self.__to43 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MeasurementRelationship44"):
                    opp_val = getattr(item, "MeasurementRelationship44", None)
                    
                    if opp_val == self:
                        setattr(item, "MeasurementRelationship44", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MeasurementRelationship44"):
                    opp_val = getattr(item, "MeasurementRelationship44", None)
                    
                    setattr(item, "MeasurementRelationship44", self)
                    

    @property
    def from41(self):
        return self.__from41

    @from41.setter
    def from41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measurement__from41", None)
        self.__from41 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MeasurementRelationship"):
                    opp_val = getattr(item, "MeasurementRelationship", None)
                    
                    if opp_val == self:
                        setattr(item, "MeasurementRelationship", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MeasurementRelationship"):
                    opp_val = getattr(item, "MeasurementRelationship", None)
                    
                    setattr(item, "MeasurementRelationship", self)
                    

    @property
    def Measurement65(self):
        return self.__Measurement65

    @Measurement65.setter
    def Measurement65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measurement__Measurement65", None)
        self.__Measurement65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outMeasurement"):
                opp_val = getattr(old_value, "outMeasurement", None)
                if opp_val == self:
                    setattr(old_value, "outMeasurement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outMeasurement"):
                opp_val = getattr(value, "outMeasurement", None)
                setattr(value, "outMeasurement", self)

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
            if hasattr(old_value, "measure"):
                opp_val = getattr(old_value, "measure", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "measure"):
                opp_val = getattr(value, "measure", None)
                if opp_val is None:
                    setattr(value, "measure", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Measurement67(self):
        return self.__Measurement67

    @Measurement67.setter
    def Measurement67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measurement__Measurement67", None)
        self.__Measurement67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "inMeasurement"):
                opp_val = getattr(old_value, "inMeasurement", None)
                if opp_val == self:
                    setattr(old_value, "inMeasurement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "inMeasurement"):
                opp_val = getattr(value, "inMeasurement", None)
                setattr(value, "inMeasurement", self)

    @property
    def smm_Measurement(self):
        return self.__smm_Measurement

    @smm_Measurement.setter
    def smm_Measurement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measurement__smm_Measurement", None)
        self.__smm_Measurement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_Observation"):
                opp_val = getattr(old_value, "smm_Observation", None)
                if opp_val == self:
                    setattr(old_value, "smm_Observation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_Observation"):
                opp_val = getattr(value, "smm_Observation", None)
                setattr(value, "smm_Observation", self)

class smm_Scope(SmmElement):

    def __init__(self, class: str, enumerated: bool, name: str, recognizer: str, Scope: "smm_Measure" = None, scope: set["smm_Measure"] = None):
        self.class = class
        self.enumerated = enumerated
        self.name = name
        self.recognizer = recognizer
        self.Scope = Scope
        self.scope = scope if scope is not None else set()
        
    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def enumerated(self) -> bool:
        return self.__enumerated

    @enumerated.setter
    def enumerated(self, enumerated: bool):
        self.__enumerated = enumerated

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def recognizer(self) -> str:
        return self.__recognizer

    @recognizer.setter
    def recognizer(self, recognizer: str):
        self.__recognizer = recognizer

    @property
    def scope(self):
        return self.__scope

    @scope.setter
    def scope(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Scope__scope", None)
        self.__scope = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Measure56"):
                    opp_val = getattr(item, "Measure56", None)
                    
                    if opp_val == self:
                        setattr(item, "Measure56", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Measure56"):
                    opp_val = getattr(item, "Measure56", None)
                    
                    setattr(item, "Measure56", self)
                    

    @property
    def Scope(self):
        return self.__Scope

    @Scope.setter
    def Scope(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Scope__Scope", None)
        self.__Scope = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "measures"):
                opp_val = getattr(old_value, "measures", None)
                if opp_val == self:
                    setattr(old_value, "measures", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "measures"):
                opp_val = getattr(value, "measures", None)
                setattr(value, "measures", self)

class smm_Observation(SmmElement):

    def __init__(self, observer: str, tool: str, whenObserved: str, smm_Observation: "smm_Measurement" = None):
        self.observer = observer
        self.tool = tool
        self.whenObserved = whenObserved
        self.smm_Observation = smm_Observation
        
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
    def smm_Observation(self):
        return self.__smm_Observation

    @smm_Observation.setter
    def smm_Observation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Observation__smm_Observation", None)
        self.__smm_Observation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_Measurement"):
                opp_val = getattr(old_value, "smm_Measurement", None)
                if opp_val == self:
                    setattr(old_value, "smm_Measurement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_Measurement"):
                opp_val = getattr(value, "smm_Measurement", None)
                setattr(value, "smm_Measurement", self)

class smm_RankingInterval(SmmElement):

    def __init__(self, maximumEndpoint: float, maximumOpen: bool, minimumEndpoint: float, minimumOpen: bool, symbol: str, RankingInterval: "smm_Ranking" = None, interval: "smm_Ranking" = None):
        self.maximumEndpoint = maximumEndpoint
        self.maximumOpen = maximumOpen
        self.minimumEndpoint = minimumEndpoint
        self.minimumOpen = minimumOpen
        self.symbol = symbol
        self.RankingInterval = RankingInterval
        self.interval = interval
        
    @property
    def minimumEndpoint(self) -> float:
        return self.__minimumEndpoint

    @minimumEndpoint.setter
    def minimumEndpoint(self, minimumEndpoint: float):
        self.__minimumEndpoint = minimumEndpoint

    @property
    def minimumOpen(self) -> bool:
        return self.__minimumOpen

    @minimumOpen.setter
    def minimumOpen(self, minimumOpen: bool):
        self.__minimumOpen = minimumOpen

    @property
    def maximumOpen(self) -> bool:
        return self.__maximumOpen

    @maximumOpen.setter
    def maximumOpen(self, maximumOpen: bool):
        self.__maximumOpen = maximumOpen

    @property
    def maximumEndpoint(self) -> float:
        return self.__maximumEndpoint

    @maximumEndpoint.setter
    def maximumEndpoint(self, maximumEndpoint: float):
        self.__maximumEndpoint = maximumEndpoint

    @property
    def symbol(self) -> str:
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol: str):
        self.__symbol = symbol

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
            if hasattr(old_value, "rank"):
                opp_val = getattr(old_value, "rank", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rank"):
                opp_val = getattr(value, "rank", None)
                if opp_val is None:
                    setattr(value, "rank", set([self]))
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
            if hasattr(old_value, "Ranking"):
                opp_val = getattr(old_value, "Ranking", None)
                if opp_val == self:
                    setattr(old_value, "Ranking", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Ranking"):
                opp_val = getattr(value, "Ranking", None)
                setattr(value, "Ranking", self)

class smm_Measure(SmmElement):

    def __init__(self, library: str, name: str, from31: set["smm_MeasureRelationship"] = None, to33: set["smm_MeasureRelationship"] = None, characteristics: "smm_Characteristic" = None, measures: "smm_Scope" = None, Measure38: "smm_Measurement" = None, Measure: "smm_Category" = None, categoryMeasure: set["smm_Category"] = None, Measure23: "smm_Measure" = None, equivalentTo: set["smm_Measure"] = None, Measure26: "smm_Measure" = None, equivalentFrom: set["smm_Measure"] = None, smm_Measure: "smm_Measure" = None, smm_Measure27: set["smm_Measure"] = None, measure: set["smm_Measurement"] = None, Measure46: "smm_MeasureRelationship" = None, Measure48: "smm_MeasureRelationship" = None, Measure54: "smm_Characteristic" = None, Measure56: "smm_Scope" = None):
        self.library = library
        self.name = name
        self.from31 = from31 if from31 is not None else set()
        self.to33 = to33 if to33 is not None else set()
        self.characteristics = characteristics
        self.measures = measures
        self.Measure38 = Measure38
        self.Measure = Measure
        self.categoryMeasure = categoryMeasure if categoryMeasure is not None else set()
        self.Measure23 = Measure23
        self.equivalentTo = equivalentTo if equivalentTo is not None else set()
        self.Measure26 = Measure26
        self.equivalentFrom = equivalentFrom if equivalentFrom is not None else set()
        self.smm_Measure = smm_Measure
        self.smm_Measure27 = smm_Measure27 if smm_Measure27 is not None else set()
        self.measure = measure if measure is not None else set()
        self.Measure46 = Measure46
        self.Measure48 = Measure48
        self.Measure54 = Measure54
        self.Measure56 = Measure56
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def library(self) -> str:
        return self.__library

    @library.setter
    def library(self, library: str):
        self.__library = library

    @property
    def smm_Measure(self):
        return self.__smm_Measure

    @smm_Measure.setter
    def smm_Measure(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measure__smm_Measure", None)
        self.__smm_Measure = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_Measure27"):
                opp_val = getattr(old_value, "smm_Measure27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_Measure27"):
                opp_val = getattr(value, "smm_Measure27", None)
                if opp_val is None:
                    setattr(value, "smm_Measure27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def from31(self):
        return self.__from31

    @from31.setter
    def from31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measure__from31", None)
        self.__from31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MeasureRelationship"):
                    opp_val = getattr(item, "MeasureRelationship", None)
                    
                    if opp_val == self:
                        setattr(item, "MeasureRelationship", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MeasureRelationship"):
                    opp_val = getattr(item, "MeasureRelationship", None)
                    
                    setattr(item, "MeasureRelationship", self)
                    

    @property
    def equivalentTo(self):
        return self.__equivalentTo

    @equivalentTo.setter
    def equivalentTo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measure__equivalentTo", None)
        self.__equivalentTo = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Measure23"):
                    opp_val = getattr(item, "Measure23", None)
                    
                    if opp_val == self:
                        setattr(item, "Measure23", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Measure23"):
                    opp_val = getattr(item, "Measure23", None)
                    
                    setattr(item, "Measure23", self)
                    

    @property
    def Measure54(self):
        return self.__Measure54

    @Measure54.setter
    def Measure54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measure__Measure54", None)
        self.__Measure54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trait"):
                opp_val = getattr(old_value, "trait", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trait"):
                opp_val = getattr(value, "trait", None)
                if opp_val is None:
                    setattr(value, "trait", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def equivalentFrom(self):
        return self.__equivalentFrom

    @equivalentFrom.setter
    def equivalentFrom(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measure__equivalentFrom", None)
        self.__equivalentFrom = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Measure26"):
                    opp_val = getattr(item, "Measure26", None)
                    
                    if opp_val == self:
                        setattr(item, "Measure26", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Measure26"):
                    opp_val = getattr(item, "Measure26", None)
                    
                    setattr(item, "Measure26", self)
                    

    @property
    def Measure38(self):
        return self.__Measure38

    @Measure38.setter
    def Measure38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measure__Measure38", None)
        self.__Measure38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "measurement"):
                opp_val = getattr(old_value, "measurement", None)
                if opp_val == self:
                    setattr(old_value, "measurement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "measurement"):
                opp_val = getattr(value, "measurement", None)
                setattr(value, "measurement", self)

    @property
    def smm_Measure27(self):
        return self.__smm_Measure27

    @smm_Measure27.setter
    def smm_Measure27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measure__smm_Measure27", None)
        self.__smm_Measure27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smm_Measure"):
                    opp_val = getattr(item, "smm_Measure", None)
                    
                    if opp_val == self:
                        setattr(item, "smm_Measure", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smm_Measure"):
                    opp_val = getattr(item, "smm_Measure", None)
                    
                    setattr(item, "smm_Measure", self)
                    

    @property
    def Measure46(self):
        return self.__Measure46

    @Measure46.setter
    def Measure46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measure__Measure46", None)
        self.__Measure46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outMeasure"):
                opp_val = getattr(old_value, "outMeasure", None)
                if opp_val == self:
                    setattr(old_value, "outMeasure", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outMeasure"):
                opp_val = getattr(value, "outMeasure", None)
                setattr(value, "outMeasure", self)

    @property
    def characteristics(self):
        return self.__characteristics

    @characteristics.setter
    def characteristics(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measure__characteristics", None)
        self.__characteristics = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Characteristic"):
                opp_val = getattr(old_value, "Characteristic", None)
                if opp_val == self:
                    setattr(old_value, "Characteristic", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Characteristic"):
                opp_val = getattr(value, "Characteristic", None)
                setattr(value, "Characteristic", self)

    @property
    def Measure48(self):
        return self.__Measure48

    @Measure48.setter
    def Measure48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measure__Measure48", None)
        self.__Measure48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "inMeasure"):
                opp_val = getattr(old_value, "inMeasure", None)
                if opp_val == self:
                    setattr(old_value, "inMeasure", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "inMeasure"):
                opp_val = getattr(value, "inMeasure", None)
                setattr(value, "inMeasure", self)

    @property
    def Measure56(self):
        return self.__Measure56

    @Measure56.setter
    def Measure56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measure__Measure56", None)
        self.__Measure56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scope"):
                opp_val = getattr(old_value, "scope", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scope"):
                opp_val = getattr(value, "scope", None)
                if opp_val is None:
                    setattr(value, "scope", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "category18"):
                opp_val = getattr(old_value, "category18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "category18"):
                opp_val = getattr(value, "category18", None)
                if opp_val is None:
                    setattr(value, "category18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Measure26(self):
        return self.__Measure26

    @Measure26.setter
    def Measure26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measure__Measure26", None)
        self.__Measure26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "equivalentFrom"):
                opp_val = getattr(old_value, "equivalentFrom", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "equivalentFrom"):
                opp_val = getattr(value, "equivalentFrom", None)
                if opp_val is None:
                    setattr(value, "equivalentFrom", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Measure23(self):
        return self.__Measure23

    @Measure23.setter
    def Measure23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measure__Measure23", None)
        self.__Measure23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "equivalentTo"):
                opp_val = getattr(old_value, "equivalentTo", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "equivalentTo"):
                opp_val = getattr(value, "equivalentTo", None)
                if opp_val is None:
                    setattr(value, "equivalentTo", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def to33(self):
        return self.__to33

    @to33.setter
    def to33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measure__to33", None)
        self.__to33 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MeasureRelationship34"):
                    opp_val = getattr(item, "MeasureRelationship34", None)
                    
                    if opp_val == self:
                        setattr(item, "MeasureRelationship34", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MeasureRelationship34"):
                    opp_val = getattr(item, "MeasureRelationship34", None)
                    
                    setattr(item, "MeasureRelationship34", self)
                    

    @property
    def measure(self):
        return self.__measure

    @measure.setter
    def measure(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measure__measure", None)
        self.__measure = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Measurement"):
                    opp_val = getattr(item, "Measurement", None)
                    
                    if opp_val == self:
                        setattr(item, "Measurement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Measurement"):
                    opp_val = getattr(item, "Measurement", None)
                    
                    setattr(item, "Measurement", self)
                    

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
                if hasattr(item, "Category20"):
                    opp_val = getattr(item, "Category20", None)
                    
                    if opp_val == self:
                        setattr(item, "Category20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Category20"):
                    opp_val = getattr(item, "Category20", None)
                    
                    setattr(item, "Category20", self)
                    

    @property
    def measures(self):
        return self.__measures

    @measures.setter
    def measures(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measure__measures", None)
        self.__measures = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Scope"):
                opp_val = getattr(old_value, "Scope", None)
                if opp_val == self:
                    setattr(old_value, "Scope", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Scope"):
                opp_val = getattr(value, "Scope", None)
                setattr(value, "Scope", self)

class smm_SmmRelationship(SmmElement):

    def __init__(self):
        
    def getTo(self) -> SmmElement:
        # TODO: Implement getTo method
        pass

    def getFrom(self) -> SmmElement:
        # TODO: Implement getFrom method
        pass

class smm_Characteristic(SmmElement):

    def __init__(self, name: str, Characteristic: "smm_Measure" = None, smm_Characteristic: "smm_Characteristic" = None, smm_Characteristic51: "smm_Characteristic" = None, trait: set["smm_Measure"] = None):
        self.name = name
        self.Characteristic = Characteristic
        self.smm_Characteristic = smm_Characteristic
        self.smm_Characteristic51 = smm_Characteristic51
        self.trait = trait if trait is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def smm_Characteristic(self):
        return self.__smm_Characteristic

    @smm_Characteristic.setter
    def smm_Characteristic(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Characteristic__smm_Characteristic", None)
        self.__smm_Characteristic = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_Characteristic51"):
                opp_val = getattr(old_value, "smm_Characteristic51", None)
                if opp_val == self:
                    setattr(old_value, "smm_Characteristic51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_Characteristic51"):
                opp_val = getattr(value, "smm_Characteristic51", None)
                setattr(value, "smm_Characteristic51", self)

    @property
    def trait(self):
        return self.__trait

    @trait.setter
    def trait(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Characteristic__trait", None)
        self.__trait = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Measure54"):
                    opp_val = getattr(item, "Measure54", None)
                    
                    if opp_val == self:
                        setattr(item, "Measure54", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Measure54"):
                    opp_val = getattr(item, "Measure54", None)
                    
                    setattr(item, "Measure54", self)
                    

    @property
    def Characteristic(self):
        return self.__Characteristic

    @Characteristic.setter
    def Characteristic(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Characteristic__Characteristic", None)
        self.__Characteristic = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "characteristics"):
                opp_val = getattr(old_value, "characteristics", None)
                if opp_val == self:
                    setattr(old_value, "characteristics", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "characteristics"):
                opp_val = getattr(value, "characteristics", None)
                setattr(value, "characteristics", self)

    @property
    def smm_Characteristic51(self):
        return self.__smm_Characteristic51

    @smm_Characteristic51.setter
    def smm_Characteristic51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Characteristic__smm_Characteristic51", None)
        self.__smm_Characteristic51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_Characteristic"):
                opp_val = getattr(old_value, "smm_Characteristic", None)
                if opp_val == self:
                    setattr(old_value, "smm_Characteristic", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_Characteristic"):
                opp_val = getattr(value, "smm_Characteristic", None)
                setattr(value, "smm_Characteristic", self)

class smm_Annotation(SmmElement):

    def __init__(self, text: str, Annotation: "smm_SmmElement" = None, annotation: "smm_SmmElement" = None):
        self.text = text
        self.Annotation = Annotation
        self.annotation = annotation
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def Annotation(self):
        return self.__Annotation

    @Annotation.setter
    def Annotation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Annotation__Annotation", None)
        self.__Annotation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owner3"):
                opp_val = getattr(old_value, "owner3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner3"):
                opp_val = getattr(value, "owner3", None)
                if opp_val is None:
                    setattr(value, "owner3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def annotation(self):
        return self.__annotation

    @annotation.setter
    def annotation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Annotation__annotation", None)
        self.__annotation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SmmElement75"):
                opp_val = getattr(old_value, "SmmElement75", None)
                if opp_val == self:
                    setattr(old_value, "SmmElement75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SmmElement75"):
                opp_val = getattr(value, "SmmElement75", None)
                setattr(value, "SmmElement75", self)

class smm_Attribute(SmmElement):

    def __init__(self, tag: str, value: str, Attribute: "smm_SmmElement" = None, attribute: "smm_SmmElement" = None):
        self.tag = tag
        self.value = value
        self.Attribute = Attribute
        self.attribute = attribute
        
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
    def attribute(self):
        return self.__attribute

    @attribute.setter
    def attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Attribute__attribute", None)
        self.__attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SmmElement73"):
                opp_val = getattr(old_value, "SmmElement73", None)
                if opp_val == self:
                    setattr(old_value, "SmmElement73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SmmElement73"):
                opp_val = getattr(value, "SmmElement73", None)
                setattr(value, "SmmElement73", self)

    @property
    def Attribute(self):
        return self.__Attribute

    @Attribute.setter
    def Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Attribute__Attribute", None)
        self.__Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owner"):
                opp_val = getattr(old_value, "owner", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner"):
                opp_val = getattr(value, "owner", None)
                if opp_val is None:
                    setattr(value, "owner", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class smm_SmmModel(SmmElement):

    pass
class smm_Category(SmmElement):

    def __init__(self, name: str, Category: "smm_CategoryRelationship" = None, Category7: "smm_CategoryRelationship" = None, Category10: "smm_Category" = None, categoryElement: set["smm_Category"] = None, Category13: "smm_Category" = None, category: set["smm_Category"] = None, from: set["smm_CategoryRelationship"] = None, to: set["smm_CategoryRelationship"] = None, category18: set["smm_Measure"] = None, Category20: "smm_Measure" = None):
        self.name = name
        self.Category = Category
        self.Category7 = Category7
        self.Category10 = Category10
        self.categoryElement = categoryElement if categoryElement is not None else set()
        self.Category13 = Category13
        self.category = category if category is not None else set()
        self.from = from if from is not None else set()
        self.to = to if to is not None else set()
        self.category18 = category18 if category18 is not None else set()
        self.Category20 = Category20
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Category13(self):
        return self.__Category13

    @Category13.setter
    def Category13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Category__Category13", None)
        self.__Category13 = value
        
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
    def Category(self):
        return self.__Category

    @Category.setter
    def Category(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Category__Category", None)
        self.__Category = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outCategory"):
                opp_val = getattr(old_value, "outCategory", None)
                if opp_val == self:
                    setattr(old_value, "outCategory", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outCategory"):
                opp_val = getattr(value, "outCategory", None)
                setattr(value, "outCategory", self)

    @property
    def from(self):
        return self.__from

    @from.setter
    def from(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Category__from", None)
        self.__from = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CategoryRelationship"):
                    opp_val = getattr(item, "CategoryRelationship", None)
                    
                    if opp_val == self:
                        setattr(item, "CategoryRelationship", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CategoryRelationship"):
                    opp_val = getattr(item, "CategoryRelationship", None)
                    
                    setattr(item, "CategoryRelationship", self)
                    

    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Category__category", None)
        self.__category = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Category13"):
                    opp_val = getattr(item, "Category13", None)
                    
                    if opp_val == self:
                        setattr(item, "Category13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Category13"):
                    opp_val = getattr(item, "Category13", None)
                    
                    setattr(item, "Category13", self)
                    

    @property
    def category18(self):
        return self.__category18

    @category18.setter
    def category18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Category__category18", None)
        self.__category18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Measure"):
                    opp_val = getattr(item, "Measure", None)
                    
                    if opp_val == self:
                        setattr(item, "Measure", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Measure"):
                    opp_val = getattr(item, "Measure", None)
                    
                    setattr(item, "Measure", self)
                    

    @property
    def Category10(self):
        return self.__Category10

    @Category10.setter
    def Category10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Category__Category10", None)
        self.__Category10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "categoryElement"):
                opp_val = getattr(old_value, "categoryElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "categoryElement"):
                opp_val = getattr(value, "categoryElement", None)
                if opp_val is None:
                    setattr(value, "categoryElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Category20(self):
        return self.__Category20

    @Category20.setter
    def Category20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Category__Category20", None)
        self.__Category20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "categoryMeasure"):
                opp_val = getattr(old_value, "categoryMeasure", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "categoryMeasure"):
                opp_val = getattr(value, "categoryMeasure", None)
                if opp_val is None:
                    setattr(value, "categoryMeasure", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def categoryElement(self):
        return self.__categoryElement

    @categoryElement.setter
    def categoryElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Category__categoryElement", None)
        self.__categoryElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Category10"):
                    opp_val = getattr(item, "Category10", None)
                    
                    if opp_val == self:
                        setattr(item, "Category10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Category10"):
                    opp_val = getattr(item, "Category10", None)
                    
                    setattr(item, "Category10", self)
                    

    @property
    def Category7(self):
        return self.__Category7

    @Category7.setter
    def Category7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Category__Category7", None)
        self.__Category7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "inCategory"):
                opp_val = getattr(old_value, "inCategory", None)
                if opp_val == self:
                    setattr(old_value, "inCategory", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "inCategory"):
                opp_val = getattr(value, "inCategory", None)
                setattr(value, "inCategory", self)

    @property
    def to(self):
        return self.__to

    @to.setter
    def to(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Category__to", None)
        self.__to = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CategoryRelationship16"):
                    opp_val = getattr(item, "CategoryRelationship16", None)
                    
                    if opp_val == self:
                        setattr(item, "CategoryRelationship16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CategoryRelationship16"):
                    opp_val = getattr(item, "CategoryRelationship16", None)
                    
                    setattr(item, "CategoryRelationship16", self)
                    

class smm_SmmElement(ABC):

    def __init__(self, modelElement: "smm_SmmModel" = None, owner: set["smm_Attribute"] = None, owner3: set["smm_Annotation"] = None, SmmElement: "smm_SmmModel" = None, SmmElement73: "smm_Attribute" = None, SmmElement75: "smm_Annotation" = None):
        self.modelElement = modelElement
        self.owner = owner if owner is not None else set()
        self.owner3 = owner3 if owner3 is not None else set()
        self.SmmElement = SmmElement
        self.SmmElement73 = SmmElement73
        self.SmmElement75 = SmmElement75
        
    @property
    def owner3(self):
        return self.__owner3

    @owner3.setter
    def owner3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_SmmElement__owner3", None)
        self.__owner3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Annotation"):
                    opp_val = getattr(item, "Annotation", None)
                    
                    if opp_val == self:
                        setattr(item, "Annotation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Annotation"):
                    opp_val = getattr(item, "Annotation", None)
                    
                    setattr(item, "Annotation", self)
                    

    @property
    def SmmElement75(self):
        return self.__SmmElement75

    @SmmElement75.setter
    def SmmElement75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_SmmElement__SmmElement75", None)
        self.__SmmElement75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "annotation"):
                opp_val = getattr(old_value, "annotation", None)
                if opp_val == self:
                    setattr(old_value, "annotation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "annotation"):
                opp_val = getattr(value, "annotation", None)
                setattr(value, "annotation", self)

    @property
    def SmmElement73(self):
        return self.__SmmElement73

    @SmmElement73.setter
    def SmmElement73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_SmmElement__SmmElement73", None)
        self.__SmmElement73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "attribute"):
                opp_val = getattr(old_value, "attribute", None)
                if opp_val == self:
                    setattr(old_value, "attribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "attribute"):
                opp_val = getattr(value, "attribute", None)
                setattr(value, "attribute", self)

    @property
    def modelElement(self):
        return self.__modelElement

    @modelElement.setter
    def modelElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_SmmElement__modelElement", None)
        self.__modelElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SmmModel"):
                opp_val = getattr(old_value, "SmmModel", None)
                if opp_val == self:
                    setattr(old_value, "SmmModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SmmModel"):
                opp_val = getattr(value, "SmmModel", None)
                setattr(value, "SmmModel", self)

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
            if hasattr(old_value, "model"):
                opp_val = getattr(old_value, "model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model"):
                opp_val = getattr(value, "model", None)
                if opp_val is None:
                    setattr(value, "model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_SmmElement__owner", None)
        self.__owner = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Attribute"):
                    opp_val = getattr(item, "Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Attribute"):
                    opp_val = getattr(item, "Attribute", None)
                    
                    setattr(item, "Attribute", self)
                    

    def getOutbound(self) -> str:
        # TODO: Implement getOutbound method
        pass

    def getInbound(self) -> str:
        # TODO: Implement getInbound method
        pass
