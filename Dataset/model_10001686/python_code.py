from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class G:

    pass


class F:

    def __init__(self, attF: str):
        self.attF = attF
        
        pass
    @property
    def attF(self):
        return self.__attF
    @attF.setter
    def attF(self, attF: str):
        self.__attF = attF



class E:

    def __init__(self, attE: str, g7: "G" = None):
        self.attE = attE
        self.g7 = g7
        
        pass
    @property
    def attE(self):
        return self.__attE
    @attE.setter
    def attE(self, attE: str):
        self.__attE = attE

    @property
    def g7(self):
        return self.__g7
    @g7.setter
    def g7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_E__g7", None)
        self.__g7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "e6"):
                opp_val = getattr(old_value, "e6", None)
                if opp_val == self:
                    setattr(old_value, "e6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "e6"):
                opp_val = getattr(value, "e6", None)
                setattr(value, "e6", self)



class C2:

    pass


class C3:

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



class C:

    def __init__(self, attC1: int, attC2: str, b2: "B" = None):
        self.attC1 = attC1
        self.attC2 = attC2
        self.b2 = b2
        
        pass
    @property
    def attC2(self):
        return self.__attC2
    @attC2.setter
    def attC2(self, attC2: str):
        self.__attC2 = attC2

    @property
    def attC1(self):
        return self.__attC1
    @attC1.setter
    def attC1(self, attC1: int):
        self.__attC1 = attC1

    @property
    def b2(self):
        return self.__b2
    @b2.setter
    def b2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_C__b2", None)
        self.__b2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "c3"):
                opp_val = getattr(old_value, "c3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "c3"):
                opp_val = getattr(value, "c3", None)
                if opp_val is None:
                    setattr(value, "c3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class B:

    def __init__(self, attB: str, a1: "A" = None, c3: set["C"] = None):
        self.attB = attB
        self.a1 = a1
        self.c3 = c3 if c3 is not None else set()
        
        pass
    @property
    def attB(self):
        return self.__attB
    @attB.setter
    def attB(self, attB: str):
        self.__attB = attB

    @property
    def c3(self):
        return self.__c3
    @c3.setter
    def c3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B__c3", None)
        self.__c3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "b2"):
                    opp_val = getattr(item, "b2", None)
                    
                    if opp_val == self:
                        setattr(item, "b2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "b2"):
                    opp_val = getattr(item, "b2", None)
                    
                    setattr(item, "b2", self)
                    

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

    def __init__(self, attA: str, b0: set["B"] = None, r5: "R" = None):
        self.attA = attA
        self.b0 = b0 if b0 is not None else set()
        self.r5 = r5
        
        pass
    @property
    def attA(self):
        return self.__attA
    @attA.setter
    def attA(self, attA: str):
        self.__attA = attA

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
            if hasattr(old_value, "a4"):
                opp_val = getattr(old_value, "a4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "a4"):
                opp_val = getattr(value, "a4", None)
                if opp_val is None:
                    setattr(value, "a4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
                    

