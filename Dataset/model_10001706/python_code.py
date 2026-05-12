from __future__ import annotations
from datetime import datetime, date, time
from abc import ABC, abstractmethod

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



class A(ABC):

    def __init__(self, attA: str, b2: set["B"] = None, r5: "R" = None):
        self.attA = attA
        self.b2 = b2 if b2 is not None else set()
        self.r5 = r5
        
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
            if hasattr(old_value, "aR4"):
                opp_val = getattr(old_value, "aR4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aR4"):
                opp_val = getattr(value, "aR4", None)
                if opp_val is None:
                    setattr(value, "aR4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class C(ABC):

    def __init__(self, atC1: int, attC2: bool, b1: "B" = None):
        self.atC1 = atC1
        self.attC2 = attC2
        self.b1 = b1
        
        pass
    @property
    def atC1(self):
        return self.__atC1
    @atC1.setter
    def atC1(self, atC1: int):
        self.__atC1 = atC1

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
                    

