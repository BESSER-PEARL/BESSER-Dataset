from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class TestEnumeration(Enum):
    TestLiteral1 = "TestLiteral1"
    TestLiteral2 = "TestLiteral2"


############################################
# Definition of Classes
############################################

class package1_TestPropertyClass:

    def __init__(self, identifierProperty: str, nonidentifierProperty: str, package1_TestPropertyClass: "package1_TestTypeClass1" = None, package1_TestPropertyClass2: set["package1_TestTypeClass1"] = None, package1_TestPropertyClass5: set["package1_TestTypeClass1"] = None, package1_TestPropertyClass8: set["package1_TestTypeClass1"] = None, package1_TestPropertyClass11: set["package1_TestTypeClass1"] = None, package1_TestPropertyClass14: "package1_TestTypeClass1" = None, package1_TestPropertyClass17: set["package1_TestTypeClass1"] = None, package1_TestPropertyClass20: set["package1_TestTypeClass1"] = None, package1_TestPropertyClass23: set["package1_TestTypeClass1"] = None, package1_TestPropertyClass26: set["package1_TestTypeClass1"] = None):
        self.identifierProperty = identifierProperty
        self.nonidentifierProperty = nonidentifierProperty
        self.package1_TestPropertyClass = package1_TestPropertyClass
        self.package1_TestPropertyClass2 = package1_TestPropertyClass2 if package1_TestPropertyClass2 is not None else set()
        self.package1_TestPropertyClass5 = package1_TestPropertyClass5 if package1_TestPropertyClass5 is not None else set()
        self.package1_TestPropertyClass8 = package1_TestPropertyClass8 if package1_TestPropertyClass8 is not None else set()
        self.package1_TestPropertyClass11 = package1_TestPropertyClass11 if package1_TestPropertyClass11 is not None else set()
        self.package1_TestPropertyClass14 = package1_TestPropertyClass14
        self.package1_TestPropertyClass17 = package1_TestPropertyClass17 if package1_TestPropertyClass17 is not None else set()
        self.package1_TestPropertyClass20 = package1_TestPropertyClass20 if package1_TestPropertyClass20 is not None else set()
        self.package1_TestPropertyClass23 = package1_TestPropertyClass23 if package1_TestPropertyClass23 is not None else set()
        self.package1_TestPropertyClass26 = package1_TestPropertyClass26 if package1_TestPropertyClass26 is not None else set()
        
    @property
    def identifierProperty(self) -> str:
        return self.__identifierProperty

    @identifierProperty.setter
    def identifierProperty(self, identifierProperty: str):
        self.__identifierProperty = identifierProperty

    @property
    def nonidentifierProperty(self) -> str:
        return self.__nonidentifierProperty

    @nonidentifierProperty.setter
    def nonidentifierProperty(self, nonidentifierProperty: str):
        self.__nonidentifierProperty = nonidentifierProperty

    @property
    def package1_TestPropertyClass23(self):
        return self.__package1_TestPropertyClass23

    @package1_TestPropertyClass23.setter
    def package1_TestPropertyClass23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_package1_TestPropertyClass__package1_TestPropertyClass23", None)
        self.__package1_TestPropertyClass23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "package1_TestTypeClass124"):
                    opp_val = getattr(item, "package1_TestTypeClass124", None)
                    
                    if opp_val == self:
                        setattr(item, "package1_TestTypeClass124", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "package1_TestTypeClass124"):
                    opp_val = getattr(item, "package1_TestTypeClass124", None)
                    
                    setattr(item, "package1_TestTypeClass124", self)
                    

    @property
    def package1_TestPropertyClass5(self):
        return self.__package1_TestPropertyClass5

    @package1_TestPropertyClass5.setter
    def package1_TestPropertyClass5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_package1_TestPropertyClass__package1_TestPropertyClass5", None)
        self.__package1_TestPropertyClass5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "package1_TestTypeClass16"):
                    opp_val = getattr(item, "package1_TestTypeClass16", None)
                    
                    if opp_val == self:
                        setattr(item, "package1_TestTypeClass16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "package1_TestTypeClass16"):
                    opp_val = getattr(item, "package1_TestTypeClass16", None)
                    
                    setattr(item, "package1_TestTypeClass16", self)
                    

    @property
    def package1_TestPropertyClass26(self):
        return self.__package1_TestPropertyClass26

    @package1_TestPropertyClass26.setter
    def package1_TestPropertyClass26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_package1_TestPropertyClass__package1_TestPropertyClass26", None)
        self.__package1_TestPropertyClass26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "package1_TestTypeClass127"):
                    opp_val = getattr(item, "package1_TestTypeClass127", None)
                    
                    if opp_val == self:
                        setattr(item, "package1_TestTypeClass127", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "package1_TestTypeClass127"):
                    opp_val = getattr(item, "package1_TestTypeClass127", None)
                    
                    setattr(item, "package1_TestTypeClass127", self)
                    

    @property
    def package1_TestPropertyClass8(self):
        return self.__package1_TestPropertyClass8

    @package1_TestPropertyClass8.setter
    def package1_TestPropertyClass8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_package1_TestPropertyClass__package1_TestPropertyClass8", None)
        self.__package1_TestPropertyClass8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "package1_TestTypeClass19"):
                    opp_val = getattr(item, "package1_TestTypeClass19", None)
                    
                    if opp_val == self:
                        setattr(item, "package1_TestTypeClass19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "package1_TestTypeClass19"):
                    opp_val = getattr(item, "package1_TestTypeClass19", None)
                    
                    setattr(item, "package1_TestTypeClass19", self)
                    

    @property
    def package1_TestPropertyClass20(self):
        return self.__package1_TestPropertyClass20

    @package1_TestPropertyClass20.setter
    def package1_TestPropertyClass20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_package1_TestPropertyClass__package1_TestPropertyClass20", None)
        self.__package1_TestPropertyClass20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "package1_TestTypeClass121"):
                    opp_val = getattr(item, "package1_TestTypeClass121", None)
                    
                    if opp_val == self:
                        setattr(item, "package1_TestTypeClass121", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "package1_TestTypeClass121"):
                    opp_val = getattr(item, "package1_TestTypeClass121", None)
                    
                    setattr(item, "package1_TestTypeClass121", self)
                    

    @property
    def package1_TestPropertyClass17(self):
        return self.__package1_TestPropertyClass17

    @package1_TestPropertyClass17.setter
    def package1_TestPropertyClass17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_package1_TestPropertyClass__package1_TestPropertyClass17", None)
        self.__package1_TestPropertyClass17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "package1_TestTypeClass118"):
                    opp_val = getattr(item, "package1_TestTypeClass118", None)
                    
                    if opp_val == self:
                        setattr(item, "package1_TestTypeClass118", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "package1_TestTypeClass118"):
                    opp_val = getattr(item, "package1_TestTypeClass118", None)
                    
                    setattr(item, "package1_TestTypeClass118", self)
                    

    @property
    def package1_TestPropertyClass11(self):
        return self.__package1_TestPropertyClass11

    @package1_TestPropertyClass11.setter
    def package1_TestPropertyClass11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_package1_TestPropertyClass__package1_TestPropertyClass11", None)
        self.__package1_TestPropertyClass11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "package1_TestTypeClass112"):
                    opp_val = getattr(item, "package1_TestTypeClass112", None)
                    
                    if opp_val == self:
                        setattr(item, "package1_TestTypeClass112", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "package1_TestTypeClass112"):
                    opp_val = getattr(item, "package1_TestTypeClass112", None)
                    
                    setattr(item, "package1_TestTypeClass112", self)
                    

    @property
    def package1_TestPropertyClass2(self):
        return self.__package1_TestPropertyClass2

    @package1_TestPropertyClass2.setter
    def package1_TestPropertyClass2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_package1_TestPropertyClass__package1_TestPropertyClass2", None)
        self.__package1_TestPropertyClass2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "package1_TestTypeClass13"):
                    opp_val = getattr(item, "package1_TestTypeClass13", None)
                    
                    if opp_val == self:
                        setattr(item, "package1_TestTypeClass13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "package1_TestTypeClass13"):
                    opp_val = getattr(item, "package1_TestTypeClass13", None)
                    
                    setattr(item, "package1_TestTypeClass13", self)
                    

    @property
    def package1_TestPropertyClass14(self):
        return self.__package1_TestPropertyClass14

    @package1_TestPropertyClass14.setter
    def package1_TestPropertyClass14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_package1_TestPropertyClass__package1_TestPropertyClass14", None)
        self.__package1_TestPropertyClass14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "package1_TestTypeClass115"):
                opp_val = getattr(old_value, "package1_TestTypeClass115", None)
                if opp_val == self:
                    setattr(old_value, "package1_TestTypeClass115", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "package1_TestTypeClass115"):
                opp_val = getattr(value, "package1_TestTypeClass115", None)
                setattr(value, "package1_TestTypeClass115", self)

    @property
    def package1_TestPropertyClass(self):
        return self.__package1_TestPropertyClass

    @package1_TestPropertyClass.setter
    def package1_TestPropertyClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_package1_TestPropertyClass__package1_TestPropertyClass", None)
        self.__package1_TestPropertyClass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "package1_TestTypeClass1"):
                opp_val = getattr(old_value, "package1_TestTypeClass1", None)
                if opp_val == self:
                    setattr(old_value, "package1_TestTypeClass1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "package1_TestTypeClass1"):
                opp_val = getattr(value, "package1_TestTypeClass1", None)
                setattr(value, "package1_TestTypeClass1", self)

class package1_TestPrimitiveTypeClass:

    def __init__(self, anIntegerBigDecimal: str, aRealFloat: str, aRealFloatObject: str, aRealDouble: str, aRealDoubleObject: str, aBooleanBoolean: str, aBooleanBooleanObject: str, aStringChar: str, aStringCharacterObject: str, aStringString: str, anIntegerEByte: str, anIntegerEByteObject: str, anIntegerEShort: str, anIntegerEShortObject: str, anIntegerEInt: int, anIntegerEIntegerObject: str, anIntegerELong: str, anIntegerELongObject: str, anIntegerEBigInteger: str, anIntegerEBigDecimal: str, aRealEFloat: float, aRealEFloatObject: str, aRealEDouble: float, aRealEDoubleObject: str, aBooleanEBoolean: bool, aBooleanEBooleanObject: str, aStringEChar: str, aStringECharacterObject: str, aStringEString: str, anIntegerByte: str, anIntegerByteObject: str, anIntegerShort: str, anIntegerShortObject: str, anIntegerInt: str, anIntegerIntegerObject: str, anIntegerLong: str, anIntegerLongObject: str, anIntegerBigInteger: str):
        self.anIntegerBigDecimal = anIntegerBigDecimal
        self.aRealFloat = aRealFloat
        self.aRealFloatObject = aRealFloatObject
        self.aRealDouble = aRealDouble
        self.aRealDoubleObject = aRealDoubleObject
        self.aBooleanBoolean = aBooleanBoolean
        self.aBooleanBooleanObject = aBooleanBooleanObject
        self.aStringChar = aStringChar
        self.aStringCharacterObject = aStringCharacterObject
        self.aStringString = aStringString
        self.anIntegerEByte = anIntegerEByte
        self.anIntegerEByteObject = anIntegerEByteObject
        self.anIntegerEShort = anIntegerEShort
        self.anIntegerEShortObject = anIntegerEShortObject
        self.anIntegerEInt = anIntegerEInt
        self.anIntegerEIntegerObject = anIntegerEIntegerObject
        self.anIntegerELong = anIntegerELong
        self.anIntegerELongObject = anIntegerELongObject
        self.anIntegerEBigInteger = anIntegerEBigInteger
        self.anIntegerEBigDecimal = anIntegerEBigDecimal
        self.aRealEFloat = aRealEFloat
        self.aRealEFloatObject = aRealEFloatObject
        self.aRealEDouble = aRealEDouble
        self.aRealEDoubleObject = aRealEDoubleObject
        self.aBooleanEBoolean = aBooleanEBoolean
        self.aBooleanEBooleanObject = aBooleanEBooleanObject
        self.aStringEChar = aStringEChar
        self.aStringECharacterObject = aStringECharacterObject
        self.aStringEString = aStringEString
        self.anIntegerByte = anIntegerByte
        self.anIntegerByteObject = anIntegerByteObject
        self.anIntegerShort = anIntegerShort
        self.anIntegerShortObject = anIntegerShortObject
        self.anIntegerInt = anIntegerInt
        self.anIntegerIntegerObject = anIntegerIntegerObject
        self.anIntegerLong = anIntegerLong
        self.anIntegerLongObject = anIntegerLongObject
        self.anIntegerBigInteger = anIntegerBigInteger
        
    @property
    def anIntegerEByteObject(self) -> str:
        return self.__anIntegerEByteObject

    @anIntegerEByteObject.setter
    def anIntegerEByteObject(self, anIntegerEByteObject: str):
        self.__anIntegerEByteObject = anIntegerEByteObject

    @property
    def aStringCharacterObject(self) -> str:
        return self.__aStringCharacterObject

    @aStringCharacterObject.setter
    def aStringCharacterObject(self, aStringCharacterObject: str):
        self.__aStringCharacterObject = aStringCharacterObject

    @property
    def aStringChar(self) -> str:
        return self.__aStringChar

    @aStringChar.setter
    def aStringChar(self, aStringChar: str):
        self.__aStringChar = aStringChar

    @property
    def anIntegerIntegerObject(self) -> str:
        return self.__anIntegerIntegerObject

    @anIntegerIntegerObject.setter
    def anIntegerIntegerObject(self, anIntegerIntegerObject: str):
        self.__anIntegerIntegerObject = anIntegerIntegerObject

    @property
    def anIntegerBigInteger(self) -> str:
        return self.__anIntegerBigInteger

    @anIntegerBigInteger.setter
    def anIntegerBigInteger(self, anIntegerBigInteger: str):
        self.__anIntegerBigInteger = anIntegerBigInteger

    @property
    def aRealFloat(self) -> str:
        return self.__aRealFloat

    @aRealFloat.setter
    def aRealFloat(self, aRealFloat: str):
        self.__aRealFloat = aRealFloat

    @property
    def aStringString(self) -> str:
        return self.__aStringString

    @aStringString.setter
    def aStringString(self, aStringString: str):
        self.__aStringString = aStringString

    @property
    def aRealFloatObject(self) -> str:
        return self.__aRealFloatObject

    @aRealFloatObject.setter
    def aRealFloatObject(self, aRealFloatObject: str):
        self.__aRealFloatObject = aRealFloatObject

    @property
    def aBooleanBooleanObject(self) -> str:
        return self.__aBooleanBooleanObject

    @aBooleanBooleanObject.setter
    def aBooleanBooleanObject(self, aBooleanBooleanObject: str):
        self.__aBooleanBooleanObject = aBooleanBooleanObject

    @property
    def aRealEFloatObject(self) -> str:
        return self.__aRealEFloatObject

    @aRealEFloatObject.setter
    def aRealEFloatObject(self, aRealEFloatObject: str):
        self.__aRealEFloatObject = aRealEFloatObject

    @property
    def anIntegerEBigDecimal(self) -> str:
        return self.__anIntegerEBigDecimal

    @anIntegerEBigDecimal.setter
    def anIntegerEBigDecimal(self, anIntegerEBigDecimal: str):
        self.__anIntegerEBigDecimal = anIntegerEBigDecimal

    @property
    def anIntegerEShort(self) -> str:
        return self.__anIntegerEShort

    @anIntegerEShort.setter
    def anIntegerEShort(self, anIntegerEShort: str):
        self.__anIntegerEShort = anIntegerEShort

    @property
    def anIntegerShort(self) -> str:
        return self.__anIntegerShort

    @anIntegerShort.setter
    def anIntegerShort(self, anIntegerShort: str):
        self.__anIntegerShort = anIntegerShort

    @property
    def anIntegerEByte(self) -> str:
        return self.__anIntegerEByte

    @anIntegerEByte.setter
    def anIntegerEByte(self, anIntegerEByte: str):
        self.__anIntegerEByte = anIntegerEByte

    @property
    def anIntegerLongObject(self) -> str:
        return self.__anIntegerLongObject

    @anIntegerLongObject.setter
    def anIntegerLongObject(self, anIntegerLongObject: str):
        self.__anIntegerLongObject = anIntegerLongObject

    @property
    def aStringEString(self) -> str:
        return self.__aStringEString

    @aStringEString.setter
    def aStringEString(self, aStringEString: str):
        self.__aStringEString = aStringEString

    @property
    def anIntegerInt(self) -> str:
        return self.__anIntegerInt

    @anIntegerInt.setter
    def anIntegerInt(self, anIntegerInt: str):
        self.__anIntegerInt = anIntegerInt

    @property
    def aRealDouble(self) -> str:
        return self.__aRealDouble

    @aRealDouble.setter
    def aRealDouble(self, aRealDouble: str):
        self.__aRealDouble = aRealDouble

    @property
    def aStringEChar(self) -> str:
        return self.__aStringEChar

    @aStringEChar.setter
    def aStringEChar(self, aStringEChar: str):
        self.__aStringEChar = aStringEChar

    @property
    def anIntegerLong(self) -> str:
        return self.__anIntegerLong

    @anIntegerLong.setter
    def anIntegerLong(self, anIntegerLong: str):
        self.__anIntegerLong = anIntegerLong

    @property
    def aRealDoubleObject(self) -> str:
        return self.__aRealDoubleObject

    @aRealDoubleObject.setter
    def aRealDoubleObject(self, aRealDoubleObject: str):
        self.__aRealDoubleObject = aRealDoubleObject

    @property
    def anIntegerBigDecimal(self) -> str:
        return self.__anIntegerBigDecimal

    @anIntegerBigDecimal.setter
    def anIntegerBigDecimal(self, anIntegerBigDecimal: str):
        self.__anIntegerBigDecimal = anIntegerBigDecimal

    @property
    def aRealEDouble(self) -> float:
        return self.__aRealEDouble

    @aRealEDouble.setter
    def aRealEDouble(self, aRealEDouble: float):
        self.__aRealEDouble = aRealEDouble

    @property
    def anIntegerEInt(self) -> int:
        return self.__anIntegerEInt

    @anIntegerEInt.setter
    def anIntegerEInt(self, anIntegerEInt: int):
        self.__anIntegerEInt = anIntegerEInt

    @property
    def aBooleanEBoolean(self) -> bool:
        return self.__aBooleanEBoolean

    @aBooleanEBoolean.setter
    def aBooleanEBoolean(self, aBooleanEBoolean: bool):
        self.__aBooleanEBoolean = aBooleanEBoolean

    @property
    def anIntegerEShortObject(self) -> str:
        return self.__anIntegerEShortObject

    @anIntegerEShortObject.setter
    def anIntegerEShortObject(self, anIntegerEShortObject: str):
        self.__anIntegerEShortObject = anIntegerEShortObject

    @property
    def aBooleanBoolean(self) -> str:
        return self.__aBooleanBoolean

    @aBooleanBoolean.setter
    def aBooleanBoolean(self, aBooleanBoolean: str):
        self.__aBooleanBoolean = aBooleanBoolean

    @property
    def anIntegerByte(self) -> str:
        return self.__anIntegerByte

    @anIntegerByte.setter
    def anIntegerByte(self, anIntegerByte: str):
        self.__anIntegerByte = anIntegerByte

    @property
    def aRealEFloat(self) -> float:
        return self.__aRealEFloat

    @aRealEFloat.setter
    def aRealEFloat(self, aRealEFloat: float):
        self.__aRealEFloat = aRealEFloat

    @property
    def anIntegerShortObject(self) -> str:
        return self.__anIntegerShortObject

    @anIntegerShortObject.setter
    def anIntegerShortObject(self, anIntegerShortObject: str):
        self.__anIntegerShortObject = anIntegerShortObject

    @property
    def aBooleanEBooleanObject(self) -> str:
        return self.__aBooleanEBooleanObject

    @aBooleanEBooleanObject.setter
    def aBooleanEBooleanObject(self, aBooleanEBooleanObject: str):
        self.__aBooleanEBooleanObject = aBooleanEBooleanObject

    @property
    def anIntegerEIntegerObject(self) -> str:
        return self.__anIntegerEIntegerObject

    @anIntegerEIntegerObject.setter
    def anIntegerEIntegerObject(self, anIntegerEIntegerObject: str):
        self.__anIntegerEIntegerObject = anIntegerEIntegerObject

    @property
    def aStringECharacterObject(self) -> str:
        return self.__aStringECharacterObject

    @aStringECharacterObject.setter
    def aStringECharacterObject(self, aStringECharacterObject: str):
        self.__aStringECharacterObject = aStringECharacterObject

    @property
    def aRealEDoubleObject(self) -> str:
        return self.__aRealEDoubleObject

    @aRealEDoubleObject.setter
    def aRealEDoubleObject(self, aRealEDoubleObject: str):
        self.__aRealEDoubleObject = aRealEDoubleObject

    @property
    def anIntegerEBigInteger(self) -> str:
        return self.__anIntegerEBigInteger

    @anIntegerEBigInteger.setter
    def anIntegerEBigInteger(self, anIntegerEBigInteger: str):
        self.__anIntegerEBigInteger = anIntegerEBigInteger

    @property
    def anIntegerELong(self) -> str:
        return self.__anIntegerELong

    @anIntegerELong.setter
    def anIntegerELong(self, anIntegerELong: str):
        self.__anIntegerELong = anIntegerELong

    @property
    def anIntegerELongObject(self) -> str:
        return self.__anIntegerELongObject

    @anIntegerELongObject.setter
    def anIntegerELongObject(self, anIntegerELongObject: str):
        self.__anIntegerELongObject = anIntegerELongObject

    @property
    def anIntegerByteObject(self) -> str:
        return self.__anIntegerByteObject

    @anIntegerByteObject.setter
    def anIntegerByteObject(self, anIntegerByteObject: str):
        self.__anIntegerByteObject = anIntegerByteObject

class package1_TestOperationAndParameterClass:

    def __init__(self):
        
    def unorderedMultipleOperation(self) -> TestTypeClass1:
        # TODO: Implement unorderedMultipleOperation method
        pass

    def nonuniqueMultipleOperation(self) -> TestTypeClass1:
        # TODO: Implement nonuniqueMultipleOperation method
        pass

    def orderedMultipleOperation(self) -> TestTypeClass1:
        # TODO: Implement orderedMultipleOperation method
        pass

    def operationWithoutParameters(self) -> TestTypeClass1:
        # TODO: Implement operationWithoutParameters method
        pass

    def uniqueMultipleOperation(self) -> TestTypeClass1:
        # TODO: Implement uniqueMultipleOperation method
        pass

    def voidOperationWithParameter(self, in1: TestTypeClass1):
        # TODO: Implement voidOperationWithParameter method
        pass

class TestTypeClass1:

    pass
class package1_TestTypeClass2(TestTypeClass1):

    def __init__(self, property2: bool):
        self.property2 = property2
        
    @property
    def property2(self) -> bool:
        return self.__property2

    @property2.setter
    def property2(self, property2: bool):
        self.__property2 = property2

    def operation2(self):
        # TODO: Implement operation2 method
        pass

class package1_TestTypeClass1:

    def __init__(self, property1: bool, package1_TestTypeClass1: "package1_TestPropertyClass" = None, package1_TestTypeClass13: "package1_TestPropertyClass" = None, package1_TestTypeClass16: "package1_TestPropertyClass" = None, package1_TestTypeClass19: "package1_TestPropertyClass" = None, package1_TestTypeClass112: "package1_TestPropertyClass" = None, package1_TestTypeClass115: "package1_TestPropertyClass" = None, package1_TestTypeClass118: "package1_TestPropertyClass" = None, package1_TestTypeClass121: "package1_TestPropertyClass" = None, package1_TestTypeClass124: "package1_TestPropertyClass" = None, package1_TestTypeClass127: "package1_TestPropertyClass" = None):
        self.property1 = property1
        self.package1_TestTypeClass1 = package1_TestTypeClass1
        self.package1_TestTypeClass13 = package1_TestTypeClass13
        self.package1_TestTypeClass16 = package1_TestTypeClass16
        self.package1_TestTypeClass19 = package1_TestTypeClass19
        self.package1_TestTypeClass112 = package1_TestTypeClass112
        self.package1_TestTypeClass115 = package1_TestTypeClass115
        self.package1_TestTypeClass118 = package1_TestTypeClass118
        self.package1_TestTypeClass121 = package1_TestTypeClass121
        self.package1_TestTypeClass124 = package1_TestTypeClass124
        self.package1_TestTypeClass127 = package1_TestTypeClass127
        
    @property
    def property1(self) -> bool:
        return self.__property1

    @property1.setter
    def property1(self, property1: bool):
        self.__property1 = property1

    @property
    def package1_TestTypeClass118(self):
        return self.__package1_TestTypeClass118

    @package1_TestTypeClass118.setter
    def package1_TestTypeClass118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_package1_TestTypeClass1__package1_TestTypeClass118", None)
        self.__package1_TestTypeClass118 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "package1_TestPropertyClass17"):
                opp_val = getattr(old_value, "package1_TestPropertyClass17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "package1_TestPropertyClass17"):
                opp_val = getattr(value, "package1_TestPropertyClass17", None)
                if opp_val is None:
                    setattr(value, "package1_TestPropertyClass17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def package1_TestTypeClass127(self):
        return self.__package1_TestTypeClass127

    @package1_TestTypeClass127.setter
    def package1_TestTypeClass127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_package1_TestTypeClass1__package1_TestTypeClass127", None)
        self.__package1_TestTypeClass127 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "package1_TestPropertyClass26"):
                opp_val = getattr(old_value, "package1_TestPropertyClass26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "package1_TestPropertyClass26"):
                opp_val = getattr(value, "package1_TestPropertyClass26", None)
                if opp_val is None:
                    setattr(value, "package1_TestPropertyClass26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def package1_TestTypeClass124(self):
        return self.__package1_TestTypeClass124

    @package1_TestTypeClass124.setter
    def package1_TestTypeClass124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_package1_TestTypeClass1__package1_TestTypeClass124", None)
        self.__package1_TestTypeClass124 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "package1_TestPropertyClass23"):
                opp_val = getattr(old_value, "package1_TestPropertyClass23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "package1_TestPropertyClass23"):
                opp_val = getattr(value, "package1_TestPropertyClass23", None)
                if opp_val is None:
                    setattr(value, "package1_TestPropertyClass23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def package1_TestTypeClass1(self):
        return self.__package1_TestTypeClass1

    @package1_TestTypeClass1.setter
    def package1_TestTypeClass1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_package1_TestTypeClass1__package1_TestTypeClass1", None)
        self.__package1_TestTypeClass1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "package1_TestPropertyClass"):
                opp_val = getattr(old_value, "package1_TestPropertyClass", None)
                if opp_val == self:
                    setattr(old_value, "package1_TestPropertyClass", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "package1_TestPropertyClass"):
                opp_val = getattr(value, "package1_TestPropertyClass", None)
                setattr(value, "package1_TestPropertyClass", self)

    @property
    def package1_TestTypeClass112(self):
        return self.__package1_TestTypeClass112

    @package1_TestTypeClass112.setter
    def package1_TestTypeClass112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_package1_TestTypeClass1__package1_TestTypeClass112", None)
        self.__package1_TestTypeClass112 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "package1_TestPropertyClass11"):
                opp_val = getattr(old_value, "package1_TestPropertyClass11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "package1_TestPropertyClass11"):
                opp_val = getattr(value, "package1_TestPropertyClass11", None)
                if opp_val is None:
                    setattr(value, "package1_TestPropertyClass11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def package1_TestTypeClass115(self):
        return self.__package1_TestTypeClass115

    @package1_TestTypeClass115.setter
    def package1_TestTypeClass115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_package1_TestTypeClass1__package1_TestTypeClass115", None)
        self.__package1_TestTypeClass115 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "package1_TestPropertyClass14"):
                opp_val = getattr(old_value, "package1_TestPropertyClass14", None)
                if opp_val == self:
                    setattr(old_value, "package1_TestPropertyClass14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "package1_TestPropertyClass14"):
                opp_val = getattr(value, "package1_TestPropertyClass14", None)
                setattr(value, "package1_TestPropertyClass14", self)

    @property
    def package1_TestTypeClass16(self):
        return self.__package1_TestTypeClass16

    @package1_TestTypeClass16.setter
    def package1_TestTypeClass16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_package1_TestTypeClass1__package1_TestTypeClass16", None)
        self.__package1_TestTypeClass16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "package1_TestPropertyClass5"):
                opp_val = getattr(old_value, "package1_TestPropertyClass5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "package1_TestPropertyClass5"):
                opp_val = getattr(value, "package1_TestPropertyClass5", None)
                if opp_val is None:
                    setattr(value, "package1_TestPropertyClass5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def package1_TestTypeClass121(self):
        return self.__package1_TestTypeClass121

    @package1_TestTypeClass121.setter
    def package1_TestTypeClass121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_package1_TestTypeClass1__package1_TestTypeClass121", None)
        self.__package1_TestTypeClass121 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "package1_TestPropertyClass20"):
                opp_val = getattr(old_value, "package1_TestPropertyClass20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "package1_TestPropertyClass20"):
                opp_val = getattr(value, "package1_TestPropertyClass20", None)
                if opp_val is None:
                    setattr(value, "package1_TestPropertyClass20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def package1_TestTypeClass19(self):
        return self.__package1_TestTypeClass19

    @package1_TestTypeClass19.setter
    def package1_TestTypeClass19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_package1_TestTypeClass1__package1_TestTypeClass19", None)
        self.__package1_TestTypeClass19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "package1_TestPropertyClass8"):
                opp_val = getattr(old_value, "package1_TestPropertyClass8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "package1_TestPropertyClass8"):
                opp_val = getattr(value, "package1_TestPropertyClass8", None)
                if opp_val is None:
                    setattr(value, "package1_TestPropertyClass8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def package1_TestTypeClass13(self):
        return self.__package1_TestTypeClass13

    @package1_TestTypeClass13.setter
    def package1_TestTypeClass13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_package1_TestTypeClass1__package1_TestTypeClass13", None)
        self.__package1_TestTypeClass13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "package1_TestPropertyClass2"):
                opp_val = getattr(old_value, "package1_TestPropertyClass2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "package1_TestPropertyClass2"):
                opp_val = getattr(value, "package1_TestPropertyClass2", None)
                if opp_val is None:
                    setattr(value, "package1_TestPropertyClass2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def operation1(self):
        # TODO: Implement operation1 method
        pass
