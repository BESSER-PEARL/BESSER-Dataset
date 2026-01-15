from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class FeatureKind(Enum):
    attribute = "attribute"
    reference = "reference"
    containment = "containment"


############################################
# Definition of Classes
############################################

class ube_EntityModel:

    pass
class Type:

    pass
class ube_Entity(Type):

    def __init__(self, abstract: bool, ube_Entity: set["ube_Feature"] = None):
        self.abstract = abstract
        self.ube_Entity = ube_Entity if ube_Entity is not None else set()
        
    @property
    def abstract(self) -> bool:
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: bool):
        self.__abstract = abstract

    @property
    def ube_Entity(self):
        return self.__ube_Entity

    @ube_Entity.setter
    def ube_Entity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ube_Entity__ube_Entity", None)
        self.__ube_Entity = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ube_Feature"):
                    opp_val = getattr(item, "ube_Feature", None)
                    
                    if opp_val == self:
                        setattr(item, "ube_Feature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ube_Feature"):
                    opp_val = getattr(item, "ube_Feature", None)
                    
                    setattr(item, "ube_Feature", self)
                    

class ube_DataType(Type):

    pass
class NamedElement:

    pass
class ube_Feature(NamedElement):

    def __init__(self, kind: str, ube_Feature3: "ube_Type" = None, ube_Feature: "ube_Entity" = None):
        self.kind = kind
        self.ube_Feature3 = ube_Feature3
        self.ube_Feature = ube_Feature
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def ube_Feature3(self):
        return self.__ube_Feature3

    @ube_Feature3.setter
    def ube_Feature3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ube_Feature__ube_Feature3", None)
        self.__ube_Feature3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ube_Type4"):
                opp_val = getattr(old_value, "ube_Type4", None)
                if opp_val == self:
                    setattr(old_value, "ube_Type4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ube_Type4"):
                opp_val = getattr(value, "ube_Type4", None)
                setattr(value, "ube_Type4", self)

    @property
    def ube_Feature(self):
        return self.__ube_Feature

    @ube_Feature.setter
    def ube_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ube_Feature__ube_Feature", None)
        self.__ube_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ube_Entity"):
                opp_val = getattr(old_value, "ube_Entity", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ube_Entity"):
                opp_val = getattr(value, "ube_Entity", None)
                if opp_val is None:
                    setattr(value, "ube_Entity", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ube_Type(NamedElement):

    pass
class ube_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name
