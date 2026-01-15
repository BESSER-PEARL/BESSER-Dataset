from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class SubExpression2:

    pass
class expression_StringExpression(SubExpression2):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class expression_ExpressionList:

    pass
class Expression:

    pass
class expression_SubExpression2(Expression):

    pass
class expression_SubExpression(Expression):

    pass
class expression_NegativeIntExpression(SubExpression2):

    def __init__(self, value: str, isNegative: str):
        self.value = value
        self.isNegative = isNegative
        
    @property
    def isNegative(self) -> str:
        return self.__isNegative

    @isNegative.setter
    def isNegative(self, isNegative: str):
        self.__isNegative = isNegative

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class expression_Expression(ABC):

    pass
class SubExpression:

    pass
class expression_BooleanExpression(SubExpression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class expression_IncludingExpression(SubExpression):

    pass