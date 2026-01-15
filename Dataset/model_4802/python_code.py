from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class pltest_Circle:

    def __init__(self, area: float, diameter: str, circumference: float, pltest_Circle5: "pltest_WhatEver" = None, pltest_Circle: set["pltest_Red"] = None):
        self.area = area
        self.diameter = diameter
        self.circumference = circumference
        self.pltest_Circle5 = pltest_Circle5
        self.pltest_Circle = pltest_Circle if pltest_Circle is not None else set()
        
    @property
    def diameter(self) -> str:
        return self.__diameter

    @diameter.setter
    def diameter(self, diameter: str):
        self.__diameter = diameter

    @property
    def circumference(self) -> float:
        return self.__circumference

    @circumference.setter
    def circumference(self, circumference: float):
        self.__circumference = circumference

    @property
    def area(self) -> float:
        return self.__area

    @area.setter
    def area(self, area: float):
        self.__area = area

    @property
    def pltest_Circle5(self):
        return self.__pltest_Circle5

    @pltest_Circle5.setter
    def pltest_Circle5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pltest_Circle__pltest_Circle5", None)
        self.__pltest_Circle5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pltest_WhatEver"):
                opp_val = getattr(old_value, "pltest_WhatEver", None)
                if opp_val == self:
                    setattr(old_value, "pltest_WhatEver", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pltest_WhatEver"):
                opp_val = getattr(value, "pltest_WhatEver", None)
                setattr(value, "pltest_WhatEver", self)

    @property
    def pltest_Circle(self):
        return self.__pltest_Circle

    @pltest_Circle.setter
    def pltest_Circle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pltest_Circle__pltest_Circle", None)
        self.__pltest_Circle = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pltest_Red"):
                    opp_val = getattr(item, "pltest_Red", None)
                    
                    if opp_val == self:
                        setattr(item, "pltest_Red", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pltest_Red"):
                    opp_val = getattr(item, "pltest_Red", None)
                    
                    setattr(item, "pltest_Red", self)
                    

class pltest_Red:

    def __init__(self, redness: int, pltest_Red: "pltest_Circle" = None):
        self.redness = redness
        self.pltest_Red = pltest_Red
        
    @property
    def redness(self) -> int:
        return self.__redness

    @redness.setter
    def redness(self, redness: int):
        self.__redness = redness

    @property
    def pltest_Red(self):
        return self.__pltest_Red

    @pltest_Red.setter
    def pltest_Red(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pltest_Red__pltest_Red", None)
        self.__pltest_Red = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pltest_Circle"):
                opp_val = getattr(old_value, "pltest_Circle", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pltest_Circle"):
                opp_val = getattr(value, "pltest_Circle", None)
                if opp_val is None:
                    setattr(value, "pltest_Circle", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Child2:

    pass
class pltest_GrandChild2(Child2):

    pass
class pltest_Child3:

    pass
class Child1:

    pass
class Child3:

    pass
class pltest_GrandChild(Child3, Child1):

    pass
class TestClassifier:

    pass
class pltest_TestInterface(TestClassifier):

    pass
class pltest_TestClass(TestClassifier):

    pass
class TestPackageableElement:

    pass
class pltest_TestClassifier(TestPackageableElement):

    pass
class pltest_TestPackage(TestPackageableElement):

    pass
class pltest_TestPackageableElement:

    pass
class pltest_Numbers:

    def __init__(self, int: int, long: str, float: float, double: float, bigInt: str, bigDecimal: str):
        self.int = int
        self.long = long
        self.float = float
        self.double = double
        self.bigInt = bigInt
        self.bigDecimal = bigDecimal
        
    @property
    def float(self) -> float:
        return self.__float

    @float.setter
    def float(self, float: float):
        self.__float = float

    @property
    def double(self) -> float:
        return self.__double

    @double.setter
    def double(self, double: float):
        self.__double = double

    @property
    def int(self) -> int:
        return self.__int

    @int.setter
    def int(self, int: int):
        self.__int = int

    @property
    def long(self) -> str:
        return self.__long

    @long.setter
    def long(self, long: str):
        self.__long = long

    @property
    def bigDecimal(self) -> str:
        return self.__bigDecimal

    @bigDecimal.setter
    def bigDecimal(self, bigDecimal: str):
        self.__bigDecimal = bigDecimal

    @property
    def bigInt(self) -> str:
        return self.__bigInt

    @bigInt.setter
    def bigInt(self, bigInt: str):
        self.__bigInt = bigInt

class GrandChildD:

    pass
class pltest_GrandGrandChildF(GrandChildD, Child2):

    pass
class pltest_GrandGrandChildE(GrandChildD, Child1):

    pass
class pltest_GrandChildD(Child3):

    pass
class pltest_WhatEver:

    pass
class Interface:

    pass
class Common:

    pass
class pltest_Child2(Interface, Child3, Common):

    pass
class pltest_Child1(Interface, Common):

    def __init__(self, name: str, pltest_Child1: "pltest_Common" = None):
        self.name = name
        self.pltest_Child1 = pltest_Child1
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def pltest_Child1(self):
        return self.__pltest_Child1

    @pltest_Child1.setter
    def pltest_Child1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pltest_Child1__pltest_Child1", None)
        self.__pltest_Child1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pltest_Common"):
                opp_val = getattr(old_value, "pltest_Common", None)
                if opp_val == self:
                    setattr(old_value, "pltest_Common", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pltest_Common"):
                opp_val = getattr(value, "pltest_Common", None)
                setattr(value, "pltest_Common", self)

class pltest_Interface(ABC):

    pass
class Base:

    pass
class pltest_Common(Base):

    pass
class pltest_Base:

    pass