from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Function:

    pass
class expressions_Count(Function):

    pass
class expressions_Model:

    pass
class UnaryOperator:

    pass
class expressions_Neg(UnaryOperator):

    pass
class BinaryOperator:

    pass
class expressions_And(BinaryOperator):

    pass
class expressions_Or(BinaryOperator):

    pass
class expressions_Implies(BinaryOperator):

    pass
class ComparisonOperand:

    pass
class expressions_Function(ComparisonOperand):

    pass
class expressions_Quantity(ComparisonOperand):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class ComparisonOperator:

    pass
class expressions_E(ComparisonOperator):

    pass
class expressions_G(ComparisonOperator):

    pass
class expressions_L(ComparisonOperator):

    pass
class expressions_D(ComparisonOperator):

    pass
class expressions_LE(ComparisonOperator):

    pass
class expressions_GE(ComparisonOperator):

    pass
class QuantifyOperator:

    pass
class expressions_Number(QuantifyOperator):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class expressions_Any(QuantifyOperator):

    pass
class expressions_All(QuantifyOperator):

    pass
class Expression:

    pass
class expressions_Feature(Expression):

    def __init__(self, name: str, expressions_Feature: "expressions_Function" = None, expressions_Feature14: "expressions_QuantifyOperator" = None):
        self.name = name
        self.expressions_Feature = expressions_Feature
        self.expressions_Feature14 = expressions_Feature14
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def expressions_Feature14(self):
        return self.__expressions_Feature14

    @expressions_Feature14.setter
    def expressions_Feature14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expressions_Feature__expressions_Feature14", None)
        self.__expressions_Feature14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expressions_QuantifyOperator"):
                opp_val = getattr(old_value, "expressions_QuantifyOperator", None)
                if opp_val == self:
                    setattr(old_value, "expressions_QuantifyOperator", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expressions_QuantifyOperator"):
                opp_val = getattr(value, "expressions_QuantifyOperator", None)
                setattr(value, "expressions_QuantifyOperator", self)

    @property
    def expressions_Feature(self):
        return self.__expressions_Feature

    @expressions_Feature.setter
    def expressions_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expressions_Feature__expressions_Feature", None)
        self.__expressions_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expressions_Function"):
                opp_val = getattr(old_value, "expressions_Function", None)
                if opp_val == self:
                    setattr(old_value, "expressions_Function", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expressions_Function"):
                opp_val = getattr(value, "expressions_Function", None)
                setattr(value, "expressions_Function", self)

class expressions_ComparisonOperator(Expression):

    pass
class expressions_ComparisonOperand(Expression):

    pass
class expressions_UnaryOperator(Expression):

    pass
class expressions_QuantifyOperator(Expression):

    pass
class expressions_BinaryOperator(Expression):

    pass
class expressions_Expression(ABC):

    pass