from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class UnaryOp(Enum):
    NEGATE = "NEGATE"
    NOT = "NOT"
class BinaryOp(Enum):
    ADD = "ADD"
    SUB = "SUB"
    MUL = "MUL"
    LT = "LT"
    LEQ = "LEQ"
    EQ = "EQ"
    GEQ = "GEQ"
    GT = "GT"
    AND = "AND"
    OR = "OR"


############################################
# Definition of Classes
############################################

class Value:

    pass
class imp_BoolValue(Value):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class imp_IntValue(Value):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class imp_Value(ABC):

    pass
class imp_Store:

    pass
class Expr:

    pass
class imp_Binary(Expr):

    def __init__(self, op: str, imp_Binary: "imp_Expr" = None, imp_Binary20: "imp_Expr" = None):
        self.op = op
        self.imp_Binary = imp_Binary
        self.imp_Binary20 = imp_Binary20
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def imp_Binary20(self):
        return self.__imp_Binary20

    @imp_Binary20.setter
    def imp_Binary20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imp_Binary__imp_Binary20", None)
        self.__imp_Binary20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "imp_Expr21"):
                opp_val = getattr(old_value, "imp_Expr21", None)
                if opp_val == self:
                    setattr(old_value, "imp_Expr21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "imp_Expr21"):
                opp_val = getattr(value, "imp_Expr21", None)
                setattr(value, "imp_Expr21", self)

    @property
    def imp_Binary(self):
        return self.__imp_Binary

    @imp_Binary.setter
    def imp_Binary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imp_Binary__imp_Binary", None)
        self.__imp_Binary = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "imp_Expr18"):
                opp_val = getattr(old_value, "imp_Expr18", None)
                if opp_val == self:
                    setattr(old_value, "imp_Expr18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "imp_Expr18"):
                opp_val = getattr(value, "imp_Expr18", None)
                setattr(value, "imp_Expr18", self)

class imp_Var(Expr):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class imp_Unary(Expr):

    def __init__(self, op: str, imp_Unary: "imp_Expr" = None):
        self.op = op
        self.imp_Unary = imp_Unary
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def imp_Unary(self):
        return self.__imp_Unary

    @imp_Unary.setter
    def imp_Unary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imp_Unary__imp_Unary", None)
        self.__imp_Unary = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "imp_Expr16"):
                opp_val = getattr(old_value, "imp_Expr16", None)
                if opp_val == self:
                    setattr(old_value, "imp_Expr16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "imp_Expr16"):
                opp_val = getattr(value, "imp_Expr16", None)
                setattr(value, "imp_Expr16", self)

class imp_IntConst(Expr):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class imp_StringToValueMap:

    def __init__(self, key: str, imp_StringToValueMap: "imp_Store" = None, imp_StringToValueMap24: "imp_Value" = None):
        self.key = key
        self.imp_StringToValueMap = imp_StringToValueMap
        self.imp_StringToValueMap24 = imp_StringToValueMap24
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def imp_StringToValueMap(self):
        return self.__imp_StringToValueMap

    @imp_StringToValueMap.setter
    def imp_StringToValueMap(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imp_StringToValueMap__imp_StringToValueMap", None)
        self.__imp_StringToValueMap = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "imp_Store"):
                opp_val = getattr(old_value, "imp_Store", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "imp_Store"):
                opp_val = getattr(value, "imp_Store", None)
                if opp_val is None:
                    setattr(value, "imp_Store", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def imp_StringToValueMap24(self):
        return self.__imp_StringToValueMap24

    @imp_StringToValueMap24.setter
    def imp_StringToValueMap24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imp_StringToValueMap__imp_StringToValueMap24", None)
        self.__imp_StringToValueMap24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "imp_Value"):
                opp_val = getattr(old_value, "imp_Value", None)
                if opp_val == self:
                    setattr(old_value, "imp_Value", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "imp_Value"):
                opp_val = getattr(value, "imp_Value", None)
                setattr(value, "imp_Value", self)

class Stmt:

    pass
class imp_If(Stmt):

    pass
class imp_While(Stmt):

    pass
class imp_Block(Stmt):

    pass
class imp_Skip(Stmt):

    pass
class imp_Stmt(ABC):

    pass
class imp_Expr(ABC):

    pass
class imp_Assign(Stmt):

    def __init__(self, name: str, imp_Assign: "imp_Expr" = None):
        self.name = name
        self.imp_Assign = imp_Assign
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def imp_Assign(self):
        return self.__imp_Assign

    @imp_Assign.setter
    def imp_Assign(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imp_Assign__imp_Assign", None)
        self.__imp_Assign = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "imp_Expr"):
                opp_val = getattr(old_value, "imp_Expr", None)
                if opp_val == self:
                    setattr(old_value, "imp_Expr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "imp_Expr"):
                opp_val = getattr(value, "imp_Expr", None)
                setattr(value, "imp_Expr", self)
