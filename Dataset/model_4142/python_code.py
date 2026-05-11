from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Expression:

    pass
class arithmetics_Minus(Expression):

    pass
class arithmetics_Plus(Expression):

    pass
class arithmetics_Expression:

    pass
class arithmetics_Evaluation:

    pass
class arithmetics_NumberLiteral(Expression):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class arithmetics_Div(Expression):

    pass
class arithmetics_Multi(Expression):

    pass