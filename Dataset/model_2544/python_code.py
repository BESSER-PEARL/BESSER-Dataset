from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class foo_J:

    pass
class foo_I:

    pass
class I:

    pass
class foo_E:

    pass
class B:

    pass
class foo_D(B):

    pass
class foo_H:

    def __init__(self, EAttribute0: str):
        self.EAttribute0 = EAttribute0
        
    @property
    def EAttribute0(self) -> str:
        return self.__EAttribute0

    @EAttribute0.setter
    def EAttribute0(self, EAttribute0: str):
        self.__EAttribute0 = EAttribute0

class J:

    pass
class foo_C(B):

    def __init__(self, EAttribute1: float, foo_C: "foo_A" = None):
        self.EAttribute1 = EAttribute1
        self.foo_C = foo_C
        
    @property
    def EAttribute1(self) -> float:
        return self.__EAttribute1

    @EAttribute1.setter
    def EAttribute1(self, EAttribute1: float):
        self.__EAttribute1 = EAttribute1

    @property
    def foo_C(self):
        return self.__foo_C

    @foo_C.setter
    def foo_C(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foo_C__foo_C", None)
        self.__foo_C = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "foo_A2"):
                opp_val = getattr(old_value, "foo_A2", None)
                if opp_val == self:
                    setattr(old_value, "foo_A2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "foo_A2"):
                opp_val = getattr(value, "foo_A2", None)
                setattr(value, "foo_A2", self)

class foo_F(I):

    pass
class foo_A:

    def __init__(self, fooA: bool, fooo: str, foo_A: "foo_B" = None, foo_A2: "foo_C" = None):
        self.fooA = fooA
        self.fooo = fooo
        self.foo_A = foo_A
        self.foo_A2 = foo_A2
        
    @property
    def fooA(self) -> bool:
        return self.__fooA

    @fooA.setter
    def fooA(self, fooA: bool):
        self.__fooA = fooA

    @property
    def fooo(self) -> str:
        return self.__fooo

    @fooo.setter
    def fooo(self, fooo: str):
        self.__fooo = fooo

    @property
    def foo_A2(self):
        return self.__foo_A2

    @foo_A2.setter
    def foo_A2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foo_A__foo_A2", None)
        self.__foo_A2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "foo_C"):
                opp_val = getattr(old_value, "foo_C", None)
                if opp_val == self:
                    setattr(old_value, "foo_C", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "foo_C"):
                opp_val = getattr(value, "foo_C", None)
                setattr(value, "foo_C", self)

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
            if hasattr(old_value, "foo_B"):
                opp_val = getattr(old_value, "foo_B", None)
                if opp_val == self:
                    setattr(old_value, "foo_B", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "foo_B"):
                opp_val = getattr(value, "foo_B", None)
                setattr(value, "foo_B", self)

class foo_B(J):

    def __init__(self, EAttribute0: bool, foo_B: "foo_A" = None, foo_B4: "foo_F" = None):
        self.EAttribute0 = EAttribute0
        self.foo_B = foo_B
        self.foo_B4 = foo_B4
        
    @property
    def EAttribute0(self) -> bool:
        return self.__EAttribute0

    @EAttribute0.setter
    def EAttribute0(self, EAttribute0: bool):
        self.__EAttribute0 = EAttribute0

    @property
    def foo_B4(self):
        return self.__foo_B4

    @foo_B4.setter
    def foo_B4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foo_B__foo_B4", None)
        self.__foo_B4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "foo_F"):
                opp_val = getattr(old_value, "foo_F", None)
                if opp_val == self:
                    setattr(old_value, "foo_F", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "foo_F"):
                opp_val = getattr(value, "foo_F", None)
                setattr(value, "foo_F", self)

    @property
    def foo_B(self):
        return self.__foo_B

    @foo_B.setter
    def foo_B(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foo_B__foo_B", None)
        self.__foo_B = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "foo_A"):
                opp_val = getattr(old_value, "foo_A", None)
                if opp_val == self:
                    setattr(old_value, "foo_A", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "foo_A"):
                opp_val = getattr(value, "foo_A", None)
                setattr(value, "foo_A", self)
