from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Exp:

    pass
class mathAssignmentLanguage_Parenthesis(Exp):

    pass
class mathAssignmentLanguage_Number(Exp):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class ExpOp:

    pass
class mathAssignmentLanguage_Minus(ExpOp):

    pass
class mathAssignmentLanguage_Plus(ExpOp):

    pass
class mathAssignmentLanguage_Div(ExpOp):

    pass
class mathAssignmentLanguage_Mult(ExpOp):

    pass
class mathAssignmentLanguage_Exp:

    pass
class mathAssignmentLanguage_MathExp:

    pass
class mathAssignmentLanguage_ExpOp:

    pass