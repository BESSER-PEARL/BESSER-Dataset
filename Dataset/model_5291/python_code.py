from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Root:

    pass
class MMA_Element(ABC):

    def __init__(self, name: str, 02: set["Element"] = None, 05: set["Element"] = None, 08: "Root" = None):
        self.name = name
        self.02 = 02 if 02 is not None else set()
        self.05 = 05 if 05 is not None else set()
        self.08 = 08
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def 08(self):
        return self.__08

    @08.setter
    def 08(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MMA_Element__08", None)
        self.__08 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "9"):
                opp_val = getattr(old_value, "9", None)
                if opp_val == self:
                    setattr(old_value, "9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "9"):
                opp_val = getattr(value, "9", None)
                setattr(value, "9", self)

    @property
    def 05(self):
        return self.__05

    @05.setter
    def 05(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MMA_Element__05", None)
        self.__05 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "6"):
                    opp_val = getattr(item, "6", None)
                    
                    if opp_val == self:
                        setattr(item, "6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "6"):
                    opp_val = getattr(item, "6", None)
                    
                    setattr(item, "6", self)
                    

    @property
    def 02(self):
        return self.__02

    @02.setter
    def 02(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MMA_Element__02", None)
        self.__02 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "3"):
                    opp_val = getattr(item, "3", None)
                    
                    if opp_val == self:
                        setattr(item, "3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "3"):
                    opp_val = getattr(item, "3", None)
                    
                    setattr(item, "3", self)
                    

class Element:

    pass
class MMA_A(Element):

    pass
class MMA_B(Element):

    pass
class MMA_Root:

    pass