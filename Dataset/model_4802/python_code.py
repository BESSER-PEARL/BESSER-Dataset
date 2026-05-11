from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class TestEnum(Enum):
    Enum0 = "Enum0"
    Enum1 = "Enum1"
    Enum2 = "Enum2"
class TestNextEnum(Enum):
    Enum1 = "Enum1"
    Enum2 = "Enum2"


############################################
# Definition of Classes
############################################

class types_ManyTypes:

    def __init__(self, stringArray: str, longArray: str, string: str, integerObject: str, long: str, doubleObject: str, floatObject: str, clazz: str, charObject: str, byteObject: str, byteArray: str, bigDecimal: str, bigInteger: str, enum: str, date: date):
        self.stringArray = stringArray
        self.longArray = longArray
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
        
        pass
    @property
    def byteObject(self):
        return self.__byteObject

    @byteObject.setter
    def byteObject(self, byteObject: str):
        self.__byteObject = byteObject


    @property
    def bigDecimal(self):
        return self.__bigDecimal

    @bigDecimal.setter
    def bigDecimal(self, bigDecimal: str):
        self.__bigDecimal = bigDecimal


    @property
    def doubleObject(self):
        return self.__doubleObject

    @doubleObject.setter
    def doubleObject(self, doubleObject: str):
        self.__doubleObject = doubleObject


    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date: date):
        self.__date = date


    @property
    def enum(self):
        return self.__enum

    @enum.setter
    def enum(self, enum: str):
        self.__enum = enum


    @property
    def long(self):
        return self.__long

    @long.setter
    def long(self, long: str):
        self.__long = long


    @property
    def clazz(self):
        return self.__clazz

    @clazz.setter
    def clazz(self, clazz: str):
        self.__clazz = clazz


    @property
    def string(self):
        return self.__string

    @string.setter
    def string(self, string: str):
        self.__string = string


    @property
    def bigInteger(self):
        return self.__bigInteger

    @bigInteger.setter
    def bigInteger(self, bigInteger: str):
        self.__bigInteger = bigInteger


    @property
    def floatObject(self):
        return self.__floatObject

    @floatObject.setter
    def floatObject(self, floatObject: str):
        self.__floatObject = floatObject


    @property
    def charObject(self):
        return self.__charObject

    @charObject.setter
    def charObject(self, charObject: str):
        self.__charObject = charObject


    @property
    def integerObject(self):
        return self.__integerObject

    @integerObject.setter
    def integerObject(self, integerObject: str):
        self.__integerObject = integerObject


    @property
    def byteArray(self):
        return self.__byteArray

    @byteArray.setter
    def byteArray(self, byteArray: str):
        self.__byteArray = byteArray


    @property
    def longArray(self):
        return self.__longArray

    @longArray.setter
    def longArray(self, longArray: str):
        self.__longArray = longArray


    @property
    def stringArray(self):
        return self.__stringArray

    @stringArray.setter
    def stringArray(self, stringArray: str):
        self.__stringArray = stringArray


class types_SingleTypes:

    def __init__(self, long: str, longObject: str, double: float, doubleObject: str, float: float, floatObject: str, clazz: str, char: str, charObject: str, byte: str, byteObject: str, byteArray: str, bigDecimal: str, bigInteger: str, enum: str, date: date, string: str, integer: int, integerObject: str, stringArray: str, longArray: str, nextEnum: str):
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
        self.date = date
        self.string = string
        self.integer = integer
        self.integerObject = integerObject
        self.stringArray = stringArray
        self.longArray = longArray
        self.nextEnum = nextEnum
        
        pass
    @property
    def bigDecimal(self):
        return self.__bigDecimal

    @bigDecimal.setter
    def bigDecimal(self, bigDecimal: str):
        self.__bigDecimal = bigDecimal


    @property
    def enum(self):
        return self.__enum

    @enum.setter
    def enum(self, enum: str):
        self.__enum = enum


    @property
    def float(self):
        return self.__float

    @float.setter
    def float(self, float: float):
        self.__float = float


    @property
    def clazz(self):
        return self.__clazz

    @clazz.setter
    def clazz(self, clazz: str):
        self.__clazz = clazz


    @property
    def integer(self):
        return self.__integer

    @integer.setter
    def integer(self, integer: int):
        self.__integer = integer


    @property
    def charObject(self):
        return self.__charObject

    @charObject.setter
    def charObject(self, charObject: str):
        self.__charObject = charObject


    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date: date):
        self.__date = date


    @property
    def integerObject(self):
        return self.__integerObject

    @integerObject.setter
    def integerObject(self, integerObject: str):
        self.__integerObject = integerObject


    @property
    def long(self):
        return self.__long

    @long.setter
    def long(self, long: str):
        self.__long = long


    @property
    def string(self):
        return self.__string

    @string.setter
    def string(self, string: str):
        self.__string = string


    @property
    def char(self):
        return self.__char

    @char.setter
    def char(self, char: str):
        self.__char = char


    @property
    def stringArray(self):
        return self.__stringArray

    @stringArray.setter
    def stringArray(self, stringArray: str):
        self.__stringArray = stringArray


    @property
    def floatObject(self):
        return self.__floatObject

    @floatObject.setter
    def floatObject(self, floatObject: str):
        self.__floatObject = floatObject


    @property
    def double(self):
        return self.__double

    @double.setter
    def double(self, double: float):
        self.__double = double


    @property
    def byteObject(self):
        return self.__byteObject

    @byteObject.setter
    def byteObject(self, byteObject: str):
        self.__byteObject = byteObject


    @property
    def bigInteger(self):
        return self.__bigInteger

    @bigInteger.setter
    def bigInteger(self, bigInteger: str):
        self.__bigInteger = bigInteger


    @property
    def doubleObject(self):
        return self.__doubleObject

    @doubleObject.setter
    def doubleObject(self, doubleObject: str):
        self.__doubleObject = doubleObject


    @property
    def byte(self):
        return self.__byte

    @byte.setter
    def byte(self, byte: str):
        self.__byte = byte


    @property
    def longObject(self):
        return self.__longObject

    @longObject.setter
    def longObject(self, longObject: str):
        self.__longObject = longObject


    @property
    def longArray(self):
        return self.__longArray

    @longArray.setter
    def longArray(self, longArray: str):
        self.__longArray = longArray


    @property
    def nextEnum(self):
        return self.__nextEnum

    @nextEnum.setter
    def nextEnum(self, nextEnum: str):
        self.__nextEnum = nextEnum


    @property
    def byteArray(self):
        return self.__byteArray

    @byteArray.setter
    def byteArray(self, byteArray: str):
        self.__byteArray = byteArray

