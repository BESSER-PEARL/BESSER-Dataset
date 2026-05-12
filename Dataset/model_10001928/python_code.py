from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Y:

    def __init__(self, attY: str):
        self.attY = attY
        
        pass
    @property
    def attY(self):
        return self.__attY
    @attY.setter
    def attY(self, attY: str):
        self.__attY = attY



class C3:

    pass


class R:

    pass


class B:

    def __init__(self, attB: int, a3: "A" = None, c4: set["C"] = None):
        self.attB = attB
        self.a3 = a3
        self.c4 = c4 if c4 is not None else set()
        
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
    def c4(self):
        return self.__c4
    @c4.setter
    def c4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B__c4", None)
        self.__c4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "b5"):
                    opp_val = getattr(item, "b5", None)
                    
                    if opp_val == self:
                        setattr(item, "b5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "b5"):
                    opp_val = getattr(item, "b5", None)
                    
                    setattr(item, "b5", self)
                    



class C:

    pass


class A:

    def __init__(self, attA: str, r1: "R" = None, b2: "B" = None):
        self.attA = attA
        self.r1 = r1
        self.b2 = b2
        
        pass
    @property
    def attA(self):
        return self.__attA
    @attA.setter
    def attA(self, attA: str):
        self.__attA = attA

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

    @property
    def r1(self):
        return self.__r1
    @r1.setter
    def r1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_A__r1", None)
        self.__r1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "a0"):
                opp_val = getattr(old_value, "a0", None)
                if opp_val == self:
                    setattr(old_value, "a0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "a0"):
                opp_val = getattr(value, "a0", None)
                setattr(value, "a0", self)



class C2:

    pass


class Z:

    pass
