from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class EnumTestEnum(Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    INCREDIBLE = "INCREDIBLE"


############################################
# Definition of Classes
############################################

class TestCategoryBeanAbstract:

    pass
class dmf_DObject:

    pass
class tests_TestCategoryBeanConcrete(TestCategoryBeanAbstract, dmf_DObject):

    pass
class tests_ExternalTestType:

    pass
class TestCategoryBase:

    pass
class tests_TestCategoryExtends(TestCategoryBase, dmf_DObject):

    def __init__(self, testExtendsProperty: int):
        self.testExtendsProperty = testExtendsProperty
        
    @property
    def testExtendsProperty(self) -> int:
        return self.__testExtendsProperty

    @testExtendsProperty.setter
    def testExtendsProperty(self, testExtendsProperty: int):
        self.__testExtendsProperty = testExtendsProperty

class DObject:

    pass
class tests_TestCrossLinkedParametersWithCalculation(DObject):

    def __init__(self, calcedTrl: float):
        self.calcedTrl = calcedTrl
        
    @property
    def calcedTrl(self) -> float:
        return self.__calcedTrl

    @calcedTrl.setter
    def calcedTrl(self, calcedTrl: float):
        self.__calcedTrl = calcedTrl

class tests_TestParameter(DObject):

    def __init__(self, defaultValue: float, tests_TestParameter: "tests_TestMassParameters" = None):
        self.defaultValue = defaultValue
        self.tests_TestParameter = tests_TestParameter
        
    @property
    def defaultValue(self) -> float:
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: float):
        self.__defaultValue = defaultValue

    @property
    def tests_TestParameter(self):
        return self.__tests_TestParameter

    @tests_TestParameter.setter
    def tests_TestParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tests_TestParameter__tests_TestParameter", None)
        self.__tests_TestParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tests_TestMassParameters"):
                opp_val = getattr(old_value, "tests_TestMassParameters", None)
                if opp_val == self:
                    setattr(old_value, "tests_TestMassParameters", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tests_TestMassParameters"):
                opp_val = getattr(value, "tests_TestMassParameters", None)
                setattr(value, "tests_TestMassParameters", self)

class tests_TestCategoryBeanAbstract(DObject):

    pass
class tests_TestMassParameters(DObject):

    pass
class tests_EReferenceTest(DObject):

    pass
class tests_TestCategoryComposition(DObject):

    pass
class tests_TestCategoryBase(DObject):

    def __init__(self, testBaseProperty: int, tests_TestCategoryBase: "tests_TestCategoryBase" = None, tests_TestCategoryBase13: set["tests_TestCategoryBase"] = None, tests_TestCategoryBase17: "tests_TestCategoryBase" = None, tests_TestCategoryBase15: "tests_TestCategoryBase" = None):
        self.testBaseProperty = testBaseProperty
        self.tests_TestCategoryBase = tests_TestCategoryBase
        self.tests_TestCategoryBase13 = tests_TestCategoryBase13 if tests_TestCategoryBase13 is not None else set()
        self.tests_TestCategoryBase17 = tests_TestCategoryBase17
        self.tests_TestCategoryBase15 = tests_TestCategoryBase15
        
    @property
    def testBaseProperty(self) -> int:
        return self.__testBaseProperty

    @testBaseProperty.setter
    def testBaseProperty(self, testBaseProperty: int):
        self.__testBaseProperty = testBaseProperty

    @property
    def tests_TestCategoryBase17(self):
        return self.__tests_TestCategoryBase17

    @tests_TestCategoryBase17.setter
    def tests_TestCategoryBase17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tests_TestCategoryBase__tests_TestCategoryBase17", None)
        self.__tests_TestCategoryBase17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tests_TestCategoryBase15"):
                opp_val = getattr(old_value, "tests_TestCategoryBase15", None)
                if opp_val == self:
                    setattr(old_value, "tests_TestCategoryBase15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tests_TestCategoryBase15"):
                opp_val = getattr(value, "tests_TestCategoryBase15", None)
                setattr(value, "tests_TestCategoryBase15", self)

    @property
    def tests_TestCategoryBase15(self):
        return self.__tests_TestCategoryBase15

    @tests_TestCategoryBase15.setter
    def tests_TestCategoryBase15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tests_TestCategoryBase__tests_TestCategoryBase15", None)
        self.__tests_TestCategoryBase15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tests_TestCategoryBase17"):
                opp_val = getattr(old_value, "tests_TestCategoryBase17", None)
                if opp_val == self:
                    setattr(old_value, "tests_TestCategoryBase17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tests_TestCategoryBase17"):
                opp_val = getattr(value, "tests_TestCategoryBase17", None)
                setattr(value, "tests_TestCategoryBase17", self)

    @property
    def tests_TestCategoryBase13(self):
        return self.__tests_TestCategoryBase13

    @tests_TestCategoryBase13.setter
    def tests_TestCategoryBase13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tests_TestCategoryBase__tests_TestCategoryBase13", None)
        self.__tests_TestCategoryBase13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tests_TestCategoryBase"):
                    opp_val = getattr(item, "tests_TestCategoryBase", None)
                    
                    if opp_val == self:
                        setattr(item, "tests_TestCategoryBase", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tests_TestCategoryBase"):
                    opp_val = getattr(item, "tests_TestCategoryBase", None)
                    
                    setattr(item, "tests_TestCategoryBase", self)
                    

    @property
    def tests_TestCategoryBase(self):
        return self.__tests_TestCategoryBase

    @tests_TestCategoryBase.setter
    def tests_TestCategoryBase(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tests_TestCategoryBase__tests_TestCategoryBase", None)
        self.__tests_TestCategoryBase = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tests_TestCategoryBase13"):
                opp_val = getattr(old_value, "tests_TestCategoryBase13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tests_TestCategoryBase13"):
                opp_val = getattr(value, "tests_TestCategoryBase13", None)
                if opp_val is None:
                    setattr(value, "tests_TestCategoryBase13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class tests_TestCategoryAllProperty(DObject):

    def __init__(self, testString: str, testInt: int, testFloat: float, testBool: bool, testResource: str, testEnum: str, tests_TestCategoryAllProperty: "tests_TestCategoryComposition" = None, tests_TestCategoryAllProperty2: "tests_TestCategoryReference" = None, tests_TestCategoryAllProperty4: "tests_TestCategoryCompositionArray" = None, tests_TestCategoryAllProperty7: "tests_TestCategoryCompositionArray" = None, tests_TestCategoryAllProperty9: "tests_TestCategoryReferenceArray" = None, tests_TestCategoryAllProperty12: "tests_TestCategoryReferenceArray" = None):
        self.testString = testString
        self.testInt = testInt
        self.testFloat = testFloat
        self.testBool = testBool
        self.testResource = testResource
        self.testEnum = testEnum
        self.tests_TestCategoryAllProperty = tests_TestCategoryAllProperty
        self.tests_TestCategoryAllProperty2 = tests_TestCategoryAllProperty2
        self.tests_TestCategoryAllProperty4 = tests_TestCategoryAllProperty4
        self.tests_TestCategoryAllProperty7 = tests_TestCategoryAllProperty7
        self.tests_TestCategoryAllProperty9 = tests_TestCategoryAllProperty9
        self.tests_TestCategoryAllProperty12 = tests_TestCategoryAllProperty12
        
    @property
    def testBool(self) -> bool:
        return self.__testBool

    @testBool.setter
    def testBool(self, testBool: bool):
        self.__testBool = testBool

    @property
    def testFloat(self) -> float:
        return self.__testFloat

    @testFloat.setter
    def testFloat(self, testFloat: float):
        self.__testFloat = testFloat

    @property
    def testString(self) -> str:
        return self.__testString

    @testString.setter
    def testString(self, testString: str):
        self.__testString = testString

    @property
    def testEnum(self) -> str:
        return self.__testEnum

    @testEnum.setter
    def testEnum(self, testEnum: str):
        self.__testEnum = testEnum

    @property
    def testInt(self) -> int:
        return self.__testInt

    @testInt.setter
    def testInt(self, testInt: int):
        self.__testInt = testInt

    @property
    def testResource(self) -> str:
        return self.__testResource

    @testResource.setter
    def testResource(self, testResource: str):
        self.__testResource = testResource

    @property
    def tests_TestCategoryAllProperty12(self):
        return self.__tests_TestCategoryAllProperty12

    @tests_TestCategoryAllProperty12.setter
    def tests_TestCategoryAllProperty12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tests_TestCategoryAllProperty__tests_TestCategoryAllProperty12", None)
        self.__tests_TestCategoryAllProperty12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tests_TestCategoryReferenceArray11"):
                opp_val = getattr(old_value, "tests_TestCategoryReferenceArray11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tests_TestCategoryReferenceArray11"):
                opp_val = getattr(value, "tests_TestCategoryReferenceArray11", None)
                if opp_val is None:
                    setattr(value, "tests_TestCategoryReferenceArray11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tests_TestCategoryAllProperty9(self):
        return self.__tests_TestCategoryAllProperty9

    @tests_TestCategoryAllProperty9.setter
    def tests_TestCategoryAllProperty9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tests_TestCategoryAllProperty__tests_TestCategoryAllProperty9", None)
        self.__tests_TestCategoryAllProperty9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tests_TestCategoryReferenceArray"):
                opp_val = getattr(old_value, "tests_TestCategoryReferenceArray", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tests_TestCategoryReferenceArray"):
                opp_val = getattr(value, "tests_TestCategoryReferenceArray", None)
                if opp_val is None:
                    setattr(value, "tests_TestCategoryReferenceArray", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tests_TestCategoryAllProperty4(self):
        return self.__tests_TestCategoryAllProperty4

    @tests_TestCategoryAllProperty4.setter
    def tests_TestCategoryAllProperty4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tests_TestCategoryAllProperty__tests_TestCategoryAllProperty4", None)
        self.__tests_TestCategoryAllProperty4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tests_TestCategoryCompositionArray"):
                opp_val = getattr(old_value, "tests_TestCategoryCompositionArray", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tests_TestCategoryCompositionArray"):
                opp_val = getattr(value, "tests_TestCategoryCompositionArray", None)
                if opp_val is None:
                    setattr(value, "tests_TestCategoryCompositionArray", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tests_TestCategoryAllProperty2(self):
        return self.__tests_TestCategoryAllProperty2

    @tests_TestCategoryAllProperty2.setter
    def tests_TestCategoryAllProperty2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tests_TestCategoryAllProperty__tests_TestCategoryAllProperty2", None)
        self.__tests_TestCategoryAllProperty2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tests_TestCategoryReference"):
                opp_val = getattr(old_value, "tests_TestCategoryReference", None)
                if opp_val == self:
                    setattr(old_value, "tests_TestCategoryReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tests_TestCategoryReference"):
                opp_val = getattr(value, "tests_TestCategoryReference", None)
                setattr(value, "tests_TestCategoryReference", self)

    @property
    def tests_TestCategoryAllProperty(self):
        return self.__tests_TestCategoryAllProperty

    @tests_TestCategoryAllProperty.setter
    def tests_TestCategoryAllProperty(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tests_TestCategoryAllProperty__tests_TestCategoryAllProperty", None)
        self.__tests_TestCategoryAllProperty = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tests_TestCategoryComposition"):
                opp_val = getattr(old_value, "tests_TestCategoryComposition", None)
                if opp_val == self:
                    setattr(old_value, "tests_TestCategoryComposition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tests_TestCategoryComposition"):
                opp_val = getattr(value, "tests_TestCategoryComposition", None)
                setattr(value, "tests_TestCategoryComposition", self)

    @property
    def tests_TestCategoryAllProperty7(self):
        return self.__tests_TestCategoryAllProperty7

    @tests_TestCategoryAllProperty7.setter
    def tests_TestCategoryAllProperty7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tests_TestCategoryAllProperty__tests_TestCategoryAllProperty7", None)
        self.__tests_TestCategoryAllProperty7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tests_TestCategoryCompositionArray6"):
                opp_val = getattr(old_value, "tests_TestCategoryCompositionArray6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tests_TestCategoryCompositionArray6"):
                opp_val = getattr(value, "tests_TestCategoryCompositionArray6", None)
                if opp_val is None:
                    setattr(value, "tests_TestCategoryCompositionArray6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class tests_TestCategoryBeanB(DObject):

    pass
class tests_TestCategoryBeanA(DObject):

    pass
class tests_TestCategoryReferenceArray(DObject):

    pass
class tests_TestCategoryCompositionArray(DObject):

    pass
class tests_TestCategoryIntrinsicArray(DObject):

    def __init__(self, testStringArrayDynamic: str, testStringArrayStatic: str):
        self.testStringArrayDynamic = testStringArrayDynamic
        self.testStringArrayStatic = testStringArrayStatic
        
    @property
    def testStringArrayStatic(self) -> str:
        return self.__testStringArrayStatic

    @testStringArrayStatic.setter
    def testStringArrayStatic(self, testStringArrayStatic: str):
        self.__testStringArrayStatic = testStringArrayStatic

    @property
    def testStringArrayDynamic(self) -> str:
        return self.__testStringArrayDynamic

    @testStringArrayDynamic.setter
    def testStringArrayDynamic(self, testStringArrayDynamic: str):
        self.__testStringArrayDynamic = testStringArrayDynamic

class tests_TestCategoryReference(DObject):

    pass