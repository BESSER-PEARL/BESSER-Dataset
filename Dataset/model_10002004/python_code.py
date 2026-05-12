from __future__ import annotations
from datetime import datetime, date, time
from abc import ABC, abstractmethod

############################################
# Definition of Classes
############################################










class Class2:

    pass


class Class1:

    pass


class Z:

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


class V2:

    pass


class V1:

    pass


class V(ABC):

    def __init__(self, attV1: str, attV2: bool, b9: "W" = None):
        self.attV1 = attV1
        self.attV2 = attV2
        self.b9 = b9
        
        pass
    @property
    def attV1(self):
        return self.__attV1
    @attV1.setter
    def attV1(self, attV1: str):
        self.__attV1 = attV1

    @property
    def attV2(self):
        return self.__attV2
    @attV2.setter
    def attV2(self, attV2: bool):
        self.__attV2 = attV2

    @property
    def b9(self):
        return self.__b9
    @b9.setter
    def b9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_V__b9", None)
        self.__b9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "v8"):
                opp_val = getattr(old_value, "v8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "v8"):
                opp_val = getattr(value, "v8", None)
                if opp_val is None:
                    setattr(value, "v8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class W:

    def __init__(self, attW: str, x7: "X" = None, v8: set["V"] = None):
        self.attW = attW
        self.x7 = x7
        self.v8 = v8 if v8 is not None else set()
        
        pass
    @property
    def attW(self):
        return self.__attW
    @attW.setter
    def attW(self, attW: str):
        self.__attW = attW

    @property
    def v8(self):
        return self.__v8
    @v8.setter
    def v8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_W__v8", None)
        self.__v8 = value if value is not None else set()
        
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
    def x7(self):
        return self.__x7
    @x7.setter
    def x7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_W__x7", None)
        self.__x7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "w6"):
                opp_val = getattr(old_value, "w6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "w6"):
                opp_val = getattr(value, "w6", None)
                if opp_val is None:
                    setattr(value, "w6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class X(ABC):

    def __init__(self, attX: str, r5: "R" = None, w6: set["W"] = None):
        self.attX = attX
        self.r5 = r5
        self.w6 = w6 if w6 is not None else set()
        
        pass
    @property
    def attX(self):
        return self.__attX
    @attX.setter
    def attX(self, attX: str):
        self.__attX = attX

    @property
    def r5(self):
        return self.__r5
    @r5.setter
    def r5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_X__r5", None)
        self.__r5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "x4"):
                opp_val = getattr(old_value, "x4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "x4"):
                opp_val = getattr(value, "x4", None)
                if opp_val is None:
                    setattr(value, "x4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def w6(self):
        return self.__w6
    @w6.setter
    def w6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_X__w6", None)
        self.__w6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "x7"):
                    opp_val = getattr(item, "x7", None)
                    
                    if opp_val == self:
                        setattr(item, "x7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "x7"):
                    opp_val = getattr(item, "x7", None)
                    
                    setattr(item, "x7", self)
                    



class C:

    def __init__(self, attC1: int, attC2: bool, b3: "B" = None):
        self.attC1 = attC1
        self.attC2 = attC2
        self.b3 = b3
        
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
                    

