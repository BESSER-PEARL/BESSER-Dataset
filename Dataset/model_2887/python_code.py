from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class HibernateCascadeTypes(Enum):
    NONE = "NONE"
    ALL = "ALL"
class HibernateAnnotationTypes(Enum):
    OneToMany = "OneToMany"
    ManyToOne = "ManyToOne"
    ManyToMany = "ManyToMany"
    OneToOne = "OneToOne"
    Column = "Column"


############################################
# Definition of Classes
############################################

class metamodel_HibernateAnnotation:

    def __init__(self, annotationType: str, unique: str, cascade: str, metamodel_HibernateAnnotation: "metamodel_Attribute" = None, metamodel_HibernateAnnotation8: "metamodel_Attribute" = None):
        self.annotationType = annotationType
        self.unique = unique
        self.cascade = cascade
        self.metamodel_HibernateAnnotation = metamodel_HibernateAnnotation
        self.metamodel_HibernateAnnotation8 = metamodel_HibernateAnnotation8
        
    @property
    def cascade(self) -> str:
        return self.__cascade

    @cascade.setter
    def cascade(self, cascade: str):
        self.__cascade = cascade

    @property
    def unique(self) -> str:
        return self.__unique

    @unique.setter
    def unique(self, unique: str):
        self.__unique = unique

    @property
    def annotationType(self) -> str:
        return self.__annotationType

    @annotationType.setter
    def annotationType(self, annotationType: str):
        self.__annotationType = annotationType

    @property
    def metamodel_HibernateAnnotation(self):
        return self.__metamodel_HibernateAnnotation

    @metamodel_HibernateAnnotation.setter
    def metamodel_HibernateAnnotation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_HibernateAnnotation__metamodel_HibernateAnnotation", None)
        self.__metamodel_HibernateAnnotation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodel_Attribute6"):
                opp_val = getattr(old_value, "metamodel_Attribute6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodel_Attribute6"):
                opp_val = getattr(value, "metamodel_Attribute6", None)
                if opp_val is None:
                    setattr(value, "metamodel_Attribute6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def metamodel_HibernateAnnotation8(self):
        return self.__metamodel_HibernateAnnotation8

    @metamodel_HibernateAnnotation8.setter
    def metamodel_HibernateAnnotation8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_HibernateAnnotation__metamodel_HibernateAnnotation8", None)
        self.__metamodel_HibernateAnnotation8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodel_Attribute9"):
                opp_val = getattr(old_value, "metamodel_Attribute9", None)
                if opp_val == self:
                    setattr(old_value, "metamodel_Attribute9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodel_Attribute9"):
                opp_val = getattr(value, "metamodel_Attribute9", None)
                setattr(value, "metamodel_Attribute9", self)

class metamodel_Attribute:

    def __init__(self, name: str, list: bool, metamodel_Attribute: "metamodel_Entity" = None, metamodel_Attribute3: "metamodel_Type" = None, metamodel_Attribute6: set["metamodel_HibernateAnnotation"] = None, metamodel_Attribute9: "metamodel_HibernateAnnotation" = None):
        self.name = name
        self.list = list
        self.metamodel_Attribute = metamodel_Attribute
        self.metamodel_Attribute3 = metamodel_Attribute3
        self.metamodel_Attribute6 = metamodel_Attribute6 if metamodel_Attribute6 is not None else set()
        self.metamodel_Attribute9 = metamodel_Attribute9
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def list(self) -> bool:
        return self.__list

    @list.setter
    def list(self, list: bool):
        self.__list = list

    @property
    def metamodel_Attribute(self):
        return self.__metamodel_Attribute

    @metamodel_Attribute.setter
    def metamodel_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_Attribute__metamodel_Attribute", None)
        self.__metamodel_Attribute = value
        
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
    def metamodel_Attribute6(self):
        return self.__metamodel_Attribute6

    @metamodel_Attribute6.setter
    def metamodel_Attribute6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_Attribute__metamodel_Attribute6", None)
        self.__metamodel_Attribute6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "metamodel_HibernateAnnotation"):
                    opp_val = getattr(item, "metamodel_HibernateAnnotation", None)
                    
                    if opp_val == self:
                        setattr(item, "metamodel_HibernateAnnotation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "metamodel_HibernateAnnotation"):
                    opp_val = getattr(item, "metamodel_HibernateAnnotation", None)
                    
                    setattr(item, "metamodel_HibernateAnnotation", self)
                    

    @property
    def metamodel_Attribute3(self):
        return self.__metamodel_Attribute3

    @metamodel_Attribute3.setter
    def metamodel_Attribute3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_Attribute__metamodel_Attribute3", None)
        self.__metamodel_Attribute3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodel_Type4"):
                opp_val = getattr(old_value, "metamodel_Type4", None)
                if opp_val == self:
                    setattr(old_value, "metamodel_Type4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodel_Type4"):
                opp_val = getattr(value, "metamodel_Type4", None)
                setattr(value, "metamodel_Type4", self)

    @property
    def metamodel_Attribute9(self):
        return self.__metamodel_Attribute9

    @metamodel_Attribute9.setter
    def metamodel_Attribute9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_Attribute__metamodel_Attribute9", None)
        self.__metamodel_Attribute9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodel_HibernateAnnotation8"):
                opp_val = getattr(old_value, "metamodel_HibernateAnnotation8", None)
                if opp_val == self:
                    setattr(old_value, "metamodel_HibernateAnnotation8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodel_HibernateAnnotation8"):
                opp_val = getattr(value, "metamodel_HibernateAnnotation8", None)
                setattr(value, "metamodel_HibernateAnnotation8", self)

class Type:

    pass
class metamodel_Entity(Type):

    pass
class metamodel_Datatype(Type):

    pass
class metamodel_Type(ABC):

    def __init__(self, name: str, metamodel_Type: "metamodel_Model" = None, metamodel_Type4: "metamodel_Attribute" = None):
        self.name = name
        self.metamodel_Type = metamodel_Type
        self.metamodel_Type4 = metamodel_Type4
        
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
    def metamodel_Type4(self):
        return self.__metamodel_Type4

    @metamodel_Type4.setter
    def metamodel_Type4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_Type__metamodel_Type4", None)
        self.__metamodel_Type4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodel_Attribute3"):
                opp_val = getattr(old_value, "metamodel_Attribute3", None)
                if opp_val == self:
                    setattr(old_value, "metamodel_Attribute3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodel_Attribute3"):
                opp_val = getattr(value, "metamodel_Attribute3", None)
                setattr(value, "metamodel_Attribute3", self)

class metamodel_Model:

    pass