from __future__ import annotations
from datetime import datetime, date, time
from abc import ABC, abstractmethod

############################################
# Definition of Classes
############################################










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



class R2:

    pass


class B2:

    def __init__(self, attB: int, c6: set["C4"] = None, a9: "A2" = None):
        self.attB = attB
        self.c6 = c6 if c6 is not None else set()
        self.a9 = a9
        
        pass
    @property
    def attB(self):
        return self.__attB
    @attB.setter
    def attB(self, attB: int):
        self.__attB = attB

    @property
    def c6(self):
        return self.__c6
    @c6.setter
    def c6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B2__c6", None)
        self.__c6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "b7"):
                    opp_val = getattr(item, "b7", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "b7"):
                    opp_val = getattr(item, "b7", None)
                    
                    if opp_val is None:
                        setattr(item, "b7", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def a9(self):
        return self.__a9
    @a9.setter
    def a9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B2__a9", None)
        self.__a9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "b8"):
                opp_val = getattr(old_value, "b8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "b8"):
                opp_val = getattr(value, "b8", None)
                if opp_val is None:
                    setattr(value, "b8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class A2(ABC):

    def __init__(self, attA: str, b8: set["B2"] = None, r11: "R2" = None):
        self.attA = attA
        self.b8 = b8 if b8 is not None else set()
        self.r11 = r11
        
        pass
    @property
    def attA(self):
        return self.__attA
    @attA.setter
    def attA(self, attA: str):
        self.__attA = attA

    @property
    def b8(self):
        return self.__b8
    @b8.setter
    def b8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_A2__b8", None)
        self.__b8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "a9"):
                    opp_val = getattr(item, "a9", None)
                    
                    if opp_val == self:
                        setattr(item, "a9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "a9"):
                    opp_val = getattr(item, "a9", None)
                    
                    setattr(item, "a9", self)
                    

    @property
    def r11(self):
        return self.__r11
    @r11.setter
    def r11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_A2__r11", None)
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



class Z2:

    pass


class C4(ABC):

    def __init__(self, attC1: int, attC2: bool, b7: set["B2"] = None):
        self.attC1 = attC1
        self.attC2 = attC2
        self.b7 = b7 if b7 is not None else set()
        
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
    def b7(self):
        return self.__b7
    @b7.setter
    def b7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_C4__b7", None)
        self.__b7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "c6"):
                    opp_val = getattr(item, "c6", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "c6"):
                    opp_val = getattr(item, "c6", None)
                    
                    if opp_val is None:
                        setattr(item, "c6", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class C32:

    pass


class C22:

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



class R:

    pass


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
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "b1"):
                    opp_val = getattr(item, "b1", None)
                    
                    if opp_val is None:
                        setattr(item, "b1", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class A(ABC):

    def __init__(self, attA: str, r5: "R" = None, b2: set["B"] = None):
        self.attA = attA
        self.r5 = r5
        self.b2 = b2 if b2 is not None else set()
        
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
                    



class Z:

    pass


class C(ABC):

    def __init__(self, attC1: int, attC2: bool, b1: set["B"] = None):
        self.attC1 = attC1
        self.attC2 = attC2
        self.b1 = b1 if b1 is not None else set()
        
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
    def b1(self):
        return self.__b1
    @b1.setter
    def b1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_C__b1", None)
        self.__b1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "c0"):
                    opp_val = getattr(item, "c0", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "c0"):
                    opp_val = getattr(item, "c0", None)
                    
                    if opp_val is None:
                        setattr(item, "c0", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class C3:

    pass


class C2:

    pass
