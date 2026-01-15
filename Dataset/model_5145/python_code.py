from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class A:

    pass
class b_C(A):

    def __init__(self, z: str):
        self.z = z
        
    @property
    def z(self) -> str:
        return self.__z

    @z.setter
    def z(self, z: str):
        self.__z = z

class b_B:

    def __init__(self, y: bool, b_B: "b_B" = None, b_B0: "b_B" = None, b_B3: set["b_A"] = None):
        self.y = y
        self.b_B = b_B
        self.b_B0 = b_B0
        self.b_B3 = b_B3 if b_B3 is not None else set()
        
    @property
    def y(self) -> bool:
        return self.__y

    @y.setter
    def y(self, y: bool):
        self.__y = y

    @property
    def b_B3(self):
        return self.__b_B3

    @b_B3.setter
    def b_B3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_b_B__b_B3", None)
        self.__b_B3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "b_A"):
                    opp_val = getattr(item, "b_A", None)
                    
                    if opp_val == self:
                        setattr(item, "b_A", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "b_A"):
                    opp_val = getattr(item, "b_A", None)
                    
                    setattr(item, "b_A", self)
                    

    @property
    def b_B(self):
        return self.__b_B

    @b_B.setter
    def b_B(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_b_B__b_B", None)
        self.__b_B = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "b_B0"):
                opp_val = getattr(old_value, "b_B0", None)
                if opp_val == self:
                    setattr(old_value, "b_B0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "b_B0"):
                opp_val = getattr(value, "b_B0", None)
                setattr(value, "b_B0", self)

    @property
    def b_B0(self):
        return self.__b_B0

    @b_B0.setter
    def b_B0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_b_B__b_B0", None)
        self.__b_B0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "b_B"):
                opp_val = getattr(old_value, "b_B", None)
                if opp_val == self:
                    setattr(old_value, "b_B", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "b_B"):
                opp_val = getattr(value, "b_B", None)
                setattr(value, "b_B", self)

class b_A:

    def __init__(self, x: str, b_A: "b_B" = None):
        self.x = x
        self.b_A = b_A
        
    @property
    def x(self) -> str:
        return self.__x

    @x.setter
    def x(self, x: str):
        self.__x = x

    @property
    def b_A(self):
        return self.__b_A

    @b_A.setter
    def b_A(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_b_A__b_A", None)
        self.__b_A = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "b_B3"):
                opp_val = getattr(old_value, "b_B3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "b_B3"):
                opp_val = getattr(value, "b_B3", None)
                if opp_val is None:
                    setattr(value, "b_B3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def bar(self) -> str:
        # TODO: Implement bar method
        pass
