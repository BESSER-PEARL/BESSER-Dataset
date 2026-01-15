from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class rootPackage_aSubSubPackage_F:

    pass
class AbstractA:

    pass
class rootPackage_A(AbstractA):

    def __init__(self, a: int, a2: bool, rootPackage_A: "rootPackage_C" = None, rootPackage_A2: set["rootPackage_B"] = None):
        self.a = a
        self.a2 = a2
        self.rootPackage_A = rootPackage_A
        self.rootPackage_A2 = rootPackage_A2 if rootPackage_A2 is not None else set()
        
    @property
    def a2(self) -> bool:
        return self.__a2

    @a2.setter
    def a2(self, a2: bool):
        self.__a2 = a2

    @property
    def a(self) -> int:
        return self.__a

    @a.setter
    def a(self, a: int):
        self.__a = a

    @property
    def rootPackage_A2(self):
        return self.__rootPackage_A2

    @rootPackage_A2.setter
    def rootPackage_A2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rootPackage_A__rootPackage_A2", None)
        self.__rootPackage_A2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rootPackage_B"):
                    opp_val = getattr(item, "rootPackage_B", None)
                    
                    if opp_val == self:
                        setattr(item, "rootPackage_B", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rootPackage_B"):
                    opp_val = getattr(item, "rootPackage_B", None)
                    
                    setattr(item, "rootPackage_B", self)
                    

    @property
    def rootPackage_A(self):
        return self.__rootPackage_A

    @rootPackage_A.setter
    def rootPackage_A(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rootPackage_A__rootPackage_A", None)
        self.__rootPackage_A = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rootPackage_C"):
                opp_val = getattr(old_value, "rootPackage_C", None)
                if opp_val == self:
                    setattr(old_value, "rootPackage_C", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rootPackage_C"):
                opp_val = getattr(value, "rootPackage_C", None)
                setattr(value, "rootPackage_C", self)

class aSubSubPackage_F:

    pass
class rootPackage_aSubSubPackage_E:

    pass
class rootPackage_aSubPackage_D:

    def __init__(self, d: int):
        self.d = d
        
    @property
    def d(self) -> int:
        return self.__d

    @d.setter
    def d(self, d: int):
        self.__d = d

class rootPackage_AbstractA(ABC):

    pass
class rootPackage_B:

    def __init__(self, bint: int, stuff: str, rootPackage_B: "rootPackage_A" = None, b: "rootPackage_C" = None, B: "rootPackage_C" = None):
        self.bint = bint
        self.stuff = stuff
        self.rootPackage_B = rootPackage_B
        self.b = b
        self.B = B
        
    @property
    def bint(self) -> int:
        return self.__bint

    @bint.setter
    def bint(self, bint: int):
        self.__bint = bint

    @property
    def stuff(self) -> str:
        return self.__stuff

    @stuff.setter
    def stuff(self, stuff: str):
        self.__stuff = stuff

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rootPackage_B__b", None)
        self.__b = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "C"):
                opp_val = getattr(old_value, "C", None)
                if opp_val == self:
                    setattr(old_value, "C", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "C"):
                opp_val = getattr(value, "C", None)
                setattr(value, "C", self)

    @property
    def rootPackage_B(self):
        return self.__rootPackage_B

    @rootPackage_B.setter
    def rootPackage_B(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rootPackage_B__rootPackage_B", None)
        self.__rootPackage_B = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rootPackage_A2"):
                opp_val = getattr(old_value, "rootPackage_A2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rootPackage_A2"):
                opp_val = getattr(value, "rootPackage_A2", None)
                if opp_val is None:
                    setattr(value, "rootPackage_A2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def B(self):
        return self.__B

    @B.setter
    def B(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rootPackage_B__B", None)
        self.__B = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "c"):
                opp_val = getattr(old_value, "c", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "c"):
                opp_val = getattr(value, "c", None)
                if opp_val is None:
                    setattr(value, "c", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class rootPackage_C:

    def __init__(self, cstring: str, rootPackage_C: "rootPackage_A" = None, C: "rootPackage_B" = None, c: set["rootPackage_B"] = None):
        self.cstring = cstring
        self.rootPackage_C = rootPackage_C
        self.C = C
        self.c = c if c is not None else set()
        
    @property
    def cstring(self) -> str:
        return self.__cstring

    @cstring.setter
    def cstring(self, cstring: str):
        self.__cstring = cstring

    @property
    def C(self):
        return self.__C

    @C.setter
    def C(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rootPackage_C__C", None)
        self.__C = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "b"):
                opp_val = getattr(old_value, "b", None)
                if opp_val == self:
                    setattr(old_value, "b", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "b"):
                opp_val = getattr(value, "b", None)
                setattr(value, "b", self)

    @property
    def rootPackage_C(self):
        return self.__rootPackage_C

    @rootPackage_C.setter
    def rootPackage_C(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rootPackage_C__rootPackage_C", None)
        self.__rootPackage_C = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rootPackage_A"):
                opp_val = getattr(old_value, "rootPackage_A", None)
                if opp_val == self:
                    setattr(old_value, "rootPackage_A", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rootPackage_A"):
                opp_val = getattr(value, "rootPackage_A", None)
                setattr(value, "rootPackage_A", self)

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rootPackage_C__c", None)
        self.__c = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "B"):
                    opp_val = getattr(item, "B", None)
                    
                    if opp_val == self:
                        setattr(item, "B", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "B"):
                    opp_val = getattr(item, "B", None)
                    
                    setattr(item, "B", self)
                    
