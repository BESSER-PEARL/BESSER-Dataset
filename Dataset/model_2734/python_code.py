from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class abc_A:

    def __init__(self, x: int, : set["abc_B"] = None, abc_A: "abc_C" = None, 7: "abc_B" = None):
        self.x = x
        self. =  if  is not None else set()
        self.abc_A = abc_A
        self.7 = 7
        
    @property
    def x(self) -> int:
        return self.__x

    @x.setter
    def x(self, x: int):
        self.__x = x

    @property
    def 7(self):
        return self.__7

    @7.setter
    def 7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abc_A__7", None)
        self.__7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "6"):
                opp_val = getattr(old_value, "6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "6"):
                opp_val = getattr(value, "6", None)
                if opp_val is None:
                    setattr(value, "6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "abc_C4"):
                opp_val = getattr(old_value, "abc_C4", None)
                if opp_val == self:
                    setattr(old_value, "abc_C4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "abc_C4"):
                opp_val = getattr(value, "abc_C4", None)
                setattr(value, "abc_C4", self)

    @property
    def (self):
        return self.__

    @.setter
    def (self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abc_A__", None)
        self.__ = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "2"):
                    opp_val = getattr(item, "2", None)
                    
                    if opp_val == self:
                        setattr(item, "2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "2"):
                    opp_val = getattr(item, "2", None)
                    
                    setattr(item, "2", self)
                    

class abc_B:

    def __init__(self, x: int, abc_B: "abc_C" = None, 2: "abc_A" = None, 6: set["abc_A"] = None):
        self.x = x
        self.abc_B = abc_B
        self.2 = 2
        self.6 = 6 if 6 is not None else set()
        
    @property
    def x(self) -> int:
        return self.__x

    @x.setter
    def x(self, x: int):
        self.__x = x

    @property
    def 6(self):
        return self.__6

    @6.setter
    def 6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abc_B__6", None)
        self.__6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "7"):
                    opp_val = getattr(item, "7", None)
                    
                    if opp_val == self:
                        setattr(item, "7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "7"):
                    opp_val = getattr(item, "7", None)
                    
                    setattr(item, "7", self)
                    

    @property
    def 2(self):
        return self.__2

    @2.setter
    def 2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abc_B__2", None)
        self.__2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, ""):
                opp_val = getattr(old_value, "", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, ""):
                opp_val = getattr(value, "", None)
                if opp_val is None:
                    setattr(value, "", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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

class abc_C:

    def __init__(self, x: int, abc_C: set["abc_B"] = None, abc_C4: "abc_A" = None):
        self.x = x
        self.abc_C = abc_C if abc_C is not None else set()
        self.abc_C4 = abc_C4
        
    @property
    def x(self) -> int:
        return self.__x

    @x.setter
    def x(self, x: int):
        self.__x = x

    @property
    def abc_C4(self):
        return self.__abc_C4

    @abc_C4.setter
    def abc_C4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_abc_C__abc_C4", None)
        self.__abc_C4 = value
        
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
                    
