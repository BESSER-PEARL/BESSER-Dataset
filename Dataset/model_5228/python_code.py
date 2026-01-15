from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Operator(Enum):
    PLUS = "PLUS"
    MINUS = "MINUS"
    TIMES = "TIMES"
    LESS_THAN_OR_EQUAL_TO = "LESS_THAN_OR_EQUAL_TO"
    GREATER_THAN_OR_EQUAL_TO = "GREATER_THAN_OR_EQUAL_TO"
    EQUAL_TO = "EQUAL_TO"
class ILPDataType(Enum):
    BINARY = "BINARY"
    INTEGER = "INTEGER"
    REAL = "REAL"
class ObjectiveGoal(Enum):
    MIN = "MIN"
    MAX = "MAX"


############################################
# Definition of Classes
############################################

class Expression:

    pass
class ilp_LiteralExpression(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class ilp_Expression(ABC):

    def __init__(self, comment: str, ilp_Expression: "ilp_BinaryExpression" = None, ilp_Expression8: "ilp_BinaryExpression" = None, ilp_Expression13: "ilp_ObjectiveFunctionExpression" = None):
        self.comment = comment
        self.ilp_Expression = ilp_Expression
        self.ilp_Expression8 = ilp_Expression8
        self.ilp_Expression13 = ilp_Expression13
        
    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def ilp_Expression(self):
        return self.__ilp_Expression

    @ilp_Expression.setter
    def ilp_Expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ilp_Expression__ilp_Expression", None)
        self.__ilp_Expression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ilp_BinaryExpression"):
                opp_val = getattr(old_value, "ilp_BinaryExpression", None)
                if opp_val == self:
                    setattr(old_value, "ilp_BinaryExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ilp_BinaryExpression"):
                opp_val = getattr(value, "ilp_BinaryExpression", None)
                setattr(value, "ilp_BinaryExpression", self)

    @property
    def ilp_Expression13(self):
        return self.__ilp_Expression13

    @ilp_Expression13.setter
    def ilp_Expression13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ilp_Expression__ilp_Expression13", None)
        self.__ilp_Expression13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ilp_ObjectiveFunctionExpression12"):
                opp_val = getattr(old_value, "ilp_ObjectiveFunctionExpression12", None)
                if opp_val == self:
                    setattr(old_value, "ilp_ObjectiveFunctionExpression12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ilp_ObjectiveFunctionExpression12"):
                opp_val = getattr(value, "ilp_ObjectiveFunctionExpression12", None)
                setattr(value, "ilp_ObjectiveFunctionExpression12", self)

    @property
    def ilp_Expression8(self):
        return self.__ilp_Expression8

    @ilp_Expression8.setter
    def ilp_Expression8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ilp_Expression__ilp_Expression8", None)
        self.__ilp_Expression8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ilp_BinaryExpression7"):
                opp_val = getattr(old_value, "ilp_BinaryExpression7", None)
                if opp_val == self:
                    setattr(old_value, "ilp_BinaryExpression7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ilp_BinaryExpression7"):
                opp_val = getattr(value, "ilp_BinaryExpression7", None)
                setattr(value, "ilp_BinaryExpression7", self)

class ilp_VariableExpression(Expression):

    pass
class BinaryExpression:

    pass
class ilp_ArithmeticExpression(BinaryExpression):

    pass
class ilp_BinaryExpression(Expression):

    def __init__(self, operator: str, ilp_BinaryExpression: "ilp_Expression" = None, ilp_BinaryExpression7: "ilp_Expression" = None):
        self.operator = operator
        self.ilp_BinaryExpression = ilp_BinaryExpression
        self.ilp_BinaryExpression7 = ilp_BinaryExpression7
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def ilp_BinaryExpression(self):
        return self.__ilp_BinaryExpression

    @ilp_BinaryExpression.setter
    def ilp_BinaryExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ilp_BinaryExpression__ilp_BinaryExpression", None)
        self.__ilp_BinaryExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ilp_Expression"):
                opp_val = getattr(old_value, "ilp_Expression", None)
                if opp_val == self:
                    setattr(old_value, "ilp_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ilp_Expression"):
                opp_val = getattr(value, "ilp_Expression", None)
                setattr(value, "ilp_Expression", self)

    @property
    def ilp_BinaryExpression7(self):
        return self.__ilp_BinaryExpression7

    @ilp_BinaryExpression7.setter
    def ilp_BinaryExpression7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ilp_BinaryExpression__ilp_BinaryExpression7", None)
        self.__ilp_BinaryExpression7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ilp_Expression8"):
                opp_val = getattr(old_value, "ilp_Expression8", None)
                if opp_val == self:
                    setattr(old_value, "ilp_Expression8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ilp_Expression8"):
                opp_val = getattr(value, "ilp_Expression8", None)
                setattr(value, "ilp_Expression8", self)

class ilp_ObjectiveFunctionExpression:

    def __init__(self, goal: str, ilp_ObjectiveFunctionExpression: "ilp_IntegerLinearProgram" = None, ilp_ObjectiveFunctionExpression12: "ilp_Expression" = None):
        self.goal = goal
        self.ilp_ObjectiveFunctionExpression = ilp_ObjectiveFunctionExpression
        self.ilp_ObjectiveFunctionExpression12 = ilp_ObjectiveFunctionExpression12
        
    @property
    def goal(self) -> str:
        return self.__goal

    @goal.setter
    def goal(self, goal: str):
        self.__goal = goal

    @property
    def ilp_ObjectiveFunctionExpression(self):
        return self.__ilp_ObjectiveFunctionExpression

    @ilp_ObjectiveFunctionExpression.setter
    def ilp_ObjectiveFunctionExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ilp_ObjectiveFunctionExpression__ilp_ObjectiveFunctionExpression", None)
        self.__ilp_ObjectiveFunctionExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ilp_IntegerLinearProgram4"):
                opp_val = getattr(old_value, "ilp_IntegerLinearProgram4", None)
                if opp_val == self:
                    setattr(old_value, "ilp_IntegerLinearProgram4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ilp_IntegerLinearProgram4"):
                opp_val = getattr(value, "ilp_IntegerLinearProgram4", None)
                setattr(value, "ilp_IntegerLinearProgram4", self)

    @property
    def ilp_ObjectiveFunctionExpression12(self):
        return self.__ilp_ObjectiveFunctionExpression12

    @ilp_ObjectiveFunctionExpression12.setter
    def ilp_ObjectiveFunctionExpression12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ilp_ObjectiveFunctionExpression__ilp_ObjectiveFunctionExpression12", None)
        self.__ilp_ObjectiveFunctionExpression12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ilp_Expression13"):
                opp_val = getattr(old_value, "ilp_Expression13", None)
                if opp_val == self:
                    setattr(old_value, "ilp_Expression13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ilp_Expression13"):
                opp_val = getattr(value, "ilp_Expression13", None)
                setattr(value, "ilp_Expression13", self)

class ilp_ConstraintExpression(BinaryExpression):

    pass
class ilp_Variable:

    def __init__(self, dataType: str, name: str, ilp_Variable: "ilp_IntegerLinearProgram" = None, ilp_Variable10: "ilp_VariableExpression" = None):
        self.dataType = dataType
        self.name = name
        self.ilp_Variable = ilp_Variable
        self.ilp_Variable10 = ilp_Variable10
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dataType(self) -> str:
        return self.__dataType

    @dataType.setter
    def dataType(self, dataType: str):
        self.__dataType = dataType

    @property
    def ilp_Variable10(self):
        return self.__ilp_Variable10

    @ilp_Variable10.setter
    def ilp_Variable10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ilp_Variable__ilp_Variable10", None)
        self.__ilp_Variable10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ilp_VariableExpression"):
                opp_val = getattr(old_value, "ilp_VariableExpression", None)
                if opp_val == self:
                    setattr(old_value, "ilp_VariableExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ilp_VariableExpression"):
                opp_val = getattr(value, "ilp_VariableExpression", None)
                setattr(value, "ilp_VariableExpression", self)

    @property
    def ilp_Variable(self):
        return self.__ilp_Variable

    @ilp_Variable.setter
    def ilp_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ilp_Variable__ilp_Variable", None)
        self.__ilp_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ilp_IntegerLinearProgram"):
                opp_val = getattr(old_value, "ilp_IntegerLinearProgram", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ilp_IntegerLinearProgram"):
                opp_val = getattr(value, "ilp_IntegerLinearProgram", None)
                if opp_val is None:
                    setattr(value, "ilp_IntegerLinearProgram", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ilp_IntegerLinearProgram:

    pass