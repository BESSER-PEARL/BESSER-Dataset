from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class expressions_Model:

    pass
class UnaryOperator:

    pass
class expressions_Neg(UnaryOperator):

    pass
class BinaryOperator:

    pass
class expressions_Or(BinaryOperator):

    pass
class expressions_And(BinaryOperator):

    pass
class expressions_Implies(BinaryOperator):

    pass
class expressions_Any(UnaryOperator):

    pass
class expressions_Number(UnaryOperator):

    pass
class expressions_All(UnaryOperator):

    pass
class Expression:

    pass
class expressions_Feature(Expression):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class expressions_UnaryOperator(Expression):

    pass
class expressions_BinaryOperator(Expression):

    pass
class expressions_Expression(ABC):

    pass