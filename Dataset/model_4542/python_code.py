from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class AngleOperation:

    pass
class QuantityScalarOperation:

    pass
class units_AngleScalarMultiply(AngleOperation, QuantityScalarOperation):

    pass
class units_AngleScalarDivide(AngleOperation, QuantityScalarOperation):

    pass
class QuantityHomogenousOperation:

    pass
class units_AngleDistinct(AngleOperation, QuantityHomogenousOperation):

    pass
class units_AngleGreater(AngleOperation, QuantityHomogenousOperation):

    pass
class units_AngleAdd(AngleOperation, QuantityHomogenousOperation):

    pass
class units_AngleEquals(AngleOperation, QuantityHomogenousOperation):

    pass
class units_AngleSubtract(AngleOperation, QuantityHomogenousOperation):

    pass
class units_AngleSmaller(AngleOperation, QuantityHomogenousOperation):

    pass
class LengthOperation:

    pass
class units_LengthEquals(LengthOperation, QuantityHomogenousOperation):

    pass
class units_LengthSubtract(LengthOperation, QuantityHomogenousOperation):

    pass
class units_LengthScalarMultiply(LengthOperation, QuantityScalarOperation):

    pass
class units_LengthSmaller(LengthOperation, QuantityHomogenousOperation):

    pass
class units_LengthScalarDivide(LengthOperation, QuantityScalarOperation):

    pass
class units_LengthDistinct(LengthOperation, QuantityHomogenousOperation):

    pass
class units_LengthGreater(LengthOperation, QuantityHomogenousOperation):

    pass
class units_LengthAdd(LengthOperation, QuantityHomogenousOperation):

    pass
class QuantityOperation:

    pass
class units_QuantityComparisonOperation(QuantityOperation):

    pass
class units_AngleOperation(QuantityOperation):

    pass
class units_QuantityHomogenousOperation(QuantityOperation):

    pass
class units_QuantityArithmeticOperation(QuantityOperation):

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

class units_LengthOperation(QuantityOperation):

    pass
class units_QuantityOperation(ABC):

    pass
class Quantity:

    pass
class units_Angle(Quantity):

    def __init__(self):
        
    def toRad(self):
        # TODO: Implement toRad method
        pass

    def print(self):
        # TODO: Implement print method
        pass

class units_Length(Quantity):

    def __init__(self):
        
    def toCm(self):
        # TODO: Implement toCm method
        pass

    def print(self):
        # TODO: Implement print method
        pass

class units_Quantity(ABC):

    def __init__(self, value: str, units_Quantity: "units_Unit" = None, units_Quantity2: "units_QuantityHomogenousOperation" = None, units_Quantity5: "units_QuantityHomogenousOperation" = None, units_Quantity7: "units_QuantityScalarOperation" = None):
        self.value = value
        self.units_Quantity = units_Quantity
        self.units_Quantity2 = units_Quantity2
        self.units_Quantity5 = units_Quantity5
        self.units_Quantity7 = units_Quantity7
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

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

    def getNormalized(self):
        # TODO: Implement getNormalized method
        pass

    def print(self):
        # TODO: Implement print method
        pass

class ImperialSystemUnit:

    pass
class AngleUnit:

    pass
class units_Gradian(AngleUnit):

    def __init__(self):
        
    def toRad(self, value: float):
        # TODO: Implement toRad method
        pass

    def getSymbol(self):
        # TODO: Implement getSymbol method
        pass

class units_Turn(AngleUnit):

    def __init__(self):
        
    def toRad(self, value: float):
        # TODO: Implement toRad method
        pass

    def getSymbol(self):
        # TODO: Implement getSymbol method
        pass

class units_Degree(AngleUnit):

    def __init__(self):
        
    def toRad(self, value: float):
        # TODO: Implement toRad method
        pass

    def getSymbol(self):
        # TODO: Implement getSymbol method
        pass

class units_Radian(AngleUnit):

    def __init__(self):
        
    def getSymbol(self):
        # TODO: Implement getSymbol method
        pass

    def toRad(self, value: float):
        # TODO: Implement toRad method
        pass

class LengthUnit:

    pass
class units_Inch(LengthUnit, ImperialSystemUnit):

    def __init__(self):
        
    def toCm(self, value: float):
        # TODO: Implement toCm method
        pass

    def getSymbol(self):
        # TODO: Implement getSymbol method
        pass

class units_Yard(LengthUnit, ImperialSystemUnit):

    def __init__(self):
        
    def getSymbol(self):
        # TODO: Implement getSymbol method
        pass

    def toCm(self, value: float):
        # TODO: Implement toCm method
        pass

class units_Foot(LengthUnit, ImperialSystemUnit):

    def __init__(self):
        
    def toCm(self, value: float):
        # TODO: Implement toCm method
        pass

    def getSymbol(self):
        # TODO: Implement getSymbol method
        pass

class MetricSystemUnit:

    pass
class units_Meter(LengthUnit, MetricSystemUnit):

    def __init__(self):
        
    def getSymbol(self):
        # TODO: Implement getSymbol method
        pass

    def toCm(self, value: float):
        # TODO: Implement toCm method
        pass

class units_Millimeter(LengthUnit, MetricSystemUnit):

    def __init__(self):
        
    def getSymbol(self):
        # TODO: Implement getSymbol method
        pass

    def toCm(self, value: float):
        # TODO: Implement toCm method
        pass

class units_Centimeter(LengthUnit, MetricSystemUnit):

    def __init__(self):
        
    def toCm(self, value: float):
        # TODO: Implement toCm method
        pass

    def getSymbol(self):
        # TODO: Implement getSymbol method
        pass

class Unit:

    pass
class units_AngleUnit(Unit):

    def __init__(self):
        
    def toRad(self, value: float):
        # TODO: Implement toRad method
        pass

class units_MetricSystemUnit(Unit):

    pass
class units_ImperialSystemUnit(Unit):

    pass
class units_LengthUnit(Unit):

    def __init__(self):
        
    def toCm(self, value: float):
        # TODO: Implement toCm method
        pass

class units_Unit(ABC):

    def __init__(self, units_Unit: "units_Quantity" = None):
        self.units_Unit = units_Unit
        
    @property
    def units_Unit(self):
        return self.__units_Unit

    @units_Unit.setter
    def units_Unit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_units_Unit__units_Unit", None)
        self.__units_Unit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "units_Quantity"):
                opp_val = getattr(old_value, "units_Quantity", None)
                if opp_val == self:
                    setattr(old_value, "units_Quantity", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "units_Quantity"):
                opp_val = getattr(value, "units_Quantity", None)
                setattr(value, "units_Quantity", self)

    def getSymbol(self):
        # TODO: Implement getSymbol method
        pass
