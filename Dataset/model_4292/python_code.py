from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Expression:

    pass
class expression_SubExpression2(Expression):

    pass
class expression_SubExpression(Expression):

    pass
class SubExpression2:

    pass
class expression_NegativeIntExpression(SubExpression2):

    def __init__(self, value: str, isNegative: str):
        self.value = value
        self.isNegative = isNegative
        
        pass
    @property
    def isNegative(self):
        return self.__isNegative

    @isNegative.setter
    def isNegative(self, isNegative: str):
        self.__isNegative = isNegative


    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class expression_StringExpression(SubExpression2):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class expression_ExpressionList:

    pass
class expression_Expression(ABC):

    pass
class SubExpression:

    pass
class expression_BooleanExpression(SubExpression):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class expression_IncludingExpression(SubExpression):

    pass