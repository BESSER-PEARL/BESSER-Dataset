from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class RootOut:

    pass
class out_E(RootOut):

    def __init__(self, name: str, out_E5: "out_D" = None, out_E: "out_D" = None):
        self.name = name
        self.out_E5 = out_E5
        self.out_E = out_E
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def out_E(self):
        return self.__out_E

    @out_E.setter
    def out_E(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_out_E__out_E", None)
        self.__out_E = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "out_D"):
                opp_val = getattr(old_value, "out_D", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "out_D"):
                opp_val = getattr(value, "out_D", None)
                if opp_val is None:
                    setattr(value, "out_D", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def out_E5(self):
        return self.__out_E5

    @out_E5.setter
    def out_E5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_out_E__out_E5", None)
        self.__out_E5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "out_D6"):
                opp_val = getattr(old_value, "out_D6", None)
                if opp_val == self:
                    setattr(old_value, "out_D6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "out_D6"):
                opp_val = getattr(value, "out_D6", None)
                setattr(value, "out_D6", self)

class out_D(RootOut):

    def __init__(self, name: str, out_D1: "out_D" = None, out_D6: "out_E" = None, out_D: set["out_E"] = None, out_D3: "out_D" = None):
        self.name = name
        self.out_D1 = out_D1
        self.out_D6 = out_D6
        self.out_D = out_D if out_D is not None else set()
        self.out_D3 = out_D3
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def out_D1(self):
        return self.__out_D1

    @out_D1.setter
    def out_D1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_out_D__out_D1", None)
        self.__out_D1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "out_D3"):
                opp_val = getattr(old_value, "out_D3", None)
                if opp_val == self:
                    setattr(old_value, "out_D3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "out_D3"):
                opp_val = getattr(value, "out_D3", None)
                setattr(value, "out_D3", self)

    @property
    def out_D(self):
        return self.__out_D

    @out_D.setter
    def out_D(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_out_D__out_D", None)
        self.__out_D = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "out_E"):
                    opp_val = getattr(item, "out_E", None)
                    
                    if opp_val == self:
                        setattr(item, "out_E", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "out_E"):
                    opp_val = getattr(item, "out_E", None)
                    
                    setattr(item, "out_E", self)
                    

    @property
    def out_D6(self):
        return self.__out_D6

    @out_D6.setter
    def out_D6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_out_D__out_D6", None)
        self.__out_D6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "out_E5"):
                opp_val = getattr(old_value, "out_E5", None)
                if opp_val == self:
                    setattr(old_value, "out_E5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "out_E5"):
                opp_val = getattr(value, "out_E5", None)
                setattr(value, "out_E5", self)

    @property
    def out_D3(self):
        return self.__out_D3

    @out_D3.setter
    def out_D3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_out_D__out_D3", None)
        self.__out_D3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "out_D1"):
                opp_val = getattr(old_value, "out_D1", None)
                if opp_val == self:
                    setattr(old_value, "out_D1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "out_D1"):
                opp_val = getattr(value, "out_D1", None)
                setattr(value, "out_D1", self)

class out_RootOut(ABC):

    pass