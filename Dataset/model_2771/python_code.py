from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class C2:

    pass
class javascriptSupportTest_C3(C2):

    def __init__(self, title: str):
        self.title = title
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

class javascriptSupportTest_C2:

    def __init__(self, name: str, string1: str, int1: int, C2: "javascriptSupportTest_C1" = None, c2s: "javascriptSupportTest_C1" = None):
        self.name = name
        self.string1 = string1
        self.int1 = int1
        self.C2 = C2
        self.c2s = c2s
        
    @property
    def int1(self) -> int:
        return self.__int1

    @int1.setter
    def int1(self, int1: int):
        self.__int1 = int1

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def string1(self) -> str:
        return self.__string1

    @string1.setter
    def string1(self, string1: str):
        self.__string1 = string1

    @property
    def c2s(self):
        return self.__c2s

    @c2s.setter
    def c2s(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javascriptSupportTest_C2__c2s", None)
        self.__c2s = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "C1"):
                opp_val = getattr(old_value, "C1", None)
                if opp_val == self:
                    setattr(old_value, "C1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "C1"):
                opp_val = getattr(value, "C1", None)
                setattr(value, "C1", self)

    @property
    def C2(self):
        return self.__C2

    @C2.setter
    def C2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javascriptSupportTest_C2__C2", None)
        self.__C2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "c1"):
                opp_val = getattr(old_value, "c1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "c1"):
                opp_val = getattr(value, "c1", None)
                if opp_val is None:
                    setattr(value, "c1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def getSuffixedName(self, suffix: str):
        # TODO: Implement getSuffixedName method
        pass

class javascriptSupportTest_C1:

    def __init__(self, string1: str, int1: int, name: str, c1: set["javascriptSupportTest_C2"] = None, C1: "javascriptSupportTest_C2" = None):
        self.string1 = string1
        self.int1 = int1
        self.name = name
        self.c1 = c1 if c1 is not None else set()
        self.C1 = C1
        
    @property
    def string1(self) -> str:
        return self.__string1

    @string1.setter
    def string1(self, string1: str):
        self.__string1 = string1

    @property
    def int1(self) -> int:
        return self.__int1

    @int1.setter
    def int1(self, int1: int):
        self.__int1 = int1

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def C1(self):
        return self.__C1

    @C1.setter
    def C1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javascriptSupportTest_C1__C1", None)
        self.__C1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "c2s"):
                opp_val = getattr(old_value, "c2s", None)
                if opp_val == self:
                    setattr(old_value, "c2s", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "c2s"):
                opp_val = getattr(value, "c2s", None)
                setattr(value, "c2s", self)

    @property
    def c1(self):
        return self.__c1

    @c1.setter
    def c1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javascriptSupportTest_C1__c1", None)
        self.__c1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "C2"):
                    opp_val = getattr(item, "C2", None)
                    
                    if opp_val == self:
                        setattr(item, "C2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "C2"):
                    opp_val = getattr(item, "C2", None)
                    
                    setattr(item, "C2", self)
                    

    def getPrefixedName(self, prefix: str):
        # TODO: Implement getPrefixedName method
        pass

    def createC2(self, name: str):
        # TODO: Implement createC2 method
        pass
