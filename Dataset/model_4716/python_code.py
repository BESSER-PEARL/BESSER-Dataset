from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class UnaryExpression:

    pass
class core_UMinus(UnaryExpression):

    pass
class core_Not(UnaryExpression):

    pass
class IntegerExpression:

    pass
class core_Conditional(IntegerExpression):

    pass
class core_BinaryExpression(IntegerExpression):

    pass
class core_IntegerLiteral(IntegerExpression):

    def __init__(self, val: int):
        self.val = val
        
    @property
    def val(self) -> int:
        return self.__val

    @val.setter
    def val(self, val: int):
        self.__val = val

class core_UnaryExpression(IntegerExpression):

    pass
class BinaryExpression:

    pass
class core_Greater(BinaryExpression):

    pass
class core_Lower(BinaryExpression):

    pass
class core_Equal(BinaryExpression):

    pass
class core_Div(BinaryExpression):

    pass
class core_And(BinaryExpression):

    pass
class core_Minus(BinaryExpression):

    pass
class core_Mult(BinaryExpression):

    pass
class core_Mod(BinaryExpression):

    pass
class core_Or(BinaryExpression):

    pass
class core_Add(BinaryExpression):

    pass
class core_Filter(ABC):

    pass
class core_IntegerExpression(ABC):

    pass
class core_Rule:

    pass