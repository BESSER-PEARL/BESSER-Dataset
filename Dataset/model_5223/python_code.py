from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class E:

    pass
class linkinher_M(E):

    pass
class C:

    pass
class linkinher_T(ABC):

    pass
class linkinher_X:

    pass
class linkinher_K(C):

    pass
class S:

    pass
class linkinher_C(E, S):

    pass
class T:

    pass
class linkinher_L(C, T):

    pass
class linkinher_Named(ABC):

    def __init__(self, name: str, linkinher_Named: "linkinher_X" = None):
        self.name = name
        self.linkinher_Named = linkinher_Named
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def linkinher_Named(self):
        return self.__linkinher_Named

    @linkinher_Named.setter
    def linkinher_Named(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_linkinher_Named__linkinher_Named", None)
        self.__linkinher_Named = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "linkinher_X"):
                opp_val = getattr(old_value, "linkinher_X", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "linkinher_X"):
                opp_val = getattr(value, "linkinher_X", None)
                if opp_val is None:
                    setattr(value, "linkinher_X", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Named:

    pass
class linkinher_S(Named):

    pass
class linkinher_N(Named, T, S):

    pass
class linkinher_E(Named):

    pass