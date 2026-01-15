from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class test_StringToTestElementMap:

    def __init__(self, key: str, test_StringToTestElementMap: "test_TestElement" = None, test_StringToTestElementMap58: "test_TestElement" = None):
        self.key = key
        self.test_StringToTestElementMap = test_StringToTestElementMap
        self.test_StringToTestElementMap58 = test_StringToTestElementMap58
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def test_StringToTestElementMap58(self):
        return self.__test_StringToTestElementMap58

    @test_StringToTestElementMap58.setter
    def test_StringToTestElementMap58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_StringToTestElementMap__test_StringToTestElementMap58", None)
        self.__test_StringToTestElementMap58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test_TestElement59"):
                opp_val = getattr(old_value, "test_TestElement59", None)
                if opp_val == self:
                    setattr(old_value, "test_TestElement59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test_TestElement59"):
                opp_val = getattr(value, "test_TestElement59", None)
                setattr(value, "test_TestElement59", self)

    @property
    def test_StringToTestElementMap(self):
        return self.__test_StringToTestElementMap

    @test_StringToTestElementMap.setter
    def test_StringToTestElementMap(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_StringToTestElementMap__test_StringToTestElementMap", None)
        self.__test_StringToTestElementMap = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test_TestElement26"):
                opp_val = getattr(old_value, "test_TestElement26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test_TestElement26"):
                opp_val = getattr(value, "test_TestElement26", None)
                if opp_val is None:
                    setattr(value, "test_TestElement26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class test_TestElementToStringMap:

    def __init__(self, value: str, test_TestElementToStringMap: "test_TestElement" = None, test_TestElementToStringMap49: "test_TestElement" = None):
        self.value = value
        self.test_TestElementToStringMap = test_TestElementToStringMap
        self.test_TestElementToStringMap49 = test_TestElementToStringMap49
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def test_TestElementToStringMap49(self):
        return self.__test_TestElementToStringMap49

    @test_TestElementToStringMap49.setter
    def test_TestElementToStringMap49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_TestElementToStringMap__test_TestElementToStringMap49", None)
        self.__test_TestElementToStringMap49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test_TestElement50"):
                opp_val = getattr(old_value, "test_TestElement50", None)
                if opp_val == self:
                    setattr(old_value, "test_TestElement50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test_TestElement50"):
                opp_val = getattr(value, "test_TestElement50", None)
                setattr(value, "test_TestElement50", self)

    @property
    def test_TestElementToStringMap(self):
        return self.__test_TestElementToStringMap

    @test_TestElementToStringMap.setter
    def test_TestElementToStringMap(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_TestElementToStringMap__test_TestElementToStringMap", None)
        self.__test_TestElementToStringMap = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test_TestElement24"):
                opp_val = getattr(old_value, "test_TestElement24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test_TestElement24"):
                opp_val = getattr(value, "test_TestElement24", None)
                if opp_val is None:
                    setattr(value, "test_TestElement24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class test_StringToStringMap:

    def __init__(self, key: str, value: str, test_StringToStringMap: "test_TestElement" = None):
        self.key = key
        self.value = value
        self.test_StringToStringMap = test_StringToStringMap
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def test_StringToStringMap(self):
        return self.__test_StringToStringMap

    @test_StringToStringMap.setter
    def test_StringToStringMap(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_StringToStringMap__test_StringToStringMap", None)
        self.__test_StringToStringMap = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test_TestElement22"):
                opp_val = getattr(old_value, "test_TestElement22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test_TestElement22"):
                opp_val = getattr(value, "test_TestElement22", None)
                if opp_val is None:
                    setattr(value, "test_TestElement22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class test_TestElementToTestElementMap:

    pass
class EObject:

    pass
class test_TestElement(EObject):

    def __init__(self, name: str, strings: str, description: str, test_TestElement: "test_TestElement" = None, test_TestElement0: set["test_TestElement"] = None, TestElement: "test_TestElement" = None, container: set["test_TestElement"] = None, test_TestElement6: "test_TestElement" = None, test_TestElement4: "test_TestElement" = None, TestElement9: "test_TestElement" = None, srefContainer: "test_TestElement" = None, test_TestElement12: "test_TestElement" = None, test_TestElement10: "test_TestElement" = None, TestElement15: "test_TestElement" = None, containedElements: "test_TestElement" = None, TestElement18: "test_TestElement" = None, containedElement: "test_TestElement" = None, test_TestElement20: set["test_TestElementToTestElementMap"] = None, test_TestElement22: set["test_StringToStringMap"] = None, test_TestElement24: set["test_TestElementToStringMap"] = None, test_TestElement26: set["test_StringToTestElementMap"] = None, TestElement29: "test_TestElement" = None, nonContained_1ToN: "test_TestElement" = None, TestElement32: "test_TestElement" = None, nonContained_NTo1: set["test_TestElement"] = None, TestElement35: "test_TestElement" = None, nonContained_MToN: set["test_TestElement"] = None, TestElement38: "test_TestElement" = None, nonContained_NToM: set["test_TestElement"] = None, TestElement41: "test_TestElement" = None, container2: set["test_TestElement"] = None, TestElement44: "test_TestElement" = None, containedElements2: "test_TestElement" = None, test_TestElement47: "test_TestElement" = None, test_TestElement45: set["test_TestElement"] = None, test_TestElement50: "test_TestElementToStringMap" = None, test_TestElement53: "test_TestElementToTestElementMap" = None, test_TestElement56: "test_TestElementToTestElementMap" = None, test_TestElement59: "test_StringToTestElementMap" = None):
        self.name = name
        self.strings = strings
        self.description = description
        self.test_TestElement = test_TestElement
        self.test_TestElement0 = test_TestElement0 if test_TestElement0 is not None else set()
        self.TestElement = TestElement
        self.container = container if container is not None else set()
        self.test_TestElement6 = test_TestElement6
        self.test_TestElement4 = test_TestElement4
        self.TestElement9 = TestElement9
        self.srefContainer = srefContainer
        self.test_TestElement12 = test_TestElement12
        self.test_TestElement10 = test_TestElement10
        self.TestElement15 = TestElement15
        self.containedElements = containedElements
        self.TestElement18 = TestElement18
        self.containedElement = containedElement
        self.test_TestElement20 = test_TestElement20 if test_TestElement20 is not None else set()
        self.test_TestElement22 = test_TestElement22 if test_TestElement22 is not None else set()
        self.test_TestElement24 = test_TestElement24 if test_TestElement24 is not None else set()
        self.test_TestElement26 = test_TestElement26 if test_TestElement26 is not None else set()
        self.TestElement29 = TestElement29
        self.nonContained_1ToN = nonContained_1ToN
        self.TestElement32 = TestElement32
        self.nonContained_NTo1 = nonContained_NTo1 if nonContained_NTo1 is not None else set()
        self.TestElement35 = TestElement35
        self.nonContained_MToN = nonContained_MToN if nonContained_MToN is not None else set()
        self.TestElement38 = TestElement38
        self.nonContained_NToM = nonContained_NToM if nonContained_NToM is not None else set()
        self.TestElement41 = TestElement41
        self.container2 = container2 if container2 is not None else set()
        self.TestElement44 = TestElement44
        self.containedElements2 = containedElements2
        self.test_TestElement47 = test_TestElement47
        self.test_TestElement45 = test_TestElement45 if test_TestElement45 is not None else set()
        self.test_TestElement50 = test_TestElement50
        self.test_TestElement53 = test_TestElement53
        self.test_TestElement56 = test_TestElement56
        self.test_TestElement59 = test_TestElement59
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def strings(self) -> str:
        return self.__strings

    @strings.setter
    def strings(self, strings: str):
        self.__strings = strings

    @property
    def test_TestElement50(self):
        return self.__test_TestElement50

    @test_TestElement50.setter
    def test_TestElement50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_TestElement__test_TestElement50", None)
        self.__test_TestElement50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test_TestElementToStringMap49"):
                opp_val = getattr(old_value, "test_TestElementToStringMap49", None)
                if opp_val == self:
                    setattr(old_value, "test_TestElementToStringMap49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test_TestElementToStringMap49"):
                opp_val = getattr(value, "test_TestElementToStringMap49", None)
                setattr(value, "test_TestElementToStringMap49", self)

    @property
    def nonContained_NTo1(self):
        return self.__nonContained_NTo1

    @nonContained_NTo1.setter
    def nonContained_NTo1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_TestElement__nonContained_NTo1", None)
        self.__nonContained_NTo1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TestElement32"):
                    opp_val = getattr(item, "TestElement32", None)
                    
                    if opp_val == self:
                        setattr(item, "TestElement32", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TestElement32"):
                    opp_val = getattr(item, "TestElement32", None)
                    
                    setattr(item, "TestElement32", self)
                    

    @property
    def test_TestElement22(self):
        return self.__test_TestElement22

    @test_TestElement22.setter
    def test_TestElement22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_TestElement__test_TestElement22", None)
        self.__test_TestElement22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "test_StringToStringMap"):
                    opp_val = getattr(item, "test_StringToStringMap", None)
                    
                    if opp_val == self:
                        setattr(item, "test_StringToStringMap", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "test_StringToStringMap"):
                    opp_val = getattr(item, "test_StringToStringMap", None)
                    
                    setattr(item, "test_StringToStringMap", self)
                    

    @property
    def test_TestElement0(self):
        return self.__test_TestElement0

    @test_TestElement0.setter
    def test_TestElement0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_TestElement__test_TestElement0", None)
        self.__test_TestElement0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "test_TestElement"):
                    opp_val = getattr(item, "test_TestElement", None)
                    
                    if opp_val == self:
                        setattr(item, "test_TestElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "test_TestElement"):
                    opp_val = getattr(item, "test_TestElement", None)
                    
                    setattr(item, "test_TestElement", self)
                    

    @property
    def test_TestElement10(self):
        return self.__test_TestElement10

    @test_TestElement10.setter
    def test_TestElement10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_TestElement__test_TestElement10", None)
        self.__test_TestElement10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test_TestElement12"):
                opp_val = getattr(old_value, "test_TestElement12", None)
                if opp_val == self:
                    setattr(old_value, "test_TestElement12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test_TestElement12"):
                opp_val = getattr(value, "test_TestElement12", None)
                setattr(value, "test_TestElement12", self)

    @property
    def test_TestElement56(self):
        return self.__test_TestElement56

    @test_TestElement56.setter
    def test_TestElement56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_TestElement__test_TestElement56", None)
        self.__test_TestElement56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test_TestElementToTestElementMap55"):
                opp_val = getattr(old_value, "test_TestElementToTestElementMap55", None)
                if opp_val == self:
                    setattr(old_value, "test_TestElementToTestElementMap55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test_TestElementToTestElementMap55"):
                opp_val = getattr(value, "test_TestElementToTestElementMap55", None)
                setattr(value, "test_TestElementToTestElementMap55", self)

    @property
    def srefContainer(self):
        return self.__srefContainer

    @srefContainer.setter
    def srefContainer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_TestElement__srefContainer", None)
        self.__srefContainer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TestElement9"):
                opp_val = getattr(old_value, "TestElement9", None)
                if opp_val == self:
                    setattr(old_value, "TestElement9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TestElement9"):
                opp_val = getattr(value, "TestElement9", None)
                setattr(value, "TestElement9", self)

    @property
    def container(self):
        return self.__container

    @container.setter
    def container(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_TestElement__container", None)
        self.__container = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TestElement"):
                    opp_val = getattr(item, "TestElement", None)
                    
                    if opp_val == self:
                        setattr(item, "TestElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TestElement"):
                    opp_val = getattr(item, "TestElement", None)
                    
                    setattr(item, "TestElement", self)
                    

    @property
    def TestElement38(self):
        return self.__TestElement38

    @TestElement38.setter
    def TestElement38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_TestElement__TestElement38", None)
        self.__TestElement38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nonContained_NToM"):
                opp_val = getattr(old_value, "nonContained_NToM", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nonContained_NToM"):
                opp_val = getattr(value, "nonContained_NToM", None)
                if opp_val is None:
                    setattr(value, "nonContained_NToM", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def container2(self):
        return self.__container2

    @container2.setter
    def container2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_TestElement__container2", None)
        self.__container2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TestElement41"):
                    opp_val = getattr(item, "TestElement41", None)
                    
                    if opp_val == self:
                        setattr(item, "TestElement41", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TestElement41"):
                    opp_val = getattr(item, "TestElement41", None)
                    
                    setattr(item, "TestElement41", self)
                    

    @property
    def test_TestElement45(self):
        return self.__test_TestElement45

    @test_TestElement45.setter
    def test_TestElement45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_TestElement__test_TestElement45", None)
        self.__test_TestElement45 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "test_TestElement47"):
                    opp_val = getattr(item, "test_TestElement47", None)
                    
                    if opp_val == self:
                        setattr(item, "test_TestElement47", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "test_TestElement47"):
                    opp_val = getattr(item, "test_TestElement47", None)
                    
                    setattr(item, "test_TestElement47", self)
                    

    @property
    def test_TestElement20(self):
        return self.__test_TestElement20

    @test_TestElement20.setter
    def test_TestElement20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_TestElement__test_TestElement20", None)
        self.__test_TestElement20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "test_TestElementToTestElementMap"):
                    opp_val = getattr(item, "test_TestElementToTestElementMap", None)
                    
                    if opp_val == self:
                        setattr(item, "test_TestElementToTestElementMap", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "test_TestElementToTestElementMap"):
                    opp_val = getattr(item, "test_TestElementToTestElementMap", None)
                    
                    setattr(item, "test_TestElementToTestElementMap", self)
                    

    @property
    def test_TestElement12(self):
        return self.__test_TestElement12

    @test_TestElement12.setter
    def test_TestElement12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_TestElement__test_TestElement12", None)
        self.__test_TestElement12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test_TestElement10"):
                opp_val = getattr(old_value, "test_TestElement10", None)
                if opp_val == self:
                    setattr(old_value, "test_TestElement10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test_TestElement10"):
                opp_val = getattr(value, "test_TestElement10", None)
                setattr(value, "test_TestElement10", self)

    @property
    def TestElement(self):
        return self.__TestElement

    @TestElement.setter
    def TestElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_TestElement__TestElement", None)
        self.__TestElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "container"):
                opp_val = getattr(old_value, "container", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "container"):
                opp_val = getattr(value, "container", None)
                if opp_val is None:
                    setattr(value, "container", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def test_TestElement24(self):
        return self.__test_TestElement24

    @test_TestElement24.setter
    def test_TestElement24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_TestElement__test_TestElement24", None)
        self.__test_TestElement24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "test_TestElementToStringMap"):
                    opp_val = getattr(item, "test_TestElementToStringMap", None)
                    
                    if opp_val == self:
                        setattr(item, "test_TestElementToStringMap", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "test_TestElementToStringMap"):
                    opp_val = getattr(item, "test_TestElementToStringMap", None)
                    
                    setattr(item, "test_TestElementToStringMap", self)
                    

    @property
    def containedElement(self):
        return self.__containedElement

    @containedElement.setter
    def containedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_TestElement__containedElement", None)
        self.__containedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TestElement18"):
                opp_val = getattr(old_value, "TestElement18", None)
                if opp_val == self:
                    setattr(old_value, "TestElement18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TestElement18"):
                opp_val = getattr(value, "TestElement18", None)
                setattr(value, "TestElement18", self)

    @property
    def test_TestElement26(self):
        return self.__test_TestElement26

    @test_TestElement26.setter
    def test_TestElement26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_TestElement__test_TestElement26", None)
        self.__test_TestElement26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "test_StringToTestElementMap"):
                    opp_val = getattr(item, "test_StringToTestElementMap", None)
                    
                    if opp_val == self:
                        setattr(item, "test_StringToTestElementMap", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "test_StringToTestElementMap"):
                    opp_val = getattr(item, "test_StringToTestElementMap", None)
                    
                    setattr(item, "test_StringToTestElementMap", self)
                    

    @property
    def containedElements2(self):
        return self.__containedElements2

    @containedElements2.setter
    def containedElements2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_TestElement__containedElements2", None)
        self.__containedElements2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TestElement44"):
                opp_val = getattr(old_value, "TestElement44", None)
                if opp_val == self:
                    setattr(old_value, "TestElement44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TestElement44"):
                opp_val = getattr(value, "TestElement44", None)
                setattr(value, "TestElement44", self)

    @property
    def test_TestElement4(self):
        return self.__test_TestElement4

    @test_TestElement4.setter
    def test_TestElement4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_TestElement__test_TestElement4", None)
        self.__test_TestElement4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test_TestElement6"):
                opp_val = getattr(old_value, "test_TestElement6", None)
                if opp_val == self:
                    setattr(old_value, "test_TestElement6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test_TestElement6"):
                opp_val = getattr(value, "test_TestElement6", None)
                setattr(value, "test_TestElement6", self)

    @property
    def test_TestElement53(self):
        return self.__test_TestElement53

    @test_TestElement53.setter
    def test_TestElement53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_TestElement__test_TestElement53", None)
        self.__test_TestElement53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test_TestElementToTestElementMap52"):
                opp_val = getattr(old_value, "test_TestElementToTestElementMap52", None)
                if opp_val == self:
                    setattr(old_value, "test_TestElementToTestElementMap52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test_TestElementToTestElementMap52"):
                opp_val = getattr(value, "test_TestElementToTestElementMap52", None)
                setattr(value, "test_TestElementToTestElementMap52", self)

    @property
    def containedElements(self):
        return self.__containedElements

    @containedElements.setter
    def containedElements(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_TestElement__containedElements", None)
        self.__containedElements = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TestElement15"):
                opp_val = getattr(old_value, "TestElement15", None)
                if opp_val == self:
                    setattr(old_value, "TestElement15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TestElement15"):
                opp_val = getattr(value, "TestElement15", None)
                setattr(value, "TestElement15", self)

    @property
    def TestElement9(self):
        return self.__TestElement9

    @TestElement9.setter
    def TestElement9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_TestElement__TestElement9", None)
        self.__TestElement9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "srefContainer"):
                opp_val = getattr(old_value, "srefContainer", None)
                if opp_val == self:
                    setattr(old_value, "srefContainer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "srefContainer"):
                opp_val = getattr(value, "srefContainer", None)
                setattr(value, "srefContainer", self)

    @property
    def test_TestElement(self):
        return self.__test_TestElement

    @test_TestElement.setter
    def test_TestElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_TestElement__test_TestElement", None)
        self.__test_TestElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test_TestElement0"):
                opp_val = getattr(old_value, "test_TestElement0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test_TestElement0"):
                opp_val = getattr(value, "test_TestElement0", None)
                if opp_val is None:
                    setattr(value, "test_TestElement0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def nonContained_MToN(self):
        return self.__nonContained_MToN

    @nonContained_MToN.setter
    def nonContained_MToN(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_TestElement__nonContained_MToN", None)
        self.__nonContained_MToN = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TestElement35"):
                    opp_val = getattr(item, "TestElement35", None)
                    
                    if opp_val == self:
                        setattr(item, "TestElement35", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TestElement35"):
                    opp_val = getattr(item, "TestElement35", None)
                    
                    setattr(item, "TestElement35", self)
                    

    @property
    def TestElement18(self):
        return self.__TestElement18

    @TestElement18.setter
    def TestElement18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_TestElement__TestElement18", None)
        self.__TestElement18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "containedElement"):
                opp_val = getattr(old_value, "containedElement", None)
                if opp_val == self:
                    setattr(old_value, "containedElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "containedElement"):
                opp_val = getattr(value, "containedElement", None)
                setattr(value, "containedElement", self)

    @property
    def test_TestElement59(self):
        return self.__test_TestElement59

    @test_TestElement59.setter
    def test_TestElement59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_TestElement__test_TestElement59", None)
        self.__test_TestElement59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test_StringToTestElementMap58"):
                opp_val = getattr(old_value, "test_StringToTestElementMap58", None)
                if opp_val == self:
                    setattr(old_value, "test_StringToTestElementMap58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test_StringToTestElementMap58"):
                opp_val = getattr(value, "test_StringToTestElementMap58", None)
                setattr(value, "test_StringToTestElementMap58", self)

    @property
    def TestElement41(self):
        return self.__TestElement41

    @TestElement41.setter
    def TestElement41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_TestElement__TestElement41", None)
        self.__TestElement41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "container2"):
                opp_val = getattr(old_value, "container2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "container2"):
                opp_val = getattr(value, "container2", None)
                if opp_val is None:
                    setattr(value, "container2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def TestElement15(self):
        return self.__TestElement15

    @TestElement15.setter
    def TestElement15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_TestElement__TestElement15", None)
        self.__TestElement15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "containedElements"):
                opp_val = getattr(old_value, "containedElements", None)
                if opp_val == self:
                    setattr(old_value, "containedElements", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "containedElements"):
                opp_val = getattr(value, "containedElements", None)
                setattr(value, "containedElements", self)

    @property
    def TestElement29(self):
        return self.__TestElement29

    @TestElement29.setter
    def TestElement29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_TestElement__TestElement29", None)
        self.__TestElement29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nonContained_1ToN"):
                opp_val = getattr(old_value, "nonContained_1ToN", None)
                if opp_val == self:
                    setattr(old_value, "nonContained_1ToN", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nonContained_1ToN"):
                opp_val = getattr(value, "nonContained_1ToN", None)
                setattr(value, "nonContained_1ToN", self)

    @property
    def nonContained_NToM(self):
        return self.__nonContained_NToM

    @nonContained_NToM.setter
    def nonContained_NToM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_TestElement__nonContained_NToM", None)
        self.__nonContained_NToM = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TestElement38"):
                    opp_val = getattr(item, "TestElement38", None)
                    
                    if opp_val == self:
                        setattr(item, "TestElement38", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TestElement38"):
                    opp_val = getattr(item, "TestElement38", None)
                    
                    setattr(item, "TestElement38", self)
                    

    @property
    def test_TestElement6(self):
        return self.__test_TestElement6

    @test_TestElement6.setter
    def test_TestElement6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_TestElement__test_TestElement6", None)
        self.__test_TestElement6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test_TestElement4"):
                opp_val = getattr(old_value, "test_TestElement4", None)
                if opp_val == self:
                    setattr(old_value, "test_TestElement4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test_TestElement4"):
                opp_val = getattr(value, "test_TestElement4", None)
                setattr(value, "test_TestElement4", self)

    @property
    def TestElement35(self):
        return self.__TestElement35

    @TestElement35.setter
    def TestElement35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_TestElement__TestElement35", None)
        self.__TestElement35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nonContained_MToN"):
                opp_val = getattr(old_value, "nonContained_MToN", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nonContained_MToN"):
                opp_val = getattr(value, "nonContained_MToN", None)
                if opp_val is None:
                    setattr(value, "nonContained_MToN", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def nonContained_1ToN(self):
        return self.__nonContained_1ToN

    @nonContained_1ToN.setter
    def nonContained_1ToN(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_TestElement__nonContained_1ToN", None)
        self.__nonContained_1ToN = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TestElement29"):
                opp_val = getattr(old_value, "TestElement29", None)
                if opp_val == self:
                    setattr(old_value, "TestElement29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TestElement29"):
                opp_val = getattr(value, "TestElement29", None)
                setattr(value, "TestElement29", self)

    @property
    def TestElement44(self):
        return self.__TestElement44

    @TestElement44.setter
    def TestElement44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_TestElement__TestElement44", None)
        self.__TestElement44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "containedElements2"):
                opp_val = getattr(old_value, "containedElements2", None)
                if opp_val == self:
                    setattr(old_value, "containedElements2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "containedElements2"):
                opp_val = getattr(value, "containedElements2", None)
                setattr(value, "containedElements2", self)

    @property
    def test_TestElement47(self):
        return self.__test_TestElement47

    @test_TestElement47.setter
    def test_TestElement47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_TestElement__test_TestElement47", None)
        self.__test_TestElement47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test_TestElement45"):
                opp_val = getattr(old_value, "test_TestElement45", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test_TestElement45"):
                opp_val = getattr(value, "test_TestElement45", None)
                if opp_val is None:
                    setattr(value, "test_TestElement45", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def TestElement32(self):
        return self.__TestElement32

    @TestElement32.setter
    def TestElement32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_TestElement__TestElement32", None)
        self.__TestElement32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nonContained_NTo1"):
                opp_val = getattr(old_value, "nonContained_NTo1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nonContained_NTo1"):
                opp_val = getattr(value, "nonContained_NTo1", None)
                if opp_val is None:
                    setattr(value, "nonContained_NTo1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
