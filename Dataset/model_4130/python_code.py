from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class mdsdassignment2_Exp:

    pass
class mdsdassignment2_MathExp:

    pass
class ExpOp:

    pass
class mdsdassignment2_Mult(ExpOp):

    pass
class mdsdassignment2_Sub(ExpOp):

    pass
class mdsdassignment2_Add(ExpOp):

    pass
class mdsdassignment2_Div(ExpOp):

    pass
class mdsdassignment2_Num(ExpOp):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class mdsdassignment2_Parenthesis(ExpOp):

    pass
class mdsdassignment2_ExpOp:

    pass