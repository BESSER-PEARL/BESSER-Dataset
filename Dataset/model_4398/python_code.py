from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class BooleanOperator(Enum):
    eq = "eq"
    neq = "neq"
class NumericOperator(Enum):
    lt = "lt"
    eq = "eq"
    neq = "neq"
    gt = "gt"
    leq = "leq"
    geq = "geq"
class StringOperator(Enum):
    eq = "eq"
    neq = "neq"


############################################
# Definition of Classes
############################################

class AngleOperation:

    pass
class QuantityScalarOperation:

    pass
class raspirover_AngleScalarMultiply(QuantityScalarOperation, AngleOperation):

    pass
class raspirover_AngleScalarDivide(QuantityScalarOperation, AngleOperation):

    pass
class QuantityHomogenousOperation:

    pass
class raspirover_AngleGreater(QuantityHomogenousOperation, AngleOperation):

    pass
class raspirover_AngleAdd(QuantityHomogenousOperation, AngleOperation):

    pass
class raspirover_AngleSmaller(QuantityHomogenousOperation, AngleOperation):

    pass
class raspirover_AngleSubtract(QuantityHomogenousOperation, AngleOperation):

    pass
class raspirover_AngleEquals(QuantityHomogenousOperation, AngleOperation):

    pass
class raspirover_AngleDistinct(QuantityHomogenousOperation, AngleOperation):

    pass
class LengthOperation:

    pass
class raspirover_LengthSmaller(LengthOperation, QuantityHomogenousOperation):

    pass
class raspirover_LengthDistinct(LengthOperation, QuantityHomogenousOperation):

    pass
class raspirover_LengthSubtract(LengthOperation, QuantityHomogenousOperation):

    pass
class raspirover_LengthEquals(LengthOperation, QuantityHomogenousOperation):

    pass
class raspirover_LengthGreater(LengthOperation, QuantityHomogenousOperation):

    pass
class raspirover_LengthScalarDivide(LengthOperation, QuantityScalarOperation):

    pass
class raspirover_LengthScalarMultiply(LengthOperation, QuantityScalarOperation):

    pass
class raspirover_LengthAdd(LengthOperation, QuantityHomogenousOperation):

    pass
class QuantityOperation:

    pass
class raspirover_QuantityHomogenousOperation(QuantityOperation):

    pass
class raspirover_QuantityArithmeticOperation(QuantityOperation):

    pass
class raspirover_QuantityScalarOperation(QuantityOperation):

    def __init__(self, rhs: float, raspirover_QuantityScalarOperation: "raspirover_Quantity" = None):
        self.rhs = rhs
        self.raspirover_QuantityScalarOperation = raspirover_QuantityScalarOperation
        
    @property
    def rhs(self) -> float:
        return self.__rhs

    @rhs.setter
    def rhs(self, rhs: float):
        self.__rhs = rhs

    @property
    def raspirover_QuantityScalarOperation(self):
        return self.__raspirover_QuantityScalarOperation

    @raspirover_QuantityScalarOperation.setter
    def raspirover_QuantityScalarOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_QuantityScalarOperation__raspirover_QuantityScalarOperation", None)
        self.__raspirover_QuantityScalarOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "raspirover_Quantity76"):
                opp_val = getattr(old_value, "raspirover_Quantity76", None)
                if opp_val == self:
                    setattr(old_value, "raspirover_Quantity76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raspirover_Quantity76"):
                opp_val = getattr(value, "raspirover_Quantity76", None)
                setattr(value, "raspirover_Quantity76", self)

class raspirover_AngleOperation(QuantityOperation):

    pass
class raspirover_QuantityComparisonOperation(QuantityOperation):

    pass
class raspirover_LengthOperation(QuantityOperation):

    pass
class raspirover_QuantityOperation(ABC):

    pass
class Quantity:

    pass
class raspirover_Angle(Quantity):

    def __init__(self):
        
    def toRad(self):
        # TODO: Implement toRad method
        pass

    def print(self):
        # TODO: Implement print method
        pass

class raspirover_Length(Quantity):

    def __init__(self):
        
    def toCm(self):
        # TODO: Implement toCm method
        pass

    def print(self):
        # TODO: Implement print method
        pass

class AngleUnit:

    pass
class raspirover_Gradian(AngleUnit):

    def __init__(self):
        
    def toRad(self, value: float):
        # TODO: Implement toRad method
        pass

    def getSymbol(self):
        # TODO: Implement getSymbol method
        pass

class raspirover_Degree(AngleUnit):

    def __init__(self):
        
    def getSymbol(self):
        # TODO: Implement getSymbol method
        pass

    def toRad(self, value: float):
        # TODO: Implement toRad method
        pass

class raspirover_Turn(AngleUnit):

    def __init__(self):
        
    def getSymbol(self):
        # TODO: Implement getSymbol method
        pass

    def toRad(self, value: float):
        # TODO: Implement toRad method
        pass

class raspirover_Radian(AngleUnit):

    def __init__(self):
        
    def toRad(self, value: float):
        # TODO: Implement toRad method
        pass

    def getSymbol(self):
        # TODO: Implement getSymbol method
        pass

class ImperialSystemUnit:

    pass
class LengthUnit:

    pass
class raspirover_Foot(LengthUnit, ImperialSystemUnit):

    def __init__(self):
        
    def getSymbol(self):
        # TODO: Implement getSymbol method
        pass

    def toCm(self, value: float):
        # TODO: Implement toCm method
        pass

class raspirover_Yard(LengthUnit, ImperialSystemUnit):

    def __init__(self):
        
    def toCm(self, value: float):
        # TODO: Implement toCm method
        pass

    def getSymbol(self):
        # TODO: Implement getSymbol method
        pass

class raspirover_Inch(LengthUnit, ImperialSystemUnit):

    def __init__(self):
        
    def getSymbol(self):
        # TODO: Implement getSymbol method
        pass

    def toCm(self, value: float):
        # TODO: Implement toCm method
        pass

class MetricSystemUnit:

    pass
class raspirover_Meter(LengthUnit, MetricSystemUnit):

    def __init__(self):
        
    def toCm(self, value: float):
        # TODO: Implement toCm method
        pass

    def getSymbol(self):
        # TODO: Implement getSymbol method
        pass

class raspirover_Millimeter(LengthUnit, MetricSystemUnit):

    def __init__(self):
        
    def toCm(self, value: float):
        # TODO: Implement toCm method
        pass

    def getSymbol(self):
        # TODO: Implement getSymbol method
        pass

class raspirover_Centimeter(LengthUnit, MetricSystemUnit):

    def __init__(self):
        
    def getSymbol(self):
        # TODO: Implement getSymbol method
        pass

    def toCm(self, value: float):
        # TODO: Implement toCm method
        pass

class Unit:

    pass
class raspirover_MetricSystemUnit(Unit):

    pass
class raspirover_AngleUnit(Unit):

    def __init__(self):
        
    def toRad(self, value: float):
        # TODO: Implement toRad method
        pass

class raspirover_ImperialSystemUnit(Unit):

    pass
class raspirover_LengthUnit(Unit):

    def __init__(self):
        
    def toCm(self, value: float):
        # TODO: Implement toCm method
        pass

class raspirover_Unit(ABC):

    def __init__(self, raspirover_Unit: "raspirover_Quantity" = None):
        self.raspirover_Unit = raspirover_Unit
        
    @property
    def raspirover_Unit(self):
        return self.__raspirover_Unit

    @raspirover_Unit.setter
    def raspirover_Unit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_Unit__raspirover_Unit", None)
        self.__raspirover_Unit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "raspirover_Quantity69"):
                opp_val = getattr(old_value, "raspirover_Quantity69", None)
                if opp_val == self:
                    setattr(old_value, "raspirover_Quantity69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raspirover_Quantity69"):
                opp_val = getattr(value, "raspirover_Quantity69", None)
                setattr(value, "raspirover_Quantity69", self)

    def getSymbol(self):
        # TODO: Implement getSymbol method
        pass

class Action:

    pass
class raspirover_ForwardMinAction(Action):

    def __init__(self, raspirover_ForwardMinAction: "raspirover_NumberValue" = None):
        self.raspirover_ForwardMinAction = raspirover_ForwardMinAction
        
    @property
    def raspirover_ForwardMinAction(self):
        return self.__raspirover_ForwardMinAction

    @raspirover_ForwardMinAction.setter
    def raspirover_ForwardMinAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_ForwardMinAction__raspirover_ForwardMinAction", None)
        self.__raspirover_ForwardMinAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "raspirover_NumberValue63"):
                opp_val = getattr(old_value, "raspirover_NumberValue63", None)
                if opp_val == self:
                    setattr(old_value, "raspirover_NumberValue63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raspirover_NumberValue63"):
                opp_val = getattr(value, "raspirover_NumberValue63", None)
                setattr(value, "raspirover_NumberValue63", self)

    def eval(self):
        # TODO: Implement eval method
        pass

class raspirover_SendAction(Action):

    def __init__(self, message: str):
        self.message = message
        
    @property
    def message(self) -> str:
        return self.__message

    @message.setter
    def message(self, message: str):
        self.__message = message

    def eval(self):
        # TODO: Implement eval method
        pass

class raspirover_TurnAction(Action):

    def __init__(self):
        
    def eval(self):
        # TODO: Implement eval method
        pass

class raspirover_StopAction(Action):

    def __init__(self):
        
    def eval(self):
        # TODO: Implement eval method
        pass

class raspirover_LogAction(Action):

    def __init__(self, message: str):
        self.message = message
        
    @property
    def message(self) -> str:
        return self.__message

    @message.setter
    def message(self, message: str):
        self.__message = message

    def eval(self):
        # TODO: Implement eval method
        pass

class raspirover_BackwardMinAction(Action):

    def __init__(self, raspirover_BackwardMinAction: "raspirover_NumberValue" = None):
        self.raspirover_BackwardMinAction = raspirover_BackwardMinAction
        
    @property
    def raspirover_BackwardMinAction(self):
        return self.__raspirover_BackwardMinAction

    @raspirover_BackwardMinAction.setter
    def raspirover_BackwardMinAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_BackwardMinAction__raspirover_BackwardMinAction", None)
        self.__raspirover_BackwardMinAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "raspirover_NumberValue65"):
                opp_val = getattr(old_value, "raspirover_NumberValue65", None)
                if opp_val == self:
                    setattr(old_value, "raspirover_NumberValue65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raspirover_NumberValue65"):
                opp_val = getattr(value, "raspirover_NumberValue65", None)
                setattr(value, "raspirover_NumberValue65", self)

    def eval(self):
        # TODO: Implement eval method
        pass

class raspirover_TurnDegAction(Action):

    def __init__(self, raspirover_TurnDegAction: "raspirover_NumberValue" = None):
        self.raspirover_TurnDegAction = raspirover_TurnDegAction
        
    @property
    def raspirover_TurnDegAction(self):
        return self.__raspirover_TurnDegAction

    @raspirover_TurnDegAction.setter
    def raspirover_TurnDegAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_TurnDegAction__raspirover_TurnDegAction", None)
        self.__raspirover_TurnDegAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "raspirover_NumberValue67"):
                opp_val = getattr(old_value, "raspirover_NumberValue67", None)
                if opp_val == self:
                    setattr(old_value, "raspirover_NumberValue67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raspirover_NumberValue67"):
                opp_val = getattr(value, "raspirover_NumberValue67", None)
                setattr(value, "raspirover_NumberValue67", self)

    def eval(self):
        # TODO: Implement eval method
        pass

class raspirover_BackwardAction(Action):

    def __init__(self):
        
    def eval(self):
        # TODO: Implement eval method
        pass

class raspirover_ForwardAction(Action):

    def __init__(self):
        
    def eval(self):
        # TODO: Implement eval method
        pass

class raspirover_Quantity:

    def __init__(self, value: str, raspirover_Quantity: "raspirover_NumberValue" = None, raspirover_Quantity69: "raspirover_Unit" = None, raspirover_Quantity71: "raspirover_QuantityHomogenousOperation" = None, raspirover_Quantity74: "raspirover_QuantityHomogenousOperation" = None, raspirover_Quantity76: "raspirover_QuantityScalarOperation" = None):
        self.value = value
        self.raspirover_Quantity = raspirover_Quantity
        self.raspirover_Quantity69 = raspirover_Quantity69
        self.raspirover_Quantity71 = raspirover_Quantity71
        self.raspirover_Quantity74 = raspirover_Quantity74
        self.raspirover_Quantity76 = raspirover_Quantity76
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def raspirover_Quantity69(self):
        return self.__raspirover_Quantity69

    @raspirover_Quantity69.setter
    def raspirover_Quantity69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_Quantity__raspirover_Quantity69", None)
        self.__raspirover_Quantity69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "raspirover_Unit"):
                opp_val = getattr(old_value, "raspirover_Unit", None)
                if opp_val == self:
                    setattr(old_value, "raspirover_Unit", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raspirover_Unit"):
                opp_val = getattr(value, "raspirover_Unit", None)
                setattr(value, "raspirover_Unit", self)

    @property
    def raspirover_Quantity71(self):
        return self.__raspirover_Quantity71

    @raspirover_Quantity71.setter
    def raspirover_Quantity71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_Quantity__raspirover_Quantity71", None)
        self.__raspirover_Quantity71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "raspirover_QuantityHomogenousOperation"):
                opp_val = getattr(old_value, "raspirover_QuantityHomogenousOperation", None)
                if opp_val == self:
                    setattr(old_value, "raspirover_QuantityHomogenousOperation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raspirover_QuantityHomogenousOperation"):
                opp_val = getattr(value, "raspirover_QuantityHomogenousOperation", None)
                setattr(value, "raspirover_QuantityHomogenousOperation", self)

    @property
    def raspirover_Quantity(self):
        return self.__raspirover_Quantity

    @raspirover_Quantity.setter
    def raspirover_Quantity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_Quantity__raspirover_Quantity", None)
        self.__raspirover_Quantity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "raspirover_NumberValue60"):
                opp_val = getattr(old_value, "raspirover_NumberValue60", None)
                if opp_val == self:
                    setattr(old_value, "raspirover_NumberValue60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raspirover_NumberValue60"):
                opp_val = getattr(value, "raspirover_NumberValue60", None)
                setattr(value, "raspirover_NumberValue60", self)

    @property
    def raspirover_Quantity74(self):
        return self.__raspirover_Quantity74

    @raspirover_Quantity74.setter
    def raspirover_Quantity74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_Quantity__raspirover_Quantity74", None)
        self.__raspirover_Quantity74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "raspirover_QuantityHomogenousOperation73"):
                opp_val = getattr(old_value, "raspirover_QuantityHomogenousOperation73", None)
                if opp_val == self:
                    setattr(old_value, "raspirover_QuantityHomogenousOperation73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raspirover_QuantityHomogenousOperation73"):
                opp_val = getattr(value, "raspirover_QuantityHomogenousOperation73", None)
                setattr(value, "raspirover_QuantityHomogenousOperation73", self)

    @property
    def raspirover_Quantity76(self):
        return self.__raspirover_Quantity76

    @raspirover_Quantity76.setter
    def raspirover_Quantity76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_Quantity__raspirover_Quantity76", None)
        self.__raspirover_Quantity76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "raspirover_QuantityScalarOperation"):
                opp_val = getattr(old_value, "raspirover_QuantityScalarOperation", None)
                if opp_val == self:
                    setattr(old_value, "raspirover_QuantityScalarOperation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raspirover_QuantityScalarOperation"):
                opp_val = getattr(value, "raspirover_QuantityScalarOperation", None)
                setattr(value, "raspirover_QuantityScalarOperation", self)

    def getNormalized(self):
        # TODO: Implement getNormalized method
        pass

    def print(self):
        # TODO: Implement print method
        pass

class RoverValue:

    pass
class raspirover_BooleanValue(RoverValue):

    def __init__(self, bValue: bool, raspirover_BooleanValue: "raspirover_BooleanExpression" = None, raspirover_BooleanValue58: "raspirover_BooleanExpression" = None):
        self.bValue = bValue
        self.raspirover_BooleanValue = raspirover_BooleanValue
        self.raspirover_BooleanValue58 = raspirover_BooleanValue58
        
    @property
    def bValue(self) -> bool:
        return self.__bValue

    @bValue.setter
    def bValue(self, bValue: bool):
        self.__bValue = bValue

    @property
    def raspirover_BooleanValue58(self):
        return self.__raspirover_BooleanValue58

    @raspirover_BooleanValue58.setter
    def raspirover_BooleanValue58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_BooleanValue__raspirover_BooleanValue58", None)
        self.__raspirover_BooleanValue58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "raspirover_BooleanExpression57"):
                opp_val = getattr(old_value, "raspirover_BooleanExpression57", None)
                if opp_val == self:
                    setattr(old_value, "raspirover_BooleanExpression57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raspirover_BooleanExpression57"):
                opp_val = getattr(value, "raspirover_BooleanExpression57", None)
                setattr(value, "raspirover_BooleanExpression57", self)

    @property
    def raspirover_BooleanValue(self):
        return self.__raspirover_BooleanValue

    @raspirover_BooleanValue.setter
    def raspirover_BooleanValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_BooleanValue__raspirover_BooleanValue", None)
        self.__raspirover_BooleanValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "raspirover_BooleanExpression"):
                opp_val = getattr(old_value, "raspirover_BooleanExpression", None)
                if opp_val == self:
                    setattr(old_value, "raspirover_BooleanExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raspirover_BooleanExpression"):
                opp_val = getattr(value, "raspirover_BooleanExpression", None)
                setattr(value, "raspirover_BooleanExpression", self)

    def getBooleanValue(self):
        # TODO: Implement getBooleanValue method
        pass

class raspirover_StringValue(RoverValue):

    def __init__(self, sValue: bool, raspirover_StringValue: "raspirover_StringExpression" = None, raspirover_StringValue54: "raspirover_StringExpression" = None):
        self.sValue = sValue
        self.raspirover_StringValue = raspirover_StringValue
        self.raspirover_StringValue54 = raspirover_StringValue54
        
    @property
    def sValue(self) -> bool:
        return self.__sValue

    @sValue.setter
    def sValue(self, sValue: bool):
        self.__sValue = sValue

    @property
    def raspirover_StringValue54(self):
        return self.__raspirover_StringValue54

    @raspirover_StringValue54.setter
    def raspirover_StringValue54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_StringValue__raspirover_StringValue54", None)
        self.__raspirover_StringValue54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "raspirover_StringExpression53"):
                opp_val = getattr(old_value, "raspirover_StringExpression53", None)
                if opp_val == self:
                    setattr(old_value, "raspirover_StringExpression53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raspirover_StringExpression53"):
                opp_val = getattr(value, "raspirover_StringExpression53", None)
                setattr(value, "raspirover_StringExpression53", self)

    @property
    def raspirover_StringValue(self):
        return self.__raspirover_StringValue

    @raspirover_StringValue.setter
    def raspirover_StringValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_StringValue__raspirover_StringValue", None)
        self.__raspirover_StringValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "raspirover_StringExpression"):
                opp_val = getattr(old_value, "raspirover_StringExpression", None)
                if opp_val == self:
                    setattr(old_value, "raspirover_StringExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raspirover_StringExpression"):
                opp_val = getattr(value, "raspirover_StringExpression", None)
                setattr(value, "raspirover_StringExpression", self)

    def getStringValue(self):
        # TODO: Implement getStringValue method
        pass

class raspirover_NumberValue(RoverValue):

    def __init__(self, nValue: str, raspirover_NumberValue: "raspirover_NumericExpression" = None, raspirover_NumberValue50: "raspirover_NumericExpression" = None, raspirover_NumberValue60: "raspirover_Quantity" = None, raspirover_NumberValue63: "raspirover_ForwardMinAction" = None, raspirover_NumberValue65: "raspirover_BackwardMinAction" = None, raspirover_NumberValue67: "raspirover_TurnDegAction" = None):
        self.nValue = nValue
        self.raspirover_NumberValue = raspirover_NumberValue
        self.raspirover_NumberValue50 = raspirover_NumberValue50
        self.raspirover_NumberValue60 = raspirover_NumberValue60
        self.raspirover_NumberValue63 = raspirover_NumberValue63
        self.raspirover_NumberValue65 = raspirover_NumberValue65
        self.raspirover_NumberValue67 = raspirover_NumberValue67
        
    @property
    def nValue(self) -> str:
        return self.__nValue

    @nValue.setter
    def nValue(self, nValue: str):
        self.__nValue = nValue

    @property
    def raspirover_NumberValue67(self):
        return self.__raspirover_NumberValue67

    @raspirover_NumberValue67.setter
    def raspirover_NumberValue67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_NumberValue__raspirover_NumberValue67", None)
        self.__raspirover_NumberValue67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "raspirover_TurnDegAction"):
                opp_val = getattr(old_value, "raspirover_TurnDegAction", None)
                if opp_val == self:
                    setattr(old_value, "raspirover_TurnDegAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raspirover_TurnDegAction"):
                opp_val = getattr(value, "raspirover_TurnDegAction", None)
                setattr(value, "raspirover_TurnDegAction", self)

    @property
    def raspirover_NumberValue63(self):
        return self.__raspirover_NumberValue63

    @raspirover_NumberValue63.setter
    def raspirover_NumberValue63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_NumberValue__raspirover_NumberValue63", None)
        self.__raspirover_NumberValue63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "raspirover_ForwardMinAction"):
                opp_val = getattr(old_value, "raspirover_ForwardMinAction", None)
                if opp_val == self:
                    setattr(old_value, "raspirover_ForwardMinAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raspirover_ForwardMinAction"):
                opp_val = getattr(value, "raspirover_ForwardMinAction", None)
                setattr(value, "raspirover_ForwardMinAction", self)

    @property
    def raspirover_NumberValue50(self):
        return self.__raspirover_NumberValue50

    @raspirover_NumberValue50.setter
    def raspirover_NumberValue50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_NumberValue__raspirover_NumberValue50", None)
        self.__raspirover_NumberValue50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "raspirover_NumericExpression49"):
                opp_val = getattr(old_value, "raspirover_NumericExpression49", None)
                if opp_val == self:
                    setattr(old_value, "raspirover_NumericExpression49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raspirover_NumericExpression49"):
                opp_val = getattr(value, "raspirover_NumericExpression49", None)
                setattr(value, "raspirover_NumericExpression49", self)

    @property
    def raspirover_NumberValue65(self):
        return self.__raspirover_NumberValue65

    @raspirover_NumberValue65.setter
    def raspirover_NumberValue65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_NumberValue__raspirover_NumberValue65", None)
        self.__raspirover_NumberValue65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "raspirover_BackwardMinAction"):
                opp_val = getattr(old_value, "raspirover_BackwardMinAction", None)
                if opp_val == self:
                    setattr(old_value, "raspirover_BackwardMinAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raspirover_BackwardMinAction"):
                opp_val = getattr(value, "raspirover_BackwardMinAction", None)
                setattr(value, "raspirover_BackwardMinAction", self)

    @property
    def raspirover_NumberValue60(self):
        return self.__raspirover_NumberValue60

    @raspirover_NumberValue60.setter
    def raspirover_NumberValue60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_NumberValue__raspirover_NumberValue60", None)
        self.__raspirover_NumberValue60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "raspirover_Quantity"):
                opp_val = getattr(old_value, "raspirover_Quantity", None)
                if opp_val == self:
                    setattr(old_value, "raspirover_Quantity", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raspirover_Quantity"):
                opp_val = getattr(value, "raspirover_Quantity", None)
                setattr(value, "raspirover_Quantity", self)

    @property
    def raspirover_NumberValue(self):
        return self.__raspirover_NumberValue

    @raspirover_NumberValue.setter
    def raspirover_NumberValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_NumberValue__raspirover_NumberValue", None)
        self.__raspirover_NumberValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "raspirover_NumericExpression"):
                opp_val = getattr(old_value, "raspirover_NumericExpression", None)
                if opp_val == self:
                    setattr(old_value, "raspirover_NumericExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raspirover_NumericExpression"):
                opp_val = getattr(value, "raspirover_NumericExpression", None)
                setattr(value, "raspirover_NumericExpression", self)

    def getIntValue(self):
        # TODO: Implement getIntValue method
        pass

    def print(self):
        # TODO: Implement print method
        pass

class RoverExpression:

    pass
class raspirover_BooleanExpression(RoverExpression):

    def __init__(self, op: str, raspirover_BooleanExpression: "raspirover_BooleanValue" = None, raspirover_BooleanExpression57: "raspirover_BooleanValue" = None):
        self.op = op
        self.raspirover_BooleanExpression = raspirover_BooleanExpression
        self.raspirover_BooleanExpression57 = raspirover_BooleanExpression57
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def raspirover_BooleanExpression57(self):
        return self.__raspirover_BooleanExpression57

    @raspirover_BooleanExpression57.setter
    def raspirover_BooleanExpression57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_BooleanExpression__raspirover_BooleanExpression57", None)
        self.__raspirover_BooleanExpression57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "raspirover_BooleanValue58"):
                opp_val = getattr(old_value, "raspirover_BooleanValue58", None)
                if opp_val == self:
                    setattr(old_value, "raspirover_BooleanValue58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raspirover_BooleanValue58"):
                opp_val = getattr(value, "raspirover_BooleanValue58", None)
                setattr(value, "raspirover_BooleanValue58", self)

    @property
    def raspirover_BooleanExpression(self):
        return self.__raspirover_BooleanExpression

    @raspirover_BooleanExpression.setter
    def raspirover_BooleanExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_BooleanExpression__raspirover_BooleanExpression", None)
        self.__raspirover_BooleanExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "raspirover_BooleanValue"):
                opp_val = getattr(old_value, "raspirover_BooleanValue", None)
                if opp_val == self:
                    setattr(old_value, "raspirover_BooleanValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raspirover_BooleanValue"):
                opp_val = getattr(value, "raspirover_BooleanValue", None)
                setattr(value, "raspirover_BooleanValue", self)

    def eval(self):
        # TODO: Implement eval method
        pass

class raspirover_StringExpression(RoverExpression):

    def __init__(self, op: bool, raspirover_StringExpression: "raspirover_StringValue" = None, raspirover_StringExpression53: "raspirover_StringValue" = None):
        self.op = op
        self.raspirover_StringExpression = raspirover_StringExpression
        self.raspirover_StringExpression53 = raspirover_StringExpression53
        
    @property
    def op(self) -> bool:
        return self.__op

    @op.setter
    def op(self, op: bool):
        self.__op = op

    @property
    def raspirover_StringExpression(self):
        return self.__raspirover_StringExpression

    @raspirover_StringExpression.setter
    def raspirover_StringExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_StringExpression__raspirover_StringExpression", None)
        self.__raspirover_StringExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "raspirover_StringValue"):
                opp_val = getattr(old_value, "raspirover_StringValue", None)
                if opp_val == self:
                    setattr(old_value, "raspirover_StringValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raspirover_StringValue"):
                opp_val = getattr(value, "raspirover_StringValue", None)
                setattr(value, "raspirover_StringValue", self)

    @property
    def raspirover_StringExpression53(self):
        return self.__raspirover_StringExpression53

    @raspirover_StringExpression53.setter
    def raspirover_StringExpression53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_StringExpression__raspirover_StringExpression53", None)
        self.__raspirover_StringExpression53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "raspirover_StringValue54"):
                opp_val = getattr(old_value, "raspirover_StringValue54", None)
                if opp_val == self:
                    setattr(old_value, "raspirover_StringValue54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raspirover_StringValue54"):
                opp_val = getattr(value, "raspirover_StringValue54", None)
                setattr(value, "raspirover_StringValue54", self)

    def eval(self):
        # TODO: Implement eval method
        pass

class raspirover_NumericExpression(RoverExpression):

    def __init__(self, op: bool, raspirover_NumericExpression: "raspirover_NumberValue" = None, raspirover_NumericExpression49: "raspirover_NumberValue" = None):
        self.op = op
        self.raspirover_NumericExpression = raspirover_NumericExpression
        self.raspirover_NumericExpression49 = raspirover_NumericExpression49
        
    @property
    def op(self) -> bool:
        return self.__op

    @op.setter
    def op(self, op: bool):
        self.__op = op

    @property
    def raspirover_NumericExpression(self):
        return self.__raspirover_NumericExpression

    @raspirover_NumericExpression.setter
    def raspirover_NumericExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_NumericExpression__raspirover_NumericExpression", None)
        self.__raspirover_NumericExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "raspirover_NumberValue"):
                opp_val = getattr(old_value, "raspirover_NumberValue", None)
                if opp_val == self:
                    setattr(old_value, "raspirover_NumberValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raspirover_NumberValue"):
                opp_val = getattr(value, "raspirover_NumberValue", None)
                setattr(value, "raspirover_NumberValue", self)

    @property
    def raspirover_NumericExpression49(self):
        return self.__raspirover_NumericExpression49

    @raspirover_NumericExpression49.setter
    def raspirover_NumericExpression49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_NumericExpression__raspirover_NumericExpression49", None)
        self.__raspirover_NumericExpression49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "raspirover_NumberValue50"):
                opp_val = getattr(old_value, "raspirover_NumberValue50", None)
                if opp_val == self:
                    setattr(old_value, "raspirover_NumberValue50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raspirover_NumberValue50"):
                opp_val = getattr(value, "raspirover_NumberValue50", None)
                setattr(value, "raspirover_NumberValue50", self)

    def eval(self):
        # TODO: Implement eval method
        pass

class BooleanValue:

    pass
class StringValue:

    pass
class NumberValue:

    pass
class Query:

    pass
class raspirover_MessageQuery(StringValue, Query):

    def __init__(self):
        
    def getStringValue(self):
        # TODO: Implement getStringValue method
        pass

class raspirover_ObstacleQuery(BooleanValue, Query):

    def __init__(self, front: bool):
        self.front = front
        
    @property
    def front(self) -> bool:
        return self.__front

    @front.setter
    def front(self, front: bool):
        self.__front = front

    def getBooleanValue(self):
        # TODO: Implement getBooleanValue method
        pass

class raspirover_TemperatureQuery(NumberValue, Query):

    def __init__(self):
        
    def getIntValue(self):
        # TODO: Implement getIntValue method
        pass

class raspirover_Query(ABC):

    pass
class raspirover_RoverExpression(ABC):

    def __init__(self, raspirover_RoverExpression: "raspirover_Conditional" = None, raspirover_RoverExpression40: "raspirover_Loop" = None):
        self.raspirover_RoverExpression = raspirover_RoverExpression
        self.raspirover_RoverExpression40 = raspirover_RoverExpression40
        
    @property
    def raspirover_RoverExpression40(self):
        return self.__raspirover_RoverExpression40

    @raspirover_RoverExpression40.setter
    def raspirover_RoverExpression40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_RoverExpression__raspirover_RoverExpression40", None)
        self.__raspirover_RoverExpression40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "raspirover_Loop"):
                opp_val = getattr(old_value, "raspirover_Loop", None)
                if opp_val == self:
                    setattr(old_value, "raspirover_Loop", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raspirover_Loop"):
                opp_val = getattr(value, "raspirover_Loop", None)
                setattr(value, "raspirover_Loop", self)

    @property
    def raspirover_RoverExpression(self):
        return self.__raspirover_RoverExpression

    @raspirover_RoverExpression.setter
    def raspirover_RoverExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_RoverExpression__raspirover_RoverExpression", None)
        self.__raspirover_RoverExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "raspirover_Conditional"):
                opp_val = getattr(old_value, "raspirover_Conditional", None)
                if opp_val == self:
                    setattr(old_value, "raspirover_Conditional", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raspirover_Conditional"):
                opp_val = getattr(value, "raspirover_Conditional", None)
                setattr(value, "raspirover_Conditional", self)

    def eval(self):
        # TODO: Implement eval method
        pass

class raspirover_RoverValue:

    pass
class Statement:

    pass
class raspirover_VarRef(Statement, StringValue, BooleanValue, NumberValue):

    def __init__(self, name: float):
        self.name = name
        
    @property
    def name(self) -> float:
        return self.__name

    @name.setter
    def name(self, name: float):
        self.__name = name

    def getBooleanValue(self):
        # TODO: Implement getBooleanValue method
        pass

    def getStringValue(self):
        # TODO: Implement getStringValue method
        pass

    def getIntValue(self):
        # TODO: Implement getIntValue method
        pass

    def eval(self):
        # TODO: Implement eval method
        pass

class raspirover_Loop(Statement):

    def __init__(self, raspirover_Loop: "raspirover_RoverExpression" = None, raspirover_Loop42: "raspirover_RclBlock" = None):
        self.raspirover_Loop = raspirover_Loop
        self.raspirover_Loop42 = raspirover_Loop42
        
    @property
    def raspirover_Loop42(self):
        return self.__raspirover_Loop42

    @raspirover_Loop42.setter
    def raspirover_Loop42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_Loop__raspirover_Loop42", None)
        self.__raspirover_Loop42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "raspirover_RclBlock43"):
                opp_val = getattr(old_value, "raspirover_RclBlock43", None)
                if opp_val == self:
                    setattr(old_value, "raspirover_RclBlock43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raspirover_RclBlock43"):
                opp_val = getattr(value, "raspirover_RclBlock43", None)
                setattr(value, "raspirover_RclBlock43", self)

    @property
    def raspirover_Loop(self):
        return self.__raspirover_Loop

    @raspirover_Loop.setter
    def raspirover_Loop(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_Loop__raspirover_Loop", None)
        self.__raspirover_Loop = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "raspirover_RoverExpression40"):
                opp_val = getattr(old_value, "raspirover_RoverExpression40", None)
                if opp_val == self:
                    setattr(old_value, "raspirover_RoverExpression40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raspirover_RoverExpression40"):
                opp_val = getattr(value, "raspirover_RoverExpression40", None)
                setattr(value, "raspirover_RoverExpression40", self)

    def eval(self):
        # TODO: Implement eval method
        pass

class raspirover_Action(Statement):

    pass
class raspirover_Conditional(Statement):

    def __init__(self, raspirover_Conditional: "raspirover_RoverExpression" = None, raspirover_Conditional34: "raspirover_RclBlock" = None, raspirover_Conditional37: "raspirover_RclBlock" = None):
        self.raspirover_Conditional = raspirover_Conditional
        self.raspirover_Conditional34 = raspirover_Conditional34
        self.raspirover_Conditional37 = raspirover_Conditional37
        
    @property
    def raspirover_Conditional34(self):
        return self.__raspirover_Conditional34

    @raspirover_Conditional34.setter
    def raspirover_Conditional34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_Conditional__raspirover_Conditional34", None)
        self.__raspirover_Conditional34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "raspirover_RclBlock35"):
                opp_val = getattr(old_value, "raspirover_RclBlock35", None)
                if opp_val == self:
                    setattr(old_value, "raspirover_RclBlock35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raspirover_RclBlock35"):
                opp_val = getattr(value, "raspirover_RclBlock35", None)
                setattr(value, "raspirover_RclBlock35", self)

    @property
    def raspirover_Conditional(self):
        return self.__raspirover_Conditional

    @raspirover_Conditional.setter
    def raspirover_Conditional(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_Conditional__raspirover_Conditional", None)
        self.__raspirover_Conditional = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "raspirover_RoverExpression"):
                opp_val = getattr(old_value, "raspirover_RoverExpression", None)
                if opp_val == self:
                    setattr(old_value, "raspirover_RoverExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raspirover_RoverExpression"):
                opp_val = getattr(value, "raspirover_RoverExpression", None)
                setattr(value, "raspirover_RoverExpression", self)

    @property
    def raspirover_Conditional37(self):
        return self.__raspirover_Conditional37

    @raspirover_Conditional37.setter
    def raspirover_Conditional37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_Conditional__raspirover_Conditional37", None)
        self.__raspirover_Conditional37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "raspirover_RclBlock38"):
                opp_val = getattr(old_value, "raspirover_RclBlock38", None)
                if opp_val == self:
                    setattr(old_value, "raspirover_RclBlock38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raspirover_RclBlock38"):
                opp_val = getattr(value, "raspirover_RclBlock38", None)
                setattr(value, "raspirover_RclBlock38", self)

    def eval(self):
        # TODO: Implement eval method
        pass

class raspirover_VarAssignment(Statement):

    def __init__(self, name: bool, raspirover_VarAssignment: "raspirover_RoverValue" = None):
        self.name = name
        self.raspirover_VarAssignment = raspirover_VarAssignment
        
    @property
    def name(self) -> bool:
        return self.__name

    @name.setter
    def name(self, name: bool):
        self.__name = name

    @property
    def raspirover_VarAssignment(self):
        return self.__raspirover_VarAssignment

    @raspirover_VarAssignment.setter
    def raspirover_VarAssignment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_VarAssignment__raspirover_VarAssignment", None)
        self.__raspirover_VarAssignment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "raspirover_RoverValue"):
                opp_val = getattr(old_value, "raspirover_RoverValue", None)
                if opp_val == self:
                    setattr(old_value, "raspirover_RoverValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raspirover_RoverValue"):
                opp_val = getattr(value, "raspirover_RoverValue", None)
                setattr(value, "raspirover_RoverValue", self)

    def eval(self):
        # TODO: Implement eval method
        pass

class raspirover_Statement(ABC):

    def __init__(self, 29: "raspirover_RclBlock" = None, 46: "raspirover_RclBlock" = None):
        self.29 = 29
        self.46 = 46
        
    @property
    def 29(self):
        return self.__29

    @29.setter
    def 29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_Statement__29", None)
        self.__29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "30"):
                opp_val = getattr(old_value, "30", None)
                if opp_val == self:
                    setattr(old_value, "30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "30"):
                opp_val = getattr(value, "30", None)
                setattr(value, "30", self)

    @property
    def 46(self):
        return self.__46

    @46.setter
    def 46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_Statement__46", None)
        self.__46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "45"):
                opp_val = getattr(old_value, "45", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "45"):
                opp_val = getattr(value, "45", None)
                if opp_val is None:
                    setattr(value, "45", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def eval(self):
        # TODO: Implement eval method
        pass

    def getProgram(self) -> str:
        # TODO: Implement getProgram method
        pass

class raspirover_HumidityQuery(NumberValue, Query):

    def __init__(self):
        
    def getIntValue(self):
        # TODO: Implement getIntValue method
        pass

class Module:

    pass
class raspirover_ArduinoModule(Module):

    pass
class ArduinoModule:

    pass
class raspirover_ArduinoAnalogModule(ArduinoModule):

    pass
class raspirover_ArduinoDigitalModule(ArduinoModule):

    pass
class Pin:

    pass
class raspirover_Instruction(ABC):

    def __init__(self, raspirover_Instruction: "raspirover_Block" = None):
        self.raspirover_Instruction = raspirover_Instruction
        
    @property
    def raspirover_Instruction(self):
        return self.__raspirover_Instruction

    @raspirover_Instruction.setter
    def raspirover_Instruction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_Instruction__raspirover_Instruction", None)
        self.__raspirover_Instruction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "raspirover_Block19"):
                opp_val = getattr(old_value, "raspirover_Block19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raspirover_Block19"):
                opp_val = getattr(value, "raspirover_Block19", None)
                if opp_val is None:
                    setattr(value, "raspirover_Block19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def execute(self):
        # TODO: Implement execute method
        pass

    def finalize(self):
        # TODO: Implement finalize method
        pass

class raspirover_Block:

    def __init__(self, raspirover_Block: "raspirover_Sketch" = None, raspirover_Block19: set["raspirover_Instruction"] = None):
        self.raspirover_Block = raspirover_Block
        self.raspirover_Block19 = raspirover_Block19 if raspirover_Block19 is not None else set()
        
    @property
    def raspirover_Block(self):
        return self.__raspirover_Block

    @raspirover_Block.setter
    def raspirover_Block(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_Block__raspirover_Block", None)
        self.__raspirover_Block = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "raspirover_Sketch"):
                opp_val = getattr(old_value, "raspirover_Sketch", None)
                if opp_val == self:
                    setattr(old_value, "raspirover_Sketch", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raspirover_Sketch"):
                opp_val = getattr(value, "raspirover_Sketch", None)
                setattr(value, "raspirover_Sketch", self)

    @property
    def raspirover_Block19(self):
        return self.__raspirover_Block19

    @raspirover_Block19.setter
    def raspirover_Block19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_Block__raspirover_Block19", None)
        self.__raspirover_Block19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "raspirover_Instruction"):
                    opp_val = getattr(item, "raspirover_Instruction", None)
                    
                    if opp_val == self:
                        setattr(item, "raspirover_Instruction", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "raspirover_Instruction"):
                    opp_val = getattr(item, "raspirover_Instruction", None)
                    
                    setattr(item, "raspirover_Instruction", self)
                    

    def execute(self):
        # TODO: Implement execute method
        pass

class raspirover_RoverProgram:

    def __init__(self, name: str, raspirover_RoverProgram25: set["raspirover_Param"] = None, raspirover_RoverProgram: "raspirover_Project" = None, raspirover_RoverProgram27: "raspirover_RclBlock" = None):
        self.name = name
        self.raspirover_RoverProgram25 = raspirover_RoverProgram25 if raspirover_RoverProgram25 is not None else set()
        self.raspirover_RoverProgram = raspirover_RoverProgram
        self.raspirover_RoverProgram27 = raspirover_RoverProgram27
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def raspirover_RoverProgram27(self):
        return self.__raspirover_RoverProgram27

    @raspirover_RoverProgram27.setter
    def raspirover_RoverProgram27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_RoverProgram__raspirover_RoverProgram27", None)
        self.__raspirover_RoverProgram27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "raspirover_RclBlock"):
                opp_val = getattr(old_value, "raspirover_RclBlock", None)
                if opp_val == self:
                    setattr(old_value, "raspirover_RclBlock", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raspirover_RclBlock"):
                opp_val = getattr(value, "raspirover_RclBlock", None)
                setattr(value, "raspirover_RclBlock", self)

    @property
    def raspirover_RoverProgram(self):
        return self.__raspirover_RoverProgram

    @raspirover_RoverProgram.setter
    def raspirover_RoverProgram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_RoverProgram__raspirover_RoverProgram", None)
        self.__raspirover_RoverProgram = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "raspirover_Project"):
                opp_val = getattr(old_value, "raspirover_Project", None)
                if opp_val == self:
                    setattr(old_value, "raspirover_Project", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raspirover_Project"):
                opp_val = getattr(value, "raspirover_Project", None)
                setattr(value, "raspirover_Project", self)

    @property
    def raspirover_RoverProgram25(self):
        return self.__raspirover_RoverProgram25

    @raspirover_RoverProgram25.setter
    def raspirover_RoverProgram25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_RoverProgram__raspirover_RoverProgram25", None)
        self.__raspirover_RoverProgram25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "raspirover_Param"):
                    opp_val = getattr(item, "raspirover_Param", None)
                    
                    if opp_val == self:
                        setattr(item, "raspirover_Param", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "raspirover_Param"):
                    opp_val = getattr(item, "raspirover_Param", None)
                    
                    setattr(item, "raspirover_Param", self)
                    

    def getVar(self, n: str) -> str:
        # TODO: Implement getVar method
        pass

    def bindVar(self, n: str, v: str):
        # TODO: Implement bindVar method
        pass

    def run(self):
        # TODO: Implement run method
        pass

class raspirover_RclBlock(Statement):

    def __init__(self, raspirover_RclBlock: "raspirover_RoverProgram" = None, 30: "raspirover_Statement" = None, raspirover_RclBlock35: "raspirover_Conditional" = None, raspirover_RclBlock38: "raspirover_Conditional" = None, raspirover_RclBlock43: "raspirover_Loop" = None, 45: set["raspirover_Statement"] = None):
        self.raspirover_RclBlock = raspirover_RclBlock
        self.30 = 30
        self.raspirover_RclBlock35 = raspirover_RclBlock35
        self.raspirover_RclBlock38 = raspirover_RclBlock38
        self.raspirover_RclBlock43 = raspirover_RclBlock43
        self.45 = 45 if 45 is not None else set()
        
    @property
    def raspirover_RclBlock38(self):
        return self.__raspirover_RclBlock38

    @raspirover_RclBlock38.setter
    def raspirover_RclBlock38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_RclBlock__raspirover_RclBlock38", None)
        self.__raspirover_RclBlock38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "raspirover_Conditional37"):
                opp_val = getattr(old_value, "raspirover_Conditional37", None)
                if opp_val == self:
                    setattr(old_value, "raspirover_Conditional37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raspirover_Conditional37"):
                opp_val = getattr(value, "raspirover_Conditional37", None)
                setattr(value, "raspirover_Conditional37", self)

    @property
    def raspirover_RclBlock(self):
        return self.__raspirover_RclBlock

    @raspirover_RclBlock.setter
    def raspirover_RclBlock(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_RclBlock__raspirover_RclBlock", None)
        self.__raspirover_RclBlock = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "raspirover_RoverProgram27"):
                opp_val = getattr(old_value, "raspirover_RoverProgram27", None)
                if opp_val == self:
                    setattr(old_value, "raspirover_RoverProgram27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raspirover_RoverProgram27"):
                opp_val = getattr(value, "raspirover_RoverProgram27", None)
                setattr(value, "raspirover_RoverProgram27", self)

    @property
    def 45(self):
        return self.__45

    @45.setter
    def 45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_RclBlock__45", None)
        self.__45 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "46"):
                    opp_val = getattr(item, "46", None)
                    
                    if opp_val == self:
                        setattr(item, "46", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "46"):
                    opp_val = getattr(item, "46", None)
                    
                    setattr(item, "46", self)
                    

    @property
    def 30(self):
        return self.__30

    @30.setter
    def 30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_RclBlock__30", None)
        self.__30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "29"):
                opp_val = getattr(old_value, "29", None)
                if opp_val == self:
                    setattr(old_value, "29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "29"):
                opp_val = getattr(value, "29", None)
                setattr(value, "29", self)

    @property
    def raspirover_RclBlock35(self):
        return self.__raspirover_RclBlock35

    @raspirover_RclBlock35.setter
    def raspirover_RclBlock35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_RclBlock__raspirover_RclBlock35", None)
        self.__raspirover_RclBlock35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "raspirover_Conditional34"):
                opp_val = getattr(old_value, "raspirover_Conditional34", None)
                if opp_val == self:
                    setattr(old_value, "raspirover_Conditional34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raspirover_Conditional34"):
                opp_val = getattr(value, "raspirover_Conditional34", None)
                setattr(value, "raspirover_Conditional34", self)

    @property
    def raspirover_RclBlock43(self):
        return self.__raspirover_RclBlock43

    @raspirover_RclBlock43.setter
    def raspirover_RclBlock43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_RclBlock__raspirover_RclBlock43", None)
        self.__raspirover_RclBlock43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "raspirover_Loop42"):
                opp_val = getattr(old_value, "raspirover_Loop42", None)
                if opp_val == self:
                    setattr(old_value, "raspirover_Loop42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raspirover_Loop42"):
                opp_val = getattr(value, "raspirover_Loop42", None)
                setattr(value, "raspirover_Loop42", self)

    def eval(self):
        # TODO: Implement eval method
        pass

class raspirover_Param:

    def __init__(self, name: str, raspirover_Param: "raspirover_RoverProgram" = None):
        self.name = name
        self.raspirover_Param = raspirover_Param
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def raspirover_Param(self):
        return self.__raspirover_Param

    @raspirover_Param.setter
    def raspirover_Param(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_Param__raspirover_Param", None)
        self.__raspirover_Param = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "raspirover_RoverProgram25"):
                opp_val = getattr(old_value, "raspirover_RoverProgram25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raspirover_RoverProgram25"):
                opp_val = getattr(value, "raspirover_RoverProgram25", None)
                if opp_val is None:
                    setattr(value, "raspirover_RoverProgram25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class raspirover_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class raspirover_Project:

    def __init__(self, 4: "raspirover_Board" = None, 6: set["raspirover_Board"] = None, 9: set["raspirover_Sketch"] = None, raspirover_Project: "raspirover_RoverProgram" = None, 14: "raspirover_Sketch" = None):
        self.4 = 4
        self.6 = 6 if 6 is not None else set()
        self.9 = 9 if 9 is not None else set()
        self.raspirover_Project = raspirover_Project
        self.14 = 14
        
    @property
    def 4(self):
        return self.__4

    @4.setter
    def 4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_Project__4", None)
        self.__4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, ""):
                opp_val = getattr(old_value, "", None)
                if opp_val == self:
                    setattr(old_value, "", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, ""):
                opp_val = getattr(value, "", None)
                setattr(value, "", self)

    @property
    def 14(self):
        return self.__14

    @14.setter
    def 14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_Project__14", None)
        self.__14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "13"):
                opp_val = getattr(old_value, "13", None)
                if opp_val == self:
                    setattr(old_value, "13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "13"):
                opp_val = getattr(value, "13", None)
                setattr(value, "13", self)

    @property
    def 6(self):
        return self.__6

    @6.setter
    def 6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_Project__6", None)
        self.__6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "7"):
                    opp_val = getattr(item, "7", None)
                    
                    if opp_val == self:
                        setattr(item, "7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "7"):
                    opp_val = getattr(item, "7", None)
                    
                    setattr(item, "7", self)
                    

    @property
    def 9(self):
        return self.__9

    @9.setter
    def 9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_Project__9", None)
        self.__9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "10"):
                    opp_val = getattr(item, "10", None)
                    
                    if opp_val == self:
                        setattr(item, "10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "10"):
                    opp_val = getattr(item, "10", None)
                    
                    setattr(item, "10", self)
                    

    @property
    def raspirover_Project(self):
        return self.__raspirover_Project

    @raspirover_Project.setter
    def raspirover_Project(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_Project__raspirover_Project", None)
        self.__raspirover_Project = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "raspirover_RoverProgram"):
                opp_val = getattr(old_value, "raspirover_RoverProgram", None)
                if opp_val == self:
                    setattr(old_value, "raspirover_RoverProgram", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raspirover_RoverProgram"):
                opp_val = getattr(value, "raspirover_RoverProgram", None)
                setattr(value, "raspirover_RoverProgram", self)

    def execute(self):
        # TODO: Implement execute method
        pass

class NamedElement:

    pass
class raspirover_Sketch(NamedElement):

    pass
class raspirover_Pin(NamedElement):

    def __init__(self, level: int, raspirover_Pin: "raspirover_Action" = None):
        self.level = level
        self.raspirover_Pin = raspirover_Pin
        
    @property
    def level(self) -> int:
        return self.__level

    @level.setter
    def level(self, level: int):
        self.__level = level

    @property
    def raspirover_Pin(self):
        return self.__raspirover_Pin

    @raspirover_Pin.setter
    def raspirover_Pin(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_Pin__raspirover_Pin", None)
        self.__raspirover_Pin = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "raspirover_Action"):
                opp_val = getattr(old_value, "raspirover_Action", None)
                if opp_val == self:
                    setattr(old_value, "raspirover_Action", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raspirover_Action"):
                opp_val = getattr(value, "raspirover_Action", None)
                setattr(value, "raspirover_Action", self)

class raspirover_Module(NamedElement):

    pass
class raspirover_Board(NamedElement):

    pass
class raspirover_AnalogPin(Pin):

    pass
class raspirover_DigitalPin(Pin):

    pass
class Board:

    pass
class raspirover_RasPiBoard(Board):

    pass