from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class BinaryExp:

    pass
class rules_core_Equals(BinaryExp):

    pass
class rules_core_Lower(BinaryExp):

    pass
class rules_core_Plus(BinaryExp):

    pass
class Expression:

    pass
class rules_core_Constant(Expression):

    def __init__(self, integerValue: int):
        self.integerValue = integerValue
        
    @property
    def integerValue(self) -> int:
        return self.__integerValue

    @integerValue.setter
    def integerValue(self, integerValue: int):
        self.__integerValue = integerValue

class rules_core_If(Expression):

    pass
class rules_core_BinaryExp(Expression):

    pass
class rules_core_Filter:

    pass
class rules_core_Rule:

    pass
class rules_core_Expression(ABC):

    pass
class rules_core_Greater(BinaryExp):

    pass
class rules_core_Min(BinaryExp):

    pass
class rules_core_Max(BinaryExp):

    pass
class rules_core_Div(BinaryExp):

    pass
class rules_core_Mult(BinaryExp):

    pass
class rules_core_Minus(BinaryExp):

    pass