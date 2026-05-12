from __future__ import annotations
from datetime import datetime, date, time
from abc import ABC, abstractmethod

############################################
# Definition of Classes
############################################










class C3:

    pass


class C2:

    pass


class C(ABC):

    def __init__(self, attC1: int, attC2: bool, b8: "B" = None):
        self.attC1 = attC1
        self.attC2 = attC2
        self.b8 = b8
        
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
    def b8(self):
        return self.__b8
    @b8.setter
    def b8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_C__b8", None)
        self.__b8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "c9"):
                opp_val = getattr(old_value, "c9", None)
                if opp_val == self:
                    setattr(old_value, "c9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "c9"):
                opp_val = getattr(value, "c9", None)
                setattr(value, "c9", self)



class Z:

    pass


class B:

    def __init__(self, attB: int, a7: "A" = None, c9: "C" = None):
        self.attB = attB
        self.a7 = a7
        self.c9 = c9
        
        pass
    @property
    def attB(self):
        return self.__attB
    @attB.setter
    def attB(self, attB: int):
        self.__attB = attB

    @property
    def a7(self):
        return self.__a7
    @a7.setter
    def a7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B__a7", None)
        self.__a7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "b6"):
                opp_val = getattr(old_value, "b6", None)
                if opp_val == self:
                    setattr(old_value, "b6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "b6"):
                opp_val = getattr(value, "b6", None)
                setattr(value, "b6", self)

    @property
    def c9(self):
        return self.__c9
    @c9.setter
    def c9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B__c9", None)
        self.__c9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "b8"):
                opp_val = getattr(old_value, "b8", None)
                if opp_val == self:
                    setattr(old_value, "b8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "b8"):
                opp_val = getattr(value, "b8", None)
                setattr(value, "b8", self)



class R:

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



class A(ABC):

    def __init__(self, attA: str, r5: "R" = None, b6: "B" = None):
        self.attA = attA
        self.r5 = r5
        self.b6 = b6
        
        pass
    @property
    def attA(self):
        return self.__attA
    @attA.setter
    def attA(self, attA: str):
        self.__attA = attA

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
    def b6(self):
        return self.__b6
    @b6.setter
    def b6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_A__b6", None)
        self.__b6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "a7"):
                opp_val = getattr(old_value, "a7", None)
                if opp_val == self:
                    setattr(old_value, "a7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "a7"):
                opp_val = getattr(value, "a7", None)
                setattr(value, "a7", self)



class Cc:

    def __init__(self, attC1: int, attC2: bool, b3: "Bb" = None):
        self.attC1 = attC1
        self.attC2 = attC2
        self.b3 = b3
        
        pass
    @property
    def attC2(self):
        return self.__attC2
    @attC2.setter
    def attC2(self, attC2: bool):
        self.__attC2 = attC2

    @property
    def attC1(self):
        return self.__attC1
    @attC1.setter
    def attC1(self, attC1: int):
        self.__attC1 = attC1

    @property
    def b3(self):
        return self.__b3
    @b3.setter
    def b3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cc__b3", None)
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



class Bb:

    def __init__(self, attB: int, a1: "Aa" = None, c2: "Cc" = None):
        self.attB = attB
        self.a1 = a1
        self.c2 = c2
        
        pass
    @property
    def attB(self):
        return self.__attB
    @attB.setter
    def attB(self, attB: int):
        self.__attB = attB

    @property
    def c2(self):
        return self.__c2
    @c2.setter
    def c2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Bb__c2", None)
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
        old_value = getattr(self, f"_Bb__a1", None)
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



class Aa:

    def __init__(self, attA: str, b0: "Bb" = None):
        self.attA = attA
        self.b0 = b0
        
        pass
    @property
    def attA(self):
        return self.__attA
    @attA.setter
    def attA(self, attA: str):
        self.__attA = attA

    @property
    def b0(self):
        return self.__b0
    @b0.setter
    def b0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Aa__b0", None)
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

