from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class SecType(Enum):
    PRIVATE = "PRIVATE"
    PUBLIC = "PUBLIC"
class BlockType(Enum):
    INSERT = "INSERT"
    COMP = "COMP"
    SEARCH = "SEARCH"
    ANONYMIZATION = "ANONYMIZATION"
    ACCESS = "ACCESS"
    PERMISSION = "PERMISSION"
class BasicType(Enum):
    INT = "INT"
    DOUBLE = "DOUBLE"
    BOOLEAN = "BOOLEAN"
    STRING = "STRING"
    ENCRYPTED = "ENCRYPTED"


############################################
# Definition of Classes
############################################

class AccessControl:

    pass
class smc_Covered(AccessControl):

    pass
class smc_BellLapadula(AccessControl):

    def __init__(self, mode: str, smc_BellLapadula: "smc_VariableDecl" = None):
        self.mode = mode
        self.smc_BellLapadula = smc_BellLapadula
        
    @property
    def mode(self) -> str:
        return self.__mode

    @mode.setter
    def mode(self, mode: str):
        self.__mode = mode

    @property
    def smc_BellLapadula(self):
        return self.__smc_BellLapadula

    @smc_BellLapadula.setter
    def smc_BellLapadula(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smc_BellLapadula__smc_BellLapadula", None)
        self.__smc_BellLapadula = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smc_VariableDecl67"):
                opp_val = getattr(old_value, "smc_VariableDecl67", None)
                if opp_val == self:
                    setattr(old_value, "smc_VariableDecl67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smc_VariableDecl67"):
                opp_val = getattr(value, "smc_VariableDecl67", None)
                setattr(value, "smc_VariableDecl67", self)

class Functions:

    pass
class smc_CreateTable(Functions):

    pass
class smc_AddValues(Functions):

    pass
class smc_CheckTable(Functions):

    pass
class smc_BloomFilter(Functions):

    pass
class smc_AccessControl(Functions):

    pass
class smc_Search(Functions):

    def __init__(self, column: str, smc_Search: "smc_VariableDecl" = None, smc_Search76: "smc_VariableDecl" = None):
        self.column = column
        self.smc_Search = smc_Search
        self.smc_Search76 = smc_Search76
        
    @property
    def column(self) -> str:
        return self.__column

    @column.setter
    def column(self, column: str):
        self.__column = column

    @property
    def smc_Search76(self):
        return self.__smc_Search76

    @smc_Search76.setter
    def smc_Search76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smc_Search__smc_Search76", None)
        self.__smc_Search76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smc_VariableDecl77"):
                opp_val = getattr(old_value, "smc_VariableDecl77", None)
                if opp_val == self:
                    setattr(old_value, "smc_VariableDecl77", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smc_VariableDecl77"):
                opp_val = getattr(value, "smc_VariableDecl77", None)
                setattr(value, "smc_VariableDecl77", self)

    @property
    def smc_Search(self):
        return self.__smc_Search

    @smc_Search.setter
    def smc_Search(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smc_Search__smc_Search", None)
        self.__smc_Search = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smc_VariableDecl74"):
                opp_val = getattr(old_value, "smc_VariableDecl74", None)
                if opp_val == self:
                    setattr(old_value, "smc_VariableDecl74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smc_VariableDecl74"):
                opp_val = getattr(value, "smc_VariableDecl74", None)
                setattr(value, "smc_VariableDecl74", self)

class smc_Computation(Functions):

    pass
class smc_Functions:

    pass
class Computation:

    pass
class smc_WeightedAvg(Computation):

    pass
class smc_Median(Computation):

    pass
class smc_Average(Computation):

    pass
class smc_Count(Computation):

    pass
class smc_Multiplication(Computation):

    pass
class Download:

    pass
class smc_Client(Download):

    def __init__(self, arg: str):
        self.arg = arg
        
    @property
    def arg(self) -> str:
        return self.__arg

    @arg.setter
    def arg(self, arg: str):
        self.__arg = arg

class smc_Database(Download):

    def __init__(self, clm: str, smc_Database: "smc_Expression" = None):
        self.clm = clm
        self.smc_Database = smc_Database
        
    @property
    def clm(self) -> str:
        return self.__clm

    @clm.setter
    def clm(self, clm: str):
        self.__clm = clm

    @property
    def smc_Database(self):
        return self.__smc_Database

    @smc_Database.setter
    def smc_Database(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smc_Database__smc_Database", None)
        self.__smc_Database = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smc_Expression27"):
                opp_val = getattr(old_value, "smc_Expression27", None)
                if opp_val == self:
                    setattr(old_value, "smc_Expression27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smc_Expression27"):
                opp_val = getattr(value, "smc_Expression27", None)
                setattr(value, "smc_Expression27", self)

class AbstractAssignment:

    pass
class smc_Download(AbstractAssignment):

    pass
class Expression:

    pass
class smc_DoubleLiteral(Expression):

    def __init__(self, value: float):
        self.value = value
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

class smc_TimeLiteral(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class smc_Comparison(Expression):

    def __init__(self, op: str, smc_Comparison114: "smc_Expression" = None, smc_Comparison: "smc_Expression" = None):
        self.op = op
        self.smc_Comparison114 = smc_Comparison114
        self.smc_Comparison = smc_Comparison
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def smc_Comparison(self):
        return self.__smc_Comparison

    @smc_Comparison.setter
    def smc_Comparison(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smc_Comparison__smc_Comparison", None)
        self.__smc_Comparison = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smc_Expression112"):
                opp_val = getattr(old_value, "smc_Expression112", None)
                if opp_val == self:
                    setattr(old_value, "smc_Expression112", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smc_Expression112"):
                opp_val = getattr(value, "smc_Expression112", None)
                setattr(value, "smc_Expression112", self)

    @property
    def smc_Comparison114(self):
        return self.__smc_Comparison114

    @smc_Comparison114.setter
    def smc_Comparison114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smc_Comparison__smc_Comparison114", None)
        self.__smc_Comparison114 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smc_Expression115"):
                opp_val = getattr(old_value, "smc_Expression115", None)
                if opp_val == self:
                    setattr(old_value, "smc_Expression115", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smc_Expression115"):
                opp_val = getattr(value, "smc_Expression115", None)
                setattr(value, "smc_Expression115", self)

class smc_StringLiteral(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class smc_PlusOrMinus(Expression):

    def __init__(self, op: str, smc_PlusOrMinus: "smc_Expression" = None, smc_PlusOrMinus119: "smc_Expression" = None):
        self.op = op
        self.smc_PlusOrMinus = smc_PlusOrMinus
        self.smc_PlusOrMinus119 = smc_PlusOrMinus119
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def smc_PlusOrMinus(self):
        return self.__smc_PlusOrMinus

    @smc_PlusOrMinus.setter
    def smc_PlusOrMinus(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smc_PlusOrMinus__smc_PlusOrMinus", None)
        self.__smc_PlusOrMinus = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smc_Expression117"):
                opp_val = getattr(old_value, "smc_Expression117", None)
                if opp_val == self:
                    setattr(old_value, "smc_Expression117", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smc_Expression117"):
                opp_val = getattr(value, "smc_Expression117", None)
                setattr(value, "smc_Expression117", self)

    @property
    def smc_PlusOrMinus119(self):
        return self.__smc_PlusOrMinus119

    @smc_PlusOrMinus119.setter
    def smc_PlusOrMinus119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smc_PlusOrMinus__smc_PlusOrMinus119", None)
        self.__smc_PlusOrMinus119 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smc_Expression120"):
                opp_val = getattr(old_value, "smc_Expression120", None)
                if opp_val == self:
                    setattr(old_value, "smc_Expression120", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smc_Expression120"):
                opp_val = getattr(value, "smc_Expression120", None)
                setattr(value, "smc_Expression120", self)

class smc_BooleanLiteral(Expression):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class smc_Or(Expression):

    pass
class smc_And(Expression):

    pass
class smc_Equality(Expression):

    def __init__(self, op: str, smc_Equality: "smc_Expression" = None, smc_Equality109: "smc_Expression" = None):
        self.op = op
        self.smc_Equality = smc_Equality
        self.smc_Equality109 = smc_Equality109
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def smc_Equality(self):
        return self.__smc_Equality

    @smc_Equality.setter
    def smc_Equality(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smc_Equality__smc_Equality", None)
        self.__smc_Equality = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smc_Expression107"):
                opp_val = getattr(old_value, "smc_Expression107", None)
                if opp_val == self:
                    setattr(old_value, "smc_Expression107", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smc_Expression107"):
                opp_val = getattr(value, "smc_Expression107", None)
                setattr(value, "smc_Expression107", self)

    @property
    def smc_Equality109(self):
        return self.__smc_Equality109

    @smc_Equality109.setter
    def smc_Equality109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smc_Equality__smc_Equality109", None)
        self.__smc_Equality109 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smc_Expression110"):
                opp_val = getattr(old_value, "smc_Expression110", None)
                if opp_val == self:
                    setattr(old_value, "smc_Expression110", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smc_Expression110"):
                opp_val = getattr(value, "smc_Expression110", None)
                setattr(value, "smc_Expression110", self)

class smc_MulOrDiv(Expression):

    def __init__(self, op: str, smc_MulOrDiv: "smc_Expression" = None, smc_MulOrDiv124: "smc_Expression" = None):
        self.op = op
        self.smc_MulOrDiv = smc_MulOrDiv
        self.smc_MulOrDiv124 = smc_MulOrDiv124
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def smc_MulOrDiv124(self):
        return self.__smc_MulOrDiv124

    @smc_MulOrDiv124.setter
    def smc_MulOrDiv124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smc_MulOrDiv__smc_MulOrDiv124", None)
        self.__smc_MulOrDiv124 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smc_Expression125"):
                opp_val = getattr(old_value, "smc_Expression125", None)
                if opp_val == self:
                    setattr(old_value, "smc_Expression125", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smc_Expression125"):
                opp_val = getattr(value, "smc_Expression125", None)
                setattr(value, "smc_Expression125", self)

    @property
    def smc_MulOrDiv(self):
        return self.__smc_MulOrDiv

    @smc_MulOrDiv.setter
    def smc_MulOrDiv(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smc_MulOrDiv__smc_MulOrDiv", None)
        self.__smc_MulOrDiv = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smc_Expression122"):
                opp_val = getattr(old_value, "smc_Expression122", None)
                if opp_val == self:
                    setattr(old_value, "smc_Expression122", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smc_Expression122"):
                opp_val = getattr(value, "smc_Expression122", None)
                setattr(value, "smc_Expression122", self)

class smc_IntLiteral(Expression):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class smc_Not(Expression):

    pass
class smc_List(Expression):

    pass
class smc_DateLiteral(Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class smc_VariableRef(Expression):

    pass
class smc_Dict(Expression):

    pass
class smc_Tuple(Expression):

    pass
class smc_AbstractAssignment:

    pass
class smc_Expression(AbstractAssignment):

    pass
class smc_Invocation(Expression):

    pass
class Command:

    pass
class smc_IfThenElse(Command):

    pass
class smc_Print(Command):

    pass
class smc_Block(Command):

    pass
class smc_InvocationVoid(Command):

    pass
class smc_VariableDecl(Command):

    def __init__(self, visibility: str, type: str, array: bool, length: int, name: str, smc_VariableDecl: "smc_AbstractAssignment" = None, smc_VariableDecl22: "smc_VariableAssignment" = None, smc_VariableDecl46: "smc_Multiplication" = None, smc_VariableDecl65: "smc_AccessControl" = None, smc_VariableDecl49: "smc_Multiplication" = None, smc_VariableDecl51: "smc_Median" = None, smc_VariableDecl53: "smc_WeightedAvg" = None, smc_VariableDecl56: "smc_WeightedAvg" = None, smc_VariableDecl58: "smc_Average" = None, smc_VariableDecl60: "smc_Count" = None, smc_VariableDecl62: "smc_AccessControl" = None, smc_VariableDecl82: "smc_BloomFilter" = None, smc_VariableDecl67: "smc_BellLapadula" = None, smc_VariableDecl69: "smc_Covered" = None, smc_VariableDecl72: "smc_Covered" = None, smc_VariableDecl74: "smc_Search" = None, smc_VariableDecl77: "smc_Search" = None, smc_VariableDecl79: "smc_BloomFilter" = None, smc_VariableDecl84: "smc_CheckTable" = None, smc_VariableDecl86: "smc_AddValues" = None, smc_VariableDecl89: "smc_AddValues" = None, smc_VariableDecl91: "smc_CreateTable" = None, smc_VariableDecl129: "smc_VariableRef" = None):
        self.visibility = visibility
        self.type = type
        self.array = array
        self.length = length
        self.name = name
        self.smc_VariableDecl = smc_VariableDecl
        self.smc_VariableDecl22 = smc_VariableDecl22
        self.smc_VariableDecl46 = smc_VariableDecl46
        self.smc_VariableDecl65 = smc_VariableDecl65
        self.smc_VariableDecl49 = smc_VariableDecl49
        self.smc_VariableDecl51 = smc_VariableDecl51
        self.smc_VariableDecl53 = smc_VariableDecl53
        self.smc_VariableDecl56 = smc_VariableDecl56
        self.smc_VariableDecl58 = smc_VariableDecl58
        self.smc_VariableDecl60 = smc_VariableDecl60
        self.smc_VariableDecl62 = smc_VariableDecl62
        self.smc_VariableDecl82 = smc_VariableDecl82
        self.smc_VariableDecl67 = smc_VariableDecl67
        self.smc_VariableDecl69 = smc_VariableDecl69
        self.smc_VariableDecl72 = smc_VariableDecl72
        self.smc_VariableDecl74 = smc_VariableDecl74
        self.smc_VariableDecl77 = smc_VariableDecl77
        self.smc_VariableDecl79 = smc_VariableDecl79
        self.smc_VariableDecl84 = smc_VariableDecl84
        self.smc_VariableDecl86 = smc_VariableDecl86
        self.smc_VariableDecl89 = smc_VariableDecl89
        self.smc_VariableDecl91 = smc_VariableDecl91
        self.smc_VariableDecl129 = smc_VariableDecl129
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def array(self) -> bool:
        return self.__array

    @array.setter
    def array(self, array: bool):
        self.__array = array

    @property
    def length(self) -> int:
        return self.__length

    @length.setter
    def length(self, length: int):
        self.__length = length

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def smc_VariableDecl129(self):
        return self.__smc_VariableDecl129

    @smc_VariableDecl129.setter
    def smc_VariableDecl129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smc_VariableDecl__smc_VariableDecl129", None)
        self.__smc_VariableDecl129 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smc_VariableRef"):
                opp_val = getattr(old_value, "smc_VariableRef", None)
                if opp_val == self:
                    setattr(old_value, "smc_VariableRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smc_VariableRef"):
                opp_val = getattr(value, "smc_VariableRef", None)
                setattr(value, "smc_VariableRef", self)

    @property
    def smc_VariableDecl84(self):
        return self.__smc_VariableDecl84

    @smc_VariableDecl84.setter
    def smc_VariableDecl84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smc_VariableDecl__smc_VariableDecl84", None)
        self.__smc_VariableDecl84 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smc_CheckTable"):
                opp_val = getattr(old_value, "smc_CheckTable", None)
                if opp_val == self:
                    setattr(old_value, "smc_CheckTable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smc_CheckTable"):
                opp_val = getattr(value, "smc_CheckTable", None)
                setattr(value, "smc_CheckTable", self)

    @property
    def smc_VariableDecl72(self):
        return self.__smc_VariableDecl72

    @smc_VariableDecl72.setter
    def smc_VariableDecl72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smc_VariableDecl__smc_VariableDecl72", None)
        self.__smc_VariableDecl72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smc_Covered71"):
                opp_val = getattr(old_value, "smc_Covered71", None)
                if opp_val == self:
                    setattr(old_value, "smc_Covered71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smc_Covered71"):
                opp_val = getattr(value, "smc_Covered71", None)
                setattr(value, "smc_Covered71", self)

    @property
    def smc_VariableDecl86(self):
        return self.__smc_VariableDecl86

    @smc_VariableDecl86.setter
    def smc_VariableDecl86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smc_VariableDecl__smc_VariableDecl86", None)
        self.__smc_VariableDecl86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smc_AddValues"):
                opp_val = getattr(old_value, "smc_AddValues", None)
                if opp_val == self:
                    setattr(old_value, "smc_AddValues", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smc_AddValues"):
                opp_val = getattr(value, "smc_AddValues", None)
                setattr(value, "smc_AddValues", self)

    @property
    def smc_VariableDecl69(self):
        return self.__smc_VariableDecl69

    @smc_VariableDecl69.setter
    def smc_VariableDecl69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smc_VariableDecl__smc_VariableDecl69", None)
        self.__smc_VariableDecl69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smc_Covered"):
                opp_val = getattr(old_value, "smc_Covered", None)
                if opp_val == self:
                    setattr(old_value, "smc_Covered", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smc_Covered"):
                opp_val = getattr(value, "smc_Covered", None)
                setattr(value, "smc_Covered", self)

    @property
    def smc_VariableDecl65(self):
        return self.__smc_VariableDecl65

    @smc_VariableDecl65.setter
    def smc_VariableDecl65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smc_VariableDecl__smc_VariableDecl65", None)
        self.__smc_VariableDecl65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smc_AccessControl64"):
                opp_val = getattr(old_value, "smc_AccessControl64", None)
                if opp_val == self:
                    setattr(old_value, "smc_AccessControl64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smc_AccessControl64"):
                opp_val = getattr(value, "smc_AccessControl64", None)
                setattr(value, "smc_AccessControl64", self)

    @property
    def smc_VariableDecl91(self):
        return self.__smc_VariableDecl91

    @smc_VariableDecl91.setter
    def smc_VariableDecl91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smc_VariableDecl__smc_VariableDecl91", None)
        self.__smc_VariableDecl91 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smc_CreateTable"):
                opp_val = getattr(old_value, "smc_CreateTable", None)
                if opp_val == self:
                    setattr(old_value, "smc_CreateTable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smc_CreateTable"):
                opp_val = getattr(value, "smc_CreateTable", None)
                setattr(value, "smc_CreateTable", self)

    @property
    def smc_VariableDecl82(self):
        return self.__smc_VariableDecl82

    @smc_VariableDecl82.setter
    def smc_VariableDecl82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smc_VariableDecl__smc_VariableDecl82", None)
        self.__smc_VariableDecl82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smc_BloomFilter81"):
                opp_val = getattr(old_value, "smc_BloomFilter81", None)
                if opp_val == self:
                    setattr(old_value, "smc_BloomFilter81", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smc_BloomFilter81"):
                opp_val = getattr(value, "smc_BloomFilter81", None)
                setattr(value, "smc_BloomFilter81", self)

    @property
    def smc_VariableDecl77(self):
        return self.__smc_VariableDecl77

    @smc_VariableDecl77.setter
    def smc_VariableDecl77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smc_VariableDecl__smc_VariableDecl77", None)
        self.__smc_VariableDecl77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smc_Search76"):
                opp_val = getattr(old_value, "smc_Search76", None)
                if opp_val == self:
                    setattr(old_value, "smc_Search76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smc_Search76"):
                opp_val = getattr(value, "smc_Search76", None)
                setattr(value, "smc_Search76", self)

    @property
    def smc_VariableDecl51(self):
        return self.__smc_VariableDecl51

    @smc_VariableDecl51.setter
    def smc_VariableDecl51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smc_VariableDecl__smc_VariableDecl51", None)
        self.__smc_VariableDecl51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smc_Median"):
                opp_val = getattr(old_value, "smc_Median", None)
                if opp_val == self:
                    setattr(old_value, "smc_Median", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smc_Median"):
                opp_val = getattr(value, "smc_Median", None)
                setattr(value, "smc_Median", self)

    @property
    def smc_VariableDecl79(self):
        return self.__smc_VariableDecl79

    @smc_VariableDecl79.setter
    def smc_VariableDecl79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smc_VariableDecl__smc_VariableDecl79", None)
        self.__smc_VariableDecl79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smc_BloomFilter"):
                opp_val = getattr(old_value, "smc_BloomFilter", None)
                if opp_val == self:
                    setattr(old_value, "smc_BloomFilter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smc_BloomFilter"):
                opp_val = getattr(value, "smc_BloomFilter", None)
                setattr(value, "smc_BloomFilter", self)

    @property
    def smc_VariableDecl(self):
        return self.__smc_VariableDecl

    @smc_VariableDecl.setter
    def smc_VariableDecl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smc_VariableDecl__smc_VariableDecl", None)
        self.__smc_VariableDecl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smc_AbstractAssignment"):
                opp_val = getattr(old_value, "smc_AbstractAssignment", None)
                if opp_val == self:
                    setattr(old_value, "smc_AbstractAssignment", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smc_AbstractAssignment"):
                opp_val = getattr(value, "smc_AbstractAssignment", None)
                setattr(value, "smc_AbstractAssignment", self)

    @property
    def smc_VariableDecl67(self):
        return self.__smc_VariableDecl67

    @smc_VariableDecl67.setter
    def smc_VariableDecl67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smc_VariableDecl__smc_VariableDecl67", None)
        self.__smc_VariableDecl67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smc_BellLapadula"):
                opp_val = getattr(old_value, "smc_BellLapadula", None)
                if opp_val == self:
                    setattr(old_value, "smc_BellLapadula", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smc_BellLapadula"):
                opp_val = getattr(value, "smc_BellLapadula", None)
                setattr(value, "smc_BellLapadula", self)

    @property
    def smc_VariableDecl46(self):
        return self.__smc_VariableDecl46

    @smc_VariableDecl46.setter
    def smc_VariableDecl46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smc_VariableDecl__smc_VariableDecl46", None)
        self.__smc_VariableDecl46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smc_Multiplication"):
                opp_val = getattr(old_value, "smc_Multiplication", None)
                if opp_val == self:
                    setattr(old_value, "smc_Multiplication", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smc_Multiplication"):
                opp_val = getattr(value, "smc_Multiplication", None)
                setattr(value, "smc_Multiplication", self)

    @property
    def smc_VariableDecl74(self):
        return self.__smc_VariableDecl74

    @smc_VariableDecl74.setter
    def smc_VariableDecl74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smc_VariableDecl__smc_VariableDecl74", None)
        self.__smc_VariableDecl74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smc_Search"):
                opp_val = getattr(old_value, "smc_Search", None)
                if opp_val == self:
                    setattr(old_value, "smc_Search", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smc_Search"):
                opp_val = getattr(value, "smc_Search", None)
                setattr(value, "smc_Search", self)

    @property
    def smc_VariableDecl22(self):
        return self.__smc_VariableDecl22

    @smc_VariableDecl22.setter
    def smc_VariableDecl22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smc_VariableDecl__smc_VariableDecl22", None)
        self.__smc_VariableDecl22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smc_VariableAssignment"):
                opp_val = getattr(old_value, "smc_VariableAssignment", None)
                if opp_val == self:
                    setattr(old_value, "smc_VariableAssignment", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smc_VariableAssignment"):
                opp_val = getattr(value, "smc_VariableAssignment", None)
                setattr(value, "smc_VariableAssignment", self)

    @property
    def smc_VariableDecl53(self):
        return self.__smc_VariableDecl53

    @smc_VariableDecl53.setter
    def smc_VariableDecl53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smc_VariableDecl__smc_VariableDecl53", None)
        self.__smc_VariableDecl53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smc_WeightedAvg"):
                opp_val = getattr(old_value, "smc_WeightedAvg", None)
                if opp_val == self:
                    setattr(old_value, "smc_WeightedAvg", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smc_WeightedAvg"):
                opp_val = getattr(value, "smc_WeightedAvg", None)
                setattr(value, "smc_WeightedAvg", self)

    @property
    def smc_VariableDecl49(self):
        return self.__smc_VariableDecl49

    @smc_VariableDecl49.setter
    def smc_VariableDecl49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smc_VariableDecl__smc_VariableDecl49", None)
        self.__smc_VariableDecl49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smc_Multiplication48"):
                opp_val = getattr(old_value, "smc_Multiplication48", None)
                if opp_val == self:
                    setattr(old_value, "smc_Multiplication48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smc_Multiplication48"):
                opp_val = getattr(value, "smc_Multiplication48", None)
                setattr(value, "smc_Multiplication48", self)

    @property
    def smc_VariableDecl58(self):
        return self.__smc_VariableDecl58

    @smc_VariableDecl58.setter
    def smc_VariableDecl58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smc_VariableDecl__smc_VariableDecl58", None)
        self.__smc_VariableDecl58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smc_Average"):
                opp_val = getattr(old_value, "smc_Average", None)
                if opp_val == self:
                    setattr(old_value, "smc_Average", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smc_Average"):
                opp_val = getattr(value, "smc_Average", None)
                setattr(value, "smc_Average", self)

    @property
    def smc_VariableDecl56(self):
        return self.__smc_VariableDecl56

    @smc_VariableDecl56.setter
    def smc_VariableDecl56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smc_VariableDecl__smc_VariableDecl56", None)
        self.__smc_VariableDecl56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smc_WeightedAvg55"):
                opp_val = getattr(old_value, "smc_WeightedAvg55", None)
                if opp_val == self:
                    setattr(old_value, "smc_WeightedAvg55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smc_WeightedAvg55"):
                opp_val = getattr(value, "smc_WeightedAvg55", None)
                setattr(value, "smc_WeightedAvg55", self)

    @property
    def smc_VariableDecl60(self):
        return self.__smc_VariableDecl60

    @smc_VariableDecl60.setter
    def smc_VariableDecl60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smc_VariableDecl__smc_VariableDecl60", None)
        self.__smc_VariableDecl60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smc_Count"):
                opp_val = getattr(old_value, "smc_Count", None)
                if opp_val == self:
                    setattr(old_value, "smc_Count", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smc_Count"):
                opp_val = getattr(value, "smc_Count", None)
                setattr(value, "smc_Count", self)

    @property
    def smc_VariableDecl62(self):
        return self.__smc_VariableDecl62

    @smc_VariableDecl62.setter
    def smc_VariableDecl62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smc_VariableDecl__smc_VariableDecl62", None)
        self.__smc_VariableDecl62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smc_AccessControl"):
                opp_val = getattr(old_value, "smc_AccessControl", None)
                if opp_val == self:
                    setattr(old_value, "smc_AccessControl", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smc_AccessControl"):
                opp_val = getattr(value, "smc_AccessControl", None)
                setattr(value, "smc_AccessControl", self)

    @property
    def smc_VariableDecl89(self):
        return self.__smc_VariableDecl89

    @smc_VariableDecl89.setter
    def smc_VariableDecl89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smc_VariableDecl__smc_VariableDecl89", None)
        self.__smc_VariableDecl89 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smc_AddValues88"):
                opp_val = getattr(old_value, "smc_AddValues88", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smc_AddValues88"):
                opp_val = getattr(value, "smc_AddValues88", None)
                if opp_val is None:
                    setattr(value, "smc_AddValues88", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class smc_VariableAssignment(Command):

    pass
class smc_Return(Command):

    pass
class smc_ParamDecl(Command):

    def __init__(self, name: str, stype: str, btype: str, parName: str, smc_ParamDecl: "smc_CreateTable" = None):
        self.name = name
        self.stype = stype
        self.btype = btype
        self.parName = parName
        self.smc_ParamDecl = smc_ParamDecl
        
    @property
    def btype(self) -> str:
        return self.__btype

    @btype.setter
    def btype(self, btype: str):
        self.__btype = btype

    @property
    def stype(self) -> str:
        return self.__stype

    @stype.setter
    def stype(self, stype: str):
        self.__stype = stype

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def parName(self) -> str:
        return self.__parName

    @parName.setter
    def parName(self, parName: str):
        self.__parName = parName

    @property
    def smc_ParamDecl(self):
        return self.__smc_ParamDecl

    @smc_ParamDecl.setter
    def smc_ParamDecl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smc_ParamDecl__smc_ParamDecl", None)
        self.__smc_ParamDecl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smc_CreateTable93"):
                opp_val = getattr(old_value, "smc_CreateTable93", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smc_CreateTable93"):
                opp_val = getattr(value, "smc_CreateTable93", None)
                if opp_val is None:
                    setattr(value, "smc_CreateTable93", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class smc_Command:

    pass
class smc_While(Command):

    pass
class smc_MainSMC:

    pass
class smc_BlockSMC:

    def __init__(self, type: str, name: str, smc_BlockSMC: "smc_Smc" = None, smc_BlockSMC42: "smc_Invocation" = None):
        self.type = type
        self.name = name
        self.smc_BlockSMC = smc_BlockSMC
        self.smc_BlockSMC42 = smc_BlockSMC42
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def smc_BlockSMC42(self):
        return self.__smc_BlockSMC42

    @smc_BlockSMC42.setter
    def smc_BlockSMC42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smc_BlockSMC__smc_BlockSMC42", None)
        self.__smc_BlockSMC42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smc_Invocation41"):
                opp_val = getattr(old_value, "smc_Invocation41", None)
                if opp_val == self:
                    setattr(old_value, "smc_Invocation41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smc_Invocation41"):
                opp_val = getattr(value, "smc_Invocation41", None)
                setattr(value, "smc_Invocation41", self)

    @property
    def smc_BlockSMC(self):
        return self.__smc_BlockSMC

    @smc_BlockSMC.setter
    def smc_BlockSMC(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smc_BlockSMC__smc_BlockSMC", None)
        self.__smc_BlockSMC = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smc_Smc"):
                opp_val = getattr(old_value, "smc_Smc", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smc_Smc"):
                opp_val = getattr(value, "smc_Smc", None)
                if opp_val is None:
                    setattr(value, "smc_Smc", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class smc_Smc:

    pass