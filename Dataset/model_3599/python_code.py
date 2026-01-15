from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class CardExpression:

    pass
class SMTlib2extended_CardLtExpression(CardExpression):

    pass
class SMTlib2extended_CardLeExpression(CardExpression):

    pass
class SMTlib2extended_CardGtExpression(CardExpression):

    pass
class SMTlib2extended_CardGeExpression(CardExpression):

    pass
class SMTlib2extended_CardEqExpression(CardExpression):

    pass
class UnaryExpression:

    pass
class SMTlib2extended_BvNotExpression(UnaryExpression):

    pass
class SMTlib2extended_OneHotExpression(UnaryExpression):

    pass
class SMTlib2extended_ExtractIndexExpression(UnaryExpression):

    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
        
    @property
    def end(self) -> int:
        return self.__end

    @end.setter
    def end(self, end: int):
        self.__end = end

    @property
    def start(self) -> int:
        return self.__start

    @start.setter
    def start(self, start: int):
        self.__start = start

class SMTlib2extended_NotExpression(UnaryExpression):

    pass
class BinaryExpression:

    pass
class SMTlib2extended_LessExpression(BinaryExpression):

    pass
class SMTlib2extended_ImpliesExpression(BinaryExpression):

    pass
class SMTlib2extended_SubExpression(BinaryExpression):

    pass
class SMTlib2extended_BvXorExpression(BinaryExpression):

    pass
class SMTlib2extended_GreaterEqualsExpression(BinaryExpression):

    pass
class SMTlib2extended_BvAndExpression(BinaryExpression):

    pass
class SMTlib2extended_GreaterExpression(BinaryExpression):

    pass
class SMTlib2extended_EqualsExpression(BinaryExpression):

    pass
class SMTlib2extended_NandExpression(BinaryExpression):

    pass
class SMTlib2extended_LessEqualsExpression(BinaryExpression):

    pass
class SMTlib2extended_DivExpression(BinaryExpression):

    pass
class SMTlib2extended_BvOrExpression(BinaryExpression):

    pass
class SMTlib2extended_MulExpression(BinaryExpression):

    pass
class SMTlib2extended_ModExpression(BinaryExpression):

    pass
class SMTlib2extended_AddExpression(BinaryExpression):

    pass
class NAryExpression:

    pass
class SMTlib2extended_AndExpression(NAryExpression):

    pass
class SMTlib2extended_OrExpression(NAryExpression):

    pass
class SMTlib2extended_ConcatExpression(NAryExpression):

    pass
class Variable:

    pass
class SMTlib2extended_Bitvector(Variable):

    def __init__(self, width: int):
        self.width = width
        
    @property
    def width(self) -> int:
        return self.__width

    @width.setter
    def width(self, width: int):
        self.__width = width

class SMTlib2extended_Predicate(Variable):

    pass
class NamedElement:

    pass
class SMTlib2extended_NamedElement:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class SMTlib2extended_Expression(NamedElement):

    pass
class SMTlib2extended_Variable(NamedElement):

    pass
class SMTlib2extended_Instance:

    pass
class ConstExpression:

    pass
class SMTlib2extended_BitstringExpression(ConstExpression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class SMTlib2extended_ConstIntegerExpression(ConstExpression):

    def __init__(self, value: int, width: int):
        self.value = value
        self.width = width
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def width(self) -> int:
        return self.__width

    @width.setter
    def width(self, width: int):
        self.__width = width

class SMTlib2extended_ConstBooleanExpression(ConstExpression):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class Expression:

    pass
class SMTlib2extended_NAryExpression(Expression):

    pass
class SMTlib2extended_UnaryExpression(Expression):

    pass
class SMTlib2extended_CardExpression(Expression):

    def __init__(self, k: int, SMTlib2extended_CardExpression: set["SMTlib2extended_Expression"] = None):
        self.k = k
        self.SMTlib2extended_CardExpression = SMTlib2extended_CardExpression if SMTlib2extended_CardExpression is not None else set()
        
    @property
    def k(self) -> int:
        return self.__k

    @k.setter
    def k(self, k: int):
        self.__k = k

    @property
    def SMTlib2extended_CardExpression(self):
        return self.__SMTlib2extended_CardExpression

    @SMTlib2extended_CardExpression.setter
    def SMTlib2extended_CardExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SMTlib2extended_CardExpression__SMTlib2extended_CardExpression", None)
        self.__SMTlib2extended_CardExpression = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SMTlib2extended_Expression23"):
                    opp_val = getattr(item, "SMTlib2extended_Expression23", None)
                    
                    if opp_val == self:
                        setattr(item, "SMTlib2extended_Expression23", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SMTlib2extended_Expression23"):
                    opp_val = getattr(item, "SMTlib2extended_Expression23", None)
                    
                    setattr(item, "SMTlib2extended_Expression23", self)
                    

class SMTlib2extended_BinaryExpression(Expression):

    pass
class SMTlib2extended_IteExpression(Expression):

    pass
class SMTlib2extended_ConstExpression(Expression):

    pass
class SMTlib2extended_VariableExpression(Expression):

    pass