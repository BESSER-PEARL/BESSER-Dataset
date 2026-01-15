from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Foo:

    pass
class c_Bar(Foo):

    def __init__(self, value: str, c_Bar: "c_Foo" = None, c_Bar2: set["c_Foo"] = None):
        self.value = value
        self.c_Bar = c_Bar
        self.c_Bar2 = c_Bar2 if c_Bar2 is not None else set()
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def c_Bar(self):
        return self.__c_Bar

    @c_Bar.setter
    def c_Bar(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_c_Bar__c_Bar", None)
        self.__c_Bar = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "c_Foo"):
                opp_val = getattr(old_value, "c_Foo", None)
                if opp_val == self:
                    setattr(old_value, "c_Foo", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "c_Foo"):
                opp_val = getattr(value, "c_Foo", None)
                setattr(value, "c_Foo", self)

    @property
    def c_Bar2(self):
        return self.__c_Bar2

    @c_Bar2.setter
    def c_Bar2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_c_Bar__c_Bar2", None)
        self.__c_Bar2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "c_Foo3"):
                    opp_val = getattr(item, "c_Foo3", None)
                    
                    if opp_val == self:
                        setattr(item, "c_Foo3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "c_Foo3"):
                    opp_val = getattr(item, "c_Foo3", None)
                    
                    setattr(item, "c_Foo3", self)
                    

class AbstractClass:

    pass
class c_Foo(AbstractClass):

    def __init__(self, description: str, c_Foo: "c_Bar" = None, c_Foo3: "c_Bar" = None):
        self.description = description
        self.c_Foo = c_Foo
        self.c_Foo3 = c_Foo3
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def c_Foo3(self):
        return self.__c_Foo3

    @c_Foo3.setter
    def c_Foo3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_c_Foo__c_Foo3", None)
        self.__c_Foo3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "c_Bar2"):
                opp_val = getattr(old_value, "c_Bar2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "c_Bar2"):
                opp_val = getattr(value, "c_Bar2", None)
                if opp_val is None:
                    setattr(value, "c_Bar2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def c_Foo(self):
        return self.__c_Foo

    @c_Foo.setter
    def c_Foo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_c_Foo__c_Foo", None)
        self.__c_Foo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "c_Bar"):
                opp_val = getattr(old_value, "c_Bar", None)
                if opp_val == self:
                    setattr(old_value, "c_Bar", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "c_Bar"):
                opp_val = getattr(value, "c_Bar", None)
                setattr(value, "c_Bar", self)

class c_AbstractClass(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name
