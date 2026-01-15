from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class foo_A:

    def __init__(self, fooA: str, foo_A: "B" = None):
        self.fooA = fooA
        self.foo_A = foo_A
        
    @property
    def fooA(self) -> str:
        return self.__fooA

    @fooA.setter
    def fooA(self, fooA: str):
        self.__fooA = fooA

    @property
    def foo_A(self):
        return self.__foo_A

    @foo_A.setter
    def foo_A(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foo_A__foo_A", None)
        self.__foo_A = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "B"):
                opp_val = getattr(old_value, "B", None)
                if opp_val == self:
                    setattr(old_value, "B", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "B"):
                opp_val = getattr(value, "B", None)
                setattr(value, "B", self)

class foo_J:

    pass
class J:

    pass
class foo_B(J):

    pass
class B:

    pass