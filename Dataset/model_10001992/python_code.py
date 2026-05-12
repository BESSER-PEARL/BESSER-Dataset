from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class A:

    def __init__(self, attA: int, A_B_00: set["B"] = None):
        self.attA = attA
        self.A_B_00 = A_B_00 if A_B_00 is not None else set()
        
        pass
    @property
    def attA(self):
        return self.__attA
    @attA.setter
    def attA(self, attA: int):
        self.__attA = attA

    @property
    def A_B_00(self):
        return self.__A_B_00
    @A_B_00.setter
    def A_B_00(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_A__A_B_00", None)
        self.__A_B_00 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "A_B_11"):
                    opp_val = getattr(item, "A_B_11", None)
                    
                    if opp_val == self:
                        setattr(item, "A_B_11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "A_B_11"):
                    opp_val = getattr(item, "A_B_11", None)
                    
                    setattr(item, "A_B_11", self)
                    



class B:

    def __init__(self, attB: int, A_B_11: "A" = None):
        self.attB = attB
        self.A_B_11 = A_B_11
        
        pass
    @property
    def attB(self):
        return self.__attB
    @attB.setter
    def attB(self, attB: int):
        self.__attB = attB

    @property
    def A_B_11(self):
        return self.__A_B_11
    @A_B_11.setter
    def A_B_11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B__A_B_11", None)
        self.__A_B_11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "A_B_00"):
                opp_val = getattr(old_value, "A_B_00", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "A_B_00"):
                opp_val = getattr(value, "A_B_00", None)
                if opp_val is None:
                    setattr(value, "A_B_00", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

