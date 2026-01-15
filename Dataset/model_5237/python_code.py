from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class f_Y:

    def __init__(self, a: str, f_Y: "f_X" = None):
        self.a = a
        self.f_Y = f_Y
        
    @property
    def a(self) -> str:
        return self.__a

    @a.setter
    def a(self, a: str):
        self.__a = a

    @property
    def f_Y(self):
        return self.__f_Y

    @f_Y.setter
    def f_Y(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_f_Y__f_Y", None)
        self.__f_Y = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "f_X"):
                opp_val = getattr(old_value, "f_X", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "f_X"):
                opp_val = getattr(value, "f_X", None)
                if opp_val is None:
                    setattr(value, "f_X", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class f_X:

    def __init__(self, f_X: set["f_Y"] = None):
        self.f_X = f_X if f_X is not None else set()
        
    @property
    def f_X(self):
        return self.__f_X

    @f_X.setter
    def f_X(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_f_X__f_X", None)
        self.__f_X = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "f_Y"):
                    opp_val = getattr(item, "f_Y", None)
                    
                    if opp_val == self:
                        setattr(item, "f_Y", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "f_Y"):
                    opp_val = getattr(item, "f_Y", None)
                    
                    setattr(item, "f_Y", self)
                    

    def foo(self):
        # TODO: Implement foo method
        pass
