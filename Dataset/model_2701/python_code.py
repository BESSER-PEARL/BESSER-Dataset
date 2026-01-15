from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class A:

    pass
class ktest206_Y(A):

    pass
class Y:

    pass
class ktest206_V(Y):

    pass
class ktest206_X(Y):

    pass
class ktest206_D:

    def __init__(self, name: str, ktest206_D: "ktest206_A" = None):
        self.name = name
        self.ktest206_D = ktest206_D
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ktest206_D(self):
        return self.__ktest206_D

    @ktest206_D.setter
    def ktest206_D(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ktest206_D__ktest206_D", None)
        self.__ktest206_D = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ktest206_A"):
                opp_val = getattr(old_value, "ktest206_A", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ktest206_A"):
                opp_val = getattr(value, "ktest206_A", None)
                if opp_val is None:
                    setattr(value, "ktest206_A", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ktest206_N:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class ktest206_C:

    def __init__(self, name: str, ktest206_C: "ktest206_B" = None):
        self.name = name
        self.ktest206_C = ktest206_C
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ktest206_C(self):
        return self.__ktest206_C

    @ktest206_C.setter
    def ktest206_C(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ktest206_C__ktest206_C", None)
        self.__ktest206_C = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ktest206_B"):
                opp_val = getattr(old_value, "ktest206_B", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ktest206_B"):
                opp_val = getattr(value, "ktest206_B", None)
                if opp_val is None:
                    setattr(value, "ktest206_B", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class N:

    pass
class ktest206_W(N):

    pass
class ktest206_E(N):

    pass
class ktest206_B(N):

    pass
class B:

    pass
class ktest206_A(B):

    pass