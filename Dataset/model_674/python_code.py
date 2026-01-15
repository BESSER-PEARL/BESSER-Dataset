from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class smalluml_Root:

    pass
class smalluml_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class NamedElement:

    pass
class smalluml_Property(NamedElement):

    def __init__(self, upperBound: int, lowerBound: int, smalluml_Property12: "smalluml_Type" = None, smalluml_Property: "smalluml_Class" = None):
        self.upperBound = upperBound
        self.lowerBound = lowerBound
        self.smalluml_Property12 = smalluml_Property12
        self.smalluml_Property = smalluml_Property
        
    @property
    def upperBound(self) -> int:
        return self.__upperBound

    @upperBound.setter
    def upperBound(self, upperBound: int):
        self.__upperBound = upperBound

    @property
    def lowerBound(self) -> int:
        return self.__lowerBound

    @lowerBound.setter
    def lowerBound(self, lowerBound: int):
        self.__lowerBound = lowerBound

    @property
    def smalluml_Property(self):
        return self.__smalluml_Property

    @smalluml_Property.setter
    def smalluml_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smalluml_Property__smalluml_Property", None)
        self.__smalluml_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smalluml_Class5"):
                opp_val = getattr(old_value, "smalluml_Class5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smalluml_Class5"):
                opp_val = getattr(value, "smalluml_Class5", None)
                if opp_val is None:
                    setattr(value, "smalluml_Class5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def smalluml_Property12(self):
        return self.__smalluml_Property12

    @smalluml_Property12.setter
    def smalluml_Property12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smalluml_Property__smalluml_Property12", None)
        self.__smalluml_Property12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smalluml_Type13"):
                opp_val = getattr(old_value, "smalluml_Type13", None)
                if opp_val == self:
                    setattr(old_value, "smalluml_Type13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smalluml_Type13"):
                opp_val = getattr(value, "smalluml_Type13", None)
                setattr(value, "smalluml_Type13", self)

class smalluml_Type(NamedElement):

    pass
class smalluml_Operation(NamedElement):

    pass
class Type:

    pass
class smalluml_TypeInteger(Type):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class smalluml_TypeBoolean(Type):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class smalluml_TypeString(Type):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class smalluml_TypeUnlimitedNatural(Type):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class smalluml_TypeReal(Type):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class smalluml_Class(Type):

    pass