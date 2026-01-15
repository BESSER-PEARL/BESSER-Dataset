from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class sbase_EObject:

    pass
class sbase_SElement:

    pass
class SElement:

    pass
class sbase_Z(SElement):

    pass
class sbase_Y(SElement):

    def __init__(self, name: str, Y: "sbase_X" = None, toY: "sbase_Z" = None, ownsY: "sbase_X" = None, Y4: "sbase_Z" = None):
        self.name = name
        self.Y = Y
        self.toY = toY
        self.ownsY = ownsY
        self.Y4 = Y4
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ownsY(self):
        return self.__ownsY

    @ownsY.setter
    def ownsY(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sbase_Y__ownsY", None)
        self.__ownsY = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "X"):
                opp_val = getattr(old_value, "X", None)
                if opp_val == self:
                    setattr(old_value, "X", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "X"):
                opp_val = getattr(value, "X", None)
                setattr(value, "X", self)

    @property
    def Y(self):
        return self.__Y

    @Y.setter
    def Y(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sbase_Y__Y", None)
        self.__Y = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "toX"):
                opp_val = getattr(old_value, "toX", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "toX"):
                opp_val = getattr(value, "toX", None)
                if opp_val is None:
                    setattr(value, "toX", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def toY(self):
        return self.__toY

    @toY.setter
    def toY(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sbase_Y__toY", None)
        self.__toY = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Z"):
                opp_val = getattr(old_value, "Z", None)
                if opp_val == self:
                    setattr(old_value, "Z", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Z"):
                opp_val = getattr(value, "Z", None)
                setattr(value, "Z", self)

    @property
    def Y4(self):
        return self.__Y4

    @Y4.setter
    def Y4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sbase_Y__Y4", None)
        self.__Y4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownsZ"):
                opp_val = getattr(old_value, "ownsZ", None)
                if opp_val == self:
                    setattr(old_value, "ownsZ", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownsZ"):
                opp_val = getattr(value, "ownsZ", None)
                setattr(value, "ownsZ", self)

class sbase_SRoot(SElement):

    pass
class sbase_X(SElement):

    def __init__(self, name: str, toX: set["sbase_Y"] = None, X: "sbase_Y" = None, sbase_X: "sbase_SRoot" = None):
        self.name = name
        self.toX = toX if toX is not None else set()
        self.X = X
        self.sbase_X = sbase_X
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def X(self):
        return self.__X

    @X.setter
    def X(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sbase_X__X", None)
        self.__X = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ownsY"):
                opp_val = getattr(old_value, "ownsY", None)
                if opp_val == self:
                    setattr(old_value, "ownsY", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ownsY"):
                opp_val = getattr(value, "ownsY", None)
                setattr(value, "ownsY", self)

    @property
    def sbase_X(self):
        return self.__sbase_X

    @sbase_X.setter
    def sbase_X(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sbase_X__sbase_X", None)
        self.__sbase_X = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sbase_SRoot"):
                opp_val = getattr(old_value, "sbase_SRoot", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sbase_SRoot"):
                opp_val = getattr(value, "sbase_SRoot", None)
                if opp_val is None:
                    setattr(value, "sbase_SRoot", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def toX(self):
        return self.__toX

    @toX.setter
    def toX(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sbase_X__toX", None)
        self.__toX = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Y"):
                    opp_val = getattr(item, "Y", None)
                    
                    if opp_val == self:
                        setattr(item, "Y", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Y"):
                    opp_val = getattr(item, "Y", None)
                    
                    setattr(item, "Y", self)
                    
