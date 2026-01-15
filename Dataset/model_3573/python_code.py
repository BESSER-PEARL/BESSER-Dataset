from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class UnaryType(Enum):
    NEGATIVE = "NEGATIVE"
    POSITIVE = "POSITIVE"
    TILDE = "TILDE"
class AddType(Enum):
    ADDITION = "ADDITION"
    SUBTRACTION = "SUBTRACTION"
class MultiType(Enum):
    MULTIPLICATION = "MULTIPLICATION"
    DIVISION = "DIVISION"
    MODULATION = "MODULATION"
class ShiftType(Enum):
    LEFT = "LEFT"
    RIGHT = "RIGHT"


############################################
# Definition of Classes
############################################

class expressions_IdlTypeDcl:

    pass
class Expression:

    pass
class expressions_DoubleLiteral(Expression):

    def __init__(self, value: float):
        self.value = value
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

class expressions_StringLiteral(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class expressions_AddExpression(Expression):

    def __init__(self, type: str, expressions_AddExpression24: "expressions_Expression" = None, expressions_AddExpression: "expressions_Expression" = None):
        self.type = type
        self.expressions_AddExpression24 = expressions_AddExpression24
        self.expressions_AddExpression = expressions_AddExpression
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def expressions_AddExpression(self):
        return self.__expressions_AddExpression

    @expressions_AddExpression.setter
    def expressions_AddExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expressions_AddExpression__expressions_AddExpression", None)
        self.__expressions_AddExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expressions_Expression22"):
                opp_val = getattr(old_value, "expressions_Expression22", None)
                if opp_val == self:
                    setattr(old_value, "expressions_Expression22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expressions_Expression22"):
                opp_val = getattr(value, "expressions_Expression22", None)
                setattr(value, "expressions_Expression22", self)

    @property
    def expressions_AddExpression24(self):
        return self.__expressions_AddExpression24

    @expressions_AddExpression24.setter
    def expressions_AddExpression24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expressions_AddExpression__expressions_AddExpression24", None)
        self.__expressions_AddExpression24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expressions_Expression25"):
                opp_val = getattr(old_value, "expressions_Expression25", None)
                if opp_val == self:
                    setattr(old_value, "expressions_Expression25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expressions_Expression25"):
                opp_val = getattr(value, "expressions_Expression25", None)
                setattr(value, "expressions_Expression25", self)

class expressions_MultExpression(Expression):

    def __init__(self, type: str, expressions_MultExpression: "expressions_Expression" = None, expressions_MultExpression29: "expressions_Expression" = None):
        self.type = type
        self.expressions_MultExpression = expressions_MultExpression
        self.expressions_MultExpression29 = expressions_MultExpression29
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def expressions_MultExpression(self):
        return self.__expressions_MultExpression

    @expressions_MultExpression.setter
    def expressions_MultExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expressions_MultExpression__expressions_MultExpression", None)
        self.__expressions_MultExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expressions_Expression27"):
                opp_val = getattr(old_value, "expressions_Expression27", None)
                if opp_val == self:
                    setattr(old_value, "expressions_Expression27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expressions_Expression27"):
                opp_val = getattr(value, "expressions_Expression27", None)
                setattr(value, "expressions_Expression27", self)

    @property
    def expressions_MultExpression29(self):
        return self.__expressions_MultExpression29

    @expressions_MultExpression29.setter
    def expressions_MultExpression29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expressions_MultExpression__expressions_MultExpression29", None)
        self.__expressions_MultExpression29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expressions_Expression30"):
                opp_val = getattr(old_value, "expressions_Expression30", None)
                if opp_val == self:
                    setattr(old_value, "expressions_Expression30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expressions_Expression30"):
                opp_val = getattr(value, "expressions_Expression30", None)
                setattr(value, "expressions_Expression30", self)

class expressions_AndExpression(Expression):

    pass
class expressions_WideStringLiteral(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class expressions_OrExpression(Expression):

    pass
class expressions_BooleanLiteral(Expression):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class expressions_WideCharacterLiteral(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class expressions_ScopeLiteral(Expression):

    pass
class expressions_ShiftExpression(Expression):

    def __init__(self, type: str, expressions_ShiftExpression: "expressions_Expression" = None, expressions_ShiftExpression19: "expressions_Expression" = None):
        self.type = type
        self.expressions_ShiftExpression = expressions_ShiftExpression
        self.expressions_ShiftExpression19 = expressions_ShiftExpression19
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def expressions_ShiftExpression19(self):
        return self.__expressions_ShiftExpression19

    @expressions_ShiftExpression19.setter
    def expressions_ShiftExpression19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expressions_ShiftExpression__expressions_ShiftExpression19", None)
        self.__expressions_ShiftExpression19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expressions_Expression20"):
                opp_val = getattr(old_value, "expressions_Expression20", None)
                if opp_val == self:
                    setattr(old_value, "expressions_Expression20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expressions_Expression20"):
                opp_val = getattr(value, "expressions_Expression20", None)
                setattr(value, "expressions_Expression20", self)

    @property
    def expressions_ShiftExpression(self):
        return self.__expressions_ShiftExpression

    @expressions_ShiftExpression.setter
    def expressions_ShiftExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expressions_ShiftExpression__expressions_ShiftExpression", None)
        self.__expressions_ShiftExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expressions_Expression17"):
                opp_val = getattr(old_value, "expressions_Expression17", None)
                if opp_val == self:
                    setattr(old_value, "expressions_Expression17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expressions_Expression17"):
                opp_val = getattr(value, "expressions_Expression17", None)
                setattr(value, "expressions_Expression17", self)

class expressions_XOrExpression(Expression):

    pass
class expressions_UnaryExpression(Expression):

    def __init__(self, type: str, expressions_UnaryExpression: "expressions_Expression" = None):
        self.type = type
        self.expressions_UnaryExpression = expressions_UnaryExpression
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def expressions_UnaryExpression(self):
        return self.__expressions_UnaryExpression

    @expressions_UnaryExpression.setter
    def expressions_UnaryExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expressions_UnaryExpression__expressions_UnaryExpression", None)
        self.__expressions_UnaryExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expressions_Expression32"):
                opp_val = getattr(old_value, "expressions_Expression32", None)
                if opp_val == self:
                    setattr(old_value, "expressions_Expression32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expressions_Expression32"):
                opp_val = getattr(value, "expressions_Expression32", None)
                setattr(value, "expressions_Expression32", self)

class expressions_FixedPtLiteral(Expression):

    def __init__(self, integerPart: int, decimalPart: int, value: str):
        self.integerPart = integerPart
        self.decimalPart = decimalPart
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def integerPart(self) -> int:
        return self.__integerPart

    @integerPart.setter
    def integerPart(self, integerPart: int):
        self.__integerPart = integerPart

    @property
    def decimalPart(self) -> int:
        return self.__decimalPart

    @decimalPart.setter
    def decimalPart(self, decimalPart: int):
        self.__decimalPart = decimalPart

class expressions_IntegerLiteral(Expression):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class expressions_CharacterLiteral(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class expressions_FloatingPointLiteral(Expression):

    def __init__(self, value: float):
        self.value = value
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

class expressions_ConstExpression(Expression):

    pass
class FileRegion:

    pass
class expressions_Expression(FileRegion):

    pass