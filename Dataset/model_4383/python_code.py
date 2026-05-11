from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class minilang_While:

    pass
class minilang_Block:

    pass
class Statement:

    pass
class minilang_IntAssignment(Statement):

    pass
class minilang_PrintStr(Statement):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class minilang_PrintVar(Statement):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class minilang_BooleanAssignment(Statement):

    pass
class minilang_Statement:

    pass
class minilang_VariableRef:

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class VariableRef:

    pass
class IntOperation:

    pass
class minilang_Divide(IntOperation):

    pass
class minilang_Multiply(IntOperation):

    pass
class minilang_Minus(IntOperation):

    pass
class minilang_Plus(IntOperation):

    pass
class BooleanOperation:

    pass
class minilang_And(BooleanOperation):

    pass
class minilang_Or(BooleanOperation):

    pass
class minilang_BooleanExpression:

    pass
class minilang_If:

    pass
class IntComparison:

    pass
class minilang_Greater(IntComparison):

    pass
class minilang_LessOrEqual(IntComparison):

    pass
class minilang_Equal(IntComparison):

    pass
class BooleanExpression:

    pass
class minilang_Not(BooleanExpression):

    pass
class minilang_BooleanVariableRef(VariableRef, BooleanExpression):

    pass
class minilang_IntComparison(BooleanExpression):

    pass
class minilang_BooleanOperation(BooleanExpression):

    pass
class minilang_Boolean(BooleanExpression):

    def __init__(self, value: bool):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value


class IntExpression:

    pass
class minilang_IntOperation(IntExpression):

    pass
class minilang_IntVariableRef(VariableRef, IntExpression):

    pass
class minilang_Integer(IntExpression):

    def __init__(self, value: int):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value


class minilang_IntExpression:

    pass
class minilang_Less(IntComparison):

    pass
class minilang_GreaterOrEqual(IntComparison):

    pass