from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class DatetimeType:

    pass
class DDL_Time(DatetimeType):

    def __init__(self, precision: int, withTimeZone: bool):
        self.precision = precision
        self.withTimeZone = withTimeZone
        
    @property
    def withTimeZone(self) -> bool:
        return self.__withTimeZone

    @withTimeZone.setter
    def withTimeZone(self, withTimeZone: bool):
        self.__withTimeZone = withTimeZone

    @property
    def precision(self) -> int:
        return self.__precision

    @precision.setter
    def precision(self, precision: int):
        self.__precision = precision

class DDL_TimeStamp(DatetimeType):

    def __init__(self, precision: int, withTimeZone: bool):
        self.precision = precision
        self.withTimeZone = withTimeZone
        
    @property
    def precision(self) -> int:
        return self.__precision

    @precision.setter
    def precision(self, precision: int):
        self.__precision = precision

    @property
    def withTimeZone(self) -> bool:
        return self.__withTimeZone

    @withTimeZone.setter
    def withTimeZone(self, withTimeZone: bool):
        self.__withTimeZone = withTimeZone

class DDL_Date(DatetimeType):

    pass
class ExactNumericType:

    pass
class DDL_Decimal(ExactNumericType):

    def __init__(self, precision: int, scale: int):
        self.precision = precision
        self.scale = scale
        
    @property
    def scale(self) -> int:
        return self.__scale

    @scale.setter
    def scale(self, scale: int):
        self.__scale = scale

    @property
    def precision(self) -> int:
        return self.__precision

    @precision.setter
    def precision(self, precision: int):
        self.__precision = precision

class DDL_Numeric(ExactNumericType):

    def __init__(self, precision: int, scale: int):
        self.precision = precision
        self.scale = scale
        
    @property
    def scale(self) -> int:
        return self.__scale

    @scale.setter
    def scale(self, scale: int):
        self.__scale = scale

    @property
    def precision(self) -> int:
        return self.__precision

    @precision.setter
    def precision(self, precision: int):
        self.__precision = precision

class NumericType:

    pass
class DDL_ExactNumericType(NumericType):

    pass
class BitStringType:

    pass
class DDL_BitVarying(BitStringType):

    pass
class DDL_Bit(BitStringType):

    pass
class ApproximateNumericType:

    pass
class DDL_DoublePrecision(ApproximateNumericType):

    pass
class DDL_Real(ApproximateNumericType):

    pass
class DDL_Float(ApproximateNumericType):

    def __init__(self, precision: int):
        self.precision = precision
        
    @property
    def precision(self) -> int:
        return self.__precision

    @precision.setter
    def precision(self, precision: int):
        self.__precision = precision

class DDL_ApproximateNumericType(NumericType):

    pass
class DDL_Small(ExactNumericType):

    pass
class DDL_Int(ExactNumericType):

    pass
class DDL_Integer(ExactNumericType):

    pass
class DDL_Dec(ExactNumericType):

    def __init__(self, precision: int, scale: int):
        self.precision = precision
        self.scale = scale
        
    @property
    def scale(self) -> int:
        return self.__scale

    @scale.setter
    def scale(self, scale: int):
        self.__scale = scale

    @property
    def precision(self) -> int:
        return self.__precision

    @precision.setter
    def precision(self, precision: int):
        self.__precision = precision

class CharacterStringType:

    pass
class DDL_CharacterVarying(CharacterStringType):

    pass
class DDL_Char(CharacterStringType):

    pass
class DDL_Varchar(CharacterStringType):

    pass
class DDL_CharVarying(CharacterStringType):

    pass
class DDL_Character(CharacterStringType):

    pass
class Type:

    pass
class DDL_DatetimeType(Type):

    pass
class DDL_NumericType(Type):

    pass
class DDL_Interval(Type):

    def __init__(self, field2: str, precision1: int, precision2: int, field1: str):
        self.field2 = field2
        self.precision1 = precision1
        self.precision2 = precision2
        self.field1 = field1
        
    @property
    def field2(self) -> str:
        return self.__field2

    @field2.setter
    def field2(self, field2: str):
        self.__field2 = field2

    @property
    def precision2(self) -> int:
        return self.__precision2

    @precision2.setter
    def precision2(self, precision2: int):
        self.__precision2 = precision2

    @property
    def precision1(self) -> int:
        return self.__precision1

    @precision1.setter
    def precision1(self, precision1: int):
        self.__precision1 = precision1

    @property
    def field1(self) -> str:
        return self.__field1

    @field1.setter
    def field1(self, field1: str):
        self.__field1 = field1

class DDL_CharacterStringType(Type):

    def __init__(self, length: int):
        self.length = length
        
    @property
    def length(self) -> int:
        return self.__length

    @length.setter
    def length(self, length: int):
        self.__length = length

class DDL_BitStringType(Type):

    def __init__(self, length: int):
        self.length = length
        
    @property
    def length(self) -> int:
        return self.__length

    @length.setter
    def length(self, length: int):
        self.__length = length

class NationalCharacterStringType:

    pass
class DDL_NationalCharVarying(NationalCharacterStringType):

    pass
class DDL_NationalCharacterVarying(NationalCharacterStringType):

    pass
class DDL_NChar(NationalCharacterStringType):

    pass
class DDL_NationalChar(NationalCharacterStringType):

    pass
class DDL_NCharVarying(NationalCharacterStringType):

    pass
class DDL_NationalCharacter(NationalCharacterStringType):

    pass
class DDL_NationalCharacterStringType(Type):

    def __init__(self, length: int):
        self.length = length
        
    @property
    def length(self) -> int:
        return self.__length

    @length.setter
    def length(self, length: int):
        self.__length = length

class DDL_Type(ABC):

    pass
class DDL_ValuesCheck:

    def __init__(self, value: str, comparator: str, columnName: str, logConjuntion: str, DDL_ValuesCheck: "DDL_Check" = None):
        self.value = value
        self.comparator = comparator
        self.columnName = columnName
        self.logConjuntion = logConjuntion
        self.DDL_ValuesCheck = DDL_ValuesCheck
        
    @property
    def comparator(self) -> str:
        return self.__comparator

    @comparator.setter
    def comparator(self, comparator: str):
        self.__comparator = comparator

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def columnName(self) -> str:
        return self.__columnName

    @columnName.setter
    def columnName(self, columnName: str):
        self.__columnName = columnName

    @property
    def logConjuntion(self) -> str:
        return self.__logConjuntion

    @logConjuntion.setter
    def logConjuntion(self, logConjuntion: str):
        self.__logConjuntion = logConjuntion

    @property
    def DDL_ValuesCheck(self):
        return self.__DDL_ValuesCheck

    @DDL_ValuesCheck.setter
    def DDL_ValuesCheck(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DDL_ValuesCheck__DDL_ValuesCheck", None)
        self.__DDL_ValuesCheck = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DDL_Check16"):
                opp_val = getattr(old_value, "DDL_Check16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DDL_Check16"):
                opp_val = getattr(value, "DDL_Check16", None)
                if opp_val is None:
                    setattr(value, "DDL_Check16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class DDL_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class DDL_Statement(ABC):

    pass
class DDL_DDLDefinition:

    pass
class NamedElement:

    pass
class DDL_Column(NamedElement):

    def __init__(self, columnNull: bool, DDL_Column: "DDL_Table" = None, DDL_Column11: "DDL_Type" = None):
        self.columnNull = columnNull
        self.DDL_Column = DDL_Column
        self.DDL_Column11 = DDL_Column11
        
    @property
    def columnNull(self) -> bool:
        return self.__columnNull

    @columnNull.setter
    def columnNull(self, columnNull: bool):
        self.__columnNull = columnNull

    @property
    def DDL_Column11(self):
        return self.__DDL_Column11

    @DDL_Column11.setter
    def DDL_Column11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DDL_Column__DDL_Column11", None)
        self.__DDL_Column11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DDL_Type"):
                opp_val = getattr(old_value, "DDL_Type", None)
                if opp_val == self:
                    setattr(old_value, "DDL_Type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DDL_Type"):
                opp_val = getattr(value, "DDL_Type", None)
                setattr(value, "DDL_Type", self)

    @property
    def DDL_Column(self):
        return self.__DDL_Column

    @DDL_Column.setter
    def DDL_Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DDL_Column__DDL_Column", None)
        self.__DDL_Column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DDL_Table"):
                opp_val = getattr(old_value, "DDL_Table", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DDL_Table"):
                opp_val = getattr(value, "DDL_Table", None)
                if opp_val is None:
                    setattr(value, "DDL_Table", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class DDL_Fk(NamedElement):

    def __init__(self, columnName: str, columnReference: str, DDL_Fk13: "DDL_Table" = None, DDL_Fk: "DDL_Table" = None):
        self.columnName = columnName
        self.columnReference = columnReference
        self.DDL_Fk13 = DDL_Fk13
        self.DDL_Fk = DDL_Fk
        
    @property
    def columnName(self) -> str:
        return self.__columnName

    @columnName.setter
    def columnName(self, columnName: str):
        self.__columnName = columnName

    @property
    def columnReference(self) -> str:
        return self.__columnReference

    @columnReference.setter
    def columnReference(self, columnReference: str):
        self.__columnReference = columnReference

    @property
    def DDL_Fk(self):
        return self.__DDL_Fk

    @DDL_Fk.setter
    def DDL_Fk(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DDL_Fk__DDL_Fk", None)
        self.__DDL_Fk = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DDL_Table7"):
                opp_val = getattr(old_value, "DDL_Table7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DDL_Table7"):
                opp_val = getattr(value, "DDL_Table7", None)
                if opp_val is None:
                    setattr(value, "DDL_Table7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def DDL_Fk13(self):
        return self.__DDL_Fk13

    @DDL_Fk13.setter
    def DDL_Fk13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DDL_Fk__DDL_Fk13", None)
        self.__DDL_Fk13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DDL_Table14"):
                opp_val = getattr(old_value, "DDL_Table14", None)
                if opp_val == self:
                    setattr(old_value, "DDL_Table14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DDL_Table14"):
                opp_val = getattr(value, "DDL_Table14", None)
                setattr(value, "DDL_Table14", self)

class DDL_Ck(NamedElement):

    def __init__(self, columnName: str, DDL_Ck: "DDL_Table" = None):
        self.columnName = columnName
        self.DDL_Ck = DDL_Ck
        
    @property
    def columnName(self) -> str:
        return self.__columnName

    @columnName.setter
    def columnName(self, columnName: str):
        self.__columnName = columnName

    @property
    def DDL_Ck(self):
        return self.__DDL_Ck

    @DDL_Ck.setter
    def DDL_Ck(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DDL_Ck__DDL_Ck", None)
        self.__DDL_Ck = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DDL_Table5"):
                opp_val = getattr(old_value, "DDL_Table5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DDL_Table5"):
                opp_val = getattr(value, "DDL_Table5", None)
                if opp_val is None:
                    setattr(value, "DDL_Table5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class DDL_Pk(NamedElement):

    def __init__(self, columnName: str, DDL_Pk: "DDL_Table" = None):
        self.columnName = columnName
        self.DDL_Pk = DDL_Pk
        
    @property
    def columnName(self) -> str:
        return self.__columnName

    @columnName.setter
    def columnName(self, columnName: str):
        self.__columnName = columnName

    @property
    def DDL_Pk(self):
        return self.__DDL_Pk

    @DDL_Pk.setter
    def DDL_Pk(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DDL_Pk__DDL_Pk", None)
        self.__DDL_Pk = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DDL_Table3"):
                opp_val = getattr(old_value, "DDL_Table3", None)
                if opp_val == self:
                    setattr(old_value, "DDL_Table3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DDL_Table3"):
                opp_val = getattr(value, "DDL_Table3", None)
                setattr(value, "DDL_Table3", self)

class DDL_Check(NamedElement):

    pass
class Statement:

    pass
class DDL_Table(NamedElement, Statement):

    pass
class DDL_Database(NamedElement, Statement):

    pass