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

class bombXML_EntityModel:

    pass
class Type:

    pass
class bombXML_Entity(Type):

    def __init__(self, abstract: bool, bombXML_Entity: set["bombXML_Feature"] = None):
        self.abstract = abstract
        self.bombXML_Entity = bombXML_Entity if bombXML_Entity is not None else set()
        
    @property
    def abstract(self) -> bool:
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: bool):
        self.__abstract = abstract

    @property
    def bombXML_Entity(self):
        return self.__bombXML_Entity

    @bombXML_Entity.setter
    def bombXML_Entity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bombXML_Entity__bombXML_Entity", None)
        self.__bombXML_Entity = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bombXML_Feature"):
                    opp_val = getattr(item, "bombXML_Feature", None)
                    
                    if opp_val == self:
                        setattr(item, "bombXML_Feature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bombXML_Feature"):
                    opp_val = getattr(item, "bombXML_Feature", None)
                    
                    setattr(item, "bombXML_Feature", self)
                    

class bombXML_DataType(Type):

    pass
class NamedElement:

    pass
class bombXML_Feature(NamedElement):

    def __init__(self, kind: str, bombXML_Feature: "bombXML_Entity" = None, bombXML_Feature3: "bombXML_Type" = None):
        self.kind = kind
        self.bombXML_Feature = bombXML_Feature
        self.bombXML_Feature3 = bombXML_Feature3
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def bombXML_Feature3(self):
        return self.__bombXML_Feature3

    @bombXML_Feature3.setter
    def bombXML_Feature3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bombXML_Feature__bombXML_Feature3", None)
        self.__bombXML_Feature3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bombXML_Type4"):
                opp_val = getattr(old_value, "bombXML_Type4", None)
                if opp_val == self:
                    setattr(old_value, "bombXML_Type4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bombXML_Type4"):
                opp_val = getattr(value, "bombXML_Type4", None)
                setattr(value, "bombXML_Type4", self)

    @property
    def bombXML_Feature(self):
        return self.__bombXML_Feature

    @bombXML_Feature.setter
    def bombXML_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bombXML_Feature__bombXML_Feature", None)
        self.__bombXML_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bombXML_Entity"):
                opp_val = getattr(old_value, "bombXML_Entity", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bombXML_Entity"):
                opp_val = getattr(value, "bombXML_Entity", None)
                if opp_val is None:
                    setattr(value, "bombXML_Entity", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class bombXML_Type(NamedElement):

    pass
class bombXML_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name
