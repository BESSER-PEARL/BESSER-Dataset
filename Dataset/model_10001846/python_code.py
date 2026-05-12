from __future__ import annotations
from datetime import datetime, date, time
from abc import ABC, abstractmethod

############################################
# Definition of Classes
############################################










class C32:

    pass


class C22:

    pass


class Z2:

    pass


class R2:

    pass


class Y2:

    def __init__(self, alty: str):
        self.alty = alty
        
        pass
    @property
    def alty(self):
        return self.__alty
    @alty.setter
    def alty(self, alty: str):
        self.__alty = alty



class C12:

    def __init__(self, altC1: int, altc2: bool, b11: "B12" = None):
        self.altC1 = altC1
        self.altc2 = altc2
        self.b11 = b11
        
        pass
    @property
    def altC1(self):
        return self.__altC1
    @altC1.setter
    def altC1(self, altC1: int):
        self.__altC1 = altC1

    @property
    def altc2(self):
        return self.__altc2
    @altc2.setter
    def altc2(self, altc2: bool):
        self.__altc2 = altc2

    @property
    def b11(self):
        return self.__b11
    @b11.setter
    def b11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_C12__b11", None)
        self.__b11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "c10"):
                opp_val = getattr(old_value, "c10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "c10"):
                opp_val = getattr(value, "c10", None)
                if opp_val is None:
                    setattr(value, "c10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class B12:

    def __init__(self, altB1: int, a7: "A12" = None, c10: set["C12"] = None):
        self.altB1 = altB1
        self.a7 = a7
        self.c10 = c10 if c10 is not None else set()
        
        pass
    @property
    def altB1(self):
        return self.__altB1
    @altB1.setter
    def altB1(self, altB1: int):
        self.__altB1 = altB1

    @property
    def c10(self):
        return self.__c10
    @c10.setter
    def c10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B12__c10", None)
        self.__c10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "b11"):
                    opp_val = getattr(item, "b11", None)
                    
                    if opp_val == self:
                        setattr(item, "b11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "b11"):
                    opp_val = getattr(item, "b11", None)
                    
                    setattr(item, "b11", self)
                    

    @property
    def a7(self):
        return self.__a7
    @a7.setter
    def a7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B12__a7", None)
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



class A12(ABC):

    def __init__(self, altA: str, b6: set["B12"] = None, r9: "R2" = None):
        self.altA = altA
        self.b6 = b6 if b6 is not None else set()
        self.r9 = r9
        
        pass
    @property
    def altA(self):
        return self.__altA
    @altA.setter
    def altA(self, altA: str):
        self.__altA = altA

    @property
    def b6(self):
        return self.__b6
    @b6.setter
    def b6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_A12__b6", None)
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
    def r9(self):
        return self.__r9
    @r9.setter
    def r9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_A12__r9", None)
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



class C3:

    pass


class C2:

    pass


class Z:

    pass


class R:

    pass


class Y:

    def __init__(self, alty: str):
        self.alty = alty
        
        pass
    @property
    def alty(self):
        return self.__alty
    @alty.setter
    def alty(self, alty: str):
        self.__alty = alty



class C1:

    def __init__(self, altC1: int, altc2: bool, b5: "B1" = None):
        self.altC1 = altC1
        self.altc2 = altc2
        self.b5 = b5
        
        pass
    @property
    def altC1(self):
        return self.__altC1
    @altC1.setter
    def altC1(self, altC1: int):
        self.__altC1 = altC1

    @property
    def altc2(self):
        return self.__altc2
    @altc2.setter
    def altc2(self, altc2: bool):
        self.__altc2 = altc2

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



class B1:

    def __init__(self, altB1: int, a1: "A1" = None, c4: set["C1"] = None):
        self.altB1 = altB1
        self.a1 = a1
        self.c4 = c4 if c4 is not None else set()
        
        pass
    @property
    def altB1(self):
        return self.__altB1
    @altB1.setter
    def altB1(self, altB1: int):
        self.__altB1 = altB1

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
                    



class A1:

    def __init__(self, altA: str, b0: set["B1"] = None, r3: "R" = None):
        self.altA = altA
        self.b0 = b0 if b0 is not None else set()
        self.r3 = r3
        
        pass
    @property
    def altA(self):
        return self.__altA
    @altA.setter
    def altA(self, altA: str):
        self.__altA = altA

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
                    

    @property
    def r3(self):
        return self.__r3
    @r3.setter
    def r3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_A1__r3", None)
        self.__r3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aR2"):
                opp_val = getattr(old_value, "aR2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aR2"):
                opp_val = getattr(value, "aR2", None)
                if opp_val is None:
                    setattr(value, "aR2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

