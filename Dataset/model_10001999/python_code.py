from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class C:

    def __init__(self, attrCA: int, attrC2: bool, b3: "B" = None):
        self.attrCA = attrCA
        self.attrC2 = attrC2
        self.b3 = b3
        
        pass
    @property
    def attrCA(self):
        return self.__attrCA
    @attrCA.setter
    def attrCA(self, attrCA: int):
        self.__attrCA = attrCA

    @property
    def attrC2(self):
        return self.__attrC2
    @attrC2.setter
    def attrC2(self, attrC2: bool):
        self.__attrC2 = attrC2

    @property
    def b3(self):
        return self.__b3
    @b3.setter
    def b3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_C__b3", None)
        self.__b3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "c2"):
                opp_val = getattr(old_value, "c2", None)
                if opp_val == self:
                    setattr(old_value, "c2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "c2"):
                opp_val = getattr(value, "c2", None)
                setattr(value, "c2", self)



class B:

    def __init__(self, attrB: str, a1: "A" = None, c2: "C" = None):
        self.attrB = attrB
        self.a1 = a1
        self.c2 = c2
        
        pass
    @property
    def attrB(self):
        return self.__attrB
    @attrB.setter
    def attrB(self, attrB: str):
        self.__attrB = attrB

    @property
    def c2(self):
        return self.__c2
    @c2.setter
    def c2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B__c2", None)
        self.__c2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "b3"):
                opp_val = getattr(old_value, "b3", None)
                if opp_val == self:
                    setattr(old_value, "b3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "b3"):
                opp_val = getattr(value, "b3", None)
                setattr(value, "b3", self)

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
                if opp_val == self:
                    setattr(old_value, "b0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "b0"):
                opp_val = getattr(value, "b0", None)
                setattr(value, "b0", self)



class A:

    def __init__(self, attrA: str, b0: "B" = None):
        self.attrA = attrA
        self.b0 = b0
        
        pass
    @property
    def attrA(self):
        return self.__attrA
    @attrA.setter
    def attrA(self, attrA: str):
        self.__attrA = attrA

    @property
    def b0(self):
        return self.__b0
    @b0.setter
    def b0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_A__b0", None)
        self.__b0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "a1"):
                opp_val = getattr(old_value, "a1", None)
                if opp_val == self:
                    setattr(old_value, "a1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "a1"):
                opp_val = getattr(value, "a1", None)
                setattr(value, "a1", self)

