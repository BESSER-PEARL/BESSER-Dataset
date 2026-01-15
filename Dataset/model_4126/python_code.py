from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Primary:

    pass
class mathInterpeter_Number(Primary):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class mathInterpeter_Parenthesis(Primary):

    pass
class Exp:

    pass
class mathInterpeter_Minus(Exp):

    pass
class mathInterpeter_Plus(Exp):

    pass
class mathInterpeter_Primary(Exp):

    pass
class mathInterpeter_Div(Exp):

    pass
class mathInterpeter_Mult(Exp):

    pass
class mathInterpeter_Exp:

    pass
class mathInterpeter_MathExp:

    pass