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


class Z:

    pass


class R:

    pass


class C1(ABC):

    def __init__(self, attC1: int, atC2: bool, b5: "B1" = None):
        self.attC1 = attC1
        self.atC2 = atC2
        self.b5 = b5
        
        pass
    @property
    def atC2(self):
        return self.__atC2
    @atC2.setter
    def atC2(self, atC2: bool):
        self.__atC2 = atC2

    @property
    def attC1(self):
        return self.__attC1
    @attC1.setter
    def attC1(self, attC1: int):
        self.__attC1 = attC1

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
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "c4"):
                opp_val = getattr(value, "c4", None)
                if opp_val is None:
                    setattr(value, "c4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class A1(ABC):

    def __init__(self, attA: str, r7: "R" = None, b8: set["B1"] = None):
        self.attA = attA
        self.r7 = r7
        self.b8 = b8 if b8 is not None else set()
        
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
        old_value = getattr(self, f"_A1__b8", None)
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
    def r7(self):
        return self.__r7
    @r7.setter
    def r7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_A1__r7", None)
        self.__r7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aR6"):
                opp_val = getattr(old_value, "aR6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aR6"):
                opp_val = getattr(value, "aR6", None)
                if opp_val is None:
                    setattr(value, "aR6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class B1:

    def __init__(self, attB: int, c4: set["C1"] = None, a9: "A1" = None):
        self.attB = attB
        self.c4 = c4 if c4 is not None else set()
        self.a9 = a9
        
        pass
    @property
    def attB(self):
        return self.__attB
    @attB.setter
    def attB(self, attB: int):
        self.__attB = attB

    @property
    def c4(self):
        return self.__c4
    @c4.setter
    def c4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B1__c4", None)
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
                    

    @property
    def a9(self):
        return self.__a9
    @a9.setter
    def a9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B1__a9", None)
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

    def __init__(self, attC1: int, atC2: bool, b3: "B" = None):
        self.attC1 = attC1
        self.atC2 = atC2
        self.b3 = b3
        
        pass
    @property
    def atC2(self):
        return self.__atC2
    @atC2.setter
    def atC2(self, atC2: bool):
        self.__atC2 = atC2

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



class B:

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



class A:

    def __init__(self, attA: str, b0: set["B"] = None):
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
                    

