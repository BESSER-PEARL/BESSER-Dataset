from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class C:

    def __init__(self, attrC1: int, attrC2: str, b2: set["B"] = None):
        self.attrC1 = attrC1
        self.attrC2 = attrC2
        self.b2 = b2 if b2 is not None else set()
        
        pass
    @property
    def attrC1(self):
        return self.__attrC1
    @attrC1.setter
    def attrC1(self, attrC1: int):
        self.__attrC1 = attrC1

    @property
    def attrC2(self):
        return self.__attrC2
    @attrC2.setter
    def attrC2(self, attrC2: str):
        self.__attrC2 = attrC2

    @property
    def b2(self):
        return self.__b2
    @b2.setter
    def b2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_C__b2", None)
        self.__b2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "c3"):
                    opp_val = getattr(item, "c3", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "c3"):
                    opp_val = getattr(item, "c3", None)
                    
                    if opp_val is None:
                        setattr(item, "c3", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class B:

    def __init__(self, attrB1: int, attrB2: str, a1: "A" = None, c3: set["C"] = None):
        self.attrB1 = attrB1
        self.attrB2 = attrB2
        self.a1 = a1
        self.c3 = c3 if c3 is not None else set()
        
        pass
    @property
    def attrB2(self):
        return self.__attrB2
    @attrB2.setter
    def attrB2(self, attrB2: str):
        self.__attrB2 = attrB2

    @property
    def attrB1(self):
        return self.__attrB1
    @attrB1.setter
    def attrB1(self, attrB1: int):
        self.__attrB1 = attrB1

    @property
    def c3(self):
        return self.__c3
    @c3.setter
    def c3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B__c3", None)
        self.__c3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "b2"):
                    opp_val = getattr(item, "b2", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "b2"):
                    opp_val = getattr(item, "b2", None)
                    
                    if opp_val is None:
                        setattr(item, "b2", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def a1(self):
        return self.__a1
    @a1.setter
    def a1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B__a1", None)
        self.__a1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "b0"):
                opp_val = getattr(old_value, "b0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "b0"):
                opp_val = getattr(value, "b0", None)
                if opp_val is None:
                    setattr(value, "b0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class A:

    def __init__(self, attrA1: int, attrA2: str, b0: set["B"] = None):
        self.attrA1 = attrA1
        self.attrA2 = attrA2
        self.b0 = b0 if b0 is not None else set()
        
        pass
    @property
    def attrA1(self):
        return self.__attrA1
    @attrA1.setter
    def attrA1(self, attrA1: int):
        self.__attrA1 = attrA1

    @property
    def attrA2(self):
        return self.__attrA2
    @attrA2.setter
    def attrA2(self, attrA2: str):
        self.__attrA2 = attrA2

    @property
    def b0(self):
        return self.__b0
    @b0.setter
    def b0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_A__b0", None)
        self.__b0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "a1"):
                    opp_val = getattr(item, "a1", None)
                    
                    if opp_val == self:
                        setattr(item, "a1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "a1"):
                    opp_val = getattr(item, "a1", None)
                    
                    setattr(item, "a1", self)
                    

