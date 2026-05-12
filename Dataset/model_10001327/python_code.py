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

    def __init__(self, attE: str, g3: "G" = None):
        self.attE = attE
        self.g3 = g3
        
        pass
    @property
    def attE(self):
        return self.__attE
    @attE.setter
    def attE(self, attE: str):
        self.__attE = attE

    @property
    def g3(self):
        return self.__g3
    @g3.setter
    def g3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_E__g3", None)
        self.__g3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "e2"):
                opp_val = getattr(old_value, "e2", None)
                if opp_val == self:
                    setattr(old_value, "e2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "e2"):
                opp_val = getattr(value, "e2", None)
                setattr(value, "e2", self)



class B2:

    pass


class A3:

    pass


class A2:

    pass


class B:

    pass


class A:

    def __init__(self, b: bool, d: int, c0: "B" = None):
        self.b = b
        self.d = d
        self.c0 = c0
        
        pass
    @property
    def b(self):
        return self.__b
    @b.setter
    def b(self, b: bool):
        self.__b = b

    @property
    def d(self):
        return self.__d
    @d.setter
    def d(self, d: int):
        self.__d = d

    @property
    def c0(self):
        return self.__c0
    @c0.setter
    def c0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_A__c0", None)
        self.__c0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "a1"):
                opp_val = getattr(old_value, "a1", None)
                if opp_val == self:
                    setattr(old_value, "a1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "a1"):
                opp_val = getattr(value, "a1", None)
                setattr(value, "a1", self)



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



class R:

    pass


class Z:

    pass


class C2:

    pass


class C3:

    pass
