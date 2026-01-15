from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

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
class UnaryOp(Enum):
    NEGATE = "NEGATE"
    NOT = "NOT"


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

class imp_ArrayValue(Value):

    pass
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
class Expr:

    pass
class imp_Var(Expr):

    def __init__(self, name: str, imp_Var: "imp_Expr" = None):
        self.name = name
        self.imp_Var = imp_Var
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def imp_Var(self):
        return self.__imp_Var

    @imp_Var.setter
    def imp_Var(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imp_Var__imp_Var", None)
        self.__imp_Var = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "imp_Expr19"):
                opp_val = getattr(old_value, "imp_Expr19", None)
                if opp_val == self:
                    setattr(old_value, "imp_Expr19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "imp_Expr19"):
                opp_val = getattr(value, "imp_Expr19", None)
                setattr(value, "imp_Expr19", self)

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
            if hasattr(old_value, "imp_Expr21"):
                opp_val = getattr(old_value, "imp_Expr21", None)
                if opp_val == self:
                    setattr(old_value, "imp_Expr21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "imp_Expr21"):
                opp_val = getattr(value, "imp_Expr21", None)
                setattr(value, "imp_Expr21", self)

class imp_BoolConst(Expr):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class imp_ArrayDecl(Expr):

    pass
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

    def __init__(self, key: str, imp_StringToValueMap: "imp_Store" = None, imp_StringToValueMap29: "imp_Value" = None):
        self.key = key
        self.imp_StringToValueMap = imp_StringToValueMap
        self.imp_StringToValueMap29 = imp_StringToValueMap29
        
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
    def imp_StringToValueMap29(self):
        return self.__imp_StringToValueMap29

    @imp_StringToValueMap29.setter
    def imp_StringToValueMap29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imp_StringToValueMap__imp_StringToValueMap29", None)
        self.__imp_StringToValueMap29 = value
        
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

class imp_Store:

    pass
class imp_Binary(Expr):

    def __init__(self, op: str, imp_Binary: "imp_Expr" = None, imp_Binary25: "imp_Expr" = None):
        self.op = op
        self.imp_Binary = imp_Binary
        self.imp_Binary25 = imp_Binary25
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

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
            if hasattr(old_value, "imp_Expr23"):
                opp_val = getattr(old_value, "imp_Expr23", None)
                if opp_val == self:
                    setattr(old_value, "imp_Expr23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "imp_Expr23"):
                opp_val = getattr(value, "imp_Expr23", None)
                setattr(value, "imp_Expr23", self)

    @property
    def imp_Binary25(self):
        return self.__imp_Binary25

    @imp_Binary25.setter
    def imp_Binary25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imp_Binary__imp_Binary25", None)
        self.__imp_Binary25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "imp_Expr26"):
                opp_val = getattr(old_value, "imp_Expr26", None)
                if opp_val == self:
                    setattr(old_value, "imp_Expr26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "imp_Expr26"):
                opp_val = getattr(value, "imp_Expr26", None)
                setattr(value, "imp_Expr26", self)

class imp_Expr(ABC):

    pass
class Stmt:

    pass
class imp_Assign(Stmt):

    def __init__(self, name: str, imp_Assign: "imp_Expr" = None, imp_Assign2: "imp_Expr" = None):
        self.name = name
        self.imp_Assign = imp_Assign
        self.imp_Assign2 = imp_Assign2
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def imp_Assign2(self):
        return self.__imp_Assign2

    @imp_Assign2.setter
    def imp_Assign2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imp_Assign__imp_Assign2", None)
        self.__imp_Assign2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "imp_Expr3"):
                opp_val = getattr(old_value, "imp_Expr3", None)
                if opp_val == self:
                    setattr(old_value, "imp_Expr3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "imp_Expr3"):
                opp_val = getattr(value, "imp_Expr3", None)
                setattr(value, "imp_Expr3", self)

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

class imp_Block(Stmt):

    pass
class imp_If(Stmt):

    pass
class imp_While(Stmt):

    pass
class imp_Skip(Stmt):

    pass
class imp_Stmt(ABC):

    pass