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

class myDSL_EntityModel:

    pass
class NamedElement:

    pass
class myDSL_Type(NamedElement):

    pass
class myDSL_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class myDSL_Feature(NamedElement):

    def __init__(self, kind: str, myDSL_Feature: "myDSL_Entity" = None, myDSL_Feature3: "myDSL_Type" = None):
        self.kind = kind
        self.myDSL_Feature = myDSL_Feature
        self.myDSL_Feature3 = myDSL_Feature3
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def myDSL_Feature(self):
        return self.__myDSL_Feature

    @myDSL_Feature.setter
    def myDSL_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDSL_Feature__myDSL_Feature", None)
        self.__myDSL_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDSL_Entity"):
                opp_val = getattr(old_value, "myDSL_Entity", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDSL_Entity"):
                opp_val = getattr(value, "myDSL_Entity", None)
                if opp_val is None:
                    setattr(value, "myDSL_Entity", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myDSL_Feature3(self):
        return self.__myDSL_Feature3

    @myDSL_Feature3.setter
    def myDSL_Feature3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDSL_Feature__myDSL_Feature3", None)
        self.__myDSL_Feature3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDSL_Type4"):
                opp_val = getattr(old_value, "myDSL_Type4", None)
                if opp_val == self:
                    setattr(old_value, "myDSL_Type4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDSL_Type4"):
                opp_val = getattr(value, "myDSL_Type4", None)
                setattr(value, "myDSL_Type4", self)

class Type:

    pass
class myDSL_Entity(Type):

    def __init__(self, abstract: bool, myDSL_Entity: set["myDSL_Feature"] = None):
        self.abstract = abstract
        self.myDSL_Entity = myDSL_Entity if myDSL_Entity is not None else set()
        
    @property
    def abstract(self) -> bool:
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: bool):
        self.__abstract = abstract

    @property
    def myDSL_Entity(self):
        return self.__myDSL_Entity

    @myDSL_Entity.setter
    def myDSL_Entity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDSL_Entity__myDSL_Entity", None)
        self.__myDSL_Entity = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDSL_Feature"):
                    opp_val = getattr(item, "myDSL_Feature", None)
                    
                    if opp_val == self:
                        setattr(item, "myDSL_Feature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDSL_Feature"):
                    opp_val = getattr(item, "myDSL_Feature", None)
                    
                    setattr(item, "myDSL_Feature", self)
                    

class myDSL_DataType(Type):

    pass