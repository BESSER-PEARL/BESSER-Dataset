from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class e_Y:

    def __init__(self, a: str):
        self.a = a
        
    @property
    def a(self) -> str:
        return self.__a

    @a.setter
    def a(self, a: str):
        self.__a = a

class e_Z:

    def __init__(self, b: int, e_Z: "e_B" = None):
        self.b = b
        self.e_Z = e_Z
        
    @property
    def b(self) -> int:
        return self.__b

    @b.setter
    def b(self, b: int):
        self.__b = b

    @property
    def e_Z(self):
        return self.__e_Z

    @e_Z.setter
    def e_Z(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_e_Z__e_Z", None)
        self.__e_Z = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "e_B5"):
                opp_val = getattr(old_value, "e_B5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "e_B5"):
                opp_val = getattr(value, "e_B5", None)
                if opp_val is None:
                    setattr(value, "e_B5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Y:

    pass
class e_B(Y):

    def __init__(self, c: float, e_B5: set["e_Z"] = None, cc: "e_C" = None, B: "e_C" = None, e_B: "e_A" = None, e_B3: "e_A" = None):
        self.c = c
        self.e_B5 = e_B5 if e_B5 is not None else set()
        self.cc = cc
        self.B = B
        self.e_B = e_B
        self.e_B3 = e_B3
        
    @property
    def c(self) -> float:
        return self.__c

    @c.setter
    def c(self, c: float):
        self.__c = c

    @property
    def B(self):
        return self.__B

    @B.setter
    def B(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_e_B__B", None)
        self.__B = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cc8"):
                opp_val = getattr(old_value, "cc8", None)
                if opp_val == self:
                    setattr(old_value, "cc8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cc8"):
                opp_val = getattr(value, "cc8", None)
                setattr(value, "cc8", self)

    @property
    def cc(self):
        return self.__cc

    @cc.setter
    def cc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_e_B__cc", None)
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
    def e_B(self):
        return self.__e_B

    @e_B.setter
    def e_B(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_e_B__e_B", None)
        self.__e_B = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "e_A"):
                opp_val = getattr(old_value, "e_A", None)
                if opp_val == self:
                    setattr(old_value, "e_A", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "e_A"):
                opp_val = getattr(value, "e_A", None)
                setattr(value, "e_A", self)

    @property
    def e_B5(self):
        return self.__e_B5

    @e_B5.setter
    def e_B5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_e_B__e_B5", None)
        self.__e_B5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "e_Z"):
                    opp_val = getattr(item, "e_Z", None)
                    
                    if opp_val == self:
                        setattr(item, "e_Z", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "e_Z"):
                    opp_val = getattr(item, "e_Z", None)
                    
                    setattr(item, "e_Z", self)
                    

    @property
    def e_B3(self):
        return self.__e_B3

    @e_B3.setter
    def e_B3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_e_B__e_B3", None)
        self.__e_B3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "e_A2"):
                opp_val = getattr(old_value, "e_A2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "e_A2"):
                opp_val = getattr(value, "e_A2", None)
                if opp_val is None:
                    setattr(value, "e_A2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class A:

    pass
class e_X(A):

    def __init__(self):
        
    def bar(self, aaa: Y):
        # TODO: Implement bar method
        pass

class e_C(A):

    def __init__(self, c: int, C: "e_B" = None, cc8: "e_B" = None):
        self.c = c
        self.C = C
        self.cc8 = cc8
        
    @property
    def c(self) -> int:
        return self.__c

    @c.setter
    def c(self, c: int):
        self.__c = c

    @property
    def cc8(self):
        return self.__cc8

    @cc8.setter
    def cc8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_e_C__cc8", None)
        self.__cc8 = value
        
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
        old_value = getattr(self, f"_e_C__C", None)
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

class e_A:

    def __init__(self, a: str, b: str, e_A: "e_B" = None, e_A2: set["e_B"] = None):
        self.a = a
        self.b = b
        self.e_A = e_A
        self.e_A2 = e_A2 if e_A2 is not None else set()
        
    @property
    def a(self) -> str:
        return self.__a

    @a.setter
    def a(self, a: str):
        self.__a = a

    @property
    def b(self) -> str:
        return self.__b

    @b.setter
    def b(self, b: str):
        self.__b = b

    @property
    def e_A2(self):
        return self.__e_A2

    @e_A2.setter
    def e_A2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_e_A__e_A2", None)
        self.__e_A2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "e_B3"):
                    opp_val = getattr(item, "e_B3", None)
                    
                    if opp_val == self:
                        setattr(item, "e_B3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "e_B3"):
                    opp_val = getattr(item, "e_B3", None)
                    
                    setattr(item, "e_B3", self)
                    

    @property
    def e_A(self):
        return self.__e_A

    @e_A.setter
    def e_A(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_e_A__e_A", None)
        self.__e_A = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "e_B"):
                opp_val = getattr(old_value, "e_B", None)
                if opp_val == self:
                    setattr(old_value, "e_B", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "e_B"):
                opp_val = getattr(value, "e_B", None)
                setattr(value, "e_B", self)

    def foo(self, a: int, b: str):
        # TODO: Implement foo method
        pass
