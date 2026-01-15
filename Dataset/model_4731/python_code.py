from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Type(Enum):
    BOOLEAN = "BOOLEAN"
    INTEGER = "INTEGER"


############################################
# Definition of Classes
############################################

class SetOp:

    pass
class simple_csp_Min(SetOp):

    pass
class simple_csp_Max(SetOp):

    pass
class simple_csp_Sum(SetOp):

    pass
class simple_csp_DescribedElement(ABC):

    def __init__(self, description: str):
        self.description = description
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

class simple_csp_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class Goal:

    pass
class simple_csp_MinimizeGoal(Goal):

    pass
class simple_csp_MaximizeGoal(Goal):

    pass
class BooleanLiteral:

    pass
class simple_csp_FalseValue(BooleanLiteral):

    pass
class simple_csp_TrueValue(BooleanLiteral):

    pass
class Domain:

    pass
class simple_csp_IntegerDomain(Domain):

    def __init__(self, minValue: str, maxValue: str):
        self.minValue = minValue
        self.maxValue = maxValue
        
    @property
    def maxValue(self) -> str:
        return self.__maxValue

    @maxValue.setter
    def maxValue(self, maxValue: str):
        self.__maxValue = maxValue

    @property
    def minValue(self) -> str:
        return self.__minValue

    @minValue.setter
    def minValue(self, minValue: str):
        self.__minValue = minValue

class simple_csp_TypedElement(ABC):

    def __init__(self, type: str, simple_csp_TypedElement: "simple_csp_Domain" = None):
        self.type = type
        self.simple_csp_TypedElement = simple_csp_TypedElement
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def simple_csp_TypedElement(self):
        return self.__simple_csp_TypedElement

    @simple_csp_TypedElement.setter
    def simple_csp_TypedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simple_csp_TypedElement__simple_csp_TypedElement", None)
        self.__simple_csp_TypedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simple_csp_Domain8"):
                opp_val = getattr(old_value, "simple_csp_Domain8", None)
                if opp_val == self:
                    setattr(old_value, "simple_csp_Domain8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simple_csp_Domain8"):
                opp_val = getattr(value, "simple_csp_Domain8", None)
                setattr(value, "simple_csp_Domain8", self)

class BinaryOp:

    pass
class simple_csp_GreaterEqual(BinaryOp):

    pass
class simple_csp_LessEqual(BinaryOp):

    pass
class simple_csp_UnEqual(BinaryOp):

    pass
class simple_csp_Power(BinaryOp):

    pass
class simple_csp_Equal(BinaryOp):

    pass
class simple_csp_Times(BinaryOp):

    pass
class simple_csp_Plus(BinaryOp):

    pass
class simple_csp_Implies(BinaryOp):

    pass
class simple_csp_Less(BinaryOp):

    pass
class simple_csp_Minus(BinaryOp):

    pass
class simple_csp_Greater(BinaryOp):

    pass
class simple_csp_Or(BinaryOp):

    pass
class simple_csp_And(BinaryOp):

    pass
class UnaryOp:

    pass
class simple_csp_Not(UnaryOp):

    pass
class Operator:

    pass
class simple_csp_UnaryOp(Operator):

    pass
class simple_csp_BinaryOp(Operator):

    pass
class simple_csp_SetOp(Operator):

    pass
class Expression:

    pass
class simple_csp_BooleanLiteral(Expression):

    pass
class simple_csp_VarOccurence(Expression):

    pass
class simple_csp_Operator(Expression):

    pass
class simple_csp_Expression(ABC):

    pass
class TypedElement:

    pass
class DescribedElement:

    pass
class simple_csp_Domain(ABC):

    pass
class NamedElement:

    pass
class simple_csp_Goal(NamedElement):

    pass
class simple_csp_Constraint(NamedElement):

    pass
class simple_csp_Variable(TypedElement, DescribedElement, NamedElement):

    pass
class simple_csp_Problem(NamedElement):

    pass