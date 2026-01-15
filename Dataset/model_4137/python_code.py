from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Expression:

    pass
class mathInterpreter_Divide(Expression):

    pass
class mathInterpreter_Minus(Expression):

    pass
class mathInterpreter_Num(Expression):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class mathInterpreter_Plus(Expression):

    pass
class mathInterpreter_Multiply(Expression):

    pass
class mathInterpreter_Exp(Expression):

    pass
class mathInterpreter_Expression:

    pass
class mathInterpreter_MathExp:

    pass