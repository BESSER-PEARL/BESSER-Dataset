from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Type:

    pass
class smalluml_String(Type):

    pass
class smalluml_Boolean(Type):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class smalluml_Infinity(Type):

    pass
class smalluml_Integer(Type):

    pass
class smalluml_Real(Type):

    pass
class NamedElement:

    pass
class smalluml_Relation(NamedElement):

    pass
class smalluml_Class(NamedElement):

    pass
class smalluml_Cardinality(NamedElement):

    def __init__(self, lowerBound: int, upperBound: int, smalluml_Cardinality: "smalluml_Relation" = None):
        self.lowerBound = lowerBound
        self.upperBound = upperBound
        self.smalluml_Cardinality = smalluml_Cardinality
        
    @property
    def lowerBound(self) -> int:
        return self.__lowerBound

    @lowerBound.setter
    def lowerBound(self, lowerBound: int):
        self.__lowerBound = lowerBound

    @property
    def upperBound(self) -> int:
        return self.__upperBound

    @upperBound.setter
    def upperBound(self, upperBound: int):
        self.__upperBound = upperBound

    @property
    def smalluml_Cardinality(self):
        return self.__smalluml_Cardinality

    @smalluml_Cardinality.setter
    def smalluml_Cardinality(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smalluml_Cardinality__smalluml_Cardinality", None)
        self.__smalluml_Cardinality = value
        
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

class smalluml_Generalisation(NamedElement):

    pass
class smalluml_Attribute(NamedElement):

    pass
class smalluml_Package(NamedElement):

    pass
class smalluml_Enumeration(NamedElement, Type):

    pass
class smalluml_Method(NamedElement):

    pass
class smalluml_Type(NamedElement):

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
