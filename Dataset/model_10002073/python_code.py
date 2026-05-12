from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class C:

    def __init__(self, attC: str):
        self.attC = attC
        
        pass
    @property
    def attC(self):
        return self.__attC
    @attC.setter
    def attC(self, attC: str):
        self.__attC = attC



class B:

    def __init__(self, attB: int, a1: "A" = None):
        self.attB = attB
        self.a1 = a1
        
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
            if hasattr(old_value, "bs0"):
                opp_val = getattr(old_value, "bs0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bs0"):
                opp_val = getattr(value, "bs0", None)
                if opp_val is None:
                    setattr(value, "bs0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class A:

    def __init__(self, attA: bool, bs0: set["B"] = None):
        self.attA = attA
        self.bs0 = bs0 if bs0 is not None else set()
        
        pass
    @property
    def attA(self):
        return self.__attA
    @attA.setter
    def attA(self, attA: bool):
        self.__attA = attA

    @property
    def bs0(self):
        return self.__bs0
    @bs0.setter
    def bs0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_A__bs0", None)
        self.__bs0 = value if value is not None else set()
        
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
                    

