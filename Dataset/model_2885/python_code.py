from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Annotation(Enum):
    None = "None"
    OneToOne = "OneToOne"
    OneToMany = "OneToMany"
    ManyToOne = "ManyToOne"
    ManyToMany = "ManyToMany"
    ManyToManyMapped = "ManyToManyMapped"
    Id = "Id"


############################################
# Definition of Classes
############################################

class metamodel_parameter:

    def __init__(self, name: str, metamodel_parameter: "metamodel_Query" = None, metamodel_parameter13: "metamodel_Type" = None):
        self.name = name
        self.metamodel_parameter = metamodel_parameter
        self.metamodel_parameter13 = metamodel_parameter13
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def metamodel_parameter(self):
        return self.__metamodel_parameter

    @metamodel_parameter.setter
    def metamodel_parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_parameter__metamodel_parameter", None)
        self.__metamodel_parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodel_Query11"):
                opp_val = getattr(old_value, "metamodel_Query11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodel_Query11"):
                opp_val = getattr(value, "metamodel_Query11", None)
                if opp_val is None:
                    setattr(value, "metamodel_Query11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def metamodel_parameter13(self):
        return self.__metamodel_parameter13

    @metamodel_parameter13.setter
    def metamodel_parameter13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_parameter__metamodel_parameter13", None)
        self.__metamodel_parameter13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodel_Type14"):
                opp_val = getattr(old_value, "metamodel_Type14", None)
                if opp_val == self:
                    setattr(old_value, "metamodel_Type14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodel_Type14"):
                opp_val = getattr(value, "metamodel_Type14", None)
                setattr(value, "metamodel_Type14", self)

class metamodel_Query:

    def __init__(self, methodName: str, queryString: str, metamodel_Query: "metamodel_Entity" = None, metamodel_Query8: "metamodel_Entity" = None, metamodel_Query11: set["metamodel_parameter"] = None):
        self.methodName = methodName
        self.queryString = queryString
        self.metamodel_Query = metamodel_Query
        self.metamodel_Query8 = metamodel_Query8
        self.metamodel_Query11 = metamodel_Query11 if metamodel_Query11 is not None else set()
        
    @property
    def queryString(self) -> str:
        return self.__queryString

    @queryString.setter
    def queryString(self, queryString: str):
        self.__queryString = queryString

    @property
    def methodName(self) -> str:
        return self.__methodName

    @methodName.setter
    def methodName(self, methodName: str):
        self.__methodName = methodName

    @property
    def metamodel_Query11(self):
        return self.__metamodel_Query11

    @metamodel_Query11.setter
    def metamodel_Query11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_Query__metamodel_Query11", None)
        self.__metamodel_Query11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "metamodel_parameter"):
                    opp_val = getattr(item, "metamodel_parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "metamodel_parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "metamodel_parameter"):
                    opp_val = getattr(item, "metamodel_parameter", None)
                    
                    setattr(item, "metamodel_parameter", self)
                    

    @property
    def metamodel_Query(self):
        return self.__metamodel_Query

    @metamodel_Query.setter
    def metamodel_Query(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_Query__metamodel_Query", None)
        self.__metamodel_Query = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodel_Entity3"):
                opp_val = getattr(old_value, "metamodel_Entity3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodel_Entity3"):
                opp_val = getattr(value, "metamodel_Entity3", None)
                if opp_val is None:
                    setattr(value, "metamodel_Entity3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def metamodel_Query8(self):
        return self.__metamodel_Query8

    @metamodel_Query8.setter
    def metamodel_Query8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_Query__metamodel_Query8", None)
        self.__metamodel_Query8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodel_Entity9"):
                opp_val = getattr(old_value, "metamodel_Entity9", None)
                if opp_val == self:
                    setattr(old_value, "metamodel_Entity9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodel_Entity9"):
                opp_val = getattr(value, "metamodel_Entity9", None)
                setattr(value, "metamodel_Entity9", self)

class metamodel_Feature:

    def __init__(self, name: str, annotation: str, mappedBy: str, metamodel_Feature: "metamodel_Entity" = None, metamodel_Feature5: "metamodel_Type" = None):
        self.name = name
        self.annotation = annotation
        self.mappedBy = mappedBy
        self.metamodel_Feature = metamodel_Feature
        self.metamodel_Feature5 = metamodel_Feature5
        
    @property
    def mappedBy(self) -> str:
        return self.__mappedBy

    @mappedBy.setter
    def mappedBy(self, mappedBy: str):
        self.__mappedBy = mappedBy

    @property
    def annotation(self) -> str:
        return self.__annotation

    @annotation.setter
    def annotation(self, annotation: str):
        self.__annotation = annotation

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def metamodel_Feature(self):
        return self.__metamodel_Feature

    @metamodel_Feature.setter
    def metamodel_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_Feature__metamodel_Feature", None)
        self.__metamodel_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodel_Entity"):
                opp_val = getattr(old_value, "metamodel_Entity", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodel_Entity"):
                opp_val = getattr(value, "metamodel_Entity", None)
                if opp_val is None:
                    setattr(value, "metamodel_Entity", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def metamodel_Feature5(self):
        return self.__metamodel_Feature5

    @metamodel_Feature5.setter
    def metamodel_Feature5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_Feature__metamodel_Feature5", None)
        self.__metamodel_Feature5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodel_Type6"):
                opp_val = getattr(old_value, "metamodel_Type6", None)
                if opp_val == self:
                    setattr(old_value, "metamodel_Type6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodel_Type6"):
                opp_val = getattr(value, "metamodel_Type6", None)
                setattr(value, "metamodel_Type6", self)

class Type:

    pass
class metamodel_Entity(Type):

    pass
class metamodel_Datatype(Type):

    pass
class metamodel_Type(ABC):

    def __init__(self, name: str, metamodel_Type: "metamodel_Model" = None, metamodel_Type6: "metamodel_Feature" = None, metamodel_Type14: "metamodel_parameter" = None):
        self.name = name
        self.metamodel_Type = metamodel_Type
        self.metamodel_Type6 = metamodel_Type6
        self.metamodel_Type14 = metamodel_Type14
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def metamodel_Type(self):
        return self.__metamodel_Type

    @metamodel_Type.setter
    def metamodel_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_Type__metamodel_Type", None)
        self.__metamodel_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodel_Model"):
                opp_val = getattr(old_value, "metamodel_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodel_Model"):
                opp_val = getattr(value, "metamodel_Model", None)
                if opp_val is None:
                    setattr(value, "metamodel_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def metamodel_Type6(self):
        return self.__metamodel_Type6

    @metamodel_Type6.setter
    def metamodel_Type6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_Type__metamodel_Type6", None)
        self.__metamodel_Type6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodel_Feature5"):
                opp_val = getattr(old_value, "metamodel_Feature5", None)
                if opp_val == self:
                    setattr(old_value, "metamodel_Feature5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodel_Feature5"):
                opp_val = getattr(value, "metamodel_Feature5", None)
                setattr(value, "metamodel_Feature5", self)

    @property
    def metamodel_Type14(self):
        return self.__metamodel_Type14

    @metamodel_Type14.setter
    def metamodel_Type14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_Type__metamodel_Type14", None)
        self.__metamodel_Type14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodel_parameter13"):
                opp_val = getattr(old_value, "metamodel_parameter13", None)
                if opp_val == self:
                    setattr(old_value, "metamodel_parameter13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodel_parameter13"):
                opp_val = getattr(value, "metamodel_parameter13", None)
                setattr(value, "metamodel_parameter13", self)

class metamodel_Model:

    pass