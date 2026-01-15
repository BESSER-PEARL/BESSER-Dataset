from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ArithmeticOperator(Enum):
    plus = "plus"
    minus = "minus"
    mult = "mult"
    div = "div"
class RelationalOperator(Enum):
    lessThan = "lessThan"
    greaterThan = "greaterThan"
    equals = "equals"
    notEqual = "notEqual"
    lessThanOrEqualTo = "lessThanOrEqualTo"
    greaterThanOrEqualTo = "greaterThanOrEqualTo"


############################################
# Definition of Classes
############################################

class Literal:

    pass
class kmLogo_StringLit(Literal):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class kmLogo_BoolLit(Literal):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class kmLogo_IntegerLit(Literal):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class Expression:

    pass
class kmLogo_ArithmeticExpression(Expression):

    def __init__(self, operator: str, kmLogo_ArithmeticExpression: "kmLogo_Expression" = None, kmLogo_ArithmeticExpression13: "kmLogo_Expression" = None):
        self.operator = operator
        self.kmLogo_ArithmeticExpression = kmLogo_ArithmeticExpression
        self.kmLogo_ArithmeticExpression13 = kmLogo_ArithmeticExpression13
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def kmLogo_ArithmeticExpression13(self):
        return self.__kmLogo_ArithmeticExpression13

    @kmLogo_ArithmeticExpression13.setter
    def kmLogo_ArithmeticExpression13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kmLogo_ArithmeticExpression__kmLogo_ArithmeticExpression13", None)
        self.__kmLogo_ArithmeticExpression13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kmLogo_Expression14"):
                opp_val = getattr(old_value, "kmLogo_Expression14", None)
                if opp_val == self:
                    setattr(old_value, "kmLogo_Expression14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kmLogo_Expression14"):
                opp_val = getattr(value, "kmLogo_Expression14", None)
                setattr(value, "kmLogo_Expression14", self)

    @property
    def kmLogo_ArithmeticExpression(self):
        return self.__kmLogo_ArithmeticExpression

    @kmLogo_ArithmeticExpression.setter
    def kmLogo_ArithmeticExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kmLogo_ArithmeticExpression__kmLogo_ArithmeticExpression", None)
        self.__kmLogo_ArithmeticExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kmLogo_Expression11"):
                opp_val = getattr(old_value, "kmLogo_Expression11", None)
                if opp_val == self:
                    setattr(old_value, "kmLogo_Expression11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kmLogo_Expression11"):
                opp_val = getattr(value, "kmLogo_Expression11", None)
                setattr(value, "kmLogo_Expression11", self)

class kmLogo_RelationalExpression(Expression):

    def __init__(self, operator: str, kmLogo_RelationalExpression: "kmLogo_Expression" = None, kmLogo_RelationalExpression18: "kmLogo_Expression" = None):
        self.operator = operator
        self.kmLogo_RelationalExpression = kmLogo_RelationalExpression
        self.kmLogo_RelationalExpression18 = kmLogo_RelationalExpression18
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def kmLogo_RelationalExpression18(self):
        return self.__kmLogo_RelationalExpression18

    @kmLogo_RelationalExpression18.setter
    def kmLogo_RelationalExpression18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kmLogo_RelationalExpression__kmLogo_RelationalExpression18", None)
        self.__kmLogo_RelationalExpression18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kmLogo_Expression19"):
                opp_val = getattr(old_value, "kmLogo_Expression19", None)
                if opp_val == self:
                    setattr(old_value, "kmLogo_Expression19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kmLogo_Expression19"):
                opp_val = getattr(value, "kmLogo_Expression19", None)
                setattr(value, "kmLogo_Expression19", self)

    @property
    def kmLogo_RelationalExpression(self):
        return self.__kmLogo_RelationalExpression

    @kmLogo_RelationalExpression.setter
    def kmLogo_RelationalExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kmLogo_RelationalExpression__kmLogo_RelationalExpression", None)
        self.__kmLogo_RelationalExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kmLogo_Expression16"):
                opp_val = getattr(old_value, "kmLogo_Expression16", None)
                if opp_val == self:
                    setattr(old_value, "kmLogo_Expression16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kmLogo_Expression16"):
                opp_val = getattr(value, "kmLogo_Expression16", None)
                setattr(value, "kmLogo_Expression16", self)

class kmLogo_VarReference(Expression):

    def __init__(self, key: str):
        self.key = key
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

class kmLogo_Literal(Expression):

    pass
class kmLogo_Expression(ABC):

    pass
class Primitive:

    pass
class kmLogo_PenDown(Primitive):

    pass
class kmLogo_Clear(Primitive):

    pass
class kmLogo_Left(Primitive):

    pass
class kmLogo_Forward(Primitive):

    pass
class kmLogo_PenUp(Primitive):

    pass
class kmLogo_Right(Primitive):

    pass
class kmLogo_Back(Primitive):

    pass
class Instruction:

    pass
class kmLogo_Primitive(Instruction):

    pass
class kmLogo_Instruction(ABC):

    pass
class kmLogo_VarDecl(Instruction):

    def __init__(self, key: str, kmLogo_VarDecl: "kmLogo_LogoProgram" = None, kmLogo_VarDecl21: "kmLogo_Expression" = None):
        self.key = key
        self.kmLogo_VarDecl = kmLogo_VarDecl
        self.kmLogo_VarDecl21 = kmLogo_VarDecl21
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def kmLogo_VarDecl21(self):
        return self.__kmLogo_VarDecl21

    @kmLogo_VarDecl21.setter
    def kmLogo_VarDecl21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kmLogo_VarDecl__kmLogo_VarDecl21", None)
        self.__kmLogo_VarDecl21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kmLogo_Expression22"):
                opp_val = getattr(old_value, "kmLogo_Expression22", None)
                if opp_val == self:
                    setattr(old_value, "kmLogo_Expression22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kmLogo_Expression22"):
                opp_val = getattr(value, "kmLogo_Expression22", None)
                setattr(value, "kmLogo_Expression22", self)

    @property
    def kmLogo_VarDecl(self):
        return self.__kmLogo_VarDecl

    @kmLogo_VarDecl.setter
    def kmLogo_VarDecl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kmLogo_VarDecl__kmLogo_VarDecl", None)
        self.__kmLogo_VarDecl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kmLogo_LogoProgram"):
                opp_val = getattr(old_value, "kmLogo_LogoProgram", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kmLogo_LogoProgram"):
                opp_val = getattr(value, "kmLogo_LogoProgram", None)
                if opp_val is None:
                    setattr(value, "kmLogo_LogoProgram", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class kmLogo_LogoProgram:

    pass