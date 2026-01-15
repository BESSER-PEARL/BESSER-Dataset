from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class SimpleUML_NamedElement(ABC):

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
class SimpleUML_Property(NamedElement):

    def __init__(self, primitiveType: str, isContainment: bool, SimpleUML_Property: "SimpleUML_Class" = None, SimpleUML_Property5: "SimpleUML_Class" = None):
        self.primitiveType = primitiveType
        self.isContainment = isContainment
        self.SimpleUML_Property = SimpleUML_Property
        self.SimpleUML_Property5 = SimpleUML_Property5
        
    @property
    def primitiveType(self) -> str:
        return self.__primitiveType

    @primitiveType.setter
    def primitiveType(self, primitiveType: str):
        self.__primitiveType = primitiveType

    @property
    def isContainment(self) -> bool:
        return self.__isContainment

    @isContainment.setter
    def isContainment(self, isContainment: bool):
        self.__isContainment = isContainment

    @property
    def SimpleUML_Property5(self):
        return self.__SimpleUML_Property5

    @SimpleUML_Property5.setter
    def SimpleUML_Property5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimpleUML_Property__SimpleUML_Property5", None)
        self.__SimpleUML_Property5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimpleUML_Class6"):
                opp_val = getattr(old_value, "SimpleUML_Class6", None)
                if opp_val == self:
                    setattr(old_value, "SimpleUML_Class6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimpleUML_Class6"):
                opp_val = getattr(value, "SimpleUML_Class6", None)
                setattr(value, "SimpleUML_Class6", self)

    @property
    def SimpleUML_Property(self):
        return self.__SimpleUML_Property

    @SimpleUML_Property.setter
    def SimpleUML_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimpleUML_Property__SimpleUML_Property", None)
        self.__SimpleUML_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimpleUML_Class"):
                opp_val = getattr(old_value, "SimpleUML_Class", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimpleUML_Class"):
                opp_val = getattr(value, "SimpleUML_Class", None)
                if opp_val is None:
                    setattr(value, "SimpleUML_Class", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class SimpleUML_Package(NamedElement):

    pass
class SimpleUML_Class(NamedElement):

    pass