from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class testmodel_TestElementToTestElementMap:

    pass
class testmodel_TestElementContainer:

    pass
class testmodel_StringToTestElementMap:

    def __init__(self, key: str, testmodel_StringToTestElementMap: "testmodel_TestElement" = None, testmodel_StringToTestElementMap37: "testmodel_TestElement" = None):
        self.key = key
        self.testmodel_StringToTestElementMap = testmodel_StringToTestElementMap
        self.testmodel_StringToTestElementMap37 = testmodel_StringToTestElementMap37
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def testmodel_StringToTestElementMap(self):
        return self.__testmodel_StringToTestElementMap

    @testmodel_StringToTestElementMap.setter
    def testmodel_StringToTestElementMap(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testmodel_StringToTestElementMap__testmodel_StringToTestElementMap", None)
        self.__testmodel_StringToTestElementMap = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "testmodel_TestElement25"):
                opp_val = getattr(old_value, "testmodel_TestElement25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "testmodel_TestElement25"):
                opp_val = getattr(value, "testmodel_TestElement25", None)
                if opp_val is None:
                    setattr(value, "testmodel_TestElement25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def testmodel_StringToTestElementMap37(self):
        return self.__testmodel_StringToTestElementMap37

    @testmodel_StringToTestElementMap37.setter
    def testmodel_StringToTestElementMap37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testmodel_StringToTestElementMap__testmodel_StringToTestElementMap37", None)
        self.__testmodel_StringToTestElementMap37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "testmodel_TestElement38"):
                opp_val = getattr(old_value, "testmodel_TestElement38", None)
                if opp_val == self:
                    setattr(old_value, "testmodel_TestElement38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "testmodel_TestElement38"):
                opp_val = getattr(value, "testmodel_TestElement38", None)
                setattr(value, "testmodel_TestElement38", self)

class testmodel_TestElementToStringMap:

    def __init__(self, value: str, testmodel_TestElementToStringMap: "testmodel_TestElement" = None, testmodel_TestElementToStringMap28: "testmodel_TestElement" = None):
        self.value = value
        self.testmodel_TestElementToStringMap = testmodel_TestElementToStringMap
        self.testmodel_TestElementToStringMap28 = testmodel_TestElementToStringMap28
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def testmodel_TestElementToStringMap28(self):
        return self.__testmodel_TestElementToStringMap28

    @testmodel_TestElementToStringMap28.setter
    def testmodel_TestElementToStringMap28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testmodel_TestElementToStringMap__testmodel_TestElementToStringMap28", None)
        self.__testmodel_TestElementToStringMap28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "testmodel_TestElement29"):
                opp_val = getattr(old_value, "testmodel_TestElement29", None)
                if opp_val == self:
                    setattr(old_value, "testmodel_TestElement29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "testmodel_TestElement29"):
                opp_val = getattr(value, "testmodel_TestElement29", None)
                setattr(value, "testmodel_TestElement29", self)

    @property
    def testmodel_TestElementToStringMap(self):
        return self.__testmodel_TestElementToStringMap

    @testmodel_TestElementToStringMap.setter
    def testmodel_TestElementToStringMap(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testmodel_TestElementToStringMap__testmodel_TestElementToStringMap", None)
        self.__testmodel_TestElementToStringMap = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "testmodel_TestElement23"):
                opp_val = getattr(old_value, "testmodel_TestElement23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "testmodel_TestElement23"):
                opp_val = getattr(value, "testmodel_TestElement23", None)
                if opp_val is None:
                    setattr(value, "testmodel_TestElement23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class testmodel_StringToStringMap:

    def __init__(self, key: str, value: str, testmodel_StringToStringMap: "testmodel_TestElement" = None):
        self.key = key
        self.value = value
        self.testmodel_StringToStringMap = testmodel_StringToStringMap
        
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
    def testmodel_StringToStringMap(self):
        return self.__testmodel_StringToStringMap

    @testmodel_StringToStringMap.setter
    def testmodel_StringToStringMap(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testmodel_StringToStringMap__testmodel_StringToStringMap", None)
        self.__testmodel_StringToStringMap = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "testmodel_TestElement21"):
                opp_val = getattr(old_value, "testmodel_TestElement21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "testmodel_TestElement21"):
                opp_val = getattr(value, "testmodel_TestElement21", None)
                if opp_val is None:
                    setattr(value, "testmodel_TestElement21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class EObject:

    pass
class testmodel_TestElement(EObject):

    def __init__(self, name: str, strings: str, description: str, testmodel_TestElement21: set["testmodel_StringToStringMap"] = None, testmodel_TestElement23: set["testmodel_TestElementToStringMap"] = None, testmodel_TestElement25: set["testmodel_StringToTestElementMap"] = None, TestElement: "testmodel_TestElementContainer" = None, testmodel_TestElement29: "testmodel_TestElementToStringMap" = None, testmodel_TestElement: "testmodel_TestElement" = None, testmodel_TestElement0: set["testmodel_TestElement"] = None, testmodel_TestElement4: "testmodel_TestElement" = None, testmodel_TestElement2: set["testmodel_TestElement"] = None, testmodel_TestElement7: "testmodel_TestElement" = None, testmodel_TestElement5: "testmodel_TestElement" = None, testmodel_TestElement10: "testmodel_TestElement" = None, testmodel_TestElement8: "testmodel_TestElement" = None, testmodel_TestElement13: "testmodel_TestElement" = None, testmodel_TestElement11: "testmodel_TestElement" = None, testmodel_TestElement16: "testmodel_TestElement" = None, testmodel_TestElement14: set["testmodel_TestElement"] = None, elements: "testmodel_TestElementContainer" = None, testmodel_TestElement19: set["testmodel_TestElementToTestElementMap"] = None, testmodel_TestElement32: "testmodel_TestElementToTestElementMap" = None, testmodel_TestElement35: "testmodel_TestElementToTestElementMap" = None, testmodel_TestElement38: "testmodel_StringToTestElementMap" = None):
        self.name = name
        self.strings = strings
        self.description = description
        self.testmodel_TestElement21 = testmodel_TestElement21 if testmodel_TestElement21 is not None else set()
        self.testmodel_TestElement23 = testmodel_TestElement23 if testmodel_TestElement23 is not None else set()
        self.testmodel_TestElement25 = testmodel_TestElement25 if testmodel_TestElement25 is not None else set()
        self.TestElement = TestElement
        self.testmodel_TestElement29 = testmodel_TestElement29
        self.testmodel_TestElement = testmodel_TestElement
        self.testmodel_TestElement0 = testmodel_TestElement0 if testmodel_TestElement0 is not None else set()
        self.testmodel_TestElement4 = testmodel_TestElement4
        self.testmodel_TestElement2 = testmodel_TestElement2 if testmodel_TestElement2 is not None else set()
        self.testmodel_TestElement7 = testmodel_TestElement7
        self.testmodel_TestElement5 = testmodel_TestElement5
        self.testmodel_TestElement10 = testmodel_TestElement10
        self.testmodel_TestElement8 = testmodel_TestElement8
        self.testmodel_TestElement13 = testmodel_TestElement13
        self.testmodel_TestElement11 = testmodel_TestElement11
        self.testmodel_TestElement16 = testmodel_TestElement16
        self.testmodel_TestElement14 = testmodel_TestElement14 if testmodel_TestElement14 is not None else set()
        self.elements = elements
        self.testmodel_TestElement19 = testmodel_TestElement19 if testmodel_TestElement19 is not None else set()
        self.testmodel_TestElement32 = testmodel_TestElement32
        self.testmodel_TestElement35 = testmodel_TestElement35
        self.testmodel_TestElement38 = testmodel_TestElement38
        
    @property
    def strings(self) -> str:
        return self.__strings

    @strings.setter
    def strings(self, strings: str):
        self.__strings = strings

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def testmodel_TestElement0(self):
        return self.__testmodel_TestElement0

    @testmodel_TestElement0.setter
    def testmodel_TestElement0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testmodel_TestElement__testmodel_TestElement0", None)
        self.__testmodel_TestElement0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "testmodel_TestElement"):
                    opp_val = getattr(item, "testmodel_TestElement", None)
                    
                    if opp_val == self:
                        setattr(item, "testmodel_TestElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "testmodel_TestElement"):
                    opp_val = getattr(item, "testmodel_TestElement", None)
                    
                    setattr(item, "testmodel_TestElement", self)
                    

    @property
    def elements(self):
        return self.__elements

    @elements.setter
    def elements(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testmodel_TestElement__elements", None)
        self.__elements = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TestElementContainer"):
                opp_val = getattr(old_value, "TestElementContainer", None)
                if opp_val == self:
                    setattr(old_value, "TestElementContainer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TestElementContainer"):
                opp_val = getattr(value, "TestElementContainer", None)
                setattr(value, "TestElementContainer", self)

    @property
    def testmodel_TestElement4(self):
        return self.__testmodel_TestElement4

    @testmodel_TestElement4.setter
    def testmodel_TestElement4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testmodel_TestElement__testmodel_TestElement4", None)
        self.__testmodel_TestElement4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "testmodel_TestElement2"):
                opp_val = getattr(old_value, "testmodel_TestElement2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "testmodel_TestElement2"):
                opp_val = getattr(value, "testmodel_TestElement2", None)
                if opp_val is None:
                    setattr(value, "testmodel_TestElement2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def testmodel_TestElement32(self):
        return self.__testmodel_TestElement32

    @testmodel_TestElement32.setter
    def testmodel_TestElement32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testmodel_TestElement__testmodel_TestElement32", None)
        self.__testmodel_TestElement32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "testmodel_TestElementToTestElementMap31"):
                opp_val = getattr(old_value, "testmodel_TestElementToTestElementMap31", None)
                if opp_val == self:
                    setattr(old_value, "testmodel_TestElementToTestElementMap31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "testmodel_TestElementToTestElementMap31"):
                opp_val = getattr(value, "testmodel_TestElementToTestElementMap31", None)
                setattr(value, "testmodel_TestElementToTestElementMap31", self)

    @property
    def testmodel_TestElement38(self):
        return self.__testmodel_TestElement38

    @testmodel_TestElement38.setter
    def testmodel_TestElement38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testmodel_TestElement__testmodel_TestElement38", None)
        self.__testmodel_TestElement38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "testmodel_StringToTestElementMap37"):
                opp_val = getattr(old_value, "testmodel_StringToTestElementMap37", None)
                if opp_val == self:
                    setattr(old_value, "testmodel_StringToTestElementMap37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "testmodel_StringToTestElementMap37"):
                opp_val = getattr(value, "testmodel_StringToTestElementMap37", None)
                setattr(value, "testmodel_StringToTestElementMap37", self)

    @property
    def testmodel_TestElement25(self):
        return self.__testmodel_TestElement25

    @testmodel_TestElement25.setter
    def testmodel_TestElement25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testmodel_TestElement__testmodel_TestElement25", None)
        self.__testmodel_TestElement25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "testmodel_StringToTestElementMap"):
                    opp_val = getattr(item, "testmodel_StringToTestElementMap", None)
                    
                    if opp_val == self:
                        setattr(item, "testmodel_StringToTestElementMap", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "testmodel_StringToTestElementMap"):
                    opp_val = getattr(item, "testmodel_StringToTestElementMap", None)
                    
                    setattr(item, "testmodel_StringToTestElementMap", self)
                    

    @property
    def testmodel_TestElement14(self):
        return self.__testmodel_TestElement14

    @testmodel_TestElement14.setter
    def testmodel_TestElement14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testmodel_TestElement__testmodel_TestElement14", None)
        self.__testmodel_TestElement14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "testmodel_TestElement16"):
                    opp_val = getattr(item, "testmodel_TestElement16", None)
                    
                    if opp_val == self:
                        setattr(item, "testmodel_TestElement16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "testmodel_TestElement16"):
                    opp_val = getattr(item, "testmodel_TestElement16", None)
                    
                    setattr(item, "testmodel_TestElement16", self)
                    

    @property
    def testmodel_TestElement8(self):
        return self.__testmodel_TestElement8

    @testmodel_TestElement8.setter
    def testmodel_TestElement8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testmodel_TestElement__testmodel_TestElement8", None)
        self.__testmodel_TestElement8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "testmodel_TestElement10"):
                opp_val = getattr(old_value, "testmodel_TestElement10", None)
                if opp_val == self:
                    setattr(old_value, "testmodel_TestElement10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "testmodel_TestElement10"):
                opp_val = getattr(value, "testmodel_TestElement10", None)
                setattr(value, "testmodel_TestElement10", self)

    @property
    def testmodel_TestElement16(self):
        return self.__testmodel_TestElement16

    @testmodel_TestElement16.setter
    def testmodel_TestElement16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testmodel_TestElement__testmodel_TestElement16", None)
        self.__testmodel_TestElement16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "testmodel_TestElement14"):
                opp_val = getattr(old_value, "testmodel_TestElement14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "testmodel_TestElement14"):
                opp_val = getattr(value, "testmodel_TestElement14", None)
                if opp_val is None:
                    setattr(value, "testmodel_TestElement14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def testmodel_TestElement10(self):
        return self.__testmodel_TestElement10

    @testmodel_TestElement10.setter
    def testmodel_TestElement10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testmodel_TestElement__testmodel_TestElement10", None)
        self.__testmodel_TestElement10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "testmodel_TestElement8"):
                opp_val = getattr(old_value, "testmodel_TestElement8", None)
                if opp_val == self:
                    setattr(old_value, "testmodel_TestElement8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "testmodel_TestElement8"):
                opp_val = getattr(value, "testmodel_TestElement8", None)
                setattr(value, "testmodel_TestElement8", self)

    @property
    def testmodel_TestElement2(self):
        return self.__testmodel_TestElement2

    @testmodel_TestElement2.setter
    def testmodel_TestElement2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testmodel_TestElement__testmodel_TestElement2", None)
        self.__testmodel_TestElement2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "testmodel_TestElement4"):
                    opp_val = getattr(item, "testmodel_TestElement4", None)
                    
                    if opp_val == self:
                        setattr(item, "testmodel_TestElement4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "testmodel_TestElement4"):
                    opp_val = getattr(item, "testmodel_TestElement4", None)
                    
                    setattr(item, "testmodel_TestElement4", self)
                    

    @property
    def testmodel_TestElement13(self):
        return self.__testmodel_TestElement13

    @testmodel_TestElement13.setter
    def testmodel_TestElement13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testmodel_TestElement__testmodel_TestElement13", None)
        self.__testmodel_TestElement13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "testmodel_TestElement11"):
                opp_val = getattr(old_value, "testmodel_TestElement11", None)
                if opp_val == self:
                    setattr(old_value, "testmodel_TestElement11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "testmodel_TestElement11"):
                opp_val = getattr(value, "testmodel_TestElement11", None)
                setattr(value, "testmodel_TestElement11", self)

    @property
    def testmodel_TestElement21(self):
        return self.__testmodel_TestElement21

    @testmodel_TestElement21.setter
    def testmodel_TestElement21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testmodel_TestElement__testmodel_TestElement21", None)
        self.__testmodel_TestElement21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "testmodel_StringToStringMap"):
                    opp_val = getattr(item, "testmodel_StringToStringMap", None)
                    
                    if opp_val == self:
                        setattr(item, "testmodel_StringToStringMap", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "testmodel_StringToStringMap"):
                    opp_val = getattr(item, "testmodel_StringToStringMap", None)
                    
                    setattr(item, "testmodel_StringToStringMap", self)
                    

    @property
    def testmodel_TestElement19(self):
        return self.__testmodel_TestElement19

    @testmodel_TestElement19.setter
    def testmodel_TestElement19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testmodel_TestElement__testmodel_TestElement19", None)
        self.__testmodel_TestElement19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "testmodel_TestElementToTestElementMap"):
                    opp_val = getattr(item, "testmodel_TestElementToTestElementMap", None)
                    
                    if opp_val == self:
                        setattr(item, "testmodel_TestElementToTestElementMap", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "testmodel_TestElementToTestElementMap"):
                    opp_val = getattr(item, "testmodel_TestElementToTestElementMap", None)
                    
                    setattr(item, "testmodel_TestElementToTestElementMap", self)
                    

    @property
    def testmodel_TestElement11(self):
        return self.__testmodel_TestElement11

    @testmodel_TestElement11.setter
    def testmodel_TestElement11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testmodel_TestElement__testmodel_TestElement11", None)
        self.__testmodel_TestElement11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "testmodel_TestElement13"):
                opp_val = getattr(old_value, "testmodel_TestElement13", None)
                if opp_val == self:
                    setattr(old_value, "testmodel_TestElement13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "testmodel_TestElement13"):
                opp_val = getattr(value, "testmodel_TestElement13", None)
                setattr(value, "testmodel_TestElement13", self)

    @property
    def testmodel_TestElement5(self):
        return self.__testmodel_TestElement5

    @testmodel_TestElement5.setter
    def testmodel_TestElement5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testmodel_TestElement__testmodel_TestElement5", None)
        self.__testmodel_TestElement5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "testmodel_TestElement7"):
                opp_val = getattr(old_value, "testmodel_TestElement7", None)
                if opp_val == self:
                    setattr(old_value, "testmodel_TestElement7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "testmodel_TestElement7"):
                opp_val = getattr(value, "testmodel_TestElement7", None)
                setattr(value, "testmodel_TestElement7", self)

    @property
    def TestElement(self):
        return self.__TestElement

    @TestElement.setter
    def TestElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testmodel_TestElement__TestElement", None)
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
    def testmodel_TestElement35(self):
        return self.__testmodel_TestElement35

    @testmodel_TestElement35.setter
    def testmodel_TestElement35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testmodel_TestElement__testmodel_TestElement35", None)
        self.__testmodel_TestElement35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "testmodel_TestElementToTestElementMap34"):
                opp_val = getattr(old_value, "testmodel_TestElementToTestElementMap34", None)
                if opp_val == self:
                    setattr(old_value, "testmodel_TestElementToTestElementMap34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "testmodel_TestElementToTestElementMap34"):
                opp_val = getattr(value, "testmodel_TestElementToTestElementMap34", None)
                setattr(value, "testmodel_TestElementToTestElementMap34", self)

    @property
    def testmodel_TestElement(self):
        return self.__testmodel_TestElement

    @testmodel_TestElement.setter
    def testmodel_TestElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testmodel_TestElement__testmodel_TestElement", None)
        self.__testmodel_TestElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "testmodel_TestElement0"):
                opp_val = getattr(old_value, "testmodel_TestElement0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "testmodel_TestElement0"):
                opp_val = getattr(value, "testmodel_TestElement0", None)
                if opp_val is None:
                    setattr(value, "testmodel_TestElement0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def testmodel_TestElement23(self):
        return self.__testmodel_TestElement23

    @testmodel_TestElement23.setter
    def testmodel_TestElement23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testmodel_TestElement__testmodel_TestElement23", None)
        self.__testmodel_TestElement23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "testmodel_TestElementToStringMap"):
                    opp_val = getattr(item, "testmodel_TestElementToStringMap", None)
                    
                    if opp_val == self:
                        setattr(item, "testmodel_TestElementToStringMap", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "testmodel_TestElementToStringMap"):
                    opp_val = getattr(item, "testmodel_TestElementToStringMap", None)
                    
                    setattr(item, "testmodel_TestElementToStringMap", self)
                    

    @property
    def testmodel_TestElement7(self):
        return self.__testmodel_TestElement7

    @testmodel_TestElement7.setter
    def testmodel_TestElement7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testmodel_TestElement__testmodel_TestElement7", None)
        self.__testmodel_TestElement7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "testmodel_TestElement5"):
                opp_val = getattr(old_value, "testmodel_TestElement5", None)
                if opp_val == self:
                    setattr(old_value, "testmodel_TestElement5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "testmodel_TestElement5"):
                opp_val = getattr(value, "testmodel_TestElement5", None)
                setattr(value, "testmodel_TestElement5", self)

    @property
    def testmodel_TestElement29(self):
        return self.__testmodel_TestElement29

    @testmodel_TestElement29.setter
    def testmodel_TestElement29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testmodel_TestElement__testmodel_TestElement29", None)
        self.__testmodel_TestElement29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "testmodel_TestElementToStringMap28"):
                opp_val = getattr(old_value, "testmodel_TestElementToStringMap28", None)
                if opp_val == self:
                    setattr(old_value, "testmodel_TestElementToStringMap28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "testmodel_TestElementToStringMap28"):
                opp_val = getattr(value, "testmodel_TestElementToStringMap28", None)
                setattr(value, "testmodel_TestElementToStringMap28", self)
