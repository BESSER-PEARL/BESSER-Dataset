from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Expression:

    pass
class myMath_Sub(Expression):

    pass
class myMath_Mult(Expression):

    pass
class myMath_Num(Expression):

    def __init__(self, value: int):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value


class myMath_Add(Expression):

    pass
class myMath_Expression:

    pass
class myMath_MathExp:

    pass
class myMath_Div(Expression):

    pass