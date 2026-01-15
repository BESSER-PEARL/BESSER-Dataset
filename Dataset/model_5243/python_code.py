from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class hExample_6_RHS_Z:

    def __init__(self, name: str, hExample_6_RHS_Z: "hExample_6_RHS_model" = None, hExample_6_RHS_Z10: "hExample_6_RHS_X" = None):
        self.name = name
        self.hExample_6_RHS_Z = hExample_6_RHS_Z
        self.hExample_6_RHS_Z10 = hExample_6_RHS_Z10
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def hExample_6_RHS_Z10(self):
        return self.__hExample_6_RHS_Z10

    @hExample_6_RHS_Z10.setter
    def hExample_6_RHS_Z10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hExample_6_RHS_Z__hExample_6_RHS_Z10", None)
        self.__hExample_6_RHS_Z10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hExample_6_RHS_X9"):
                opp_val = getattr(old_value, "hExample_6_RHS_X9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hExample_6_RHS_X9"):
                opp_val = getattr(value, "hExample_6_RHS_X9", None)
                if opp_val is None:
                    setattr(value, "hExample_6_RHS_X9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def hExample_6_RHS_Z(self):
        return self.__hExample_6_RHS_Z

    @hExample_6_RHS_Z.setter
    def hExample_6_RHS_Z(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hExample_6_RHS_Z__hExample_6_RHS_Z", None)
        self.__hExample_6_RHS_Z = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hExample_6_RHS_model4"):
                opp_val = getattr(old_value, "hExample_6_RHS_model4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hExample_6_RHS_model4"):
                opp_val = getattr(value, "hExample_6_RHS_model4", None)
                if opp_val is None:
                    setattr(value, "hExample_6_RHS_model4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class hExample_6_RHS_Y:

    def __init__(self, name: str, hExample_6_RHS_Y: "hExample_6_RHS_model" = None, hExample_6_RHS_Y7: "hExample_6_RHS_X" = None):
        self.name = name
        self.hExample_6_RHS_Y = hExample_6_RHS_Y
        self.hExample_6_RHS_Y7 = hExample_6_RHS_Y7
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def hExample_6_RHS_Y7(self):
        return self.__hExample_6_RHS_Y7

    @hExample_6_RHS_Y7.setter
    def hExample_6_RHS_Y7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hExample_6_RHS_Y__hExample_6_RHS_Y7", None)
        self.__hExample_6_RHS_Y7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hExample_6_RHS_X6"):
                opp_val = getattr(old_value, "hExample_6_RHS_X6", None)
                if opp_val == self:
                    setattr(old_value, "hExample_6_RHS_X6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hExample_6_RHS_X6"):
                opp_val = getattr(value, "hExample_6_RHS_X6", None)
                setattr(value, "hExample_6_RHS_X6", self)

    @property
    def hExample_6_RHS_Y(self):
        return self.__hExample_6_RHS_Y

    @hExample_6_RHS_Y.setter
    def hExample_6_RHS_Y(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hExample_6_RHS_Y__hExample_6_RHS_Y", None)
        self.__hExample_6_RHS_Y = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hExample_6_RHS_model2"):
                opp_val = getattr(old_value, "hExample_6_RHS_model2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hExample_6_RHS_model2"):
                opp_val = getattr(value, "hExample_6_RHS_model2", None)
                if opp_val is None:
                    setattr(value, "hExample_6_RHS_model2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class hExample_6_RHS_X:

    def __init__(self, name: str, hExample_6_RHS_X: "hExample_6_RHS_model" = None, hExample_6_RHS_X6: "hExample_6_RHS_Y" = None, hExample_6_RHS_X9: set["hExample_6_RHS_Z"] = None):
        self.name = name
        self.hExample_6_RHS_X = hExample_6_RHS_X
        self.hExample_6_RHS_X6 = hExample_6_RHS_X6
        self.hExample_6_RHS_X9 = hExample_6_RHS_X9 if hExample_6_RHS_X9 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def hExample_6_RHS_X6(self):
        return self.__hExample_6_RHS_X6

    @hExample_6_RHS_X6.setter
    def hExample_6_RHS_X6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hExample_6_RHS_X__hExample_6_RHS_X6", None)
        self.__hExample_6_RHS_X6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hExample_6_RHS_Y7"):
                opp_val = getattr(old_value, "hExample_6_RHS_Y7", None)
                if opp_val == self:
                    setattr(old_value, "hExample_6_RHS_Y7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hExample_6_RHS_Y7"):
                opp_val = getattr(value, "hExample_6_RHS_Y7", None)
                setattr(value, "hExample_6_RHS_Y7", self)

    @property
    def hExample_6_RHS_X(self):
        return self.__hExample_6_RHS_X

    @hExample_6_RHS_X.setter
    def hExample_6_RHS_X(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hExample_6_RHS_X__hExample_6_RHS_X", None)
        self.__hExample_6_RHS_X = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hExample_6_RHS_model"):
                opp_val = getattr(old_value, "hExample_6_RHS_model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hExample_6_RHS_model"):
                opp_val = getattr(value, "hExample_6_RHS_model", None)
                if opp_val is None:
                    setattr(value, "hExample_6_RHS_model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def hExample_6_RHS_X9(self):
        return self.__hExample_6_RHS_X9

    @hExample_6_RHS_X9.setter
    def hExample_6_RHS_X9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hExample_6_RHS_X__hExample_6_RHS_X9", None)
        self.__hExample_6_RHS_X9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "hExample_6_RHS_Z10"):
                    opp_val = getattr(item, "hExample_6_RHS_Z10", None)
                    
                    if opp_val == self:
                        setattr(item, "hExample_6_RHS_Z10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "hExample_6_RHS_Z10"):
                    opp_val = getattr(item, "hExample_6_RHS_Z10", None)
                    
                    setattr(item, "hExample_6_RHS_Z10", self)
                    

class hExample_6_RHS_model:

    pass