from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class BinOp(Enum):
    BOR = "BOR"
    BAND = "BAND"
    BEQ = "BEQ"
    BNE = "BNE"
    BLT = "BLT"
    BGT = "BGT"
    BLE = "BLE"
    BGE = "BGE"
    BADD = "BADD"
    BMINUS = "BMINUS"
    BMUL = "BMUL"
    BDIV = "BDIV"
    BMOD = "BMOD"
    ENQUEUE = "ENQUEUE"
    APPEND = "APPEND"
class UnOp(Enum):
    UMINUS = "UMINUS"
    UDOLLAR = "UDOLLAR"
    UNOT = "UNOT"
    UFULL = "UFULL"
    UEMPTY = "UEMPTY"
    DEQUEUE = "DEQUEUE"
    FIRST = "FIRST"


############################################
# Definition of Classes
############################################

class MaxBound:

    pass
class fiacre_InfiniteBound(MaxBound):

    pass
class MinBound:

    pass
class fiacre_FiniteBound(MaxBound, MinBound):

    def __init__(self, strict: bool, val: int):
        self.strict = strict
        self.val = val
        
    @property
    def val(self) -> int:
        return self.__val

    @val.setter
    def val(self, val: int):
        self.__val = val

    @property
    def strict(self) -> bool:
        return self.__strict

    @strict.setter
    def strict(self, strict: bool):
        self.__strict = strict

class fiacre_LabeledType(ABC):

    def __init__(self, name: str, fiacre_LabeledType: "fiacre_Type" = None):
        self.name = name
        self.fiacre_LabeledType = fiacre_LabeledType
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fiacre_LabeledType(self):
        return self.__fiacre_LabeledType

    @fiacre_LabeledType.setter
    def fiacre_LabeledType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacre_LabeledType__fiacre_LabeledType", None)
        self.__fiacre_LabeledType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fiacre_Type175"):
                opp_val = getattr(old_value, "fiacre_Type175", None)
                if opp_val == self:
                    setattr(old_value, "fiacre_Type175", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fiacre_Type175"):
                opp_val = getattr(value, "fiacre_Type175", None)
                setattr(value, "fiacre_Type175", self)

class fiacre_Rule:

    pass
class Communication:

    pass
class fiacre_Reception(Communication):

    pass
class fiacre_Synchronization(Communication):

    pass
class PortDecl:

    pass
class fiacre_Emission(Communication):

    pass
class LabeledType:

    pass
class fiacre_Constr(LabeledType):

    pass
class fiacre_ValuedField:

    def __init__(self, field: str, fiacre_ValuedField: "fiacre_InlineRecord" = None, fiacre_ValuedField115: "fiacre_Exp" = None):
        self.field = field
        self.fiacre_ValuedField = fiacre_ValuedField
        self.fiacre_ValuedField115 = fiacre_ValuedField115
        
    @property
    def field(self) -> str:
        return self.__field

    @field.setter
    def field(self, field: str):
        self.__field = field

    @property
    def fiacre_ValuedField115(self):
        return self.__fiacre_ValuedField115

    @fiacre_ValuedField115.setter
    def fiacre_ValuedField115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacre_ValuedField__fiacre_ValuedField115", None)
        self.__fiacre_ValuedField115 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fiacre_Exp116"):
                opp_val = getattr(old_value, "fiacre_Exp116", None)
                if opp_val == self:
                    setattr(old_value, "fiacre_Exp116", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fiacre_Exp116"):
                opp_val = getattr(value, "fiacre_Exp116", None)
                setattr(value, "fiacre_Exp116", self)

    @property
    def fiacre_ValuedField(self):
        return self.__fiacre_ValuedField

    @fiacre_ValuedField.setter
    def fiacre_ValuedField(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacre_ValuedField__fiacre_ValuedField", None)
        self.__fiacre_ValuedField = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fiacre_InlineRecord"):
                opp_val = getattr(old_value, "fiacre_InlineRecord", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fiacre_InlineRecord"):
                opp_val = getattr(value, "fiacre_InlineRecord", None)
                if opp_val is None:
                    setattr(value, "fiacre_InlineRecord", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Channel:

    pass
class fiacre_Profile(Channel):

    pass
class fiacre_Field(LabeledType):

    pass
class BasicType:

    pass
class fiacre_NatType(BasicType):

    pass
class fiacre_IntType(BasicType):

    pass
class fiacre_BoolType(BasicType):

    pass
class Type:

    pass
class fiacre_Interval(Type):

    pass
class fiacre_Union(Type):

    pass
class fiacre_Queue(Type):

    pass
class fiacre_TypeId(Type):

    pass
class fiacre_Array(Type):

    pass
class fiacre_Record(Type):

    pass
class fiacre_BasicType(Type):

    pass
class InlineCollection:

    pass
class fiacre_InlineArray(InlineCollection):

    pass
class fiacre_InlineQueue(InlineCollection):

    pass
class fiacre_Variable(ABC):

    def __init__(self, name: str, fiacre_Variable: "fiacre_VarRef" = None, fiacre_Variable133: "fiacre_Type" = None, fiacre_Variable164: "fiacre_RefArg" = None):
        self.name = name
        self.fiacre_Variable = fiacre_Variable
        self.fiacre_Variable133 = fiacre_Variable133
        self.fiacre_Variable164 = fiacre_Variable164
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fiacre_Variable(self):
        return self.__fiacre_Variable

    @fiacre_Variable.setter
    def fiacre_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacre_Variable__fiacre_Variable", None)
        self.__fiacre_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fiacre_VarRef"):
                opp_val = getattr(old_value, "fiacre_VarRef", None)
                if opp_val == self:
                    setattr(old_value, "fiacre_VarRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fiacre_VarRef"):
                opp_val = getattr(value, "fiacre_VarRef", None)
                setattr(value, "fiacre_VarRef", self)

    @property
    def fiacre_Variable133(self):
        return self.__fiacre_Variable133

    @fiacre_Variable133.setter
    def fiacre_Variable133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacre_Variable__fiacre_Variable133", None)
        self.__fiacre_Variable133 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fiacre_Type134"):
                opp_val = getattr(old_value, "fiacre_Type134", None)
                if opp_val == self:
                    setattr(old_value, "fiacre_Type134", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fiacre_Type134"):
                opp_val = getattr(value, "fiacre_Type134", None)
                setattr(value, "fiacre_Type134", self)

    @property
    def fiacre_Variable164(self):
        return self.__fiacre_Variable164

    @fiacre_Variable164.setter
    def fiacre_Variable164(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacre_Variable__fiacre_Variable164", None)
        self.__fiacre_Variable164 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fiacre_RefArg"):
                opp_val = getattr(old_value, "fiacre_RefArg", None)
                if opp_val == self:
                    setattr(old_value, "fiacre_RefArg", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fiacre_RefArg"):
                opp_val = getattr(value, "fiacre_RefArg", None)
                setattr(value, "fiacre_RefArg", self)

class Exp:

    pass
class fiacre_ConstrExp(Exp):

    def __init__(self, name: str, fiacre_ConstrExp: "fiacre_Exp" = None):
        self.name = name
        self.fiacre_ConstrExp = fiacre_ConstrExp
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fiacre_ConstrExp(self):
        return self.__fiacre_ConstrExp

    @fiacre_ConstrExp.setter
    def fiacre_ConstrExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacre_ConstrExp__fiacre_ConstrExp", None)
        self.__fiacre_ConstrExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fiacre_Exp142"):
                opp_val = getattr(old_value, "fiacre_Exp142", None)
                if opp_val == self:
                    setattr(old_value, "fiacre_Exp142", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fiacre_Exp142"):
                opp_val = getattr(value, "fiacre_Exp142", None)
                setattr(value, "fiacre_Exp142", self)

class fiacre_RecordElem(Exp):

    def __init__(self, field: str, fiacre_RecordElem: "fiacre_Exp" = None):
        self.field = field
        self.fiacre_RecordElem = fiacre_RecordElem
        
    @property
    def field(self) -> str:
        return self.__field

    @field.setter
    def field(self, field: str):
        self.__field = field

    @property
    def fiacre_RecordElem(self):
        return self.__fiacre_RecordElem

    @fiacre_RecordElem.setter
    def fiacre_RecordElem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacre_RecordElem__fiacre_RecordElem", None)
        self.__fiacre_RecordElem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fiacre_Exp92"):
                opp_val = getattr(old_value, "fiacre_Exp92", None)
                if opp_val == self:
                    setattr(old_value, "fiacre_Exp92", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fiacre_Exp92"):
                opp_val = getattr(value, "fiacre_Exp92", None)
                setattr(value, "fiacre_Exp92", self)

class fiacre_BinExp(Exp):

    def __init__(self, binOp: str, fiacre_BinExp: "fiacre_Exp" = None, fiacre_BinExp83: "fiacre_Exp" = None):
        self.binOp = binOp
        self.fiacre_BinExp = fiacre_BinExp
        self.fiacre_BinExp83 = fiacre_BinExp83
        
    @property
    def binOp(self) -> str:
        return self.__binOp

    @binOp.setter
    def binOp(self, binOp: str):
        self.__binOp = binOp

    @property
    def fiacre_BinExp(self):
        return self.__fiacre_BinExp

    @fiacre_BinExp.setter
    def fiacre_BinExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacre_BinExp__fiacre_BinExp", None)
        self.__fiacre_BinExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fiacre_Exp81"):
                opp_val = getattr(old_value, "fiacre_Exp81", None)
                if opp_val == self:
                    setattr(old_value, "fiacre_Exp81", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fiacre_Exp81"):
                opp_val = getattr(value, "fiacre_Exp81", None)
                setattr(value, "fiacre_Exp81", self)

    @property
    def fiacre_BinExp83(self):
        return self.__fiacre_BinExp83

    @fiacre_BinExp83.setter
    def fiacre_BinExp83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacre_BinExp__fiacre_BinExp83", None)
        self.__fiacre_BinExp83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fiacre_Exp84"):
                opp_val = getattr(old_value, "fiacre_Exp84", None)
                if opp_val == self:
                    setattr(old_value, "fiacre_Exp84", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fiacre_Exp84"):
                opp_val = getattr(value, "fiacre_Exp84", None)
                setattr(value, "fiacre_Exp84", self)

class fiacre_InlineCollection(Exp):

    pass
class fiacre_ArrayElem(Exp):

    pass
class fiacre_CondExp(Exp):

    pass
class fiacre_InlineRecord(Exp):

    pass
class fiacre_UnExp(Exp):

    def __init__(self, unop: str, fiacre_UnExp: "fiacre_Exp" = None):
        self.unop = unop
        self.fiacre_UnExp = fiacre_UnExp
        
    @property
    def unop(self) -> str:
        return self.__unop

    @unop.setter
    def unop(self, unop: str):
        self.__unop = unop

    @property
    def fiacre_UnExp(self):
        return self.__fiacre_UnExp

    @fiacre_UnExp.setter
    def fiacre_UnExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacre_UnExp__fiacre_UnExp", None)
        self.__fiacre_UnExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fiacre_Exp79"):
                opp_val = getattr(old_value, "fiacre_Exp79", None)
                if opp_val == self:
                    setattr(old_value, "fiacre_Exp79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fiacre_Exp79"):
                opp_val = getattr(value, "fiacre_Exp79", None)
                setattr(value, "fiacre_Exp79", self)

class Pattern:

    pass
class fiacre_AnyPattern(Pattern):

    pass
class fiacre_ConstrPattern(Pattern):

    def __init__(self, name: str, fiacre_ConstrPattern: "fiacre_Pattern" = None):
        self.name = name
        self.fiacre_ConstrPattern = fiacre_ConstrPattern
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fiacre_ConstrPattern(self):
        return self.__fiacre_ConstrPattern

    @fiacre_ConstrPattern.setter
    def fiacre_ConstrPattern(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacre_ConstrPattern__fiacre_ConstrPattern", None)
        self.__fiacre_ConstrPattern = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fiacre_Pattern145"):
                opp_val = getattr(old_value, "fiacre_Pattern145", None)
                if opp_val == self:
                    setattr(old_value, "fiacre_Pattern145", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fiacre_Pattern145"):
                opp_val = getattr(value, "fiacre_Pattern145", None)
                setattr(value, "fiacre_Pattern145", self)

class fiacre_ConstantRef(Exp, Pattern):

    pass
class fiacre_Literal(Exp, Pattern):

    pass
class fiacre_FieldPattern(Pattern):

    def __init__(self, field: str, fiacre_FieldPattern: "fiacre_Pattern" = None):
        self.field = field
        self.fiacre_FieldPattern = fiacre_FieldPattern
        
    @property
    def field(self) -> str:
        return self.__field

    @field.setter
    def field(self, field: str):
        self.__field = field

    @property
    def fiacre_FieldPattern(self):
        return self.__fiacre_FieldPattern

    @fiacre_FieldPattern.setter
    def fiacre_FieldPattern(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacre_FieldPattern__fiacre_FieldPattern", None)
        self.__fiacre_FieldPattern = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fiacre_Pattern152"):
                opp_val = getattr(old_value, "fiacre_Pattern152", None)
                if opp_val == self:
                    setattr(old_value, "fiacre_Pattern152", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fiacre_Pattern152"):
                opp_val = getattr(value, "fiacre_Pattern152", None)
                setattr(value, "fiacre_Pattern152", self)

class fiacre_ArrayPattern(Pattern):

    pass
class fiacre_VarRef(Exp, Pattern):

    pass
class Literal:

    pass
class fiacre_BoolLiteral(Literal):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class fiacre_NatLiteral(Literal):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class fiacre_Pattern(ABC):

    pass
class fiacre_SingleAssignment:

    pass
class Assignment:

    pass
class fiacre_NonDeterministicAssignment(Assignment):

    pass
class fiacre_DeterministicAssignment(Assignment):

    pass
class fiacre_MaxBound(ABC):

    pass
class fiacre_MinBound(ABC):

    pass
class Variable:

    pass
class Statement:

    pass
class fiacre_To(Statement):

    pass
class fiacre_Assignment(Statement):

    pass
class fiacre_Select(Statement):

    pass
class fiacre_WhileStmt(Statement):

    pass
class fiacre_IfStmt(Statement):

    pass
class fiacre_Seq(Statement):

    pass
class fiacre_Foreach(Statement):

    pass
class fiacre_CaseStmt(Statement):

    pass
class fiacre_Wait(Statement):

    pass
class fiacre_Communication(Statement):

    pass
class fiacre_NullStmt(Statement):

    pass
class Arg:

    pass
class fiacre_RefArg(Arg):

    pass
class fiacre_Arg(ABC):

    pass
class fiacre_InterfacedComp:

    pass
class Composition:

    pass
class fiacre_Instance(Composition):

    def __init__(self, name: str, fiacre_Instance: "fiacre_NodeDecl" = None, fiacre_Instance29: set["fiacre_Arg"] = None, fiacre_Instance31: set["fiacre_PortDecl"] = None):
        self.name = name
        self.fiacre_Instance = fiacre_Instance
        self.fiacre_Instance29 = fiacre_Instance29 if fiacre_Instance29 is not None else set()
        self.fiacre_Instance31 = fiacre_Instance31 if fiacre_Instance31 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fiacre_Instance(self):
        return self.__fiacre_Instance

    @fiacre_Instance.setter
    def fiacre_Instance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacre_Instance__fiacre_Instance", None)
        self.__fiacre_Instance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fiacre_NodeDecl27"):
                opp_val = getattr(old_value, "fiacre_NodeDecl27", None)
                if opp_val == self:
                    setattr(old_value, "fiacre_NodeDecl27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fiacre_NodeDecl27"):
                opp_val = getattr(value, "fiacre_NodeDecl27", None)
                setattr(value, "fiacre_NodeDecl27", self)

    @property
    def fiacre_Instance31(self):
        return self.__fiacre_Instance31

    @fiacre_Instance31.setter
    def fiacre_Instance31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacre_Instance__fiacre_Instance31", None)
        self.__fiacre_Instance31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fiacre_PortDecl32"):
                    opp_val = getattr(item, "fiacre_PortDecl32", None)
                    
                    if opp_val == self:
                        setattr(item, "fiacre_PortDecl32", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fiacre_PortDecl32"):
                    opp_val = getattr(item, "fiacre_PortDecl32", None)
                    
                    setattr(item, "fiacre_PortDecl32", self)
                    

    @property
    def fiacre_Instance29(self):
        return self.__fiacre_Instance29

    @fiacre_Instance29.setter
    def fiacre_Instance29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacre_Instance__fiacre_Instance29", None)
        self.__fiacre_Instance29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fiacre_Arg"):
                    opp_val = getattr(item, "fiacre_Arg", None)
                    
                    if opp_val == self:
                        setattr(item, "fiacre_Arg", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fiacre_Arg"):
                    opp_val = getattr(item, "fiacre_Arg", None)
                    
                    setattr(item, "fiacre_Arg", self)
                    

class fiacre_Par(Composition):

    pass
class fiacre_Exp(Arg):

    pass
class fiacre_LocalVariable(Variable):

    def __init__(self, constant: bool, fiacre_LocalVariable: "fiacre_NodeDecl" = None, fiacre_LocalVariable24: "fiacre_Exp" = None, fiacre_LocalVariable188: "fiacre_Foreach" = None):
        self.constant = constant
        self.fiacre_LocalVariable = fiacre_LocalVariable
        self.fiacre_LocalVariable24 = fiacre_LocalVariable24
        self.fiacre_LocalVariable188 = fiacre_LocalVariable188
        
    @property
    def constant(self) -> bool:
        return self.__constant

    @constant.setter
    def constant(self, constant: bool):
        self.__constant = constant

    @property
    def fiacre_LocalVariable24(self):
        return self.__fiacre_LocalVariable24

    @fiacre_LocalVariable24.setter
    def fiacre_LocalVariable24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacre_LocalVariable__fiacre_LocalVariable24", None)
        self.__fiacre_LocalVariable24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fiacre_Exp"):
                opp_val = getattr(old_value, "fiacre_Exp", None)
                if opp_val == self:
                    setattr(old_value, "fiacre_Exp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fiacre_Exp"):
                opp_val = getattr(value, "fiacre_Exp", None)
                setattr(value, "fiacre_Exp", self)

    @property
    def fiacre_LocalVariable(self):
        return self.__fiacre_LocalVariable

    @fiacre_LocalVariable.setter
    def fiacre_LocalVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacre_LocalVariable__fiacre_LocalVariable", None)
        self.__fiacre_LocalVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fiacre_NodeDecl6"):
                opp_val = getattr(old_value, "fiacre_NodeDecl6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fiacre_NodeDecl6"):
                opp_val = getattr(value, "fiacre_NodeDecl6", None)
                if opp_val is None:
                    setattr(value, "fiacre_NodeDecl6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fiacre_LocalVariable188(self):
        return self.__fiacre_LocalVariable188

    @fiacre_LocalVariable188.setter
    def fiacre_LocalVariable188(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacre_LocalVariable__fiacre_LocalVariable188", None)
        self.__fiacre_LocalVariable188 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fiacre_Foreach187"):
                opp_val = getattr(old_value, "fiacre_Foreach187", None)
                if opp_val == self:
                    setattr(old_value, "fiacre_Foreach187", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fiacre_Foreach187"):
                opp_val = getattr(value, "fiacre_Foreach187", None)
                setattr(value, "fiacre_Foreach187", self)

class fiacre_ArgumentVariable(Variable):

    def __init__(self, ref: bool, read: bool, write: bool, fiacre_ArgumentVariable: "fiacre_NodeDecl" = None):
        self.ref = ref
        self.read = read
        self.write = write
        self.fiacre_ArgumentVariable = fiacre_ArgumentVariable
        
    @property
    def ref(self) -> bool:
        return self.__ref

    @ref.setter
    def ref(self, ref: bool):
        self.__ref = ref

    @property
    def write(self) -> bool:
        return self.__write

    @write.setter
    def write(self, write: bool):
        self.__write = write

    @property
    def read(self) -> bool:
        return self.__read

    @read.setter
    def read(self, read: bool):
        self.__read = read

    @property
    def fiacre_ArgumentVariable(self):
        return self.__fiacre_ArgumentVariable

    @fiacre_ArgumentVariable.setter
    def fiacre_ArgumentVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacre_ArgumentVariable__fiacre_ArgumentVariable", None)
        self.__fiacre_ArgumentVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fiacre_NodeDecl4"):
                opp_val = getattr(old_value, "fiacre_NodeDecl4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fiacre_NodeDecl4"):
                opp_val = getattr(value, "fiacre_NodeDecl4", None)
                if opp_val is None:
                    setattr(value, "fiacre_NodeDecl4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Declaration:

    pass
class fiacre_ConstantDecl(Declaration):

    pass
class fiacre_PortDecl(ABC):

    def __init__(self, in: bool, out: bool, name: str, fiacre_PortDecl32: "fiacre_Instance" = None, fiacre_PortDecl38: "fiacre_InterfacedComp" = None, fiacre_PortDecl: "fiacre_Channel" = None, fiacre_PortDecl46: "fiacre_Communication" = None, fiacre_PortDecl137: "fiacre_Priority" = None, fiacre_PortDecl140: "fiacre_Priority" = None):
        self.in = in
        self.out = out
        self.name = name
        self.fiacre_PortDecl32 = fiacre_PortDecl32
        self.fiacre_PortDecl38 = fiacre_PortDecl38
        self.fiacre_PortDecl = fiacre_PortDecl
        self.fiacre_PortDecl46 = fiacre_PortDecl46
        self.fiacre_PortDecl137 = fiacre_PortDecl137
        self.fiacre_PortDecl140 = fiacre_PortDecl140
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def out(self) -> bool:
        return self.__out

    @out.setter
    def out(self, out: bool):
        self.__out = out

    @property
    def in(self) -> bool:
        return self.__in

    @in.setter
    def in(self, in: bool):
        self.__in = in

    @property
    def fiacre_PortDecl38(self):
        return self.__fiacre_PortDecl38

    @fiacre_PortDecl38.setter
    def fiacre_PortDecl38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacre_PortDecl__fiacre_PortDecl38", None)
        self.__fiacre_PortDecl38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fiacre_InterfacedComp37"):
                opp_val = getattr(old_value, "fiacre_InterfacedComp37", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fiacre_InterfacedComp37"):
                opp_val = getattr(value, "fiacre_InterfacedComp37", None)
                if opp_val is None:
                    setattr(value, "fiacre_InterfacedComp37", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fiacre_PortDecl137(self):
        return self.__fiacre_PortDecl137

    @fiacre_PortDecl137.setter
    def fiacre_PortDecl137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacre_PortDecl__fiacre_PortDecl137", None)
        self.__fiacre_PortDecl137 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fiacre_Priority136"):
                opp_val = getattr(old_value, "fiacre_Priority136", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fiacre_Priority136"):
                opp_val = getattr(value, "fiacre_Priority136", None)
                if opp_val is None:
                    setattr(value, "fiacre_Priority136", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fiacre_PortDecl32(self):
        return self.__fiacre_PortDecl32

    @fiacre_PortDecl32.setter
    def fiacre_PortDecl32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacre_PortDecl__fiacre_PortDecl32", None)
        self.__fiacre_PortDecl32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fiacre_Instance31"):
                opp_val = getattr(old_value, "fiacre_Instance31", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fiacre_Instance31"):
                opp_val = getattr(value, "fiacre_Instance31", None)
                if opp_val is None:
                    setattr(value, "fiacre_Instance31", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fiacre_PortDecl46(self):
        return self.__fiacre_PortDecl46

    @fiacre_PortDecl46.setter
    def fiacre_PortDecl46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacre_PortDecl__fiacre_PortDecl46", None)
        self.__fiacre_PortDecl46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fiacre_Communication"):
                opp_val = getattr(old_value, "fiacre_Communication", None)
                if opp_val == self:
                    setattr(old_value, "fiacre_Communication", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fiacre_Communication"):
                opp_val = getattr(value, "fiacre_Communication", None)
                setattr(value, "fiacre_Communication", self)

    @property
    def fiacre_PortDecl140(self):
        return self.__fiacre_PortDecl140

    @fiacre_PortDecl140.setter
    def fiacre_PortDecl140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacre_PortDecl__fiacre_PortDecl140", None)
        self.__fiacre_PortDecl140 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fiacre_Priority139"):
                opp_val = getattr(old_value, "fiacre_Priority139", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fiacre_Priority139"):
                opp_val = getattr(value, "fiacre_Priority139", None)
                if opp_val is None:
                    setattr(value, "fiacre_Priority139", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fiacre_PortDecl(self):
        return self.__fiacre_PortDecl

    @fiacre_PortDecl.setter
    def fiacre_PortDecl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacre_PortDecl__fiacre_PortDecl", None)
        self.__fiacre_PortDecl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fiacre_Channel22"):
                opp_val = getattr(old_value, "fiacre_Channel22", None)
                if opp_val == self:
                    setattr(old_value, "fiacre_Channel22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fiacre_Channel22"):
                opp_val = getattr(value, "fiacre_Channel22", None)
                setattr(value, "fiacre_Channel22", self)

class fiacre_Transition:

    def __init__(self, name: str, fiacre_Transition: "fiacre_ProcessDecl" = None, fiacre_Transition40: "fiacre_State" = None, fiacre_Transition43: "fiacre_Statement" = None):
        self.name = name
        self.fiacre_Transition = fiacre_Transition
        self.fiacre_Transition40 = fiacre_Transition40
        self.fiacre_Transition43 = fiacre_Transition43
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fiacre_Transition43(self):
        return self.__fiacre_Transition43

    @fiacre_Transition43.setter
    def fiacre_Transition43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacre_Transition__fiacre_Transition43", None)
        self.__fiacre_Transition43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fiacre_Statement44"):
                opp_val = getattr(old_value, "fiacre_Statement44", None)
                if opp_val == self:
                    setattr(old_value, "fiacre_Statement44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fiacre_Statement44"):
                opp_val = getattr(value, "fiacre_Statement44", None)
                setattr(value, "fiacre_Statement44", self)

    @property
    def fiacre_Transition(self):
        return self.__fiacre_Transition

    @fiacre_Transition.setter
    def fiacre_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacre_Transition__fiacre_Transition", None)
        self.__fiacre_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fiacre_ProcessDecl20"):
                opp_val = getattr(old_value, "fiacre_ProcessDecl20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fiacre_ProcessDecl20"):
                opp_val = getattr(value, "fiacre_ProcessDecl20", None)
                if opp_val is None:
                    setattr(value, "fiacre_ProcessDecl20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fiacre_Transition40(self):
        return self.__fiacre_Transition40

    @fiacre_Transition40.setter
    def fiacre_Transition40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacre_Transition__fiacre_Transition40", None)
        self.__fiacre_Transition40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fiacre_State41"):
                opp_val = getattr(old_value, "fiacre_State41", None)
                if opp_val == self:
                    setattr(old_value, "fiacre_State41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fiacre_State41"):
                opp_val = getattr(value, "fiacre_State41", None)
                setattr(value, "fiacre_State41", self)

class fiacre_State:

    def __init__(self, name: str, fiacre_State: "fiacre_ProcessDecl" = None, fiacre_State41: "fiacre_Transition" = None, fiacre_State63: "fiacre_To" = None):
        self.name = name
        self.fiacre_State = fiacre_State
        self.fiacre_State41 = fiacre_State41
        self.fiacre_State63 = fiacre_State63
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fiacre_State(self):
        return self.__fiacre_State

    @fiacre_State.setter
    def fiacre_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacre_State__fiacre_State", None)
        self.__fiacre_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fiacre_ProcessDecl"):
                opp_val = getattr(old_value, "fiacre_ProcessDecl", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fiacre_ProcessDecl"):
                opp_val = getattr(value, "fiacre_ProcessDecl", None)
                if opp_val is None:
                    setattr(value, "fiacre_ProcessDecl", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fiacre_State41(self):
        return self.__fiacre_State41

    @fiacre_State41.setter
    def fiacre_State41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacre_State__fiacre_State41", None)
        self.__fiacre_State41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fiacre_Transition40"):
                opp_val = getattr(old_value, "fiacre_Transition40", None)
                if opp_val == self:
                    setattr(old_value, "fiacre_Transition40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fiacre_Transition40"):
                opp_val = getattr(value, "fiacre_Transition40", None)
                setattr(value, "fiacre_Transition40", self)

    @property
    def fiacre_State63(self):
        return self.__fiacre_State63

    @fiacre_State63.setter
    def fiacre_State63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacre_State__fiacre_State63", None)
        self.__fiacre_State63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fiacre_To"):
                opp_val = getattr(old_value, "fiacre_To", None)
                if opp_val == self:
                    setattr(old_value, "fiacre_To", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fiacre_To"):
                opp_val = getattr(value, "fiacre_To", None)
                setattr(value, "fiacre_To", self)

class fiacre_Priority:

    pass
class fiacre_Composition(ABC):

    pass
class NodeDecl:

    pass
class fiacre_ProcessDecl(NodeDecl):

    pass
class fiacre_ComponentDecl(NodeDecl):

    pass
class fiacre_Channel(ABC):

    pass
class fiacre_ChannelDecl(Declaration):

    pass
class fiacre_Type(ABC):

    pass
class fiacre_TypeDecl(Declaration):

    pass
class fiacre_Statement(ABC):

    def __init__(self, comment: str, fiacre_Statement: "fiacre_NodeDecl" = None, fiacre_Statement44: "fiacre_Transition" = None, fiacre_Statement56: "fiacre_IfStmt" = None, fiacre_Statement59: "fiacre_IfStmt" = None, fiacre_Statement61: "fiacre_Select" = None, fiacre_Statement51: "fiacre_WhileStmt" = None, fiacre_Statement125: "fiacre_Seq" = None, fiacre_Statement162: "fiacre_Rule" = None, fiacre_Statement185: "fiacre_Foreach" = None):
        self.comment = comment
        self.fiacre_Statement = fiacre_Statement
        self.fiacre_Statement44 = fiacre_Statement44
        self.fiacre_Statement56 = fiacre_Statement56
        self.fiacre_Statement59 = fiacre_Statement59
        self.fiacre_Statement61 = fiacre_Statement61
        self.fiacre_Statement51 = fiacre_Statement51
        self.fiacre_Statement125 = fiacre_Statement125
        self.fiacre_Statement162 = fiacre_Statement162
        self.fiacre_Statement185 = fiacre_Statement185
        
    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def fiacre_Statement185(self):
        return self.__fiacre_Statement185

    @fiacre_Statement185.setter
    def fiacre_Statement185(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacre_Statement__fiacre_Statement185", None)
        self.__fiacre_Statement185 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fiacre_Foreach"):
                opp_val = getattr(old_value, "fiacre_Foreach", None)
                if opp_val == self:
                    setattr(old_value, "fiacre_Foreach", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fiacre_Foreach"):
                opp_val = getattr(value, "fiacre_Foreach", None)
                setattr(value, "fiacre_Foreach", self)

    @property
    def fiacre_Statement51(self):
        return self.__fiacre_Statement51

    @fiacre_Statement51.setter
    def fiacre_Statement51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacre_Statement__fiacre_Statement51", None)
        self.__fiacre_Statement51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fiacre_WhileStmt50"):
                opp_val = getattr(old_value, "fiacre_WhileStmt50", None)
                if opp_val == self:
                    setattr(old_value, "fiacre_WhileStmt50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fiacre_WhileStmt50"):
                opp_val = getattr(value, "fiacre_WhileStmt50", None)
                setattr(value, "fiacre_WhileStmt50", self)

    @property
    def fiacre_Statement59(self):
        return self.__fiacre_Statement59

    @fiacre_Statement59.setter
    def fiacre_Statement59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacre_Statement__fiacre_Statement59", None)
        self.__fiacre_Statement59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fiacre_IfStmt58"):
                opp_val = getattr(old_value, "fiacre_IfStmt58", None)
                if opp_val == self:
                    setattr(old_value, "fiacre_IfStmt58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fiacre_IfStmt58"):
                opp_val = getattr(value, "fiacre_IfStmt58", None)
                setattr(value, "fiacre_IfStmt58", self)

    @property
    def fiacre_Statement162(self):
        return self.__fiacre_Statement162

    @fiacre_Statement162.setter
    def fiacre_Statement162(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacre_Statement__fiacre_Statement162", None)
        self.__fiacre_Statement162 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fiacre_Rule161"):
                opp_val = getattr(old_value, "fiacre_Rule161", None)
                if opp_val == self:
                    setattr(old_value, "fiacre_Rule161", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fiacre_Rule161"):
                opp_val = getattr(value, "fiacre_Rule161", None)
                setattr(value, "fiacre_Rule161", self)

    @property
    def fiacre_Statement44(self):
        return self.__fiacre_Statement44

    @fiacre_Statement44.setter
    def fiacre_Statement44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacre_Statement__fiacre_Statement44", None)
        self.__fiacre_Statement44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fiacre_Transition43"):
                opp_val = getattr(old_value, "fiacre_Transition43", None)
                if opp_val == self:
                    setattr(old_value, "fiacre_Transition43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fiacre_Transition43"):
                opp_val = getattr(value, "fiacre_Transition43", None)
                setattr(value, "fiacre_Transition43", self)

    @property
    def fiacre_Statement125(self):
        return self.__fiacre_Statement125

    @fiacre_Statement125.setter
    def fiacre_Statement125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacre_Statement__fiacre_Statement125", None)
        self.__fiacre_Statement125 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fiacre_Seq"):
                opp_val = getattr(old_value, "fiacre_Seq", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fiacre_Seq"):
                opp_val = getattr(value, "fiacre_Seq", None)
                if opp_val is None:
                    setattr(value, "fiacre_Seq", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fiacre_Statement61(self):
        return self.__fiacre_Statement61

    @fiacre_Statement61.setter
    def fiacre_Statement61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacre_Statement__fiacre_Statement61", None)
        self.__fiacre_Statement61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fiacre_Select"):
                opp_val = getattr(old_value, "fiacre_Select", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fiacre_Select"):
                opp_val = getattr(value, "fiacre_Select", None)
                if opp_val is None:
                    setattr(value, "fiacre_Select", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fiacre_Statement(self):
        return self.__fiacre_Statement

    @fiacre_Statement.setter
    def fiacre_Statement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacre_Statement__fiacre_Statement", None)
        self.__fiacre_Statement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fiacre_NodeDecl12"):
                opp_val = getattr(old_value, "fiacre_NodeDecl12", None)
                if opp_val == self:
                    setattr(old_value, "fiacre_NodeDecl12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fiacre_NodeDecl12"):
                opp_val = getattr(value, "fiacre_NodeDecl12", None)
                setattr(value, "fiacre_NodeDecl12", self)

    @property
    def fiacre_Statement56(self):
        return self.__fiacre_Statement56

    @fiacre_Statement56.setter
    def fiacre_Statement56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacre_Statement__fiacre_Statement56", None)
        self.__fiacre_Statement56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fiacre_IfStmt55"):
                opp_val = getattr(old_value, "fiacre_IfStmt55", None)
                if opp_val == self:
                    setattr(old_value, "fiacre_IfStmt55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fiacre_IfStmt55"):
                opp_val = getattr(value, "fiacre_IfStmt55", None)
                setattr(value, "fiacre_IfStmt55", self)

class fiacre_LocalPortDecl(PortDecl):

    pass
class fiacre_ParamPortDecl(PortDecl):

    pass
class fiacre_NodeDecl(Declaration):

    pass
class fiacre_Declaration(ABC):

    def __init__(self, name: str, fiacre_Declaration: "fiacre_Program" = None):
        self.name = name
        self.fiacre_Declaration = fiacre_Declaration
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fiacre_Declaration(self):
        return self.__fiacre_Declaration

    @fiacre_Declaration.setter
    def fiacre_Declaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacre_Declaration__fiacre_Declaration", None)
        self.__fiacre_Declaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fiacre_Program"):
                opp_val = getattr(old_value, "fiacre_Program", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fiacre_Program"):
                opp_val = getattr(value, "fiacre_Program", None)
                if opp_val is None:
                    setattr(value, "fiacre_Program", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class fiacre_Program:

    pass