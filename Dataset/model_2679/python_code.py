from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class formalmetamodel_AA(ABC):

    pass
class formalmetamodel_C:

    def __init__(self, name: str, formalmetamodel_C: "formalmetamodel_FormalModel" = None, formalmetamodel_C16: "formalmetamodel_C" = None, formalmetamodel_C14: set["formalmetamodel_C"] = None, formalmetamodel_C18: "formalmetamodel_A" = None):
        self.name = name
        self.formalmetamodel_C = formalmetamodel_C
        self.formalmetamodel_C16 = formalmetamodel_C16
        self.formalmetamodel_C14 = formalmetamodel_C14 if formalmetamodel_C14 is not None else set()
        self.formalmetamodel_C18 = formalmetamodel_C18
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def formalmetamodel_C14(self):
        return self.__formalmetamodel_C14

    @formalmetamodel_C14.setter
    def formalmetamodel_C14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_formalmetamodel_C__formalmetamodel_C14", None)
        self.__formalmetamodel_C14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "formalmetamodel_C16"):
                    opp_val = getattr(item, "formalmetamodel_C16", None)
                    
                    if opp_val == self:
                        setattr(item, "formalmetamodel_C16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "formalmetamodel_C16"):
                    opp_val = getattr(item, "formalmetamodel_C16", None)
                    
                    setattr(item, "formalmetamodel_C16", self)
                    

    @property
    def formalmetamodel_C18(self):
        return self.__formalmetamodel_C18

    @formalmetamodel_C18.setter
    def formalmetamodel_C18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_formalmetamodel_C__formalmetamodel_C18", None)
        self.__formalmetamodel_C18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "formalmetamodel_A19"):
                opp_val = getattr(old_value, "formalmetamodel_A19", None)
                if opp_val == self:
                    setattr(old_value, "formalmetamodel_A19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "formalmetamodel_A19"):
                opp_val = getattr(value, "formalmetamodel_A19", None)
                setattr(value, "formalmetamodel_A19", self)

    @property
    def formalmetamodel_C(self):
        return self.__formalmetamodel_C

    @formalmetamodel_C.setter
    def formalmetamodel_C(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_formalmetamodel_C__formalmetamodel_C", None)
        self.__formalmetamodel_C = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "formalmetamodel_FormalModel13"):
                opp_val = getattr(old_value, "formalmetamodel_FormalModel13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "formalmetamodel_FormalModel13"):
                opp_val = getattr(value, "formalmetamodel_FormalModel13", None)
                if opp_val is None:
                    setattr(value, "formalmetamodel_FormalModel13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def formalmetamodel_C16(self):
        return self.__formalmetamodel_C16

    @formalmetamodel_C16.setter
    def formalmetamodel_C16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_formalmetamodel_C__formalmetamodel_C16", None)
        self.__formalmetamodel_C16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "formalmetamodel_C14"):
                opp_val = getattr(old_value, "formalmetamodel_C14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "formalmetamodel_C14"):
                opp_val = getattr(value, "formalmetamodel_C14", None)
                if opp_val is None:
                    setattr(value, "formalmetamodel_C14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class formalmetamodel_FormalModel:

    pass
class formalmetamodel_B:

    def __init__(self, name: str, formalmetamodel_B: "formalmetamodel_A" = None, formalmetamodel_B2: set["formalmetamodel_A"] = None, formalmetamodel_B6: "formalmetamodel_B" = None, formalmetamodel_B4: "formalmetamodel_B" = None, formalmetamodel_B8: "formalmetamodel_FormalModel" = None):
        self.name = name
        self.formalmetamodel_B = formalmetamodel_B
        self.formalmetamodel_B2 = formalmetamodel_B2 if formalmetamodel_B2 is not None else set()
        self.formalmetamodel_B6 = formalmetamodel_B6
        self.formalmetamodel_B4 = formalmetamodel_B4
        self.formalmetamodel_B8 = formalmetamodel_B8
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def formalmetamodel_B2(self):
        return self.__formalmetamodel_B2

    @formalmetamodel_B2.setter
    def formalmetamodel_B2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_formalmetamodel_B__formalmetamodel_B2", None)
        self.__formalmetamodel_B2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "formalmetamodel_A3"):
                    opp_val = getattr(item, "formalmetamodel_A3", None)
                    
                    if opp_val == self:
                        setattr(item, "formalmetamodel_A3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "formalmetamodel_A3"):
                    opp_val = getattr(item, "formalmetamodel_A3", None)
                    
                    setattr(item, "formalmetamodel_A3", self)
                    

    @property
    def formalmetamodel_B4(self):
        return self.__formalmetamodel_B4

    @formalmetamodel_B4.setter
    def formalmetamodel_B4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_formalmetamodel_B__formalmetamodel_B4", None)
        self.__formalmetamodel_B4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "formalmetamodel_B6"):
                opp_val = getattr(old_value, "formalmetamodel_B6", None)
                if opp_val == self:
                    setattr(old_value, "formalmetamodel_B6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "formalmetamodel_B6"):
                opp_val = getattr(value, "formalmetamodel_B6", None)
                setattr(value, "formalmetamodel_B6", self)

    @property
    def formalmetamodel_B6(self):
        return self.__formalmetamodel_B6

    @formalmetamodel_B6.setter
    def formalmetamodel_B6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_formalmetamodel_B__formalmetamodel_B6", None)
        self.__formalmetamodel_B6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "formalmetamodel_B4"):
                opp_val = getattr(old_value, "formalmetamodel_B4", None)
                if opp_val == self:
                    setattr(old_value, "formalmetamodel_B4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "formalmetamodel_B4"):
                opp_val = getattr(value, "formalmetamodel_B4", None)
                setattr(value, "formalmetamodel_B4", self)

    @property
    def formalmetamodel_B8(self):
        return self.__formalmetamodel_B8

    @formalmetamodel_B8.setter
    def formalmetamodel_B8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_formalmetamodel_B__formalmetamodel_B8", None)
        self.__formalmetamodel_B8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "formalmetamodel_FormalModel"):
                opp_val = getattr(old_value, "formalmetamodel_FormalModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "formalmetamodel_FormalModel"):
                opp_val = getattr(value, "formalmetamodel_FormalModel", None)
                if opp_val is None:
                    setattr(value, "formalmetamodel_FormalModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def formalmetamodel_B(self):
        return self.__formalmetamodel_B

    @formalmetamodel_B.setter
    def formalmetamodel_B(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_formalmetamodel_B__formalmetamodel_B", None)
        self.__formalmetamodel_B = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "formalmetamodel_A"):
                opp_val = getattr(old_value, "formalmetamodel_A", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "formalmetamodel_A"):
                opp_val = getattr(value, "formalmetamodel_A", None)
                if opp_val is None:
                    setattr(value, "formalmetamodel_A", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class AA:

    pass
class formalmetamodel_A(AA):

    def __init__(self, name: str, formalmetamodel_A: set["formalmetamodel_B"] = None, formalmetamodel_A3: "formalmetamodel_B" = None, formalmetamodel_A11: "formalmetamodel_FormalModel" = None, formalmetamodel_A19: "formalmetamodel_C" = None):
        self.name = name
        self.formalmetamodel_A = formalmetamodel_A if formalmetamodel_A is not None else set()
        self.formalmetamodel_A3 = formalmetamodel_A3
        self.formalmetamodel_A11 = formalmetamodel_A11
        self.formalmetamodel_A19 = formalmetamodel_A19
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def formalmetamodel_A11(self):
        return self.__formalmetamodel_A11

    @formalmetamodel_A11.setter
    def formalmetamodel_A11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_formalmetamodel_A__formalmetamodel_A11", None)
        self.__formalmetamodel_A11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "formalmetamodel_FormalModel10"):
                opp_val = getattr(old_value, "formalmetamodel_FormalModel10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "formalmetamodel_FormalModel10"):
                opp_val = getattr(value, "formalmetamodel_FormalModel10", None)
                if opp_val is None:
                    setattr(value, "formalmetamodel_FormalModel10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def formalmetamodel_A(self):
        return self.__formalmetamodel_A

    @formalmetamodel_A.setter
    def formalmetamodel_A(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_formalmetamodel_A__formalmetamodel_A", None)
        self.__formalmetamodel_A = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "formalmetamodel_B"):
                    opp_val = getattr(item, "formalmetamodel_B", None)
                    
                    if opp_val == self:
                        setattr(item, "formalmetamodel_B", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "formalmetamodel_B"):
                    opp_val = getattr(item, "formalmetamodel_B", None)
                    
                    setattr(item, "formalmetamodel_B", self)
                    

    @property
    def formalmetamodel_A3(self):
        return self.__formalmetamodel_A3

    @formalmetamodel_A3.setter
    def formalmetamodel_A3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_formalmetamodel_A__formalmetamodel_A3", None)
        self.__formalmetamodel_A3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "formalmetamodel_B2"):
                opp_val = getattr(old_value, "formalmetamodel_B2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "formalmetamodel_B2"):
                opp_val = getattr(value, "formalmetamodel_B2", None)
                if opp_val is None:
                    setattr(value, "formalmetamodel_B2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def formalmetamodel_A19(self):
        return self.__formalmetamodel_A19

    @formalmetamodel_A19.setter
    def formalmetamodel_A19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_formalmetamodel_A__formalmetamodel_A19", None)
        self.__formalmetamodel_A19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "formalmetamodel_C18"):
                opp_val = getattr(old_value, "formalmetamodel_C18", None)
                if opp_val == self:
                    setattr(old_value, "formalmetamodel_C18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "formalmetamodel_C18"):
                opp_val = getattr(value, "formalmetamodel_C18", None)
                setattr(value, "formalmetamodel_C18", self)
