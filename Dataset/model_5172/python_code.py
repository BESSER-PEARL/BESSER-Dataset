from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Element:

    pass
class ABC_C(Element):

    def __init__(self, c: str):
        self.c = c
        
    @property
    def c(self) -> str:
        return self.__c

    @c.setter
    def c(self, c: str):
        self.__c = c

class ABC_B(Element):

    def __init__(self, b: str):
        self.b = b
        
    @property
    def b(self) -> str:
        return self.__b

    @b.setter
    def b(self, b: str):
        self.__b = b

class ABC_A(Element):

    def __init__(self, a: str):
        self.a = a
        
    @property
    def a(self) -> str:
        return self.__a

    @a.setter
    def a(self, a: str):
        self.__a = a

class ABC_Element(ABC):

    def __init__(self, id: int, ABC_Element: "ABC_Root" = None, ABC_Element3: "ABC_Element" = None, ABC_Element1: set["ABC_Element"] = None):
        self.id = id
        self.ABC_Element = ABC_Element
        self.ABC_Element3 = ABC_Element3
        self.ABC_Element1 = ABC_Element1 if ABC_Element1 is not None else set()
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def ABC_Element(self):
        return self.__ABC_Element

    @ABC_Element.setter
    def ABC_Element(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ABC_Element__ABC_Element", None)
        self.__ABC_Element = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ABC_Root"):
                opp_val = getattr(old_value, "ABC_Root", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ABC_Root"):
                opp_val = getattr(value, "ABC_Root", None)
                if opp_val is None:
                    setattr(value, "ABC_Root", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ABC_Element3(self):
        return self.__ABC_Element3

    @ABC_Element3.setter
    def ABC_Element3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ABC_Element__ABC_Element3", None)
        self.__ABC_Element3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ABC_Element1"):
                opp_val = getattr(old_value, "ABC_Element1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ABC_Element1"):
                opp_val = getattr(value, "ABC_Element1", None)
                if opp_val is None:
                    setattr(value, "ABC_Element1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ABC_Element1(self):
        return self.__ABC_Element1

    @ABC_Element1.setter
    def ABC_Element1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ABC_Element__ABC_Element1", None)
        self.__ABC_Element1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ABC_Element3"):
                    opp_val = getattr(item, "ABC_Element3", None)
                    
                    if opp_val == self:
                        setattr(item, "ABC_Element3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ABC_Element3"):
                    opp_val = getattr(item, "ABC_Element3", None)
                    
                    setattr(item, "ABC_Element3", self)
                    

class ABC_Root:

    pass