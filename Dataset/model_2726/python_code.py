from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class A:

    pass
class a_C(A):

    def __init__(self, c: int, C: "a_B" = None, cc3: "a_B" = None):
        self.c = c
        self.C = C
        self.cc3 = cc3
        
    @property
    def c(self) -> int:
        return self.__c

    @c.setter
    def c(self, c: int):
        self.__c = c

    @property
    def cc3(self):
        return self.__cc3

    @cc3.setter
    def cc3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_a_C__cc3", None)
        self.__cc3 = value
        
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

    @property
    def C(self):
        return self.__C

    @C.setter
    def C(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_a_C__C", None)
        self.__C = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cc"):
                opp_val = getattr(old_value, "cc", None)
                if opp_val == self:
                    setattr(old_value, "cc", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cc"):
                opp_val = getattr(value, "cc", None)
                setattr(value, "cc", self)

class a_B:

    def __init__(self, c: float, a_B: "a_A" = None, cc: "a_C" = None, B: "a_C" = None):
        self.c = c
        self.a_B = a_B
        self.cc = cc
        self.B = B
        
    @property
    def c(self) -> float:
        return self.__c

    @c.setter
    def c(self, c: float):
        self.__c = c

    @property
    def a_B(self):
        return self.__a_B

    @a_B.setter
    def a_B(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_a_B__a_B", None)
        self.__a_B = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "a_A"):
                opp_val = getattr(old_value, "a_A", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "a_A"):
                opp_val = getattr(value, "a_A", None)
                if opp_val is None:
                    setattr(value, "a_A", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cc(self):
        return self.__cc

    @cc.setter
    def cc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_a_B__cc", None)
        self.__cc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "C"):
                opp_val = getattr(old_value, "C", None)
                if opp_val == self:
                    setattr(old_value, "C", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "C"):
                opp_val = getattr(value, "C", None)
                setattr(value, "C", self)

    @property
    def B(self):
        return self.__B

    @B.setter
    def B(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_a_B__B", None)
        self.__B = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cc3"):
                opp_val = getattr(old_value, "cc3", None)
                if opp_val == self:
                    setattr(old_value, "cc3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cc3"):
                opp_val = getattr(value, "cc3", None)
                setattr(value, "cc3", self)

class a_A:

    def __init__(self, a: str, b: str, a_A: set["a_B"] = None):
        self.a = a
        self.b = b
        self.a_A = a_A if a_A is not None else set()
        
    @property
    def b(self) -> str:
        return self.__b

    @b.setter
    def b(self, b: str):
        self.__b = b

    @property
    def a(self) -> str:
        return self.__a

    @a.setter
    def a(self, a: str):
        self.__a = a

    @property
    def a_A(self):
        return self.__a_A

    @a_A.setter
    def a_A(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_a_A__a_A", None)
        self.__a_A = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "a_B"):
                    opp_val = getattr(item, "a_B", None)
                    
                    if opp_val == self:
                        setattr(item, "a_B", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "a_B"):
                    opp_val = getattr(item, "a_B", None)
                    
                    setattr(item, "a_B", self)
                    

    def foo(self, b: str, a: int):
        # TODO: Implement foo method
        pass
