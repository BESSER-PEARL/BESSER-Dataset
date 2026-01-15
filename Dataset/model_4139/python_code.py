from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Expression:

    pass
class mathDSL_NumberLiteral(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class mathDSL_Plus(Expression):

    pass
class mathDSL_Expression:

    pass
class mathDSL_Math:

    pass
class mathDSL_Div(Expression):

    pass
class mathDSL_Multi(Expression):

    pass
class mathDSL_Minus(Expression):

    pass