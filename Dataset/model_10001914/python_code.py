from __future__ import annotations
from datetime import datetime, date, time
from abc import ABC, abstractmethod

############################################
# Definition of Classes
############################################










class Z:

    pass


class C3:

    pass


class C2:

    pass


class C(ABC):

    def __init__(self, attC1: int, attC2: bool, b9: "B" = None):
        self.attC1 = attC1
        self.attC2 = attC2
        self.b9 = b9
        
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
    def b9(self):
        return self.__b9
    @b9.setter
    def b9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_C__b9", None)
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



class B:

    def __init__(self, attB: int, a7: "A" = None, c8: set["C"] = None):
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
    def c8(self):
        return self.__c8
    @c8.setter
    def c8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B__c8", None)
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



class R:

    pass


class A(ABC):

    def __init__(self, attA: str, r4: "R" = None, b6: set["B"] = None):
        self.attA = attA
        self.r4 = r4
        self.b6 = b6 if b6 is not None else set()
        
        pass
    @property
    def attA(self):
        return self.__attA
    @attA.setter
    def attA(self, attA: str):
        self.__attA = attA

    @property
    def r4(self):
        return self.__r4
    @r4.setter
    def r4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_A__r4", None)
        self.__r4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aR5"):
                opp_val = getattr(old_value, "aR5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aR5"):
                opp_val = getattr(value, "aR5", None)
                if opp_val is None:
                    setattr(value, "aR5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def b6(self):
        return self.__b6
    @b6.setter
    def b6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_A__b6", None)
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



class C1:

    def __init__(self, attC1: int, attC2: bool, test3: "B1" = None):
        self.attC1 = attC1
        self.attC2 = attC2
        self.test3 = test3
        
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
    def test3(self):
        return self.__test3
    @test3.setter
    def test3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_C1__test3", None)
        self.__test3 = value
        
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



class B1:

    def __init__(self, attB: int, a1: "A1" = None, c2: set["C1"] = None):
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
        old_value = getattr(self, f"_B1__a1", None)
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
        old_value = getattr(self, f"_B1__c2", None)
        self.__c2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "test3"):
                    opp_val = getattr(item, "test3", None)
                    
                    if opp_val == self:
                        setattr(item, "test3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "test3"):
                    opp_val = getattr(item, "test3", None)
                    
                    setattr(item, "test3", self)
                    



class A1:

    def __init__(self, attA: str, b0: set["B1"] = None):
        self.attA = attA
        self.b0 = b0 if b0 is not None else set()
        
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
        old_value = getattr(self, f"_A1__b0", None)
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
                    

