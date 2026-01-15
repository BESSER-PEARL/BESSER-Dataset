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

class Type:

    pass
class hbmxml_Entity(Type):

    def __init__(self, abstract: bool, hbmxml_Entity: set["hbmxml_Feature"] = None):
        self.abstract = abstract
        self.hbmxml_Entity = hbmxml_Entity if hbmxml_Entity is not None else set()
        
    @property
    def abstract(self) -> bool:
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: bool):
        self.__abstract = abstract

    @property
    def hbmxml_Entity(self):
        return self.__hbmxml_Entity

    @hbmxml_Entity.setter
    def hbmxml_Entity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hbmxml_Entity__hbmxml_Entity", None)
        self.__hbmxml_Entity = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "hbmxml_Feature"):
                    opp_val = getattr(item, "hbmxml_Feature", None)
                    
                    if opp_val == self:
                        setattr(item, "hbmxml_Feature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "hbmxml_Feature"):
                    opp_val = getattr(item, "hbmxml_Feature", None)
                    
                    setattr(item, "hbmxml_Feature", self)
                    

class hbmxml_DataType(Type):

    pass
class NamedElement:

    pass
class hbmxml_Feature(NamedElement):

    def __init__(self, kind: str, hbmxml_Feature3: "hbmxml_Type" = None, hbmxml_Feature: "hbmxml_Entity" = None):
        self.kind = kind
        self.hbmxml_Feature3 = hbmxml_Feature3
        self.hbmxml_Feature = hbmxml_Feature
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def hbmxml_Feature(self):
        return self.__hbmxml_Feature

    @hbmxml_Feature.setter
    def hbmxml_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hbmxml_Feature__hbmxml_Feature", None)
        self.__hbmxml_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hbmxml_Entity"):
                opp_val = getattr(old_value, "hbmxml_Entity", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hbmxml_Entity"):
                opp_val = getattr(value, "hbmxml_Entity", None)
                if opp_val is None:
                    setattr(value, "hbmxml_Entity", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def hbmxml_Feature3(self):
        return self.__hbmxml_Feature3

    @hbmxml_Feature3.setter
    def hbmxml_Feature3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hbmxml_Feature__hbmxml_Feature3", None)
        self.__hbmxml_Feature3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hbmxml_Type4"):
                opp_val = getattr(old_value, "hbmxml_Type4", None)
                if opp_val == self:
                    setattr(old_value, "hbmxml_Type4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hbmxml_Type4"):
                opp_val = getattr(value, "hbmxml_Type4", None)
                setattr(value, "hbmxml_Type4", self)

class hbmxml_Type(NamedElement):

    pass
class hbmxml_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class hbmxml_EntityModel:

    pass