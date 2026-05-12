from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class R:

    pass


class Z:

    pass


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


class C2:

    pass


class C:

    def __init__(self, attC1: int, AttC2: bool, b5: "B" = None):
        self.attC1 = attC1
        self.AttC2 = AttC2
        self.b5 = b5
        
        pass
    @property
    def attC1(self):
        return self.__attC1
    @attC1.setter
    def attC1(self, attC1: int):
        self.__attC1 = attC1

    @property
    def AttC2(self):
        return self.__AttC2
    @AttC2.setter
    def AttC2(self, AttC2: bool):
        self.__AttC2 = AttC2

    @property
    def b5(self):
        return self.__b5
    @b5.setter
    def b5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_C__b5", None)
        self.__b5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "c4"):
                opp_val = getattr(old_value, "c4", None)
                if opp_val == self:
                    setattr(old_value, "c4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "c4"):
                opp_val = getattr(value, "c4", None)
                setattr(value, "c4", self)



class B:

    def __init__(self, attB: int, a1: "A" = None, c4: "C" = None):
        self.attB = attB
        self.a1 = a1
        self.c4 = c4
        
        pass
    @property
    def attB(self):
        return self.__attB
    @attB.setter
    def attB(self, attB: int):
        self.__attB = attB

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

    @property
    def c4(self):
        return self.__c4
    @c4.setter
    def c4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B__c4", None)
        self.__c4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "b5"):
                opp_val = getattr(old_value, "b5", None)
                if opp_val == self:
                    setattr(old_value, "b5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "b5"):
                opp_val = getattr(value, "b5", None)
                setattr(value, "b5", self)



class A:

    def __init__(self, attA: str, b0: set["B"] = None, r3: "R" = None):
        self.attA = attA
        self.b0 = b0 if b0 is not None else set()
        self.r3 = r3
        
        pass
    @property
    def attA(self):
        return self.__attA
    @attA.setter
    def attA(self, attA: str):
        self.__attA = attA

    @property
    def r3(self):
        return self.__r3
    @r3.setter
    def r3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_A__r3", None)
        self.__r3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "a2"):
                opp_val = getattr(old_value, "a2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "a2"):
                opp_val = getattr(value, "a2", None)
                if opp_val is None:
                    setattr(value, "a2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
                    

