from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class BooleanUnaryOperator(Enum):
    NOT = "NOT"
class BoardType(Enum):
    RaspberryPi = "RaspberryPi"
    Arduino = "Arduino"
    BeagleBoard = "BeagleBoard"
class BooleanBinaryOperator(Enum):
    AND = "AND"
    OR = "OR"
class IntegerComparisonOperator(Enum):
    SMALLER = "SMALLER"
    SMALLER_EQUALS = "SMALLER_EQUALS"
    EQUALS = "EQUALS"
    GREATER_EQUALS = "GREATER_EQUALS"
    GREATER = "GREATER"
class PrimitiveKind(Enum):
    PK_ULONGLONG = "PK_ULONGLONG"
    PK_OBJREF = "PK_OBJREF"
    PK_LONGLONG = "PK_LONGLONG"
    PK_NULL = "PK_NULL"
    PK_VOID = "PK_VOID"
    PK_SHORT = "PK_SHORT"
    PK_LONG = "PK_LONG"
    PK_USHORT = "PK_USHORT"
    PK_ULONG = "PK_ULONG"
    PK_FLOAT = "PK_FLOAT"
    PK_DOUBLE = "PK_DOUBLE"
    PK_BOOLEAN = "PK_BOOLEAN"
    PK_CHAR = "PK_CHAR"
    PK_OCTET = "PK_OCTET"
    PK_ANY = "PK_ANY"
    PK_LONGDOUBLE = "PK_LONGDOUBLE"
    PK_WSTRING = "PK_WSTRING"
    PK_TYPECODE = "PK_TYPECODE"
    PK_WCHAR = "PK_WCHAR"
    PK_PRINCIPAL = "PK_PRINCIPAL"
    PK_STRING = "PK_STRING"
class ParameterMode(Enum):
    PARAM_IN = "PARAM_IN"
    PARAM_OUT = "PARAM_OUT"
    PARAM_INOUT = "PARAM_INOUT"
class IntegerCalculationOperator(Enum):
    ADD = "ADD"
    SUBRACT = "SUBRACT"


############################################
# Definition of Classes
############################################

class LastStatement_Return:

    pass
class iot2_LastStatement_ReturnWithValue(LastStatement_Return):

    def __init__(self, iot2_LastStatement_ReturnWithValue: set["iot2_Expression"] = None):
        self.iot2_LastStatement_ReturnWithValue = iot2_LastStatement_ReturnWithValue if iot2_LastStatement_ReturnWithValue is not None else set()
        
        pass
    @property
    def iot2_LastStatement_ReturnWithValue(self):
        return self.__iot2_LastStatement_ReturnWithValue

    @iot2_LastStatement_ReturnWithValue.setter
    def iot2_LastStatement_ReturnWithValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_LastStatement_ReturnWithValue__iot2_LastStatement_ReturnWithValue", None)
        self.__iot2_LastStatement_ReturnWithValue = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iot2_Expression100"):
                    opp_val = getattr(item, "iot2_Expression100", None)
                    
                    if opp_val == self:
                        setattr(item, "iot2_Expression100", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iot2_Expression100"):
                    opp_val = getattr(item, "iot2_Expression100", None)
                    
                    setattr(item, "iot2_Expression100", self)
                    

    def execute(self, iot2_c):
        # TODO: Implement execute method
        pass

class Field:

    pass
class iot2_Field_AddEntryToTable(Field):

    def __init__(self, key: str):
        self.key = key
        
        pass
    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key


    def execute(self, iot2_c):
        # TODO: Implement execute method
        pass

class iot2_Field_AppendEntryToTable(Field):

    def __init__(self):
        
        pass
    def execute(self, iot2_c):
        # TODO: Implement execute method
        pass

class iot2_Field_AddEntryToTable_Brackets(Field):

    def __init__(self, iot2_Field_AddEntryToTable_Brackets: "iot2_Expression" = None):
        self.iot2_Field_AddEntryToTable_Brackets = iot2_Field_AddEntryToTable_Brackets
        
        pass
    @property
    def iot2_Field_AddEntryToTable_Brackets(self):
        return self.__iot2_Field_AddEntryToTable_Brackets

    @iot2_Field_AddEntryToTable_Brackets.setter
    def iot2_Field_AddEntryToTable_Brackets(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Field_AddEntryToTable_Brackets__iot2_Field_AddEntryToTable_Brackets", None)
        self.__iot2_Field_AddEntryToTable_Brackets = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression98"):
                opp_val = getattr(old_value, "iot2_Expression98", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression98", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression98"):
                opp_val = getattr(value, "iot2_Expression98", None)
                setattr(value, "iot2_Expression98", self)

    def execute(self, iot2_c):
        # TODO: Implement execute method
        pass

class iot2_Functioncall_Arguments:

    def __init__(self, iot2_Functioncall_Arguments115: "iot2_Statement_CallFunction" = None, iot2_Functioncall_Arguments: set["iot2_Expression"] = None, iot2_Functioncall_Arguments110: "iot2_Statement_CallMemberFunction" = None, iot2_Functioncall_Arguments201: "iot2_Expression_CallMemberFunction" = None, iot2_Functioncall_Arguments206: "iot2_Expression_CallFunction" = None):
        self.iot2_Functioncall_Arguments115 = iot2_Functioncall_Arguments115
        self.iot2_Functioncall_Arguments = iot2_Functioncall_Arguments if iot2_Functioncall_Arguments is not None else set()
        self.iot2_Functioncall_Arguments110 = iot2_Functioncall_Arguments110
        self.iot2_Functioncall_Arguments201 = iot2_Functioncall_Arguments201
        self.iot2_Functioncall_Arguments206 = iot2_Functioncall_Arguments206
        
        pass
    @property
    def iot2_Functioncall_Arguments206(self):
        return self.__iot2_Functioncall_Arguments206

    @iot2_Functioncall_Arguments206.setter
    def iot2_Functioncall_Arguments206(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Functioncall_Arguments__iot2_Functioncall_Arguments206", None)
        self.__iot2_Functioncall_Arguments206 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_CallFunction205"):
                opp_val = getattr(old_value, "iot2_Expression_CallFunction205", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression_CallFunction205", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_CallFunction205"):
                opp_val = getattr(value, "iot2_Expression_CallFunction205", None)
                setattr(value, "iot2_Expression_CallFunction205", self)

    @property
    def iot2_Functioncall_Arguments110(self):
        return self.__iot2_Functioncall_Arguments110

    @iot2_Functioncall_Arguments110.setter
    def iot2_Functioncall_Arguments110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Functioncall_Arguments__iot2_Functioncall_Arguments110", None)
        self.__iot2_Functioncall_Arguments110 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Statement_CallMemberFunction109"):
                opp_val = getattr(old_value, "iot2_Statement_CallMemberFunction109", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Statement_CallMemberFunction109", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Statement_CallMemberFunction109"):
                opp_val = getattr(value, "iot2_Statement_CallMemberFunction109", None)
                setattr(value, "iot2_Statement_CallMemberFunction109", self)

    @property
    def iot2_Functioncall_Arguments201(self):
        return self.__iot2_Functioncall_Arguments201

    @iot2_Functioncall_Arguments201.setter
    def iot2_Functioncall_Arguments201(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Functioncall_Arguments__iot2_Functioncall_Arguments201", None)
        self.__iot2_Functioncall_Arguments201 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_CallMemberFunction200"):
                opp_val = getattr(old_value, "iot2_Expression_CallMemberFunction200", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression_CallMemberFunction200", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_CallMemberFunction200"):
                opp_val = getattr(value, "iot2_Expression_CallMemberFunction200", None)
                setattr(value, "iot2_Expression_CallMemberFunction200", self)

    @property
    def iot2_Functioncall_Arguments115(self):
        return self.__iot2_Functioncall_Arguments115

    @iot2_Functioncall_Arguments115.setter
    def iot2_Functioncall_Arguments115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Functioncall_Arguments__iot2_Functioncall_Arguments115", None)
        self.__iot2_Functioncall_Arguments115 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Statement_CallFunction114"):
                opp_val = getattr(old_value, "iot2_Statement_CallFunction114", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Statement_CallFunction114", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Statement_CallFunction114"):
                opp_val = getattr(value, "iot2_Statement_CallFunction114", None)
                setattr(value, "iot2_Statement_CallFunction114", self)

    @property
    def iot2_Functioncall_Arguments(self):
        return self.__iot2_Functioncall_Arguments

    @iot2_Functioncall_Arguments.setter
    def iot2_Functioncall_Arguments(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Functioncall_Arguments__iot2_Functioncall_Arguments", None)
        self.__iot2_Functioncall_Arguments = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iot2_Expression96"):
                    opp_val = getattr(item, "iot2_Expression96", None)
                    
                    if opp_val == self:
                        setattr(item, "iot2_Expression96", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iot2_Expression96"):
                    opp_val = getattr(item, "iot2_Expression96", None)
                    
                    setattr(item, "iot2_Expression96", self)
                    

    def execute(self, iot2_c):
        # TODO: Implement execute method
        pass

class Expression:

    pass
class iot2_Expression_Not_Equal(Expression):

    def __init__(self, iot2_Expression_Not_Equal: "iot2_Expression" = None, iot2_Expression_Not_Equal154: "iot2_Expression" = None):
        self.iot2_Expression_Not_Equal = iot2_Expression_Not_Equal
        self.iot2_Expression_Not_Equal154 = iot2_Expression_Not_Equal154
        
        pass
    @property
    def iot2_Expression_Not_Equal(self):
        return self.__iot2_Expression_Not_Equal

    @iot2_Expression_Not_Equal.setter
    def iot2_Expression_Not_Equal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_Not_Equal__iot2_Expression_Not_Equal", None)
        self.__iot2_Expression_Not_Equal = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression152"):
                opp_val = getattr(old_value, "iot2_Expression152", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression152", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression152"):
                opp_val = getattr(value, "iot2_Expression152", None)
                setattr(value, "iot2_Expression152", self)

    @property
    def iot2_Expression_Not_Equal154(self):
        return self.__iot2_Expression_Not_Equal154

    @iot2_Expression_Not_Equal154.setter
    def iot2_Expression_Not_Equal154(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_Not_Equal__iot2_Expression_Not_Equal154", None)
        self.__iot2_Expression_Not_Equal154 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression155"):
                opp_val = getattr(old_value, "iot2_Expression155", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression155", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression155"):
                opp_val = getattr(value, "iot2_Expression155", None)
                setattr(value, "iot2_Expression155", self)

    def execute(self, iot2_c):
        # TODO: Implement execute method
        pass

class iot2_Expression_True(Expression):

    def __init__(self):
        
        pass
    def execute(self, iot2_c):
        # TODO: Implement execute method
        pass

class iot2_Expression_Concatenation(Expression):

    def __init__(self, iot2_Expression_Concatenation: "iot2_Expression" = None, iot2_Expression_Concatenation159: "iot2_Expression" = None):
        self.iot2_Expression_Concatenation = iot2_Expression_Concatenation
        self.iot2_Expression_Concatenation159 = iot2_Expression_Concatenation159
        
        pass
    @property
    def iot2_Expression_Concatenation(self):
        return self.__iot2_Expression_Concatenation

    @iot2_Expression_Concatenation.setter
    def iot2_Expression_Concatenation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_Concatenation__iot2_Expression_Concatenation", None)
        self.__iot2_Expression_Concatenation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression157"):
                opp_val = getattr(old_value, "iot2_Expression157", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression157", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression157"):
                opp_val = getattr(value, "iot2_Expression157", None)
                setattr(value, "iot2_Expression157", self)

    @property
    def iot2_Expression_Concatenation159(self):
        return self.__iot2_Expression_Concatenation159

    @iot2_Expression_Concatenation159.setter
    def iot2_Expression_Concatenation159(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_Concatenation__iot2_Expression_Concatenation159", None)
        self.__iot2_Expression_Concatenation159 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression160"):
                opp_val = getattr(old_value, "iot2_Expression160", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression160", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression160"):
                opp_val = getattr(value, "iot2_Expression160", None)
                setattr(value, "iot2_Expression160", self)

    def execute(self, iot2_c):
        # TODO: Implement execute method
        pass

class iot2_Expression_Multiplication(Expression):

    def __init__(self, iot2_Expression_Multiplication: "iot2_Expression" = None, iot2_Expression_Multiplication174: "iot2_Expression" = None):
        self.iot2_Expression_Multiplication = iot2_Expression_Multiplication
        self.iot2_Expression_Multiplication174 = iot2_Expression_Multiplication174
        
        pass
    @property
    def iot2_Expression_Multiplication(self):
        return self.__iot2_Expression_Multiplication

    @iot2_Expression_Multiplication.setter
    def iot2_Expression_Multiplication(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_Multiplication__iot2_Expression_Multiplication", None)
        self.__iot2_Expression_Multiplication = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression172"):
                opp_val = getattr(old_value, "iot2_Expression172", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression172", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression172"):
                opp_val = getattr(value, "iot2_Expression172", None)
                setattr(value, "iot2_Expression172", self)

    @property
    def iot2_Expression_Multiplication174(self):
        return self.__iot2_Expression_Multiplication174

    @iot2_Expression_Multiplication174.setter
    def iot2_Expression_Multiplication174(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_Multiplication__iot2_Expression_Multiplication174", None)
        self.__iot2_Expression_Multiplication174 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression175"):
                opp_val = getattr(old_value, "iot2_Expression175", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression175", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression175"):
                opp_val = getattr(value, "iot2_Expression175", None)
                setattr(value, "iot2_Expression175", self)

    def execute(self, iot2_c):
        # TODO: Implement execute method
        pass

class iot2_Expression_TableConstructor(Expression):

    def __init__(self, iot2_Expression_TableConstructor: set["iot2_Field"] = None):
        self.iot2_Expression_TableConstructor = iot2_Expression_TableConstructor if iot2_Expression_TableConstructor is not None else set()
        
        pass
    @property
    def iot2_Expression_TableConstructor(self):
        return self.__iot2_Expression_TableConstructor

    @iot2_Expression_TableConstructor.setter
    def iot2_Expression_TableConstructor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_TableConstructor__iot2_Expression_TableConstructor", None)
        self.__iot2_Expression_TableConstructor = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iot2_Field91"):
                    opp_val = getattr(item, "iot2_Field91", None)
                    
                    if opp_val == self:
                        setattr(item, "iot2_Field91", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iot2_Field91"):
                    opp_val = getattr(item, "iot2_Field91", None)
                    
                    setattr(item, "iot2_Field91", self)
                    

    def execute(self, iot2_c):
        # TODO: Implement execute method
        pass

class iot2_Expression_Larger_Equal(Expression):

    def __init__(self, iot2_Expression_Larger_Equal: "iot2_Expression" = None, iot2_Expression_Larger_Equal134: "iot2_Expression" = None):
        self.iot2_Expression_Larger_Equal = iot2_Expression_Larger_Equal
        self.iot2_Expression_Larger_Equal134 = iot2_Expression_Larger_Equal134
        
        pass
    @property
    def iot2_Expression_Larger_Equal134(self):
        return self.__iot2_Expression_Larger_Equal134

    @iot2_Expression_Larger_Equal134.setter
    def iot2_Expression_Larger_Equal134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_Larger_Equal__iot2_Expression_Larger_Equal134", None)
        self.__iot2_Expression_Larger_Equal134 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression135"):
                opp_val = getattr(old_value, "iot2_Expression135", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression135", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression135"):
                opp_val = getattr(value, "iot2_Expression135", None)
                setattr(value, "iot2_Expression135", self)

    @property
    def iot2_Expression_Larger_Equal(self):
        return self.__iot2_Expression_Larger_Equal

    @iot2_Expression_Larger_Equal.setter
    def iot2_Expression_Larger_Equal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_Larger_Equal__iot2_Expression_Larger_Equal", None)
        self.__iot2_Expression_Larger_Equal = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression132"):
                opp_val = getattr(old_value, "iot2_Expression132", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression132", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression132"):
                opp_val = getattr(value, "iot2_Expression132", None)
                setattr(value, "iot2_Expression132", self)

    def execute(self, iot2_c):
        # TODO: Implement execute method
        pass

class iot2_Expression_Exponentiation(Expression):

    def __init__(self, iot2_Expression_Exponentiation: "iot2_Expression" = None, iot2_Expression_Exponentiation195: "iot2_Expression" = None):
        self.iot2_Expression_Exponentiation = iot2_Expression_Exponentiation
        self.iot2_Expression_Exponentiation195 = iot2_Expression_Exponentiation195
        
        pass
    @property
    def iot2_Expression_Exponentiation(self):
        return self.__iot2_Expression_Exponentiation

    @iot2_Expression_Exponentiation.setter
    def iot2_Expression_Exponentiation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_Exponentiation__iot2_Expression_Exponentiation", None)
        self.__iot2_Expression_Exponentiation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression193"):
                opp_val = getattr(old_value, "iot2_Expression193", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression193", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression193"):
                opp_val = getattr(value, "iot2_Expression193", None)
                setattr(value, "iot2_Expression193", self)

    @property
    def iot2_Expression_Exponentiation195(self):
        return self.__iot2_Expression_Exponentiation195

    @iot2_Expression_Exponentiation195.setter
    def iot2_Expression_Exponentiation195(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_Exponentiation__iot2_Expression_Exponentiation195", None)
        self.__iot2_Expression_Exponentiation195 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression196"):
                opp_val = getattr(old_value, "iot2_Expression196", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression196", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression196"):
                opp_val = getattr(value, "iot2_Expression196", None)
                setattr(value, "iot2_Expression196", self)

    def execute(self, iot2_c):
        # TODO: Implement execute method
        pass

class iot2_Expression_Larger(Expression):

    def __init__(self, iot2_Expression_Larger: "iot2_Expression" = None, iot2_Expression_Larger129: "iot2_Expression" = None):
        self.iot2_Expression_Larger = iot2_Expression_Larger
        self.iot2_Expression_Larger129 = iot2_Expression_Larger129
        
        pass
    @property
    def iot2_Expression_Larger129(self):
        return self.__iot2_Expression_Larger129

    @iot2_Expression_Larger129.setter
    def iot2_Expression_Larger129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_Larger__iot2_Expression_Larger129", None)
        self.__iot2_Expression_Larger129 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression130"):
                opp_val = getattr(old_value, "iot2_Expression130", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression130", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression130"):
                opp_val = getattr(value, "iot2_Expression130", None)
                setattr(value, "iot2_Expression130", self)

    @property
    def iot2_Expression_Larger(self):
        return self.__iot2_Expression_Larger

    @iot2_Expression_Larger.setter
    def iot2_Expression_Larger(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_Larger__iot2_Expression_Larger", None)
        self.__iot2_Expression_Larger = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression127"):
                opp_val = getattr(old_value, "iot2_Expression127", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression127", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression127"):
                opp_val = getattr(value, "iot2_Expression127", None)
                setattr(value, "iot2_Expression127", self)

    def execute(self, iot2_c):
        # TODO: Implement execute method
        pass

class iot2_Expression_Smaller(Expression):

    def __init__(self, iot2_Expression_Smaller: "iot2_Expression" = None, iot2_Expression_Smaller139: "iot2_Expression" = None):
        self.iot2_Expression_Smaller = iot2_Expression_Smaller
        self.iot2_Expression_Smaller139 = iot2_Expression_Smaller139
        
        pass
    @property
    def iot2_Expression_Smaller139(self):
        return self.__iot2_Expression_Smaller139

    @iot2_Expression_Smaller139.setter
    def iot2_Expression_Smaller139(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_Smaller__iot2_Expression_Smaller139", None)
        self.__iot2_Expression_Smaller139 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression140"):
                opp_val = getattr(old_value, "iot2_Expression140", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression140", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression140"):
                opp_val = getattr(value, "iot2_Expression140", None)
                setattr(value, "iot2_Expression140", self)

    @property
    def iot2_Expression_Smaller(self):
        return self.__iot2_Expression_Smaller

    @iot2_Expression_Smaller.setter
    def iot2_Expression_Smaller(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_Smaller__iot2_Expression_Smaller", None)
        self.__iot2_Expression_Smaller = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression137"):
                opp_val = getattr(old_value, "iot2_Expression137", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression137", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression137"):
                opp_val = getattr(value, "iot2_Expression137", None)
                setattr(value, "iot2_Expression137", self)

    def execute(self, iot2_c):
        # TODO: Implement execute method
        pass

class iot2_Expression_Plus(Expression):

    def __init__(self, iot2_Expression_Plus: "iot2_Expression" = None, iot2_Expression_Plus164: "iot2_Expression" = None):
        self.iot2_Expression_Plus = iot2_Expression_Plus
        self.iot2_Expression_Plus164 = iot2_Expression_Plus164
        
        pass
    @property
    def iot2_Expression_Plus(self):
        return self.__iot2_Expression_Plus

    @iot2_Expression_Plus.setter
    def iot2_Expression_Plus(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_Plus__iot2_Expression_Plus", None)
        self.__iot2_Expression_Plus = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression162"):
                opp_val = getattr(old_value, "iot2_Expression162", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression162", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression162"):
                opp_val = getattr(value, "iot2_Expression162", None)
                setattr(value, "iot2_Expression162", self)

    @property
    def iot2_Expression_Plus164(self):
        return self.__iot2_Expression_Plus164

    @iot2_Expression_Plus164.setter
    def iot2_Expression_Plus164(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_Plus__iot2_Expression_Plus164", None)
        self.__iot2_Expression_Plus164 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression165"):
                opp_val = getattr(old_value, "iot2_Expression165", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression165", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression165"):
                opp_val = getattr(value, "iot2_Expression165", None)
                setattr(value, "iot2_Expression165", self)

    def execute(self, iot2_c):
        # TODO: Implement execute method
        pass

class iot2_Expression_Equal(Expression):

    def __init__(self, iot2_Expression_Equal: "iot2_Expression" = None, iot2_Expression_Equal149: "iot2_Expression" = None):
        self.iot2_Expression_Equal = iot2_Expression_Equal
        self.iot2_Expression_Equal149 = iot2_Expression_Equal149
        
        pass
    @property
    def iot2_Expression_Equal(self):
        return self.__iot2_Expression_Equal

    @iot2_Expression_Equal.setter
    def iot2_Expression_Equal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_Equal__iot2_Expression_Equal", None)
        self.__iot2_Expression_Equal = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression147"):
                opp_val = getattr(old_value, "iot2_Expression147", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression147", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression147"):
                opp_val = getattr(value, "iot2_Expression147", None)
                setattr(value, "iot2_Expression147", self)

    @property
    def iot2_Expression_Equal149(self):
        return self.__iot2_Expression_Equal149

    @iot2_Expression_Equal149.setter
    def iot2_Expression_Equal149(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_Equal__iot2_Expression_Equal149", None)
        self.__iot2_Expression_Equal149 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression150"):
                opp_val = getattr(old_value, "iot2_Expression150", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression150", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression150"):
                opp_val = getattr(value, "iot2_Expression150", None)
                setattr(value, "iot2_Expression150", self)

    def execute(self, iot2_c):
        # TODO: Implement execute method
        pass

class iot2_Expression_Modulo(Expression):

    def __init__(self, iot2_Expression_Modulo: "iot2_Expression" = None, iot2_Expression_Modulo184: "iot2_Expression" = None):
        self.iot2_Expression_Modulo = iot2_Expression_Modulo
        self.iot2_Expression_Modulo184 = iot2_Expression_Modulo184
        
        pass
    @property
    def iot2_Expression_Modulo(self):
        return self.__iot2_Expression_Modulo

    @iot2_Expression_Modulo.setter
    def iot2_Expression_Modulo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_Modulo__iot2_Expression_Modulo", None)
        self.__iot2_Expression_Modulo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression182"):
                opp_val = getattr(old_value, "iot2_Expression182", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression182", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression182"):
                opp_val = getattr(value, "iot2_Expression182", None)
                setattr(value, "iot2_Expression182", self)

    @property
    def iot2_Expression_Modulo184(self):
        return self.__iot2_Expression_Modulo184

    @iot2_Expression_Modulo184.setter
    def iot2_Expression_Modulo184(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_Modulo__iot2_Expression_Modulo184", None)
        self.__iot2_Expression_Modulo184 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression185"):
                opp_val = getattr(old_value, "iot2_Expression185", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression185", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression185"):
                opp_val = getattr(value, "iot2_Expression185", None)
                setattr(value, "iot2_Expression185", self)

    def execute(self, iot2_c):
        # TODO: Implement execute method
        pass

class iot2_Expression_And(Expression):

    def __init__(self, iot2_Expression_And: "iot2_Expression" = None, iot2_Expression_And124: "iot2_Expression" = None):
        self.iot2_Expression_And = iot2_Expression_And
        self.iot2_Expression_And124 = iot2_Expression_And124
        
        pass
    @property
    def iot2_Expression_And(self):
        return self.__iot2_Expression_And

    @iot2_Expression_And.setter
    def iot2_Expression_And(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_And__iot2_Expression_And", None)
        self.__iot2_Expression_And = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression122"):
                opp_val = getattr(old_value, "iot2_Expression122", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression122", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression122"):
                opp_val = getattr(value, "iot2_Expression122", None)
                setattr(value, "iot2_Expression122", self)

    @property
    def iot2_Expression_And124(self):
        return self.__iot2_Expression_And124

    @iot2_Expression_And124.setter
    def iot2_Expression_And124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_And__iot2_Expression_And124", None)
        self.__iot2_Expression_And124 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression125"):
                opp_val = getattr(old_value, "iot2_Expression125", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression125", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression125"):
                opp_val = getattr(value, "iot2_Expression125", None)
                setattr(value, "iot2_Expression125", self)

    def execute(self, iot2_c):
        # TODO: Implement execute method
        pass

class iot2_Expression_Smaller_Equal(Expression):

    def __init__(self, iot2_Expression_Smaller_Equal: "iot2_Expression" = None, iot2_Expression_Smaller_Equal144: "iot2_Expression" = None):
        self.iot2_Expression_Smaller_Equal = iot2_Expression_Smaller_Equal
        self.iot2_Expression_Smaller_Equal144 = iot2_Expression_Smaller_Equal144
        
        pass
    @property
    def iot2_Expression_Smaller_Equal(self):
        return self.__iot2_Expression_Smaller_Equal

    @iot2_Expression_Smaller_Equal.setter
    def iot2_Expression_Smaller_Equal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_Smaller_Equal__iot2_Expression_Smaller_Equal", None)
        self.__iot2_Expression_Smaller_Equal = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression142"):
                opp_val = getattr(old_value, "iot2_Expression142", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression142", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression142"):
                opp_val = getattr(value, "iot2_Expression142", None)
                setattr(value, "iot2_Expression142", self)

    @property
    def iot2_Expression_Smaller_Equal144(self):
        return self.__iot2_Expression_Smaller_Equal144

    @iot2_Expression_Smaller_Equal144.setter
    def iot2_Expression_Smaller_Equal144(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_Smaller_Equal__iot2_Expression_Smaller_Equal144", None)
        self.__iot2_Expression_Smaller_Equal144 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression145"):
                opp_val = getattr(old_value, "iot2_Expression145", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression145", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression145"):
                opp_val = getattr(value, "iot2_Expression145", None)
                setattr(value, "iot2_Expression145", self)

    def execute(self, iot2_c):
        # TODO: Implement execute method
        pass

class iot2_Expression_Invert(Expression):

    def __init__(self, iot2_Expression_Invert: "iot2_Expression" = None):
        self.iot2_Expression_Invert = iot2_Expression_Invert
        
        pass
    @property
    def iot2_Expression_Invert(self):
        return self.__iot2_Expression_Invert

    @iot2_Expression_Invert.setter
    def iot2_Expression_Invert(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_Invert__iot2_Expression_Invert", None)
        self.__iot2_Expression_Invert = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression191"):
                opp_val = getattr(old_value, "iot2_Expression191", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression191", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression191"):
                opp_val = getattr(value, "iot2_Expression191", None)
                setattr(value, "iot2_Expression191", self)

    def execute(self, iot2_c):
        # TODO: Implement execute method
        pass

class iot2_Expression_Minus(Expression):

    def __init__(self, iot2_Expression_Minus: "iot2_Expression" = None, iot2_Expression_Minus169: "iot2_Expression" = None):
        self.iot2_Expression_Minus = iot2_Expression_Minus
        self.iot2_Expression_Minus169 = iot2_Expression_Minus169
        
        pass
    @property
    def iot2_Expression_Minus(self):
        return self.__iot2_Expression_Minus

    @iot2_Expression_Minus.setter
    def iot2_Expression_Minus(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_Minus__iot2_Expression_Minus", None)
        self.__iot2_Expression_Minus = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression167"):
                opp_val = getattr(old_value, "iot2_Expression167", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression167", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression167"):
                opp_val = getattr(value, "iot2_Expression167", None)
                setattr(value, "iot2_Expression167", self)

    @property
    def iot2_Expression_Minus169(self):
        return self.__iot2_Expression_Minus169

    @iot2_Expression_Minus169.setter
    def iot2_Expression_Minus169(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_Minus__iot2_Expression_Minus169", None)
        self.__iot2_Expression_Minus169 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression170"):
                opp_val = getattr(old_value, "iot2_Expression170", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression170", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression170"):
                opp_val = getattr(value, "iot2_Expression170", None)
                setattr(value, "iot2_Expression170", self)

    def execute(self, iot2_c):
        # TODO: Implement execute method
        pass

class iot2_Expression_Or(Expression):

    def __init__(self, iot2_Expression_Or: "iot2_Expression" = None, iot2_Expression_Or119: "iot2_Expression" = None):
        self.iot2_Expression_Or = iot2_Expression_Or
        self.iot2_Expression_Or119 = iot2_Expression_Or119
        
        pass
    @property
    def iot2_Expression_Or119(self):
        return self.__iot2_Expression_Or119

    @iot2_Expression_Or119.setter
    def iot2_Expression_Or119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_Or__iot2_Expression_Or119", None)
        self.__iot2_Expression_Or119 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression120"):
                opp_val = getattr(old_value, "iot2_Expression120", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression120", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression120"):
                opp_val = getattr(value, "iot2_Expression120", None)
                setattr(value, "iot2_Expression120", self)

    @property
    def iot2_Expression_Or(self):
        return self.__iot2_Expression_Or

    @iot2_Expression_Or.setter
    def iot2_Expression_Or(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_Or__iot2_Expression_Or", None)
        self.__iot2_Expression_Or = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression117"):
                opp_val = getattr(old_value, "iot2_Expression117", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression117", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression117"):
                opp_val = getattr(value, "iot2_Expression117", None)
                setattr(value, "iot2_Expression117", self)

    def execute(self, iot2_c):
        # TODO: Implement execute method
        pass

class iot2_Expression_Division(Expression):

    def __init__(self, iot2_Expression_Division: "iot2_Expression" = None, iot2_Expression_Division179: "iot2_Expression" = None):
        self.iot2_Expression_Division = iot2_Expression_Division
        self.iot2_Expression_Division179 = iot2_Expression_Division179
        
        pass
    @property
    def iot2_Expression_Division179(self):
        return self.__iot2_Expression_Division179

    @iot2_Expression_Division179.setter
    def iot2_Expression_Division179(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_Division__iot2_Expression_Division179", None)
        self.__iot2_Expression_Division179 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression180"):
                opp_val = getattr(old_value, "iot2_Expression180", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression180", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression180"):
                opp_val = getattr(value, "iot2_Expression180", None)
                setattr(value, "iot2_Expression180", self)

    @property
    def iot2_Expression_Division(self):
        return self.__iot2_Expression_Division

    @iot2_Expression_Division.setter
    def iot2_Expression_Division(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_Division__iot2_Expression_Division", None)
        self.__iot2_Expression_Division = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression177"):
                opp_val = getattr(old_value, "iot2_Expression177", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression177", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression177"):
                opp_val = getattr(value, "iot2_Expression177", None)
                setattr(value, "iot2_Expression177", self)

    def execute(self, iot2_c):
        # TODO: Implement execute method
        pass

class iot2_Expression_False(Expression):

    def __init__(self):
        
        pass
    def execute(self, iot2_c):
        # TODO: Implement execute method
        pass

class iot2_Expression_Nil(Expression):

    def __init__(self):
        
        pass
    def execute(self, iot2_c):
        # TODO: Implement execute method
        pass

class Statement_FunctioncallOrAssignment:

    pass
class iot2_Statement_CallMemberFunction(Statement_FunctioncallOrAssignment):

    def __init__(self, memberFunctionName: str, iot2_Statement_CallMemberFunction: "iot2_Expression" = None, iot2_Statement_CallMemberFunction109: "iot2_Functioncall_Arguments" = None):
        self.memberFunctionName = memberFunctionName
        self.iot2_Statement_CallMemberFunction = iot2_Statement_CallMemberFunction
        self.iot2_Statement_CallMemberFunction109 = iot2_Statement_CallMemberFunction109
        
        pass
    @property
    def memberFunctionName(self):
        return self.__memberFunctionName

    @memberFunctionName.setter
    def memberFunctionName(self, memberFunctionName: str):
        self.__memberFunctionName = memberFunctionName


    @property
    def iot2_Statement_CallMemberFunction(self):
        return self.__iot2_Statement_CallMemberFunction

    @iot2_Statement_CallMemberFunction.setter
    def iot2_Statement_CallMemberFunction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Statement_CallMemberFunction__iot2_Statement_CallMemberFunction", None)
        self.__iot2_Statement_CallMemberFunction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression107"):
                opp_val = getattr(old_value, "iot2_Expression107", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression107", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression107"):
                opp_val = getattr(value, "iot2_Expression107", None)
                setattr(value, "iot2_Expression107", self)

    @property
    def iot2_Statement_CallMemberFunction109(self):
        return self.__iot2_Statement_CallMemberFunction109

    @iot2_Statement_CallMemberFunction109.setter
    def iot2_Statement_CallMemberFunction109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Statement_CallMemberFunction__iot2_Statement_CallMemberFunction109", None)
        self.__iot2_Statement_CallMemberFunction109 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Functioncall_Arguments110"):
                opp_val = getattr(old_value, "iot2_Functioncall_Arguments110", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Functioncall_Arguments110", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Functioncall_Arguments110"):
                opp_val = getattr(value, "iot2_Functioncall_Arguments110", None)
                setattr(value, "iot2_Functioncall_Arguments110", self)

    def execute(self, iot2_c):
        # TODO: Implement execute method
        pass

class iot2_Statement_CallFunction(Statement_FunctioncallOrAssignment):

    def __init__(self, iot2_Statement_CallFunction: "iot2_Expression" = None, iot2_Statement_CallFunction114: "iot2_Functioncall_Arguments" = None):
        self.iot2_Statement_CallFunction = iot2_Statement_CallFunction
        self.iot2_Statement_CallFunction114 = iot2_Statement_CallFunction114
        
        pass
    @property
    def iot2_Statement_CallFunction114(self):
        return self.__iot2_Statement_CallFunction114

    @iot2_Statement_CallFunction114.setter
    def iot2_Statement_CallFunction114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Statement_CallFunction__iot2_Statement_CallFunction114", None)
        self.__iot2_Statement_CallFunction114 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Functioncall_Arguments115"):
                opp_val = getattr(old_value, "iot2_Functioncall_Arguments115", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Functioncall_Arguments115", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Functioncall_Arguments115"):
                opp_val = getattr(value, "iot2_Functioncall_Arguments115", None)
                setattr(value, "iot2_Functioncall_Arguments115", self)

    @property
    def iot2_Statement_CallFunction(self):
        return self.__iot2_Statement_CallFunction

    @iot2_Statement_CallFunction.setter
    def iot2_Statement_CallFunction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Statement_CallFunction__iot2_Statement_CallFunction", None)
        self.__iot2_Statement_CallFunction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression112"):
                opp_val = getattr(old_value, "iot2_Expression112", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression112", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression112"):
                opp_val = getattr(value, "iot2_Expression112", None)
                setattr(value, "iot2_Expression112", self)

    def execute(self, iot2_c):
        # TODO: Implement execute method
        pass

class iot2_Statement_Assignment(Statement_FunctioncallOrAssignment):

    def __init__(self, iot2_Statement_Assignment: set["iot2_Expression"] = None, iot2_Statement_Assignment104: set["iot2_Expression"] = None):
        self.iot2_Statement_Assignment = iot2_Statement_Assignment if iot2_Statement_Assignment is not None else set()
        self.iot2_Statement_Assignment104 = iot2_Statement_Assignment104 if iot2_Statement_Assignment104 is not None else set()
        
        pass
    @property
    def iot2_Statement_Assignment(self):
        return self.__iot2_Statement_Assignment

    @iot2_Statement_Assignment.setter
    def iot2_Statement_Assignment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Statement_Assignment__iot2_Statement_Assignment", None)
        self.__iot2_Statement_Assignment = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iot2_Expression102"):
                    opp_val = getattr(item, "iot2_Expression102", None)
                    
                    if opp_val == self:
                        setattr(item, "iot2_Expression102", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iot2_Expression102"):
                    opp_val = getattr(item, "iot2_Expression102", None)
                    
                    setattr(item, "iot2_Expression102", self)
                    

    @property
    def iot2_Statement_Assignment104(self):
        return self.__iot2_Statement_Assignment104

    @iot2_Statement_Assignment104.setter
    def iot2_Statement_Assignment104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Statement_Assignment__iot2_Statement_Assignment104", None)
        self.__iot2_Statement_Assignment104 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iot2_Expression105"):
                    opp_val = getattr(item, "iot2_Expression105", None)
                    
                    if opp_val == self:
                        setattr(item, "iot2_Expression105", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iot2_Expression105"):
                    opp_val = getattr(item, "iot2_Expression105", None)
                    
                    setattr(item, "iot2_Expression105", self)
                    

    def execute(self, iot2_c):
        # TODO: Implement execute method
        pass

class iot2_Expression_Function(Expression):

    def __init__(self, iot2_Expression_Function: "iot2_Function" = None):
        self.iot2_Expression_Function = iot2_Expression_Function
        
        pass
    @property
    def iot2_Expression_Function(self):
        return self.__iot2_Expression_Function

    @iot2_Expression_Function.setter
    def iot2_Expression_Function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_Function__iot2_Expression_Function", None)
        self.__iot2_Expression_Function = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Function89"):
                opp_val = getattr(old_value, "iot2_Function89", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Function89", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Function89"):
                opp_val = getattr(value, "iot2_Function89", None)
                setattr(value, "iot2_Function89", self)

    def execute(self, iot2_c):
        # TODO: Implement execute method
        pass

class iot2_Expression_String(Expression):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    def execute(self, iot2_c):
        # TODO: Implement execute method
        pass

class iot2_Expression_VarArgs(Expression):

    def __init__(self):
        
        pass
    def execute(self, iot2_c):
        # TODO: Implement execute method
        pass

class iot2_Expression_Number(Expression):

    def __init__(self, value: float):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value


    def execute(self, iot2_c):
        # TODO: Implement execute method
        pass

class iot2_Function:

    def __init__(self, varArgs: bool, parameters: str, iot2_Function: "iot2_Statement_GlobalFunction_Declaration" = None, iot2_Function85: "iot2_Statement_LocalFunction_Declaration" = None, iot2_Function93: "iot2_Block" = None, iot2_Function89: "iot2_Expression_Function" = None):
        self.varArgs = varArgs
        self.parameters = parameters
        self.iot2_Function = iot2_Function
        self.iot2_Function85 = iot2_Function85
        self.iot2_Function93 = iot2_Function93
        self.iot2_Function89 = iot2_Function89
        
        pass
    @property
    def varArgs(self):
        return self.__varArgs

    @varArgs.setter
    def varArgs(self, varArgs: bool):
        self.__varArgs = varArgs


    @property
    def parameters(self):
        return self.__parameters

    @parameters.setter
    def parameters(self, parameters: str):
        self.__parameters = parameters


    @property
    def iot2_Function89(self):
        return self.__iot2_Function89

    @iot2_Function89.setter
    def iot2_Function89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Function__iot2_Function89", None)
        self.__iot2_Function89 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_Function"):
                opp_val = getattr(old_value, "iot2_Expression_Function", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression_Function", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_Function"):
                opp_val = getattr(value, "iot2_Expression_Function", None)
                setattr(value, "iot2_Expression_Function", self)

    @property
    def iot2_Function93(self):
        return self.__iot2_Function93

    @iot2_Function93.setter
    def iot2_Function93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Function__iot2_Function93", None)
        self.__iot2_Function93 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Block94"):
                opp_val = getattr(old_value, "iot2_Block94", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Block94", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Block94"):
                opp_val = getattr(value, "iot2_Block94", None)
                setattr(value, "iot2_Block94", self)

    @property
    def iot2_Function(self):
        return self.__iot2_Function

    @iot2_Function.setter
    def iot2_Function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Function__iot2_Function", None)
        self.__iot2_Function = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Statement_GlobalFunction_Declaration"):
                opp_val = getattr(old_value, "iot2_Statement_GlobalFunction_Declaration", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Statement_GlobalFunction_Declaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Statement_GlobalFunction_Declaration"):
                opp_val = getattr(value, "iot2_Statement_GlobalFunction_Declaration", None)
                setattr(value, "iot2_Statement_GlobalFunction_Declaration", self)

    @property
    def iot2_Function85(self):
        return self.__iot2_Function85

    @iot2_Function85.setter
    def iot2_Function85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Function__iot2_Function85", None)
        self.__iot2_Function85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Statement_LocalFunction_Declaration"):
                opp_val = getattr(old_value, "iot2_Statement_LocalFunction_Declaration", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Statement_LocalFunction_Declaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Statement_LocalFunction_Declaration"):
                opp_val = getattr(value, "iot2_Statement_LocalFunction_Declaration", None)
                setattr(value, "iot2_Statement_LocalFunction_Declaration", self)

    def execute(self, iot2_c):
        # TODO: Implement execute method
        pass

class Statement:

    pass
class iot2_Statement_For_Numeric(Statement):

    def __init__(self, iteratorName: str, iot2_Statement_For_Numeric: "iot2_Expression" = None, iot2_Statement_For_Numeric70: "iot2_Expression" = None, iot2_Statement_For_Numeric73: "iot2_Expression" = None, iot2_Statement_For_Numeric76: "iot2_Block" = None):
        self.iteratorName = iteratorName
        self.iot2_Statement_For_Numeric = iot2_Statement_For_Numeric
        self.iot2_Statement_For_Numeric70 = iot2_Statement_For_Numeric70
        self.iot2_Statement_For_Numeric73 = iot2_Statement_For_Numeric73
        self.iot2_Statement_For_Numeric76 = iot2_Statement_For_Numeric76
        
        pass
    @property
    def iteratorName(self):
        return self.__iteratorName

    @iteratorName.setter
    def iteratorName(self, iteratorName: str):
        self.__iteratorName = iteratorName


    @property
    def iot2_Statement_For_Numeric(self):
        return self.__iot2_Statement_For_Numeric

    @iot2_Statement_For_Numeric.setter
    def iot2_Statement_For_Numeric(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Statement_For_Numeric__iot2_Statement_For_Numeric", None)
        self.__iot2_Statement_For_Numeric = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression68"):
                opp_val = getattr(old_value, "iot2_Expression68", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression68"):
                opp_val = getattr(value, "iot2_Expression68", None)
                setattr(value, "iot2_Expression68", self)

    @property
    def iot2_Statement_For_Numeric73(self):
        return self.__iot2_Statement_For_Numeric73

    @iot2_Statement_For_Numeric73.setter
    def iot2_Statement_For_Numeric73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Statement_For_Numeric__iot2_Statement_For_Numeric73", None)
        self.__iot2_Statement_For_Numeric73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression74"):
                opp_val = getattr(old_value, "iot2_Expression74", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression74"):
                opp_val = getattr(value, "iot2_Expression74", None)
                setattr(value, "iot2_Expression74", self)

    @property
    def iot2_Statement_For_Numeric76(self):
        return self.__iot2_Statement_For_Numeric76

    @iot2_Statement_For_Numeric76.setter
    def iot2_Statement_For_Numeric76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Statement_For_Numeric__iot2_Statement_For_Numeric76", None)
        self.__iot2_Statement_For_Numeric76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Block77"):
                opp_val = getattr(old_value, "iot2_Block77", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Block77", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Block77"):
                opp_val = getattr(value, "iot2_Block77", None)
                setattr(value, "iot2_Block77", self)

    @property
    def iot2_Statement_For_Numeric70(self):
        return self.__iot2_Statement_For_Numeric70

    @iot2_Statement_For_Numeric70.setter
    def iot2_Statement_For_Numeric70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Statement_For_Numeric__iot2_Statement_For_Numeric70", None)
        self.__iot2_Statement_For_Numeric70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression71"):
                opp_val = getattr(old_value, "iot2_Expression71", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression71"):
                opp_val = getattr(value, "iot2_Expression71", None)
                setattr(value, "iot2_Expression71", self)

    def execute(self, iot2_c):
        # TODO: Implement execute method
        pass

class iot2_Statement_GlobalFunction_Declaration(Statement):

    def __init__(self, prefix: str, functionName: str, iot2_Statement_GlobalFunction_Declaration: "iot2_Function" = None):
        self.prefix = prefix
        self.functionName = functionName
        self.iot2_Statement_GlobalFunction_Declaration = iot2_Statement_GlobalFunction_Declaration
        
        pass
    @property
    def functionName(self):
        return self.__functionName

    @functionName.setter
    def functionName(self, functionName: str):
        self.__functionName = functionName


    @property
    def prefix(self):
        return self.__prefix

    @prefix.setter
    def prefix(self, prefix: str):
        self.__prefix = prefix


    @property
    def iot2_Statement_GlobalFunction_Declaration(self):
        return self.__iot2_Statement_GlobalFunction_Declaration

    @iot2_Statement_GlobalFunction_Declaration.setter
    def iot2_Statement_GlobalFunction_Declaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Statement_GlobalFunction_Declaration__iot2_Statement_GlobalFunction_Declaration", None)
        self.__iot2_Statement_GlobalFunction_Declaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Function"):
                opp_val = getattr(old_value, "iot2_Function", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Function", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Function"):
                opp_val = getattr(value, "iot2_Function", None)
                setattr(value, "iot2_Function", self)

    def execute(self, iot2_c):
        # TODO: Implement execute method
        pass

class iot2_Statement_If_Then_Else(Statement):

    def __init__(self, iot2_Statement_If_Then_Else: "iot2_Expression" = None, iot2_Statement_If_Then_Else54: "iot2_Block" = None, iot2_Statement_If_Then_Else57: set["iot2_Statement_If_Then_Else_ElseIfPart"] = None, iot2_Statement_If_Then_Else59: "iot2_Block" = None):
        self.iot2_Statement_If_Then_Else = iot2_Statement_If_Then_Else
        self.iot2_Statement_If_Then_Else54 = iot2_Statement_If_Then_Else54
        self.iot2_Statement_If_Then_Else57 = iot2_Statement_If_Then_Else57 if iot2_Statement_If_Then_Else57 is not None else set()
        self.iot2_Statement_If_Then_Else59 = iot2_Statement_If_Then_Else59
        
        pass
    @property
    def iot2_Statement_If_Then_Else54(self):
        return self.__iot2_Statement_If_Then_Else54

    @iot2_Statement_If_Then_Else54.setter
    def iot2_Statement_If_Then_Else54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Statement_If_Then_Else__iot2_Statement_If_Then_Else54", None)
        self.__iot2_Statement_If_Then_Else54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Block55"):
                opp_val = getattr(old_value, "iot2_Block55", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Block55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Block55"):
                opp_val = getattr(value, "iot2_Block55", None)
                setattr(value, "iot2_Block55", self)

    @property
    def iot2_Statement_If_Then_Else(self):
        return self.__iot2_Statement_If_Then_Else

    @iot2_Statement_If_Then_Else.setter
    def iot2_Statement_If_Then_Else(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Statement_If_Then_Else__iot2_Statement_If_Then_Else", None)
        self.__iot2_Statement_If_Then_Else = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression52"):
                opp_val = getattr(old_value, "iot2_Expression52", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression52"):
                opp_val = getattr(value, "iot2_Expression52", None)
                setattr(value, "iot2_Expression52", self)

    @property
    def iot2_Statement_If_Then_Else57(self):
        return self.__iot2_Statement_If_Then_Else57

    @iot2_Statement_If_Then_Else57.setter
    def iot2_Statement_If_Then_Else57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Statement_If_Then_Else__iot2_Statement_If_Then_Else57", None)
        self.__iot2_Statement_If_Then_Else57 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iot2_Statement_If_Then_Else_ElseIfPart"):
                    opp_val = getattr(item, "iot2_Statement_If_Then_Else_ElseIfPart", None)
                    
                    if opp_val == self:
                        setattr(item, "iot2_Statement_If_Then_Else_ElseIfPart", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iot2_Statement_If_Then_Else_ElseIfPart"):
                    opp_val = getattr(item, "iot2_Statement_If_Then_Else_ElseIfPart", None)
                    
                    setattr(item, "iot2_Statement_If_Then_Else_ElseIfPart", self)
                    

    @property
    def iot2_Statement_If_Then_Else59(self):
        return self.__iot2_Statement_If_Then_Else59

    @iot2_Statement_If_Then_Else59.setter
    def iot2_Statement_If_Then_Else59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Statement_If_Then_Else__iot2_Statement_If_Then_Else59", None)
        self.__iot2_Statement_If_Then_Else59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Block60"):
                opp_val = getattr(old_value, "iot2_Block60", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Block60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Block60"):
                opp_val = getattr(value, "iot2_Block60", None)
                setattr(value, "iot2_Block60", self)

    def execute(self, iot2_c):
        # TODO: Implement execute method
        pass

class iot2_Statement_FunctioncallOrAssignment(Statement):

    def __init__(self):
        
        pass
    def execute(self, iot2_c):
        # TODO: Implement execute method
        pass

class iot2_Statement_Repeat(Statement):

    def __init__(self, iot2_Statement_Repeat: "iot2_Block" = None, iot2_Statement_Repeat49: "iot2_Expression" = None):
        self.iot2_Statement_Repeat = iot2_Statement_Repeat
        self.iot2_Statement_Repeat49 = iot2_Statement_Repeat49
        
        pass
    @property
    def iot2_Statement_Repeat49(self):
        return self.__iot2_Statement_Repeat49

    @iot2_Statement_Repeat49.setter
    def iot2_Statement_Repeat49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Statement_Repeat__iot2_Statement_Repeat49", None)
        self.__iot2_Statement_Repeat49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression50"):
                opp_val = getattr(old_value, "iot2_Expression50", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression50"):
                opp_val = getattr(value, "iot2_Expression50", None)
                setattr(value, "iot2_Expression50", self)

    @property
    def iot2_Statement_Repeat(self):
        return self.__iot2_Statement_Repeat

    @iot2_Statement_Repeat.setter
    def iot2_Statement_Repeat(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Statement_Repeat__iot2_Statement_Repeat", None)
        self.__iot2_Statement_Repeat = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Block47"):
                opp_val = getattr(old_value, "iot2_Block47", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Block47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Block47"):
                opp_val = getattr(value, "iot2_Block47", None)
                setattr(value, "iot2_Block47", self)

    def execute(self, iot2_c):
        # TODO: Implement execute method
        pass

class iot2_Statement_LocalFunction_Declaration(Statement):

    def __init__(self, functionName: str, iot2_Statement_LocalFunction_Declaration: "iot2_Function" = None):
        self.functionName = functionName
        self.iot2_Statement_LocalFunction_Declaration = iot2_Statement_LocalFunction_Declaration
        
        pass
    @property
    def functionName(self):
        return self.__functionName

    @functionName.setter
    def functionName(self, functionName: str):
        self.__functionName = functionName


    @property
    def iot2_Statement_LocalFunction_Declaration(self):
        return self.__iot2_Statement_LocalFunction_Declaration

    @iot2_Statement_LocalFunction_Declaration.setter
    def iot2_Statement_LocalFunction_Declaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Statement_LocalFunction_Declaration__iot2_Statement_LocalFunction_Declaration", None)
        self.__iot2_Statement_LocalFunction_Declaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Function85"):
                opp_val = getattr(old_value, "iot2_Function85", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Function85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Function85"):
                opp_val = getattr(value, "iot2_Function85", None)
                setattr(value, "iot2_Function85", self)

    def execute(self, iot2_c):
        # TODO: Implement execute method
        pass

class iot2_Statement_While(Statement):

    def __init__(self, iot2_Statement_While: "iot2_Expression" = None, iot2_Statement_While44: "iot2_Block" = None):
        self.iot2_Statement_While = iot2_Statement_While
        self.iot2_Statement_While44 = iot2_Statement_While44
        
        pass
    @property
    def iot2_Statement_While44(self):
        return self.__iot2_Statement_While44

    @iot2_Statement_While44.setter
    def iot2_Statement_While44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Statement_While__iot2_Statement_While44", None)
        self.__iot2_Statement_While44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Block45"):
                opp_val = getattr(old_value, "iot2_Block45", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Block45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Block45"):
                opp_val = getattr(value, "iot2_Block45", None)
                setattr(value, "iot2_Block45", self)

    @property
    def iot2_Statement_While(self):
        return self.__iot2_Statement_While

    @iot2_Statement_While.setter
    def iot2_Statement_While(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Statement_While__iot2_Statement_While", None)
        self.__iot2_Statement_While = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression42"):
                opp_val = getattr(old_value, "iot2_Expression42", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression42"):
                opp_val = getattr(value, "iot2_Expression42", None)
                setattr(value, "iot2_Expression42", self)

    def execute(self, iot2_c):
        # TODO: Implement execute method
        pass

class iot2_Statement_For_Generic(Statement):

    def __init__(self, names: str, iot2_Statement_For_Generic: set["iot2_Expression"] = None, iot2_Statement_For_Generic81: "iot2_Block" = None):
        self.names = names
        self.iot2_Statement_For_Generic = iot2_Statement_For_Generic if iot2_Statement_For_Generic is not None else set()
        self.iot2_Statement_For_Generic81 = iot2_Statement_For_Generic81
        
        pass
    @property
    def names(self):
        return self.__names

    @names.setter
    def names(self, names: str):
        self.__names = names


    @property
    def iot2_Statement_For_Generic(self):
        return self.__iot2_Statement_For_Generic

    @iot2_Statement_For_Generic.setter
    def iot2_Statement_For_Generic(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Statement_For_Generic__iot2_Statement_For_Generic", None)
        self.__iot2_Statement_For_Generic = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iot2_Expression79"):
                    opp_val = getattr(item, "iot2_Expression79", None)
                    
                    if opp_val == self:
                        setattr(item, "iot2_Expression79", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iot2_Expression79"):
                    opp_val = getattr(item, "iot2_Expression79", None)
                    
                    setattr(item, "iot2_Expression79", self)
                    

    @property
    def iot2_Statement_For_Generic81(self):
        return self.__iot2_Statement_For_Generic81

    @iot2_Statement_For_Generic81.setter
    def iot2_Statement_For_Generic81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Statement_For_Generic__iot2_Statement_For_Generic81", None)
        self.__iot2_Statement_For_Generic81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Block82"):
                opp_val = getattr(old_value, "iot2_Block82", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Block82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Block82"):
                opp_val = getattr(value, "iot2_Block82", None)
                setattr(value, "iot2_Block82", self)

    def execute(self, iot2_c):
        # TODO: Implement execute method
        pass

class iot2_Statement_Local_Variable_Declaration(Statement):

    def __init__(self, variableNames: str, iot2_Statement_Local_Variable_Declaration: set["iot2_Expression"] = None):
        self.variableNames = variableNames
        self.iot2_Statement_Local_Variable_Declaration = iot2_Statement_Local_Variable_Declaration if iot2_Statement_Local_Variable_Declaration is not None else set()
        
        pass
    @property
    def variableNames(self):
        return self.__variableNames

    @variableNames.setter
    def variableNames(self, variableNames: str):
        self.__variableNames = variableNames


    @property
    def iot2_Statement_Local_Variable_Declaration(self):
        return self.__iot2_Statement_Local_Variable_Declaration

    @iot2_Statement_Local_Variable_Declaration.setter
    def iot2_Statement_Local_Variable_Declaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Statement_Local_Variable_Declaration__iot2_Statement_Local_Variable_Declaration", None)
        self.__iot2_Statement_Local_Variable_Declaration = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iot2_Expression87"):
                    opp_val = getattr(item, "iot2_Expression87", None)
                    
                    if opp_val == self:
                        setattr(item, "iot2_Expression87", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iot2_Expression87"):
                    opp_val = getattr(item, "iot2_Expression87", None)
                    
                    setattr(item, "iot2_Expression87", self)
                    

    def execute(self, iot2_c):
        # TODO: Implement execute method
        pass

class iot2_Statement_Block(Statement):

    def __init__(self, iot2_Statement_Block: "iot2_Block" = None):
        self.iot2_Statement_Block = iot2_Statement_Block
        
        pass
    @property
    def iot2_Statement_Block(self):
        return self.__iot2_Statement_Block

    @iot2_Statement_Block.setter
    def iot2_Statement_Block(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Statement_Block__iot2_Statement_Block", None)
        self.__iot2_Statement_Block = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Block40"):
                opp_val = getattr(old_value, "iot2_Block40", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Block40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Block40"):
                opp_val = getattr(value, "iot2_Block40", None)
                setattr(value, "iot2_Block40", self)

    def execute(self, iot2_c):
        # TODO: Implement execute method
        pass

class iot2_Statement_If_Then_Else_ElseIfPart:

    def __init__(self, iot2_Statement_If_Then_Else_ElseIfPart: "iot2_Statement_If_Then_Else" = None, iot2_Statement_If_Then_Else_ElseIfPart62: "iot2_Expression" = None, iot2_Statement_If_Then_Else_ElseIfPart65: "iot2_Block" = None):
        self.iot2_Statement_If_Then_Else_ElseIfPart = iot2_Statement_If_Then_Else_ElseIfPart
        self.iot2_Statement_If_Then_Else_ElseIfPart62 = iot2_Statement_If_Then_Else_ElseIfPart62
        self.iot2_Statement_If_Then_Else_ElseIfPart65 = iot2_Statement_If_Then_Else_ElseIfPart65
        
        pass
    @property
    def iot2_Statement_If_Then_Else_ElseIfPart(self):
        return self.__iot2_Statement_If_Then_Else_ElseIfPart

    @iot2_Statement_If_Then_Else_ElseIfPart.setter
    def iot2_Statement_If_Then_Else_ElseIfPart(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Statement_If_Then_Else_ElseIfPart__iot2_Statement_If_Then_Else_ElseIfPart", None)
        self.__iot2_Statement_If_Then_Else_ElseIfPart = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Statement_If_Then_Else57"):
                opp_val = getattr(old_value, "iot2_Statement_If_Then_Else57", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Statement_If_Then_Else57"):
                opp_val = getattr(value, "iot2_Statement_If_Then_Else57", None)
                if opp_val is None:
                    setattr(value, "iot2_Statement_If_Then_Else57", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def iot2_Statement_If_Then_Else_ElseIfPart62(self):
        return self.__iot2_Statement_If_Then_Else_ElseIfPart62

    @iot2_Statement_If_Then_Else_ElseIfPart62.setter
    def iot2_Statement_If_Then_Else_ElseIfPart62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Statement_If_Then_Else_ElseIfPart__iot2_Statement_If_Then_Else_ElseIfPart62", None)
        self.__iot2_Statement_If_Then_Else_ElseIfPart62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression63"):
                opp_val = getattr(old_value, "iot2_Expression63", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression63"):
                opp_val = getattr(value, "iot2_Expression63", None)
                setattr(value, "iot2_Expression63", self)

    @property
    def iot2_Statement_If_Then_Else_ElseIfPart65(self):
        return self.__iot2_Statement_If_Then_Else_ElseIfPart65

    @iot2_Statement_If_Then_Else_ElseIfPart65.setter
    def iot2_Statement_If_Then_Else_ElseIfPart65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Statement_If_Then_Else_ElseIfPart__iot2_Statement_If_Then_Else_ElseIfPart65", None)
        self.__iot2_Statement_If_Then_Else_ElseIfPart65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Block66"):
                opp_val = getattr(old_value, "iot2_Block66", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Block66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Block66"):
                opp_val = getattr(value, "iot2_Block66", None)
                setattr(value, "iot2_Block66", self)

    def execute(self, iot2_c):
        # TODO: Implement execute method
        pass

class iot2_Expression(Statement_FunctioncallOrAssignment):

    def __init__(self, iot2_Expression: "iot2_Field" = None, iot2_Expression52: "iot2_Statement_If_Then_Else" = None, iot2_Expression100: "iot2_LastStatement_ReturnWithValue" = None, iot2_Expression102: "iot2_Statement_Assignment" = None, iot2_Expression105: "iot2_Statement_Assignment" = None, iot2_Expression127: "iot2_Expression_Larger" = None, iot2_Expression130: "iot2_Expression_Larger" = None, iot2_Expression132: "iot2_Expression_Larger_Equal" = None, iot2_Expression135: "iot2_Expression_Larger_Equal" = None, iot2_Expression112: "iot2_Statement_CallFunction" = None, iot2_Expression117: "iot2_Expression_Or" = None, iot2_Expression120: "iot2_Expression_Or" = None, iot2_Expression122: "iot2_Expression_And" = None, iot2_Expression125: "iot2_Expression_And" = None, iot2_Expression147: "iot2_Expression_Equal" = None, iot2_Expression150: "iot2_Expression_Equal" = None, iot2_Expression152: "iot2_Expression_Not_Equal" = None, iot2_Expression137: "iot2_Expression_Smaller" = None, iot2_Expression42: "iot2_Statement_While" = None, iot2_Expression50: "iot2_Statement_Repeat" = None, iot2_Expression63: "iot2_Statement_If_Then_Else_ElseIfPart" = None, iot2_Expression68: "iot2_Statement_For_Numeric" = None, iot2_Expression71: "iot2_Statement_For_Numeric" = None, iot2_Expression74: "iot2_Statement_For_Numeric" = None, iot2_Expression79: "iot2_Statement_For_Generic" = None, iot2_Expression87: "iot2_Statement_Local_Variable_Declaration" = None, iot2_Expression96: "iot2_Functioncall_Arguments" = None, iot2_Expression107: "iot2_Statement_CallMemberFunction" = None, iot2_Expression98: "iot2_Field_AddEntryToTable_Brackets" = None, iot2_Expression177: "iot2_Expression_Division" = None, iot2_Expression180: "iot2_Expression_Division" = None, iot2_Expression182: "iot2_Expression_Modulo" = None, iot2_Expression185: "iot2_Expression_Modulo" = None, iot2_Expression187: "iot2_Expression_Negate" = None, iot2_Expression208: "iot2_Expression_AccessArray" = None, iot2_Expression211: "iot2_Expression_AccessArray" = None, iot2_Expression213: "iot2_Expression_AccessMember" = None, iot2_Expression193: "iot2_Expression_Exponentiation" = None, iot2_Expression196: "iot2_Expression_Exponentiation" = None, iot2_Expression198: "iot2_Expression_CallMemberFunction" = None, iot2_Expression203: "iot2_Expression_CallFunction" = None, iot2_Expression140: "iot2_Expression_Smaller" = None, iot2_Expression142: "iot2_Expression_Smaller_Equal" = None, iot2_Expression145: "iot2_Expression_Smaller_Equal" = None, iot2_Expression167: "iot2_Expression_Minus" = None, iot2_Expression170: "iot2_Expression_Minus" = None, iot2_Expression172: "iot2_Expression_Multiplication" = None, iot2_Expression175: "iot2_Expression_Multiplication" = None, iot2_Expression155: "iot2_Expression_Not_Equal" = None, iot2_Expression157: "iot2_Expression_Concatenation" = None, iot2_Expression160: "iot2_Expression_Concatenation" = None, iot2_Expression162: "iot2_Expression_Plus" = None, iot2_Expression165: "iot2_Expression_Plus" = None, iot2_Expression189: "iot2_Expression_Length" = None, iot2_Expression191: "iot2_Expression_Invert" = None, iot2_Expression228: "iot2_OpaqueAction" = None):
        self.iot2_Expression = iot2_Expression
        self.iot2_Expression52 = iot2_Expression52
        self.iot2_Expression100 = iot2_Expression100
        self.iot2_Expression102 = iot2_Expression102
        self.iot2_Expression105 = iot2_Expression105
        self.iot2_Expression127 = iot2_Expression127
        self.iot2_Expression130 = iot2_Expression130
        self.iot2_Expression132 = iot2_Expression132
        self.iot2_Expression135 = iot2_Expression135
        self.iot2_Expression112 = iot2_Expression112
        self.iot2_Expression117 = iot2_Expression117
        self.iot2_Expression120 = iot2_Expression120
        self.iot2_Expression122 = iot2_Expression122
        self.iot2_Expression125 = iot2_Expression125
        self.iot2_Expression147 = iot2_Expression147
        self.iot2_Expression150 = iot2_Expression150
        self.iot2_Expression152 = iot2_Expression152
        self.iot2_Expression137 = iot2_Expression137
        self.iot2_Expression42 = iot2_Expression42
        self.iot2_Expression50 = iot2_Expression50
        self.iot2_Expression63 = iot2_Expression63
        self.iot2_Expression68 = iot2_Expression68
        self.iot2_Expression71 = iot2_Expression71
        self.iot2_Expression74 = iot2_Expression74
        self.iot2_Expression79 = iot2_Expression79
        self.iot2_Expression87 = iot2_Expression87
        self.iot2_Expression96 = iot2_Expression96
        self.iot2_Expression107 = iot2_Expression107
        self.iot2_Expression98 = iot2_Expression98
        self.iot2_Expression177 = iot2_Expression177
        self.iot2_Expression180 = iot2_Expression180
        self.iot2_Expression182 = iot2_Expression182
        self.iot2_Expression185 = iot2_Expression185
        self.iot2_Expression187 = iot2_Expression187
        self.iot2_Expression208 = iot2_Expression208
        self.iot2_Expression211 = iot2_Expression211
        self.iot2_Expression213 = iot2_Expression213
        self.iot2_Expression193 = iot2_Expression193
        self.iot2_Expression196 = iot2_Expression196
        self.iot2_Expression198 = iot2_Expression198
        self.iot2_Expression203 = iot2_Expression203
        self.iot2_Expression140 = iot2_Expression140
        self.iot2_Expression142 = iot2_Expression142
        self.iot2_Expression145 = iot2_Expression145
        self.iot2_Expression167 = iot2_Expression167
        self.iot2_Expression170 = iot2_Expression170
        self.iot2_Expression172 = iot2_Expression172
        self.iot2_Expression175 = iot2_Expression175
        self.iot2_Expression155 = iot2_Expression155
        self.iot2_Expression157 = iot2_Expression157
        self.iot2_Expression160 = iot2_Expression160
        self.iot2_Expression162 = iot2_Expression162
        self.iot2_Expression165 = iot2_Expression165
        self.iot2_Expression189 = iot2_Expression189
        self.iot2_Expression191 = iot2_Expression191
        self.iot2_Expression228 = iot2_Expression228
        
        pass
    @property
    def iot2_Expression(self):
        return self.__iot2_Expression

    @iot2_Expression.setter
    def iot2_Expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression", None)
        self.__iot2_Expression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Field34"):
                opp_val = getattr(old_value, "iot2_Field34", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Field34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Field34"):
                opp_val = getattr(value, "iot2_Field34", None)
                setattr(value, "iot2_Field34", self)

    @property
    def iot2_Expression150(self):
        return self.__iot2_Expression150

    @iot2_Expression150.setter
    def iot2_Expression150(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression150", None)
        self.__iot2_Expression150 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_Equal149"):
                opp_val = getattr(old_value, "iot2_Expression_Equal149", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression_Equal149", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_Equal149"):
                opp_val = getattr(value, "iot2_Expression_Equal149", None)
                setattr(value, "iot2_Expression_Equal149", self)

    @property
    def iot2_Expression203(self):
        return self.__iot2_Expression203

    @iot2_Expression203.setter
    def iot2_Expression203(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression203", None)
        self.__iot2_Expression203 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_CallFunction"):
                opp_val = getattr(old_value, "iot2_Expression_CallFunction", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression_CallFunction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_CallFunction"):
                opp_val = getattr(value, "iot2_Expression_CallFunction", None)
                setattr(value, "iot2_Expression_CallFunction", self)

    @property
    def iot2_Expression125(self):
        return self.__iot2_Expression125

    @iot2_Expression125.setter
    def iot2_Expression125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression125", None)
        self.__iot2_Expression125 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_And124"):
                opp_val = getattr(old_value, "iot2_Expression_And124", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression_And124", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_And124"):
                opp_val = getattr(value, "iot2_Expression_And124", None)
                setattr(value, "iot2_Expression_And124", self)

    @property
    def iot2_Expression189(self):
        return self.__iot2_Expression189

    @iot2_Expression189.setter
    def iot2_Expression189(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression189", None)
        self.__iot2_Expression189 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_Length"):
                opp_val = getattr(old_value, "iot2_Expression_Length", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression_Length", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_Length"):
                opp_val = getattr(value, "iot2_Expression_Length", None)
                setattr(value, "iot2_Expression_Length", self)

    @property
    def iot2_Expression147(self):
        return self.__iot2_Expression147

    @iot2_Expression147.setter
    def iot2_Expression147(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression147", None)
        self.__iot2_Expression147 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_Equal"):
                opp_val = getattr(old_value, "iot2_Expression_Equal", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression_Equal", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_Equal"):
                opp_val = getattr(value, "iot2_Expression_Equal", None)
                setattr(value, "iot2_Expression_Equal", self)

    @property
    def iot2_Expression135(self):
        return self.__iot2_Expression135

    @iot2_Expression135.setter
    def iot2_Expression135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression135", None)
        self.__iot2_Expression135 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_Larger_Equal134"):
                opp_val = getattr(old_value, "iot2_Expression_Larger_Equal134", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression_Larger_Equal134", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_Larger_Equal134"):
                opp_val = getattr(value, "iot2_Expression_Larger_Equal134", None)
                setattr(value, "iot2_Expression_Larger_Equal134", self)

    @property
    def iot2_Expression213(self):
        return self.__iot2_Expression213

    @iot2_Expression213.setter
    def iot2_Expression213(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression213", None)
        self.__iot2_Expression213 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_AccessMember"):
                opp_val = getattr(old_value, "iot2_Expression_AccessMember", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression_AccessMember", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_AccessMember"):
                opp_val = getattr(value, "iot2_Expression_AccessMember", None)
                setattr(value, "iot2_Expression_AccessMember", self)

    @property
    def iot2_Expression120(self):
        return self.__iot2_Expression120

    @iot2_Expression120.setter
    def iot2_Expression120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression120", None)
        self.__iot2_Expression120 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_Or119"):
                opp_val = getattr(old_value, "iot2_Expression_Or119", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression_Or119", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_Or119"):
                opp_val = getattr(value, "iot2_Expression_Or119", None)
                setattr(value, "iot2_Expression_Or119", self)

    @property
    def iot2_Expression165(self):
        return self.__iot2_Expression165

    @iot2_Expression165.setter
    def iot2_Expression165(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression165", None)
        self.__iot2_Expression165 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_Plus164"):
                opp_val = getattr(old_value, "iot2_Expression_Plus164", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression_Plus164", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_Plus164"):
                opp_val = getattr(value, "iot2_Expression_Plus164", None)
                setattr(value, "iot2_Expression_Plus164", self)

    @property
    def iot2_Expression42(self):
        return self.__iot2_Expression42

    @iot2_Expression42.setter
    def iot2_Expression42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression42", None)
        self.__iot2_Expression42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Statement_While"):
                opp_val = getattr(old_value, "iot2_Statement_While", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Statement_While", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Statement_While"):
                opp_val = getattr(value, "iot2_Statement_While", None)
                setattr(value, "iot2_Statement_While", self)

    @property
    def iot2_Expression130(self):
        return self.__iot2_Expression130

    @iot2_Expression130.setter
    def iot2_Expression130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression130", None)
        self.__iot2_Expression130 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_Larger129"):
                opp_val = getattr(old_value, "iot2_Expression_Larger129", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression_Larger129", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_Larger129"):
                opp_val = getattr(value, "iot2_Expression_Larger129", None)
                setattr(value, "iot2_Expression_Larger129", self)

    @property
    def iot2_Expression170(self):
        return self.__iot2_Expression170

    @iot2_Expression170.setter
    def iot2_Expression170(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression170", None)
        self.__iot2_Expression170 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_Minus169"):
                opp_val = getattr(old_value, "iot2_Expression_Minus169", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression_Minus169", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_Minus169"):
                opp_val = getattr(value, "iot2_Expression_Minus169", None)
                setattr(value, "iot2_Expression_Minus169", self)

    @property
    def iot2_Expression100(self):
        return self.__iot2_Expression100

    @iot2_Expression100.setter
    def iot2_Expression100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression100", None)
        self.__iot2_Expression100 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_LastStatement_ReturnWithValue"):
                opp_val = getattr(old_value, "iot2_LastStatement_ReturnWithValue", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_LastStatement_ReturnWithValue"):
                opp_val = getattr(value, "iot2_LastStatement_ReturnWithValue", None)
                if opp_val is None:
                    setattr(value, "iot2_LastStatement_ReturnWithValue", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def iot2_Expression193(self):
        return self.__iot2_Expression193

    @iot2_Expression193.setter
    def iot2_Expression193(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression193", None)
        self.__iot2_Expression193 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_Exponentiation"):
                opp_val = getattr(old_value, "iot2_Expression_Exponentiation", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression_Exponentiation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_Exponentiation"):
                opp_val = getattr(value, "iot2_Expression_Exponentiation", None)
                setattr(value, "iot2_Expression_Exponentiation", self)

    @property
    def iot2_Expression107(self):
        return self.__iot2_Expression107

    @iot2_Expression107.setter
    def iot2_Expression107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression107", None)
        self.__iot2_Expression107 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Statement_CallMemberFunction"):
                opp_val = getattr(old_value, "iot2_Statement_CallMemberFunction", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Statement_CallMemberFunction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Statement_CallMemberFunction"):
                opp_val = getattr(value, "iot2_Statement_CallMemberFunction", None)
                setattr(value, "iot2_Statement_CallMemberFunction", self)

    @property
    def iot2_Expression98(self):
        return self.__iot2_Expression98

    @iot2_Expression98.setter
    def iot2_Expression98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression98", None)
        self.__iot2_Expression98 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Field_AddEntryToTable_Brackets"):
                opp_val = getattr(old_value, "iot2_Field_AddEntryToTable_Brackets", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Field_AddEntryToTable_Brackets", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Field_AddEntryToTable_Brackets"):
                opp_val = getattr(value, "iot2_Field_AddEntryToTable_Brackets", None)
                setattr(value, "iot2_Field_AddEntryToTable_Brackets", self)

    @property
    def iot2_Expression140(self):
        return self.__iot2_Expression140

    @iot2_Expression140.setter
    def iot2_Expression140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression140", None)
        self.__iot2_Expression140 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_Smaller139"):
                opp_val = getattr(old_value, "iot2_Expression_Smaller139", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression_Smaller139", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_Smaller139"):
                opp_val = getattr(value, "iot2_Expression_Smaller139", None)
                setattr(value, "iot2_Expression_Smaller139", self)

    @property
    def iot2_Expression79(self):
        return self.__iot2_Expression79

    @iot2_Expression79.setter
    def iot2_Expression79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression79", None)
        self.__iot2_Expression79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Statement_For_Generic"):
                opp_val = getattr(old_value, "iot2_Statement_For_Generic", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Statement_For_Generic"):
                opp_val = getattr(value, "iot2_Statement_For_Generic", None)
                if opp_val is None:
                    setattr(value, "iot2_Statement_For_Generic", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def iot2_Expression96(self):
        return self.__iot2_Expression96

    @iot2_Expression96.setter
    def iot2_Expression96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression96", None)
        self.__iot2_Expression96 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Functioncall_Arguments"):
                opp_val = getattr(old_value, "iot2_Functioncall_Arguments", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Functioncall_Arguments"):
                opp_val = getattr(value, "iot2_Functioncall_Arguments", None)
                if opp_val is None:
                    setattr(value, "iot2_Functioncall_Arguments", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def iot2_Expression122(self):
        return self.__iot2_Expression122

    @iot2_Expression122.setter
    def iot2_Expression122(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression122", None)
        self.__iot2_Expression122 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_And"):
                opp_val = getattr(old_value, "iot2_Expression_And", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression_And", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_And"):
                opp_val = getattr(value, "iot2_Expression_And", None)
                setattr(value, "iot2_Expression_And", self)

    @property
    def iot2_Expression142(self):
        return self.__iot2_Expression142

    @iot2_Expression142.setter
    def iot2_Expression142(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression142", None)
        self.__iot2_Expression142 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_Smaller_Equal"):
                opp_val = getattr(old_value, "iot2_Expression_Smaller_Equal", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression_Smaller_Equal", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_Smaller_Equal"):
                opp_val = getattr(value, "iot2_Expression_Smaller_Equal", None)
                setattr(value, "iot2_Expression_Smaller_Equal", self)

    @property
    def iot2_Expression50(self):
        return self.__iot2_Expression50

    @iot2_Expression50.setter
    def iot2_Expression50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression50", None)
        self.__iot2_Expression50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Statement_Repeat49"):
                opp_val = getattr(old_value, "iot2_Statement_Repeat49", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Statement_Repeat49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Statement_Repeat49"):
                opp_val = getattr(value, "iot2_Statement_Repeat49", None)
                setattr(value, "iot2_Statement_Repeat49", self)

    @property
    def iot2_Expression87(self):
        return self.__iot2_Expression87

    @iot2_Expression87.setter
    def iot2_Expression87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression87", None)
        self.__iot2_Expression87 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Statement_Local_Variable_Declaration"):
                opp_val = getattr(old_value, "iot2_Statement_Local_Variable_Declaration", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Statement_Local_Variable_Declaration"):
                opp_val = getattr(value, "iot2_Statement_Local_Variable_Declaration", None)
                if opp_val is None:
                    setattr(value, "iot2_Statement_Local_Variable_Declaration", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def iot2_Expression152(self):
        return self.__iot2_Expression152

    @iot2_Expression152.setter
    def iot2_Expression152(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression152", None)
        self.__iot2_Expression152 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_Not_Equal"):
                opp_val = getattr(old_value, "iot2_Expression_Not_Equal", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression_Not_Equal", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_Not_Equal"):
                opp_val = getattr(value, "iot2_Expression_Not_Equal", None)
                setattr(value, "iot2_Expression_Not_Equal", self)

    @property
    def iot2_Expression162(self):
        return self.__iot2_Expression162

    @iot2_Expression162.setter
    def iot2_Expression162(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression162", None)
        self.__iot2_Expression162 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_Plus"):
                opp_val = getattr(old_value, "iot2_Expression_Plus", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression_Plus", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_Plus"):
                opp_val = getattr(value, "iot2_Expression_Plus", None)
                setattr(value, "iot2_Expression_Plus", self)

    @property
    def iot2_Expression208(self):
        return self.__iot2_Expression208

    @iot2_Expression208.setter
    def iot2_Expression208(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression208", None)
        self.__iot2_Expression208 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_AccessArray"):
                opp_val = getattr(old_value, "iot2_Expression_AccessArray", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression_AccessArray", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_AccessArray"):
                opp_val = getattr(value, "iot2_Expression_AccessArray", None)
                setattr(value, "iot2_Expression_AccessArray", self)

    @property
    def iot2_Expression175(self):
        return self.__iot2_Expression175

    @iot2_Expression175.setter
    def iot2_Expression175(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression175", None)
        self.__iot2_Expression175 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_Multiplication174"):
                opp_val = getattr(old_value, "iot2_Expression_Multiplication174", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression_Multiplication174", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_Multiplication174"):
                opp_val = getattr(value, "iot2_Expression_Multiplication174", None)
                setattr(value, "iot2_Expression_Multiplication174", self)

    @property
    def iot2_Expression68(self):
        return self.__iot2_Expression68

    @iot2_Expression68.setter
    def iot2_Expression68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression68", None)
        self.__iot2_Expression68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Statement_For_Numeric"):
                opp_val = getattr(old_value, "iot2_Statement_For_Numeric", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Statement_For_Numeric", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Statement_For_Numeric"):
                opp_val = getattr(value, "iot2_Statement_For_Numeric", None)
                setattr(value, "iot2_Statement_For_Numeric", self)

    @property
    def iot2_Expression228(self):
        return self.__iot2_Expression228

    @iot2_Expression228.setter
    def iot2_Expression228(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression228", None)
        self.__iot2_Expression228 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_OpaqueAction"):
                opp_val = getattr(old_value, "iot2_OpaqueAction", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_OpaqueAction"):
                opp_val = getattr(value, "iot2_OpaqueAction", None)
                if opp_val is None:
                    setattr(value, "iot2_OpaqueAction", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def iot2_Expression127(self):
        return self.__iot2_Expression127

    @iot2_Expression127.setter
    def iot2_Expression127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression127", None)
        self.__iot2_Expression127 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_Larger"):
                opp_val = getattr(old_value, "iot2_Expression_Larger", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression_Larger", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_Larger"):
                opp_val = getattr(value, "iot2_Expression_Larger", None)
                setattr(value, "iot2_Expression_Larger", self)

    @property
    def iot2_Expression105(self):
        return self.__iot2_Expression105

    @iot2_Expression105.setter
    def iot2_Expression105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression105", None)
        self.__iot2_Expression105 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Statement_Assignment104"):
                opp_val = getattr(old_value, "iot2_Statement_Assignment104", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Statement_Assignment104"):
                opp_val = getattr(value, "iot2_Statement_Assignment104", None)
                if opp_val is None:
                    setattr(value, "iot2_Statement_Assignment104", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def iot2_Expression167(self):
        return self.__iot2_Expression167

    @iot2_Expression167.setter
    def iot2_Expression167(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression167", None)
        self.__iot2_Expression167 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_Minus"):
                opp_val = getattr(old_value, "iot2_Expression_Minus", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression_Minus", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_Minus"):
                opp_val = getattr(value, "iot2_Expression_Minus", None)
                setattr(value, "iot2_Expression_Minus", self)

    @property
    def iot2_Expression185(self):
        return self.__iot2_Expression185

    @iot2_Expression185.setter
    def iot2_Expression185(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression185", None)
        self.__iot2_Expression185 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_Modulo184"):
                opp_val = getattr(old_value, "iot2_Expression_Modulo184", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression_Modulo184", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_Modulo184"):
                opp_val = getattr(value, "iot2_Expression_Modulo184", None)
                setattr(value, "iot2_Expression_Modulo184", self)

    @property
    def iot2_Expression117(self):
        return self.__iot2_Expression117

    @iot2_Expression117.setter
    def iot2_Expression117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression117", None)
        self.__iot2_Expression117 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_Or"):
                opp_val = getattr(old_value, "iot2_Expression_Or", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression_Or", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_Or"):
                opp_val = getattr(value, "iot2_Expression_Or", None)
                setattr(value, "iot2_Expression_Or", self)

    @property
    def iot2_Expression63(self):
        return self.__iot2_Expression63

    @iot2_Expression63.setter
    def iot2_Expression63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression63", None)
        self.__iot2_Expression63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Statement_If_Then_Else_ElseIfPart62"):
                opp_val = getattr(old_value, "iot2_Statement_If_Then_Else_ElseIfPart62", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Statement_If_Then_Else_ElseIfPart62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Statement_If_Then_Else_ElseIfPart62"):
                opp_val = getattr(value, "iot2_Statement_If_Then_Else_ElseIfPart62", None)
                setattr(value, "iot2_Statement_If_Then_Else_ElseIfPart62", self)

    @property
    def iot2_Expression137(self):
        return self.__iot2_Expression137

    @iot2_Expression137.setter
    def iot2_Expression137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression137", None)
        self.__iot2_Expression137 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_Smaller"):
                opp_val = getattr(old_value, "iot2_Expression_Smaller", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression_Smaller", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_Smaller"):
                opp_val = getattr(value, "iot2_Expression_Smaller", None)
                setattr(value, "iot2_Expression_Smaller", self)

    @property
    def iot2_Expression172(self):
        return self.__iot2_Expression172

    @iot2_Expression172.setter
    def iot2_Expression172(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression172", None)
        self.__iot2_Expression172 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_Multiplication"):
                opp_val = getattr(old_value, "iot2_Expression_Multiplication", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression_Multiplication", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_Multiplication"):
                opp_val = getattr(value, "iot2_Expression_Multiplication", None)
                setattr(value, "iot2_Expression_Multiplication", self)

    @property
    def iot2_Expression196(self):
        return self.__iot2_Expression196

    @iot2_Expression196.setter
    def iot2_Expression196(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression196", None)
        self.__iot2_Expression196 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_Exponentiation195"):
                opp_val = getattr(old_value, "iot2_Expression_Exponentiation195", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression_Exponentiation195", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_Exponentiation195"):
                opp_val = getattr(value, "iot2_Expression_Exponentiation195", None)
                setattr(value, "iot2_Expression_Exponentiation195", self)

    @property
    def iot2_Expression132(self):
        return self.__iot2_Expression132

    @iot2_Expression132.setter
    def iot2_Expression132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression132", None)
        self.__iot2_Expression132 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_Larger_Equal"):
                opp_val = getattr(old_value, "iot2_Expression_Larger_Equal", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression_Larger_Equal", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_Larger_Equal"):
                opp_val = getattr(value, "iot2_Expression_Larger_Equal", None)
                setattr(value, "iot2_Expression_Larger_Equal", self)

    @property
    def iot2_Expression71(self):
        return self.__iot2_Expression71

    @iot2_Expression71.setter
    def iot2_Expression71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression71", None)
        self.__iot2_Expression71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Statement_For_Numeric70"):
                opp_val = getattr(old_value, "iot2_Statement_For_Numeric70", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Statement_For_Numeric70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Statement_For_Numeric70"):
                opp_val = getattr(value, "iot2_Statement_For_Numeric70", None)
                setattr(value, "iot2_Statement_For_Numeric70", self)

    @property
    def iot2_Expression177(self):
        return self.__iot2_Expression177

    @iot2_Expression177.setter
    def iot2_Expression177(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression177", None)
        self.__iot2_Expression177 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_Division"):
                opp_val = getattr(old_value, "iot2_Expression_Division", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression_Division", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_Division"):
                opp_val = getattr(value, "iot2_Expression_Division", None)
                setattr(value, "iot2_Expression_Division", self)

    @property
    def iot2_Expression180(self):
        return self.__iot2_Expression180

    @iot2_Expression180.setter
    def iot2_Expression180(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression180", None)
        self.__iot2_Expression180 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_Division179"):
                opp_val = getattr(old_value, "iot2_Expression_Division179", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression_Division179", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_Division179"):
                opp_val = getattr(value, "iot2_Expression_Division179", None)
                setattr(value, "iot2_Expression_Division179", self)

    @property
    def iot2_Expression112(self):
        return self.__iot2_Expression112

    @iot2_Expression112.setter
    def iot2_Expression112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression112", None)
        self.__iot2_Expression112 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Statement_CallFunction"):
                opp_val = getattr(old_value, "iot2_Statement_CallFunction", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Statement_CallFunction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Statement_CallFunction"):
                opp_val = getattr(value, "iot2_Statement_CallFunction", None)
                setattr(value, "iot2_Statement_CallFunction", self)

    @property
    def iot2_Expression160(self):
        return self.__iot2_Expression160

    @iot2_Expression160.setter
    def iot2_Expression160(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression160", None)
        self.__iot2_Expression160 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_Concatenation159"):
                opp_val = getattr(old_value, "iot2_Expression_Concatenation159", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression_Concatenation159", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_Concatenation159"):
                opp_val = getattr(value, "iot2_Expression_Concatenation159", None)
                setattr(value, "iot2_Expression_Concatenation159", self)

    @property
    def iot2_Expression155(self):
        return self.__iot2_Expression155

    @iot2_Expression155.setter
    def iot2_Expression155(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression155", None)
        self.__iot2_Expression155 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_Not_Equal154"):
                opp_val = getattr(old_value, "iot2_Expression_Not_Equal154", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression_Not_Equal154", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_Not_Equal154"):
                opp_val = getattr(value, "iot2_Expression_Not_Equal154", None)
                setattr(value, "iot2_Expression_Not_Equal154", self)

    @property
    def iot2_Expression102(self):
        return self.__iot2_Expression102

    @iot2_Expression102.setter
    def iot2_Expression102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression102", None)
        self.__iot2_Expression102 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Statement_Assignment"):
                opp_val = getattr(old_value, "iot2_Statement_Assignment", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Statement_Assignment"):
                opp_val = getattr(value, "iot2_Statement_Assignment", None)
                if opp_val is None:
                    setattr(value, "iot2_Statement_Assignment", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def iot2_Expression187(self):
        return self.__iot2_Expression187

    @iot2_Expression187.setter
    def iot2_Expression187(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression187", None)
        self.__iot2_Expression187 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_Negate"):
                opp_val = getattr(old_value, "iot2_Expression_Negate", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression_Negate", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_Negate"):
                opp_val = getattr(value, "iot2_Expression_Negate", None)
                setattr(value, "iot2_Expression_Negate", self)

    @property
    def iot2_Expression191(self):
        return self.__iot2_Expression191

    @iot2_Expression191.setter
    def iot2_Expression191(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression191", None)
        self.__iot2_Expression191 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_Invert"):
                opp_val = getattr(old_value, "iot2_Expression_Invert", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression_Invert", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_Invert"):
                opp_val = getattr(value, "iot2_Expression_Invert", None)
                setattr(value, "iot2_Expression_Invert", self)

    @property
    def iot2_Expression157(self):
        return self.__iot2_Expression157

    @iot2_Expression157.setter
    def iot2_Expression157(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression157", None)
        self.__iot2_Expression157 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_Concatenation"):
                opp_val = getattr(old_value, "iot2_Expression_Concatenation", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression_Concatenation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_Concatenation"):
                opp_val = getattr(value, "iot2_Expression_Concatenation", None)
                setattr(value, "iot2_Expression_Concatenation", self)

    @property
    def iot2_Expression182(self):
        return self.__iot2_Expression182

    @iot2_Expression182.setter
    def iot2_Expression182(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression182", None)
        self.__iot2_Expression182 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_Modulo"):
                opp_val = getattr(old_value, "iot2_Expression_Modulo", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression_Modulo", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_Modulo"):
                opp_val = getattr(value, "iot2_Expression_Modulo", None)
                setattr(value, "iot2_Expression_Modulo", self)

    @property
    def iot2_Expression145(self):
        return self.__iot2_Expression145

    @iot2_Expression145.setter
    def iot2_Expression145(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression145", None)
        self.__iot2_Expression145 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_Smaller_Equal144"):
                opp_val = getattr(old_value, "iot2_Expression_Smaller_Equal144", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression_Smaller_Equal144", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_Smaller_Equal144"):
                opp_val = getattr(value, "iot2_Expression_Smaller_Equal144", None)
                setattr(value, "iot2_Expression_Smaller_Equal144", self)

    @property
    def iot2_Expression52(self):
        return self.__iot2_Expression52

    @iot2_Expression52.setter
    def iot2_Expression52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression52", None)
        self.__iot2_Expression52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Statement_If_Then_Else"):
                opp_val = getattr(old_value, "iot2_Statement_If_Then_Else", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Statement_If_Then_Else", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Statement_If_Then_Else"):
                opp_val = getattr(value, "iot2_Statement_If_Then_Else", None)
                setattr(value, "iot2_Statement_If_Then_Else", self)

    @property
    def iot2_Expression211(self):
        return self.__iot2_Expression211

    @iot2_Expression211.setter
    def iot2_Expression211(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression211", None)
        self.__iot2_Expression211 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_AccessArray210"):
                opp_val = getattr(old_value, "iot2_Expression_AccessArray210", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression_AccessArray210", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_AccessArray210"):
                opp_val = getattr(value, "iot2_Expression_AccessArray210", None)
                setattr(value, "iot2_Expression_AccessArray210", self)

    @property
    def iot2_Expression74(self):
        return self.__iot2_Expression74

    @iot2_Expression74.setter
    def iot2_Expression74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression74", None)
        self.__iot2_Expression74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Statement_For_Numeric73"):
                opp_val = getattr(old_value, "iot2_Statement_For_Numeric73", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Statement_For_Numeric73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Statement_For_Numeric73"):
                opp_val = getattr(value, "iot2_Statement_For_Numeric73", None)
                setattr(value, "iot2_Statement_For_Numeric73", self)

    @property
    def iot2_Expression198(self):
        return self.__iot2_Expression198

    @iot2_Expression198.setter
    def iot2_Expression198(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression__iot2_Expression198", None)
        self.__iot2_Expression198 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_CallMemberFunction"):
                opp_val = getattr(old_value, "iot2_Expression_CallMemberFunction", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression_CallMemberFunction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_CallMemberFunction"):
                opp_val = getattr(value, "iot2_Expression_CallMemberFunction", None)
                setattr(value, "iot2_Expression_CallMemberFunction", self)

    def execute(self, iot2_c):
        # TODO: Implement execute method
        pass

class IDLType:

    pass
class iot2_PrimitiveDef(IDLType):

    def __init__(self, kind: str):
        self.kind = kind
        
        pass
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


class LastStatement:

    pass
class iot2_LastStatement_Break(LastStatement):

    pass
class iot2_LastStatement_Return(LastStatement):

    def __init__(self):
        
        pass
    def execute(self, iot2_c):
        # TODO: Implement execute method
        pass

class iot2_LastStatement:

    def __init__(self, iot2_LastStatement: "iot2_Block" = None):
        self.iot2_LastStatement = iot2_LastStatement
        
        pass
    @property
    def iot2_LastStatement(self):
        return self.__iot2_LastStatement

    @iot2_LastStatement.setter
    def iot2_LastStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_LastStatement__iot2_LastStatement", None)
        self.__iot2_LastStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Block38"):
                opp_val = getattr(old_value, "iot2_Block38", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Block38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Block38"):
                opp_val = getattr(value, "iot2_Block38", None)
                setattr(value, "iot2_Block38", self)

    def execute(self, iot2_c):
        # TODO: Implement execute method
        pass

class iot2_Statement:

    def __init__(self, iot2_Statement: "iot2_Block" = None):
        self.iot2_Statement = iot2_Statement
        
        pass
    @property
    def iot2_Statement(self):
        return self.__iot2_Statement

    @iot2_Statement.setter
    def iot2_Statement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Statement__iot2_Statement", None)
        self.__iot2_Statement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Block36"):
                opp_val = getattr(old_value, "iot2_Block36", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Block36"):
                opp_val = getattr(value, "iot2_Block36", None)
                if opp_val is None:
                    setattr(value, "iot2_Block36", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def execute(self, iot2_c):
        # TODO: Implement execute method
        pass

class Chunk:

    pass
class iot2_NamedElement(ABC):

    def __init__(self, identifier: str, name: str):
        self.identifier = identifier
        self.name = name
        
        pass
    @property
    def identifier(self):
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    def execute(self, iot2_c):
        # TODO: Implement execute method
        pass

class iot2_Chunk:

    def __init__(self):
        
        pass
    def execute(self, iot2_c):
        # TODO: Implement execute method
        pass

class iot2_Block(Chunk):

    def __init__(self, iot2_Block: "iot2_OperationDef" = None, iot2_Block36: set["iot2_Statement"] = None, iot2_Block38: "iot2_LastStatement" = None, iot2_Block55: "iot2_Statement_If_Then_Else" = None, iot2_Block60: "iot2_Statement_If_Then_Else" = None, iot2_Block40: "iot2_Statement_Block" = None, iot2_Block45: "iot2_Statement_While" = None, iot2_Block47: "iot2_Statement_Repeat" = None, iot2_Block66: "iot2_Statement_If_Then_Else_ElseIfPart" = None, iot2_Block77: "iot2_Statement_For_Numeric" = None, iot2_Block82: "iot2_Statement_For_Generic" = None, iot2_Block94: "iot2_Function" = None):
        self.iot2_Block = iot2_Block
        self.iot2_Block36 = iot2_Block36 if iot2_Block36 is not None else set()
        self.iot2_Block38 = iot2_Block38
        self.iot2_Block55 = iot2_Block55
        self.iot2_Block60 = iot2_Block60
        self.iot2_Block40 = iot2_Block40
        self.iot2_Block45 = iot2_Block45
        self.iot2_Block47 = iot2_Block47
        self.iot2_Block66 = iot2_Block66
        self.iot2_Block77 = iot2_Block77
        self.iot2_Block82 = iot2_Block82
        self.iot2_Block94 = iot2_Block94
        
        pass
    @property
    def iot2_Block47(self):
        return self.__iot2_Block47

    @iot2_Block47.setter
    def iot2_Block47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Block__iot2_Block47", None)
        self.__iot2_Block47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Statement_Repeat"):
                opp_val = getattr(old_value, "iot2_Statement_Repeat", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Statement_Repeat", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Statement_Repeat"):
                opp_val = getattr(value, "iot2_Statement_Repeat", None)
                setattr(value, "iot2_Statement_Repeat", self)

    @property
    def iot2_Block60(self):
        return self.__iot2_Block60

    @iot2_Block60.setter
    def iot2_Block60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Block__iot2_Block60", None)
        self.__iot2_Block60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Statement_If_Then_Else59"):
                opp_val = getattr(old_value, "iot2_Statement_If_Then_Else59", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Statement_If_Then_Else59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Statement_If_Then_Else59"):
                opp_val = getattr(value, "iot2_Statement_If_Then_Else59", None)
                setattr(value, "iot2_Statement_If_Then_Else59", self)

    @property
    def iot2_Block94(self):
        return self.__iot2_Block94

    @iot2_Block94.setter
    def iot2_Block94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Block__iot2_Block94", None)
        self.__iot2_Block94 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Function93"):
                opp_val = getattr(old_value, "iot2_Function93", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Function93", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Function93"):
                opp_val = getattr(value, "iot2_Function93", None)
                setattr(value, "iot2_Function93", self)

    @property
    def iot2_Block40(self):
        return self.__iot2_Block40

    @iot2_Block40.setter
    def iot2_Block40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Block__iot2_Block40", None)
        self.__iot2_Block40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Statement_Block"):
                opp_val = getattr(old_value, "iot2_Statement_Block", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Statement_Block", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Statement_Block"):
                opp_val = getattr(value, "iot2_Statement_Block", None)
                setattr(value, "iot2_Statement_Block", self)

    @property
    def iot2_Block66(self):
        return self.__iot2_Block66

    @iot2_Block66.setter
    def iot2_Block66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Block__iot2_Block66", None)
        self.__iot2_Block66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Statement_If_Then_Else_ElseIfPart65"):
                opp_val = getattr(old_value, "iot2_Statement_If_Then_Else_ElseIfPart65", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Statement_If_Then_Else_ElseIfPart65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Statement_If_Then_Else_ElseIfPart65"):
                opp_val = getattr(value, "iot2_Statement_If_Then_Else_ElseIfPart65", None)
                setattr(value, "iot2_Statement_If_Then_Else_ElseIfPart65", self)

    @property
    def iot2_Block(self):
        return self.__iot2_Block

    @iot2_Block.setter
    def iot2_Block(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Block__iot2_Block", None)
        self.__iot2_Block = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_OperationDef25"):
                opp_val = getattr(old_value, "iot2_OperationDef25", None)
                if opp_val == self:
                    setattr(old_value, "iot2_OperationDef25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_OperationDef25"):
                opp_val = getattr(value, "iot2_OperationDef25", None)
                setattr(value, "iot2_OperationDef25", self)

    @property
    def iot2_Block36(self):
        return self.__iot2_Block36

    @iot2_Block36.setter
    def iot2_Block36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Block__iot2_Block36", None)
        self.__iot2_Block36 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iot2_Statement"):
                    opp_val = getattr(item, "iot2_Statement", None)
                    
                    if opp_val == self:
                        setattr(item, "iot2_Statement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iot2_Statement"):
                    opp_val = getattr(item, "iot2_Statement", None)
                    
                    setattr(item, "iot2_Statement", self)
                    

    @property
    def iot2_Block55(self):
        return self.__iot2_Block55

    @iot2_Block55.setter
    def iot2_Block55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Block__iot2_Block55", None)
        self.__iot2_Block55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Statement_If_Then_Else54"):
                opp_val = getattr(old_value, "iot2_Statement_If_Then_Else54", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Statement_If_Then_Else54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Statement_If_Then_Else54"):
                opp_val = getattr(value, "iot2_Statement_If_Then_Else54", None)
                setattr(value, "iot2_Statement_If_Then_Else54", self)

    @property
    def iot2_Block45(self):
        return self.__iot2_Block45

    @iot2_Block45.setter
    def iot2_Block45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Block__iot2_Block45", None)
        self.__iot2_Block45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Statement_While44"):
                opp_val = getattr(old_value, "iot2_Statement_While44", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Statement_While44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Statement_While44"):
                opp_val = getattr(value, "iot2_Statement_While44", None)
                setattr(value, "iot2_Statement_While44", self)

    @property
    def iot2_Block38(self):
        return self.__iot2_Block38

    @iot2_Block38.setter
    def iot2_Block38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Block__iot2_Block38", None)
        self.__iot2_Block38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_LastStatement"):
                opp_val = getattr(old_value, "iot2_LastStatement", None)
                if opp_val == self:
                    setattr(old_value, "iot2_LastStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_LastStatement"):
                opp_val = getattr(value, "iot2_LastStatement", None)
                setattr(value, "iot2_LastStatement", self)

    @property
    def iot2_Block82(self):
        return self.__iot2_Block82

    @iot2_Block82.setter
    def iot2_Block82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Block__iot2_Block82", None)
        self.__iot2_Block82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Statement_For_Generic81"):
                opp_val = getattr(old_value, "iot2_Statement_For_Generic81", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Statement_For_Generic81", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Statement_For_Generic81"):
                opp_val = getattr(value, "iot2_Statement_For_Generic81", None)
                setattr(value, "iot2_Statement_For_Generic81", self)

    @property
    def iot2_Block77(self):
        return self.__iot2_Block77

    @iot2_Block77.setter
    def iot2_Block77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Block__iot2_Block77", None)
        self.__iot2_Block77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Statement_For_Numeric76"):
                opp_val = getattr(old_value, "iot2_Statement_For_Numeric76", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Statement_For_Numeric76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Statement_For_Numeric76"):
                opp_val = getattr(value, "iot2_Statement_For_Numeric76", None)
                setattr(value, "iot2_Statement_For_Numeric76", self)

    def execute(self, iot2_c):
        # TODO: Implement execute method
        pass

class iot2_IDLType(ABC):

    def __init__(self, typeCode: str, iot2_IDLType: "iot2_Typed" = None):
        self.typeCode = typeCode
        self.iot2_IDLType = iot2_IDLType
        
        pass
    @property
    def typeCode(self):
        return self.__typeCode

    @typeCode.setter
    def typeCode(self, typeCode: str):
        self.__typeCode = typeCode


    @property
    def iot2_IDLType(self):
        return self.__iot2_IDLType

    @iot2_IDLType.setter
    def iot2_IDLType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_IDLType__iot2_IDLType", None)
        self.__iot2_IDLType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Typed"):
                opp_val = getattr(old_value, "iot2_Typed", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Typed", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Typed"):
                opp_val = getattr(value, "iot2_Typed", None)
                setattr(value, "iot2_Typed", self)

class iot2_Typed(ABC):

    pass
class NamedElement:

    pass
class iot2_Contained(NamedElement):

    def __init__(self, repositoryId: str, version: str, absoluteName: str, Contained: "iot2_Container" = None, contains: "iot2_Container" = None):
        self.repositoryId = repositoryId
        self.version = version
        self.absoluteName = absoluteName
        self.Contained = Contained
        self.contains = contains
        
        pass
    @property
    def repositoryId(self):
        return self.__repositoryId

    @repositoryId.setter
    def repositoryId(self, repositoryId: str):
        self.__repositoryId = repositoryId


    @property
    def absoluteName(self):
        return self.__absoluteName

    @absoluteName.setter
    def absoluteName(self, absoluteName: str):
        self.__absoluteName = absoluteName


    @property
    def version(self):
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version


    @property
    def contains(self):
        return self.__contains

    @contains.setter
    def contains(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Contained__contains", None)
        self.__contains = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Container"):
                opp_val = getattr(old_value, "Container", None)
                if opp_val == self:
                    setattr(old_value, "Container", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Container"):
                opp_val = getattr(value, "Container", None)
                setattr(value, "Container", self)

    @property
    def Contained(self):
        return self.__Contained

    @Contained.setter
    def Contained(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Contained__Contained", None)
        self.__Contained = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "definedIn"):
                opp_val = getattr(old_value, "definedIn", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "definedIn"):
                opp_val = getattr(value, "definedIn", None)
                if opp_val is None:
                    setattr(value, "definedIn", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class HWComponent:

    pass
class iot2_Actuator(HWComponent):

    pass
class iot2_Sensor(HWComponent):

    pass
class iot2_Activity(NamedElement):

    def __init__(self, activity: set["iot2_ActivityNode"] = None, iot2_Activity14: set["iot2_ActivityEdge"] = None, iot2_Activity16: set["iot2_Variable"] = None, iot2_Activity18: set["iot2_Variable"] = None, iot2_Activity: "iot2_Sketch" = None, iot2_Activity268: "iot2_Context" = None, Activity: "iot2_ActivityNode" = None):
        self.activity = activity if activity is not None else set()
        self.iot2_Activity14 = iot2_Activity14 if iot2_Activity14 is not None else set()
        self.iot2_Activity16 = iot2_Activity16 if iot2_Activity16 is not None else set()
        self.iot2_Activity18 = iot2_Activity18 if iot2_Activity18 is not None else set()
        self.iot2_Activity = iot2_Activity
        self.iot2_Activity268 = iot2_Activity268
        self.Activity = Activity
        
        pass
    @property
    def activity(self):
        return self.__activity

    @activity.setter
    def activity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Activity__activity", None)
        self.__activity = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActivityNode"):
                    opp_val = getattr(item, "ActivityNode", None)
                    
                    if opp_val == self:
                        setattr(item, "ActivityNode", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActivityNode"):
                    opp_val = getattr(item, "ActivityNode", None)
                    
                    setattr(item, "ActivityNode", self)
                    

    @property
    def Activity(self):
        return self.__Activity

    @Activity.setter
    def Activity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Activity__Activity", None)
        self.__Activity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nodes"):
                opp_val = getattr(old_value, "nodes", None)
                if opp_val == self:
                    setattr(old_value, "nodes", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nodes"):
                opp_val = getattr(value, "nodes", None)
                setattr(value, "nodes", self)

    @property
    def iot2_Activity(self):
        return self.__iot2_Activity

    @iot2_Activity.setter
    def iot2_Activity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Activity__iot2_Activity", None)
        self.__iot2_Activity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Sketch9"):
                opp_val = getattr(old_value, "iot2_Sketch9", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Sketch9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Sketch9"):
                opp_val = getattr(value, "iot2_Sketch9", None)
                setattr(value, "iot2_Sketch9", self)

    @property
    def iot2_Activity18(self):
        return self.__iot2_Activity18

    @iot2_Activity18.setter
    def iot2_Activity18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Activity__iot2_Activity18", None)
        self.__iot2_Activity18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iot2_Variable19"):
                    opp_val = getattr(item, "iot2_Variable19", None)
                    
                    if opp_val == self:
                        setattr(item, "iot2_Variable19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iot2_Variable19"):
                    opp_val = getattr(item, "iot2_Variable19", None)
                    
                    setattr(item, "iot2_Variable19", self)
                    

    @property
    def iot2_Activity14(self):
        return self.__iot2_Activity14

    @iot2_Activity14.setter
    def iot2_Activity14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Activity__iot2_Activity14", None)
        self.__iot2_Activity14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iot2_ActivityEdge"):
                    opp_val = getattr(item, "iot2_ActivityEdge", None)
                    
                    if opp_val == self:
                        setattr(item, "iot2_ActivityEdge", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iot2_ActivityEdge"):
                    opp_val = getattr(item, "iot2_ActivityEdge", None)
                    
                    setattr(item, "iot2_ActivityEdge", self)
                    

    @property
    def iot2_Activity268(self):
        return self.__iot2_Activity268

    @iot2_Activity268.setter
    def iot2_Activity268(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Activity__iot2_Activity268", None)
        self.__iot2_Activity268 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Context267"):
                opp_val = getattr(old_value, "iot2_Context267", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Context267", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Context267"):
                opp_val = getattr(value, "iot2_Context267", None)
                setattr(value, "iot2_Context267", self)

    @property
    def iot2_Activity16(self):
        return self.__iot2_Activity16

    @iot2_Activity16.setter
    def iot2_Activity16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Activity__iot2_Activity16", None)
        self.__iot2_Activity16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iot2_Variable"):
                    opp_val = getattr(item, "iot2_Variable", None)
                    
                    if opp_val == self:
                        setattr(item, "iot2_Variable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iot2_Variable"):
                    opp_val = getattr(item, "iot2_Variable", None)
                    
                    setattr(item, "iot2_Variable", self)
                    

    def main(self, iot2_value):
        # TODO: Implement main method
        pass

    def execute(self, iot2_c):
        # TODO: Implement execute method
        pass

    def getVariableValue(self, iot2_variableName) :
        # TODO: Implement getVariableValue method
        pass

    def getIntegerVariableValue(self, iot2_variableName):
        # TODO: Implement getIntegerVariableValue method
        pass

    def getBooleanVariableValue(self, iot2_variableName):
        # TODO: Implement getBooleanVariableValue method
        pass

    def getVariable(self, iot2_variableName) :
        # TODO: Implement getVariable method
        pass

    def writeTrace(self):
        # TODO: Implement writeTrace method
        pass

    def writeToFile(self):
        # TODO: Implement writeToFile method
        pass

    def printTrace(self):
        # TODO: Implement printTrace method
        pass

    def reset(self):
        # TODO: Implement reset method
        pass

class Typed:

    pass
class iot2_ParameterDef(Typed):

    def __init__(self, identifier: str, direction: str, iot2_ParameterDef: "iot2_OperationDef" = None):
        self.identifier = identifier
        self.direction = direction
        self.iot2_ParameterDef = iot2_ParameterDef
        
        pass
    @property
    def identifier(self):
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier


    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction


    @property
    def iot2_ParameterDef(self):
        return self.__iot2_ParameterDef

    @iot2_ParameterDef.setter
    def iot2_ParameterDef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_ParameterDef__iot2_ParameterDef", None)
        self.__iot2_ParameterDef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_OperationDef21"):
                opp_val = getattr(old_value, "iot2_OperationDef21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_OperationDef21"):
                opp_val = getattr(value, "iot2_OperationDef21", None)
                if opp_val is None:
                    setattr(value, "iot2_OperationDef21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class iot2_Field(Typed):

    def __init__(self, identifier: str, iot2_Field: "iot2_ExceptionDef" = None, iot2_Field34: "iot2_Expression" = None, iot2_Field91: "iot2_Expression_TableConstructor" = None):
        self.identifier = identifier
        self.iot2_Field = iot2_Field
        self.iot2_Field34 = iot2_Field34
        self.iot2_Field91 = iot2_Field91
        
        pass
    @property
    def identifier(self):
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier


    @property
    def iot2_Field34(self):
        return self.__iot2_Field34

    @iot2_Field34.setter
    def iot2_Field34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Field__iot2_Field34", None)
        self.__iot2_Field34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression"):
                opp_val = getattr(old_value, "iot2_Expression", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression"):
                opp_val = getattr(value, "iot2_Expression", None)
                setattr(value, "iot2_Expression", self)

    @property
    def iot2_Field91(self):
        return self.__iot2_Field91

    @iot2_Field91.setter
    def iot2_Field91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Field__iot2_Field91", None)
        self.__iot2_Field91 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression_TableConstructor"):
                opp_val = getattr(old_value, "iot2_Expression_TableConstructor", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression_TableConstructor"):
                opp_val = getattr(value, "iot2_Expression_TableConstructor", None)
                if opp_val is None:
                    setattr(value, "iot2_Expression_TableConstructor", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def iot2_Field(self):
        return self.__iot2_Field

    @iot2_Field.setter
    def iot2_Field(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Field__iot2_Field", None)
        self.__iot2_Field = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_ExceptionDef32"):
                opp_val = getattr(old_value, "iot2_ExceptionDef32", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_ExceptionDef32"):
                opp_val = getattr(value, "iot2_ExceptionDef32", None)
                if opp_val is None:
                    setattr(value, "iot2_ExceptionDef32", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def execute(self, iot2_c):
        # TODO: Implement execute method
        pass

class Contained:

    pass
class iot2_OperationDef(Contained, Typed):

    def __init__(self, isOneway: bool, contexts: str, iot2_OperationDef: "iot2_HWComponent" = None, iot2_OperationDef21: set["iot2_ParameterDef"] = None, iot2_OperationDef23: set["iot2_ExceptionDef"] = None, iot2_OperationDef25: "iot2_Block" = None, iot2_OperationDef231: "iot2_OpaqueAction" = None):
        self.isOneway = isOneway
        self.contexts = contexts
        self.iot2_OperationDef = iot2_OperationDef
        self.iot2_OperationDef21 = iot2_OperationDef21 if iot2_OperationDef21 is not None else set()
        self.iot2_OperationDef23 = iot2_OperationDef23 if iot2_OperationDef23 is not None else set()
        self.iot2_OperationDef25 = iot2_OperationDef25
        self.iot2_OperationDef231 = iot2_OperationDef231
        
        pass
    @property
    def contexts(self):
        return self.__contexts

    @contexts.setter
    def contexts(self, contexts: str):
        self.__contexts = contexts


    @property
    def isOneway(self):
        return self.__isOneway

    @isOneway.setter
    def isOneway(self, isOneway: bool):
        self.__isOneway = isOneway


    @property
    def iot2_OperationDef21(self):
        return self.__iot2_OperationDef21

    @iot2_OperationDef21.setter
    def iot2_OperationDef21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_OperationDef__iot2_OperationDef21", None)
        self.__iot2_OperationDef21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iot2_ParameterDef"):
                    opp_val = getattr(item, "iot2_ParameterDef", None)
                    
                    if opp_val == self:
                        setattr(item, "iot2_ParameterDef", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iot2_ParameterDef"):
                    opp_val = getattr(item, "iot2_ParameterDef", None)
                    
                    setattr(item, "iot2_ParameterDef", self)
                    

    @property
    def iot2_OperationDef25(self):
        return self.__iot2_OperationDef25

    @iot2_OperationDef25.setter
    def iot2_OperationDef25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_OperationDef__iot2_OperationDef25", None)
        self.__iot2_OperationDef25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Block"):
                opp_val = getattr(old_value, "iot2_Block", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Block", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Block"):
                opp_val = getattr(value, "iot2_Block", None)
                setattr(value, "iot2_Block", self)

    @property
    def iot2_OperationDef(self):
        return self.__iot2_OperationDef

    @iot2_OperationDef.setter
    def iot2_OperationDef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_OperationDef__iot2_OperationDef", None)
        self.__iot2_OperationDef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_HWComponent11"):
                opp_val = getattr(old_value, "iot2_HWComponent11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_HWComponent11"):
                opp_val = getattr(value, "iot2_HWComponent11", None)
                if opp_val is None:
                    setattr(value, "iot2_HWComponent11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def iot2_OperationDef231(self):
        return self.__iot2_OperationDef231

    @iot2_OperationDef231.setter
    def iot2_OperationDef231(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_OperationDef__iot2_OperationDef231", None)
        self.__iot2_OperationDef231 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_OpaqueAction230"):
                opp_val = getattr(old_value, "iot2_OpaqueAction230", None)
                if opp_val == self:
                    setattr(old_value, "iot2_OpaqueAction230", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_OpaqueAction230"):
                opp_val = getattr(value, "iot2_OpaqueAction230", None)
                setattr(value, "iot2_OpaqueAction230", self)

    @property
    def iot2_OperationDef23(self):
        return self.__iot2_OperationDef23

    @iot2_OperationDef23.setter
    def iot2_OperationDef23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_OperationDef__iot2_OperationDef23", None)
        self.__iot2_OperationDef23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iot2_ExceptionDef"):
                    opp_val = getattr(item, "iot2_ExceptionDef", None)
                    
                    if opp_val == self:
                        setattr(item, "iot2_ExceptionDef", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iot2_ExceptionDef"):
                    opp_val = getattr(item, "iot2_ExceptionDef", None)
                    
                    setattr(item, "iot2_ExceptionDef", self)
                    

    def execute(self, iot2_c):
        # TODO: Implement execute method
        pass

class iot2_TypedefDef(IDLType, Contained):

    pass
class iot2_Container(Contained):

    pass
class iot2_ExceptionDef(Contained):

    def __init__(self, typeCode: str, iot2_ExceptionDef: "iot2_OperationDef" = None, iot2_ExceptionDef32: set["iot2_Field"] = None):
        self.typeCode = typeCode
        self.iot2_ExceptionDef = iot2_ExceptionDef
        self.iot2_ExceptionDef32 = iot2_ExceptionDef32 if iot2_ExceptionDef32 is not None else set()
        
        pass
    @property
    def typeCode(self):
        return self.__typeCode

    @typeCode.setter
    def typeCode(self, typeCode: str):
        self.__typeCode = typeCode


    @property
    def iot2_ExceptionDef(self):
        return self.__iot2_ExceptionDef

    @iot2_ExceptionDef.setter
    def iot2_ExceptionDef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_ExceptionDef__iot2_ExceptionDef", None)
        self.__iot2_ExceptionDef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_OperationDef23"):
                opp_val = getattr(old_value, "iot2_OperationDef23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_OperationDef23"):
                opp_val = getattr(value, "iot2_OperationDef23", None)
                if opp_val is None:
                    setattr(value, "iot2_OperationDef23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def iot2_ExceptionDef32(self):
        return self.__iot2_ExceptionDef32

    @iot2_ExceptionDef32.setter
    def iot2_ExceptionDef32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_ExceptionDef__iot2_ExceptionDef32", None)
        self.__iot2_ExceptionDef32 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iot2_Field"):
                    opp_val = getattr(item, "iot2_Field", None)
                    
                    if opp_val == self:
                        setattr(item, "iot2_Field", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iot2_Field"):
                    opp_val = getattr(item, "iot2_Field", None)
                    
                    setattr(item, "iot2_Field", self)
                    

class iot2_Variable:

    def __init__(self, name: str, iot2_Variable: "iot2_Activity" = None, iot2_Variable19: "iot2_Activity" = None, iot2_Variable233: "iot2_Value" = None, iot2_Variable235: "iot2_Value" = None, iot2_Variable258: "iot2_InputValue" = None):
        self.name = name
        self.iot2_Variable = iot2_Variable
        self.iot2_Variable19 = iot2_Variable19
        self.iot2_Variable233 = iot2_Variable233
        self.iot2_Variable235 = iot2_Variable235
        self.iot2_Variable258 = iot2_Variable258
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def iot2_Variable(self):
        return self.__iot2_Variable

    @iot2_Variable.setter
    def iot2_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Variable__iot2_Variable", None)
        self.__iot2_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Activity16"):
                opp_val = getattr(old_value, "iot2_Activity16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Activity16"):
                opp_val = getattr(value, "iot2_Activity16", None)
                if opp_val is None:
                    setattr(value, "iot2_Activity16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def iot2_Variable19(self):
        return self.__iot2_Variable19

    @iot2_Variable19.setter
    def iot2_Variable19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Variable__iot2_Variable19", None)
        self.__iot2_Variable19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Activity18"):
                opp_val = getattr(old_value, "iot2_Activity18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Activity18"):
                opp_val = getattr(value, "iot2_Activity18", None)
                if opp_val is None:
                    setattr(value, "iot2_Activity18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def iot2_Variable258(self):
        return self.__iot2_Variable258

    @iot2_Variable258.setter
    def iot2_Variable258(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Variable__iot2_Variable258", None)
        self.__iot2_Variable258 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_InputValue257"):
                opp_val = getattr(old_value, "iot2_InputValue257", None)
                if opp_val == self:
                    setattr(old_value, "iot2_InputValue257", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_InputValue257"):
                opp_val = getattr(value, "iot2_InputValue257", None)
                setattr(value, "iot2_InputValue257", self)

    @property
    def iot2_Variable235(self):
        return self.__iot2_Variable235

    @iot2_Variable235.setter
    def iot2_Variable235(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Variable__iot2_Variable235", None)
        self.__iot2_Variable235 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Value236"):
                opp_val = getattr(old_value, "iot2_Value236", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Value236", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Value236"):
                opp_val = getattr(value, "iot2_Value236", None)
                setattr(value, "iot2_Value236", self)

    @property
    def iot2_Variable233(self):
        return self.__iot2_Variable233

    @iot2_Variable233.setter
    def iot2_Variable233(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Variable__iot2_Variable233", None)
        self.__iot2_Variable233 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Value"):
                opp_val = getattr(old_value, "iot2_Value", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Value", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Value"):
                opp_val = getattr(value, "iot2_Value", None)
                setattr(value, "iot2_Value", self)

    def init(self, iot2_c):
        # TODO: Implement init method
        pass

    def execute(self, iot2_c):
        # TODO: Implement execute method
        pass

    def print(self):
        # TODO: Implement print method
        pass

class iot2_ActivityEdge(NamedElement):

    def __init__(self, iot2_ActivityEdge: "iot2_Activity" = None, outgoing: "iot2_ActivityNode" = None, incoming: "iot2_ActivityNode" = None, iot2_ActivityEdge225: set["iot2_Offer"] = None, ActivityEdge: "iot2_ActivityNode" = None, ActivityEdge218: "iot2_ActivityNode" = None):
        self.iot2_ActivityEdge = iot2_ActivityEdge
        self.outgoing = outgoing
        self.incoming = incoming
        self.iot2_ActivityEdge225 = iot2_ActivityEdge225 if iot2_ActivityEdge225 is not None else set()
        self.ActivityEdge = ActivityEdge
        self.ActivityEdge218 = ActivityEdge218
        
        pass
    @property
    def incoming(self):
        return self.__incoming

    @incoming.setter
    def incoming(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_ActivityEdge__incoming", None)
        self.__incoming = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ActivityNode223"):
                opp_val = getattr(old_value, "ActivityNode223", None)
                if opp_val == self:
                    setattr(old_value, "ActivityNode223", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ActivityNode223"):
                opp_val = getattr(value, "ActivityNode223", None)
                setattr(value, "ActivityNode223", self)

    @property
    def ActivityEdge(self):
        return self.__ActivityEdge

    @ActivityEdge.setter
    def ActivityEdge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_ActivityEdge__ActivityEdge", None)
        self.__ActivityEdge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "source"):
                opp_val = getattr(old_value, "source", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "source"):
                opp_val = getattr(value, "source", None)
                if opp_val is None:
                    setattr(value, "source", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def outgoing(self):
        return self.__outgoing

    @outgoing.setter
    def outgoing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_ActivityEdge__outgoing", None)
        self.__outgoing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ActivityNode221"):
                opp_val = getattr(old_value, "ActivityNode221", None)
                if opp_val == self:
                    setattr(old_value, "ActivityNode221", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ActivityNode221"):
                opp_val = getattr(value, "ActivityNode221", None)
                setattr(value, "ActivityNode221", self)

    @property
    def iot2_ActivityEdge225(self):
        return self.__iot2_ActivityEdge225

    @iot2_ActivityEdge225.setter
    def iot2_ActivityEdge225(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_ActivityEdge__iot2_ActivityEdge225", None)
        self.__iot2_ActivityEdge225 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iot2_Offer"):
                    opp_val = getattr(item, "iot2_Offer", None)
                    
                    if opp_val == self:
                        setattr(item, "iot2_Offer", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iot2_Offer"):
                    opp_val = getattr(item, "iot2_Offer", None)
                    
                    setattr(item, "iot2_Offer", self)
                    

    @property
    def iot2_ActivityEdge(self):
        return self.__iot2_ActivityEdge

    @iot2_ActivityEdge.setter
    def iot2_ActivityEdge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_ActivityEdge__iot2_ActivityEdge", None)
        self.__iot2_ActivityEdge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Activity14"):
                opp_val = getattr(old_value, "iot2_Activity14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Activity14"):
                opp_val = getattr(value, "iot2_Activity14", None)
                if opp_val is None:
                    setattr(value, "iot2_Activity14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ActivityEdge218(self):
        return self.__ActivityEdge218

    @ActivityEdge218.setter
    def ActivityEdge218(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_ActivityEdge__ActivityEdge218", None)
        self.__ActivityEdge218 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "target"):
                opp_val = getattr(old_value, "target", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "target"):
                opp_val = getattr(value, "target", None)
                if opp_val is None:
                    setattr(value, "target", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def sendOffer(self, iot2_tokens):
        # TODO: Implement sendOffer method
        pass

    def takeOfferedTokens(self) :
        # TODO: Implement takeOfferedTokens method
        pass

    def hasOffer(self):
        # TODO: Implement hasOffer method
        pass

class iot2_ActivityNode(NamedElement):

    def __init__(self, running: str, ActivityNode: "iot2_Activity" = None, iot2_ActivityNode: "iot2_Token" = None, ActivityNode221: "iot2_ActivityEdge" = None, ActivityNode223: "iot2_ActivityEdge" = None, source: set["iot2_ActivityEdge"] = None, target: set["iot2_ActivityEdge"] = None, nodes: "iot2_Activity" = None, iot2_ActivityNode279: "iot2_Trace" = None):
        self.running = running
        self.ActivityNode = ActivityNode
        self.iot2_ActivityNode = iot2_ActivityNode
        self.ActivityNode221 = ActivityNode221
        self.ActivityNode223 = ActivityNode223
        self.source = source if source is not None else set()
        self.target = target if target is not None else set()
        self.nodes = nodes
        self.iot2_ActivityNode279 = iot2_ActivityNode279
        
        pass
    @property
    def running(self):
        return self.__running

    @running.setter
    def running(self, running: str):
        self.__running = running


    @property
    def nodes(self):
        return self.__nodes

    @nodes.setter
    def nodes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_ActivityNode__nodes", None)
        self.__nodes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Activity"):
                opp_val = getattr(old_value, "Activity", None)
                if opp_val == self:
                    setattr(old_value, "Activity", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Activity"):
                opp_val = getattr(value, "Activity", None)
                setattr(value, "Activity", self)

    @property
    def ActivityNode(self):
        return self.__ActivityNode

    @ActivityNode.setter
    def ActivityNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_ActivityNode__ActivityNode", None)
        self.__ActivityNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "activity"):
                opp_val = getattr(old_value, "activity", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "activity"):
                opp_val = getattr(value, "activity", None)
                if opp_val is None:
                    setattr(value, "activity", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def iot2_ActivityNode(self):
        return self.__iot2_ActivityNode

    @iot2_ActivityNode.setter
    def iot2_ActivityNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_ActivityNode__iot2_ActivityNode", None)
        self.__iot2_ActivityNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Token264"):
                opp_val = getattr(old_value, "iot2_Token264", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Token264", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Token264"):
                opp_val = getattr(value, "iot2_Token264", None)
                setattr(value, "iot2_Token264", self)

    @property
    def ActivityNode221(self):
        return self.__ActivityNode221

    @ActivityNode221.setter
    def ActivityNode221(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_ActivityNode__ActivityNode221", None)
        self.__ActivityNode221 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outgoing"):
                opp_val = getattr(old_value, "outgoing", None)
                if opp_val == self:
                    setattr(old_value, "outgoing", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outgoing"):
                opp_val = getattr(value, "outgoing", None)
                setattr(value, "outgoing", self)

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_ActivityNode__target", None)
        self.__target = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActivityEdge218"):
                    opp_val = getattr(item, "ActivityEdge218", None)
                    
                    if opp_val == self:
                        setattr(item, "ActivityEdge218", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActivityEdge218"):
                    opp_val = getattr(item, "ActivityEdge218", None)
                    
                    setattr(item, "ActivityEdge218", self)
                    

    @property
    def ActivityNode223(self):
        return self.__ActivityNode223

    @ActivityNode223.setter
    def ActivityNode223(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_ActivityNode__ActivityNode223", None)
        self.__ActivityNode223 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "incoming"):
                opp_val = getattr(old_value, "incoming", None)
                if opp_val == self:
                    setattr(old_value, "incoming", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "incoming"):
                opp_val = getattr(value, "incoming", None)
                setattr(value, "incoming", self)

    @property
    def iot2_ActivityNode279(self):
        return self.__iot2_ActivityNode279

    @iot2_ActivityNode279.setter
    def iot2_ActivityNode279(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_ActivityNode__iot2_ActivityNode279", None)
        self.__iot2_ActivityNode279 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Trace278"):
                opp_val = getattr(old_value, "iot2_Trace278", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Trace278"):
                opp_val = getattr(value, "iot2_Trace278", None)
                if opp_val is None:
                    setattr(value, "iot2_Trace278", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_ActivityNode__source", None)
        self.__source = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ActivityEdge"):
                    opp_val = getattr(item, "ActivityEdge", None)
                    
                    if opp_val == self:
                        setattr(item, "ActivityEdge", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ActivityEdge"):
                    opp_val = getattr(item, "ActivityEdge", None)
                    
                    setattr(item, "ActivityEdge", self)
                    

    def execute(self, iot2_c):
        # TODO: Implement execute method
        pass

    def takeOfferdTokens(self) :
        # TODO: Implement takeOfferdTokens method
        pass

    def removeToken(self, iot2_token):
        # TODO: Implement removeToken method
        pass

    def sendOffers(self, iot2_tokens):
        # TODO: Implement sendOffers method
        pass

    def terminate(self):
        # TODO: Implement terminate method
        pass

    def isReady(self):
        # TODO: Implement isReady method
        pass

    def hasOffers(self):
        # TODO: Implement hasOffers method
        pass

    def addTokens(self, iot2_tokens):
        # TODO: Implement addTokens method
        pass

class iot2_Sketch:

    pass
class iot2_Board:

    def __init__(self, name: str, type: str, iot2_Board: "iot2_System" = None, iot2_Board6: set["iot2_HWComponent"] = None):
        self.name = name
        self.type = type
        self.iot2_Board = iot2_Board
        self.iot2_Board6 = iot2_Board6 if iot2_Board6 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def iot2_Board6(self):
        return self.__iot2_Board6

    @iot2_Board6.setter
    def iot2_Board6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Board__iot2_Board6", None)
        self.__iot2_Board6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iot2_HWComponent7"):
                    opp_val = getattr(item, "iot2_HWComponent7", None)
                    
                    if opp_val == self:
                        setattr(item, "iot2_HWComponent7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iot2_HWComponent7"):
                    opp_val = getattr(item, "iot2_HWComponent7", None)
                    
                    setattr(item, "iot2_HWComponent7", self)
                    

    @property
    def iot2_Board(self):
        return self.__iot2_Board

    @iot2_Board.setter
    def iot2_Board(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Board__iot2_Board", None)
        self.__iot2_Board = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_System2"):
                opp_val = getattr(old_value, "iot2_System2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_System2"):
                opp_val = getattr(value, "iot2_System2", None)
                if opp_val is None:
                    setattr(value, "iot2_System2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class iot2_HWComponent(ABC):

    def __init__(self, name: bool, iot2_HWComponent: "iot2_System" = None, iot2_HWComponent7: "iot2_Board" = None, iot2_HWComponent11: set["iot2_OperationDef"] = None):
        self.name = name
        self.iot2_HWComponent = iot2_HWComponent
        self.iot2_HWComponent7 = iot2_HWComponent7
        self.iot2_HWComponent11 = iot2_HWComponent11 if iot2_HWComponent11 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: bool):
        self.__name = name


    @property
    def iot2_HWComponent(self):
        return self.__iot2_HWComponent

    @iot2_HWComponent.setter
    def iot2_HWComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_HWComponent__iot2_HWComponent", None)
        self.__iot2_HWComponent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_System"):
                opp_val = getattr(old_value, "iot2_System", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_System"):
                opp_val = getattr(value, "iot2_System", None)
                if opp_val is None:
                    setattr(value, "iot2_System", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def iot2_HWComponent7(self):
        return self.__iot2_HWComponent7

    @iot2_HWComponent7.setter
    def iot2_HWComponent7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_HWComponent__iot2_HWComponent7", None)
        self.__iot2_HWComponent7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Board6"):
                opp_val = getattr(old_value, "iot2_Board6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Board6"):
                opp_val = getattr(value, "iot2_Board6", None)
                if opp_val is None:
                    setattr(value, "iot2_Board6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def iot2_HWComponent11(self):
        return self.__iot2_HWComponent11

    @iot2_HWComponent11.setter
    def iot2_HWComponent11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_HWComponent__iot2_HWComponent11", None)
        self.__iot2_HWComponent11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iot2_OperationDef"):
                    opp_val = getattr(item, "iot2_OperationDef", None)
                    
                    if opp_val == self:
                        setattr(item, "iot2_OperationDef", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iot2_OperationDef"):
                    opp_val = getattr(item, "iot2_OperationDef", None)
                    
                    setattr(item, "iot2_OperationDef", self)
                    

class iot2_System:

    def __init__(self, name: str, iot2_System: set["iot2_HWComponent"] = None, iot2_System2: set["iot2_Board"] = None, iot2_System4: "iot2_Sketch" = None):
        self.name = name
        self.iot2_System = iot2_System if iot2_System is not None else set()
        self.iot2_System2 = iot2_System2 if iot2_System2 is not None else set()
        self.iot2_System4 = iot2_System4
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def iot2_System2(self):
        return self.__iot2_System2

    @iot2_System2.setter
    def iot2_System2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_System__iot2_System2", None)
        self.__iot2_System2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iot2_Board"):
                    opp_val = getattr(item, "iot2_Board", None)
                    
                    if opp_val == self:
                        setattr(item, "iot2_Board", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iot2_Board"):
                    opp_val = getattr(item, "iot2_Board", None)
                    
                    setattr(item, "iot2_Board", self)
                    

    @property
    def iot2_System4(self):
        return self.__iot2_System4

    @iot2_System4.setter
    def iot2_System4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_System__iot2_System4", None)
        self.__iot2_System4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Sketch"):
                opp_val = getattr(old_value, "iot2_Sketch", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Sketch", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Sketch"):
                opp_val = getattr(value, "iot2_Sketch", None)
                setattr(value, "iot2_Sketch", self)

    @property
    def iot2_System(self):
        return self.__iot2_System

    @iot2_System.setter
    def iot2_System(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_System__iot2_System", None)
        self.__iot2_System = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iot2_HWComponent"):
                    opp_val = getattr(item, "iot2_HWComponent", None)
                    
                    if opp_val == self:
                        setattr(item, "iot2_HWComponent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iot2_HWComponent"):
                    opp_val = getattr(item, "iot2_HWComponent", None)
                    
                    setattr(item, "iot2_HWComponent", self)
                    

class iot2_Trace:

    pass
class iot2_Context:

    pass
class iot2_Token:

    def __init__(self, iot2_Token: "iot2_Offer" = None, iot2_Token264: "iot2_ActivityNode" = None, iot2_Token281: "iot2_ForkedToken" = None):
        self.iot2_Token = iot2_Token
        self.iot2_Token264 = iot2_Token264
        self.iot2_Token281 = iot2_Token281
        
        pass
    @property
    def iot2_Token281(self):
        return self.__iot2_Token281

    @iot2_Token281.setter
    def iot2_Token281(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Token__iot2_Token281", None)
        self.__iot2_Token281 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_ForkedToken"):
                opp_val = getattr(old_value, "iot2_ForkedToken", None)
                if opp_val == self:
                    setattr(old_value, "iot2_ForkedToken", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_ForkedToken"):
                opp_val = getattr(value, "iot2_ForkedToken", None)
                setattr(value, "iot2_ForkedToken", self)

    @property
    def iot2_Token264(self):
        return self.__iot2_Token264

    @iot2_Token264.setter
    def iot2_Token264(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Token__iot2_Token264", None)
        self.__iot2_Token264 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_ActivityNode"):
                opp_val = getattr(old_value, "iot2_ActivityNode", None)
                if opp_val == self:
                    setattr(old_value, "iot2_ActivityNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_ActivityNode"):
                opp_val = getattr(value, "iot2_ActivityNode", None)
                setattr(value, "iot2_ActivityNode", self)

    @property
    def iot2_Token(self):
        return self.__iot2_Token

    @iot2_Token.setter
    def iot2_Token(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Token__iot2_Token", None)
        self.__iot2_Token = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Offer262"):
                opp_val = getattr(old_value, "iot2_Offer262", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Offer262"):
                opp_val = getattr(value, "iot2_Offer262", None)
                if opp_val is None:
                    setattr(value, "iot2_Offer262", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def isWithdrawn(self):
        # TODO: Implement isWithdrawn method
        pass

    def withdraw(self):
        # TODO: Implement withdraw method
        pass

    def transfer(self, iot2_holder) :
        # TODO: Implement transfer method
        pass

class iot2_Input:

    pass
class Token:

    pass
class iot2_ControlToken(Token):

    pass
class iot2_ForkedToken(Token):

    def __init__(self, remainingOffersCount: str, iot2_ForkedToken: "iot2_Token" = None):
        self.remainingOffersCount = remainingOffersCount
        self.iot2_ForkedToken = iot2_ForkedToken
        
        pass
    @property
    def remainingOffersCount(self):
        return self.__remainingOffersCount

    @remainingOffersCount.setter
    def remainingOffersCount(self, remainingOffersCount: str):
        self.__remainingOffersCount = remainingOffersCount


    @property
    def iot2_ForkedToken(self):
        return self.__iot2_ForkedToken

    @iot2_ForkedToken.setter
    def iot2_ForkedToken(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_ForkedToken__iot2_ForkedToken", None)
        self.__iot2_ForkedToken = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Token281"):
                opp_val = getattr(old_value, "iot2_Token281", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Token281", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Token281"):
                opp_val = getattr(value, "iot2_Token281", None)
                setattr(value, "iot2_Token281", self)

class BooleanExpression:

    pass
class iot2_BooleanUnaryExpression(BooleanExpression):

    def __init__(self, operator: str, iot2_BooleanUnaryExpression: "iot2_BooleanVariable" = None):
        self.operator = operator
        self.iot2_BooleanUnaryExpression = iot2_BooleanUnaryExpression
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


    @property
    def iot2_BooleanUnaryExpression(self):
        return self.__iot2_BooleanUnaryExpression

    @iot2_BooleanUnaryExpression.setter
    def iot2_BooleanUnaryExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_BooleanUnaryExpression__iot2_BooleanUnaryExpression", None)
        self.__iot2_BooleanUnaryExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_BooleanVariable248"):
                opp_val = getattr(old_value, "iot2_BooleanVariable248", None)
                if opp_val == self:
                    setattr(old_value, "iot2_BooleanVariable248", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_BooleanVariable248"):
                opp_val = getattr(value, "iot2_BooleanVariable248", None)
                setattr(value, "iot2_BooleanVariable248", self)

    def execute(self, iot2_c):
        # TODO: Implement execute method
        pass

class IntegerExpression:

    pass
class iot2_IntegerComparisonExpression(IntegerExpression):

    def __init__(self, operator: str, iot2_IntegerComparisonExpression: "iot2_BooleanVariable" = None):
        self.operator = operator
        self.iot2_IntegerComparisonExpression = iot2_IntegerComparisonExpression
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


    @property
    def iot2_IntegerComparisonExpression(self):
        return self.__iot2_IntegerComparisonExpression

    @iot2_IntegerComparisonExpression.setter
    def iot2_IntegerComparisonExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_IntegerComparisonExpression__iot2_IntegerComparisonExpression", None)
        self.__iot2_IntegerComparisonExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_BooleanVariable246"):
                opp_val = getattr(old_value, "iot2_BooleanVariable246", None)
                if opp_val == self:
                    setattr(old_value, "iot2_BooleanVariable246", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_BooleanVariable246"):
                opp_val = getattr(value, "iot2_BooleanVariable246", None)
                setattr(value, "iot2_BooleanVariable246", self)

    def execute(self, iot2_c):
        # TODO: Implement execute method
        pass

class iot2_IntegerCalculationExpression(IntegerExpression):

    def __init__(self, operator: str, iot2_IntegerCalculationExpression: "iot2_IntegerVariable" = None):
        self.operator = operator
        self.iot2_IntegerCalculationExpression = iot2_IntegerCalculationExpression
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


    @property
    def iot2_IntegerCalculationExpression(self):
        return self.__iot2_IntegerCalculationExpression

    @iot2_IntegerCalculationExpression.setter
    def iot2_IntegerCalculationExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_IntegerCalculationExpression__iot2_IntegerCalculationExpression", None)
        self.__iot2_IntegerCalculationExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_IntegerVariable244"):
                opp_val = getattr(old_value, "iot2_IntegerVariable244", None)
                if opp_val == self:
                    setattr(old_value, "iot2_IntegerVariable244", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_IntegerVariable244"):
                opp_val = getattr(value, "iot2_IntegerVariable244", None)
                setattr(value, "iot2_IntegerVariable244", self)

    def execute(self, iot2_c):
        # TODO: Implement execute method
        pass

class iot2_InputValue:

    pass
class iot2_BooleanBinaryExpression(BooleanExpression):

    def __init__(self, operator: bool, iot2_BooleanBinaryExpression: "iot2_BooleanVariable" = None, iot2_BooleanBinaryExpression252: "iot2_BooleanVariable" = None):
        self.operator = operator
        self.iot2_BooleanBinaryExpression = iot2_BooleanBinaryExpression
        self.iot2_BooleanBinaryExpression252 = iot2_BooleanBinaryExpression252
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: bool):
        self.__operator = operator


    @property
    def iot2_BooleanBinaryExpression252(self):
        return self.__iot2_BooleanBinaryExpression252

    @iot2_BooleanBinaryExpression252.setter
    def iot2_BooleanBinaryExpression252(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_BooleanBinaryExpression__iot2_BooleanBinaryExpression252", None)
        self.__iot2_BooleanBinaryExpression252 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_BooleanVariable253"):
                opp_val = getattr(old_value, "iot2_BooleanVariable253", None)
                if opp_val == self:
                    setattr(old_value, "iot2_BooleanVariable253", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_BooleanVariable253"):
                opp_val = getattr(value, "iot2_BooleanVariable253", None)
                setattr(value, "iot2_BooleanVariable253", self)

    @property
    def iot2_BooleanBinaryExpression(self):
        return self.__iot2_BooleanBinaryExpression

    @iot2_BooleanBinaryExpression.setter
    def iot2_BooleanBinaryExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_BooleanBinaryExpression__iot2_BooleanBinaryExpression", None)
        self.__iot2_BooleanBinaryExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_BooleanVariable250"):
                opp_val = getattr(old_value, "iot2_BooleanVariable250", None)
                if opp_val == self:
                    setattr(old_value, "iot2_BooleanVariable250", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_BooleanVariable250"):
                opp_val = getattr(value, "iot2_BooleanVariable250", None)
                setattr(value, "iot2_BooleanVariable250", self)

    def execute(self, iot2_c):
        # TODO: Implement execute method
        pass

class Variable:

    pass
class iot2_IntegerVariable(Variable):

    def __init__(self, iot2_IntegerVariable: "iot2_IntegerExpression" = None, iot2_IntegerVariable240: "iot2_IntegerExpression" = None, iot2_IntegerVariable244: "iot2_IntegerCalculationExpression" = None):
        self.iot2_IntegerVariable = iot2_IntegerVariable
        self.iot2_IntegerVariable240 = iot2_IntegerVariable240
        self.iot2_IntegerVariable244 = iot2_IntegerVariable244
        
        pass
    @property
    def iot2_IntegerVariable244(self):
        return self.__iot2_IntegerVariable244

    @iot2_IntegerVariable244.setter
    def iot2_IntegerVariable244(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_IntegerVariable__iot2_IntegerVariable244", None)
        self.__iot2_IntegerVariable244 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_IntegerCalculationExpression"):
                opp_val = getattr(old_value, "iot2_IntegerCalculationExpression", None)
                if opp_val == self:
                    setattr(old_value, "iot2_IntegerCalculationExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_IntegerCalculationExpression"):
                opp_val = getattr(value, "iot2_IntegerCalculationExpression", None)
                setattr(value, "iot2_IntegerCalculationExpression", self)

    @property
    def iot2_IntegerVariable(self):
        return self.__iot2_IntegerVariable

    @iot2_IntegerVariable.setter
    def iot2_IntegerVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_IntegerVariable__iot2_IntegerVariable", None)
        self.__iot2_IntegerVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_IntegerExpression"):
                opp_val = getattr(old_value, "iot2_IntegerExpression", None)
                if opp_val == self:
                    setattr(old_value, "iot2_IntegerExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_IntegerExpression"):
                opp_val = getattr(value, "iot2_IntegerExpression", None)
                setattr(value, "iot2_IntegerExpression", self)

    @property
    def iot2_IntegerVariable240(self):
        return self.__iot2_IntegerVariable240

    @iot2_IntegerVariable240.setter
    def iot2_IntegerVariable240(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_IntegerVariable__iot2_IntegerVariable240", None)
        self.__iot2_IntegerVariable240 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_IntegerExpression239"):
                opp_val = getattr(old_value, "iot2_IntegerExpression239", None)
                if opp_val == self:
                    setattr(old_value, "iot2_IntegerExpression239", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_IntegerExpression239"):
                opp_val = getattr(value, "iot2_IntegerExpression239", None)
                setattr(value, "iot2_IntegerExpression239", self)

    def execute(self, iot2_c):
        # TODO: Implement execute method
        pass

    def print(self):
        # TODO: Implement print method
        pass

class iot2_Value:

    pass
class iot2_BooleanExpression(Expression):

    pass
class iot2_IntegerExpression(Expression):

    pass
class Value:

    pass
class iot2_IntegerValue(Value):

    def __init__(self, value: int):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value


class iot2_BooleanValue(Value):

    def __init__(self, value: bool):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value


class ControlNode:

    pass
class iot2_FinalNode(ControlNode):

    pass
class iot2_InitialNode(ControlNode):

    def __init__(self):
        
        pass
    def hasOffers(self):
        # TODO: Implement hasOffers method
        pass

    def execute(self, iot2_c):
        # TODO: Implement execute method
        pass

class Action:

    pass
class iot2_OpaqueAction(Action):

    def __init__(self, iot2_OpaqueAction: set["iot2_Expression"] = None, iot2_OpaqueAction230: "iot2_OperationDef" = None):
        self.iot2_OpaqueAction = iot2_OpaqueAction if iot2_OpaqueAction is not None else set()
        self.iot2_OpaqueAction230 = iot2_OpaqueAction230
        
        pass
    @property
    def iot2_OpaqueAction230(self):
        return self.__iot2_OpaqueAction230

    @iot2_OpaqueAction230.setter
    def iot2_OpaqueAction230(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_OpaqueAction__iot2_OpaqueAction230", None)
        self.__iot2_OpaqueAction230 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_OperationDef231"):
                opp_val = getattr(old_value, "iot2_OperationDef231", None)
                if opp_val == self:
                    setattr(old_value, "iot2_OperationDef231", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_OperationDef231"):
                opp_val = getattr(value, "iot2_OperationDef231", None)
                setattr(value, "iot2_OperationDef231", self)

    @property
    def iot2_OpaqueAction(self):
        return self.__iot2_OpaqueAction

    @iot2_OpaqueAction.setter
    def iot2_OpaqueAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_OpaqueAction__iot2_OpaqueAction", None)
        self.__iot2_OpaqueAction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iot2_Expression228"):
                    opp_val = getattr(item, "iot2_Expression228", None)
                    
                    if opp_val == self:
                        setattr(item, "iot2_Expression228", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iot2_Expression228"):
                    opp_val = getattr(item, "iot2_Expression228", None)
                    
                    setattr(item, "iot2_Expression228", self)
                    

    def execute(self, iot2_c):
        # TODO: Implement execute method
        pass

    def getValueAsString(self, iot2_v):
        # TODO: Implement getValueAsString method
        pass

class ExecutableNode:

    pass
class iot2_Action(ExecutableNode):

    pass
class ActivityNode:

    pass
class iot2_ExecutableNode(ActivityNode):

    pass
class iot2_ControlNode(ActivityNode):

    pass
class iot2_DecisionNode(ControlNode):

    def __init__(self):
        
        pass
    def sendOffers(self, iot2_tokens):
        # TODO: Implement sendOffers method
        pass

    def execute(self, iot2_c):
        # TODO: Implement execute method
        pass

class iot2_MergeNode(ControlNode):

    def __init__(self):
        
        pass
    def execute(self, iot2_c):
        # TODO: Implement execute method
        pass

    def hasOffers(self):
        # TODO: Implement hasOffers method
        pass

class iot2_JoinNode(ControlNode):

    def __init__(self, iot2_JoinNode: "iot2_Context" = None):
        self.iot2_JoinNode = iot2_JoinNode
        
        pass
    @property
    def iot2_JoinNode(self):
        return self.__iot2_JoinNode

    @iot2_JoinNode.setter
    def iot2_JoinNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_JoinNode__iot2_JoinNode", None)
        self.__iot2_JoinNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Context276"):
                opp_val = getattr(old_value, "iot2_Context276", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Context276", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Context276"):
                opp_val = getattr(value, "iot2_Context276", None)
                setattr(value, "iot2_Context276", self)

    def execute(self, iot2_c):
        # TODO: Implement execute method
        pass

class iot2_ForkNode(ControlNode):

    def __init__(self):
        
        pass
    def execute(self, iot2_c):
        # TODO: Implement execute method
        pass

class FinalNode:

    pass
class iot2_ActivityFinalNode(FinalNode):

    def __init__(self):
        
        pass
    def execute(self, iot2_c):
        # TODO: Implement execute method
        pass

class iot2_BooleanVariable(Variable):

    def __init__(self, iot2_BooleanVariable: "iot2_ControlFlow" = None, iot2_BooleanVariable242: "iot2_BooleanExpression" = None, iot2_BooleanVariable248: "iot2_BooleanUnaryExpression" = None, iot2_BooleanVariable250: "iot2_BooleanBinaryExpression" = None, iot2_BooleanVariable253: "iot2_BooleanBinaryExpression" = None, iot2_BooleanVariable246: "iot2_IntegerComparisonExpression" = None):
        self.iot2_BooleanVariable = iot2_BooleanVariable
        self.iot2_BooleanVariable242 = iot2_BooleanVariable242
        self.iot2_BooleanVariable248 = iot2_BooleanVariable248
        self.iot2_BooleanVariable250 = iot2_BooleanVariable250
        self.iot2_BooleanVariable253 = iot2_BooleanVariable253
        self.iot2_BooleanVariable246 = iot2_BooleanVariable246
        
        pass
    @property
    def iot2_BooleanVariable250(self):
        return self.__iot2_BooleanVariable250

    @iot2_BooleanVariable250.setter
    def iot2_BooleanVariable250(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_BooleanVariable__iot2_BooleanVariable250", None)
        self.__iot2_BooleanVariable250 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_BooleanBinaryExpression"):
                opp_val = getattr(old_value, "iot2_BooleanBinaryExpression", None)
                if opp_val == self:
                    setattr(old_value, "iot2_BooleanBinaryExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_BooleanBinaryExpression"):
                opp_val = getattr(value, "iot2_BooleanBinaryExpression", None)
                setattr(value, "iot2_BooleanBinaryExpression", self)

    @property
    def iot2_BooleanVariable253(self):
        return self.__iot2_BooleanVariable253

    @iot2_BooleanVariable253.setter
    def iot2_BooleanVariable253(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_BooleanVariable__iot2_BooleanVariable253", None)
        self.__iot2_BooleanVariable253 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_BooleanBinaryExpression252"):
                opp_val = getattr(old_value, "iot2_BooleanBinaryExpression252", None)
                if opp_val == self:
                    setattr(old_value, "iot2_BooleanBinaryExpression252", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_BooleanBinaryExpression252"):
                opp_val = getattr(value, "iot2_BooleanBinaryExpression252", None)
                setattr(value, "iot2_BooleanBinaryExpression252", self)

    @property
    def iot2_BooleanVariable(self):
        return self.__iot2_BooleanVariable

    @iot2_BooleanVariable.setter
    def iot2_BooleanVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_BooleanVariable__iot2_BooleanVariable", None)
        self.__iot2_BooleanVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_ControlFlow"):
                opp_val = getattr(old_value, "iot2_ControlFlow", None)
                if opp_val == self:
                    setattr(old_value, "iot2_ControlFlow", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_ControlFlow"):
                opp_val = getattr(value, "iot2_ControlFlow", None)
                setattr(value, "iot2_ControlFlow", self)

    @property
    def iot2_BooleanVariable242(self):
        return self.__iot2_BooleanVariable242

    @iot2_BooleanVariable242.setter
    def iot2_BooleanVariable242(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_BooleanVariable__iot2_BooleanVariable242", None)
        self.__iot2_BooleanVariable242 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_BooleanExpression"):
                opp_val = getattr(old_value, "iot2_BooleanExpression", None)
                if opp_val == self:
                    setattr(old_value, "iot2_BooleanExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_BooleanExpression"):
                opp_val = getattr(value, "iot2_BooleanExpression", None)
                setattr(value, "iot2_BooleanExpression", self)

    @property
    def iot2_BooleanVariable248(self):
        return self.__iot2_BooleanVariable248

    @iot2_BooleanVariable248.setter
    def iot2_BooleanVariable248(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_BooleanVariable__iot2_BooleanVariable248", None)
        self.__iot2_BooleanVariable248 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_BooleanUnaryExpression"):
                opp_val = getattr(old_value, "iot2_BooleanUnaryExpression", None)
                if opp_val == self:
                    setattr(old_value, "iot2_BooleanUnaryExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_BooleanUnaryExpression"):
                opp_val = getattr(value, "iot2_BooleanUnaryExpression", None)
                setattr(value, "iot2_BooleanUnaryExpression", self)

    @property
    def iot2_BooleanVariable246(self):
        return self.__iot2_BooleanVariable246

    @iot2_BooleanVariable246.setter
    def iot2_BooleanVariable246(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_BooleanVariable__iot2_BooleanVariable246", None)
        self.__iot2_BooleanVariable246 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_IntegerComparisonExpression"):
                opp_val = getattr(old_value, "iot2_IntegerComparisonExpression", None)
                if opp_val == self:
                    setattr(old_value, "iot2_IntegerComparisonExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_IntegerComparisonExpression"):
                opp_val = getattr(value, "iot2_IntegerComparisonExpression", None)
                setattr(value, "iot2_IntegerComparisonExpression", self)

    def execute(self, iot2_c):
        # TODO: Implement execute method
        pass

    def print(self):
        # TODO: Implement print method
        pass

class ActivityEdge:

    pass
class iot2_ControlFlow(ActivityEdge):

    pass
class iot2_Offer:

    def __init__(self, iot2_Offer262: set["iot2_Token"] = None, iot2_Offer: "iot2_ActivityEdge" = None):
        self.iot2_Offer262 = iot2_Offer262 if iot2_Offer262 is not None else set()
        self.iot2_Offer = iot2_Offer
        
        pass
    @property
    def iot2_Offer(self):
        return self.__iot2_Offer

    @iot2_Offer.setter
    def iot2_Offer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Offer__iot2_Offer", None)
        self.__iot2_Offer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_ActivityEdge225"):
                opp_val = getattr(old_value, "iot2_ActivityEdge225", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_ActivityEdge225"):
                opp_val = getattr(value, "iot2_ActivityEdge225", None)
                if opp_val is None:
                    setattr(value, "iot2_ActivityEdge225", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def iot2_Offer262(self):
        return self.__iot2_Offer262

    @iot2_Offer262.setter
    def iot2_Offer262(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Offer__iot2_Offer262", None)
        self.__iot2_Offer262 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iot2_Token"):
                    opp_val = getattr(item, "iot2_Token", None)
                    
                    if opp_val == self:
                        setattr(item, "iot2_Token", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iot2_Token"):
                    opp_val = getattr(item, "iot2_Token", None)
                    
                    setattr(item, "iot2_Token", self)
                    

    def hasTokens(self):
        # TODO: Implement hasTokens method
        pass

    def removeWithdrawnTokens(self):
        # TODO: Implement removeWithdrawnTokens method
        pass

class iot2_Environment:

    def __init__(self, iot2_Environment: "iot2_Environment" = None, iot2_Environment214: "iot2_Environment" = None):
        self.iot2_Environment = iot2_Environment
        self.iot2_Environment214 = iot2_Environment214
        
        pass
    @property
    def iot2_Environment214(self):
        return self.__iot2_Environment214

    @iot2_Environment214.setter
    def iot2_Environment214(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Environment__iot2_Environment214", None)
        self.__iot2_Environment214 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Environment"):
                opp_val = getattr(old_value, "iot2_Environment", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Environment", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Environment"):
                opp_val = getattr(value, "iot2_Environment", None)
                setattr(value, "iot2_Environment", self)

    @property
    def iot2_Environment(self):
        return self.__iot2_Environment

    @iot2_Environment.setter
    def iot2_Environment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Environment__iot2_Environment", None)
        self.__iot2_Environment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Environment214"):
                opp_val = getattr(old_value, "iot2_Environment214", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Environment214", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Environment214"):
                opp_val = getattr(value, "iot2_Environment214", None)
                setattr(value, "iot2_Environment214", self)

    def putAllFunctions(self, iot2_f):
        # TODO: Implement putAllFunctions method
        pass

    def getVariables(self):
        # TODO: Implement getVariables method
        pass

    def putVariable(self, iot2_o, iot2_s):
        # TODO: Implement putVariable method
        pass

    def getFunctions(self):
        # TODO: Implement getFunctions method
        pass

    def putFunction(self, iot2_s, iot2_f):
        # TODO: Implement putFunction method
        pass

    def getFunction(self, iot2_s) :
        # TODO: Implement getFunction method
        pass

    def getVariable(self, iot2_s) :
        # TODO: Implement getVariable method
        pass

    def pushValue(self, iot2_o):
        # TODO: Implement pushValue method
        pass

    def getValues(self) :
        # TODO: Implement getValues method
        pass

    def putAllVariables(self, iot2_v):
        # TODO: Implement putAllVariables method
        pass

    def popValue(self) :
        # TODO: Implement popValue method
        pass

    def pushAllValues(self, iot2_v):
        # TODO: Implement pushAllValues method
        pass

class iot2_Expression_VariableName(Expression):

    def __init__(self, variable: bool):
        self.variable = variable
        
        pass
    @property
    def variable(self):
        return self.__variable

    @variable.setter
    def variable(self, variable: bool):
        self.__variable = variable


    def execute(self, iot2_c):
        # TODO: Implement execute method
        pass

class iot2_Expression_CallFunction(Expression):

    def __init__(self, iot2_Expression_CallFunction: "iot2_Expression" = None, iot2_Expression_CallFunction205: "iot2_Functioncall_Arguments" = None):
        self.iot2_Expression_CallFunction = iot2_Expression_CallFunction
        self.iot2_Expression_CallFunction205 = iot2_Expression_CallFunction205
        
        pass
    @property
    def iot2_Expression_CallFunction205(self):
        return self.__iot2_Expression_CallFunction205

    @iot2_Expression_CallFunction205.setter
    def iot2_Expression_CallFunction205(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_CallFunction__iot2_Expression_CallFunction205", None)
        self.__iot2_Expression_CallFunction205 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Functioncall_Arguments206"):
                opp_val = getattr(old_value, "iot2_Functioncall_Arguments206", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Functioncall_Arguments206", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Functioncall_Arguments206"):
                opp_val = getattr(value, "iot2_Functioncall_Arguments206", None)
                setattr(value, "iot2_Functioncall_Arguments206", self)

    @property
    def iot2_Expression_CallFunction(self):
        return self.__iot2_Expression_CallFunction

    @iot2_Expression_CallFunction.setter
    def iot2_Expression_CallFunction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_CallFunction__iot2_Expression_CallFunction", None)
        self.__iot2_Expression_CallFunction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression203"):
                opp_val = getattr(old_value, "iot2_Expression203", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression203", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression203"):
                opp_val = getattr(value, "iot2_Expression203", None)
                setattr(value, "iot2_Expression203", self)

    def execute(self, iot2_c):
        # TODO: Implement execute method
        pass

class iot2_Expression_CallMemberFunction(Expression):

    def __init__(self, memberFunctionName: str, iot2_Expression_CallMemberFunction: "iot2_Expression" = None, iot2_Expression_CallMemberFunction200: "iot2_Functioncall_Arguments" = None):
        self.memberFunctionName = memberFunctionName
        self.iot2_Expression_CallMemberFunction = iot2_Expression_CallMemberFunction
        self.iot2_Expression_CallMemberFunction200 = iot2_Expression_CallMemberFunction200
        
        pass
    @property
    def memberFunctionName(self):
        return self.__memberFunctionName

    @memberFunctionName.setter
    def memberFunctionName(self, memberFunctionName: str):
        self.__memberFunctionName = memberFunctionName


    @property
    def iot2_Expression_CallMemberFunction(self):
        return self.__iot2_Expression_CallMemberFunction

    @iot2_Expression_CallMemberFunction.setter
    def iot2_Expression_CallMemberFunction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_CallMemberFunction__iot2_Expression_CallMemberFunction", None)
        self.__iot2_Expression_CallMemberFunction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression198"):
                opp_val = getattr(old_value, "iot2_Expression198", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression198", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression198"):
                opp_val = getattr(value, "iot2_Expression198", None)
                setattr(value, "iot2_Expression198", self)

    @property
    def iot2_Expression_CallMemberFunction200(self):
        return self.__iot2_Expression_CallMemberFunction200

    @iot2_Expression_CallMemberFunction200.setter
    def iot2_Expression_CallMemberFunction200(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_CallMemberFunction__iot2_Expression_CallMemberFunction200", None)
        self.__iot2_Expression_CallMemberFunction200 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Functioncall_Arguments201"):
                opp_val = getattr(old_value, "iot2_Functioncall_Arguments201", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Functioncall_Arguments201", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Functioncall_Arguments201"):
                opp_val = getattr(value, "iot2_Functioncall_Arguments201", None)
                setattr(value, "iot2_Functioncall_Arguments201", self)

    def execute(self, iot2_c):
        # TODO: Implement execute method
        pass

class iot2_Expression_AccessMember(Expression):

    def __init__(self, memberName: str, iot2_Expression_AccessMember: "iot2_Expression" = None):
        self.memberName = memberName
        self.iot2_Expression_AccessMember = iot2_Expression_AccessMember
        
        pass
    @property
    def memberName(self):
        return self.__memberName

    @memberName.setter
    def memberName(self, memberName: str):
        self.__memberName = memberName


    @property
    def iot2_Expression_AccessMember(self):
        return self.__iot2_Expression_AccessMember

    @iot2_Expression_AccessMember.setter
    def iot2_Expression_AccessMember(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_AccessMember__iot2_Expression_AccessMember", None)
        self.__iot2_Expression_AccessMember = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression213"):
                opp_val = getattr(old_value, "iot2_Expression213", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression213", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression213"):
                opp_val = getattr(value, "iot2_Expression213", None)
                setattr(value, "iot2_Expression213", self)

    def execute(self, iot2_c):
        # TODO: Implement execute method
        pass

class iot2_Expression_AccessArray(Expression):

    def __init__(self, iot2_Expression_AccessArray: "iot2_Expression" = None, iot2_Expression_AccessArray210: "iot2_Expression" = None):
        self.iot2_Expression_AccessArray = iot2_Expression_AccessArray
        self.iot2_Expression_AccessArray210 = iot2_Expression_AccessArray210
        
        pass
    @property
    def iot2_Expression_AccessArray210(self):
        return self.__iot2_Expression_AccessArray210

    @iot2_Expression_AccessArray210.setter
    def iot2_Expression_AccessArray210(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_AccessArray__iot2_Expression_AccessArray210", None)
        self.__iot2_Expression_AccessArray210 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression211"):
                opp_val = getattr(old_value, "iot2_Expression211", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression211", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression211"):
                opp_val = getattr(value, "iot2_Expression211", None)
                setattr(value, "iot2_Expression211", self)

    @property
    def iot2_Expression_AccessArray(self):
        return self.__iot2_Expression_AccessArray

    @iot2_Expression_AccessArray.setter
    def iot2_Expression_AccessArray(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_AccessArray__iot2_Expression_AccessArray", None)
        self.__iot2_Expression_AccessArray = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression208"):
                opp_val = getattr(old_value, "iot2_Expression208", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression208", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression208"):
                opp_val = getattr(value, "iot2_Expression208", None)
                setattr(value, "iot2_Expression208", self)

    def execute(self, iot2_c):
        # TODO: Implement execute method
        pass

class iot2_Expression_Length(Expression):

    def __init__(self, iot2_Expression_Length: "iot2_Expression" = None):
        self.iot2_Expression_Length = iot2_Expression_Length
        
        pass
    @property
    def iot2_Expression_Length(self):
        return self.__iot2_Expression_Length

    @iot2_Expression_Length.setter
    def iot2_Expression_Length(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_Length__iot2_Expression_Length", None)
        self.__iot2_Expression_Length = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression189"):
                opp_val = getattr(old_value, "iot2_Expression189", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression189", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression189"):
                opp_val = getattr(value, "iot2_Expression189", None)
                setattr(value, "iot2_Expression189", self)

    def execute(self, iot2_c):
        # TODO: Implement execute method
        pass

class iot2_Expression_Negate(Expression):

    def __init__(self, iot2_Expression_Negate: "iot2_Expression" = None):
        self.iot2_Expression_Negate = iot2_Expression_Negate
        
        pass
    @property
    def iot2_Expression_Negate(self):
        return self.__iot2_Expression_Negate

    @iot2_Expression_Negate.setter
    def iot2_Expression_Negate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot2_Expression_Negate__iot2_Expression_Negate", None)
        self.__iot2_Expression_Negate = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot2_Expression187"):
                opp_val = getattr(old_value, "iot2_Expression187", None)
                if opp_val == self:
                    setattr(old_value, "iot2_Expression187", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot2_Expression187"):
                opp_val = getattr(value, "iot2_Expression187", None)
                setattr(value, "iot2_Expression187", self)

    def execute(self, iot2_c):
        # TODO: Implement execute method
        pass
