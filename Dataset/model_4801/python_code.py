from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class TestNextEnum(Enum):
    Enum1 = "Enum1"
    Enum2 = "Enum2"
class TestEnum(Enum):
    Enum0 = "Enum0"
    Enum1 = "Enum1"
    Enum2 = "Enum2"


############################################
# Definition of Classes
############################################

class types_ManyTypes:

    def __init__(self, string: str, integerObject: str, long: str, doubleObject: str, floatObject: str, clazz: str, charObject: str, byteObject: str, byteArray: str, bigDecimal: str, bigInteger: str, enum: str, date: date, stringArray: str, longArray: str):
        self.string = string
        self.integerObject = integerObject
        self.long = long
        self.doubleObject = doubleObject
        self.floatObject = floatObject
        self.clazz = clazz
        self.charObject = charObject
        self.byteObject = byteObject
        self.byteArray = byteArray
        self.bigDecimal = bigDecimal
        self.bigInteger = bigInteger
        self.enum = enum
        self.date = date
        self.stringArray = stringArray
        self.longArray = longArray
        
    @property
    def stringArray(self) -> str:
        return self.__stringArray

    @stringArray.setter
    def stringArray(self, stringArray: str):
        self.__stringArray = stringArray

    @property
    def floatObject(self) -> str:
        return self.__floatObject

    @floatObject.setter
    def floatObject(self, floatObject: str):
        self.__floatObject = floatObject

    @property
    def integerObject(self) -> str:
        return self.__integerObject

    @integerObject.setter
    def integerObject(self, integerObject: str):
        self.__integerObject = integerObject

    @property
    def byteObject(self) -> str:
        return self.__byteObject

    @byteObject.setter
    def byteObject(self, byteObject: str):
        self.__byteObject = byteObject

    @property
    def string(self) -> str:
        return self.__string

    @string.setter
    def string(self, string: str):
        self.__string = string

    @property
    def date(self) -> date:
        return self.__date

    @date.setter
    def date(self, date: date):
        self.__date = date

    @property
    def longArray(self) -> str:
        return self.__longArray

    @longArray.setter
    def longArray(self, longArray: str):
        self.__longArray = longArray

    @property
    def bigDecimal(self) -> str:
        return self.__bigDecimal

    @bigDecimal.setter
    def bigDecimal(self, bigDecimal: str):
        self.__bigDecimal = bigDecimal

    @property
    def byteArray(self) -> str:
        return self.__byteArray

    @byteArray.setter
    def byteArray(self, byteArray: str):
        self.__byteArray = byteArray

    @property
    def doubleObject(self) -> str:
        return self.__doubleObject

    @doubleObject.setter
    def doubleObject(self, doubleObject: str):
        self.__doubleObject = doubleObject

    @property
    def clazz(self) -> str:
        return self.__clazz

    @clazz.setter
    def clazz(self, clazz: str):
        self.__clazz = clazz

    @property
    def bigInteger(self) -> str:
        return self.__bigInteger

    @bigInteger.setter
    def bigInteger(self, bigInteger: str):
        self.__bigInteger = bigInteger

    @property
    def long(self) -> str:
        return self.__long

    @long.setter
    def long(self, long: str):
        self.__long = long

    @property
    def charObject(self) -> str:
        return self.__charObject

    @charObject.setter
    def charObject(self, charObject: str):
        self.__charObject = charObject

    @property
    def enum(self) -> str:
        return self.__enum

    @enum.setter
    def enum(self, enum: str):
        self.__enum = enum

class types_SingleTypes:

    def __init__(self, date: date, stringArray: str, longArray: str, string: str, integer: int, integerObject: str, long: str, longObject: str, double: float, doubleObject: str, float: float, floatObject: str, clazz: str, char: str, charObject: str, byte: str, byteObject: str, byteArray: str, bigDecimal: str, bigInteger: str, enum: str, nextEnum: str):
        self.date = date
        self.stringArray = stringArray
        self.longArray = longArray
        self.string = string
        self.integer = integer
        self.integerObject = integerObject
        self.long = long
        self.longObject = longObject
        self.double = double
        self.doubleObject = doubleObject
        self.float = float
        self.floatObject = floatObject
        self.clazz = clazz
        self.char = char
        self.charObject = charObject
        self.byte = byte
        self.byteObject = byteObject
        self.byteArray = byteArray
        self.bigDecimal = bigDecimal
        self.bigInteger = bigInteger
        self.enum = enum
        self.nextEnum = nextEnum
        
    @property
    def date(self) -> date:
        return self.__date

    @date.setter
    def date(self, date: date):
        self.__date = date

    @property
    def byte(self) -> str:
        return self.__byte

    @byte.setter
    def byte(self, byte: str):
        self.__byte = byte

    @property
    def bigInteger(self) -> str:
        return self.__bigInteger

    @bigInteger.setter
    def bigInteger(self, bigInteger: str):
        self.__bigInteger = bigInteger

    @property
    def integer(self) -> int:
        return self.__integer

    @integer.setter
    def integer(self, integer: int):
        self.__integer = integer

    @property
    def nextEnum(self) -> str:
        return self.__nextEnum

    @nextEnum.setter
    def nextEnum(self, nextEnum: str):
        self.__nextEnum = nextEnum

    @property
    def char(self) -> str:
        return self.__char

    @char.setter
    def char(self, char: str):
        self.__char = char

    @property
    def clazz(self) -> str:
        return self.__clazz

    @clazz.setter
    def clazz(self, clazz: str):
        self.__clazz = clazz

    @property
    def bigDecimal(self) -> str:
        return self.__bigDecimal

    @bigDecimal.setter
    def bigDecimal(self, bigDecimal: str):
        self.__bigDecimal = bigDecimal

    @property
    def longArray(self) -> str:
        return self.__longArray

    @longArray.setter
    def longArray(self, longArray: str):
        self.__longArray = longArray

    @property
    def charObject(self) -> str:
        return self.__charObject

    @charObject.setter
    def charObject(self, charObject: str):
        self.__charObject = charObject

    @property
    def enum(self) -> str:
        return self.__enum

    @enum.setter
    def enum(self, enum: str):
        self.__enum = enum

    @property
    def string(self) -> str:
        return self.__string

    @string.setter
    def string(self, string: str):
        self.__string = string

    @property
    def float(self) -> float:
        return self.__float

    @float.setter
    def float(self, float: float):
        self.__float = float

    @property
    def integerObject(self) -> str:
        return self.__integerObject

    @integerObject.setter
    def integerObject(self, integerObject: str):
        self.__integerObject = integerObject

    @property
    def double(self) -> float:
        return self.__double

    @double.setter
    def double(self, double: float):
        self.__double = double

    @property
    def longObject(self) -> str:
        return self.__longObject

    @longObject.setter
    def longObject(self, longObject: str):
        self.__longObject = longObject

    @property
    def floatObject(self) -> str:
        return self.__floatObject

    @floatObject.setter
    def floatObject(self, floatObject: str):
        self.__floatObject = floatObject

    @property
    def long(self) -> str:
        return self.__long

    @long.setter
    def long(self, long: str):
        self.__long = long

    @property
    def byteArray(self) -> str:
        return self.__byteArray

    @byteArray.setter
    def byteArray(self, byteArray: str):
        self.__byteArray = byteArray

    @property
    def byteObject(self) -> str:
        return self.__byteObject

    @byteObject.setter
    def byteObject(self, byteObject: str):
        self.__byteObject = byteObject

    @property
    def stringArray(self) -> str:
        return self.__stringArray

    @stringArray.setter
    def stringArray(self, stringArray: str):
        self.__stringArray = stringArray

    @property
    def doubleObject(self) -> str:
        return self.__doubleObject

    @doubleObject.setter
    def doubleObject(self, doubleObject: str):
        self.__doubleObject = doubleObject
