from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class lhs_B:

    def __init__(self, b: str, lhs_B: "lhs_A" = None, lhs_B5: "lhs_C" = None):
        self.b = b
        self.lhs_B = lhs_B
        self.lhs_B5 = lhs_B5
        
    @property
    def b(self) -> str:
        return self.__b

    @b.setter
    def b(self, b: str):
        self.__b = b

    @property
    def lhs_B(self):
        return self.__lhs_B

    @lhs_B.setter
    def lhs_B(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lhs_B__lhs_B", None)
        self.__lhs_B = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lhs_A"):
                opp_val = getattr(old_value, "lhs_A", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lhs_A"):
                opp_val = getattr(value, "lhs_A", None)
                if opp_val is None:
                    setattr(value, "lhs_A", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def lhs_B5(self):
        return self.__lhs_B5

    @lhs_B5.setter
    def lhs_B5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lhs_B__lhs_B5", None)
        self.__lhs_B5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lhs_C4"):
                opp_val = getattr(old_value, "lhs_C4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lhs_C4"):
                opp_val = getattr(value, "lhs_C4", None)
                if opp_val is None:
                    setattr(value, "lhs_C4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class lhs_A:

    def __init__(self, a: str, lhs_A2: set["lhs_C"] = None, lhs_A: set["lhs_B"] = None):
        self.a = a
        self.lhs_A2 = lhs_A2 if lhs_A2 is not None else set()
        self.lhs_A = lhs_A if lhs_A is not None else set()
        
    @property
    def a(self) -> str:
        return self.__a

    @a.setter
    def a(self, a: str):
        self.__a = a

    @property
    def lhs_A(self):
        return self.__lhs_A

    @lhs_A.setter
    def lhs_A(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lhs_A__lhs_A", None)
        self.__lhs_A = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "lhs_B"):
                    opp_val = getattr(item, "lhs_B", None)
                    
                    if opp_val == self:
                        setattr(item, "lhs_B", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "lhs_B"):
                    opp_val = getattr(item, "lhs_B", None)
                    
                    setattr(item, "lhs_B", self)
                    

    @property
    def lhs_A2(self):
        return self.__lhs_A2

    @lhs_A2.setter
    def lhs_A2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lhs_A__lhs_A2", None)
        self.__lhs_A2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "lhs_C"):
                    opp_val = getattr(item, "lhs_C", None)
                    
                    if opp_val == self:
                        setattr(item, "lhs_C", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "lhs_C"):
                    opp_val = getattr(item, "lhs_C", None)
                    
                    setattr(item, "lhs_C", self)
                    

class lhs_C:

    def __init__(self, c: str, lhs_C: "lhs_A" = None, lhs_C4: set["lhs_B"] = None):
        self.c = c
        self.lhs_C = lhs_C
        self.lhs_C4 = lhs_C4 if lhs_C4 is not None else set()
        
    @property
    def c(self) -> str:
        return self.__c

    @c.setter
    def c(self, c: str):
        self.__c = c

    @property
    def lhs_C(self):
        return self.__lhs_C

    @lhs_C.setter
    def lhs_C(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lhs_C__lhs_C", None)
        self.__lhs_C = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lhs_A2"):
                opp_val = getattr(old_value, "lhs_A2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lhs_A2"):
                opp_val = getattr(value, "lhs_A2", None)
                if opp_val is None:
                    setattr(value, "lhs_A2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def lhs_C4(self):
        return self.__lhs_C4

    @lhs_C4.setter
    def lhs_C4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lhs_C__lhs_C4", None)
        self.__lhs_C4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "lhs_B5"):
                    opp_val = getattr(item, "lhs_B5", None)
                    
                    if opp_val == self:
                        setattr(item, "lhs_B5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "lhs_B5"):
                    opp_val = getattr(item, "lhs_B5", None)
                    
                    setattr(item, "lhs_B5", self)
                    
