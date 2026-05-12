from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class C1:

    def __init__(self, attc1: int, attc2: bool, b3: "B1" = None):
        self.attc1 = attc1
        self.attc2 = attc2
        self.b3 = b3
        
        pass
    @property
    def attc2(self):
        return self.__attc2
    @attc2.setter
    def attc2(self, attc2: bool):
        self.__attc2 = attc2

    @property
    def attc1(self):
        return self.__attc1
    @attc1.setter
    def attc1(self, attc1: int):
        self.__attc1 = attc1

    @property
    def b3(self):
        return self.__b3
    @b3.setter
    def b3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_C1__b3", None)
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



class B1:

    def __init__(self, attb: int, a1: "A1" = None, c2: set["C1"] = None):
        self.attb = attb
        self.a1 = a1
        self.c2 = c2 if c2 is not None else set()
        
        pass
    @property
    def attb(self):
        return self.__attb
    @attb.setter
    def attb(self, attb: int):
        self.__attb = attb

    @property
    def c2(self):
        return self.__c2
    @c2.setter
    def c2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B1__c2", None)
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



class A1:

    def __init__(self, atta: str, b0: set["B1"] = None):
        self.atta = atta
        self.b0 = b0 if b0 is not None else set()
        
        pass
    @property
    def atta(self):
        return self.__atta
    @atta.setter
    def atta(self, atta: str):
        self.__atta = atta

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
                    

