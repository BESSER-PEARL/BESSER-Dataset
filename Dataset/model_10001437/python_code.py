from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class B:

    def __init__(self, attB: int, g_re1: "A" = None):
        self.attB = attB
        self.g_re1 = g_re1
        
        pass
    @property
    def attB(self):
        return self.__attB
    @attB.setter
    def attB(self, attB: int):
        self.__attB = attB

    @property
    def g_re1(self):
        return self.__g_re1
    @g_re1.setter
    def g_re1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B__g_re1", None)
        self.__g_re1 = value
        
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
                if hasattr(item, "g_re1"):
                    opp_val = getattr(item, "g_re1", None)
                    
                    if opp_val == self:
                        setattr(item, "g_re1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "g_re1"):
                    opp_val = getattr(item, "g_re1", None)
                    
                    setattr(item, "g_re1", self)
                    

