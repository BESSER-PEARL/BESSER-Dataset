from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class beans_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class NamedElement:

    pass
class beans_BeanProperty(NamedElement):

    def __init__(self, typeName: str, changeable: bool, properties: "beans_Bean" = None, BeanProperty: "beans_Bean" = None):
        self.typeName = typeName
        self.changeable = changeable
        self.properties = properties
        self.BeanProperty = BeanProperty
        
    @property
    def typeName(self) -> str:
        return self.__typeName

    @typeName.setter
    def typeName(self, typeName: str):
        self.__typeName = typeName

    @property
    def changeable(self) -> bool:
        return self.__changeable

    @changeable.setter
    def changeable(self, changeable: bool):
        self.__changeable = changeable

    @property
    def properties(self):
        return self.__properties

    @properties.setter
    def properties(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_beans_BeanProperty__properties", None)
        self.__properties = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Bean4"):
                opp_val = getattr(old_value, "Bean4", None)
                if opp_val == self:
                    setattr(old_value, "Bean4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Bean4"):
                opp_val = getattr(value, "Bean4", None)
                setattr(value, "Bean4", self)

    @property
    def BeanProperty(self):
        return self.__BeanProperty

    @BeanProperty.setter
    def BeanProperty(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_beans_BeanProperty__BeanProperty", None)
        self.__BeanProperty = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bean"):
                opp_val = getattr(old_value, "bean", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bean"):
                opp_val = getattr(value, "bean", None)
                if opp_val is None:
                    setattr(value, "bean", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class beans_Bean(NamedElement):

    pass
class beans_BeanLibrary(NamedElement):

    def __init__(self, packageName: str, beanLibrary: set["beans_Bean"] = None, BeanLibrary: "beans_Bean" = None):
        self.packageName = packageName
        self.beanLibrary = beanLibrary if beanLibrary is not None else set()
        self.BeanLibrary = BeanLibrary
        
    @property
    def packageName(self) -> str:
        return self.__packageName

    @packageName.setter
    def packageName(self, packageName: str):
        self.__packageName = packageName

    @property
    def beanLibrary(self):
        return self.__beanLibrary

    @beanLibrary.setter
    def beanLibrary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_beans_BeanLibrary__beanLibrary", None)
        self.__beanLibrary = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Bean"):
                    opp_val = getattr(item, "Bean", None)
                    
                    if opp_val == self:
                        setattr(item, "Bean", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Bean"):
                    opp_val = getattr(item, "Bean", None)
                    
                    setattr(item, "Bean", self)
                    

    @property
    def BeanLibrary(self):
        return self.__BeanLibrary

    @BeanLibrary.setter
    def BeanLibrary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_beans_BeanLibrary__BeanLibrary", None)
        self.__BeanLibrary = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "beans"):
                opp_val = getattr(old_value, "beans", None)
                if opp_val == self:
                    setattr(old_value, "beans", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "beans"):
                opp_val = getattr(value, "beans", None)
                setattr(value, "beans", self)
