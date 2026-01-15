from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class attributeTest_Root:

    def __init__(self, shortPrimitive: str, bigDecimal: str, bigInteger: str, boolPrimitive: bool, boolObj: str, bytePrimitive: str, byteObj: str, byteArray: str, charPrimitive: str, charObj: str, doublePrimitive: float, doubleObj: str, floatPrimitive: float, floatObj: str, intPrimitive: int, intObj: str, javaObject: str, longPrimitive: str, longObj: str, shortObj: str, eList: str, date: date, stringObj: str, listString: str, listInt: int, listShort: str, listInt1: int, listInt2: int, map: str):
        self.shortPrimitive = shortPrimitive
        self.bigDecimal = bigDecimal
        self.bigInteger = bigInteger
        self.boolPrimitive = boolPrimitive
        self.boolObj = boolObj
        self.bytePrimitive = bytePrimitive
        self.byteObj = byteObj
        self.byteArray = byteArray
        self.charPrimitive = charPrimitive
        self.charObj = charObj
        self.doublePrimitive = doublePrimitive
        self.doubleObj = doubleObj
        self.floatPrimitive = floatPrimitive
        self.floatObj = floatObj
        self.intPrimitive = intPrimitive
        self.intObj = intObj
        self.javaObject = javaObject
        self.longPrimitive = longPrimitive
        self.longObj = longObj
        self.shortObj = shortObj
        self.eList = eList
        self.date = date
        self.stringObj = stringObj
        self.listString = listString
        self.listInt = listInt
        self.listShort = listShort
        self.listInt1 = listInt1
        self.listInt2 = listInt2
        self.map = map
        
    @property
    def longPrimitive(self) -> str:
        return self.__longPrimitive

    @longPrimitive.setter
    def longPrimitive(self, longPrimitive: str):
        self.__longPrimitive = longPrimitive

    @property
    def listInt1(self) -> int:
        return self.__listInt1

    @listInt1.setter
    def listInt1(self, listInt1: int):
        self.__listInt1 = listInt1

    @property
    def byteObj(self) -> str:
        return self.__byteObj

    @byteObj.setter
    def byteObj(self, byteObj: str):
        self.__byteObj = byteObj

    @property
    def bigInteger(self) -> str:
        return self.__bigInteger

    @bigInteger.setter
    def bigInteger(self, bigInteger: str):
        self.__bigInteger = bigInteger

    @property
    def javaObject(self) -> str:
        return self.__javaObject

    @javaObject.setter
    def javaObject(self, javaObject: str):
        self.__javaObject = javaObject

    @property
    def stringObj(self) -> str:
        return self.__stringObj

    @stringObj.setter
    def stringObj(self, stringObj: str):
        self.__stringObj = stringObj

    @property
    def listString(self) -> str:
        return self.__listString

    @listString.setter
    def listString(self, listString: str):
        self.__listString = listString

    @property
    def doubleObj(self) -> str:
        return self.__doubleObj

    @doubleObj.setter
    def doubleObj(self, doubleObj: str):
        self.__doubleObj = doubleObj

    @property
    def charPrimitive(self) -> str:
        return self.__charPrimitive

    @charPrimitive.setter
    def charPrimitive(self, charPrimitive: str):
        self.__charPrimitive = charPrimitive

    @property
    def shortObj(self) -> str:
        return self.__shortObj

    @shortObj.setter
    def shortObj(self, shortObj: str):
        self.__shortObj = shortObj

    @property
    def listShort(self) -> str:
        return self.__listShort

    @listShort.setter
    def listShort(self, listShort: str):
        self.__listShort = listShort

    @property
    def map(self) -> str:
        return self.__map

    @map.setter
    def map(self, map: str):
        self.__map = map

    @property
    def floatPrimitive(self) -> float:
        return self.__floatPrimitive

    @floatPrimitive.setter
    def floatPrimitive(self, floatPrimitive: float):
        self.__floatPrimitive = floatPrimitive

    @property
    def intObj(self) -> str:
        return self.__intObj

    @intObj.setter
    def intObj(self, intObj: str):
        self.__intObj = intObj

    @property
    def listInt(self) -> int:
        return self.__listInt

    @listInt.setter
    def listInt(self, listInt: int):
        self.__listInt = listInt

    @property
    def longObj(self) -> str:
        return self.__longObj

    @longObj.setter
    def longObj(self, longObj: str):
        self.__longObj = longObj

    @property
    def date(self) -> date:
        return self.__date

    @date.setter
    def date(self, date: date):
        self.__date = date

    @property
    def boolPrimitive(self) -> bool:
        return self.__boolPrimitive

    @boolPrimitive.setter
    def boolPrimitive(self, boolPrimitive: bool):
        self.__boolPrimitive = boolPrimitive

    @property
    def boolObj(self) -> str:
        return self.__boolObj

    @boolObj.setter
    def boolObj(self, boolObj: str):
        self.__boolObj = boolObj

    @property
    def shortPrimitive(self) -> str:
        return self.__shortPrimitive

    @shortPrimitive.setter
    def shortPrimitive(self, shortPrimitive: str):
        self.__shortPrimitive = shortPrimitive

    @property
    def intPrimitive(self) -> int:
        return self.__intPrimitive

    @intPrimitive.setter
    def intPrimitive(self, intPrimitive: int):
        self.__intPrimitive = intPrimitive

    @property
    def eList(self) -> str:
        return self.__eList

    @eList.setter
    def eList(self, eList: str):
        self.__eList = eList

    @property
    def floatObj(self) -> str:
        return self.__floatObj

    @floatObj.setter
    def floatObj(self, floatObj: str):
        self.__floatObj = floatObj

    @property
    def bytePrimitive(self) -> str:
        return self.__bytePrimitive

    @bytePrimitive.setter
    def bytePrimitive(self, bytePrimitive: str):
        self.__bytePrimitive = bytePrimitive

    @property
    def bigDecimal(self) -> str:
        return self.__bigDecimal

    @bigDecimal.setter
    def bigDecimal(self, bigDecimal: str):
        self.__bigDecimal = bigDecimal

    @property
    def listInt2(self) -> int:
        return self.__listInt2

    @listInt2.setter
    def listInt2(self, listInt2: int):
        self.__listInt2 = listInt2

    @property
    def byteArray(self) -> str:
        return self.__byteArray

    @byteArray.setter
    def byteArray(self, byteArray: str):
        self.__byteArray = byteArray

    @property
    def charObj(self) -> str:
        return self.__charObj

    @charObj.setter
    def charObj(self, charObj: str):
        self.__charObj = charObj

    @property
    def doublePrimitive(self) -> float:
        return self.__doublePrimitive

    @doublePrimitive.setter
    def doublePrimitive(self, doublePrimitive: float):
        self.__doublePrimitive = doublePrimitive
