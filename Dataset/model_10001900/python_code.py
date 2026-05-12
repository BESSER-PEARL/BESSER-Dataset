from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class C32:

    pass


class C22:

    pass


class C4:

    def __init__(self, attC: bool, attC2: int, b9: "B2" = None):
        self.attC = attC
        self.attC2 = attC2
        self.b9 = b9
        
        pass
    @property
    def attC2(self):
        return self.__attC2
    @attC2.setter
    def attC2(self, attC2: int):
        self.__attC2 = attC2

    @property
    def attC(self):
        return self.__attC
    @attC.setter
    def attC(self, attC: bool):
        self.__attC = attC

    @property
    def b9(self):
        return self.__b9
    @b9.setter
    def b9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_C4__b9", None)
        self.__b9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "c8"):
                opp_val = getattr(old_value, "c8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "c8"):
                opp_val = getattr(value, "c8", None)
                if opp_val is None:
                    setattr(value, "c8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class B2:

    def __init__(self, attB: int, a7: "A2" = None, c8: set["C4"] = None):
        self.attB = attB
        self.a7 = a7
        self.c8 = c8 if c8 is not None else set()
        
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
        old_value = getattr(self, f"_B2__a7", None)
        self.__a7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "b6"):
                opp_val = getattr(old_value, "b6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "b6"):
                opp_val = getattr(value, "b6", None)
                if opp_val is None:
                    setattr(value, "b6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def c8(self):
        return self.__c8
    @c8.setter
    def c8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B2__c8", None)
        self.__c8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "b9"):
                    opp_val = getattr(item, "b9", None)
                    
                    if opp_val == self:
                        setattr(item, "b9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "b9"):
                    opp_val = getattr(item, "b9", None)
                    
                    setattr(item, "b9", self)
                    



class Z2:

    pass


class A2:

    def __init__(self, attA: str, r5: "R2" = None, b6: set["B2"] = None):
        self.attA = attA
        self.r5 = r5
        self.b6 = b6 if b6 is not None else set()
        
        pass
    @property
    def attA(self):
        return self.__attA
    @attA.setter
    def attA(self, attA: str):
        self.__attA = attA

    @property
    def b6(self):
        return self.__b6
    @b6.setter
    def b6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_A2__b6", None)
        self.__b6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "a7"):
                    opp_val = getattr(item, "a7", None)
                    
                    if opp_val == self:
                        setattr(item, "a7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "a7"):
                    opp_val = getattr(item, "a7", None)
                    
                    setattr(item, "a7", self)
                    

    @property
    def r5(self):
        return self.__r5
    @r5.setter
    def r5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_A2__r5", None)
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



class R2:

    pass


class Y2:

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

    def __init__(self, attA: str, r1: "R" = None, b2: set["B"] = None):
        self.attA = attA
        self.r1 = r1
        self.b2 = b2 if b2 is not None else set()
        
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
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "a0"):
                opp_val = getattr(value, "a0", None)
                if opp_val is None:
                    setattr(value, "a0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class C3:

    pass


class C2:

    pass


class R:

    pass


class Z:

    pass


class B:

    def __init__(self, attB: int, a3: "A" = None):
        self.attB = attB
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

