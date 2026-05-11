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
    eq = "eq"
    neq = "neq"
    gt = "gt"
    leq = "leq"
    geq = "geq"
    lt = "lt"
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
class raspirover_AngleSubtract(AngleOperation, QuantityHomogenousOperation):

    pass
class raspirover_AngleEquals(AngleOperation, QuantityHomogenousOperation):

    pass
class raspirover_AngleAdd(AngleOperation, QuantityHomogenousOperation):

    pass
class raspirover_AngleGreater(AngleOperation, QuantityHomogenousOperation):

    pass
class raspirover_AngleSmaller(AngleOperation, QuantityHomogenousOperation):

    pass
class raspirover_AngleDistinct(AngleOperation, QuantityHomogenousOperation):

    pass
class LengthOperation:

    pass
class raspirover_LengthGreater(LengthOperation, QuantityHomogenousOperation):

    pass
class raspirover_LengthSmaller(LengthOperation, QuantityHomogenousOperation):

    pass
class raspirover_LengthScalarMultiply(QuantityScalarOperation, LengthOperation):

    pass
class raspirover_LengthSubtract(LengthOperation, QuantityHomogenousOperation):

    pass
class raspirover_LengthAdd(LengthOperation, QuantityHomogenousOperation):

    pass
class QuantityOperation:

    pass
class raspirover_QuantityComparisonOperation(QuantityOperation):

    pass
class raspirover_QuantityArithmeticOperation(QuantityOperation):

    pass
class raspirover_QuantityHomogenousOperation(QuantityOperation):

    pass
class raspirover_AngleOperation(QuantityOperation):

    pass
class raspirover_QuantityScalarOperation(QuantityOperation):

    def __init__(self, rhs: float, raspirover_QuantityScalarOperation: "raspirover_Quantity" = None):
        self.rhs = rhs
        self.raspirover_QuantityScalarOperation = raspirover_QuantityScalarOperation
        
        pass
    @property
    def rhs(self):
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
            if hasattr(old_value, "raspirover_Quantity67"):
                opp_val = getattr(old_value, "raspirover_Quantity67", None)
                if opp_val == self:
                    setattr(old_value, "raspirover_Quantity67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raspirover_Quantity67"):
                opp_val = getattr(value, "raspirover_Quantity67", None)
                setattr(value, "raspirover_Quantity67", self)

class raspirover_LengthOperation(QuantityOperation):

    pass
class raspirover_QuantityOperation(ABC):

    pass
class raspirover_LengthDistinct(LengthOperation, QuantityHomogenousOperation):

    pass
class raspirover_LengthEquals(LengthOperation, QuantityHomogenousOperation):

    pass
class raspirover_LengthScalarDivide(LengthOperation, QuantityScalarOperation):

    pass
class Quantity:

    pass
class raspirover_Angle(Quantity):

    def __init__(self):
        
        pass
    def print(self):
        # TODO: Implement print method
        pass

    def toRad(self):
        # TODO: Implement toRad method
        pass

class raspirover_Length(Quantity):

    def __init__(self):
        
        pass
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
        
        pass
    def toRad(self, raspirover_value):
        # TODO: Implement toRad method
        pass

    def getSymbol(self):
        # TODO: Implement getSymbol method
        pass

class raspirover_Turn(AngleUnit):

    def __init__(self):
        
        pass
    def toRad(self, raspirover_value):
        # TODO: Implement toRad method
        pass

    def getSymbol(self):
        # TODO: Implement getSymbol method
        pass

class raspirover_Degree(AngleUnit):

    def __init__(self):
        
        pass
    def toRad(self, raspirover_value):
        # TODO: Implement toRad method
        pass

    def getSymbol(self):
        # TODO: Implement getSymbol method
        pass

class raspirover_Radian(AngleUnit):

    def __init__(self):
        
        pass
    def toRad(self, raspirover_value):
        # TODO: Implement toRad method
        pass

    def getSymbol(self):
        # TODO: Implement getSymbol method
        pass

class ImperialSystemUnit:

    pass
class LengthUnit:

    pass
class raspirover_Yard(ImperialSystemUnit, LengthUnit):

    def __init__(self):
        
        pass
    def getSymbol(self):
        # TODO: Implement getSymbol method
        pass

    def toCm(self, raspirover_value):
        # TODO: Implement toCm method
        pass

class raspirover_Inch(ImperialSystemUnit, LengthUnit):

    def __init__(self):
        
        pass
    def getSymbol(self):
        # TODO: Implement getSymbol method
        pass

    def toCm(self, raspirover_value):
        # TODO: Implement toCm method
        pass

class raspirover_Foot(ImperialSystemUnit, LengthUnit):

    def __init__(self):
        
        pass
    def getSymbol(self):
        # TODO: Implement getSymbol method
        pass

    def toCm(self, raspirover_value):
        # TODO: Implement toCm method
        pass

class MetricSystemUnit:

    pass
class raspirover_Meter(MetricSystemUnit, LengthUnit):

    def __init__(self):
        
        pass
    def getSymbol(self):
        # TODO: Implement getSymbol method
        pass

    def toCm(self, raspirover_value):
        # TODO: Implement toCm method
        pass

class raspirover_Millimeter(MetricSystemUnit, LengthUnit):

    def __init__(self):
        
        pass
    def getSymbol(self):
        # TODO: Implement getSymbol method
        pass

    def toCm(self, raspirover_value):
        # TODO: Implement toCm method
        pass

class raspirover_Centimeter(LengthUnit, MetricSystemUnit):

    def __init__(self):
        
        pass
    def toCm(self, raspirover_value):
        # TODO: Implement toCm method
        pass

    def getSymbol(self):
        # TODO: Implement getSymbol method
        pass

class Unit:

    pass
class raspirover_MetricSystemUnit(Unit):

    pass
class raspirover_AngleUnit(Unit):

    def __init__(self):
        
        pass
    def toRad(self, raspirover_value):
        # TODO: Implement toRad method
        pass

class raspirover_ImperialSystemUnit(Unit):

    pass
class raspirover_LengthUnit(Unit):

    def __init__(self):
        
        pass
    def toCm(self, raspirover_value):
        # TODO: Implement toCm method
        pass

class raspirover_Unit(ABC):

    def __init__(self, raspirover_Unit: "raspirover_Quantity" = None):
        self.raspirover_Unit = raspirover_Unit
        
        pass
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
            if hasattr(old_value, "raspirover_Quantity60"):
                opp_val = getattr(old_value, "raspirover_Quantity60", None)
                if opp_val == self:
                    setattr(old_value, "raspirover_Quantity60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raspirover_Quantity60"):
                opp_val = getattr(value, "raspirover_Quantity60", None)
                setattr(value, "raspirover_Quantity60", self)

    def getSymbol(self):
        # TODO: Implement getSymbol method
        pass

class Action:

    pass
class raspirover_TurnDegAction(Action):

    def __init__(self, raspirover_TurnDegAction: "raspirover_NumberValue" = None):
        self.raspirover_TurnDegAction = raspirover_TurnDegAction
        
        pass
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
            if hasattr(old_value, "raspirover_NumberValue58"):
                opp_val = getattr(old_value, "raspirover_NumberValue58", None)
                if opp_val == self:
                    setattr(old_value, "raspirover_NumberValue58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raspirover_NumberValue58"):
                opp_val = getattr(value, "raspirover_NumberValue58", None)
                setattr(value, "raspirover_NumberValue58", self)

    def eval(self):
        # TODO: Implement eval method
        pass

class raspirover_SendAction(Action):

    def __init__(self, message: str):
        self.message = message
        
        pass
    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, message: str):
        self.__message = message


    def eval(self):
        # TODO: Implement eval method
        pass

class raspirover_TurnAction(Action):

    def __init__(self):
        
        pass
    def eval(self):
        # TODO: Implement eval method
        pass

class raspirover_StopAction(Action):

    def __init__(self):
        
        pass
    def eval(self):
        # TODO: Implement eval method
        pass

class raspirover_ForwardMinAction(Action):

    def __init__(self, raspirover_ForwardMinAction: "raspirover_NumberValue" = None):
        self.raspirover_ForwardMinAction = raspirover_ForwardMinAction
        
        pass
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
            if hasattr(old_value, "raspirover_NumberValue54"):
                opp_val = getattr(old_value, "raspirover_NumberValue54", None)
                if opp_val == self:
                    setattr(old_value, "raspirover_NumberValue54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raspirover_NumberValue54"):
                opp_val = getattr(value, "raspirover_NumberValue54", None)
                setattr(value, "raspirover_NumberValue54", self)

    def eval(self):
        # TODO: Implement eval method
        pass

class raspirover_LogAction(Action):

    def __init__(self, message: str):
        self.message = message
        
        pass
    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, message: str):
        self.__message = message


    def eval(self):
        # TODO: Implement eval method
        pass

class raspirover_ForwardAction(Action):

    def __init__(self):
        
        pass
    def eval(self):
        # TODO: Implement eval method
        pass

class raspirover_BackwardMinAction(Action):

    def __init__(self, raspirover_BackwardMinAction: "raspirover_NumberValue" = None):
        self.raspirover_BackwardMinAction = raspirover_BackwardMinAction
        
        pass
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
            if hasattr(old_value, "raspirover_NumberValue56"):
                opp_val = getattr(old_value, "raspirover_NumberValue56", None)
                if opp_val == self:
                    setattr(old_value, "raspirover_NumberValue56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raspirover_NumberValue56"):
                opp_val = getattr(value, "raspirover_NumberValue56", None)
                setattr(value, "raspirover_NumberValue56", self)

    def eval(self):
        # TODO: Implement eval method
        pass

class raspirover_BackwardAction(Action):

    def __init__(self):
        
        pass
    def eval(self):
        # TODO: Implement eval method
        pass

class RoverValue:

    pass
class raspirover_BooleanValue(RoverValue):

    def __init__(self, bValue: bool, raspirover_BooleanValue: "raspirover_BooleanExpression" = None, raspirover_BooleanValue49: "raspirover_BooleanExpression" = None):
        self.bValue = bValue
        self.raspirover_BooleanValue = raspirover_BooleanValue
        self.raspirover_BooleanValue49 = raspirover_BooleanValue49
        
        pass
    @property
    def bValue(self):
        return self.__bValue

    @bValue.setter
    def bValue(self, bValue: bool):
        self.__bValue = bValue


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

    @property
    def raspirover_BooleanValue49(self):
        return self.__raspirover_BooleanValue49

    @raspirover_BooleanValue49.setter
    def raspirover_BooleanValue49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_BooleanValue__raspirover_BooleanValue49", None)
        self.__raspirover_BooleanValue49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "raspirover_BooleanExpression48"):
                opp_val = getattr(old_value, "raspirover_BooleanExpression48", None)
                if opp_val == self:
                    setattr(old_value, "raspirover_BooleanExpression48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raspirover_BooleanExpression48"):
                opp_val = getattr(value, "raspirover_BooleanExpression48", None)
                setattr(value, "raspirover_BooleanExpression48", self)

    def getBooleanValue(self):
        # TODO: Implement getBooleanValue method
        pass

class raspirover_StringValue(RoverValue):

    def __init__(self, sValue: bool, raspirover_StringValue: "raspirover_StringExpression" = None, raspirover_StringValue45: "raspirover_StringExpression" = None):
        self.sValue = sValue
        self.raspirover_StringValue = raspirover_StringValue
        self.raspirover_StringValue45 = raspirover_StringValue45
        
        pass
    @property
    def sValue(self):
        return self.__sValue

    @sValue.setter
    def sValue(self, sValue: bool):
        self.__sValue = sValue


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

    @property
    def raspirover_StringValue45(self):
        return self.__raspirover_StringValue45

    @raspirover_StringValue45.setter
    def raspirover_StringValue45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_StringValue__raspirover_StringValue45", None)
        self.__raspirover_StringValue45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "raspirover_StringExpression44"):
                opp_val = getattr(old_value, "raspirover_StringExpression44", None)
                if opp_val == self:
                    setattr(old_value, "raspirover_StringExpression44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raspirover_StringExpression44"):
                opp_val = getattr(value, "raspirover_StringExpression44", None)
                setattr(value, "raspirover_StringExpression44", self)

    def getStringValue(self):
        # TODO: Implement getStringValue method
        pass

class raspirover_Quantity:

    def __init__(self, value: str, raspirover_Quantity: "raspirover_NumberValue" = None, raspirover_Quantity60: "raspirover_Unit" = None, raspirover_Quantity65: "raspirover_QuantityHomogenousOperation" = None, raspirover_Quantity67: "raspirover_QuantityScalarOperation" = None, raspirover_Quantity62: "raspirover_QuantityHomogenousOperation" = None):
        self.value = value
        self.raspirover_Quantity = raspirover_Quantity
        self.raspirover_Quantity60 = raspirover_Quantity60
        self.raspirover_Quantity65 = raspirover_Quantity65
        self.raspirover_Quantity67 = raspirover_Quantity67
        self.raspirover_Quantity62 = raspirover_Quantity62
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def raspirover_Quantity60(self):
        return self.__raspirover_Quantity60

    @raspirover_Quantity60.setter
    def raspirover_Quantity60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_Quantity__raspirover_Quantity60", None)
        self.__raspirover_Quantity60 = value
        
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
    def raspirover_Quantity67(self):
        return self.__raspirover_Quantity67

    @raspirover_Quantity67.setter
    def raspirover_Quantity67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_Quantity__raspirover_Quantity67", None)
        self.__raspirover_Quantity67 = value
        
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

    @property
    def raspirover_Quantity65(self):
        return self.__raspirover_Quantity65

    @raspirover_Quantity65.setter
    def raspirover_Quantity65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_Quantity__raspirover_Quantity65", None)
        self.__raspirover_Quantity65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "raspirover_QuantityHomogenousOperation64"):
                opp_val = getattr(old_value, "raspirover_QuantityHomogenousOperation64", None)
                if opp_val == self:
                    setattr(old_value, "raspirover_QuantityHomogenousOperation64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raspirover_QuantityHomogenousOperation64"):
                opp_val = getattr(value, "raspirover_QuantityHomogenousOperation64", None)
                setattr(value, "raspirover_QuantityHomogenousOperation64", self)

    @property
    def raspirover_Quantity62(self):
        return self.__raspirover_Quantity62

    @raspirover_Quantity62.setter
    def raspirover_Quantity62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_Quantity__raspirover_Quantity62", None)
        self.__raspirover_Quantity62 = value
        
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
            if hasattr(old_value, "raspirover_NumberValue51"):
                opp_val = getattr(old_value, "raspirover_NumberValue51", None)
                if opp_val == self:
                    setattr(old_value, "raspirover_NumberValue51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raspirover_NumberValue51"):
                opp_val = getattr(value, "raspirover_NumberValue51", None)
                setattr(value, "raspirover_NumberValue51", self)

    def print(self):
        # TODO: Implement print method
        pass

    def getNormalized(self):
        # TODO: Implement getNormalized method
        pass

class raspirover_NumberValue(RoverValue):

    def __init__(self, nValue: str, raspirover_NumberValue: "raspirover_NumericExpression" = None, raspirover_NumberValue41: "raspirover_NumericExpression" = None, raspirover_NumberValue51: "raspirover_Quantity" = None, raspirover_NumberValue54: "raspirover_ForwardMinAction" = None, raspirover_NumberValue56: "raspirover_BackwardMinAction" = None, raspirover_NumberValue58: "raspirover_TurnDegAction" = None):
        self.nValue = nValue
        self.raspirover_NumberValue = raspirover_NumberValue
        self.raspirover_NumberValue41 = raspirover_NumberValue41
        self.raspirover_NumberValue51 = raspirover_NumberValue51
        self.raspirover_NumberValue54 = raspirover_NumberValue54
        self.raspirover_NumberValue56 = raspirover_NumberValue56
        self.raspirover_NumberValue58 = raspirover_NumberValue58
        
        pass
    @property
    def nValue(self):
        return self.__nValue

    @nValue.setter
    def nValue(self, nValue: str):
        self.__nValue = nValue


    @property
    def raspirover_NumberValue41(self):
        return self.__raspirover_NumberValue41

    @raspirover_NumberValue41.setter
    def raspirover_NumberValue41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_NumberValue__raspirover_NumberValue41", None)
        self.__raspirover_NumberValue41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "raspirover_NumericExpression40"):
                opp_val = getattr(old_value, "raspirover_NumericExpression40", None)
                if opp_val == self:
                    setattr(old_value, "raspirover_NumericExpression40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raspirover_NumericExpression40"):
                opp_val = getattr(value, "raspirover_NumericExpression40", None)
                setattr(value, "raspirover_NumericExpression40", self)

    @property
    def raspirover_NumberValue54(self):
        return self.__raspirover_NumberValue54

    @raspirover_NumberValue54.setter
    def raspirover_NumberValue54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_NumberValue__raspirover_NumberValue54", None)
        self.__raspirover_NumberValue54 = value
        
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

    @property
    def raspirover_NumberValue51(self):
        return self.__raspirover_NumberValue51

    @raspirover_NumberValue51.setter
    def raspirover_NumberValue51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_NumberValue__raspirover_NumberValue51", None)
        self.__raspirover_NumberValue51 = value
        
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
    def raspirover_NumberValue58(self):
        return self.__raspirover_NumberValue58

    @raspirover_NumberValue58.setter
    def raspirover_NumberValue58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_NumberValue__raspirover_NumberValue58", None)
        self.__raspirover_NumberValue58 = value
        
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
    def raspirover_NumberValue56(self):
        return self.__raspirover_NumberValue56

    @raspirover_NumberValue56.setter
    def raspirover_NumberValue56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_NumberValue__raspirover_NumberValue56", None)
        self.__raspirover_NumberValue56 = value
        
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

    def print(self):
        # TODO: Implement print method
        pass

    def getIntValue(self):
        # TODO: Implement getIntValue method
        pass

class RoverExpression:

    pass
class raspirover_BooleanExpression(RoverExpression):

    def __init__(self, op: str, raspirover_BooleanExpression: "raspirover_BooleanValue" = None, raspirover_BooleanExpression48: "raspirover_BooleanValue" = None):
        self.op = op
        self.raspirover_BooleanExpression = raspirover_BooleanExpression
        self.raspirover_BooleanExpression48 = raspirover_BooleanExpression48
        
        pass
    @property
    def op(self):
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op


    @property
    def raspirover_BooleanExpression48(self):
        return self.__raspirover_BooleanExpression48

    @raspirover_BooleanExpression48.setter
    def raspirover_BooleanExpression48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_BooleanExpression__raspirover_BooleanExpression48", None)
        self.__raspirover_BooleanExpression48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "raspirover_BooleanValue49"):
                opp_val = getattr(old_value, "raspirover_BooleanValue49", None)
                if opp_val == self:
                    setattr(old_value, "raspirover_BooleanValue49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raspirover_BooleanValue49"):
                opp_val = getattr(value, "raspirover_BooleanValue49", None)
                setattr(value, "raspirover_BooleanValue49", self)

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

class raspirover_NumericExpression(RoverExpression):

    def __init__(self, op: bool, raspirover_NumericExpression: "raspirover_NumberValue" = None, raspirover_NumericExpression40: "raspirover_NumberValue" = None):
        self.op = op
        self.raspirover_NumericExpression = raspirover_NumericExpression
        self.raspirover_NumericExpression40 = raspirover_NumericExpression40
        
        pass
    @property
    def op(self):
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
    def raspirover_NumericExpression40(self):
        return self.__raspirover_NumericExpression40

    @raspirover_NumericExpression40.setter
    def raspirover_NumericExpression40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_NumericExpression__raspirover_NumericExpression40", None)
        self.__raspirover_NumericExpression40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "raspirover_NumberValue41"):
                opp_val = getattr(old_value, "raspirover_NumberValue41", None)
                if opp_val == self:
                    setattr(old_value, "raspirover_NumberValue41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raspirover_NumberValue41"):
                opp_val = getattr(value, "raspirover_NumberValue41", None)
                setattr(value, "raspirover_NumberValue41", self)

    def eval(self):
        # TODO: Implement eval method
        pass

class BooleanValue:

    pass
class raspirover_StringExpression(RoverExpression):

    def __init__(self, op: bool, raspirover_StringExpression: "raspirover_StringValue" = None, raspirover_StringExpression44: "raspirover_StringValue" = None):
        self.op = op
        self.raspirover_StringExpression = raspirover_StringExpression
        self.raspirover_StringExpression44 = raspirover_StringExpression44
        
        pass
    @property
    def op(self):
        return self.__op

    @op.setter
    def op(self, op: bool):
        self.__op = op


    @property
    def raspirover_StringExpression44(self):
        return self.__raspirover_StringExpression44

    @raspirover_StringExpression44.setter
    def raspirover_StringExpression44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_StringExpression__raspirover_StringExpression44", None)
        self.__raspirover_StringExpression44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "raspirover_StringValue45"):
                opp_val = getattr(old_value, "raspirover_StringValue45", None)
                if opp_val == self:
                    setattr(old_value, "raspirover_StringValue45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raspirover_StringValue45"):
                opp_val = getattr(value, "raspirover_StringValue45", None)
                setattr(value, "raspirover_StringValue45", self)

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

    def eval(self):
        # TODO: Implement eval method
        pass

class StringValue:

    pass
class NumberValue:

    pass
class Query:

    pass
class raspirover_ObstacleQuery(Query, BooleanValue):

    def __init__(self, front: bool):
        self.front = front
        
        pass
    @property
    def front(self):
        return self.__front

    @front.setter
    def front(self, front: bool):
        self.__front = front


    def getBooleanValue(self):
        # TODO: Implement getBooleanValue method
        pass

class raspirover_MessageQuery(Query, StringValue):

    def __init__(self):
        
        pass
    def getStringValue(self):
        # TODO: Implement getStringValue method
        pass

class raspirover_HumidityQuery(Query, NumberValue):

    def __init__(self):
        
        pass
    def getIntValue(self):
        # TODO: Implement getIntValue method
        pass

class raspirover_TemperatureQuery(Query, NumberValue):

    def __init__(self):
        
        pass
    def getIntValue(self):
        # TODO: Implement getIntValue method
        pass

class raspirover_Query(ABC):

    pass
class raspirover_RoverExpression(ABC):

    def __init__(self, raspirover_RoverExpression: "raspirover_Conditional" = None, raspirover_RoverExpression33: "raspirover_Loop" = None):
        self.raspirover_RoverExpression = raspirover_RoverExpression
        self.raspirover_RoverExpression33 = raspirover_RoverExpression33
        
        pass
    @property
    def raspirover_RoverExpression33(self):
        return self.__raspirover_RoverExpression33

    @raspirover_RoverExpression33.setter
    def raspirover_RoverExpression33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_RoverExpression__raspirover_RoverExpression33", None)
        self.__raspirover_RoverExpression33 = value
        
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
class raspirover_Action(Statement):

    pass
class raspirover_Loop(Statement):

    def __init__(self, raspirover_Loop: "raspirover_RoverExpression" = None, raspirover_Loop35: "raspirover_RclBlock" = None):
        self.raspirover_Loop = raspirover_Loop
        self.raspirover_Loop35 = raspirover_Loop35
        
        pass
    @property
    def raspirover_Loop35(self):
        return self.__raspirover_Loop35

    @raspirover_Loop35.setter
    def raspirover_Loop35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_Loop__raspirover_Loop35", None)
        self.__raspirover_Loop35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "raspirover_RclBlock36"):
                opp_val = getattr(old_value, "raspirover_RclBlock36", None)
                if opp_val == self:
                    setattr(old_value, "raspirover_RclBlock36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raspirover_RclBlock36"):
                opp_val = getattr(value, "raspirover_RclBlock36", None)
                setattr(value, "raspirover_RclBlock36", self)

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
            if hasattr(old_value, "raspirover_RoverExpression33"):
                opp_val = getattr(old_value, "raspirover_RoverExpression33", None)
                if opp_val == self:
                    setattr(old_value, "raspirover_RoverExpression33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raspirover_RoverExpression33"):
                opp_val = getattr(value, "raspirover_RoverExpression33", None)
                setattr(value, "raspirover_RoverExpression33", self)

    def eval(self):
        # TODO: Implement eval method
        pass

class raspirover_RclBlock(Statement):

    def __init__(self, RclBlock: "raspirover_Statement" = None, raspirover_RclBlock: "raspirover_RoverProgram" = None, raspirover_RclBlock28: "raspirover_Conditional" = None, raspirover_RclBlock31: "raspirover_Conditional" = None, raspirover_RclBlock36: "raspirover_Loop" = None, enclosing: set["raspirover_Statement"] = None):
        self.RclBlock = RclBlock
        self.raspirover_RclBlock = raspirover_RclBlock
        self.raspirover_RclBlock28 = raspirover_RclBlock28
        self.raspirover_RclBlock31 = raspirover_RclBlock31
        self.raspirover_RclBlock36 = raspirover_RclBlock36
        self.enclosing = enclosing if enclosing is not None else set()
        
        pass
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
            if hasattr(old_value, "raspirover_RoverProgram22"):
                opp_val = getattr(old_value, "raspirover_RoverProgram22", None)
                if opp_val == self:
                    setattr(old_value, "raspirover_RoverProgram22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raspirover_RoverProgram22"):
                opp_val = getattr(value, "raspirover_RoverProgram22", None)
                setattr(value, "raspirover_RoverProgram22", self)

    @property
    def raspirover_RclBlock28(self):
        return self.__raspirover_RclBlock28

    @raspirover_RclBlock28.setter
    def raspirover_RclBlock28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_RclBlock__raspirover_RclBlock28", None)
        self.__raspirover_RclBlock28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "raspirover_Conditional27"):
                opp_val = getattr(old_value, "raspirover_Conditional27", None)
                if opp_val == self:
                    setattr(old_value, "raspirover_Conditional27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raspirover_Conditional27"):
                opp_val = getattr(value, "raspirover_Conditional27", None)
                setattr(value, "raspirover_Conditional27", self)

    @property
    def raspirover_RclBlock36(self):
        return self.__raspirover_RclBlock36

    @raspirover_RclBlock36.setter
    def raspirover_RclBlock36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_RclBlock__raspirover_RclBlock36", None)
        self.__raspirover_RclBlock36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "raspirover_Loop35"):
                opp_val = getattr(old_value, "raspirover_Loop35", None)
                if opp_val == self:
                    setattr(old_value, "raspirover_Loop35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raspirover_Loop35"):
                opp_val = getattr(value, "raspirover_Loop35", None)
                setattr(value, "raspirover_Loop35", self)

    @property
    def raspirover_RclBlock31(self):
        return self.__raspirover_RclBlock31

    @raspirover_RclBlock31.setter
    def raspirover_RclBlock31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_RclBlock__raspirover_RclBlock31", None)
        self.__raspirover_RclBlock31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "raspirover_Conditional30"):
                opp_val = getattr(old_value, "raspirover_Conditional30", None)
                if opp_val == self:
                    setattr(old_value, "raspirover_Conditional30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raspirover_Conditional30"):
                opp_val = getattr(value, "raspirover_Conditional30", None)
                setattr(value, "raspirover_Conditional30", self)

    @property
    def enclosing(self):
        return self.__enclosing

    @enclosing.setter
    def enclosing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_RclBlock__enclosing", None)
        self.__enclosing = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Statement"):
                    opp_val = getattr(item, "Statement", None)
                    
                    if opp_val == self:
                        setattr(item, "Statement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Statement"):
                    opp_val = getattr(item, "Statement", None)
                    
                    setattr(item, "Statement", self)
                    

    @property
    def RclBlock(self):
        return self.__RclBlock

    @RclBlock.setter
    def RclBlock(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_RclBlock__RclBlock", None)
        self.__RclBlock = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stmts"):
                opp_val = getattr(old_value, "stmts", None)
                if opp_val == self:
                    setattr(old_value, "stmts", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stmts"):
                opp_val = getattr(value, "stmts", None)
                setattr(value, "stmts", self)

    def eval(self):
        # TODO: Implement eval method
        pass

class raspirover_Conditional(Statement):

    def __init__(self, raspirover_Conditional: "raspirover_RoverExpression" = None, raspirover_Conditional27: "raspirover_RclBlock" = None, raspirover_Conditional30: "raspirover_RclBlock" = None):
        self.raspirover_Conditional = raspirover_Conditional
        self.raspirover_Conditional27 = raspirover_Conditional27
        self.raspirover_Conditional30 = raspirover_Conditional30
        
        pass
    @property
    def raspirover_Conditional30(self):
        return self.__raspirover_Conditional30

    @raspirover_Conditional30.setter
    def raspirover_Conditional30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_Conditional__raspirover_Conditional30", None)
        self.__raspirover_Conditional30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "raspirover_RclBlock31"):
                opp_val = getattr(old_value, "raspirover_RclBlock31", None)
                if opp_val == self:
                    setattr(old_value, "raspirover_RclBlock31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raspirover_RclBlock31"):
                opp_val = getattr(value, "raspirover_RclBlock31", None)
                setattr(value, "raspirover_RclBlock31", self)

    @property
    def raspirover_Conditional27(self):
        return self.__raspirover_Conditional27

    @raspirover_Conditional27.setter
    def raspirover_Conditional27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_Conditional__raspirover_Conditional27", None)
        self.__raspirover_Conditional27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "raspirover_RclBlock28"):
                opp_val = getattr(old_value, "raspirover_RclBlock28", None)
                if opp_val == self:
                    setattr(old_value, "raspirover_RclBlock28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raspirover_RclBlock28"):
                opp_val = getattr(value, "raspirover_RclBlock28", None)
                setattr(value, "raspirover_RclBlock28", self)

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

    def eval(self):
        # TODO: Implement eval method
        pass

class raspirover_VarRef(NumberValue, BooleanValue, StringValue, Statement):

    def __init__(self, name: float):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: float):
        self.__name = name


    def getIntValue(self):
        # TODO: Implement getIntValue method
        pass

    def getBooleanValue(self):
        # TODO: Implement getBooleanValue method
        pass

    def eval(self):
        # TODO: Implement eval method
        pass

    def getStringValue(self):
        # TODO: Implement getStringValue method
        pass

class raspirover_VarAssignment(Statement):

    def __init__(self, name: bool, raspirover_VarAssignment: "raspirover_RoverValue" = None):
        self.name = name
        self.raspirover_VarAssignment = raspirover_VarAssignment
        
        pass
    @property
    def name(self):
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

    def __init__(self, stmts: "raspirover_RclBlock" = None, Statement: "raspirover_RclBlock" = None):
        self.stmts = stmts
        self.Statement = Statement
        
        pass
    @property
    def Statement(self):
        return self.__Statement

    @Statement.setter
    def Statement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_Statement__Statement", None)
        self.__Statement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "enclosing"):
                opp_val = getattr(old_value, "enclosing", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "enclosing"):
                opp_val = getattr(value, "enclosing", None)
                if opp_val is None:
                    setattr(value, "enclosing", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def stmts(self):
        return self.__stmts

    @stmts.setter
    def stmts(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_Statement__stmts", None)
        self.__stmts = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RclBlock"):
                opp_val = getattr(old_value, "RclBlock", None)
                if opp_val == self:
                    setattr(old_value, "RclBlock", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RclBlock"):
                opp_val = getattr(value, "RclBlock", None)
                setattr(value, "RclBlock", self)

    def getProgram(self) :
        # TODO: Implement getProgram method
        pass

    def eval(self):
        # TODO: Implement eval method
        pass

class raspirover_Param:

    def __init__(self, name: str, raspirover_Param: "raspirover_RoverProgram" = None):
        self.name = name
        self.raspirover_Param = raspirover_Param
        
        pass
    @property
    def name(self):
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
            if hasattr(old_value, "raspirover_RoverProgram20"):
                opp_val = getattr(old_value, "raspirover_RoverProgram20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raspirover_RoverProgram20"):
                opp_val = getattr(value, "raspirover_RoverProgram20", None)
                if opp_val is None:
                    setattr(value, "raspirover_RoverProgram20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
        
        pass
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
            if hasattr(old_value, "raspirover_Block14"):
                opp_val = getattr(old_value, "raspirover_Block14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raspirover_Block14"):
                opp_val = getattr(value, "raspirover_Block14", None)
                if opp_val is None:
                    setattr(value, "raspirover_Block14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def finalize(self):
        # TODO: Implement finalize method
        pass

    def execute(self):
        # TODO: Implement execute method
        pass

class raspirover_Block:

    def __init__(self, raspirover_Block14: set["raspirover_Instruction"] = None, raspirover_Block: "raspirover_Sketch" = None):
        self.raspirover_Block14 = raspirover_Block14 if raspirover_Block14 is not None else set()
        self.raspirover_Block = raspirover_Block
        
        pass
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
    def raspirover_Block14(self):
        return self.__raspirover_Block14

    @raspirover_Block14.setter
    def raspirover_Block14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_Block__raspirover_Block14", None)
        self.__raspirover_Block14 = value if value is not None else set()
        
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

    def __init__(self, name: str, raspirover_RoverProgram20: set["raspirover_Param"] = None, raspirover_RoverProgram22: "raspirover_RclBlock" = None, raspirover_RoverProgram: "raspirover_Project" = None):
        self.name = name
        self.raspirover_RoverProgram20 = raspirover_RoverProgram20 if raspirover_RoverProgram20 is not None else set()
        self.raspirover_RoverProgram22 = raspirover_RoverProgram22
        self.raspirover_RoverProgram = raspirover_RoverProgram
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def raspirover_RoverProgram20(self):
        return self.__raspirover_RoverProgram20

    @raspirover_RoverProgram20.setter
    def raspirover_RoverProgram20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_RoverProgram__raspirover_RoverProgram20", None)
        self.__raspirover_RoverProgram20 = value if value is not None else set()
        
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
                    

    @property
    def raspirover_RoverProgram22(self):
        return self.__raspirover_RoverProgram22

    @raspirover_RoverProgram22.setter
    def raspirover_RoverProgram22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_RoverProgram__raspirover_RoverProgram22", None)
        self.__raspirover_RoverProgram22 = value
        
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

    def run(self):
        # TODO: Implement run method
        pass

    def bindVar(self, raspirover_n, raspirover_v):
        # TODO: Implement bindVar method
        pass

    def getVar(self, raspirover_n) :
        # TODO: Implement getVar method
        pass

class raspirover_Project:

    def __init__(self, project6: set["raspirover_Sketch"] = None, Project: "raspirover_Board" = None, raspirover_Project: "raspirover_RoverProgram" = None, Project9: "raspirover_Sketch" = None, project: set["raspirover_Board"] = None):
        self.project6 = project6 if project6 is not None else set()
        self.Project = Project
        self.raspirover_Project = raspirover_Project
        self.Project9 = Project9
        self.project = project if project is not None else set()
        
        pass
    @property
    def Project(self):
        return self.__Project

    @Project.setter
    def Project(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_Project__Project", None)
        self.__Project = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "boards"):
                opp_val = getattr(old_value, "boards", None)
                if opp_val == self:
                    setattr(old_value, "boards", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "boards"):
                opp_val = getattr(value, "boards", None)
                setattr(value, "boards", self)

    @property
    def project6(self):
        return self.__project6

    @project6.setter
    def project6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_Project__project6", None)
        self.__project6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Sketch"):
                    opp_val = getattr(item, "Sketch", None)
                    
                    if opp_val == self:
                        setattr(item, "Sketch", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Sketch"):
                    opp_val = getattr(item, "Sketch", None)
                    
                    setattr(item, "Sketch", self)
                    

    @property
    def project(self):
        return self.__project

    @project.setter
    def project(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_Project__project", None)
        self.__project = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Board"):
                    opp_val = getattr(item, "Board", None)
                    
                    if opp_val == self:
                        setattr(item, "Board", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Board"):
                    opp_val = getattr(item, "Board", None)
                    
                    setattr(item, "Board", self)
                    

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

    @property
    def Project9(self):
        return self.__Project9

    @Project9.setter
    def Project9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raspirover_Project__Project9", None)
        self.__Project9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sketches"):
                opp_val = getattr(old_value, "sketches", None)
                if opp_val == self:
                    setattr(old_value, "sketches", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sketches"):
                opp_val = getattr(value, "sketches", None)
                setattr(value, "sketches", self)

    def execute(self):
        # TODO: Implement execute method
        pass

class NamedElement:

    pass
class raspirover_Pin(NamedElement):

    def __init__(self, level: int, raspirover_Pin: "raspirover_Action" = None):
        self.level = level
        self.raspirover_Pin = raspirover_Pin
        
        pass
    @property
    def level(self):
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
class raspirover_Sketch(NamedElement):

    pass
class raspirover_Board(NamedElement):

    pass
class raspirover_AnalogPin(Pin):

    pass
class raspirover_DigitalPin(Pin):

    pass
class Board:

    pass
class raspirover_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class raspirover_RasPiBoard(Board):

    pass