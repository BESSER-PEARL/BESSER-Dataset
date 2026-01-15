from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class listType(Enum):
    ArrayList = "ArrayList"
    List = "List"


############################################
# Definition of Classes
############################################

class TestPackage_List_Element:

    pass
class SubTestPackage_List_Element:

    pass
class List_SubTestPackage_SubTest:

    def __init__(self, value: int, subTestPointer: "SubTestPackage_List_Element" = None):
        self.value = value
        self.subTestPointer = subTestPointer
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def subTestPointer(self):
        return self.__subTestPointer

    @subTestPointer.setter
    def subTestPointer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_List_SubTestPackage_SubTest__subTestPointer", None)
        self.__subTestPointer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Element"):
                opp_val = getattr(old_value, "Element", None)
                if opp_val == self:
                    setattr(old_value, "Element", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Element"):
                opp_val = getattr(value, "Element", None)
                setattr(value, "Element", self)

class List_TestPackage_Test:

    def __init__(self, value: int, List_TestPackage_Test: "TestPackage_List_Element" = None, List_TestPackage_Test18: "TestPackage_List_Element" = None):
        self.value = value
        self.List_TestPackage_Test = List_TestPackage_Test
        self.List_TestPackage_Test18 = List_TestPackage_Test18
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def List_TestPackage_Test(self):
        return self.__List_TestPackage_Test

    @List_TestPackage_Test.setter
    def List_TestPackage_Test(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_List_TestPackage_Test__List_TestPackage_Test", None)
        self.__List_TestPackage_Test = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TestPackage_List_Element"):
                opp_val = getattr(old_value, "TestPackage_List_Element", None)
                if opp_val == self:
                    setattr(old_value, "TestPackage_List_Element", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TestPackage_List_Element"):
                opp_val = getattr(value, "TestPackage_List_Element", None)
                setattr(value, "TestPackage_List_Element", self)

    @property
    def List_TestPackage_Test18(self):
        return self.__List_TestPackage_Test18

    @List_TestPackage_Test18.setter
    def List_TestPackage_Test18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_List_TestPackage_Test__List_TestPackage_Test18", None)
        self.__List_TestPackage_Test18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TestPackage_List_Element19"):
                opp_val = getattr(old_value, "TestPackage_List_Element19", None)
                if opp_val == self:
                    setattr(old_value, "TestPackage_List_Element19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TestPackage_List_Element19"):
                opp_val = getattr(value, "TestPackage_List_Element19", None)
                setattr(value, "TestPackage_List_Element19", self)

class SubTestPackage_SubTest:

    pass
class Test:

    pass
class List_Element:

    def __init__(self, name: str, value: int, List_Element: "List_List" = None, List_Element3: "List_List" = None, List_Element6: "List_List" = None, List_Element13: "List_List" = None, SubTestPackage: "SubTestPackage_SubTest" = None):
        self.name = name
        self.value = value
        self.List_Element = List_Element
        self.List_Element3 = List_Element3
        self.List_Element6 = List_Element6
        self.List_Element13 = List_Element13
        self.SubTestPackage = SubTestPackage
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def List_Element13(self):
        return self.__List_Element13

    @List_Element13.setter
    def List_Element13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_List_Element__List_Element13", None)
        self.__List_Element13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "List_List14"):
                opp_val = getattr(old_value, "List_List14", None)
                if opp_val == self:
                    setattr(old_value, "List_List14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "List_List14"):
                opp_val = getattr(value, "List_List14", None)
                setattr(value, "List_List14", self)

    @property
    def List_Element6(self):
        return self.__List_Element6

    @List_Element6.setter
    def List_Element6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_List_Element__List_Element6", None)
        self.__List_Element6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "List_List5"):
                opp_val = getattr(old_value, "List_List5", None)
                if opp_val == self:
                    setattr(old_value, "List_List5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "List_List5"):
                opp_val = getattr(value, "List_List5", None)
                setattr(value, "List_List5", self)

    @property
    def List_Element(self):
        return self.__List_Element

    @List_Element.setter
    def List_Element(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_List_Element__List_Element", None)
        self.__List_Element = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "List_List"):
                opp_val = getattr(old_value, "List_List", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "List_List"):
                opp_val = getattr(value, "List_List", None)
                if opp_val is None:
                    setattr(value, "List_List", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def SubTestPackage(self):
        return self.__SubTestPackage

    @SubTestPackage.setter
    def SubTestPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_List_Element__SubTestPackage", None)
        self.__SubTestPackage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TestPackage"):
                opp_val = getattr(old_value, "TestPackage", None)
                if opp_val == self:
                    setattr(old_value, "TestPackage", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TestPackage"):
                opp_val = getattr(value, "TestPackage", None)
                setattr(value, "TestPackage", self)

    @property
    def List_Element3(self):
        return self.__List_Element3

    @List_Element3.setter
    def List_Element3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_List_Element__List_Element3", None)
        self.__List_Element3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "List_List2"):
                opp_val = getattr(old_value, "List_List2", None)
                if opp_val == self:
                    setattr(old_value, "List_List2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "List_List2"):
                opp_val = getattr(value, "List_List2", None)
                setattr(value, "List_List2", self)

class List_List:

    def __init__(self, size: int, type: str, List_List: set["List_Element"] = None, List_List2: "List_Element" = None, List_List5: "List_Element" = None, List_List9: "List_List" = None, List_List7: "List_List" = None, List_List11: "Test" = None, List_List14: "List_Element" = None):
        self.size = size
        self.type = type
        self.List_List = List_List if List_List is not None else set()
        self.List_List2 = List_List2
        self.List_List5 = List_List5
        self.List_List9 = List_List9
        self.List_List7 = List_List7
        self.List_List11 = List_List11
        self.List_List14 = List_List14
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, size: int):
        self.__size = size

    @property
    def List_List2(self):
        return self.__List_List2

    @List_List2.setter
    def List_List2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_List_List__List_List2", None)
        self.__List_List2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "List_Element3"):
                opp_val = getattr(old_value, "List_Element3", None)
                if opp_val == self:
                    setattr(old_value, "List_Element3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "List_Element3"):
                opp_val = getattr(value, "List_Element3", None)
                setattr(value, "List_Element3", self)

    @property
    def List_List7(self):
        return self.__List_List7

    @List_List7.setter
    def List_List7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_List_List__List_List7", None)
        self.__List_List7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "List_List9"):
                opp_val = getattr(old_value, "List_List9", None)
                if opp_val == self:
                    setattr(old_value, "List_List9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "List_List9"):
                opp_val = getattr(value, "List_List9", None)
                setattr(value, "List_List9", self)

    @property
    def List_List9(self):
        return self.__List_List9

    @List_List9.setter
    def List_List9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_List_List__List_List9", None)
        self.__List_List9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "List_List7"):
                opp_val = getattr(old_value, "List_List7", None)
                if opp_val == self:
                    setattr(old_value, "List_List7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "List_List7"):
                opp_val = getattr(value, "List_List7", None)
                setattr(value, "List_List7", self)

    @property
    def List_List11(self):
        return self.__List_List11

    @List_List11.setter
    def List_List11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_List_List__List_List11", None)
        self.__List_List11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Test"):
                opp_val = getattr(old_value, "Test", None)
                if opp_val == self:
                    setattr(old_value, "Test", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Test"):
                opp_val = getattr(value, "Test", None)
                setattr(value, "Test", self)

    @property
    def List_List5(self):
        return self.__List_List5

    @List_List5.setter
    def List_List5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_List_List__List_List5", None)
        self.__List_List5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "List_Element6"):
                opp_val = getattr(old_value, "List_Element6", None)
                if opp_val == self:
                    setattr(old_value, "List_Element6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "List_Element6"):
                opp_val = getattr(value, "List_Element6", None)
                setattr(value, "List_Element6", self)

    @property
    def List_List14(self):
        return self.__List_List14

    @List_List14.setter
    def List_List14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_List_List__List_List14", None)
        self.__List_List14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "List_Element13"):
                opp_val = getattr(old_value, "List_Element13", None)
                if opp_val == self:
                    setattr(old_value, "List_Element13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "List_Element13"):
                opp_val = getattr(value, "List_Element13", None)
                setattr(value, "List_Element13", self)

    @property
    def List_List(self):
        return self.__List_List

    @List_List.setter
    def List_List(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_List_List__List_List", None)
        self.__List_List = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "List_Element"):
                    opp_val = getattr(item, "List_Element", None)
                    
                    if opp_val == self:
                        setattr(item, "List_Element", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "List_Element"):
                    opp_val = getattr(item, "List_Element", None)
                    
                    setattr(item, "List_Element", self)
                    
