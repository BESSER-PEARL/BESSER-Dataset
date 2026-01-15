from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class hExample_6_LHS_C:

    def __init__(self, name: str, hExample_6_LHS_C: "hExample_6_LHS_model" = None, hExample_6_LHS_C10: "hExample_6_LHS_A" = None):
        self.name = name
        self.hExample_6_LHS_C = hExample_6_LHS_C
        self.hExample_6_LHS_C10 = hExample_6_LHS_C10
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def hExample_6_LHS_C(self):
        return self.__hExample_6_LHS_C

    @hExample_6_LHS_C.setter
    def hExample_6_LHS_C(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hExample_6_LHS_C__hExample_6_LHS_C", None)
        self.__hExample_6_LHS_C = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hExample_6_LHS_model4"):
                opp_val = getattr(old_value, "hExample_6_LHS_model4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hExample_6_LHS_model4"):
                opp_val = getattr(value, "hExample_6_LHS_model4", None)
                if opp_val is None:
                    setattr(value, "hExample_6_LHS_model4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def hExample_6_LHS_C10(self):
        return self.__hExample_6_LHS_C10

    @hExample_6_LHS_C10.setter
    def hExample_6_LHS_C10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hExample_6_LHS_C__hExample_6_LHS_C10", None)
        self.__hExample_6_LHS_C10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hExample_6_LHS_A9"):
                opp_val = getattr(old_value, "hExample_6_LHS_A9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hExample_6_LHS_A9"):
                opp_val = getattr(value, "hExample_6_LHS_A9", None)
                if opp_val is None:
                    setattr(value, "hExample_6_LHS_A9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class hExample_6_LHS_A:

    def __init__(self, name: str, hExample_6_LHS_A: "hExample_6_LHS_model" = None, hExample_6_LHS_A6: "hExample_6_LHS_B" = None, hExample_6_LHS_A9: set["hExample_6_LHS_C"] = None):
        self.name = name
        self.hExample_6_LHS_A = hExample_6_LHS_A
        self.hExample_6_LHS_A6 = hExample_6_LHS_A6
        self.hExample_6_LHS_A9 = hExample_6_LHS_A9 if hExample_6_LHS_A9 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def hExample_6_LHS_A9(self):
        return self.__hExample_6_LHS_A9

    @hExample_6_LHS_A9.setter
    def hExample_6_LHS_A9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hExample_6_LHS_A__hExample_6_LHS_A9", None)
        self.__hExample_6_LHS_A9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "hExample_6_LHS_C10"):
                    opp_val = getattr(item, "hExample_6_LHS_C10", None)
                    
                    if opp_val == self:
                        setattr(item, "hExample_6_LHS_C10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "hExample_6_LHS_C10"):
                    opp_val = getattr(item, "hExample_6_LHS_C10", None)
                    
                    setattr(item, "hExample_6_LHS_C10", self)
                    

    @property
    def hExample_6_LHS_A6(self):
        return self.__hExample_6_LHS_A6

    @hExample_6_LHS_A6.setter
    def hExample_6_LHS_A6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hExample_6_LHS_A__hExample_6_LHS_A6", None)
        self.__hExample_6_LHS_A6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hExample_6_LHS_B7"):
                opp_val = getattr(old_value, "hExample_6_LHS_B7", None)
                if opp_val == self:
                    setattr(old_value, "hExample_6_LHS_B7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hExample_6_LHS_B7"):
                opp_val = getattr(value, "hExample_6_LHS_B7", None)
                setattr(value, "hExample_6_LHS_B7", self)

    @property
    def hExample_6_LHS_A(self):
        return self.__hExample_6_LHS_A

    @hExample_6_LHS_A.setter
    def hExample_6_LHS_A(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hExample_6_LHS_A__hExample_6_LHS_A", None)
        self.__hExample_6_LHS_A = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hExample_6_LHS_model"):
                opp_val = getattr(old_value, "hExample_6_LHS_model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hExample_6_LHS_model"):
                opp_val = getattr(value, "hExample_6_LHS_model", None)
                if opp_val is None:
                    setattr(value, "hExample_6_LHS_model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class hExample_6_LHS_model:

    pass
class hExample_6_LHS_B:

    def __init__(self, name: str, hExample_6_LHS_B: "hExample_6_LHS_model" = None, hExample_6_LHS_B7: "hExample_6_LHS_A" = None):
        self.name = name
        self.hExample_6_LHS_B = hExample_6_LHS_B
        self.hExample_6_LHS_B7 = hExample_6_LHS_B7
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def hExample_6_LHS_B(self):
        return self.__hExample_6_LHS_B

    @hExample_6_LHS_B.setter
    def hExample_6_LHS_B(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hExample_6_LHS_B__hExample_6_LHS_B", None)
        self.__hExample_6_LHS_B = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hExample_6_LHS_model2"):
                opp_val = getattr(old_value, "hExample_6_LHS_model2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hExample_6_LHS_model2"):
                opp_val = getattr(value, "hExample_6_LHS_model2", None)
                if opp_val is None:
                    setattr(value, "hExample_6_LHS_model2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def hExample_6_LHS_B7(self):
        return self.__hExample_6_LHS_B7

    @hExample_6_LHS_B7.setter
    def hExample_6_LHS_B7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hExample_6_LHS_B__hExample_6_LHS_B7", None)
        self.__hExample_6_LHS_B7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hExample_6_LHS_A6"):
                opp_val = getattr(old_value, "hExample_6_LHS_A6", None)
                if opp_val == self:
                    setattr(old_value, "hExample_6_LHS_A6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hExample_6_LHS_A6"):
                opp_val = getattr(value, "hExample_6_LHS_A6", None)
                setattr(value, "hExample_6_LHS_A6", self)
