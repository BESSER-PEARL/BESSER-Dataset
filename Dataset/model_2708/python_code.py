from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class strictSample_D:

    pass
class strictSample_C:

    pass
class strictSample_B:

    def __init__(self, b: str, strictSample_B: "strictSample_A" = None, strictSample_B2: set["strictSample_C"] = None, strictSample_B4: "strictSample_D" = None):
        self.b = b
        self.strictSample_B = strictSample_B
        self.strictSample_B2 = strictSample_B2 if strictSample_B2 is not None else set()
        self.strictSample_B4 = strictSample_B4
        
    @property
    def b(self) -> str:
        return self.__b

    @b.setter
    def b(self, b: str):
        self.__b = b

    @property
    def strictSample_B4(self):
        return self.__strictSample_B4

    @strictSample_B4.setter
    def strictSample_B4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_strictSample_B__strictSample_B4", None)
        self.__strictSample_B4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "strictSample_D"):
                opp_val = getattr(old_value, "strictSample_D", None)
                if opp_val == self:
                    setattr(old_value, "strictSample_D", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "strictSample_D"):
                opp_val = getattr(value, "strictSample_D", None)
                setattr(value, "strictSample_D", self)

    @property
    def strictSample_B(self):
        return self.__strictSample_B

    @strictSample_B.setter
    def strictSample_B(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_strictSample_B__strictSample_B", None)
        self.__strictSample_B = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "strictSample_A"):
                opp_val = getattr(old_value, "strictSample_A", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "strictSample_A"):
                opp_val = getattr(value, "strictSample_A", None)
                if opp_val is None:
                    setattr(value, "strictSample_A", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def strictSample_B2(self):
        return self.__strictSample_B2

    @strictSample_B2.setter
    def strictSample_B2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_strictSample_B__strictSample_B2", None)
        self.__strictSample_B2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "strictSample_C"):
                    opp_val = getattr(item, "strictSample_C", None)
                    
                    if opp_val == self:
                        setattr(item, "strictSample_C", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "strictSample_C"):
                    opp_val = getattr(item, "strictSample_C", None)
                    
                    setattr(item, "strictSample_C", self)
                    

class strictSample_A:

    def __init__(self, a: str, strictSample_A: set["strictSample_B"] = None):
        self.a = a
        self.strictSample_A = strictSample_A if strictSample_A is not None else set()
        
    @property
    def a(self) -> str:
        return self.__a

    @a.setter
    def a(self, a: str):
        self.__a = a

    @property
    def strictSample_A(self):
        return self.__strictSample_A

    @strictSample_A.setter
    def strictSample_A(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_strictSample_A__strictSample_A", None)
        self.__strictSample_A = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "strictSample_B"):
                    opp_val = getattr(item, "strictSample_B", None)
                    
                    if opp_val == self:
                        setattr(item, "strictSample_B", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "strictSample_B"):
                    opp_val = getattr(item, "strictSample_B", None)
                    
                    setattr(item, "strictSample_B", self)
                    
