from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class A:

    pass
class refinher3_M:

    def __init__(self, id: str, refinher3_M: "refinher3_DG" = None, refinher3_M13: set["refinher3_E"] = None, refinher3_M16: set["refinher3_Foobar"] = None):
        self.id = id
        self.refinher3_M = refinher3_M
        self.refinher3_M13 = refinher3_M13 if refinher3_M13 is not None else set()
        self.refinher3_M16 = refinher3_M16 if refinher3_M16 is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def refinher3_M16(self):
        return self.__refinher3_M16

    @refinher3_M16.setter
    def refinher3_M16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_refinher3_M__refinher3_M16", None)
        self.__refinher3_M16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "refinher3_Foobar"):
                    opp_val = getattr(item, "refinher3_Foobar", None)
                    
                    if opp_val == self:
                        setattr(item, "refinher3_Foobar", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "refinher3_Foobar"):
                    opp_val = getattr(item, "refinher3_Foobar", None)
                    
                    setattr(item, "refinher3_Foobar", self)
                    

    @property
    def refinher3_M13(self):
        return self.__refinher3_M13

    @refinher3_M13.setter
    def refinher3_M13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_refinher3_M__refinher3_M13", None)
        self.__refinher3_M13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "refinher3_E14"):
                    opp_val = getattr(item, "refinher3_E14", None)
                    
                    if opp_val == self:
                        setattr(item, "refinher3_E14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "refinher3_E14"):
                    opp_val = getattr(item, "refinher3_E14", None)
                    
                    setattr(item, "refinher3_E14", self)
                    

    @property
    def refinher3_M(self):
        return self.__refinher3_M

    @refinher3_M.setter
    def refinher3_M(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_refinher3_M__refinher3_M", None)
        self.__refinher3_M = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "refinher3_DG11"):
                opp_val = getattr(old_value, "refinher3_DG11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "refinher3_DG11"):
                opp_val = getattr(value, "refinher3_DG11", None)
                if opp_val is None:
                    setattr(value, "refinher3_DG11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class E:

    pass
class refinher3_CE(A, E):

    pass
class refinher3_DR(E):

    pass
class CE:

    pass
class refinher3_DC(CE):

    pass
class refinher3_DL(CE):

    pass
class refinher3_DNamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class refinher3_N:

    def __init__(self, nam: str, refinher3_N: "refinher3_E" = None, refinher3_N3: "refinher3_E" = None, refinher3_N9: "refinher3_DG" = None):
        self.nam = nam
        self.refinher3_N = refinher3_N
        self.refinher3_N3 = refinher3_N3
        self.refinher3_N9 = refinher3_N9
        
    @property
    def nam(self) -> str:
        return self.__nam

    @nam.setter
    def nam(self, nam: str):
        self.__nam = nam

    @property
    def refinher3_N3(self):
        return self.__refinher3_N3

    @refinher3_N3.setter
    def refinher3_N3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_refinher3_N__refinher3_N3", None)
        self.__refinher3_N3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "refinher3_E2"):
                opp_val = getattr(old_value, "refinher3_E2", None)
                if opp_val == self:
                    setattr(old_value, "refinher3_E2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "refinher3_E2"):
                opp_val = getattr(value, "refinher3_E2", None)
                setattr(value, "refinher3_E2", self)

    @property
    def refinher3_N(self):
        return self.__refinher3_N

    @refinher3_N.setter
    def refinher3_N(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_refinher3_N__refinher3_N", None)
        self.__refinher3_N = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "refinher3_E"):
                opp_val = getattr(old_value, "refinher3_E", None)
                if opp_val == self:
                    setattr(old_value, "refinher3_E", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "refinher3_E"):
                opp_val = getattr(value, "refinher3_E", None)
                setattr(value, "refinher3_E", self)

    @property
    def refinher3_N9(self):
        return self.__refinher3_N9

    @refinher3_N9.setter
    def refinher3_N9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_refinher3_N__refinher3_N9", None)
        self.__refinher3_N9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "refinher3_DG8"):
                opp_val = getattr(old_value, "refinher3_DG8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "refinher3_DG8"):
                opp_val = getattr(value, "refinher3_DG8", None)
                if opp_val is None:
                    setattr(value, "refinher3_DG8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class DNamedElement:

    pass
class refinher3_Foobar(DNamedElement):

    pass
class refinher3_A(DNamedElement):

    pass
class refinher3_BB(DNamedElement):

    pass
class refinher3_E(DNamedElement):

    pass
class refinher3_DG:

    pass