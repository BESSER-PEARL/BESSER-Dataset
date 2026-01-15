from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ArithmeticOperator(Enum):
    Add = "Add"
    Subtract = "Subtract"
    Multiply = "Multiply"
    Divide = "Divide"


############################################
# Definition of Classes
############################################

class Operand:

    pass
class ast_Number(Operand):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class ast_Variable(Operand):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class Expression:

    pass
class ast_Operand(Expression):

    pass
class ast_Operator(Expression):

    def __init__(self, op: str, Operator: "ast_Expression" = None, Operator4: "ast_Expression" = None, leftInverse: "ast_Expression" = None, rightInverse: "ast_Expression" = None):
        self.op = op
        self.Operator = Operator
        self.Operator4 = Operator4
        self.leftInverse = leftInverse
        self.rightInverse = rightInverse
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def Operator(self):
        return self.__Operator

    @Operator.setter
    def Operator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_Operator__Operator", None)
        self.__Operator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "left"):
                opp_val = getattr(old_value, "left", None)
                if opp_val == self:
                    setattr(old_value, "left", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "left"):
                opp_val = getattr(value, "left", None)
                setattr(value, "left", self)

    @property
    def Operator4(self):
        return self.__Operator4

    @Operator4.setter
    def Operator4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_Operator__Operator4", None)
        self.__Operator4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "right"):
                opp_val = getattr(old_value, "right", None)
                if opp_val == self:
                    setattr(old_value, "right", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "right"):
                opp_val = getattr(value, "right", None)
                setattr(value, "right", self)

    @property
    def rightInverse(self):
        return self.__rightInverse

    @rightInverse.setter
    def rightInverse(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_Operator__rightInverse", None)
        self.__rightInverse = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression8"):
                opp_val = getattr(old_value, "Expression8", None)
                if opp_val == self:
                    setattr(old_value, "Expression8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression8"):
                opp_val = getattr(value, "Expression8", None)
                setattr(value, "Expression8", self)

    @property
    def leftInverse(self):
        return self.__leftInverse

    @leftInverse.setter
    def leftInverse(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_Operator__leftInverse", None)
        self.__leftInverse = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression6"):
                opp_val = getattr(old_value, "Expression6", None)
                if opp_val == self:
                    setattr(old_value, "Expression6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression6"):
                opp_val = getattr(value, "Expression6", None)
                setattr(value, "Expression6", self)

class ast_Expression(ABC):

    def __init__(self, incrementalID: str, Expression: "ast_Model" = None, expr: "ast_Model" = None, left: "ast_Operator" = None, right: "ast_Operator" = None, Expression6: "ast_Operator" = None, Expression8: "ast_Operator" = None):
        self.incrementalID = incrementalID
        self.Expression = Expression
        self.expr = expr
        self.left = left
        self.right = right
        self.Expression6 = Expression6
        self.Expression8 = Expression8
        
    @property
    def incrementalID(self) -> str:
        return self.__incrementalID

    @incrementalID.setter
    def incrementalID(self, incrementalID: str):
        self.__incrementalID = incrementalID

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_Expression__right", None)
        self.__right = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Operator4"):
                opp_val = getattr(old_value, "Operator4", None)
                if opp_val == self:
                    setattr(old_value, "Operator4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Operator4"):
                opp_val = getattr(value, "Operator4", None)
                setattr(value, "Operator4", self)

    @property
    def Expression6(self):
        return self.__Expression6

    @Expression6.setter
    def Expression6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_Expression__Expression6", None)
        self.__Expression6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "leftInverse"):
                opp_val = getattr(old_value, "leftInverse", None)
                if opp_val == self:
                    setattr(old_value, "leftInverse", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "leftInverse"):
                opp_val = getattr(value, "leftInverse", None)
                setattr(value, "leftInverse", self)

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_Expression__left", None)
        self.__left = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Operator"):
                opp_val = getattr(old_value, "Operator", None)
                if opp_val == self:
                    setattr(old_value, "Operator", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Operator"):
                opp_val = getattr(value, "Operator", None)
                setattr(value, "Operator", self)

    @property
    def expr(self):
        return self.__expr

    @expr.setter
    def expr(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_Expression__expr", None)
        self.__expr = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Model"):
                opp_val = getattr(old_value, "Model", None)
                if opp_val == self:
                    setattr(old_value, "Model", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Model"):
                opp_val = getattr(value, "Model", None)
                setattr(value, "Model", self)

    @property
    def Expression8(self):
        return self.__Expression8

    @Expression8.setter
    def Expression8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_Expression__Expression8", None)
        self.__Expression8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rightInverse"):
                opp_val = getattr(old_value, "rightInverse", None)
                if opp_val == self:
                    setattr(old_value, "rightInverse", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rightInverse"):
                opp_val = getattr(value, "rightInverse", None)
                setattr(value, "rightInverse", self)

    @property
    def Expression(self):
        return self.__Expression

    @Expression.setter
    def Expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_Expression__Expression", None)
        self.__Expression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model"):
                opp_val = getattr(old_value, "model", None)
                if opp_val == self:
                    setattr(old_value, "model", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model"):
                opp_val = getattr(value, "model", None)
                setattr(value, "model", self)

class ast_Model:

    pass