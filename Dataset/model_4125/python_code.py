from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class ExpMD:

    pass
class assignment2_Div(ExpMD):

    pass
class assignment2_Mult(ExpMD):

    pass
class assignment2_MathExp:

    pass
class assignment2_Model:

    pass
class ExpPM:

    pass
class assignment2_Minus(ExpPM):

    pass
class assignment2_Plus(ExpPM):

    pass
class Primary:

    pass
class assignment2_Number(Primary):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class assignment2_Parenthesis(Primary):

    pass
class ExpMultDiv:

    pass
class assignment2_Exp(ExpMultDiv):

    pass
class assignment2_Primary(ExpMultDiv):

    pass
class assignment2_ExpMD:

    pass
class assignment2_ExpPM:

    pass
class assignment2_EObject:

    pass
class ExpMinusPlus:

    pass
class assignment2_ExpMultDiv(ExpMinusPlus):

    pass
class assignment2_ExpMinusPlus:

    pass