from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class largemapvalue_StringToStringMap:

    def __init__(self, key: str, value: str, largemapvalue_StringToStringMap: "largemapvalue_TestElement" = None):
        self.key = key
        self.value = value
        self.largemapvalue_StringToStringMap = largemapvalue_StringToStringMap
        
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
    def largemapvalue_StringToStringMap(self):
        return self.__largemapvalue_StringToStringMap

    @largemapvalue_StringToStringMap.setter
    def largemapvalue_StringToStringMap(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_largemapvalue_StringToStringMap__largemapvalue_StringToStringMap", None)
        self.__largemapvalue_StringToStringMap = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "largemapvalue_TestElement"):
                opp_val = getattr(old_value, "largemapvalue_TestElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "largemapvalue_TestElement"):
                opp_val = getattr(value, "largemapvalue_TestElement", None)
                if opp_val is None:
                    setattr(value, "largemapvalue_TestElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class largemapvalue_TestElement:

    def __init__(self, testProp: str, largemapvalue_TestElement: set["largemapvalue_StringToStringMap"] = None):
        self.testProp = testProp
        self.largemapvalue_TestElement = largemapvalue_TestElement if largemapvalue_TestElement is not None else set()
        
    @property
    def testProp(self) -> str:
        return self.__testProp

    @testProp.setter
    def testProp(self, testProp: str):
        self.__testProp = testProp

    @property
    def largemapvalue_TestElement(self):
        return self.__largemapvalue_TestElement

    @largemapvalue_TestElement.setter
    def largemapvalue_TestElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_largemapvalue_TestElement__largemapvalue_TestElement", None)
        self.__largemapvalue_TestElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "largemapvalue_StringToStringMap"):
                    opp_val = getattr(item, "largemapvalue_StringToStringMap", None)
                    
                    if opp_val == self:
                        setattr(item, "largemapvalue_StringToStringMap", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "largemapvalue_StringToStringMap"):
                    opp_val = getattr(item, "largemapvalue_StringToStringMap", None)
                    
                    setattr(item, "largemapvalue_StringToStringMap", self)
                    
