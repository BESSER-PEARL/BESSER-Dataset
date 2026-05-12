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


class C(ABC):

    def __init__(self, attc1: int, attc2: bool, B5: "B" = None):
        self.attc1 = attc1
        self.attc2 = attc2
        self.B5 = B5
        
        pass
    @property
    def attc1(self):
        return self.__attc1
    @attc1.setter
    def attc1(self, attc1: int):
        self.__attc1 = attc1

    @property
    def attc2(self):
        return self.__attc2
    @attc2.setter
    def attc2(self, attc2: bool):
        self.__attc2 = attc2

    @property
    def B5(self):
        return self.__B5
    @B5.setter
    def B5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_C__B5", None)
        self.__B5 = value
        
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



class Z:

    pass


class B:

    def __init__(self, attb: int, A3: "A" = None, c4: set["C"] = None):
        self.attb = attb
        self.A3 = A3
        self.c4 = c4 if c4 is not None else set()
        
        pass
    @property
    def attb(self):
        return self.__attb
    @attb.setter
    def attb(self, attb: int):
        self.__attb = attb

    @property
    def c4(self):
        return self.__c4
    @c4.setter
    def c4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B__c4", None)
        self.__c4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "B5"):
                    opp_val = getattr(item, "B5", None)
                    
                    if opp_val == self:
                        setattr(item, "B5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "B5"):
                    opp_val = getattr(item, "B5", None)
                    
                    setattr(item, "B5", self)
                    

    @property
    def A3(self):
        return self.__A3
    @A3.setter
    def A3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B__A3", None)
        self.__A3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "B2"):
                opp_val = getattr(old_value, "B2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "B2"):
                opp_val = getattr(value, "B2", None)
                if opp_val is None:
                    setattr(value, "B2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class A(ABC):

    def __init__(self, attA: str, r1: "r" = None, B2: set["B"] = None):
        self.attA = attA
        self.r1 = r1
        self.B2 = B2 if B2 is not None else set()
        
        pass
    @property
    def attA(self):
        return self.__attA
    @attA.setter
    def attA(self, attA: str):
        self.__attA = attA

    @property
    def B2(self):
        return self.__B2
    @B2.setter
    def B2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_A__B2", None)
        self.__B2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "A3"):
                    opp_val = getattr(item, "A3", None)
                    
                    if opp_val == self:
                        setattr(item, "A3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "A3"):
                    opp_val = getattr(item, "A3", None)
                    
                    setattr(item, "A3", self)
                    

    @property
    def r1(self):
        return self.__r1
    @r1.setter
    def r1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_A__r1", None)
        self.__r1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aR0"):
                opp_val = getattr(old_value, "aR0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aR0"):
                opp_val = getattr(value, "aR0", None)
                if opp_val is None:
                    setattr(value, "aR0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class r:

    pass


class y:

    def __init__(self, attY: str):
        self.attY = attY
        
        pass
    @property
    def attY(self):
        return self.__attY
    @attY.setter
    def attY(self, attY: str):
        self.__attY = attY

