from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Relation:

    pass
class smalluml_Reference(Relation):

    pass
class smalluml_Composition(Relation):

    pass
class Type:

    pass
class smalluml_Real(Type):

    pass
class smalluml_Bool(Type):

    pass
class smalluml_Integer(Type):

    pass
class smalluml_UnlimitedNatural(Type):

    pass
class smalluml_String(Type):

    pass
class smalluml_Type(ABC):

    pass
class NamedElement:

    pass
class smalluml_Attribute(NamedElement):

    pass
class smalluml_Relation(NamedElement):

    pass
class smalluml_Parameter(NamedElement):

    pass
class smalluml_Enumeration(Type, NamedElement):

    def __init__(self, values: str):
        self.values = values
        
    @property
    def values(self) -> str:
        return self.__values

    @values.setter
    def values(self, values: str):
        self.__values = values

class smalluml_Package(NamedElement):

    pass
class smalluml_Method(NamedElement):

    pass
class smalluml_Role(NamedElement):

    def __init__(self, upperBound: int, lowerBound: int, smalluml_Role: "smalluml_Relation" = None, smalluml_Role19: "smalluml_Relation" = None, smalluml_Role21: "smalluml_Class" = None):
        self.upperBound = upperBound
        self.lowerBound = lowerBound
        self.smalluml_Role = smalluml_Role
        self.smalluml_Role19 = smalluml_Role19
        self.smalluml_Role21 = smalluml_Role21
        
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
    def smalluml_Role21(self):
        return self.__smalluml_Role21

    @smalluml_Role21.setter
    def smalluml_Role21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smalluml_Role__smalluml_Role21", None)
        self.__smalluml_Role21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smalluml_Class22"):
                opp_val = getattr(old_value, "smalluml_Class22", None)
                if opp_val == self:
                    setattr(old_value, "smalluml_Class22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smalluml_Class22"):
                opp_val = getattr(value, "smalluml_Class22", None)
                setattr(value, "smalluml_Class22", self)

    @property
    def smalluml_Role(self):
        return self.__smalluml_Role

    @smalluml_Role.setter
    def smalluml_Role(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smalluml_Role__smalluml_Role", None)
        self.__smalluml_Role = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smalluml_Relation"):
                opp_val = getattr(old_value, "smalluml_Relation", None)
                if opp_val == self:
                    setattr(old_value, "smalluml_Relation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smalluml_Relation"):
                opp_val = getattr(value, "smalluml_Relation", None)
                setattr(value, "smalluml_Relation", self)

    @property
    def smalluml_Role19(self):
        return self.__smalluml_Role19

    @smalluml_Role19.setter
    def smalluml_Role19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smalluml_Role__smalluml_Role19", None)
        self.__smalluml_Role19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smalluml_Relation18"):
                opp_val = getattr(old_value, "smalluml_Relation18", None)
                if opp_val == self:
                    setattr(old_value, "smalluml_Relation18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smalluml_Relation18"):
                opp_val = getattr(value, "smalluml_Relation18", None)
                setattr(value, "smalluml_Relation18", self)

class smalluml_NamedElement(ABC):

    def __init__(self, name: str, smalluml_NamedElement: "smalluml_Package" = None):
        self.name = name
        self.smalluml_NamedElement = smalluml_NamedElement
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def smalluml_NamedElement(self):
        return self.__smalluml_NamedElement

    @smalluml_NamedElement.setter
    def smalluml_NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smalluml_NamedElement__smalluml_NamedElement", None)
        self.__smalluml_NamedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smalluml_Package"):
                opp_val = getattr(old_value, "smalluml_Package", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smalluml_Package"):
                opp_val = getattr(value, "smalluml_Package", None)
                if opp_val is None:
                    setattr(value, "smalluml_Package", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class smalluml_Class(NamedElement):

    pass