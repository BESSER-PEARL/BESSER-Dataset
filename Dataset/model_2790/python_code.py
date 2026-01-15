from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Gggg:

    pass
class kreq108c_Gggg(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class kreq108c_Ffff(Gggg):

    def __init__(self, id: str, kreq108c_Ffff: "kreq108c_Cccc" = None, kreq108c_Ffff6: set["kreq108c_Eeee"] = None, kreq108c_Ffff10: "kreq108c_Ffff" = None, kreq108c_Ffff8: set["kreq108c_Ffff"] = None):
        self.id = id
        self.kreq108c_Ffff = kreq108c_Ffff
        self.kreq108c_Ffff6 = kreq108c_Ffff6 if kreq108c_Ffff6 is not None else set()
        self.kreq108c_Ffff10 = kreq108c_Ffff10
        self.kreq108c_Ffff8 = kreq108c_Ffff8 if kreq108c_Ffff8 is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def kreq108c_Ffff10(self):
        return self.__kreq108c_Ffff10

    @kreq108c_Ffff10.setter
    def kreq108c_Ffff10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kreq108c_Ffff__kreq108c_Ffff10", None)
        self.__kreq108c_Ffff10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kreq108c_Ffff8"):
                opp_val = getattr(old_value, "kreq108c_Ffff8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kreq108c_Ffff8"):
                opp_val = getattr(value, "kreq108c_Ffff8", None)
                if opp_val is None:
                    setattr(value, "kreq108c_Ffff8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def kreq108c_Ffff8(self):
        return self.__kreq108c_Ffff8

    @kreq108c_Ffff8.setter
    def kreq108c_Ffff8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kreq108c_Ffff__kreq108c_Ffff8", None)
        self.__kreq108c_Ffff8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "kreq108c_Ffff10"):
                    opp_val = getattr(item, "kreq108c_Ffff10", None)
                    
                    if opp_val == self:
                        setattr(item, "kreq108c_Ffff10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "kreq108c_Ffff10"):
                    opp_val = getattr(item, "kreq108c_Ffff10", None)
                    
                    setattr(item, "kreq108c_Ffff10", self)
                    

    @property
    def kreq108c_Ffff6(self):
        return self.__kreq108c_Ffff6

    @kreq108c_Ffff6.setter
    def kreq108c_Ffff6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kreq108c_Ffff__kreq108c_Ffff6", None)
        self.__kreq108c_Ffff6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "kreq108c_Eeee7"):
                    opp_val = getattr(item, "kreq108c_Eeee7", None)
                    
                    if opp_val == self:
                        setattr(item, "kreq108c_Eeee7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "kreq108c_Eeee7"):
                    opp_val = getattr(item, "kreq108c_Eeee7", None)
                    
                    setattr(item, "kreq108c_Eeee7", self)
                    

    @property
    def kreq108c_Ffff(self):
        return self.__kreq108c_Ffff

    @kreq108c_Ffff.setter
    def kreq108c_Ffff(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kreq108c_Ffff__kreq108c_Ffff", None)
        self.__kreq108c_Ffff = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kreq108c_Cccc4"):
                opp_val = getattr(old_value, "kreq108c_Cccc4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kreq108c_Cccc4"):
                opp_val = getattr(value, "kreq108c_Cccc4", None)
                if opp_val is None:
                    setattr(value, "kreq108c_Cccc4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class kreq108c_Eeee(Gggg):

    def __init__(self, id: str, kreq108c_Eeee: "kreq108c_Bbbb" = None, kreq108c_Eeee7: "kreq108c_Ffff" = None):
        self.id = id
        self.kreq108c_Eeee = kreq108c_Eeee
        self.kreq108c_Eeee7 = kreq108c_Eeee7
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def kreq108c_Eeee7(self):
        return self.__kreq108c_Eeee7

    @kreq108c_Eeee7.setter
    def kreq108c_Eeee7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kreq108c_Eeee__kreq108c_Eeee7", None)
        self.__kreq108c_Eeee7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kreq108c_Ffff6"):
                opp_val = getattr(old_value, "kreq108c_Ffff6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kreq108c_Ffff6"):
                opp_val = getattr(value, "kreq108c_Ffff6", None)
                if opp_val is None:
                    setattr(value, "kreq108c_Ffff6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def kreq108c_Eeee(self):
        return self.__kreq108c_Eeee

    @kreq108c_Eeee.setter
    def kreq108c_Eeee(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kreq108c_Eeee__kreq108c_Eeee", None)
        self.__kreq108c_Eeee = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kreq108c_Bbbb2"):
                opp_val = getattr(old_value, "kreq108c_Bbbb2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kreq108c_Bbbb2"):
                opp_val = getattr(value, "kreq108c_Bbbb2", None)
                if opp_val is None:
                    setattr(value, "kreq108c_Bbbb2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class kreq108c_Cccc:

    def __init__(self, id: str, kreq108c_Cccc: "kreq108c_Bbbb" = None, kreq108c_Cccc4: set["kreq108c_Ffff"] = None):
        self.id = id
        self.kreq108c_Cccc = kreq108c_Cccc
        self.kreq108c_Cccc4 = kreq108c_Cccc4 if kreq108c_Cccc4 is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def kreq108c_Cccc4(self):
        return self.__kreq108c_Cccc4

    @kreq108c_Cccc4.setter
    def kreq108c_Cccc4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kreq108c_Cccc__kreq108c_Cccc4", None)
        self.__kreq108c_Cccc4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "kreq108c_Ffff"):
                    opp_val = getattr(item, "kreq108c_Ffff", None)
                    
                    if opp_val == self:
                        setattr(item, "kreq108c_Ffff", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "kreq108c_Ffff"):
                    opp_val = getattr(item, "kreq108c_Ffff", None)
                    
                    setattr(item, "kreq108c_Ffff", self)
                    

    @property
    def kreq108c_Cccc(self):
        return self.__kreq108c_Cccc

    @kreq108c_Cccc.setter
    def kreq108c_Cccc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kreq108c_Cccc__kreq108c_Cccc", None)
        self.__kreq108c_Cccc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kreq108c_Bbbb"):
                opp_val = getattr(old_value, "kreq108c_Bbbb", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kreq108c_Bbbb"):
                opp_val = getattr(value, "kreq108c_Bbbb", None)
                if opp_val is None:
                    setattr(value, "kreq108c_Bbbb", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class kreq108c_Bbbb:

    pass