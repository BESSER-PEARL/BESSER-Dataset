from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class A5:

    pass


class A4:

    pass


class dz_aklm:

    pass


class cxw:

    pass


class B2:

    pass


class B1:

    pass


class A1:

    def __init__(self, b: bool, d: int, c8: "B1" = None, a10: "A1" = None, a11: "A1" = None, a315: "A3" = None):
        self.b = b
        self.d = d
        self.c8 = c8
        self.a10 = a10
        self.a11 = a11
        self.a315 = a315
        
        pass
    @property
    def d(self):
        return self.__d
    @d.setter
    def d(self, d: int):
        self.__d = d

    @property
    def b(self):
        return self.__b
    @b.setter
    def b(self, b: bool):
        self.__b = b

    @property
    def a315(self):
        return self.__a315
    @a315.setter
    def a315(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_A1__a315", None)
        self.__a315 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "a14"):
                opp_val = getattr(old_value, "a14", None)
                if opp_val == self:
                    setattr(old_value, "a14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "a14"):
                opp_val = getattr(value, "a14", None)
                setattr(value, "a14", self)

    @property
    def a10(self):
        return self.__a10
    @a10.setter
    def a10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_A1__a10", None)
        self.__a10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "a11"):
                opp_val = getattr(old_value, "a11", None)
                if opp_val == self:
                    setattr(old_value, "a11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "a11"):
                opp_val = getattr(value, "a11", None)
                setattr(value, "a11", self)

    @property
    def a11(self):
        return self.__a11
    @a11.setter
    def a11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_A1__a11", None)
        self.__a11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "a10"):
                opp_val = getattr(old_value, "a10", None)
                if opp_val == self:
                    setattr(old_value, "a10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "a10"):
                opp_val = getattr(value, "a10", None)
                setattr(value, "a10", self)

    @property
    def c8(self):
        return self.__c8
    @c8.setter
    def c8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_A1__c8", None)
        self.__c8 = value
        
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



class A3:

    pass


class A2:

    pass


class C:

    def __init__(self, attC1: int, attC2: bool, c21: "C2" = None, b7: "B" = None):
        self.attC1 = attC1
        self.attC2 = attC2
        self.c21 = c21
        self.b7 = b7
        
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
    def c21(self):
        return self.__c21
    @c21.setter
    def c21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_C__c21", None)
        self.__c21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "c0"):
                opp_val = getattr(old_value, "c0", None)
                if opp_val == self:
                    setattr(old_value, "c0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "c0"):
                opp_val = getattr(value, "c0", None)
                setattr(value, "c0", self)

    @property
    def b7(self):
        return self.__b7
    @b7.setter
    def b7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_C__b7", None)
        self.__b7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "c6"):
                opp_val = getattr(old_value, "c6", None)
                if opp_val == self:
                    setattr(old_value, "c6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "c6"):
                opp_val = getattr(value, "c6", None)
                setattr(value, "c6", self)



class C3:

    pass


class C2:

    pass


class Z:

    pass


class B:

    def __init__(self, attB: int, a3: "A" = None, c6: "C" = None):
        self.attB = attB
        self.a3 = a3
        self.c6 = c6
        
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
    def c6(self):
        return self.__c6
    @c6.setter
    def c6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B__c6", None)
        self.__c6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "b7"):
                opp_val = getattr(old_value, "b7", None)
                if opp_val == self:
                    setattr(old_value, "b7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "b7"):
                opp_val = getattr(value, "b7", None)
                setattr(value, "b7", self)



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



class A:

    def __init__(self, attA: str, b2: set["B"] = None, r5: "R" = None):
        self.attA = attA
        self.b2 = b2 if b2 is not None else set()
        self.r5 = r5
        
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
            if hasattr(old_value, "aR4"):
                opp_val = getattr(old_value, "aR4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aR4"):
                opp_val = getattr(value, "aR4", None)
                if opp_val is None:
                    setattr(value, "aR4", set([self]))
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
                    

