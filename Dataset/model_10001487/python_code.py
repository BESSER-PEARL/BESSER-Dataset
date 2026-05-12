from __future__ import annotations
from datetime import datetime, date, time
from abc import ABC, abstractmethod

############################################
# Definition of Classes
############################################










class C3:

    pass


class C21:

    pass


class Z:

    pass


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



class C1(ABC):

    def __init__(self, attC1: int, attC2: bool, b6: "B1" = None):
        self.attC1 = attC1
        self.attC2 = attC2
        self.b6 = b6
        
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
    def b6(self):
        return self.__b6
    @b6.setter
    def b6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_C1__b6", None)
        self.__b6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "c7"):
                opp_val = getattr(old_value, "c7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "c7"):
                opp_val = getattr(value, "c7", None)
                if opp_val is None:
                    setattr(value, "c7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class B1:

    def __init__(self, attB: int, c7: set["C1"] = None, a11: "A1" = None):
        self.attB = attB
        self.c7 = c7 if c7 is not None else set()
        self.a11 = a11
        
        pass
    @property
    def attB(self):
        return self.__attB
    @attB.setter
    def attB(self, attB: int):
        self.__attB = attB

    @property
    def a11(self):
        return self.__a11
    @a11.setter
    def a11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B1__a11", None)
        self.__a11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "b10"):
                opp_val = getattr(old_value, "b10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "b10"):
                opp_val = getattr(value, "b10", None)
                if opp_val is None:
                    setattr(value, "b10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def c7(self):
        return self.__c7
    @c7.setter
    def c7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B1__c7", None)
        self.__c7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "b6"):
                    opp_val = getattr(item, "b6", None)
                    
                    if opp_val == self:
                        setattr(item, "b6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "b6"):
                    opp_val = getattr(item, "b6", None)
                    
                    setattr(item, "b6", self)
                    



class A1(ABC):

    def __init__(self, attA: str, r9: "R" = None, b10: set["B1"] = None):
        self.attA = attA
        self.r9 = r9
        self.b10 = b10 if b10 is not None else set()
        
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
            if hasattr(old_value, "aR8"):
                opp_val = getattr(old_value, "aR8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aR8"):
                opp_val = getattr(value, "aR8", None)
                if opp_val is None:
                    setattr(value, "aR8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def b10(self):
        return self.__b10
    @b10.setter
    def b10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_A1__b10", None)
        self.__b10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "a11"):
                    opp_val = getattr(item, "a11", None)
                    
                    if opp_val == self:
                        setattr(item, "a11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "a11"):
                    opp_val = getattr(item, "a11", None)
                    
                    setattr(item, "a11", self)
                    



class C2:

    def __init__(self, attC1: int, attC2: bool, b4: "B2" = None):
        self.attC1 = attC1
        self.attC2 = attC2
        self.b4 = b4
        
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
    def b4(self):
        return self.__b4
    @b4.setter
    def b4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_C2__b4", None)
        self.__b4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "c5"):
                opp_val = getattr(old_value, "c5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "c5"):
                opp_val = getattr(value, "c5", None)
                if opp_val is None:
                    setattr(value, "c5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class B2:

    def __init__(self, attB: int, c5: set["C2"] = None):
        self.attB = attB
        self.c5 = c5 if c5 is not None else set()
        
        pass
    @property
    def attB(self):
        return self.__attB
    @attB.setter
    def attB(self, attB: int):
        self.__attB = attB

    @property
    def c5(self):
        return self.__c5
    @c5.setter
    def c5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B2__c5", None)
        self.__c5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "b4"):
                    opp_val = getattr(item, "b4", None)
                    
                    if opp_val == self:
                        setattr(item, "b4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "b4"):
                    opp_val = getattr(item, "b4", None)
                    
                    setattr(item, "b4", self)
                    



class A2:

    def __init__(self, attA: str):
        self.attA = attA
        
        pass
    @property
    def attA(self):
        return self.__attA
    @attA.setter
    def attA(self, attA: str):
        self.__attA = attA



class C:

    def __init__(self, attC1: int, attC2: bool, b2: "B" = None):
        self.attC1 = attC1
        self.attC2 = attC2
        self.b2 = b2
        
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
    def b2(self):
        return self.__b2
    @b2.setter
    def b2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_C__b2", None)
        self.__b2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "c3"):
                opp_val = getattr(old_value, "c3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "c3"):
                opp_val = getattr(value, "c3", None)
                if opp_val is None:
                    setattr(value, "c3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class B:

    def __init__(self, attB: int, a1: "A" = None, c3: set["C"] = None):
        self.attB = attB
        self.a1 = a1
        self.c3 = c3 if c3 is not None else set()
        
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
    def c3(self):
        return self.__c3
    @c3.setter
    def c3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B__c3", None)
        self.__c3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "b2"):
                    opp_val = getattr(item, "b2", None)
                    
                    if opp_val == self:
                        setattr(item, "b2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "b2"):
                    opp_val = getattr(item, "b2", None)
                    
                    setattr(item, "b2", self)
                    



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
                    

