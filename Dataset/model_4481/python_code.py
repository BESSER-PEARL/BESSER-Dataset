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
class BooleanOperator(Enum):
    equal = "equal"
    diff = "diff"
    greaterThan = "greaterThan"
    lowerThan = "lowerThan"


############################################
# Definition of Classes
############################################

class ControlStructure:

    pass
class Logo_While(ControlStructure):

    pass
class Logo_Block(ControlStructure):

    pass
class Logo_If(ControlStructure):

    pass
class BinaryExpr:

    pass
class Logo_BooleanExpr(BinaryExpr):

    def __init__(self, operator: str):
        self.operator = operator
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

class Logo_ArithmeticExpr(BinaryExpr):

    def __init__(self, operator: str):
        self.operator = operator
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

class Primitive:

    pass
class Logo_Back(Primitive):

    pass
class Logo_Left(Primitive):

    pass
class Logo_Forward(Primitive):

    pass
class Instruction:

    pass
class Logo_Procedure(Instruction):

    def __init__(self, name: str, Logo_Procedure: "Logo_Block" = None, Logo_Procedure32: "Logo_Literal" = None, Logo_Procedure34: "Logo_ProcedureCall" = None):
        self.name = name
        self.Logo_Procedure = Logo_Procedure
        self.Logo_Procedure32 = Logo_Procedure32
        self.Logo_Procedure34 = Logo_Procedure34
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Logo_Procedure34(self):
        return self.__Logo_Procedure34

    @Logo_Procedure34.setter
    def Logo_Procedure34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Logo_Procedure__Logo_Procedure34", None)
        self.__Logo_Procedure34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Logo_ProcedureCall"):
                opp_val = getattr(old_value, "Logo_ProcedureCall", None)
                if opp_val == self:
                    setattr(old_value, "Logo_ProcedureCall", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Logo_ProcedureCall"):
                opp_val = getattr(value, "Logo_ProcedureCall", None)
                setattr(value, "Logo_ProcedureCall", self)

    @property
    def Logo_Procedure32(self):
        return self.__Logo_Procedure32

    @Logo_Procedure32.setter
    def Logo_Procedure32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Logo_Procedure__Logo_Procedure32", None)
        self.__Logo_Procedure32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Logo_Literal"):
                opp_val = getattr(old_value, "Logo_Literal", None)
                if opp_val == self:
                    setattr(old_value, "Logo_Literal", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Logo_Literal"):
                opp_val = getattr(value, "Logo_Literal", None)
                setattr(value, "Logo_Literal", self)

    @property
    def Logo_Procedure(self):
        return self.__Logo_Procedure

    @Logo_Procedure.setter
    def Logo_Procedure(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Logo_Procedure__Logo_Procedure", None)
        self.__Logo_Procedure = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Logo_Block30"):
                opp_val = getattr(old_value, "Logo_Block30", None)
                if opp_val == self:
                    setattr(old_value, "Logo_Block30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Logo_Block30"):
                opp_val = getattr(value, "Logo_Block30", None)
                setattr(value, "Logo_Block30", self)

class Logo_Assignation(Instruction):

    pass
class Logo_Expression(Instruction):

    pass
class Logo_ControlStructure(Instruction):

    pass
class Logo_Primitive(Instruction):

    pass
class Logo_Instruction(ABC):

    pass
class Logo_VarDecl(Instruction):

    def __init__(self, name: str, Logo_VarDecl: "Logo_Expression" = None, Logo_VarDecl11: "Logo_VarReference" = None, Logo_VarDecl36: "Logo_Assignation" = None):
        self.name = name
        self.Logo_VarDecl = Logo_VarDecl
        self.Logo_VarDecl11 = Logo_VarDecl11
        self.Logo_VarDecl36 = Logo_VarDecl36
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Logo_VarDecl(self):
        return self.__Logo_VarDecl

    @Logo_VarDecl.setter
    def Logo_VarDecl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Logo_VarDecl__Logo_VarDecl", None)
        self.__Logo_VarDecl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Logo_Expression9"):
                opp_val = getattr(old_value, "Logo_Expression9", None)
                if opp_val == self:
                    setattr(old_value, "Logo_Expression9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Logo_Expression9"):
                opp_val = getattr(value, "Logo_Expression9", None)
                setattr(value, "Logo_Expression9", self)

    @property
    def Logo_VarDecl36(self):
        return self.__Logo_VarDecl36

    @Logo_VarDecl36.setter
    def Logo_VarDecl36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Logo_VarDecl__Logo_VarDecl36", None)
        self.__Logo_VarDecl36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Logo_Assignation"):
                opp_val = getattr(old_value, "Logo_Assignation", None)
                if opp_val == self:
                    setattr(old_value, "Logo_Assignation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Logo_Assignation"):
                opp_val = getattr(value, "Logo_Assignation", None)
                setattr(value, "Logo_Assignation", self)

    @property
    def Logo_VarDecl11(self):
        return self.__Logo_VarDecl11

    @Logo_VarDecl11.setter
    def Logo_VarDecl11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Logo_VarDecl__Logo_VarDecl11", None)
        self.__Logo_VarDecl11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Logo_VarReference"):
                opp_val = getattr(old_value, "Logo_VarReference", None)
                if opp_val == self:
                    setattr(old_value, "Logo_VarReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Logo_VarReference"):
                opp_val = getattr(value, "Logo_VarReference", None)
                setattr(value, "Logo_VarReference", self)

class Literal:

    pass
class Logo_Void(Literal):

    pass
class Logo_Double(Literal):

    def __init__(self, value: float):
        self.value = value
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

class Logo_String(Literal):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class Logo_Boolean(Literal):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class Logo_Integer(Literal):

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
class Logo_ProcedureCall(Expression):

    pass
class Logo_BinaryExpr(Expression):

    pass
class Logo_VarReference(Expression):

    pass
class Logo_Literal(Expression):

    pass
class Logo_Right(Primitive):

    pass
class Logo_LogoProgram:

    pass