from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class A:

    pass
class g_C(A):

    def __init__(self, z: str):
        self.z = z
        
    @property
    def z(self) -> str:
        return self.__z

    @z.setter
    def z(self, z: str):
        self.__z = z

class g_B:

    def __init__(self, y: bool, g_B: set["g_A"] = None, g_B3: "g_B" = None, g_B1: "g_B" = None):
        self.y = y
        self.g_B = g_B if g_B is not None else set()
        self.g_B3 = g_B3
        self.g_B1 = g_B1
        
    @property
    def y(self) -> bool:
        return self.__y

    @y.setter
    def y(self, y: bool):
        self.__y = y

    @property
    def g_B(self):
        return self.__g_B

    @g_B.setter
    def g_B(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_g_B__g_B", None)
        self.__g_B = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "g_A"):
                    opp_val = getattr(item, "g_A", None)
                    
                    if opp_val == self:
                        setattr(item, "g_A", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "g_A"):
                    opp_val = getattr(item, "g_A", None)
                    
                    setattr(item, "g_A", self)
                    

    @property
    def g_B3(self):
        return self.__g_B3

    @g_B3.setter
    def g_B3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_g_B__g_B3", None)
        self.__g_B3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "g_B1"):
                opp_val = getattr(old_value, "g_B1", None)
                if opp_val == self:
                    setattr(old_value, "g_B1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "g_B1"):
                opp_val = getattr(value, "g_B1", None)
                setattr(value, "g_B1", self)

    @property
    def g_B1(self):
        return self.__g_B1

    @g_B1.setter
    def g_B1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_g_B__g_B1", None)
        self.__g_B1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "g_B3"):
                opp_val = getattr(old_value, "g_B3", None)
                if opp_val == self:
                    setattr(old_value, "g_B3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "g_B3"):
                opp_val = getattr(value, "g_B3", None)
                setattr(value, "g_B3", self)

class g_A:

    def __init__(self, x: str, g_A: "g_B" = None):
        self.x = x
        self.g_A = g_A
        
    @property
    def x(self) -> str:
        return self.__x

    @x.setter
    def x(self, x: str):
        self.__x = x

    @property
    def g_A(self):
        return self.__g_A

    @g_A.setter
    def g_A(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_g_A__g_A", None)
        self.__g_A = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "g_B"):
                opp_val = getattr(old_value, "g_B", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "g_B"):
                opp_val = getattr(value, "g_B", None)
                if opp_val is None:
                    setattr(value, "g_B", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def bar(self) -> str:
        # TODO: Implement bar method
        pass

class g_Y:

    def __init__(self, a: str, g_Y: "g_X" = None):
        self.a = a
        self.g_Y = g_Y
        
    @property
    def a(self) -> str:
        return self.__a

    @a.setter
    def a(self, a: str):
        self.__a = a

    @property
    def g_Y(self):
        return self.__g_Y

    @g_Y.setter
    def g_Y(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_g_Y__g_Y", None)
        self.__g_Y = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "g_X"):
                opp_val = getattr(old_value, "g_X", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "g_X"):
                opp_val = getattr(value, "g_X", None)
                if opp_val is None:
                    setattr(value, "g_X", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class g_X:

    def __init__(self, g_X: set["g_Y"] = None):
        self.g_X = g_X if g_X is not None else set()
        
    @property
    def g_X(self):
        return self.__g_X

    @g_X.setter
    def g_X(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_g_X__g_X", None)
        self.__g_X = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "g_Y"):
                    opp_val = getattr(item, "g_Y", None)
                    
                    if opp_val == self:
                        setattr(item, "g_Y", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "g_Y"):
                    opp_val = getattr(item, "g_Y", None)
                    
                    setattr(item, "g_Y", self)
                    

    def foo(self):
        # TODO: Implement foo method
        pass
