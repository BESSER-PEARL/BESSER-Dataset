from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Type(Enum):
    Energy = "Energy"
    Duration = "Duration"
    Power = "Power"
    Current = "Current"
    Voltage = "Voltage"
    Scalar = "Scalar"
    Frequency = "Frequency"
class Visibility(Enum):
    LOCAL = "LOCAL"
    GLOBAL = "GLOBAL"


############################################
# Definition of Classes
############################################

class eel_Sample:

    pass
class MeasurementUncertaintyInformation:

    pass
class eel_Sampling(MeasurementUncertaintyInformation):

    def __init__(self, measurementProcedure: str, eel_Sampling: set["eel_Sample"] = None):
        self.measurementProcedure = measurementProcedure
        self.eel_Sampling = eel_Sampling if eel_Sampling is not None else set()
        
    @property
    def measurementProcedure(self) -> str:
        return self.__measurementProcedure

    @measurementProcedure.setter
    def measurementProcedure(self, measurementProcedure: str):
        self.__measurementProcedure = measurementProcedure

    @property
    def eel_Sampling(self):
        return self.__eel_Sampling

    @eel_Sampling.setter
    def eel_Sampling(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eel_Sampling__eel_Sampling", None)
        self.__eel_Sampling = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eel_Sample"):
                    opp_val = getattr(item, "eel_Sample", None)
                    
                    if opp_val == self:
                        setattr(item, "eel_Sample", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eel_Sample"):
                    opp_val = getattr(item, "eel_Sample", None)
                    
                    setattr(item, "eel_Sample", self)
                    

class eel_Interval(MeasurementUncertaintyInformation):

    pass
class eel_NormalDistribution(MeasurementUncertaintyInformation):

    def __init__(self, meanValue: str, standardDeviation: str):
        self.meanValue = meanValue
        self.standardDeviation = standardDeviation
        
    @property
    def meanValue(self) -> str:
        return self.__meanValue

    @meanValue.setter
    def meanValue(self, meanValue: str):
        self.__meanValue = meanValue

    @property
    def standardDeviation(self) -> str:
        return self.__standardDeviation

    @standardDeviation.setter
    def standardDeviation(self, standardDeviation: str):
        self.__standardDeviation = standardDeviation

class eel_MeasurementUncertaintyInformation(ABC):

    pass
class eel_Integral(MeasurementUncertaintyInformation):

    def __init__(self, function: str, eel_Integral: "eel_Interval" = None):
        self.function = function
        self.eel_Integral = eel_Integral
        
    @property
    def function(self) -> str:
        return self.__function

    @function.setter
    def function(self, function: str):
        self.__function = function

    @property
    def eel_Integral(self):
        return self.__eel_Integral

    @eel_Integral.setter
    def eel_Integral(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eel_Integral__eel_Integral", None)
        self.__eel_Integral = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eel_Interval23"):
                opp_val = getattr(old_value, "eel_Interval23", None)
                if opp_val == self:
                    setattr(old_value, "eel_Interval23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eel_Interval23"):
                opp_val = getattr(value, "eel_Interval23", None)
                setattr(value, "eel_Interval23", self)

class MeasureUnboundOperation:

    pass
class eel_MeasureUnboundProductOperation(MeasureUnboundOperation):

    def __init__(self):
        
    def value(self) -> str:
        # TODO: Implement value method
        pass

class eel_MeasureUnboundSumOperation(MeasureUnboundOperation):

    def __init__(self):
        
    def value(self) -> str:
        # TODO: Implement value method
        pass

class MeasureBinaryProductOperation:

    pass
class eel_PowerComputation(MeasureBinaryProductOperation):

    def __init__(self):
        
    def type(self) -> str:
        # TODO: Implement type method
        pass

    def value(self) -> str:
        # TODO: Implement value method
        pass

class eel_EnergyComputation(MeasureBinaryProductOperation):

    def __init__(self):
        
    def value(self) -> str:
        # TODO: Implement value method
        pass

    def type(self) -> str:
        # TODO: Implement type method
        pass

class MeasureBinaryOperation:

    pass
class eel_MeasureBinarySumOperation(MeasureBinaryOperation):

    def __init__(self):
        
    def value(self) -> str:
        # TODO: Implement value method
        pass

class eel_MeasureBinaryProductOperation(MeasureBinaryOperation):

    def __init__(self):
        
    def value(self) -> str:
        # TODO: Implement value method
        pass

class MeasureValue:

    pass
class eel_RealTimeDuration(MeasureValue):

    def __init__(self):
        
    def type(self) -> str:
        # TODO: Implement type method
        pass

class eel_MeasureAttribute(MeasureValue):

    def __init__(self, att: str):
        self.att = att
        
    @property
    def att(self) -> str:
        return self.__att

    @att.setter
    def att(self, att: str):
        self.__att = att

class eel_MeasureOCL(MeasureValue):

    def __init__(self, oclQuery: str):
        self.oclQuery = oclQuery
        
    @property
    def oclQuery(self) -> str:
        return self.__oclQuery

    @oclQuery.setter
    def oclQuery(self, oclQuery: str):
        self.__oclQuery = oclQuery

class TypedMeasure:

    pass
class eel_MeasureUnboundOperation(TypedMeasure):

    pass
class eel_MeasureValue(TypedMeasure):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    def value(self) -> str:
        # TODO: Implement value method
        pass

class eel_MeasureBinaryOperation(TypedMeasure):

    pass
class eel_MeasureCast(TypedMeasure):

    pass
class eel_Measure(ABC):

    def __init__(self, name: str, subname: str, targetClass: str, targetOperation: str, eel_Measure4: "eel_MeasurementUncertainty" = None, eel_Measure: "eel_Platform" = None, eel_Measure6: "eel_MeasureCast" = None, eel_Measure8: "eel_MeasureBinaryOperation" = None, eel_Measure11: "eel_MeasureBinaryOperation" = None, eel_Measure13: "eel_MeasureUnboundOperation" = None, eel_Measure26: "eel_Sample" = None, eel_Measure17: "eel_Interval" = None, eel_Measure20: "eel_Interval" = None):
        self.name = name
        self.subname = subname
        self.targetClass = targetClass
        self.targetOperation = targetOperation
        self.eel_Measure4 = eel_Measure4
        self.eel_Measure = eel_Measure
        self.eel_Measure6 = eel_Measure6
        self.eel_Measure8 = eel_Measure8
        self.eel_Measure11 = eel_Measure11
        self.eel_Measure13 = eel_Measure13
        self.eel_Measure26 = eel_Measure26
        self.eel_Measure17 = eel_Measure17
        self.eel_Measure20 = eel_Measure20
        
    @property
    def targetOperation(self) -> str:
        return self.__targetOperation

    @targetOperation.setter
    def targetOperation(self, targetOperation: str):
        self.__targetOperation = targetOperation

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def subname(self) -> str:
        return self.__subname

    @subname.setter
    def subname(self, subname: str):
        self.__subname = subname

    @property
    def targetClass(self) -> str:
        return self.__targetClass

    @targetClass.setter
    def targetClass(self, targetClass: str):
        self.__targetClass = targetClass

    @property
    def eel_Measure20(self):
        return self.__eel_Measure20

    @eel_Measure20.setter
    def eel_Measure20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eel_Measure__eel_Measure20", None)
        self.__eel_Measure20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eel_Interval19"):
                opp_val = getattr(old_value, "eel_Interval19", None)
                if opp_val == self:
                    setattr(old_value, "eel_Interval19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eel_Interval19"):
                opp_val = getattr(value, "eel_Interval19", None)
                setattr(value, "eel_Interval19", self)

    @property
    def eel_Measure8(self):
        return self.__eel_Measure8

    @eel_Measure8.setter
    def eel_Measure8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eel_Measure__eel_Measure8", None)
        self.__eel_Measure8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eel_MeasureBinaryOperation"):
                opp_val = getattr(old_value, "eel_MeasureBinaryOperation", None)
                if opp_val == self:
                    setattr(old_value, "eel_MeasureBinaryOperation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eel_MeasureBinaryOperation"):
                opp_val = getattr(value, "eel_MeasureBinaryOperation", None)
                setattr(value, "eel_MeasureBinaryOperation", self)

    @property
    def eel_Measure17(self):
        return self.__eel_Measure17

    @eel_Measure17.setter
    def eel_Measure17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eel_Measure__eel_Measure17", None)
        self.__eel_Measure17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eel_Interval"):
                opp_val = getattr(old_value, "eel_Interval", None)
                if opp_val == self:
                    setattr(old_value, "eel_Interval", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eel_Interval"):
                opp_val = getattr(value, "eel_Interval", None)
                setattr(value, "eel_Interval", self)

    @property
    def eel_Measure(self):
        return self.__eel_Measure

    @eel_Measure.setter
    def eel_Measure(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eel_Measure__eel_Measure", None)
        self.__eel_Measure = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eel_Platform2"):
                opp_val = getattr(old_value, "eel_Platform2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eel_Platform2"):
                opp_val = getattr(value, "eel_Platform2", None)
                if opp_val is None:
                    setattr(value, "eel_Platform2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eel_Measure13(self):
        return self.__eel_Measure13

    @eel_Measure13.setter
    def eel_Measure13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eel_Measure__eel_Measure13", None)
        self.__eel_Measure13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eel_MeasureUnboundOperation"):
                opp_val = getattr(old_value, "eel_MeasureUnboundOperation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eel_MeasureUnboundOperation"):
                opp_val = getattr(value, "eel_MeasureUnboundOperation", None)
                if opp_val is None:
                    setattr(value, "eel_MeasureUnboundOperation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eel_Measure6(self):
        return self.__eel_Measure6

    @eel_Measure6.setter
    def eel_Measure6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eel_Measure__eel_Measure6", None)
        self.__eel_Measure6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eel_MeasureCast"):
                opp_val = getattr(old_value, "eel_MeasureCast", None)
                if opp_val == self:
                    setattr(old_value, "eel_MeasureCast", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eel_MeasureCast"):
                opp_val = getattr(value, "eel_MeasureCast", None)
                setattr(value, "eel_MeasureCast", self)

    @property
    def eel_Measure4(self):
        return self.__eel_Measure4

    @eel_Measure4.setter
    def eel_Measure4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eel_Measure__eel_Measure4", None)
        self.__eel_Measure4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eel_MeasurementUncertainty"):
                opp_val = getattr(old_value, "eel_MeasurementUncertainty", None)
                if opp_val == self:
                    setattr(old_value, "eel_MeasurementUncertainty", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eel_MeasurementUncertainty"):
                opp_val = getattr(value, "eel_MeasurementUncertainty", None)
                setattr(value, "eel_MeasurementUncertainty", self)

    @property
    def eel_Measure26(self):
        return self.__eel_Measure26

    @eel_Measure26.setter
    def eel_Measure26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eel_Measure__eel_Measure26", None)
        self.__eel_Measure26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eel_Sample25"):
                opp_val = getattr(old_value, "eel_Sample25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eel_Sample25"):
                opp_val = getattr(value, "eel_Sample25", None)
                if opp_val is None:
                    setattr(value, "eel_Sample25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eel_Measure11(self):
        return self.__eel_Measure11

    @eel_Measure11.setter
    def eel_Measure11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eel_Measure__eel_Measure11", None)
        self.__eel_Measure11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eel_MeasureBinaryOperation10"):
                opp_val = getattr(old_value, "eel_MeasureBinaryOperation10", None)
                if opp_val == self:
                    setattr(old_value, "eel_MeasureBinaryOperation10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eel_MeasureBinaryOperation10"):
                opp_val = getattr(value, "eel_MeasureBinaryOperation10", None)
                setattr(value, "eel_MeasureBinaryOperation10", self)

    def name(self) -> str:
        # TODO: Implement name method
        pass

    def value(self) -> str:
        # TODO: Implement value method
        pass

    def type(self) -> str:
        # TODO: Implement type method
        pass

class eel_Variable:

    def __init__(self, value: str, name: str, vibility: str, eel_Variable: "eel_Platform" = None):
        self.value = value
        self.name = name
        self.vibility = vibility
        self.eel_Variable = eel_Variable
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def vibility(self) -> str:
        return self.__vibility

    @vibility.setter
    def vibility(self, vibility: str):
        self.__vibility = vibility

    @property
    def eel_Variable(self):
        return self.__eel_Variable

    @eel_Variable.setter
    def eel_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eel_Variable__eel_Variable", None)
        self.__eel_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eel_Platform"):
                opp_val = getattr(old_value, "eel_Platform", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eel_Platform"):
                opp_val = getattr(value, "eel_Platform", None)
                if opp_val is None:
                    setattr(value, "eel_Platform", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class eel_Platform:

    def __init__(self, name: str, eel_Platform: set["eel_Variable"] = None, eel_Platform2: set["eel_Measure"] = None):
        self.name = name
        self.eel_Platform = eel_Platform if eel_Platform is not None else set()
        self.eel_Platform2 = eel_Platform2 if eel_Platform2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def eel_Platform2(self):
        return self.__eel_Platform2

    @eel_Platform2.setter
    def eel_Platform2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eel_Platform__eel_Platform2", None)
        self.__eel_Platform2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eel_Measure"):
                    opp_val = getattr(item, "eel_Measure", None)
                    
                    if opp_val == self:
                        setattr(item, "eel_Measure", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eel_Measure"):
                    opp_val = getattr(item, "eel_Measure", None)
                    
                    setattr(item, "eel_Measure", self)
                    

    @property
    def eel_Platform(self):
        return self.__eel_Platform

    @eel_Platform.setter
    def eel_Platform(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eel_Platform__eel_Platform", None)
        self.__eel_Platform = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eel_Variable"):
                    opp_val = getattr(item, "eel_Variable", None)
                    
                    if opp_val == self:
                        setattr(item, "eel_Variable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eel_Variable"):
                    opp_val = getattr(item, "eel_Variable", None)
                    
                    setattr(item, "eel_Variable", self)
                    

class Measure:

    pass
class eel_TypedMeasure(Measure):

    def __init__(self, type: str):
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    def type(self) -> str:
        # TODO: Implement type method
        pass

    def name(self) -> str:
        # TODO: Implement name method
        pass

class eel_MeasurementUncertainty:

    def __init__(self, standardUncertainty: str, eel_MeasurementUncertainty: "eel_Measure" = None, eel_MeasurementUncertainty15: "eel_MeasurementUncertaintyInformation" = None):
        self.standardUncertainty = standardUncertainty
        self.eel_MeasurementUncertainty = eel_MeasurementUncertainty
        self.eel_MeasurementUncertainty15 = eel_MeasurementUncertainty15
        
    @property
    def standardUncertainty(self) -> str:
        return self.__standardUncertainty

    @standardUncertainty.setter
    def standardUncertainty(self, standardUncertainty: str):
        self.__standardUncertainty = standardUncertainty

    @property
    def eel_MeasurementUncertainty(self):
        return self.__eel_MeasurementUncertainty

    @eel_MeasurementUncertainty.setter
    def eel_MeasurementUncertainty(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eel_MeasurementUncertainty__eel_MeasurementUncertainty", None)
        self.__eel_MeasurementUncertainty = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eel_Measure4"):
                opp_val = getattr(old_value, "eel_Measure4", None)
                if opp_val == self:
                    setattr(old_value, "eel_Measure4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eel_Measure4"):
                opp_val = getattr(value, "eel_Measure4", None)
                setattr(value, "eel_Measure4", self)

    @property
    def eel_MeasurementUncertainty15(self):
        return self.__eel_MeasurementUncertainty15

    @eel_MeasurementUncertainty15.setter
    def eel_MeasurementUncertainty15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eel_MeasurementUncertainty__eel_MeasurementUncertainty15", None)
        self.__eel_MeasurementUncertainty15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eel_MeasurementUncertaintyInformation"):
                opp_val = getattr(old_value, "eel_MeasurementUncertaintyInformation", None)
                if opp_val == self:
                    setattr(old_value, "eel_MeasurementUncertaintyInformation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eel_MeasurementUncertaintyInformation"):
                opp_val = getattr(value, "eel_MeasurementUncertaintyInformation", None)
                setattr(value, "eel_MeasurementUncertaintyInformation", self)
