from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class ex1_G:

    pass
class ex1_F:

    pass
class ex1_E:

    pass
class A:

    pass
class ex1_C(A):

    pass
class ex1_B(A):

    pass
class ex1_D:

    def __init__(self, dAttr: bool, ex1_D: "ex1_A" = None, ex1_D7: "ex1_E" = None):
        self.dAttr = dAttr
        self.ex1_D = ex1_D
        self.ex1_D7 = ex1_D7
        
    @property
    def dAttr(self) -> bool:
        return self.__dAttr

    @dAttr.setter
    def dAttr(self, dAttr: bool):
        self.__dAttr = dAttr

    @property
    def ex1_D7(self):
        return self.__ex1_D7

    @ex1_D7.setter
    def ex1_D7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ex1_D__ex1_D7", None)
        self.__ex1_D7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ex1_E8"):
                opp_val = getattr(old_value, "ex1_E8", None)
                if opp_val == self:
                    setattr(old_value, "ex1_E8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ex1_E8"):
                opp_val = getattr(value, "ex1_E8", None)
                setattr(value, "ex1_E8", self)

    @property
    def ex1_D(self):
        return self.__ex1_D

    @ex1_D.setter
    def ex1_D(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ex1_D__ex1_D", None)
        self.__ex1_D = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ex1_A"):
                opp_val = getattr(old_value, "ex1_A", None)
                if opp_val == self:
                    setattr(old_value, "ex1_A", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ex1_A"):
                opp_val = getattr(value, "ex1_A", None)
                setattr(value, "ex1_A", self)

class F:

    pass
class ex1_A(F):

    def __init__(self, a1: int, ex1_A: "ex1_D" = None, ex1_A3: "ex1_A" = None, ex1_A1: "ex1_A" = None):
        self.a1 = a1
        self.ex1_A = ex1_A
        self.ex1_A3 = ex1_A3
        self.ex1_A1 = ex1_A1
        
    @property
    def a1(self) -> int:
        return self.__a1

    @a1.setter
    def a1(self, a1: int):
        self.__a1 = a1

    @property
    def ex1_A3(self):
        return self.__ex1_A3

    @ex1_A3.setter
    def ex1_A3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ex1_A__ex1_A3", None)
        self.__ex1_A3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ex1_A1"):
                opp_val = getattr(old_value, "ex1_A1", None)
                if opp_val == self:
                    setattr(old_value, "ex1_A1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ex1_A1"):
                opp_val = getattr(value, "ex1_A1", None)
                setattr(value, "ex1_A1", self)

    @property
    def ex1_A1(self):
        return self.__ex1_A1

    @ex1_A1.setter
    def ex1_A1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ex1_A__ex1_A1", None)
        self.__ex1_A1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ex1_A3"):
                opp_val = getattr(old_value, "ex1_A3", None)
                if opp_val == self:
                    setattr(old_value, "ex1_A3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ex1_A3"):
                opp_val = getattr(value, "ex1_A3", None)
                setattr(value, "ex1_A3", self)

    @property
    def ex1_A(self):
        return self.__ex1_A

    @ex1_A.setter
    def ex1_A(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ex1_A__ex1_A", None)
        self.__ex1_A = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ex1_D"):
                opp_val = getattr(old_value, "ex1_D", None)
                if opp_val == self:
                    setattr(old_value, "ex1_D", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ex1_D"):
                opp_val = getattr(value, "ex1_D", None)
                setattr(value, "ex1_D", self)
