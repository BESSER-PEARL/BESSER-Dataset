from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class M:

    def __init__(self, attA: str, c9: "R" = None, b4: "N" = None):
        self.attA = attA
        self.c9 = c9
        self.b4 = b4
        
        pass
    @property
    def attA(self):
        return self.__attA
    @attA.setter
    def attA(self, attA: str):
        self.__attA = attA

    @property
    def b4(self):
        return self.__b4
    @b4.setter
    def b4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_M__b4", None)
        self.__b4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "a5"):
                opp_val = getattr(old_value, "a5", None)
                if opp_val == self:
                    setattr(old_value, "a5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "a5"):
                opp_val = getattr(value, "a5", None)
                setattr(value, "a5", self)

    @property
    def c9(self):
        return self.__c9
    @c9.setter
    def c9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_M__c9", None)
        self.__c9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aR8"):
                opp_val = getattr(old_value, "aR8", None)
                if opp_val == self:
                    setattr(old_value, "aR8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aR8"):
                opp_val = getattr(value, "aR8", None)
                setattr(value, "aR8", self)



class C3:

    pass


class C2:

    pass


class W:

    def __init__(self, attC1: int, attC2: bool, class37: "N" = None):
        self.attC1 = attC1
        self.attC2 = attC2
        self.class37 = class37
        
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
    def class37(self):
        return self.__class37
    @class37.setter
    def class37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_W__class37", None)
        self.__class37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "class46"):
                opp_val = getattr(old_value, "class46", None)
                if opp_val == self:
                    setattr(old_value, "class46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "class46"):
                opp_val = getattr(value, "class46", None)
                setattr(value, "class46", self)



class N:

    def __init__(self, attB: int, a5: "M" = None, class46: "W" = None):
        self.attB = attB
        self.a5 = a5
        self.class46 = class46
        
        pass
    @property
    def attB(self):
        return self.__attB
    @attB.setter
    def attB(self, attB: int):
        self.__attB = attB

    @property
    def class46(self):
        return self.__class46
    @class46.setter
    def class46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_N__class46", None)
        self.__class46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "class37"):
                opp_val = getattr(old_value, "class37", None)
                if opp_val == self:
                    setattr(old_value, "class37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "class37"):
                opp_val = getattr(value, "class37", None)
                setattr(value, "class37", self)

    @property
    def a5(self):
        return self.__a5
    @a5.setter
    def a5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_N__a5", None)
        self.__a5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "b4"):
                opp_val = getattr(old_value, "b4", None)
                if opp_val == self:
                    setattr(old_value, "b4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "b4"):
                opp_val = getattr(value, "b4", None)
                setattr(value, "b4", self)



class R:

    pass


class Z:

    pass


class T:

    def __init__(self, attY: str):
        self.attY = attY
        
        pass
    @property
    def attY(self):
        return self.__attY
    @attY.setter
    def attY(self, attY: str):
        self.__attY = attY



class C:

    def __init__(self, attC1: int, attC2: bool, b3: "B" = None):
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

    def __init__(self, attB: int, a1: "A" = None, c2: "C" = None):
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



class A:

    def __init__(self, attA: str, b0: "B" = None):
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

