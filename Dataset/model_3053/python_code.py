from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class EntityAnnotation(Enum):
    Cache = "Cache"
class FetureAnnotation(Enum):
    Index = "Index"
    Id = "Id"
    Load = "Load"
    Ignore = "Ignore"
class DataTypes(Enum):
    Object = "Object"
    String = "String"
    Integer = "Integer"
    Boolean = "Boolean"
    Long = "Long"
    Double = "Double"


############################################
# Definition of Classes
############################################

class Feature:

    pass
class hibernate_DataType(Feature):

    def __init__(self, type: str):
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class hibernate_Reference(Feature):

    pass
class NamedElement:

    pass
class hibernate_Feature(NamedElement):

    def __init__(self, many: bool, annotations: str, hibernate_Feature: "hibernate_Entity" = None):
        self.many = many
        self.annotations = annotations
        self.hibernate_Feature = hibernate_Feature
        
    @property
    def annotations(self) -> str:
        return self.__annotations

    @annotations.setter
    def annotations(self, annotations: str):
        self.__annotations = annotations

    @property
    def many(self) -> bool:
        return self.__many

    @many.setter
    def many(self, many: bool):
        self.__many = many

    @property
    def hibernate_Feature(self):
        return self.__hibernate_Feature

    @hibernate_Feature.setter
    def hibernate_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hibernate_Feature__hibernate_Feature", None)
        self.__hibernate_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hibernate_Entity4"):
                opp_val = getattr(old_value, "hibernate_Entity4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hibernate_Entity4"):
                opp_val = getattr(value, "hibernate_Entity4", None)
                if opp_val is None:
                    setattr(value, "hibernate_Entity4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class hibernate_Package(NamedElement):

    pass
class hibernate_Module(NamedElement):

    pass
class hibernate_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class hibernate_Entity(NamedElement):

    def __init__(self, annotations: str, hibernate_Entity: "hibernate_Package" = None, hibernate_Entity9: "hibernate_Reference" = None, hibernate_Entity4: set["hibernate_Feature"] = None, hibernate_Entity7: "hibernate_Entity" = None, hibernate_Entity5: "hibernate_Entity" = None):
        self.annotations = annotations
        self.hibernate_Entity = hibernate_Entity
        self.hibernate_Entity9 = hibernate_Entity9
        self.hibernate_Entity4 = hibernate_Entity4 if hibernate_Entity4 is not None else set()
        self.hibernate_Entity7 = hibernate_Entity7
        self.hibernate_Entity5 = hibernate_Entity5
        
    @property
    def annotations(self) -> str:
        return self.__annotations

    @annotations.setter
    def annotations(self, annotations: str):
        self.__annotations = annotations

    @property
    def hibernate_Entity(self):
        return self.__hibernate_Entity

    @hibernate_Entity.setter
    def hibernate_Entity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hibernate_Entity__hibernate_Entity", None)
        self.__hibernate_Entity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hibernate_Package2"):
                opp_val = getattr(old_value, "hibernate_Package2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hibernate_Package2"):
                opp_val = getattr(value, "hibernate_Package2", None)
                if opp_val is None:
                    setattr(value, "hibernate_Package2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def hibernate_Entity4(self):
        return self.__hibernate_Entity4

    @hibernate_Entity4.setter
    def hibernate_Entity4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hibernate_Entity__hibernate_Entity4", None)
        self.__hibernate_Entity4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "hibernate_Feature"):
                    opp_val = getattr(item, "hibernate_Feature", None)
                    
                    if opp_val == self:
                        setattr(item, "hibernate_Feature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "hibernate_Feature"):
                    opp_val = getattr(item, "hibernate_Feature", None)
                    
                    setattr(item, "hibernate_Feature", self)
                    

    @property
    def hibernate_Entity9(self):
        return self.__hibernate_Entity9

    @hibernate_Entity9.setter
    def hibernate_Entity9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hibernate_Entity__hibernate_Entity9", None)
        self.__hibernate_Entity9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hibernate_Reference"):
                opp_val = getattr(old_value, "hibernate_Reference", None)
                if opp_val == self:
                    setattr(old_value, "hibernate_Reference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hibernate_Reference"):
                opp_val = getattr(value, "hibernate_Reference", None)
                setattr(value, "hibernate_Reference", self)

    @property
    def hibernate_Entity5(self):
        return self.__hibernate_Entity5

    @hibernate_Entity5.setter
    def hibernate_Entity5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hibernate_Entity__hibernate_Entity5", None)
        self.__hibernate_Entity5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hibernate_Entity7"):
                opp_val = getattr(old_value, "hibernate_Entity7", None)
                if opp_val == self:
                    setattr(old_value, "hibernate_Entity7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hibernate_Entity7"):
                opp_val = getattr(value, "hibernate_Entity7", None)
                setattr(value, "hibernate_Entity7", self)

    @property
    def hibernate_Entity7(self):
        return self.__hibernate_Entity7

    @hibernate_Entity7.setter
    def hibernate_Entity7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hibernate_Entity__hibernate_Entity7", None)
        self.__hibernate_Entity7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hibernate_Entity5"):
                opp_val = getattr(old_value, "hibernate_Entity5", None)
                if opp_val == self:
                    setattr(old_value, "hibernate_Entity5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hibernate_Entity5"):
                opp_val = getattr(value, "hibernate_Entity5", None)
                setattr(value, "hibernate_Entity5", self)
