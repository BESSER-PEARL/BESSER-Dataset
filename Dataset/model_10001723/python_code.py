from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class c2:

    pass


class c1:

    pass


class y:

    def __init__(self, atty: str):
        self.atty = atty
        
        pass
    @property
    def atty(self):
        return self.__atty
    @atty.setter
    def atty(self, atty: str):
        self.__atty = atty



class z:

    pass


class r:

    pass


class B:

    def __init__(self, attb: str, c0: set["C"] = None, a3: "A" = None):
        self.attb = attb
        self.c0 = c0 if c0 is not None else set()
        self.a3 = a3
        
        pass
    @property
    def attb(self):
        return self.__attb
    @attb.setter
    def attb(self, attb: str):
        self.__attb = attb

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
                    



class C:

    def __init__(self, attc1: int, attc2: bool, b1: "B" = None):
        self.attc1 = attc1
        self.attc2 = attc2
        self.b1 = b1
        
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



class A:

    def __init__(self, atta: str, r5: "r" = None, b2: set["B"] = None):
        self.atta = atta
        self.r5 = r5
        self.b2 = b2 if b2 is not None else set()
        
        pass
    @property
    def atta(self):
        return self.__atta
    @atta.setter
    def atta(self, atta: str):
        self.__atta = atta

    @property
    def r5(self):
        return self.__r5
    @r5.setter
    def r5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_A__r5", None)
        self.__r5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ar4"):
                opp_val = getattr(old_value, "ar4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ar4"):
                opp_val = getattr(value, "ar4", None)
                if opp_val is None:
                    setattr(value, "ar4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
                    

