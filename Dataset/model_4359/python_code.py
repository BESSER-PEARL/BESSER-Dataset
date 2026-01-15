from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Statement:

    pass
class simple_lang_WhileStatement(Statement):

    pass
class simple_lang_IfStatement(Statement):

    pass
class simple_lang_AssignmentStatement(Statement):

    pass
class simple_lang_ExpressionStatement(Statement):

    pass
class FeatureCallExpression:

    pass
class simple_lang_PropertyCallExpression(FeatureCallExpression):

    pass
class simple_lang_MethodCallExpression(FeatureCallExpression):

    pass
class BinaryExpression:

    pass
class simple_lang_ComparisonExpression(BinaryExpression):

    pass
class simple_lang_ArithmeticExpression(BinaryExpression):

    pass
class simple_lang_LogicalExpression(BinaryExpression):

    pass
class Expression:

    pass
class simple_lang_FeatureCallExpression(Expression):

    def __init__(self, name: str, simple_lang_FeatureCallExpression: "simple_lang_Expression" = None):
        self.name = name
        self.simple_lang_FeatureCallExpression = simple_lang_FeatureCallExpression
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def simple_lang_FeatureCallExpression(self):
        return self.__simple_lang_FeatureCallExpression

    @simple_lang_FeatureCallExpression.setter
    def simple_lang_FeatureCallExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simple_lang_FeatureCallExpression__simple_lang_FeatureCallExpression", None)
        self.__simple_lang_FeatureCallExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simple_lang_Expression8"):
                opp_val = getattr(old_value, "simple_lang_Expression8", None)
                if opp_val == self:
                    setattr(old_value, "simple_lang_Expression8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simple_lang_Expression8"):
                opp_val = getattr(value, "simple_lang_Expression8", None)
                setattr(value, "simple_lang_Expression8", self)

class simple_lang_BinaryExpression(Expression):

    def __init__(self, operator: str, simple_lang_BinaryExpression: "simple_lang_Expression" = None, simple_lang_BinaryExpression5: "simple_lang_Expression" = None):
        self.operator = operator
        self.simple_lang_BinaryExpression = simple_lang_BinaryExpression
        self.simple_lang_BinaryExpression5 = simple_lang_BinaryExpression5
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def simple_lang_BinaryExpression5(self):
        return self.__simple_lang_BinaryExpression5

    @simple_lang_BinaryExpression5.setter
    def simple_lang_BinaryExpression5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simple_lang_BinaryExpression__simple_lang_BinaryExpression5", None)
        self.__simple_lang_BinaryExpression5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simple_lang_Expression6"):
                opp_val = getattr(old_value, "simple_lang_Expression6", None)
                if opp_val == self:
                    setattr(old_value, "simple_lang_Expression6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simple_lang_Expression6"):
                opp_val = getattr(value, "simple_lang_Expression6", None)
                setattr(value, "simple_lang_Expression6", self)

    @property
    def simple_lang_BinaryExpression(self):
        return self.__simple_lang_BinaryExpression

    @simple_lang_BinaryExpression.setter
    def simple_lang_BinaryExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simple_lang_BinaryExpression__simple_lang_BinaryExpression", None)
        self.__simple_lang_BinaryExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simple_lang_Expression3"):
                opp_val = getattr(old_value, "simple_lang_Expression3", None)
                if opp_val == self:
                    setattr(old_value, "simple_lang_Expression3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simple_lang_Expression3"):
                opp_val = getattr(value, "simple_lang_Expression3", None)
                setattr(value, "simple_lang_Expression3", self)

class simple_lang_Type:

    pass
class simple_lang_Expression(ABC):

    pass
class simple_lang_Statement(ABC):

    pass
class simple_lang_SimpleLang:

    pass