from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class C2:

    pass
class ecoreJavascriptTest_C3(C2):

    pass
class ecoreJavascriptTest_C1:

    def __init__(self, name: str, c1: set["ecoreJavascriptTest_C2"] = None, ecoreJavascriptTest_C1: "ecoreJavascriptTest_C1" = None, ecoreJavascriptTest_C11: set["ecoreJavascriptTest_C1"] = None, C1: "ecoreJavascriptTest_C2" = None):
        self.name = name
        self.c1 = c1 if c1 is not None else set()
        self.ecoreJavascriptTest_C1 = ecoreJavascriptTest_C1
        self.ecoreJavascriptTest_C11 = ecoreJavascriptTest_C11 if ecoreJavascriptTest_C11 is not None else set()
        self.C1 = C1
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ecoreJavascriptTest_C1(self):
        return self.__ecoreJavascriptTest_C1

    @ecoreJavascriptTest_C1.setter
    def ecoreJavascriptTest_C1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreJavascriptTest_C1__ecoreJavascriptTest_C1", None)
        self.__ecoreJavascriptTest_C1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreJavascriptTest_C11"):
                opp_val = getattr(old_value, "ecoreJavascriptTest_C11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreJavascriptTest_C11"):
                opp_val = getattr(value, "ecoreJavascriptTest_C11", None)
                if opp_val is None:
                    setattr(value, "ecoreJavascriptTest_C11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def c1(self):
        return self.__c1

    @c1.setter
    def c1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreJavascriptTest_C1__c1", None)
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
                    

    @property
    def ecoreJavascriptTest_C11(self):
        return self.__ecoreJavascriptTest_C11

    @ecoreJavascriptTest_C11.setter
    def ecoreJavascriptTest_C11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreJavascriptTest_C1__ecoreJavascriptTest_C11", None)
        self.__ecoreJavascriptTest_C11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecoreJavascriptTest_C1"):
                    opp_val = getattr(item, "ecoreJavascriptTest_C1", None)
                    
                    if opp_val == self:
                        setattr(item, "ecoreJavascriptTest_C1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecoreJavascriptTest_C1"):
                    opp_val = getattr(item, "ecoreJavascriptTest_C1", None)
                    
                    setattr(item, "ecoreJavascriptTest_C1", self)
                    

    @property
    def C1(self):
        return self.__C1

    @C1.setter
    def C1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreJavascriptTest_C1__C1", None)
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

class ecoreJavascriptTest_C2:

    def __init__(self, name: str, value: int, C2: "ecoreJavascriptTest_C1" = None, c2s: "ecoreJavascriptTest_C1" = None):
        self.name = name
        self.value = value
        self.C2 = C2
        self.c2s = c2s
        
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
    def c2s(self):
        return self.__c2s

    @c2s.setter
    def c2s(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreJavascriptTest_C2__c2s", None)
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
        old_value = getattr(self, f"_ecoreJavascriptTest_C2__C2", None)
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
