from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class expression_ExpressionStatement:

    pass
class expression_Expression(ABC):

    def __init__(self, calculatedValue: float, expression_Expression: "expression_BinaryExpression" = None, expression_Expression3: "expression_BinaryExpression" = None, expression_Expression5: "expression_UnaryExpression" = None, expression_Expression7: "expression_ExpressionStatement" = None):
        self.calculatedValue = calculatedValue
        self.expression_Expression = expression_Expression
        self.expression_Expression3 = expression_Expression3
        self.expression_Expression5 = expression_Expression5
        self.expression_Expression7 = expression_Expression7
        
    @property
    def calculatedValue(self) -> float:
        return self.__calculatedValue

    @calculatedValue.setter
    def calculatedValue(self, calculatedValue: float):
        self.__calculatedValue = calculatedValue

    @property
    def expression_Expression3(self):
        return self.__expression_Expression3

    @expression_Expression3.setter
    def expression_Expression3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expression_Expression__expression_Expression3", None)
        self.__expression_Expression3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expression_BinaryExpression2"):
                opp_val = getattr(old_value, "expression_BinaryExpression2", None)
                if opp_val == self:
                    setattr(old_value, "expression_BinaryExpression2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expression_BinaryExpression2"):
                opp_val = getattr(value, "expression_BinaryExpression2", None)
                setattr(value, "expression_BinaryExpression2", self)

    @property
    def expression_Expression(self):
        return self.__expression_Expression

    @expression_Expression.setter
    def expression_Expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expression_Expression__expression_Expression", None)
        self.__expression_Expression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expression_BinaryExpression"):
                opp_val = getattr(old_value, "expression_BinaryExpression", None)
                if opp_val == self:
                    setattr(old_value, "expression_BinaryExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expression_BinaryExpression"):
                opp_val = getattr(value, "expression_BinaryExpression", None)
                setattr(value, "expression_BinaryExpression", self)

    @property
    def expression_Expression5(self):
        return self.__expression_Expression5

    @expression_Expression5.setter
    def expression_Expression5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expression_Expression__expression_Expression5", None)
        self.__expression_Expression5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expression_UnaryExpression"):
                opp_val = getattr(old_value, "expression_UnaryExpression", None)
                if opp_val == self:
                    setattr(old_value, "expression_UnaryExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expression_UnaryExpression"):
                opp_val = getattr(value, "expression_UnaryExpression", None)
                setattr(value, "expression_UnaryExpression", self)

    @property
    def expression_Expression7(self):
        return self.__expression_Expression7

    @expression_Expression7.setter
    def expression_Expression7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_expression_Expression__expression_Expression7", None)
        self.__expression_Expression7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "expression_ExpressionStatement"):
                opp_val = getattr(old_value, "expression_ExpressionStatement", None)
                if opp_val == self:
                    setattr(old_value, "expression_ExpressionStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "expression_ExpressionStatement"):
                opp_val = getattr(value, "expression_ExpressionStatement", None)
                setattr(value, "expression_ExpressionStatement", self)

class Expression:

    pass
class expression_BinaryExpression(Expression):

    pass
class expression_IntegerExpression(Expression):

    def __init__(self, value: float):
        self.value = value
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

class expression_UnaryExpression(Expression):

    pass