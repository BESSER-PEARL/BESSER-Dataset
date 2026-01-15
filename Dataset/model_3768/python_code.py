from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class d_Y:

    def __init__(self, a: str):
        self.a = a
        
    @property
    def a(self) -> str:
        return self.__a

    @a.setter
    def a(self, a: str):
        self.__a = a

class A:

    pass
class d_X(A):

    def __init__(self):
        
    def baz(self, aaa: Y):
        # TODO: Implement baz method
        pass

class d_A:

    pass
class d_Z:

    def __init__(self, b: int, d_Z: "d_B" = None):
        self.b = b
        self.d_Z = d_Z
        
    @property
    def b(self) -> int:
        return self.__b

    @b.setter
    def b(self, b: int):
        self.__b = b

    @property
    def d_Z(self):
        return self.__d_Z

    @d_Z.setter
    def d_Z(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_d_Z__d_Z", None)
        self.__d_Z = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "d_B2"):
                opp_val = getattr(old_value, "d_B2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "d_B2"):
                opp_val = getattr(value, "d_B2", None)
                if opp_val is None:
                    setattr(value, "d_B2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Y:

    pass
class d_B(Y):

    pass