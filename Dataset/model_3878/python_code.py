from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ETwoOperator(Enum):
    GE = "GE"
    LE = "LE"
    OR = "OR"
    AND = "AND"
    XOR = "XOR"
    MINUS = "MINUS"
    PLUS = "PLUS"
    TIMES = "TIMES"
    DEVIDE = "DEVIDE"
    EQUAL = "EQUAL"
    NOT_EQUAL = "NOT_EQUAL"
    GT = "GT"
    LT = "LT"
class EBaseType(Enum):
    INT = "INT"
    BOOL = "BOOL"
    CHAR = "CHAR"
class EOneOperator(Enum):
    MINUS = "MINUS"
    NOT = "NOT"


############################################
# Definition of Classes
############################################

class Expression:

    pass
class dinkiemodel_ArrayExpr(Expression):

    def __init__(self, varName: str, dinkiemodel_ArrayExpr: "dinkiemodel_Expression" = None):
        self.varName = varName
        self.dinkiemodel_ArrayExpr = dinkiemodel_ArrayExpr
        
    @property
    def varName(self) -> str:
        return self.__varName

    @varName.setter
    def varName(self, varName: str):
        self.__varName = varName

    @property
    def dinkiemodel_ArrayExpr(self):
        return self.__dinkiemodel_ArrayExpr

    @dinkiemodel_ArrayExpr.setter
    def dinkiemodel_ArrayExpr(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dinkiemodel_ArrayExpr__dinkiemodel_ArrayExpr", None)
        self.__dinkiemodel_ArrayExpr = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dinkiemodel_Expression69"):
                opp_val = getattr(old_value, "dinkiemodel_Expression69", None)
                if opp_val == self:
                    setattr(old_value, "dinkiemodel_Expression69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dinkiemodel_Expression69"):
                opp_val = getattr(value, "dinkiemodel_Expression69", None)
                setattr(value, "dinkiemodel_Expression69", self)

class dinkiemodel_OneOperator(Expression):

    def __init__(self, operator: str, dinkiemodel_OneOperator: "dinkiemodel_Expression" = None):
        self.operator = operator
        self.dinkiemodel_OneOperator = dinkiemodel_OneOperator
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def dinkiemodel_OneOperator(self):
        return self.__dinkiemodel_OneOperator

    @dinkiemodel_OneOperator.setter
    def dinkiemodel_OneOperator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dinkiemodel_OneOperator__dinkiemodel_OneOperator", None)
        self.__dinkiemodel_OneOperator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dinkiemodel_Expression60"):
                opp_val = getattr(old_value, "dinkiemodel_Expression60", None)
                if opp_val == self:
                    setattr(old_value, "dinkiemodel_Expression60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dinkiemodel_Expression60"):
                opp_val = getattr(value, "dinkiemodel_Expression60", None)
                setattr(value, "dinkiemodel_Expression60", self)

class dinkiemodel_VariableExpr(Expression):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class dinkiemodel_ThreadID(Expression):

    pass
class dinkiemodel_BoolVal(Expression):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class dinkiemodel_TwoOperator(Expression):

    def __init__(self, operator: str, dinkiemodel_TwoOperator: "dinkiemodel_Expression" = None, dinkiemodel_TwoOperator64: "dinkiemodel_Expression" = None):
        self.operator = operator
        self.dinkiemodel_TwoOperator = dinkiemodel_TwoOperator
        self.dinkiemodel_TwoOperator64 = dinkiemodel_TwoOperator64
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def dinkiemodel_TwoOperator(self):
        return self.__dinkiemodel_TwoOperator

    @dinkiemodel_TwoOperator.setter
    def dinkiemodel_TwoOperator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dinkiemodel_TwoOperator__dinkiemodel_TwoOperator", None)
        self.__dinkiemodel_TwoOperator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dinkiemodel_Expression62"):
                opp_val = getattr(old_value, "dinkiemodel_Expression62", None)
                if opp_val == self:
                    setattr(old_value, "dinkiemodel_Expression62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dinkiemodel_Expression62"):
                opp_val = getattr(value, "dinkiemodel_Expression62", None)
                setattr(value, "dinkiemodel_Expression62", self)

    @property
    def dinkiemodel_TwoOperator64(self):
        return self.__dinkiemodel_TwoOperator64

    @dinkiemodel_TwoOperator64.setter
    def dinkiemodel_TwoOperator64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dinkiemodel_TwoOperator__dinkiemodel_TwoOperator64", None)
        self.__dinkiemodel_TwoOperator64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dinkiemodel_Expression65"):
                opp_val = getattr(old_value, "dinkiemodel_Expression65", None)
                if opp_val == self:
                    setattr(old_value, "dinkiemodel_Expression65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dinkiemodel_Expression65"):
                opp_val = getattr(value, "dinkiemodel_Expression65", None)
                setattr(value, "dinkiemodel_Expression65", self)

class dinkiemodel_Character(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class dinkiemodel_BracketExpr(Expression):

    pass
class dinkiemodel_Number(Expression):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class Type:

    pass
class dinkiemodel_ArrayType(Type):

    def __init__(self, arrayType: str, dinkiemodel_ArrayType: "dinkiemodel_EmptyArrayDecl" = None, dinkiemodel_ArrayType26: "dinkiemodel_FilledArrayDecl" = None):
        self.arrayType = arrayType
        self.dinkiemodel_ArrayType = dinkiemodel_ArrayType
        self.dinkiemodel_ArrayType26 = dinkiemodel_ArrayType26
        
    @property
    def arrayType(self) -> str:
        return self.__arrayType

    @arrayType.setter
    def arrayType(self, arrayType: str):
        self.__arrayType = arrayType

    @property
    def dinkiemodel_ArrayType26(self):
        return self.__dinkiemodel_ArrayType26

    @dinkiemodel_ArrayType26.setter
    def dinkiemodel_ArrayType26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dinkiemodel_ArrayType__dinkiemodel_ArrayType26", None)
        self.__dinkiemodel_ArrayType26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dinkiemodel_FilledArrayDecl"):
                opp_val = getattr(old_value, "dinkiemodel_FilledArrayDecl", None)
                if opp_val == self:
                    setattr(old_value, "dinkiemodel_FilledArrayDecl", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dinkiemodel_FilledArrayDecl"):
                opp_val = getattr(value, "dinkiemodel_FilledArrayDecl", None)
                setattr(value, "dinkiemodel_FilledArrayDecl", self)

    @property
    def dinkiemodel_ArrayType(self):
        return self.__dinkiemodel_ArrayType

    @dinkiemodel_ArrayType.setter
    def dinkiemodel_ArrayType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dinkiemodel_ArrayType__dinkiemodel_ArrayType", None)
        self.__dinkiemodel_ArrayType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dinkiemodel_EmptyArrayDecl"):
                opp_val = getattr(old_value, "dinkiemodel_EmptyArrayDecl", None)
                if opp_val == self:
                    setattr(old_value, "dinkiemodel_EmptyArrayDecl", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dinkiemodel_EmptyArrayDecl"):
                opp_val = getattr(value, "dinkiemodel_EmptyArrayDecl", None)
                setattr(value, "dinkiemodel_EmptyArrayDecl", self)

class dinkiemodel_Expression(ABC):

    pass
class dinkiemodel_BaseType(Type):

    def __init__(self, type: str, dinkiemodel_BaseType17: "dinkiemodel_ReadStatement" = None, dinkiemodel_BaseType: "dinkiemodel_Declaration" = None):
        self.type = type
        self.dinkiemodel_BaseType17 = dinkiemodel_BaseType17
        self.dinkiemodel_BaseType = dinkiemodel_BaseType
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def dinkiemodel_BaseType(self):
        return self.__dinkiemodel_BaseType

    @dinkiemodel_BaseType.setter
    def dinkiemodel_BaseType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dinkiemodel_BaseType__dinkiemodel_BaseType", None)
        self.__dinkiemodel_BaseType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dinkiemodel_Declaration"):
                opp_val = getattr(old_value, "dinkiemodel_Declaration", None)
                if opp_val == self:
                    setattr(old_value, "dinkiemodel_Declaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dinkiemodel_Declaration"):
                opp_val = getattr(value, "dinkiemodel_Declaration", None)
                setattr(value, "dinkiemodel_Declaration", self)

    @property
    def dinkiemodel_BaseType17(self):
        return self.__dinkiemodel_BaseType17

    @dinkiemodel_BaseType17.setter
    def dinkiemodel_BaseType17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dinkiemodel_BaseType__dinkiemodel_BaseType17", None)
        self.__dinkiemodel_BaseType17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dinkiemodel_ReadStatement"):
                opp_val = getattr(old_value, "dinkiemodel_ReadStatement", None)
                if opp_val == self:
                    setattr(old_value, "dinkiemodel_ReadStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dinkiemodel_ReadStatement"):
                opp_val = getattr(value, "dinkiemodel_ReadStatement", None)
                setattr(value, "dinkiemodel_ReadStatement", self)

class Statement:

    pass
class dinkiemodel_EmptyArrayDecl(Statement):

    def __init__(self, size: int, global: bool, varName: str, dinkiemodel_EmptyArrayDecl: "dinkiemodel_ArrayType" = None):
        self.size = size
        self.global = global
        self.varName = varName
        self.dinkiemodel_EmptyArrayDecl = dinkiemodel_EmptyArrayDecl
        
    @property
    def varName(self) -> str:
        return self.__varName

    @varName.setter
    def varName(self, varName: str):
        self.__varName = varName

    @property
    def global(self) -> bool:
        return self.__global

    @global.setter
    def global(self, global: bool):
        self.__global = global

    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, size: int):
        self.__size = size

    @property
    def dinkiemodel_EmptyArrayDecl(self):
        return self.__dinkiemodel_EmptyArrayDecl

    @dinkiemodel_EmptyArrayDecl.setter
    def dinkiemodel_EmptyArrayDecl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dinkiemodel_EmptyArrayDecl__dinkiemodel_EmptyArrayDecl", None)
        self.__dinkiemodel_EmptyArrayDecl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dinkiemodel_ArrayType"):
                opp_val = getattr(old_value, "dinkiemodel_ArrayType", None)
                if opp_val == self:
                    setattr(old_value, "dinkiemodel_ArrayType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dinkiemodel_ArrayType"):
                opp_val = getattr(value, "dinkiemodel_ArrayType", None)
                setattr(value, "dinkiemodel_ArrayType", self)

class dinkiemodel_Assign(Statement):

    def __init__(self, varName: str, dinkiemodel_Assign: "dinkiemodel_Expression" = None):
        self.varName = varName
        self.dinkiemodel_Assign = dinkiemodel_Assign
        
    @property
    def varName(self) -> str:
        return self.__varName

    @varName.setter
    def varName(self, varName: str):
        self.__varName = varName

    @property
    def dinkiemodel_Assign(self):
        return self.__dinkiemodel_Assign

    @dinkiemodel_Assign.setter
    def dinkiemodel_Assign(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dinkiemodel_Assign__dinkiemodel_Assign", None)
        self.__dinkiemodel_Assign = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dinkiemodel_Expression24"):
                opp_val = getattr(old_value, "dinkiemodel_Expression24", None)
                if opp_val == self:
                    setattr(old_value, "dinkiemodel_Expression24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dinkiemodel_Expression24"):
                opp_val = getattr(value, "dinkiemodel_Expression24", None)
                setattr(value, "dinkiemodel_Expression24", self)

class dinkiemodel_Return(Statement):

    pass
class dinkiemodel_While(Statement):

    pass
class dinkiemodel_IfTwo(Statement):

    pass
class dinkiemodel_IfOne(Statement):

    pass
class dinkiemodel_StringArrayDecl(Statement):

    def __init__(self, global: bool, varName: str, content: str):
        self.global = global
        self.varName = varName
        self.content = content
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def global(self) -> bool:
        return self.__global

    @global.setter
    def global(self, global: bool):
        self.__global = global

    @property
    def varName(self) -> str:
        return self.__varName

    @varName.setter
    def varName(self, varName: str):
        self.__varName = varName

class dinkiemodel_Sync(Statement):

    def __init__(self, varName: str, dinkiemodel_Sync: set["dinkiemodel_Statement"] = None):
        self.varName = varName
        self.dinkiemodel_Sync = dinkiemodel_Sync if dinkiemodel_Sync is not None else set()
        
    @property
    def varName(self) -> str:
        return self.__varName

    @varName.setter
    def varName(self, varName: str):
        self.__varName = varName

    @property
    def dinkiemodel_Sync(self):
        return self.__dinkiemodel_Sync

    @dinkiemodel_Sync.setter
    def dinkiemodel_Sync(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dinkiemodel_Sync__dinkiemodel_Sync", None)
        self.__dinkiemodel_Sync = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dinkiemodel_Statement56"):
                    opp_val = getattr(item, "dinkiemodel_Statement56", None)
                    
                    if opp_val == self:
                        setattr(item, "dinkiemodel_Statement56", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dinkiemodel_Statement56"):
                    opp_val = getattr(item, "dinkiemodel_Statement56", None)
                    
                    setattr(item, "dinkiemodel_Statement56", self)
                    

class dinkiemodel_FuncExpr(Expression, Statement):

    def __init__(self, funcName: str, dinkiemodel_FuncExpr: set["dinkiemodel_Expression"] = None):
        self.funcName = funcName
        self.dinkiemodel_FuncExpr = dinkiemodel_FuncExpr if dinkiemodel_FuncExpr is not None else set()
        
    @property
    def funcName(self) -> str:
        return self.__funcName

    @funcName.setter
    def funcName(self, funcName: str):
        self.__funcName = funcName

    @property
    def dinkiemodel_FuncExpr(self):
        return self.__dinkiemodel_FuncExpr

    @dinkiemodel_FuncExpr.setter
    def dinkiemodel_FuncExpr(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dinkiemodel_FuncExpr__dinkiemodel_FuncExpr", None)
        self.__dinkiemodel_FuncExpr = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dinkiemodel_Expression71"):
                    opp_val = getattr(item, "dinkiemodel_Expression71", None)
                    
                    if opp_val == self:
                        setattr(item, "dinkiemodel_Expression71", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dinkiemodel_Expression71"):
                    opp_val = getattr(item, "dinkiemodel_Expression71", None)
                    
                    setattr(item, "dinkiemodel_Expression71", self)
                    

class dinkiemodel_ArrayAssign(Statement):

    def __init__(self, varName: str, dinkiemodel_ArrayAssign: "dinkiemodel_Expression" = None, dinkiemodel_ArrayAssign33: "dinkiemodel_Expression" = None):
        self.varName = varName
        self.dinkiemodel_ArrayAssign = dinkiemodel_ArrayAssign
        self.dinkiemodel_ArrayAssign33 = dinkiemodel_ArrayAssign33
        
    @property
    def varName(self) -> str:
        return self.__varName

    @varName.setter
    def varName(self, varName: str):
        self.__varName = varName

    @property
    def dinkiemodel_ArrayAssign(self):
        return self.__dinkiemodel_ArrayAssign

    @dinkiemodel_ArrayAssign.setter
    def dinkiemodel_ArrayAssign(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dinkiemodel_ArrayAssign__dinkiemodel_ArrayAssign", None)
        self.__dinkiemodel_ArrayAssign = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dinkiemodel_Expression31"):
                opp_val = getattr(old_value, "dinkiemodel_Expression31", None)
                if opp_val == self:
                    setattr(old_value, "dinkiemodel_Expression31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dinkiemodel_Expression31"):
                opp_val = getattr(value, "dinkiemodel_Expression31", None)
                setattr(value, "dinkiemodel_Expression31", self)

    @property
    def dinkiemodel_ArrayAssign33(self):
        return self.__dinkiemodel_ArrayAssign33

    @dinkiemodel_ArrayAssign33.setter
    def dinkiemodel_ArrayAssign33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dinkiemodel_ArrayAssign__dinkiemodel_ArrayAssign33", None)
        self.__dinkiemodel_ArrayAssign33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dinkiemodel_Expression34"):
                opp_val = getattr(old_value, "dinkiemodel_Expression34", None)
                if opp_val == self:
                    setattr(old_value, "dinkiemodel_Expression34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dinkiemodel_Expression34"):
                opp_val = getattr(value, "dinkiemodel_Expression34", None)
                setattr(value, "dinkiemodel_Expression34", self)

class dinkiemodel_Parallel(Statement):

    def __init__(self, nrOfThreads: int, dinkiemodel_Parallel: set["dinkiemodel_Statement"] = None):
        self.nrOfThreads = nrOfThreads
        self.dinkiemodel_Parallel = dinkiemodel_Parallel if dinkiemodel_Parallel is not None else set()
        
    @property
    def nrOfThreads(self) -> int:
        return self.__nrOfThreads

    @nrOfThreads.setter
    def nrOfThreads(self, nrOfThreads: int):
        self.__nrOfThreads = nrOfThreads

    @property
    def dinkiemodel_Parallel(self):
        return self.__dinkiemodel_Parallel

    @dinkiemodel_Parallel.setter
    def dinkiemodel_Parallel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dinkiemodel_Parallel__dinkiemodel_Parallel", None)
        self.__dinkiemodel_Parallel = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dinkiemodel_Statement54"):
                    opp_val = getattr(item, "dinkiemodel_Statement54", None)
                    
                    if opp_val == self:
                        setattr(item, "dinkiemodel_Statement54", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dinkiemodel_Statement54"):
                    opp_val = getattr(item, "dinkiemodel_Statement54", None)
                    
                    setattr(item, "dinkiemodel_Statement54", self)
                    

class dinkiemodel_FilledArrayDecl(Statement):

    def __init__(self, global: bool, varName: str, dinkiemodel_FilledArrayDecl: "dinkiemodel_ArrayType" = None, dinkiemodel_FilledArrayDecl28: set["dinkiemodel_Expression"] = None):
        self.global = global
        self.varName = varName
        self.dinkiemodel_FilledArrayDecl = dinkiemodel_FilledArrayDecl
        self.dinkiemodel_FilledArrayDecl28 = dinkiemodel_FilledArrayDecl28 if dinkiemodel_FilledArrayDecl28 is not None else set()
        
    @property
    def global(self) -> bool:
        return self.__global

    @global.setter
    def global(self, global: bool):
        self.__global = global

    @property
    def varName(self) -> str:
        return self.__varName

    @varName.setter
    def varName(self, varName: str):
        self.__varName = varName

    @property
    def dinkiemodel_FilledArrayDecl(self):
        return self.__dinkiemodel_FilledArrayDecl

    @dinkiemodel_FilledArrayDecl.setter
    def dinkiemodel_FilledArrayDecl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dinkiemodel_FilledArrayDecl__dinkiemodel_FilledArrayDecl", None)
        self.__dinkiemodel_FilledArrayDecl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dinkiemodel_ArrayType26"):
                opp_val = getattr(old_value, "dinkiemodel_ArrayType26", None)
                if opp_val == self:
                    setattr(old_value, "dinkiemodel_ArrayType26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dinkiemodel_ArrayType26"):
                opp_val = getattr(value, "dinkiemodel_ArrayType26", None)
                setattr(value, "dinkiemodel_ArrayType26", self)

    @property
    def dinkiemodel_FilledArrayDecl28(self):
        return self.__dinkiemodel_FilledArrayDecl28

    @dinkiemodel_FilledArrayDecl28.setter
    def dinkiemodel_FilledArrayDecl28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dinkiemodel_FilledArrayDecl__dinkiemodel_FilledArrayDecl28", None)
        self.__dinkiemodel_FilledArrayDecl28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dinkiemodel_Expression29"):
                    opp_val = getattr(item, "dinkiemodel_Expression29", None)
                    
                    if opp_val == self:
                        setattr(item, "dinkiemodel_Expression29", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dinkiemodel_Expression29"):
                    opp_val = getattr(item, "dinkiemodel_Expression29", None)
                    
                    setattr(item, "dinkiemodel_Expression29", self)
                    

class dinkiemodel_Declaration(Statement):

    def __init__(self, global: bool, varName: str, dinkiemodel_Declaration: "dinkiemodel_BaseType" = None, dinkiemodel_Declaration14: "dinkiemodel_Expression" = None):
        self.global = global
        self.varName = varName
        self.dinkiemodel_Declaration = dinkiemodel_Declaration
        self.dinkiemodel_Declaration14 = dinkiemodel_Declaration14
        
    @property
    def global(self) -> bool:
        return self.__global

    @global.setter
    def global(self, global: bool):
        self.__global = global

    @property
    def varName(self) -> str:
        return self.__varName

    @varName.setter
    def varName(self, varName: str):
        self.__varName = varName

    @property
    def dinkiemodel_Declaration14(self):
        return self.__dinkiemodel_Declaration14

    @dinkiemodel_Declaration14.setter
    def dinkiemodel_Declaration14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dinkiemodel_Declaration__dinkiemodel_Declaration14", None)
        self.__dinkiemodel_Declaration14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dinkiemodel_Expression"):
                opp_val = getattr(old_value, "dinkiemodel_Expression", None)
                if opp_val == self:
                    setattr(old_value, "dinkiemodel_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dinkiemodel_Expression"):
                opp_val = getattr(value, "dinkiemodel_Expression", None)
                setattr(value, "dinkiemodel_Expression", self)

    @property
    def dinkiemodel_Declaration(self):
        return self.__dinkiemodel_Declaration

    @dinkiemodel_Declaration.setter
    def dinkiemodel_Declaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dinkiemodel_Declaration__dinkiemodel_Declaration", None)
        self.__dinkiemodel_Declaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dinkiemodel_BaseType"):
                opp_val = getattr(old_value, "dinkiemodel_BaseType", None)
                if opp_val == self:
                    setattr(old_value, "dinkiemodel_BaseType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dinkiemodel_BaseType"):
                opp_val = getattr(value, "dinkiemodel_BaseType", None)
                setattr(value, "dinkiemodel_BaseType", self)

class dinkiemodel_Type(ABC):

    pass
class dinkiemodel_Argument:

    def __init__(self, name: str, dinkiemodel_Argument: "dinkiemodel_FunctionDecl" = None, dinkiemodel_Argument73: "dinkiemodel_Type" = None):
        self.name = name
        self.dinkiemodel_Argument = dinkiemodel_Argument
        self.dinkiemodel_Argument73 = dinkiemodel_Argument73
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dinkiemodel_Argument73(self):
        return self.__dinkiemodel_Argument73

    @dinkiemodel_Argument73.setter
    def dinkiemodel_Argument73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dinkiemodel_Argument__dinkiemodel_Argument73", None)
        self.__dinkiemodel_Argument73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dinkiemodel_Type74"):
                opp_val = getattr(old_value, "dinkiemodel_Type74", None)
                if opp_val == self:
                    setattr(old_value, "dinkiemodel_Type74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dinkiemodel_Type74"):
                opp_val = getattr(value, "dinkiemodel_Type74", None)
                setattr(value, "dinkiemodel_Type74", self)

    @property
    def dinkiemodel_Argument(self):
        return self.__dinkiemodel_Argument

    @dinkiemodel_Argument.setter
    def dinkiemodel_Argument(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dinkiemodel_Argument__dinkiemodel_Argument", None)
        self.__dinkiemodel_Argument = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dinkiemodel_FunctionDecl9"):
                opp_val = getattr(old_value, "dinkiemodel_FunctionDecl9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dinkiemodel_FunctionDecl9"):
                opp_val = getattr(value, "dinkiemodel_FunctionDecl9", None)
                if opp_val is None:
                    setattr(value, "dinkiemodel_FunctionDecl9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dinkiemodel_WriteStatement(Statement):

    pass
class dinkiemodel_ReadStatement(Statement):

    def __init__(self, varName: str, dinkiemodel_ReadStatement: "dinkiemodel_BaseType" = None):
        self.varName = varName
        self.dinkiemodel_ReadStatement = dinkiemodel_ReadStatement
        
    @property
    def varName(self) -> str:
        return self.__varName

    @varName.setter
    def varName(self, varName: str):
        self.__varName = varName

    @property
    def dinkiemodel_ReadStatement(self):
        return self.__dinkiemodel_ReadStatement

    @dinkiemodel_ReadStatement.setter
    def dinkiemodel_ReadStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dinkiemodel_ReadStatement__dinkiemodel_ReadStatement", None)
        self.__dinkiemodel_ReadStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dinkiemodel_BaseType17"):
                opp_val = getattr(old_value, "dinkiemodel_BaseType17", None)
                if opp_val == self:
                    setattr(old_value, "dinkiemodel_BaseType17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dinkiemodel_BaseType17"):
                opp_val = getattr(value, "dinkiemodel_BaseType17", None)
                setattr(value, "dinkiemodel_BaseType17", self)

class dinkiemodel_Program:

    pass
class dinkiemodel_Statement(ABC):

    pass
class dinkiemodel_Main:

    pass
class dinkiemodel_FunctionDecl:

    def __init__(self, name: str, dinkiemodel_FunctionDecl: "dinkiemodel_Program" = None, dinkiemodel_FunctionDecl6: set["dinkiemodel_Statement"] = None, dinkiemodel_FunctionDecl9: set["dinkiemodel_Argument"] = None, dinkiemodel_FunctionDecl11: "dinkiemodel_Type" = None):
        self.name = name
        self.dinkiemodel_FunctionDecl = dinkiemodel_FunctionDecl
        self.dinkiemodel_FunctionDecl6 = dinkiemodel_FunctionDecl6 if dinkiemodel_FunctionDecl6 is not None else set()
        self.dinkiemodel_FunctionDecl9 = dinkiemodel_FunctionDecl9 if dinkiemodel_FunctionDecl9 is not None else set()
        self.dinkiemodel_FunctionDecl11 = dinkiemodel_FunctionDecl11
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dinkiemodel_FunctionDecl9(self):
        return self.__dinkiemodel_FunctionDecl9

    @dinkiemodel_FunctionDecl9.setter
    def dinkiemodel_FunctionDecl9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dinkiemodel_FunctionDecl__dinkiemodel_FunctionDecl9", None)
        self.__dinkiemodel_FunctionDecl9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dinkiemodel_Argument"):
                    opp_val = getattr(item, "dinkiemodel_Argument", None)
                    
                    if opp_val == self:
                        setattr(item, "dinkiemodel_Argument", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dinkiemodel_Argument"):
                    opp_val = getattr(item, "dinkiemodel_Argument", None)
                    
                    setattr(item, "dinkiemodel_Argument", self)
                    

    @property
    def dinkiemodel_FunctionDecl11(self):
        return self.__dinkiemodel_FunctionDecl11

    @dinkiemodel_FunctionDecl11.setter
    def dinkiemodel_FunctionDecl11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dinkiemodel_FunctionDecl__dinkiemodel_FunctionDecl11", None)
        self.__dinkiemodel_FunctionDecl11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dinkiemodel_Type"):
                opp_val = getattr(old_value, "dinkiemodel_Type", None)
                if opp_val == self:
                    setattr(old_value, "dinkiemodel_Type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dinkiemodel_Type"):
                opp_val = getattr(value, "dinkiemodel_Type", None)
                setattr(value, "dinkiemodel_Type", self)

    @property
    def dinkiemodel_FunctionDecl6(self):
        return self.__dinkiemodel_FunctionDecl6

    @dinkiemodel_FunctionDecl6.setter
    def dinkiemodel_FunctionDecl6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dinkiemodel_FunctionDecl__dinkiemodel_FunctionDecl6", None)
        self.__dinkiemodel_FunctionDecl6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dinkiemodel_Statement7"):
                    opp_val = getattr(item, "dinkiemodel_Statement7", None)
                    
                    if opp_val == self:
                        setattr(item, "dinkiemodel_Statement7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dinkiemodel_Statement7"):
                    opp_val = getattr(item, "dinkiemodel_Statement7", None)
                    
                    setattr(item, "dinkiemodel_Statement7", self)
                    

    @property
    def dinkiemodel_FunctionDecl(self):
        return self.__dinkiemodel_FunctionDecl

    @dinkiemodel_FunctionDecl.setter
    def dinkiemodel_FunctionDecl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dinkiemodel_FunctionDecl__dinkiemodel_FunctionDecl", None)
        self.__dinkiemodel_FunctionDecl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dinkiemodel_Program"):
                opp_val = getattr(old_value, "dinkiemodel_Program", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dinkiemodel_Program"):
                opp_val = getattr(value, "dinkiemodel_Program", None)
                if opp_val is None:
                    setattr(value, "dinkiemodel_Program", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
