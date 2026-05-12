from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class c3:

    pass


class c2:

    pass


class c:

    def __init__(self, att1: int, att2: bool):
        self.att1 = att1
        self.att2 = att2
        
        pass
    @property
    def att1(self):
        return self.__att1
    @att1.setter
    def att1(self, att1: int):
        self.__att1 = att1

    @property
    def att2(self):
        return self.__att2
    @att2.setter
    def att2(self, att2: bool):
        self.__att2 = att2



class B1:

    def __init__(self, attb: int, a5: "A1" = None):
        self.attb = attb
        self.a5 = a5
        
        pass
    @property
    def attb(self):
        return self.__attb
    @attb.setter
    def attb(self, attb: int):
        self.__attb = attb

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



class Z:

    pass


class A1:

    def __init__(self, atta: str, b4: set["B1"] = None, r7: "R" = None):
        self.atta = atta
        self.b4 = b4 if b4 is not None else set()
        self.r7 = r7
        
        pass
    @property
    def atta(self):
        return self.__atta
    @atta.setter
    def atta(self, atta: str):
        self.__atta = atta

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
                    



class R:

    pass


class Y:

    def __init__(self, atty: str):
        self.atty = atty
        
        pass
    @property
    def atty(self):
        return self.__atty
    @atty.setter
    def atty(self, atty: str):
        self.__atty = atty



class C:

    def __init__(self, att1: int, att2: bool, b3: set["B"] = None):
        self.att1 = att1
        self.att2 = att2
        self.b3 = b3 if b3 is not None else set()
        
        pass
    @property
    def att1(self):
        return self.__att1
    @att1.setter
    def att1(self, att1: int):
        self.__att1 = att1

    @property
    def att2(self):
        return self.__att2
    @att2.setter
    def att2(self, att2: bool):
        self.__att2 = att2

    @property
    def b3(self):
        return self.__b3
    @b3.setter
    def b3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_C__b3", None)
        self.__b3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "c2"):
                    opp_val = getattr(item, "c2", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "c2"):
                    opp_val = getattr(item, "c2", None)
                    
                    if opp_val is None:
                        setattr(item, "c2", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class B:

    def __init__(self, attb: int, a1: "A" = None, c2: set["C"] = None):
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
        old_value = getattr(self, f"_B__c2", None)
        self.__c2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "b3"):
                    opp_val = getattr(item, "b3", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "b3"):
                    opp_val = getattr(item, "b3", None)
                    
                    if opp_val is None:
                        setattr(item, "b3", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

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



class A:

    def __init__(self, atta: str, b0: set["B"] = None):
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
                    

