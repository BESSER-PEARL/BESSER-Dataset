from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ElementType(Enum):
    Type1 = "Type1"
    Type2 = "Type2"


############################################
# Definition of Classes
############################################

class testModel_Element(ABC):

    pass
class Element:

    pass
class testModel_multiRefElement(Element):

    def __init__(self, name: str, testModel_multiRefElement: "testModel_referenziertesElement" = None):
        self.name = name
        self.testModel_multiRefElement = testModel_multiRefElement
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def testModel_multiRefElement(self):
        return self.__testModel_multiRefElement

    @testModel_multiRefElement.setter
    def testModel_multiRefElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testModel_multiRefElement__testModel_multiRefElement", None)
        self.__testModel_multiRefElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "testModel_referenziertesElement9"):
                opp_val = getattr(old_value, "testModel_referenziertesElement9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "testModel_referenziertesElement9"):
                opp_val = getattr(value, "testModel_referenziertesElement9", None)
                if opp_val is None:
                    setattr(value, "testModel_referenziertesElement9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class testModel_ContainedElement:

    def __init__(self, char: str, Character: str, date: date, DiagnosticChain: str, double: float, DoubleObj: str, float: float, elementType: str, name: str, byteArray: str, byteObject: str, testModel_ContainedElement5: set["testModel_referenziertesElement"] = None, testModel_ContainedElement7: set["testModel_upperBound"] = None, testModel_ContainedElement: "testModel_Kategorie" = None):
        self.char = char
        self.Character = Character
        self.date = date
        self.DiagnosticChain = DiagnosticChain
        self.double = double
        self.DoubleObj = DoubleObj
        self.float = float
        self.elementType = elementType
        self.name = name
        self.byteArray = byteArray
        self.byteObject = byteObject
        self.testModel_ContainedElement5 = testModel_ContainedElement5 if testModel_ContainedElement5 is not None else set()
        self.testModel_ContainedElement7 = testModel_ContainedElement7 if testModel_ContainedElement7 is not None else set()
        self.testModel_ContainedElement = testModel_ContainedElement
        
    @property
    def DiagnosticChain(self) -> str:
        return self.__DiagnosticChain

    @DiagnosticChain.setter
    def DiagnosticChain(self, DiagnosticChain: str):
        self.__DiagnosticChain = DiagnosticChain

    @property
    def char(self) -> str:
        return self.__char

    @char.setter
    def char(self, char: str):
        self.__char = char

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def byteArray(self) -> str:
        return self.__byteArray

    @byteArray.setter
    def byteArray(self, byteArray: str):
        self.__byteArray = byteArray

    @property
    def elementType(self) -> str:
        return self.__elementType

    @elementType.setter
    def elementType(self, elementType: str):
        self.__elementType = elementType

    @property
    def Character(self) -> str:
        return self.__Character

    @Character.setter
    def Character(self, Character: str):
        self.__Character = Character

    @property
    def DoubleObj(self) -> str:
        return self.__DoubleObj

    @DoubleObj.setter
    def DoubleObj(self, DoubleObj: str):
        self.__DoubleObj = DoubleObj

    @property
    def float(self) -> float:
        return self.__float

    @float.setter
    def float(self, float: float):
        self.__float = float

    @property
    def byteObject(self) -> str:
        return self.__byteObject

    @byteObject.setter
    def byteObject(self, byteObject: str):
        self.__byteObject = byteObject

    @property
    def double(self) -> float:
        return self.__double

    @double.setter
    def double(self, double: float):
        self.__double = double

    @property
    def date(self) -> date:
        return self.__date

    @date.setter
    def date(self, date: date):
        self.__date = date

    @property
    def testModel_ContainedElement5(self):
        return self.__testModel_ContainedElement5

    @testModel_ContainedElement5.setter
    def testModel_ContainedElement5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testModel_ContainedElement__testModel_ContainedElement5", None)
        self.__testModel_ContainedElement5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "testModel_referenziertesElement"):
                    opp_val = getattr(item, "testModel_referenziertesElement", None)
                    
                    if opp_val == self:
                        setattr(item, "testModel_referenziertesElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "testModel_referenziertesElement"):
                    opp_val = getattr(item, "testModel_referenziertesElement", None)
                    
                    setattr(item, "testModel_referenziertesElement", self)
                    

    @property
    def testModel_ContainedElement7(self):
        return self.__testModel_ContainedElement7

    @testModel_ContainedElement7.setter
    def testModel_ContainedElement7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testModel_ContainedElement__testModel_ContainedElement7", None)
        self.__testModel_ContainedElement7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "testModel_upperBound"):
                    opp_val = getattr(item, "testModel_upperBound", None)
                    
                    if opp_val == self:
                        setattr(item, "testModel_upperBound", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "testModel_upperBound"):
                    opp_val = getattr(item, "testModel_upperBound", None)
                    
                    setattr(item, "testModel_upperBound", self)
                    

    @property
    def testModel_ContainedElement(self):
        return self.__testModel_ContainedElement

    @testModel_ContainedElement.setter
    def testModel_ContainedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testModel_ContainedElement__testModel_ContainedElement", None)
        self.__testModel_ContainedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "testModel_Kategorie3"):
                opp_val = getattr(old_value, "testModel_Kategorie3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "testModel_Kategorie3"):
                opp_val = getattr(value, "testModel_Kategorie3", None)
                if opp_val is None:
                    setattr(value, "testModel_Kategorie3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class testModel_Kategorie:

    def __init__(self, name: str, bigdeci: str, bigint: str, bool: bool, Boolean: str, byte: str, testModel_Kategorie: "testModel_Kategorie" = None, testModel_Kategorie0: set["testModel_Kategorie"] = None, testModel_Kategorie3: set["testModel_ContainedElement"] = None):
        self.name = name
        self.bigdeci = bigdeci
        self.bigint = bigint
        self.bool = bool
        self.Boolean = Boolean
        self.byte = byte
        self.testModel_Kategorie = testModel_Kategorie
        self.testModel_Kategorie0 = testModel_Kategorie0 if testModel_Kategorie0 is not None else set()
        self.testModel_Kategorie3 = testModel_Kategorie3 if testModel_Kategorie3 is not None else set()
        
    @property
    def Boolean(self) -> str:
        return self.__Boolean

    @Boolean.setter
    def Boolean(self, Boolean: str):
        self.__Boolean = Boolean

    @property
    def bool(self) -> bool:
        return self.__bool

    @bool.setter
    def bool(self, bool: bool):
        self.__bool = bool

    @property
    def bigint(self) -> str:
        return self.__bigint

    @bigint.setter
    def bigint(self, bigint: str):
        self.__bigint = bigint

    @property
    def byte(self) -> str:
        return self.__byte

    @byte.setter
    def byte(self, byte: str):
        self.__byte = byte

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def bigdeci(self) -> str:
        return self.__bigdeci

    @bigdeci.setter
    def bigdeci(self, bigdeci: str):
        self.__bigdeci = bigdeci

    @property
    def testModel_Kategorie3(self):
        return self.__testModel_Kategorie3

    @testModel_Kategorie3.setter
    def testModel_Kategorie3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testModel_Kategorie__testModel_Kategorie3", None)
        self.__testModel_Kategorie3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "testModel_ContainedElement"):
                    opp_val = getattr(item, "testModel_ContainedElement", None)
                    
                    if opp_val == self:
                        setattr(item, "testModel_ContainedElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "testModel_ContainedElement"):
                    opp_val = getattr(item, "testModel_ContainedElement", None)
                    
                    setattr(item, "testModel_ContainedElement", self)
                    

    @property
    def testModel_Kategorie0(self):
        return self.__testModel_Kategorie0

    @testModel_Kategorie0.setter
    def testModel_Kategorie0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testModel_Kategorie__testModel_Kategorie0", None)
        self.__testModel_Kategorie0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "testModel_Kategorie"):
                    opp_val = getattr(item, "testModel_Kategorie", None)
                    
                    if opp_val == self:
                        setattr(item, "testModel_Kategorie", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "testModel_Kategorie"):
                    opp_val = getattr(item, "testModel_Kategorie", None)
                    
                    setattr(item, "testModel_Kategorie", self)
                    

    @property
    def testModel_Kategorie(self):
        return self.__testModel_Kategorie

    @testModel_Kategorie.setter
    def testModel_Kategorie(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testModel_Kategorie__testModel_Kategorie", None)
        self.__testModel_Kategorie = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "testModel_Kategorie0"):
                opp_val = getattr(old_value, "testModel_Kategorie0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "testModel_Kategorie0"):
                opp_val = getattr(value, "testModel_Kategorie0", None)
                if opp_val is None:
                    setattr(value, "testModel_Kategorie0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class testModel_upperBound(Element):

    def __init__(self, name: str, testModel_upperBound: "testModel_ContainedElement" = None):
        self.name = name
        self.testModel_upperBound = testModel_upperBound
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def testModel_upperBound(self):
        return self.__testModel_upperBound

    @testModel_upperBound.setter
    def testModel_upperBound(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testModel_upperBound__testModel_upperBound", None)
        self.__testModel_upperBound = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "testModel_ContainedElement7"):
                opp_val = getattr(old_value, "testModel_ContainedElement7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "testModel_ContainedElement7"):
                opp_val = getattr(value, "testModel_ContainedElement7", None)
                if opp_val is None:
                    setattr(value, "testModel_ContainedElement7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class testModel_referenziertesElement(Element):

    def __init__(self, Float: str, int: int, Integer: str, long: str, LongObj: str, short: str, ShortObj: str, name: str, notChangeable: str, testModel_referenziertesElement: "testModel_ContainedElement" = None, testModel_referenziertesElement9: set["testModel_multiRefElement"] = None):
        self.Float = Float
        self.int = int
        self.Integer = Integer
        self.long = long
        self.LongObj = LongObj
        self.short = short
        self.ShortObj = ShortObj
        self.name = name
        self.notChangeable = notChangeable
        self.testModel_referenziertesElement = testModel_referenziertesElement
        self.testModel_referenziertesElement9 = testModel_referenziertesElement9 if testModel_referenziertesElement9 is not None else set()
        
    @property
    def short(self) -> str:
        return self.__short

    @short.setter
    def short(self, short: str):
        self.__short = short

    @property
    def notChangeable(self) -> str:
        return self.__notChangeable

    @notChangeable.setter
    def notChangeable(self, notChangeable: str):
        self.__notChangeable = notChangeable

    @property
    def int(self) -> int:
        return self.__int

    @int.setter
    def int(self, int: int):
        self.__int = int

    @property
    def LongObj(self) -> str:
        return self.__LongObj

    @LongObj.setter
    def LongObj(self, LongObj: str):
        self.__LongObj = LongObj

    @property
    def Integer(self) -> str:
        return self.__Integer

    @Integer.setter
    def Integer(self, Integer: str):
        self.__Integer = Integer

    @property
    def ShortObj(self) -> str:
        return self.__ShortObj

    @ShortObj.setter
    def ShortObj(self, ShortObj: str):
        self.__ShortObj = ShortObj

    @property
    def Float(self) -> str:
        return self.__Float

    @Float.setter
    def Float(self, Float: str):
        self.__Float = Float

    @property
    def long(self) -> str:
        return self.__long

    @long.setter
    def long(self, long: str):
        self.__long = long

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def testModel_referenziertesElement9(self):
        return self.__testModel_referenziertesElement9

    @testModel_referenziertesElement9.setter
    def testModel_referenziertesElement9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testModel_referenziertesElement__testModel_referenziertesElement9", None)
        self.__testModel_referenziertesElement9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "testModel_multiRefElement"):
                    opp_val = getattr(item, "testModel_multiRefElement", None)
                    
                    if opp_val == self:
                        setattr(item, "testModel_multiRefElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "testModel_multiRefElement"):
                    opp_val = getattr(item, "testModel_multiRefElement", None)
                    
                    setattr(item, "testModel_multiRefElement", self)
                    

    @property
    def testModel_referenziertesElement(self):
        return self.__testModel_referenziertesElement

    @testModel_referenziertesElement.setter
    def testModel_referenziertesElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testModel_referenziertesElement__testModel_referenziertesElement", None)
        self.__testModel_referenziertesElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "testModel_ContainedElement5"):
                opp_val = getattr(old_value, "testModel_ContainedElement5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "testModel_ContainedElement5"):
                opp_val = getattr(value, "testModel_ContainedElement5", None)
                if opp_val is None:
                    setattr(value, "testModel_ContainedElement5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
