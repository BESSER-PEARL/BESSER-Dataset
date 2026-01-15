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

class Leafs:

    pass
class testModel_upperBoundLeaf(Leafs):

    def __init__(self, name: str, testModel_upperBoundLeaf: "testModel_ContainedLeaf" = None):
        self.name = name
        self.testModel_upperBoundLeaf = testModel_upperBoundLeaf
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def testModel_upperBoundLeaf(self):
        return self.__testModel_upperBoundLeaf

    @testModel_upperBoundLeaf.setter
    def testModel_upperBoundLeaf(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testModel_upperBoundLeaf__testModel_upperBoundLeaf", None)
        self.__testModel_upperBoundLeaf = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "testModel_ContainedLeaf7"):
                opp_val = getattr(old_value, "testModel_ContainedLeaf7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "testModel_ContainedLeaf7"):
                opp_val = getattr(value, "testModel_ContainedLeaf7", None)
                if opp_val is None:
                    setattr(value, "testModel_ContainedLeaf7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class testModel_referedLeaf(Leafs):

    def __init__(self, name: str, notChangeable: str, Float: str, int: int, Integer: str, long: str, LongObj: str, short: str, ShortObj: str, testModel_referedLeaf9: set["testModel_multiRefLeaf"] = None, testModel_referedLeaf: "testModel_ContainedLeaf" = None):
        self.name = name
        self.notChangeable = notChangeable
        self.Float = Float
        self.int = int
        self.Integer = Integer
        self.long = long
        self.LongObj = LongObj
        self.short = short
        self.ShortObj = ShortObj
        self.testModel_referedLeaf9 = testModel_referedLeaf9 if testModel_referedLeaf9 is not None else set()
        self.testModel_referedLeaf = testModel_referedLeaf
        
    @property
    def long(self) -> str:
        return self.__long

    @long.setter
    def long(self, long: str):
        self.__long = long

    @property
    def Integer(self) -> str:
        return self.__Integer

    @Integer.setter
    def Integer(self, Integer: str):
        self.__Integer = Integer

    @property
    def Float(self) -> str:
        return self.__Float

    @Float.setter
    def Float(self, Float: str):
        self.__Float = Float

    @property
    def notChangeable(self) -> str:
        return self.__notChangeable

    @notChangeable.setter
    def notChangeable(self, notChangeable: str):
        self.__notChangeable = notChangeable

    @property
    def short(self) -> str:
        return self.__short

    @short.setter
    def short(self, short: str):
        self.__short = short

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def LongObj(self) -> str:
        return self.__LongObj

    @LongObj.setter
    def LongObj(self, LongObj: str):
        self.__LongObj = LongObj

    @property
    def int(self) -> int:
        return self.__int

    @int.setter
    def int(self, int: int):
        self.__int = int

    @property
    def ShortObj(self) -> str:
        return self.__ShortObj

    @ShortObj.setter
    def ShortObj(self, ShortObj: str):
        self.__ShortObj = ShortObj

    @property
    def testModel_referedLeaf9(self):
        return self.__testModel_referedLeaf9

    @testModel_referedLeaf9.setter
    def testModel_referedLeaf9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testModel_referedLeaf__testModel_referedLeaf9", None)
        self.__testModel_referedLeaf9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "testModel_multiRefLeaf"):
                    opp_val = getattr(item, "testModel_multiRefLeaf", None)
                    
                    if opp_val == self:
                        setattr(item, "testModel_multiRefLeaf", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "testModel_multiRefLeaf"):
                    opp_val = getattr(item, "testModel_multiRefLeaf", None)
                    
                    setattr(item, "testModel_multiRefLeaf", self)
                    

    @property
    def testModel_referedLeaf(self):
        return self.__testModel_referedLeaf

    @testModel_referedLeaf.setter
    def testModel_referedLeaf(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testModel_referedLeaf__testModel_referedLeaf", None)
        self.__testModel_referedLeaf = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "testModel_ContainedLeaf5"):
                opp_val = getattr(old_value, "testModel_ContainedLeaf5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "testModel_ContainedLeaf5"):
                opp_val = getattr(value, "testModel_ContainedLeaf5", None)
                if opp_val is None:
                    setattr(value, "testModel_ContainedLeaf5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class testModel_Leafs(ABC):

    pass
class testModel_multiRefLeaf(Leafs):

    def __init__(self, name: str, testModel_multiRefLeaf: "testModel_referedLeaf" = None):
        self.name = name
        self.testModel_multiRefLeaf = testModel_multiRefLeaf
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def testModel_multiRefLeaf(self):
        return self.__testModel_multiRefLeaf

    @testModel_multiRefLeaf.setter
    def testModel_multiRefLeaf(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testModel_multiRefLeaf__testModel_multiRefLeaf", None)
        self.__testModel_multiRefLeaf = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "testModel_referedLeaf9"):
                opp_val = getattr(old_value, "testModel_referedLeaf9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "testModel_referedLeaf9"):
                opp_val = getattr(value, "testModel_referedLeaf9", None)
                if opp_val is None:
                    setattr(value, "testModel_referedLeaf9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class testModel_ContainedLeaf:

    def __init__(self, name: str, byteArray: str, byteObject: str, char: str, Character: str, date: date, double: float, DoubleObj: str, float: float, elementType: str, testModel_ContainedLeaf: "testModel_Node" = None, testModel_ContainedLeaf5: set["testModel_referedLeaf"] = None, testModel_ContainedLeaf7: set["testModel_upperBoundLeaf"] = None):
        self.name = name
        self.byteArray = byteArray
        self.byteObject = byteObject
        self.char = char
        self.Character = Character
        self.date = date
        self.double = double
        self.DoubleObj = DoubleObj
        self.float = float
        self.elementType = elementType
        self.testModel_ContainedLeaf = testModel_ContainedLeaf
        self.testModel_ContainedLeaf5 = testModel_ContainedLeaf5 if testModel_ContainedLeaf5 is not None else set()
        self.testModel_ContainedLeaf7 = testModel_ContainedLeaf7 if testModel_ContainedLeaf7 is not None else set()
        
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
    def Character(self) -> str:
        return self.__Character

    @Character.setter
    def Character(self, Character: str):
        self.__Character = Character

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
    def double(self) -> float:
        return self.__double

    @double.setter
    def double(self, double: float):
        self.__double = double

    @property
    def char(self) -> str:
        return self.__char

    @char.setter
    def char(self, char: str):
        self.__char = char

    @property
    def date(self) -> date:
        return self.__date

    @date.setter
    def date(self, date: date):
        self.__date = date

    @property
    def testModel_ContainedLeaf7(self):
        return self.__testModel_ContainedLeaf7

    @testModel_ContainedLeaf7.setter
    def testModel_ContainedLeaf7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testModel_ContainedLeaf__testModel_ContainedLeaf7", None)
        self.__testModel_ContainedLeaf7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "testModel_upperBoundLeaf"):
                    opp_val = getattr(item, "testModel_upperBoundLeaf", None)
                    
                    if opp_val == self:
                        setattr(item, "testModel_upperBoundLeaf", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "testModel_upperBoundLeaf"):
                    opp_val = getattr(item, "testModel_upperBoundLeaf", None)
                    
                    setattr(item, "testModel_upperBoundLeaf", self)
                    

    @property
    def testModel_ContainedLeaf(self):
        return self.__testModel_ContainedLeaf

    @testModel_ContainedLeaf.setter
    def testModel_ContainedLeaf(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testModel_ContainedLeaf__testModel_ContainedLeaf", None)
        self.__testModel_ContainedLeaf = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "testModel_Node3"):
                opp_val = getattr(old_value, "testModel_Node3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "testModel_Node3"):
                opp_val = getattr(value, "testModel_Node3", None)
                if opp_val is None:
                    setattr(value, "testModel_Node3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def testModel_ContainedLeaf5(self):
        return self.__testModel_ContainedLeaf5

    @testModel_ContainedLeaf5.setter
    def testModel_ContainedLeaf5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testModel_ContainedLeaf__testModel_ContainedLeaf5", None)
        self.__testModel_ContainedLeaf5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "testModel_referedLeaf"):
                    opp_val = getattr(item, "testModel_referedLeaf", None)
                    
                    if opp_val == self:
                        setattr(item, "testModel_referedLeaf", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "testModel_referedLeaf"):
                    opp_val = getattr(item, "testModel_referedLeaf", None)
                    
                    setattr(item, "testModel_referedLeaf", self)
                    

class testModel_Node:

    def __init__(self, name: str, bigdeci: str, bigint: str, bool: bool, Boolean: str, byte: str, testModel_Node: "testModel_Node" = None, testModel_Node0: set["testModel_Node"] = None, testModel_Node3: set["testModel_ContainedLeaf"] = None):
        self.name = name
        self.bigdeci = bigdeci
        self.bigint = bigint
        self.bool = bool
        self.Boolean = Boolean
        self.byte = byte
        self.testModel_Node = testModel_Node
        self.testModel_Node0 = testModel_Node0 if testModel_Node0 is not None else set()
        self.testModel_Node3 = testModel_Node3 if testModel_Node3 is not None else set()
        
    @property
    def bigint(self) -> str:
        return self.__bigint

    @bigint.setter
    def bigint(self, bigint: str):
        self.__bigint = bigint

    @property
    def bool(self) -> bool:
        return self.__bool

    @bool.setter
    def bool(self, bool: bool):
        self.__bool = bool

    @property
    def byte(self) -> str:
        return self.__byte

    @byte.setter
    def byte(self, byte: str):
        self.__byte = byte

    @property
    def Boolean(self) -> str:
        return self.__Boolean

    @Boolean.setter
    def Boolean(self, Boolean: str):
        self.__Boolean = Boolean

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
    def testModel_Node(self):
        return self.__testModel_Node

    @testModel_Node.setter
    def testModel_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testModel_Node__testModel_Node", None)
        self.__testModel_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "testModel_Node0"):
                opp_val = getattr(old_value, "testModel_Node0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "testModel_Node0"):
                opp_val = getattr(value, "testModel_Node0", None)
                if opp_val is None:
                    setattr(value, "testModel_Node0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def testModel_Node0(self):
        return self.__testModel_Node0

    @testModel_Node0.setter
    def testModel_Node0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testModel_Node__testModel_Node0", None)
        self.__testModel_Node0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "testModel_Node"):
                    opp_val = getattr(item, "testModel_Node", None)
                    
                    if opp_val == self:
                        setattr(item, "testModel_Node", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "testModel_Node"):
                    opp_val = getattr(item, "testModel_Node", None)
                    
                    setattr(item, "testModel_Node", self)
                    

    @property
    def testModel_Node3(self):
        return self.__testModel_Node3

    @testModel_Node3.setter
    def testModel_Node3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testModel_Node__testModel_Node3", None)
        self.__testModel_Node3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "testModel_ContainedLeaf"):
                    opp_val = getattr(item, "testModel_ContainedLeaf", None)
                    
                    if opp_val == self:
                        setattr(item, "testModel_ContainedLeaf", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "testModel_ContainedLeaf"):
                    opp_val = getattr(item, "testModel_ContainedLeaf", None)
                    
                    setattr(item, "testModel_ContainedLeaf", self)
                    
