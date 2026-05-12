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


class Y:

    def __init__(self, atty: str, a12: "A" = None):
        self.atty = atty
        self.a12 = a12
        
        pass
    @property
    def atty(self):
        return self.__atty
    @atty.setter
    def atty(self, atty: str):
        self.__atty = atty

    @property
    def a12(self):
        return self.__a12
    @a12.setter
    def a12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Y__a12", None)
        self.__a12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "y13"):
                opp_val = getattr(old_value, "y13", None)
                if opp_val == self:
                    setattr(old_value, "y13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "y13"):
                opp_val = getattr(value, "y13", None)
                setattr(value, "y13", self)



class R:

    pass


class Z:

    pass


class C:

    def __init__(self, attC1: int, AttC2: bool, c35: "C3" = None, c27: "C2" = None, b3: "B" = None):
        self.attC1 = attC1
        self.AttC2 = AttC2
        self.c35 = c35
        self.c27 = c27
        self.b3 = b3
        
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
    def c27(self):
        return self.__c27
    @c27.setter
    def c27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_C__c27", None)
        self.__c27 = value
        
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
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "c2"):
                opp_val = getattr(value, "c2", None)
                if opp_val is None:
                    setattr(value, "c2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def c35(self):
        return self.__c35
    @c35.setter
    def c35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_C__c35", None)
        self.__c35 = value
        
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



class B(ABC):

    def __init__(self, attB: int, a1: "A" = None, c2: set["C"] = None):
        self.attB = attB
        self.a1 = a1
        self.c2 = c2 if c2 is not None else set()
        
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
    def c2(self):
        return self.__c2
    @c2.setter
    def c2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B__c2", None)
        self.__c2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "b3"):
                    opp_val = getattr(item, "b3", None)
                    
                    if opp_val == self:
                        setattr(item, "b3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "b3"):
                    opp_val = getattr(item, "b3", None)
                    
                    setattr(item, "b3", self)
                    



class A(ABC):

    def __init__(self, attA: str, z9: "Z" = None, r11: "R" = None, y13: "Y" = None, b0: set["B"] = None):
        self.attA = attA
        self.z9 = z9
        self.r11 = r11
        self.y13 = y13
        self.b0 = b0 if b0 is not None else set()
        
        pass
    @property
    def attA(self):
        return self.__attA
    @attA.setter
    def attA(self, attA: str):
        self.__attA = attA

    @property
    def z9(self):
        return self.__z9
    @z9.setter
    def z9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_A__z9", None)
        self.__z9 = value
        
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
    def r11(self):
        return self.__r11
    @r11.setter
    def r11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_A__r11", None)
        self.__r11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aR10"):
                opp_val = getattr(old_value, "aR10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aR10"):
                opp_val = getattr(value, "aR10", None)
                if opp_val is None:
                    setattr(value, "aR10", set([self]))
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
                    

    @property
    def y13(self):
        return self.__y13
    @y13.setter
    def y13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_A__y13", None)
        self.__y13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "a12"):
                opp_val = getattr(old_value, "a12", None)
                if opp_val == self:
                    setattr(old_value, "a12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "a12"):
                opp_val = getattr(value, "a12", None)
                setattr(value, "a12", self)

