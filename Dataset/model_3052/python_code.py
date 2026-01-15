from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class DataTypes(Enum):
    Boolean = "Boolean"
    Long = "Long"
    Double = "Double"
    Object = "Object"
    String = "String"
    Integer = "Integer"
class FetureAnnotation(Enum):
    Index = "Index"
    Id = "Id"
    Load = "Load"
    Ignore = "Ignore"
class EntityAnnotation(Enum):
    Cache = "Cache"


############################################
# Definition of Classes
############################################

class Feature:

    pass
class hermes_DataType(Feature):

    def __init__(self, type: str):
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class hermes_Reference(Feature):

    pass
class NamedElement:

    pass
class hermes_Feature(NamedElement):

    def __init__(self, many: bool, annotations: str, hermes_Feature: "hermes_Entity" = None):
        self.many = many
        self.annotations = annotations
        self.hermes_Feature = hermes_Feature
        
    @property
    def many(self) -> bool:
        return self.__many

    @many.setter
    def many(self, many: bool):
        self.__many = many

    @property
    def annotations(self) -> str:
        return self.__annotations

    @annotations.setter
    def annotations(self, annotations: str):
        self.__annotations = annotations

    @property
    def hermes_Feature(self):
        return self.__hermes_Feature

    @hermes_Feature.setter
    def hermes_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hermes_Feature__hermes_Feature", None)
        self.__hermes_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hermes_Entity4"):
                opp_val = getattr(old_value, "hermes_Entity4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hermes_Entity4"):
                opp_val = getattr(value, "hermes_Entity4", None)
                if opp_val is None:
                    setattr(value, "hermes_Entity4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class hermes_Module(NamedElement):

    pass
class hermes_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class hermes_Entity(NamedElement):

    def __init__(self, annotations: str, hermes_Entity: "hermes_Package" = None, hermes_Entity9: "hermes_Reference" = None, hermes_Entity4: set["hermes_Feature"] = None, hermes_Entity7: "hermes_Entity" = None, hermes_Entity5: "hermes_Entity" = None):
        self.annotations = annotations
        self.hermes_Entity = hermes_Entity
        self.hermes_Entity9 = hermes_Entity9
        self.hermes_Entity4 = hermes_Entity4 if hermes_Entity4 is not None else set()
        self.hermes_Entity7 = hermes_Entity7
        self.hermes_Entity5 = hermes_Entity5
        
    @property
    def annotations(self) -> str:
        return self.__annotations

    @annotations.setter
    def annotations(self, annotations: str):
        self.__annotations = annotations

    @property
    def hermes_Entity9(self):
        return self.__hermes_Entity9

    @hermes_Entity9.setter
    def hermes_Entity9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hermes_Entity__hermes_Entity9", None)
        self.__hermes_Entity9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hermes_Reference"):
                opp_val = getattr(old_value, "hermes_Reference", None)
                if opp_val == self:
                    setattr(old_value, "hermes_Reference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hermes_Reference"):
                opp_val = getattr(value, "hermes_Reference", None)
                setattr(value, "hermes_Reference", self)

    @property
    def hermes_Entity(self):
        return self.__hermes_Entity

    @hermes_Entity.setter
    def hermes_Entity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hermes_Entity__hermes_Entity", None)
        self.__hermes_Entity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hermes_Package2"):
                opp_val = getattr(old_value, "hermes_Package2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hermes_Package2"):
                opp_val = getattr(value, "hermes_Package2", None)
                if opp_val is None:
                    setattr(value, "hermes_Package2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def hermes_Entity4(self):
        return self.__hermes_Entity4

    @hermes_Entity4.setter
    def hermes_Entity4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hermes_Entity__hermes_Entity4", None)
        self.__hermes_Entity4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "hermes_Feature"):
                    opp_val = getattr(item, "hermes_Feature", None)
                    
                    if opp_val == self:
                        setattr(item, "hermes_Feature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "hermes_Feature"):
                    opp_val = getattr(item, "hermes_Feature", None)
                    
                    setattr(item, "hermes_Feature", self)
                    

    @property
    def hermes_Entity7(self):
        return self.__hermes_Entity7

    @hermes_Entity7.setter
    def hermes_Entity7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hermes_Entity__hermes_Entity7", None)
        self.__hermes_Entity7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hermes_Entity5"):
                opp_val = getattr(old_value, "hermes_Entity5", None)
                if opp_val == self:
                    setattr(old_value, "hermes_Entity5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hermes_Entity5"):
                opp_val = getattr(value, "hermes_Entity5", None)
                setattr(value, "hermes_Entity5", self)

    @property
    def hermes_Entity5(self):
        return self.__hermes_Entity5

    @hermes_Entity5.setter
    def hermes_Entity5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hermes_Entity__hermes_Entity5", None)
        self.__hermes_Entity5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hermes_Entity7"):
                opp_val = getattr(old_value, "hermes_Entity7", None)
                if opp_val == self:
                    setattr(old_value, "hermes_Entity7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hermes_Entity7"):
                opp_val = getattr(value, "hermes_Entity7", None)
                setattr(value, "hermes_Entity7", self)

class hermes_Package(NamedElement):

    pass