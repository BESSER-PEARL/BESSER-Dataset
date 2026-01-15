from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class A:

    pass
class c_C(A):

    def __init__(self, c: int, z: str, C: "c_B" = None, cc9: "c_B" = None):
        self.c = c
        self.z = z
        self.C = C
        self.cc9 = cc9
        
    @property
    def z(self) -> str:
        return self.__z

    @z.setter
    def z(self, z: str):
        self.__z = z

    @property
    def c(self) -> int:
        return self.__c

    @c.setter
    def c(self, c: int):
        self.__c = c

    @property
    def cc9(self):
        return self.__cc9

    @cc9.setter
    def cc9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_c_C__cc9", None)
        self.__cc9 = value
        
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
        old_value = getattr(self, f"_c_C__C", None)
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

class c_B:

    def __init__(self, c: float, y: bool, c_B: "c_A" = None, cc: "c_C" = None, c_B3: set["c_A"] = None, c_B7: "c_B" = None, c_B5: "c_B" = None, B: "c_C" = None):
        self.c = c
        self.y = y
        self.c_B = c_B
        self.cc = cc
        self.c_B3 = c_B3 if c_B3 is not None else set()
        self.c_B7 = c_B7
        self.c_B5 = c_B5
        self.B = B
        
    @property
    def c(self) -> float:
        return self.__c

    @c.setter
    def c(self, c: float):
        self.__c = c

    @property
    def y(self) -> bool:
        return self.__y

    @y.setter
    def y(self, y: bool):
        self.__y = y

    @property
    def cc(self):
        return self.__cc

    @cc.setter
    def cc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_c_B__cc", None)
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
    def c_B5(self):
        return self.__c_B5

    @c_B5.setter
    def c_B5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_c_B__c_B5", None)
        self.__c_B5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "c_B7"):
                opp_val = getattr(old_value, "c_B7", None)
                if opp_val == self:
                    setattr(old_value, "c_B7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "c_B7"):
                opp_val = getattr(value, "c_B7", None)
                setattr(value, "c_B7", self)

    @property
    def c_B(self):
        return self.__c_B

    @c_B.setter
    def c_B(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_c_B__c_B", None)
        self.__c_B = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "c_A"):
                opp_val = getattr(old_value, "c_A", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "c_A"):
                opp_val = getattr(value, "c_A", None)
                if opp_val is None:
                    setattr(value, "c_A", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def B(self):
        return self.__B

    @B.setter
    def B(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_c_B__B", None)
        self.__B = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cc9"):
                opp_val = getattr(old_value, "cc9", None)
                if opp_val == self:
                    setattr(old_value, "cc9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cc9"):
                opp_val = getattr(value, "cc9", None)
                setattr(value, "cc9", self)

    @property
    def c_B7(self):
        return self.__c_B7

    @c_B7.setter
    def c_B7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_c_B__c_B7", None)
        self.__c_B7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "c_B5"):
                opp_val = getattr(old_value, "c_B5", None)
                if opp_val == self:
                    setattr(old_value, "c_B5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "c_B5"):
                opp_val = getattr(value, "c_B5", None)
                setattr(value, "c_B5", self)

    @property
    def c_B3(self):
        return self.__c_B3

    @c_B3.setter
    def c_B3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_c_B__c_B3", None)
        self.__c_B3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "c_A4"):
                    opp_val = getattr(item, "c_A4", None)
                    
                    if opp_val == self:
                        setattr(item, "c_A4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "c_A4"):
                    opp_val = getattr(item, "c_A4", None)
                    
                    setattr(item, "c_A4", self)
                    

class c_A:

    def __init__(self, a: str, b: str, x: str, c_A: set["c_B"] = None, c_A4: "c_B" = None):
        self.a = a
        self.b = b
        self.x = x
        self.c_A = c_A if c_A is not None else set()
        self.c_A4 = c_A4
        
    @property
    def b(self) -> str:
        return self.__b

    @b.setter
    def b(self, b: str):
        self.__b = b

    @property
    def x(self) -> str:
        return self.__x

    @x.setter
    def x(self, x: str):
        self.__x = x

    @property
    def a(self) -> str:
        return self.__a

    @a.setter
    def a(self, a: str):
        self.__a = a

    @property
    def c_A(self):
        return self.__c_A

    @c_A.setter
    def c_A(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_c_A__c_A", None)
        self.__c_A = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "c_B"):
                    opp_val = getattr(item, "c_B", None)
                    
                    if opp_val == self:
                        setattr(item, "c_B", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "c_B"):
                    opp_val = getattr(item, "c_B", None)
                    
                    setattr(item, "c_B", self)
                    

    @property
    def c_A4(self):
        return self.__c_A4

    @c_A4.setter
    def c_A4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_c_A__c_A4", None)
        self.__c_A4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "c_B3"):
                opp_val = getattr(old_value, "c_B3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "c_B3"):
                opp_val = getattr(value, "c_B3", None)
                if opp_val is None:
                    setattr(value, "c_B3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def bar(self) -> str:
        # TODO: Implement bar method
        pass

    def foo(self, b: str, a: int):
        # TODO: Implement foo method
        pass
