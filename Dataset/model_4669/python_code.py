from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class boa_StringToEvalResMap:

    def __init__(self, key: str, boa_StringToEvalResMap: "boa_Ctx" = None, boa_StringToEvalResMap70: "boa_Ctx" = None, boa_StringToEvalResMap72: "boa_EvalRes" = None, boa_StringToEvalResMap74: "boa_EvalMapRes" = None, boa_StringToEvalResMap81: "boa_EvalBoundFunRes" = None):
        self.key = key
        self.boa_StringToEvalResMap = boa_StringToEvalResMap
        self.boa_StringToEvalResMap70 = boa_StringToEvalResMap70
        self.boa_StringToEvalResMap72 = boa_StringToEvalResMap72
        self.boa_StringToEvalResMap74 = boa_StringToEvalResMap74
        self.boa_StringToEvalResMap81 = boa_StringToEvalResMap81
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def boa_StringToEvalResMap72(self):
        return self.__boa_StringToEvalResMap72

    @boa_StringToEvalResMap72.setter
    def boa_StringToEvalResMap72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_boa_StringToEvalResMap__boa_StringToEvalResMap72", None)
        self.__boa_StringToEvalResMap72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "boa_EvalRes"):
                opp_val = getattr(old_value, "boa_EvalRes", None)
                if opp_val == self:
                    setattr(old_value, "boa_EvalRes", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "boa_EvalRes"):
                opp_val = getattr(value, "boa_EvalRes", None)
                setattr(value, "boa_EvalRes", self)

    @property
    def boa_StringToEvalResMap81(self):
        return self.__boa_StringToEvalResMap81

    @boa_StringToEvalResMap81.setter
    def boa_StringToEvalResMap81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_boa_StringToEvalResMap__boa_StringToEvalResMap81", None)
        self.__boa_StringToEvalResMap81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "boa_EvalBoundFunRes"):
                opp_val = getattr(old_value, "boa_EvalBoundFunRes", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "boa_EvalBoundFunRes"):
                opp_val = getattr(value, "boa_EvalBoundFunRes", None)
                if opp_val is None:
                    setattr(value, "boa_EvalBoundFunRes", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def boa_StringToEvalResMap74(self):
        return self.__boa_StringToEvalResMap74

    @boa_StringToEvalResMap74.setter
    def boa_StringToEvalResMap74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_boa_StringToEvalResMap__boa_StringToEvalResMap74", None)
        self.__boa_StringToEvalResMap74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "boa_EvalMapRes"):
                opp_val = getattr(old_value, "boa_EvalMapRes", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "boa_EvalMapRes"):
                opp_val = getattr(value, "boa_EvalMapRes", None)
                if opp_val is None:
                    setattr(value, "boa_EvalMapRes", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def boa_StringToEvalResMap(self):
        return self.__boa_StringToEvalResMap

    @boa_StringToEvalResMap.setter
    def boa_StringToEvalResMap(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_boa_StringToEvalResMap__boa_StringToEvalResMap", None)
        self.__boa_StringToEvalResMap = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "boa_Ctx"):
                opp_val = getattr(old_value, "boa_Ctx", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "boa_Ctx"):
                opp_val = getattr(value, "boa_Ctx", None)
                if opp_val is None:
                    setattr(value, "boa_Ctx", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def boa_StringToEvalResMap70(self):
        return self.__boa_StringToEvalResMap70

    @boa_StringToEvalResMap70.setter
    def boa_StringToEvalResMap70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_boa_StringToEvalResMap__boa_StringToEvalResMap70", None)
        self.__boa_StringToEvalResMap70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "boa_Ctx69"):
                opp_val = getattr(old_value, "boa_Ctx69", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "boa_Ctx69"):
                opp_val = getattr(value, "boa_Ctx69", None)
                if opp_val is None:
                    setattr(value, "boa_Ctx69", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class EvalFunRes:

    pass
class boa_EvalBoundFunRes(EvalFunRes):

    pass
class EvalRes:

    pass
class boa_EvalFunRes(EvalRes):

    def __init__(self, name: str, boa_EvalFunRes: "boa_Expr" = None, boa_EvalFunRes78: "boa_Ctx" = None):
        self.name = name
        self.boa_EvalFunRes = boa_EvalFunRes
        self.boa_EvalFunRes78 = boa_EvalFunRes78
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def boa_EvalFunRes78(self):
        return self.__boa_EvalFunRes78

    @boa_EvalFunRes78.setter
    def boa_EvalFunRes78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_boa_EvalFunRes__boa_EvalFunRes78", None)
        self.__boa_EvalFunRes78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "boa_Ctx79"):
                opp_val = getattr(old_value, "boa_Ctx79", None)
                if opp_val == self:
                    setattr(old_value, "boa_Ctx79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "boa_Ctx79"):
                opp_val = getattr(value, "boa_Ctx79", None)
                setattr(value, "boa_Ctx79", self)

    @property
    def boa_EvalFunRes(self):
        return self.__boa_EvalFunRes

    @boa_EvalFunRes.setter
    def boa_EvalFunRes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_boa_EvalFunRes__boa_EvalFunRes", None)
        self.__boa_EvalFunRes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "boa_Expr76"):
                opp_val = getattr(old_value, "boa_Expr76", None)
                if opp_val == self:
                    setattr(old_value, "boa_Expr76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "boa_Expr76"):
                opp_val = getattr(value, "boa_Expr76", None)
                setattr(value, "boa_Expr76", self)

class boa_EvalBoolRes(EvalRes):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class boa_EvalIntRes(EvalRes):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class boa_EvalMapRes(EvalRes):

    pass
class boa_EvalRes(ABC):

    pass
class boa_Ctx:

    pass
class CmpOp:

    pass
class boa_CmpOpUnequal(CmpOp):

    pass
class boa_CmpOpLess(CmpOp):

    pass
class boa_CmpOpEqual(CmpOp):

    pass
class BoolOp:

    pass
class boa_BoolOpOr(BoolOp):

    pass
class boa_BoolOpAnd(BoolOp):

    pass
class ArithOp:

    pass
class boa_ArithOpMinus(ArithOp):

    pass
class boa_ArithOpDivide(ArithOp):

    pass
class boa_ArithOpRemainder(ArithOp):

    pass
class boa_ArithOpTimes(ArithOp):

    pass
class boa_ArithOpPlus(ArithOp):

    pass
class boa_Field:

    def __init__(self, name: str, boa_Field: "boa_BObject" = None, boa_Field11: "boa_Expr" = None):
        self.name = name
        self.boa_Field = boa_Field
        self.boa_Field11 = boa_Field11
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def boa_Field11(self):
        return self.__boa_Field11

    @boa_Field11.setter
    def boa_Field11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_boa_Field__boa_Field11", None)
        self.__boa_Field11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "boa_Expr12"):
                opp_val = getattr(old_value, "boa_Expr12", None)
                if opp_val == self:
                    setattr(old_value, "boa_Expr12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "boa_Expr12"):
                opp_val = getattr(value, "boa_Expr12", None)
                setattr(value, "boa_Expr12", self)

    @property
    def boa_Field(self):
        return self.__boa_Field

    @boa_Field.setter
    def boa_Field(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_boa_Field__boa_Field", None)
        self.__boa_Field = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "boa_BObject"):
                opp_val = getattr(old_value, "boa_BObject", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "boa_BObject"):
                opp_val = getattr(value, "boa_BObject", None)
                if opp_val is None:
                    setattr(value, "boa_BObject", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Expr:

    pass
class boa_Project(Expr):

    def __init__(self, name: str, boa_Project: "boa_Expr" = None):
        self.name = name
        self.boa_Project = boa_Project
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def boa_Project(self):
        return self.__boa_Project

    @boa_Project.setter
    def boa_Project(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_boa_Project__boa_Project", None)
        self.__boa_Project = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "boa_Expr8"):
                opp_val = getattr(old_value, "boa_Expr8", None)
                if opp_val == self:
                    setattr(old_value, "boa_Expr8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "boa_Expr8"):
                opp_val = getattr(value, "boa_Expr8", None)
                setattr(value, "boa_Expr8", self)

class boa_ArithOp(Expr):

    pass
class boa_Bool(Expr):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class boa_Assign(Expr):

    def __init__(self, name: str, boa_Assign: "boa_Expr" = None, boa_Assign50: "boa_Expr" = None):
        self.name = name
        self.boa_Assign = boa_Assign
        self.boa_Assign50 = boa_Assign50
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def boa_Assign50(self):
        return self.__boa_Assign50

    @boa_Assign50.setter
    def boa_Assign50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_boa_Assign__boa_Assign50", None)
        self.__boa_Assign50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "boa_Expr51"):
                opp_val = getattr(old_value, "boa_Expr51", None)
                if opp_val == self:
                    setattr(old_value, "boa_Expr51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "boa_Expr51"):
                opp_val = getattr(value, "boa_Expr51", None)
                setattr(value, "boa_Expr51", self)

    @property
    def boa_Assign(self):
        return self.__boa_Assign

    @boa_Assign.setter
    def boa_Assign(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_boa_Assign__boa_Assign", None)
        self.__boa_Assign = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "boa_Expr48"):
                opp_val = getattr(old_value, "boa_Expr48", None)
                if opp_val == self:
                    setattr(old_value, "boa_Expr48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "boa_Expr48"):
                opp_val = getattr(value, "boa_Expr48", None)
                setattr(value, "boa_Expr48", self)

class boa_BoolOp(Expr):

    pass
class boa_This(Expr):

    pass
class boa_Var(Expr):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class boa_Int(Expr):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class boa_Fun(Expr):

    def __init__(self, name: str, boa_Fun: "boa_Expr" = None):
        self.name = name
        self.boa_Fun = boa_Fun
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def boa_Fun(self):
        return self.__boa_Fun

    @boa_Fun.setter
    def boa_Fun(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_boa_Fun__boa_Fun", None)
        self.__boa_Fun = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "boa_Expr46"):
                opp_val = getattr(old_value, "boa_Expr46", None)
                if opp_val == self:
                    setattr(old_value, "boa_Expr46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "boa_Expr46"):
                opp_val = getattr(value, "boa_Expr46", None)
                setattr(value, "boa_Expr46", self)

class boa_CmpOp(Expr):

    pass
class boa_Not(Expr):

    pass
class boa_If(Expr):

    pass
class boa_Seq(Expr):

    pass
class boa_BObject(Expr):

    pass
class boa_Copy(Expr):

    pass
class boa_Skip(Expr):

    pass
class boa_With(Expr):

    pass
class boa_Let(Expr):

    def __init__(self, name: str, boa_Let: "boa_Expr" = None, boa_Let43: "boa_Expr" = None):
        self.name = name
        self.boa_Let = boa_Let
        self.boa_Let43 = boa_Let43
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def boa_Let(self):
        return self.__boa_Let

    @boa_Let.setter
    def boa_Let(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_boa_Let__boa_Let", None)
        self.__boa_Let = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "boa_Expr41"):
                opp_val = getattr(old_value, "boa_Expr41", None)
                if opp_val == self:
                    setattr(old_value, "boa_Expr41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "boa_Expr41"):
                opp_val = getattr(value, "boa_Expr41", None)
                setattr(value, "boa_Expr41", self)

    @property
    def boa_Let43(self):
        return self.__boa_Let43

    @boa_Let43.setter
    def boa_Let43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_boa_Let__boa_Let43", None)
        self.__boa_Let43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "boa_Expr44"):
                opp_val = getattr(old_value, "boa_Expr44", None)
                if opp_val == self:
                    setattr(old_value, "boa_Expr44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "boa_Expr44"):
                opp_val = getattr(value, "boa_Expr44", None)
                setattr(value, "boa_Expr44", self)

class boa_App(Expr):

    pass
class TopLevelCmd:

    pass
class boa_Def(TopLevelCmd):

    def __init__(self, name: str, boa_Def: "boa_Expr" = None):
        self.name = name
        self.boa_Def = boa_Def
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def boa_Def(self):
        return self.__boa_Def

    @boa_Def.setter
    def boa_Def(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_boa_Def__boa_Def", None)
        self.__boa_Def = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "boa_Expr"):
                opp_val = getattr(old_value, "boa_Expr", None)
                if opp_val == self:
                    setattr(old_value, "boa_Expr", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "boa_Expr"):
                opp_val = getattr(value, "boa_Expr", None)
                setattr(value, "boa_Expr", self)

class boa_Expr(TopLevelCmd):

    pass
class boa_TopLevelCmd(ABC):

    pass
class boa_File:

    pass