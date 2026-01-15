from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class AEnum(Enum):
    ENUM0 = "ENUM0"
    ENUM1 = "ENUM1"
class StateWithoutDefault(Enum):
    OPEN = "OPEN"
    MOVE = "MOVE"
    CLOSE = "CLOSE"
    MOVING = "MOVING"
    DELETE = "DELETE"
class Heavy(Enum):
    OPEN = "OPEN"
    MOVE = "MOVE"
    CLOSE = "CLOSE"
    MOVING = "MOVING"
    DELETE = "DELETE"
    OPEN1 = "OPEN1"
    MOVE1 = "MOVE1"
    CLOS1E = "CLOS1E"
    DELETE2 = "DELETE2"
    OPEN3 = "OPEN3"
    MOVE3 = "MOVE3"
    CLOSE3 = "CLOSE3"
    MOVING3 = "MOVING3"
    DELETE3 = "DELETE3"
    OPEN4 = "OPEN4"
    MOVE4 = "MOVE4"
    CLOSE4 = "CLOSE4"
    MOVING4 = "MOVING4"
    DELETE4 = "DELETE4"
    MOVING1 = "MOVING1"
    DELETE1 = "DELETE1"
    OPEN2 = "OPEN2"
    MOVE2 = "MOVE2"
    CLOSE2 = "CLOSE2"
    MOVING2 = "MOVING2"


############################################
# Definition of Classes
############################################

class Type:

    pass
class alldatatypes_Enums(Type):

    def __init__(self, enum_01: str, enum_01_EmptyDefault: str, enum_1: str, enums: str, notEditableEnum_01: str, states: str, statesMax2: str, statesMin1Max2: str, heavy: str):
        self.enum_01 = enum_01
        self.enum_01_EmptyDefault = enum_01_EmptyDefault
        self.enum_1 = enum_1
        self.enums = enums
        self.notEditableEnum_01 = notEditableEnum_01
        self.states = states
        self.statesMax2 = statesMax2
        self.statesMin1Max2 = statesMin1Max2
        self.heavy = heavy
        
    @property
    def states(self) -> str:
        return self.__states

    @states.setter
    def states(self, states: str):
        self.__states = states

    @property
    def enum_01(self) -> str:
        return self.__enum_01

    @enum_01.setter
    def enum_01(self, enum_01: str):
        self.__enum_01 = enum_01

    @property
    def enums(self) -> str:
        return self.__enums

    @enums.setter
    def enums(self, enums: str):
        self.__enums = enums

    @property
    def enum_01_EmptyDefault(self) -> str:
        return self.__enum_01_EmptyDefault

    @enum_01_EmptyDefault.setter
    def enum_01_EmptyDefault(self, enum_01_EmptyDefault: str):
        self.__enum_01_EmptyDefault = enum_01_EmptyDefault

    @property
    def statesMin1Max2(self) -> str:
        return self.__statesMin1Max2

    @statesMin1Max2.setter
    def statesMin1Max2(self, statesMin1Max2: str):
        self.__statesMin1Max2 = statesMin1Max2

    @property
    def statesMax2(self) -> str:
        return self.__statesMax2

    @statesMax2.setter
    def statesMax2(self, statesMax2: str):
        self.__statesMax2 = statesMax2

    @property
    def heavy(self) -> str:
        return self.__heavy

    @heavy.setter
    def heavy(self, heavy: str):
        self.__heavy = heavy

    @property
    def notEditableEnum_01(self) -> str:
        return self.__notEditableEnum_01

    @notEditableEnum_01.setter
    def notEditableEnum_01(self, notEditableEnum_01: str):
        self.__notEditableEnum_01 = notEditableEnum_01

    @property
    def enum_1(self) -> str:
        return self.__enum_1

    @enum_1.setter
    def enum_1(self, enum_1: str):
        self.__enum_1 = enum_1

class alldatatypes_BigIntegers(Type):

    def __init__(self, bigInt_01: str, bigInt_1: str, bigInt_01_EmptyDefault: str, notEditableBigInt_01: str, bigInts: str):
        self.bigInt_01 = bigInt_01
        self.bigInt_1 = bigInt_1
        self.bigInt_01_EmptyDefault = bigInt_01_EmptyDefault
        self.notEditableBigInt_01 = notEditableBigInt_01
        self.bigInts = bigInts
        
    @property
    def notEditableBigInt_01(self) -> str:
        return self.__notEditableBigInt_01

    @notEditableBigInt_01.setter
    def notEditableBigInt_01(self, notEditableBigInt_01: str):
        self.__notEditableBigInt_01 = notEditableBigInt_01

    @property
    def bigInt_01(self) -> str:
        return self.__bigInt_01

    @bigInt_01.setter
    def bigInt_01(self, bigInt_01: str):
        self.__bigInt_01 = bigInt_01

    @property
    def bigInt_01_EmptyDefault(self) -> str:
        return self.__bigInt_01_EmptyDefault

    @bigInt_01_EmptyDefault.setter
    def bigInt_01_EmptyDefault(self, bigInt_01_EmptyDefault: str):
        self.__bigInt_01_EmptyDefault = bigInt_01_EmptyDefault

    @property
    def bigInt_1(self) -> str:
        return self.__bigInt_1

    @bigInt_1.setter
    def bigInt_1(self, bigInt_1: str):
        self.__bigInt_1 = bigInt_1

    @property
    def bigInts(self) -> str:
        return self.__bigInts

    @bigInts.setter
    def bigInts(self, bigInts: str):
        self.__bigInts = bigInts

class alldatatypes_Longs(Type):

    def __init__(self, long_01: str, long_1: str, long_01_EmptyDefault: str, notEditableLong_01: str):
        self.long_01 = long_01
        self.long_1 = long_1
        self.long_01_EmptyDefault = long_01_EmptyDefault
        self.notEditableLong_01 = notEditableLong_01
        
    @property
    def notEditableLong_01(self) -> str:
        return self.__notEditableLong_01

    @notEditableLong_01.setter
    def notEditableLong_01(self, notEditableLong_01: str):
        self.__notEditableLong_01 = notEditableLong_01

    @property
    def long_01_EmptyDefault(self) -> str:
        return self.__long_01_EmptyDefault

    @long_01_EmptyDefault.setter
    def long_01_EmptyDefault(self, long_01_EmptyDefault: str):
        self.__long_01_EmptyDefault = long_01_EmptyDefault

    @property
    def long_1(self) -> str:
        return self.__long_1

    @long_1.setter
    def long_1(self, long_1: str):
        self.__long_1 = long_1

    @property
    def long_01(self) -> str:
        return self.__long_01

    @long_01.setter
    def long_01(self, long_01: str):
        self.__long_01 = long_01

class alldatatypes_Dates(Type):

    def __init__(self, dateEmptyDefault_01: date, date_01: date, date_1: date, date_01_HM: date, date_01_HMS: date, date_01_HMSms: date, notEditableDate_01: date, dates: date):
        self.dateEmptyDefault_01 = dateEmptyDefault_01
        self.date_01 = date_01
        self.date_1 = date_1
        self.date_01_HM = date_01_HM
        self.date_01_HMS = date_01_HMS
        self.date_01_HMSms = date_01_HMSms
        self.notEditableDate_01 = notEditableDate_01
        self.dates = dates
        
    @property
    def dates(self) -> date:
        return self.__dates

    @dates.setter
    def dates(self, dates: date):
        self.__dates = dates

    @property
    def date_01(self) -> date:
        return self.__date_01

    @date_01.setter
    def date_01(self, date_01: date):
        self.__date_01 = date_01

    @property
    def date_01_HM(self) -> date:
        return self.__date_01_HM

    @date_01_HM.setter
    def date_01_HM(self, date_01_HM: date):
        self.__date_01_HM = date_01_HM

    @property
    def date_1(self) -> date:
        return self.__date_1

    @date_1.setter
    def date_1(self, date_1: date):
        self.__date_1 = date_1

    @property
    def date_01_HMS(self) -> date:
        return self.__date_01_HMS

    @date_01_HMS.setter
    def date_01_HMS(self, date_01_HMS: date):
        self.__date_01_HMS = date_01_HMS

    @property
    def notEditableDate_01(self) -> date:
        return self.__notEditableDate_01

    @notEditableDate_01.setter
    def notEditableDate_01(self, notEditableDate_01: date):
        self.__notEditableDate_01 = notEditableDate_01

    @property
    def dateEmptyDefault_01(self) -> date:
        return self.__dateEmptyDefault_01

    @dateEmptyDefault_01.setter
    def dateEmptyDefault_01(self, dateEmptyDefault_01: date):
        self.__dateEmptyDefault_01 = dateEmptyDefault_01

    @property
    def date_01_HMSms(self) -> date:
        return self.__date_01_HMSms

    @date_01_HMSms.setter
    def date_01_HMSms(self, date_01_HMSms: date):
        self.__date_01_HMSms = date_01_HMSms

class alldatatypes_Floats(Type):

    def __init__(self, float_01: float, float_1: float, float_01_EmptyDefault: float, notEditableFloat_01: float):
        self.float_01 = float_01
        self.float_1 = float_1
        self.float_01_EmptyDefault = float_01_EmptyDefault
        self.notEditableFloat_01 = notEditableFloat_01
        
    @property
    def notEditableFloat_01(self) -> float:
        return self.__notEditableFloat_01

    @notEditableFloat_01.setter
    def notEditableFloat_01(self, notEditableFloat_01: float):
        self.__notEditableFloat_01 = notEditableFloat_01

    @property
    def float_1(self) -> float:
        return self.__float_1

    @float_1.setter
    def float_1(self, float_1: float):
        self.__float_1 = float_1

    @property
    def float_01_EmptyDefault(self) -> float:
        return self.__float_01_EmptyDefault

    @float_01_EmptyDefault.setter
    def float_01_EmptyDefault(self, float_01_EmptyDefault: float):
        self.__float_01_EmptyDefault = float_01_EmptyDefault

    @property
    def float_01(self) -> float:
        return self.__float_01

    @float_01.setter
    def float_01(self, float_01: float):
        self.__float_01 = float_01

class alldatatypes_Doubles(Type):

    def __init__(self, double_01: float, double_1: float, double_01_EmptyDefault: float, notEditableDouble_01: float):
        self.double_01 = double_01
        self.double_1 = double_1
        self.double_01_EmptyDefault = double_01_EmptyDefault
        self.notEditableDouble_01 = notEditableDouble_01
        
    @property
    def double_1(self) -> float:
        return self.__double_1

    @double_1.setter
    def double_1(self, double_1: float):
        self.__double_1 = double_1

    @property
    def double_01(self) -> float:
        return self.__double_01

    @double_01.setter
    def double_01(self, double_01: float):
        self.__double_01 = double_01

    @property
    def double_01_EmptyDefault(self) -> float:
        return self.__double_01_EmptyDefault

    @double_01_EmptyDefault.setter
    def double_01_EmptyDefault(self, double_01_EmptyDefault: float):
        self.__double_01_EmptyDefault = double_01_EmptyDefault

    @property
    def notEditableDouble_01(self) -> float:
        return self.__notEditableDouble_01

    @notEditableDouble_01.setter
    def notEditableDouble_01(self, notEditableDouble_01: float):
        self.__notEditableDouble_01 = notEditableDouble_01

class alldatatypes_Integers(Type):

    def __init__(self, ints: int, hiddenInt_01: int, int_01: int, int_1: int, int_01_EmptyDefault: int, notEditableInt_01: int):
        self.ints = ints
        self.hiddenInt_01 = hiddenInt_01
        self.int_01 = int_01
        self.int_1 = int_1
        self.int_01_EmptyDefault = int_01_EmptyDefault
        self.notEditableInt_01 = notEditableInt_01
        
    @property
    def hiddenInt_01(self) -> int:
        return self.__hiddenInt_01

    @hiddenInt_01.setter
    def hiddenInt_01(self, hiddenInt_01: int):
        self.__hiddenInt_01 = hiddenInt_01

    @property
    def int_01_EmptyDefault(self) -> int:
        return self.__int_01_EmptyDefault

    @int_01_EmptyDefault.setter
    def int_01_EmptyDefault(self, int_01_EmptyDefault: int):
        self.__int_01_EmptyDefault = int_01_EmptyDefault

    @property
    def notEditableInt_01(self) -> int:
        return self.__notEditableInt_01

    @notEditableInt_01.setter
    def notEditableInt_01(self, notEditableInt_01: int):
        self.__notEditableInt_01 = notEditableInt_01

    @property
    def int_01(self) -> int:
        return self.__int_01

    @int_01.setter
    def int_01(self, int_01: int):
        self.__int_01 = int_01

    @property
    def ints(self) -> int:
        return self.__ints

    @ints.setter
    def ints(self, ints: int):
        self.__ints = ints

    @property
    def int_1(self) -> int:
        return self.__int_1

    @int_1.setter
    def int_1(self, int_1: int):
        self.__int_1 = int_1

class alldatatypes_BigDecimals(Type):

    def __init__(self, bigDecimal_01: str, bigDecimal_1: str, bigDecimal_01_EmptyDefault: str, notEditableBigDecimal_01: str, bigDecimals: str):
        self.bigDecimal_01 = bigDecimal_01
        self.bigDecimal_1 = bigDecimal_1
        self.bigDecimal_01_EmptyDefault = bigDecimal_01_EmptyDefault
        self.notEditableBigDecimal_01 = notEditableBigDecimal_01
        self.bigDecimals = bigDecimals
        
    @property
    def bigDecimals(self) -> str:
        return self.__bigDecimals

    @bigDecimals.setter
    def bigDecimals(self, bigDecimals: str):
        self.__bigDecimals = bigDecimals

    @property
    def notEditableBigDecimal_01(self) -> str:
        return self.__notEditableBigDecimal_01

    @notEditableBigDecimal_01.setter
    def notEditableBigDecimal_01(self, notEditableBigDecimal_01: str):
        self.__notEditableBigDecimal_01 = notEditableBigDecimal_01

    @property
    def bigDecimal_01(self) -> str:
        return self.__bigDecimal_01

    @bigDecimal_01.setter
    def bigDecimal_01(self, bigDecimal_01: str):
        self.__bigDecimal_01 = bigDecimal_01

    @property
    def bigDecimal_1(self) -> str:
        return self.__bigDecimal_1

    @bigDecimal_1.setter
    def bigDecimal_1(self, bigDecimal_1: str):
        self.__bigDecimal_1 = bigDecimal_1

    @property
    def bigDecimal_01_EmptyDefault(self) -> str:
        return self.__bigDecimal_01_EmptyDefault

    @bigDecimal_01_EmptyDefault.setter
    def bigDecimal_01_EmptyDefault(self, bigDecimal_01_EmptyDefault: str):
        self.__bigDecimal_01_EmptyDefault = bigDecimal_01_EmptyDefault

class alldatatypes_Shorts(Type):

    def __init__(self, short_01: str, short_1: str, short_01_EmptyDefault: str, notEditableShort_01: str):
        self.short_01 = short_01
        self.short_1 = short_1
        self.short_01_EmptyDefault = short_01_EmptyDefault
        self.notEditableShort_01 = notEditableShort_01
        
    @property
    def short_1(self) -> str:
        return self.__short_1

    @short_1.setter
    def short_1(self, short_1: str):
        self.__short_1 = short_1

    @property
    def short_01_EmptyDefault(self) -> str:
        return self.__short_01_EmptyDefault

    @short_01_EmptyDefault.setter
    def short_01_EmptyDefault(self, short_01_EmptyDefault: str):
        self.__short_01_EmptyDefault = short_01_EmptyDefault

    @property
    def notEditableShort_01(self) -> str:
        return self.__notEditableShort_01

    @notEditableShort_01.setter
    def notEditableShort_01(self, notEditableShort_01: str):
        self.__notEditableShort_01 = notEditableShort_01

    @property
    def short_01(self) -> str:
        return self.__short_01

    @short_01.setter
    def short_01(self, short_01: str):
        self.__short_01 = short_01

class alldatatypes_Booleans(Type):

    def __init__(self, boolean_01: bool, boolean_01_EmptyDefault: bool, boolean_1: bool, notEditableBoolean_01: bool):
        self.boolean_01 = boolean_01
        self.boolean_01_EmptyDefault = boolean_01_EmptyDefault
        self.boolean_1 = boolean_1
        self.notEditableBoolean_01 = notEditableBoolean_01
        
    @property
    def boolean_01(self) -> bool:
        return self.__boolean_01

    @boolean_01.setter
    def boolean_01(self, boolean_01: bool):
        self.__boolean_01 = boolean_01

    @property
    def notEditableBoolean_01(self) -> bool:
        return self.__notEditableBoolean_01

    @notEditableBoolean_01.setter
    def notEditableBoolean_01(self, notEditableBoolean_01: bool):
        self.__notEditableBoolean_01 = notEditableBoolean_01

    @property
    def boolean_1(self) -> bool:
        return self.__boolean_1

    @boolean_1.setter
    def boolean_1(self, boolean_1: bool):
        self.__boolean_1 = boolean_1

    @property
    def boolean_01_EmptyDefault(self) -> bool:
        return self.__boolean_01_EmptyDefault

    @boolean_01_EmptyDefault.setter
    def boolean_01_EmptyDefault(self, boolean_01_EmptyDefault: bool):
        self.__boolean_01_EmptyDefault = boolean_01_EmptyDefault

class alldatatypes_Strings(Type):

    def __init__(self, text_01_EmptyDefault: str, link_01: str, html_01: str, notEditableText_01: str, text_01: str, text_1: str, textarea: str):
        self.text_01_EmptyDefault = text_01_EmptyDefault
        self.link_01 = link_01
        self.html_01 = html_01
        self.notEditableText_01 = notEditableText_01
        self.text_01 = text_01
        self.text_1 = text_1
        self.textarea = textarea
        
    @property
    def text_01_EmptyDefault(self) -> str:
        return self.__text_01_EmptyDefault

    @text_01_EmptyDefault.setter
    def text_01_EmptyDefault(self, text_01_EmptyDefault: str):
        self.__text_01_EmptyDefault = text_01_EmptyDefault

    @property
    def link_01(self) -> str:
        return self.__link_01

    @link_01.setter
    def link_01(self, link_01: str):
        self.__link_01 = link_01

    @property
    def html_01(self) -> str:
        return self.__html_01

    @html_01.setter
    def html_01(self, html_01: str):
        self.__html_01 = html_01

    @property
    def notEditableText_01(self) -> str:
        return self.__notEditableText_01

    @notEditableText_01.setter
    def notEditableText_01(self, notEditableText_01: str):
        self.__notEditableText_01 = notEditableText_01

    @property
    def textarea(self) -> str:
        return self.__textarea

    @textarea.setter
    def textarea(self, textarea: str):
        self.__textarea = textarea

    @property
    def text_1(self) -> str:
        return self.__text_1

    @text_1.setter
    def text_1(self, text_1: str):
        self.__text_1 = text_1

    @property
    def text_01(self) -> str:
        return self.__text_01

    @text_01.setter
    def text_01(self, text_01: str):
        self.__text_01 = text_01

class Element:

    pass
class alldatatypes_Type(Element):

    pass
class alldatatypes_Root(Element):

    def __init__(self, alldatatypes_Root: set["alldatatypes_Type"] = None):
        self.alldatatypes_Root = alldatatypes_Root if alldatatypes_Root is not None else set()
        
    @property
    def alldatatypes_Root(self):
        return self.__alldatatypes_Root

    @alldatatypes_Root.setter
    def alldatatypes_Root(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_alldatatypes_Root__alldatatypes_Root", None)
        self.__alldatatypes_Root = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "alldatatypes_Type"):
                    opp_val = getattr(item, "alldatatypes_Type", None)
                    
                    if opp_val == self:
                        setattr(item, "alldatatypes_Type", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "alldatatypes_Type"):
                    opp_val = getattr(item, "alldatatypes_Type", None)
                    
                    setattr(item, "alldatatypes_Type", self)
                    

    def getAllTypes(self) -> str:
        # TODO: Implement getAllTypes method
        pass

class alldatatypes_Element(ABC):

    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name
