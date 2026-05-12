from __future__ import annotations
from datetime import datetime, date, time
from abc import ABC, abstractmethod

############################################
# Definition of Classes
############################################










class R:

    pass


class Z:

    pass


class C3:

    pass


class C2:

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



class Cbis(ABC):

    def __init__(self, attC1: int, attC2: bool, b7: "Bbis" = None):
        self.attC1 = attC1
        self.attC2 = attC2
        self.b7 = b7
        
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
        old_value = getattr(self, f"_Cbis__b7", None)
        self.__b7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "c6"):
                opp_val = getattr(old_value, "c6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "c6"):
                opp_val = getattr(value, "c6", None)
                if opp_val is None:
                    setattr(value, "c6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Bbis:

    def __init__(self, attB: int, a5: "Abis" = None, c6: set["Cbis"] = None):
        self.attB = attB
        self.a5 = a5
        self.c6 = c6 if c6 is not None else set()
        
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
        old_value = getattr(self, f"_Bbis__a5", None)
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
    def c6(self):
        return self.__c6
    @c6.setter
    def c6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Bbis__c6", None)
        self.__c6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "b7"):
                    opp_val = getattr(item, "b7", None)
                    
                    if opp_val == self:
                        setattr(item, "b7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "b7"):
                    opp_val = getattr(item, "b7", None)
                    
                    setattr(item, "b7", self)
                    



class Abis(ABC):

    def __init__(self, attA: str, b4: set["Bbis"] = None, r9: "R" = None):
        self.attA = attA
        self.b4 = b4 if b4 is not None else set()
        self.r9 = r9
        
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
        old_value = getattr(self, f"_Abis__b4", None)
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
    def r9(self):
        return self.__r9
    @r9.setter
    def r9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Abis__r9", None)
        self.__r9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "a8"):
                opp_val = getattr(old_value, "a8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "a8"):
                opp_val = getattr(value, "a8", None)
                if opp_val is None:
                    setattr(value, "a8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class C:

    def __init__(self, attC1: int, attC2: bool, b3: "B" = None):
        self.attC1 = attC1
        self.attC2 = attC2
        self.b3 = b3
        
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

    def __init__(self, attB: int, a0: "A" = None, c2: set["C"] = None):
        self.attB = attB
        self.a0 = a0
        self.c2 = c2 if c2 is not None else set()
        
        pass
    @property
    def attB(self):
        return self.__attB
    @attB.setter
    def attB(self, attB: int):
        self.__attB = attB

    @property
    def a0(self):
        return self.__a0
    @a0.setter
    def a0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B__a0", None)
        self.__a0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "b1"):
                opp_val = getattr(old_value, "b1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "b1"):
                opp_val = getattr(value, "b1", None)
                if opp_val is None:
                    setattr(value, "b1", set([self]))
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

    def __init__(self, attA: str, b1: set["B"] = None):
        self.attA = attA
        self.b1 = b1 if b1 is not None else set()
        
        pass
    @property
    def attA(self):
        return self.__attA
    @attA.setter
    def attA(self, attA: str):
        self.__attA = attA

    @property
    def b1(self):
        return self.__b1
    @b1.setter
    def b1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_A__b1", None)
        self.__b1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "a0"):
                    opp_val = getattr(item, "a0", None)
                    
                    if opp_val == self:
                        setattr(item, "a0", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "a0"):
                    opp_val = getattr(item, "a0", None)
                    
                    setattr(item, "a0", self)
                    

