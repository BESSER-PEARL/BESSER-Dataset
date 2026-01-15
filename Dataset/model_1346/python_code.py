from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class source_EObject:

    pass
class source_SElement:

    pass
class Y:

    pass
class source_Y2(Y):

    pass
class source_Y1(Y):

    pass
class SElement:

    pass
class source_SRoot(SElement):

    pass
class source_PathElementCS(SElement):

    def __init__(self, name: str, source_PathElementCS: "source_PathNameCS" = None):
        self.name = name
        self.source_PathElementCS = source_PathElementCS
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def source_PathElementCS(self):
        return self.__source_PathElementCS

    @source_PathElementCS.setter
    def source_PathElementCS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_source_PathElementCS__source_PathElementCS", None)
        self.__source_PathElementCS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "source_PathNameCS9"):
                opp_val = getattr(old_value, "source_PathNameCS9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "source_PathNameCS9"):
                opp_val = getattr(value, "source_PathNameCS9", None)
                if opp_val is None:
                    setattr(value, "source_PathNameCS9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class source_PathNameCS(SElement):

    pass
class source_Z(SElement):

    pass
class source_Y(SElement):

    def __init__(self, name: str, toY: "source_Z" = None, ownsY: "source_X" = None, Y4: "source_Z" = None, Y: "source_X" = None):
        self.name = name
        self.toY = toY
        self.ownsY = ownsY
        self.Y4 = Y4
        self.Y = Y
        
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
        old_value = getattr(self, f"_source_Y__ownsY", None)
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
    def toY(self):
        return self.__toY

    @toY.setter
    def toY(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_source_Y__toY", None)
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
    def Y(self):
        return self.__Y

    @Y.setter
    def Y(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_source_Y__Y", None)
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
    def Y4(self):
        return self.__Y4

    @Y4.setter
    def Y4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_source_Y__Y4", None)
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

class source_X(SElement):

    def __init__(self, isA1: bool, isA2: bool, name: str, X: "source_Y" = None, toX: set["source_Y"] = None, source_X: "source_SRoot" = None):
        self.isA1 = isA1
        self.isA2 = isA2
        self.name = name
        self.X = X
        self.toX = toX if toX is not None else set()
        self.source_X = source_X
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def isA1(self) -> bool:
        return self.__isA1

    @isA1.setter
    def isA1(self, isA1: bool):
        self.__isA1 = isA1

    @property
    def isA2(self) -> bool:
        return self.__isA2

    @isA2.setter
    def isA2(self, isA2: bool):
        self.__isA2 = isA2

    @property
    def X(self):
        return self.__X

    @X.setter
    def X(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_source_X__X", None)
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
    def toX(self):
        return self.__toX

    @toX.setter
    def toX(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_source_X__toX", None)
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
                    

    @property
    def source_X(self):
        return self.__source_X

    @source_X.setter
    def source_X(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_source_X__source_X", None)
        self.__source_X = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "source_SRoot"):
                opp_val = getattr(old_value, "source_SRoot", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "source_SRoot"):
                opp_val = getattr(value, "source_SRoot", None)
                if opp_val is None:
                    setattr(value, "source_SRoot", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
