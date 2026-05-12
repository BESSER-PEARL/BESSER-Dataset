from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Z:

    pass


class R:

    pass


class C3:

    pass


class C2:

    pass


class C1:

    def __init__(self, attC1: bool, attC2: bool, b5: "B1" = None):
        self.attC1 = attC1
        self.attC2 = attC2
        self.b5 = b5
        
        pass
    @property
    def attC1(self):
        return self.__attC1
    @attC1.setter
    def attC1(self, attC1: bool):
        self.__attC1 = attC1

    @property
    def attC2(self):
        return self.__attC2
    @attC2.setter
    def attC2(self, attC2: bool):
        self.__attC2 = attC2

    @property
    def b5(self):
        return self.__b5
    @b5.setter
    def b5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_C1__b5", None)
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



class B1:

    def __init__(self, attB: bool, c4: "C1" = None, a7: "A1" = None):
        self.attB = attB
        self.c4 = c4
        self.a7 = a7
        
        pass
    @property
    def attB(self):
        return self.__attB
    @attB.setter
    def attB(self, attB: bool):
        self.__attB = attB

    @property
    def a7(self):
        return self.__a7
    @a7.setter
    def a7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B1__a7", None)
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
    def c4(self):
        return self.__c4
    @c4.setter
    def c4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B1__c4", None)
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



class A1:

    def __init__(self, attA: str, b6: "B1" = None, r9: "R" = None):
        self.attA = attA
        self.b6 = b6
        self.r9 = r9
        
        pass
    @property
    def attA(self):
        return self.__attA
    @attA.setter
    def attA(self, attA: str):
        self.__attA = attA

    @property
    def r9(self):
        return self.__r9
    @r9.setter
    def r9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_A1__r9", None)
        self.__r9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "a8"):
                opp_val = getattr(old_value, "a8", None)
                if opp_val == self:
                    setattr(old_value, "a8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "a8"):
                opp_val = getattr(value, "a8", None)
                setattr(value, "a8", self)

    @property
    def b6(self):
        return self.__b6
    @b6.setter
    def b6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_A1__b6", None)
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



class C:

    def __init__(self, attC1: int, attC2: bool, b1: "B" = None):
        self.attC1 = attC1
        self.attC2 = attC2
        self.b1 = b1
        
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

    def __init__(self, attB: int, c0: set["C"] = None, a3: "A" = None):
        self.attB = attB
        self.c0 = c0 if c0 is not None else set()
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

    def __init__(self, atttA: str, b2: set["B"] = None):
        self.atttA = atttA
        self.b2 = b2 if b2 is not None else set()
        
        pass
    @property
    def atttA(self):
        return self.__atttA
    @atttA.setter
    def atttA(self, atttA: str):
        self.__atttA = atttA

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
                    

