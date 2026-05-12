from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










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



class C3:

    pass


class C2:

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



class C1:

    def __init__(self, attC1: int, attC2: bool, b8: "B1" = None):
        self.attC1 = attC1
        self.attC2 = attC2
        self.b8 = b8
        
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
    def b8(self):
        return self.__b8
    @b8.setter
    def b8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_C1__b8", None)
        self.__b8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "c9"):
                opp_val = getattr(old_value, "c9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "c9"):
                opp_val = getattr(value, "c9", None)
                if opp_val is None:
                    setattr(value, "c9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class B1:

    def __init__(self, attB: int, a5: "A1" = None, c9: set["C1"] = None):
        self.attB = attB
        self.a5 = a5
        self.c9 = c9 if c9 is not None else set()
        
        pass
    @property
    def attB(self):
        return self.__attB
    @attB.setter
    def attB(self, attB: int):
        self.__attB = attB

    @property
    def a5(self):
        return self.__a5
    @a5.setter
    def a5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B1__a5", None)
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

    @property
    def c9(self):
        return self.__c9
    @c9.setter
    def c9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B1__c9", None)
        self.__c9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "b8"):
                    opp_val = getattr(item, "b8", None)
                    
                    if opp_val == self:
                        setattr(item, "b8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "b8"):
                    opp_val = getattr(item, "b8", None)
                    
                    setattr(item, "b8", self)
                    



class A1:

    def __init__(self, attA: str, b4: set["B1"] = None, r7: "R" = None):
        self.attA = attA
        self.b4 = b4 if b4 is not None else set()
        self.r7 = r7
        
        pass
    @property
    def attA(self):
        return self.__attA
    @attA.setter
    def attA(self, attA: str):
        self.__attA = attA

    @property
    def b4(self):
        return self.__b4
    @b4.setter
    def b4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_A1__b4", None)
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



class A:

    def __init__(self, attA: str, b2: set["B"] = None):
        self.attA = attA
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
                    

