from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class abc_A:

    def __init__(self, x: int, a: set["abc_B"] = None, abc_A: "abc_C" = None, A: "abc_B" = None):
        self.x = x
        self.a = a if a is not None else set()
        self.abc_A = abc_A
        self.A = A
        
        pass
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x: int):
        self.__x = x


    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abc_A__a", None)
        self.__a = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "B"):
                    opp_val = getattr(item, "B", None)
                    
                    if opp_val == self:
                        setattr(item, "B", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "B"):
                    opp_val = getattr(item, "B", None)
                    
                    setattr(item, "B", self)
                    

    @property
    def abc_A(self):
        return self.__abc_A

    @abc_A.setter
    def abc_A(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abc_A__abc_A", None)
        self.__abc_A = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abc_C3"):
                opp_val = getattr(old_value, "abc_C3", None)
                if opp_val == self:
                    setattr(old_value, "abc_C3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abc_C3"):
                opp_val = getattr(value, "abc_C3", None)
                setattr(value, "abc_C3", self)

    @property
    def A(self):
        return self.__A

    @A.setter
    def A(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abc_A__A", None)
        self.__A = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "b"):
                opp_val = getattr(old_value, "b", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "b"):
                opp_val = getattr(value, "b", None)
                if opp_val is None:
                    setattr(value, "b", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class abc_B:

    def __init__(self, x: int, abc_B: "abc_C" = None, B: "abc_A" = None, b: set["abc_A"] = None):
        self.x = x
        self.abc_B = abc_B
        self.B = B
        self.b = b if b is not None else set()
        
        pass
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x: int):
        self.__x = x


    @property
    def abc_B(self):
        return self.__abc_B

    @abc_B.setter
    def abc_B(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abc_B__abc_B", None)
        self.__abc_B = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abc_C"):
                opp_val = getattr(old_value, "abc_C", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abc_C"):
                opp_val = getattr(value, "abc_C", None)
                if opp_val is None:
                    setattr(value, "abc_C", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abc_B__b", None)
        self.__b = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "A"):
                    opp_val = getattr(item, "A", None)
                    
                    if opp_val == self:
                        setattr(item, "A", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "A"):
                    opp_val = getattr(item, "A", None)
                    
                    setattr(item, "A", self)
                    

    @property
    def B(self):
        return self.__B

    @B.setter
    def B(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abc_B__B", None)
        self.__B = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "a"):
                opp_val = getattr(old_value, "a", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "a"):
                opp_val = getattr(value, "a", None)
                if opp_val is None:
                    setattr(value, "a", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class abc_C:

    def __init__(self, x: int, abc_C: set["abc_B"] = None, abc_C3: "abc_A" = None):
        self.x = x
        self.abc_C = abc_C if abc_C is not None else set()
        self.abc_C3 = abc_C3
        
        pass
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x: int):
        self.__x = x


    @property
    def abc_C3(self):
        return self.__abc_C3

    @abc_C3.setter
    def abc_C3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abc_C__abc_C3", None)
        self.__abc_C3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "abc_A"):
                opp_val = getattr(old_value, "abc_A", None)
                if opp_val == self:
                    setattr(old_value, "abc_A", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abc_A"):
                opp_val = getattr(value, "abc_A", None)
                setattr(value, "abc_A", self)

    @property
    def abc_C(self):
        return self.__abc_C

    @abc_C.setter
    def abc_C(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abc_C__abc_C", None)
        self.__abc_C = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "abc_B"):
                    opp_val = getattr(item, "abc_B", None)
                    
                    if opp_val == self:
                        setattr(item, "abc_B", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "abc_B"):
                    opp_val = getattr(item, "abc_B", None)
                    
                    setattr(item, "abc_B", self)
                    
