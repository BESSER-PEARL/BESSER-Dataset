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
class coral_DataType(Type):

    pass
class NamedElement:

    pass
class coral_Type(NamedElement):

    pass
class coral_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class coral_EntityModel:

    pass
class coral_Feature(NamedElement):

    def __init__(self, kind: str, coral_Feature: "coral_Entity" = None, coral_Feature3: "coral_Type" = None):
        self.kind = kind
        self.coral_Feature = coral_Feature
        self.coral_Feature3 = coral_Feature3
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def coral_Feature3(self):
        return self.__coral_Feature3

    @coral_Feature3.setter
    def coral_Feature3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coral_Feature__coral_Feature3", None)
        self.__coral_Feature3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coral_Type4"):
                opp_val = getattr(old_value, "coral_Type4", None)
                if opp_val == self:
                    setattr(old_value, "coral_Type4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coral_Type4"):
                opp_val = getattr(value, "coral_Type4", None)
                setattr(value, "coral_Type4", self)

    @property
    def coral_Feature(self):
        return self.__coral_Feature

    @coral_Feature.setter
    def coral_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coral_Feature__coral_Feature", None)
        self.__coral_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coral_Entity"):
                opp_val = getattr(old_value, "coral_Entity", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coral_Entity"):
                opp_val = getattr(value, "coral_Entity", None)
                if opp_val is None:
                    setattr(value, "coral_Entity", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class coral_Entity(Type):

    def __init__(self, abstract: bool, coral_Entity: set["coral_Feature"] = None):
        self.abstract = abstract
        self.coral_Entity = coral_Entity if coral_Entity is not None else set()
        
    @property
    def abstract(self) -> bool:
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: bool):
        self.__abstract = abstract

    @property
    def coral_Entity(self):
        return self.__coral_Entity

    @coral_Entity.setter
    def coral_Entity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coral_Entity__coral_Entity", None)
        self.__coral_Entity = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "coral_Feature"):
                    opp_val = getattr(item, "coral_Feature", None)
                    
                    if opp_val == self:
                        setattr(item, "coral_Feature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "coral_Feature"):
                    opp_val = getattr(item, "coral_Feature", None)
                    
                    setattr(item, "coral_Feature", self)
                    
