from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Z1:

    pass


class C3:

    pass


class C2:

    pass


class Z:

    pass


class Y:

    pass


class R:

    pass


class B:

    def __init__(self, altB: str, c0: set["C"] = None, a5: "A" = None):
        self.altB = altB
        self.c0 = c0 if c0 is not None else set()
        self.a5 = a5
        
        pass
    @property
    def altB(self):
        return self.__altB
    @altB.setter
    def altB(self, altB: str):
        self.__altB = altB

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
                    

    @property
    def a5(self):
        return self.__a5
    @a5.setter
    def a5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B__a5", None)
        self.__a5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "b4"):
                opp_val = getattr(old_value, "b4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "b4"):
                opp_val = getattr(value, "b4", None)
                if opp_val is None:
                    setattr(value, "b4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class A:

    def __init__(self, altA: str, r3: "R" = None, b4: set["B"] = None):
        self.altA = altA
        self.r3 = r3
        self.b4 = b4 if b4 is not None else set()
        
        pass
    @property
    def altA(self):
        return self.__altA
    @altA.setter
    def altA(self, altA: str):
        self.__altA = altA

    @property
    def r3(self):
        return self.__r3
    @r3.setter
    def r3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_A__r3", None)
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

    @property
    def b4(self):
        return self.__b4
    @b4.setter
    def b4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_A__b4", None)
        self.__b4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "a5"):
                    opp_val = getattr(item, "a5", None)
                    
                    if opp_val == self:
                        setattr(item, "a5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "a5"):
                    opp_val = getattr(item, "a5", None)
                    
                    setattr(item, "a5", self)
                    



class C:

    def __init__(self, altC1: int, altC2: bool, b1: set["B"] = None):
        self.altC1 = altC1
        self.altC2 = altC2
        self.b1 = b1 if b1 is not None else set()
        
        pass
    @property
    def altC2(self):
        return self.__altC2
    @altC2.setter
    def altC2(self, altC2: bool):
        self.__altC2 = altC2

    @property
    def altC1(self):
        return self.__altC1
    @altC1.setter
    def altC1(self, altC1: int):
        self.__altC1 = altC1

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
                    

