from __future__ import annotations
from datetime import datetime, date, time
from abc import ABC, abstractmethod

############################################
# Definition of Classes
############################################










class C2:

    pass


class C1:

    pass


class Z:

    pass


class R:

    pass


class Y:

    pass


class C(ABC):

    def __init__(self, attC1: int, attC2: bool, b0: "B" = None):
        self.attC1 = attC1
        self.attC2 = attC2
        self.b0 = b0
        
        pass
    @property
    def attC1(self):
        return self.__attC1
    @attC1.setter
    def attC1(self, attC1: int):
        self.__attC1 = attC1

    @property
    def attC2(self):
        return self.__attC2
    @attC2.setter
    def attC2(self, attC2: bool):
        self.__attC2 = attC2

    @property
    def b0(self):
        return self.__b0
    @b0.setter
    def b0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_C__b0", None)
        self.__b0 = value
        
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



class B:

    def __init__(self, attB: int, c1: set["C"] = None, a3: "A" = None):
        self.attB = attB
        self.c1 = c1 if c1 is not None else set()
        self.a3 = a3
        
        pass
    @property
    def attB(self):
        return self.__attB
    @attB.setter
    def attB(self, attB: int):
        self.__attB = attB

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
                if opp_val == self:
                    setattr(old_value, "b2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "b2"):
                opp_val = getattr(value, "b2", None)
                setattr(value, "b2", self)

    @property
    def c1(self):
        return self.__c1
    @c1.setter
    def c1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B__c1", None)
        self.__c1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "b0"):
                    opp_val = getattr(item, "b0", None)
                    
                    if opp_val == self:
                        setattr(item, "b0", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "b0"):
                    opp_val = getattr(item, "b0", None)
                    
                    setattr(item, "b0", self)
                    



class A(ABC):

    def __init__(self, attA_: str, b2: "B" = None, r5: "R" = None):
        self.attA_ = attA_
        self.b2 = b2
        self.r5 = r5
        
        pass
    @property
    def attA_(self):
        return self.__attA_
    @attA_.setter
    def attA_(self, attA_: str):
        self.__attA_ = attA_

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
                if opp_val == self:
                    setattr(old_value, "a4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "a4"):
                opp_val = getattr(value, "a4", None)
                setattr(value, "a4", self)

    @property
    def b2(self):
        return self.__b2
    @b2.setter
    def b2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_A__b2", None)
        self.__b2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "a3"):
                opp_val = getattr(old_value, "a3", None)
                if opp_val == self:
                    setattr(old_value, "a3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "a3"):
                opp_val = getattr(value, "a3", None)
                setattr(value, "a3", self)

