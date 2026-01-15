from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class AngleOperation:

    pass
class QuantityHomogenousOperation:

    pass
class units_AngleDistinct(QuantityHomogenousOperation, AngleOperation):

    pass
class units_AngleGreater(QuantityHomogenousOperation, AngleOperation):

    pass
class units_AngleSmaller(QuantityHomogenousOperation, AngleOperation):

    pass
class units_AngleSubtract(QuantityHomogenousOperation, AngleOperation):

    pass
class units_AngleAdd(QuantityHomogenousOperation, AngleOperation):

    pass
class units_AngleEquals(QuantityHomogenousOperation, AngleOperation):

    pass
class LengthOperation:

    pass
class units_LengthGreater(QuantityHomogenousOperation, LengthOperation):

    pass
class units_LengthAdd(QuantityHomogenousOperation, LengthOperation):

    pass
class QuantityOperation:

    pass
class units_QuantityArithmeticOperation(QuantityOperation):

    pass
class units_AngleOperation(QuantityOperation):

    pass
class units_QuantityScalarOperation(QuantityOperation):

    def __init__(self, rhs: float, units_QuantityScalarOperation: "units_Quantity" = None):
        self.rhs = rhs
        self.units_QuantityScalarOperation = units_QuantityScalarOperation
        
    @property
    def rhs(self) -> float:
        return self.__rhs

    @rhs.setter
    def rhs(self, rhs: float):
        self.__rhs = rhs

    @property
    def units_QuantityScalarOperation(self):
        return self.__units_QuantityScalarOperation

    @units_QuantityScalarOperation.setter
    def units_QuantityScalarOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_units_QuantityScalarOperation__units_QuantityScalarOperation", None)
        self.__units_QuantityScalarOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "units_Quantity7"):
                opp_val = getattr(old_value, "units_Quantity7", None)
                if opp_val == self:
                    setattr(old_value, "units_Quantity7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "units_Quantity7"):
                opp_val = getattr(value, "units_Quantity7", None)
                setattr(value, "units_Quantity7", self)

class units_QuantityHomogenousOperation(QuantityOperation):

    pass
class units_QuantityComparisonOperation(QuantityOperation):

    pass
class units_LengthOperation(QuantityOperation):

    pass
class units_QuantityOperation(ABC):

    pass
class Quantity:

    pass
class units_Angle(Quantity):

    pass
class units_Length(Quantity):

    pass
class units_Quantity(ABC):

    def __init__(self, value: float, units_Quantity: "units_Unit" = None, units_Quantity2: "units_QuantityHomogenousOperation" = None, units_Quantity5: "units_QuantityHomogenousOperation" = None, units_Quantity7: "units_QuantityScalarOperation" = None):
        self.value = value
        self.units_Quantity = units_Quantity
        self.units_Quantity2 = units_Quantity2
        self.units_Quantity5 = units_Quantity5
        self.units_Quantity7 = units_Quantity7
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def units_Quantity7(self):
        return self.__units_Quantity7

    @units_Quantity7.setter
    def units_Quantity7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_units_Quantity__units_Quantity7", None)
        self.__units_Quantity7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "units_QuantityScalarOperation"):
                opp_val = getattr(old_value, "units_QuantityScalarOperation", None)
                if opp_val == self:
                    setattr(old_value, "units_QuantityScalarOperation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "units_QuantityScalarOperation"):
                opp_val = getattr(value, "units_QuantityScalarOperation", None)
                setattr(value, "units_QuantityScalarOperation", self)

    @property
    def units_Quantity(self):
        return self.__units_Quantity

    @units_Quantity.setter
    def units_Quantity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_units_Quantity__units_Quantity", None)
        self.__units_Quantity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "units_Unit"):
                opp_val = getattr(old_value, "units_Unit", None)
                if opp_val == self:
                    setattr(old_value, "units_Unit", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "units_Unit"):
                opp_val = getattr(value, "units_Unit", None)
                setattr(value, "units_Unit", self)

    @property
    def units_Quantity2(self):
        return self.__units_Quantity2

    @units_Quantity2.setter
    def units_Quantity2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_units_Quantity__units_Quantity2", None)
        self.__units_Quantity2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "units_QuantityHomogenousOperation"):
                opp_val = getattr(old_value, "units_QuantityHomogenousOperation", None)
                if opp_val == self:
                    setattr(old_value, "units_QuantityHomogenousOperation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "units_QuantityHomogenousOperation"):
                opp_val = getattr(value, "units_QuantityHomogenousOperation", None)
                setattr(value, "units_QuantityHomogenousOperation", self)

    @property
    def units_Quantity5(self):
        return self.__units_Quantity5

    @units_Quantity5.setter
    def units_Quantity5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_units_Quantity__units_Quantity5", None)
        self.__units_Quantity5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "units_QuantityHomogenousOperation4"):
                opp_val = getattr(old_value, "units_QuantityHomogenousOperation4", None)
                if opp_val == self:
                    setattr(old_value, "units_QuantityHomogenousOperation4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "units_QuantityHomogenousOperation4"):
                opp_val = getattr(value, "units_QuantityHomogenousOperation4", None)
                setattr(value, "units_QuantityHomogenousOperation4", self)

class AngleUnit:

    pass
class units_Turn(AngleUnit):

    pass
class units_Gradian(AngleUnit):

    pass
class units_Degree(AngleUnit):

    pass
class units_Radian(AngleUnit):

    pass
class units_LengthSmaller(QuantityHomogenousOperation, LengthOperation):

    pass
class units_LengthDistinct(QuantityHomogenousOperation, LengthOperation):

    pass
class units_LengthEquals(QuantityHomogenousOperation, LengthOperation):

    pass
class QuantityScalarOperation:

    pass
class units_AngleScalarDivide(AngleOperation, QuantityScalarOperation):

    pass
class units_LengthScalarDivide(QuantityScalarOperation, LengthOperation):

    pass
class units_AngleScalarMultiply(AngleOperation, QuantityScalarOperation):

    pass
class units_LengthScalarMultiply(LengthOperation, QuantityScalarOperation):

    pass
class units_LengthSubtract(QuantityHomogenousOperation, LengthOperation):

    pass
class Unit:

    pass
class units_ImperialSystemUnit(Unit):

    pass
class units_MetricSystemUnit(Unit):

    pass
class units_AngleUnit(Unit):

    pass
class units_LengthUnit(Unit):

    pass
class units_Unit(ABC):

    pass
class ImperialSystemUnit:

    pass
class LengthUnit:

    pass
class units_Inch(ImperialSystemUnit, LengthUnit):

    pass
class units_Foot(ImperialSystemUnit, LengthUnit):

    pass
class units_Yard(ImperialSystemUnit, LengthUnit):

    pass
class MetricSystemUnit:

    pass
class units_Meter(MetricSystemUnit, LengthUnit):

    pass
class units_Millimeter(MetricSystemUnit, LengthUnit):

    pass
class units_Centimeter(MetricSystemUnit, LengthUnit):

    pass