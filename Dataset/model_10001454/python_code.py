from __future__ import annotations
from datetime import datetime, date, time
from abc import ABC, abstractmethod

############################################
# Definition of Classes
############################################










class R:

    pass


class C3:

    pass


class Y:

    def __init__(self, Y: str):
        self.Y = Y
        
        pass
    @property
    def Y(self):
        return self.__Y
    @Y.setter
    def Y(self, Y: str):
        self.__Y = Y



class Z:

    pass


class C2:

    pass


class C(ABC):

    def __init__(self, c: int, d: bool, b1: "B" = None):
        self.c = c
        self.d = d
        self.b1 = b1
        
        pass
    @property
    def c(self):
        return self.__c
    @c.setter
    def c(self, c: int):
        self.__c = c

    @property
    def d(self):
        return self.__d
    @d.setter
    def d(self, d: bool):
        self.__d = d

    @property
    def b1(self):
        return self.__b1
    @b1.setter
    def b1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_C__b1", None)
        self.__b1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "c0"):
                opp_val = getattr(old_value, "c0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "c0"):
                opp_val = getattr(value, "c0", None)
                if opp_val is None:
                    setattr(value, "c0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class B:

    def __init__(self, b: int, c0: set["C"] = None, a3: "A" = None):
        self.b = b
        self.c0 = c0 if c0 is not None else set()
        self.a3 = a3
        
        pass
    @property
    def b(self):
        return self.__b
    @b.setter
    def b(self, b: int):
        self.__b = b

    @property
    def a3(self):
        return self.__a3
    @a3.setter
    def a3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B__a3", None)
        self.__a3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "b2"):
                opp_val = getattr(old_value, "b2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "b2"):
                opp_val = getattr(value, "b2", None)
                if opp_val is None:
                    setattr(value, "b2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def c0(self):
        return self.__c0
    @c0.setter
    def c0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B__c0", None)
        self.__c0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "b1"):
                    opp_val = getattr(item, "b1", None)
                    
                    if opp_val == self:
                        setattr(item, "b1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "b1"):
                    opp_val = getattr(item, "b1", None)
                    
                    setattr(item, "b1", self)
                    



class A:

    def __init__(self, a: str, b2: set["B"] = None, r5: "R" = None):
        self.a = a
        self.b2 = b2 if b2 is not None else set()
        self.r5 = r5
        
        pass
    @property
    def a(self):
        return self.__a
    @a.setter
    def a(self, a: str):
        self.__a = a

    @property
    def r5(self):
        return self.__r5
    @r5.setter
    def r5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_A__r5", None)
        self.__r5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "a4"):
                opp_val = getattr(old_value, "a4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "a4"):
                opp_val = getattr(value, "a4", None)
                if opp_val is None:
                    setattr(value, "a4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def b2(self):
        return self.__b2
    @b2.setter
    def b2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_A__b2", None)
        self.__b2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "a3"):
                    opp_val = getattr(item, "a3", None)
                    
                    if opp_val == self:
                        setattr(item, "a3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "a3"):
                    opp_val = getattr(item, "a3", None)
                    
                    setattr(item, "a3", self)
                    

