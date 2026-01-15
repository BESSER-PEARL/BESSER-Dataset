from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class mnoq_Q:

    def __init__(self, x: int, : set["mnoq_N"] = None, 7: "mnoq_N" = None):
        self.x = x
        self. =  if  is not None else set()
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
        old_value = getattr(self, f"_mnoq_Q__7", None)
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
    def (self):
        return self.__

    @.setter
    def (self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mnoq_Q__", None)
        self.__ = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "1"):
                    opp_val = getattr(item, "1", None)
                    
                    if opp_val == self:
                        setattr(item, "1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "1"):
                    opp_val = getattr(item, "1", None)
                    
                    setattr(item, "1", self)
                    

class mnoq_M:

    def __init__(self, x: int, 4: "mnoq_N" = None, 10: set["mnoq_N"] = None, mnoq_M: "mnoq_O" = None):
        self.x = x
        self.4 = 4
        self.10 = 10 if 10 is not None else set()
        self.mnoq_M = mnoq_M
        
    @property
    def x(self) -> int:
        return self.__x

    @x.setter
    def x(self, x: int):
        self.__x = x

    @property
    def 4(self):
        return self.__4

    @4.setter
    def 4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mnoq_M__4", None)
        self.__4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "3"):
                opp_val = getattr(old_value, "3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "3"):
                opp_val = getattr(value, "3", None)
                if opp_val is None:
                    setattr(value, "3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mnoq_M(self):
        return self.__mnoq_M

    @mnoq_M.setter
    def mnoq_M(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mnoq_M__mnoq_M", None)
        self.__mnoq_M = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mnoq_O"):
                opp_val = getattr(old_value, "mnoq_O", None)
                if opp_val == self:
                    setattr(old_value, "mnoq_O", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mnoq_O"):
                opp_val = getattr(value, "mnoq_O", None)
                setattr(value, "mnoq_O", self)

    @property
    def 10(self):
        return self.__10

    @10.setter
    def 10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mnoq_M__10", None)
        self.__10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "11"):
                    opp_val = getattr(item, "11", None)
                    
                    if opp_val == self:
                        setattr(item, "11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "11"):
                    opp_val = getattr(item, "11", None)
                    
                    setattr(item, "11", self)
                    

class mnoq_N:

    def __init__(self, x: int, 1: "mnoq_Q" = None, 3: set["mnoq_M"] = None, 6: set["mnoq_Q"] = None, mnoq_N: "mnoq_Foo" = None, 11: "mnoq_M" = None):
        self.x = x
        self.1 = 1
        self.3 = 3 if 3 is not None else set()
        self.6 = 6 if 6 is not None else set()
        self.mnoq_N = mnoq_N
        self.11 = 11
        
    @property
    def x(self) -> int:
        return self.__x

    @x.setter
    def x(self, x: int):
        self.__x = x

    @property
    def 1(self):
        return self.__1

    @1.setter
    def 1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mnoq_N__1", None)
        self.__1 = value
        
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
    def 3(self):
        return self.__3

    @3.setter
    def 3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mnoq_N__3", None)
        self.__3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "4"):
                    opp_val = getattr(item, "4", None)
                    
                    if opp_val == self:
                        setattr(item, "4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "4"):
                    opp_val = getattr(item, "4", None)
                    
                    setattr(item, "4", self)
                    

    @property
    def 6(self):
        return self.__6

    @6.setter
    def 6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mnoq_N__6", None)
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
    def mnoq_N(self):
        return self.__mnoq_N

    @mnoq_N.setter
    def mnoq_N(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mnoq_N__mnoq_N", None)
        self.__mnoq_N = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mnoq_Foo"):
                opp_val = getattr(old_value, "mnoq_Foo", None)
                if opp_val == self:
                    setattr(old_value, "mnoq_Foo", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mnoq_Foo"):
                opp_val = getattr(value, "mnoq_Foo", None)
                setattr(value, "mnoq_Foo", self)

    @property
    def 11(self):
        return self.__11

    @11.setter
    def 11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mnoq_N__11", None)
        self.__11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "10"):
                opp_val = getattr(old_value, "10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "10"):
                opp_val = getattr(value, "10", None)
                if opp_val is None:
                    setattr(value, "10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class mnoq_O:

    def __init__(self, x: int, mnoq_O: "mnoq_M" = None):
        self.x = x
        self.mnoq_O = mnoq_O
        
    @property
    def x(self) -> int:
        return self.__x

    @x.setter
    def x(self, x: int):
        self.__x = x

    @property
    def mnoq_O(self):
        return self.__mnoq_O

    @mnoq_O.setter
    def mnoq_O(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mnoq_O__mnoq_O", None)
        self.__mnoq_O = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mnoq_M"):
                opp_val = getattr(old_value, "mnoq_M", None)
                if opp_val == self:
                    setattr(old_value, "mnoq_M", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mnoq_M"):
                opp_val = getattr(value, "mnoq_M", None)
                setattr(value, "mnoq_M", self)

class mnoq_Foo:

    pass