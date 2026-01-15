from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class LExpression:

    pass
class expressions_Imply(LExpression):

    pass
class expressions_Not(LExpression):

    pass
class expressions_Or(LExpression):

    pass
class expressions_Xor(LExpression):

    pass
class expressions_And(LExpression):

    pass
class expressions_CExpression(LExpression):

    pass
class expressions_LExpression:

    pass
class expressions_Equivalent(LExpression):

    pass
class AExpression:

    pass
class expressions_Minus(AExpression):

    pass
class expressions_Pow(AExpression):

    pass
class expressions_Multi(AExpression):

    pass
class expressions_Mod(AExpression):

    pass
class expressions_Variable(AExpression, LExpression):

    def __init__(self, varName: str):
        self.varName = varName
        
    @property
    def varName(self) -> str:
        return self.__varName

    @varName.setter
    def varName(self, varName: str):
        self.__varName = varName

class expressions_Div(AExpression):

    pass
class expressions_Plus(AExpression):

    pass
class expressions_NumberValue(AExpression):

    def __init__(self, numValue: str):
        self.numValue = numValue
        
    @property
    def numValue(self) -> str:
        return self.__numValue

    @numValue.setter
    def numValue(self, numValue: str):
        self.__numValue = numValue

class SomeValue:

    pass
class expressions_StringValue(SomeValue):

    def __init__(self, strValue: str):
        self.strValue = strValue
        
    @property
    def strValue(self) -> str:
        return self.__strValue

    @strValue.setter
    def strValue(self, strValue: str):
        self.__strValue = strValue

class expressions_BooleanValue(SomeValue, LExpression):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class expressions_AExpression(SomeValue):

    pass
class CExpression:

    pass
class expressions_Unequal(CExpression):

    pass
class expressions_Greater(CExpression):

    pass
class expressions_Less(CExpression):

    pass
class expressions_Approx(CExpression):

    pass
class expressions_Equal(CExpression):

    pass
class expressions_LessOrEqual(CExpression):

    pass
class expressions_GreaterOrEqual(CExpression):

    pass
class expressions_SomeValue(CExpression):

    pass