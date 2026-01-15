from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Visibility(Enum):
    public = "public"
    private = "private"


############################################
# Definition of Classes
############################################

class classm1_CNamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class CNamedElement:

    pass
class classm1_Attribute(CNamedElement):

    def __init__(self, isKey: bool, visibility: str, classm1_Attribute: "classm1_Class" = None, classm1_Attribute2: "classm1_Class" = None):
        self.isKey = isKey
        self.visibility = visibility
        self.classm1_Attribute = classm1_Attribute
        self.classm1_Attribute2 = classm1_Attribute2
        
    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def isKey(self) -> bool:
        return self.__isKey

    @isKey.setter
    def isKey(self, isKey: bool):
        self.__isKey = isKey

    @property
    def classm1_Attribute(self):
        return self.__classm1_Attribute

    @classm1_Attribute.setter
    def classm1_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classm1_Attribute__classm1_Attribute", None)
        self.__classm1_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classm1_Class"):
                opp_val = getattr(old_value, "classm1_Class", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classm1_Class"):
                opp_val = getattr(value, "classm1_Class", None)
                if opp_val is None:
                    setattr(value, "classm1_Class", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def classm1_Attribute2(self):
        return self.__classm1_Attribute2

    @classm1_Attribute2.setter
    def classm1_Attribute2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classm1_Attribute__classm1_Attribute2", None)
        self.__classm1_Attribute2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classm1_Class3"):
                opp_val = getattr(old_value, "classm1_Class3", None)
                if opp_val == self:
                    setattr(old_value, "classm1_Class3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classm1_Class3"):
                opp_val = getattr(value, "classm1_Class3", None)
                setattr(value, "classm1_Class3", self)

class classm1_Class(CNamedElement):

    pass