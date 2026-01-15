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
class forms_Entity(Type):

    def __init__(self, abstract: bool, forms_Entity: set["forms_Feature"] = None):
        self.abstract = abstract
        self.forms_Entity = forms_Entity if forms_Entity is not None else set()
        
    @property
    def abstract(self) -> bool:
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: bool):
        self.__abstract = abstract

    @property
    def forms_Entity(self):
        return self.__forms_Entity

    @forms_Entity.setter
    def forms_Entity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Entity__forms_Entity", None)
        self.__forms_Entity = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "forms_Feature"):
                    opp_val = getattr(item, "forms_Feature", None)
                    
                    if opp_val == self:
                        setattr(item, "forms_Feature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "forms_Feature"):
                    opp_val = getattr(item, "forms_Feature", None)
                    
                    setattr(item, "forms_Feature", self)
                    

class forms_DataType(Type):

    pass
class NamedElement:

    pass
class forms_Type(NamedElement):

    pass
class forms_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class forms_EntityModel:

    pass
class forms_Feature(NamedElement):

    def __init__(self, kind: str, forms_Feature: "forms_Entity" = None, forms_Feature3: "forms_Type" = None):
        self.kind = kind
        self.forms_Feature = forms_Feature
        self.forms_Feature3 = forms_Feature3
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def forms_Feature3(self):
        return self.__forms_Feature3

    @forms_Feature3.setter
    def forms_Feature3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Feature__forms_Feature3", None)
        self.__forms_Feature3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_Type4"):
                opp_val = getattr(old_value, "forms_Type4", None)
                if opp_val == self:
                    setattr(old_value, "forms_Type4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Type4"):
                opp_val = getattr(value, "forms_Type4", None)
                setattr(value, "forms_Type4", self)

    @property
    def forms_Feature(self):
        return self.__forms_Feature

    @forms_Feature.setter
    def forms_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Feature__forms_Feature", None)
        self.__forms_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_Entity"):
                opp_val = getattr(old_value, "forms_Entity", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Entity"):
                opp_val = getattr(value, "forms_Entity", None)
                if opp_val is None:
                    setattr(value, "forms_Entity", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
