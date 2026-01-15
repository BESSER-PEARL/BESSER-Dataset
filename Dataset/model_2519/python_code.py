from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class E:

    pass
class ext_ExtE(E):

    def __init__(self, value: int, e: set["ext_F"] = None, ExtE: "ext_F" = None):
        self.value = value
        self.e = e if e is not None else set()
        self.ExtE = ExtE
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def e(self):
        return self.__e

    @e.setter
    def e(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ext_ExtE__e", None)
        self.__e = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "F"):
                    opp_val = getattr(item, "F", None)
                    
                    if opp_val == self:
                        setattr(item, "F", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "F"):
                    opp_val = getattr(item, "F", None)
                    
                    setattr(item, "F", self)
                    

    @property
    def ExtE(self):
        return self.__ExtE

    @ExtE.setter
    def ExtE(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ext_ExtE__ExtE", None)
        self.__ExtE = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "f"):
                opp_val = getattr(old_value, "f", None)
                if opp_val == self:
                    setattr(old_value, "f", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "f"):
                opp_val = getattr(value, "f", None)
                setattr(value, "f", self)

class ext_F:

    def __init__(self, id: str, F: "ext_ExtE" = None, f: "ext_ExtE" = None):
        self.id = id
        self.F = F
        self.f = f
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def F(self):
        return self.__F

    @F.setter
    def F(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ext_F__F", None)
        self.__F = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "e"):
                opp_val = getattr(old_value, "e", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "e"):
                opp_val = getattr(value, "e", None)
                if opp_val is None:
                    setattr(value, "e", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def f(self):
        return self.__f

    @f.setter
    def f(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ext_F__f", None)
        self.__f = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ExtE"):
                opp_val = getattr(old_value, "ExtE", None)
                if opp_val == self:
                    setattr(old_value, "ExtE", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ExtE"):
                opp_val = getattr(value, "ExtE", None)
                setattr(value, "ExtE", self)
