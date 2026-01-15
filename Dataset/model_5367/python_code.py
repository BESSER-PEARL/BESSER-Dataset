from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class X:

    pass
class wxyz_Y(X):

    def __init__(self, propOfY: str):
        self.propOfY = propOfY
        
    @property
    def propOfY(self) -> str:
        return self.__propOfY

    @propOfY.setter
    def propOfY(self, propOfY: str):
        self.__propOfY = propOfY

class W:

    pass
class wxyz_X(W):

    def __init__(self, propOfX: str, wxyz_X: "wxyz_Model" = None):
        self.propOfX = propOfX
        self.wxyz_X = wxyz_X
        
    @property
    def propOfX(self) -> str:
        return self.__propOfX

    @propOfX.setter
    def propOfX(self, propOfX: str):
        self.__propOfX = propOfX

    @property
    def wxyz_X(self):
        return self.__wxyz_X

    @wxyz_X.setter
    def wxyz_X(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wxyz_X__wxyz_X", None)
        self.__wxyz_X = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wxyz_Model4"):
                opp_val = getattr(old_value, "wxyz_Model4", None)
                if opp_val == self:
                    setattr(old_value, "wxyz_Model4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wxyz_Model4"):
                opp_val = getattr(value, "wxyz_Model4", None)
                setattr(value, "wxyz_Model4", self)

class NamedElt:

    pass
class wxyz_W(NamedElt):

    def __init__(self, propOfW: str, wxyz_W: "wxyz_Model" = None, wxyz_W7: "wxyz_W" = None, wxyz_W5: set["wxyz_W"] = None):
        self.propOfW = propOfW
        self.wxyz_W = wxyz_W
        self.wxyz_W7 = wxyz_W7
        self.wxyz_W5 = wxyz_W5 if wxyz_W5 is not None else set()
        
    @property
    def propOfW(self) -> str:
        return self.__propOfW

    @propOfW.setter
    def propOfW(self, propOfW: str):
        self.__propOfW = propOfW

    @property
    def wxyz_W5(self):
        return self.__wxyz_W5

    @wxyz_W5.setter
    def wxyz_W5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wxyz_W__wxyz_W5", None)
        self.__wxyz_W5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "wxyz_W7"):
                    opp_val = getattr(item, "wxyz_W7", None)
                    
                    if opp_val == self:
                        setattr(item, "wxyz_W7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "wxyz_W7"):
                    opp_val = getattr(item, "wxyz_W7", None)
                    
                    setattr(item, "wxyz_W7", self)
                    

    @property
    def wxyz_W(self):
        return self.__wxyz_W

    @wxyz_W.setter
    def wxyz_W(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wxyz_W__wxyz_W", None)
        self.__wxyz_W = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wxyz_Model"):
                opp_val = getattr(old_value, "wxyz_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wxyz_Model"):
                opp_val = getattr(value, "wxyz_Model", None)
                if opp_val is None:
                    setattr(value, "wxyz_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def wxyz_W7(self):
        return self.__wxyz_W7

    @wxyz_W7.setter
    def wxyz_W7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_wxyz_W__wxyz_W7", None)
        self.__wxyz_W7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wxyz_W5"):
                opp_val = getattr(old_value, "wxyz_W5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wxyz_W5"):
                opp_val = getattr(value, "wxyz_W5", None)
                if opp_val is None:
                    setattr(value, "wxyz_W5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class wxyz_Other(NamedElt):

    pass
class wxyz_Model(NamedElt):

    pass
class wxyz_NamedElt(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class Y:

    pass
class wxyz_Z3(Y):

    pass
class wxyz_Z2(Y):

    pass
class wxyz_Z1(Y):

    pass
class wxyz_Z(Y):

    def __init__(self, propOfZ: str):
        self.propOfZ = propOfZ
        
    @property
    def propOfZ(self) -> str:
        return self.__propOfZ

    @propOfZ.setter
    def propOfZ(self, propOfZ: str):
        self.__propOfZ = propOfZ

class wxyz_Y2(X):

    pass
class wxyz_Y1(X):

    pass