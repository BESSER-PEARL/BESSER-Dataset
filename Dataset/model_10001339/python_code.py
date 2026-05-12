from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class C3:

    def __init__(self, i3: int):
        self.i3 = i3
        
        pass
    @property
    def i3(self):
        return self.__i3
    @i3.setter
    def i3(self, i3: int):
        self.__i3 = i3



class C2:

    def __init__(self, b1: bool, c11: "C1" = None):
        self.b1 = b1
        self.c11 = c11
        
        pass
    @property
    def b1(self):
        return self.__b1
    @b1.setter
    def b1(self, b1: bool):
        self.__b1 = b1

    @property
    def c11(self):
        return self.__c11
    @c11.setter
    def c11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_C2__c11", None)
        self.__c11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "c20"):
                opp_val = getattr(old_value, "c20", None)
                if opp_val == self:
                    setattr(old_value, "c20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "c20"):
                opp_val = getattr(value, "c20", None)
                setattr(value, "c20", self)



class C1:

    def __init__(self, i3: int, c20: "C2" = None):
        self.i3 = i3
        self.c20 = c20
        
        pass
    @property
    def i3(self):
        return self.__i3
    @i3.setter
    def i3(self, i3: int):
        self.__i3 = i3

    @property
    def c20(self):
        return self.__c20
    @c20.setter
    def c20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_C1__c20", None)
        self.__c20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "c11"):
                opp_val = getattr(old_value, "c11", None)
                if opp_val == self:
                    setattr(old_value, "c11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "c11"):
                opp_val = getattr(value, "c11", None)
                setattr(value, "c11", self)

