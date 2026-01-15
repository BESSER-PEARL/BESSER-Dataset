from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class visType(Enum):
    public = "public"
    private = "private"


############################################
# Definition of Classes
############################################

class umlsimp_Model:

    pass
class TypedElement:

    pass
class umlsimp_Parameter(TypedElement):

    pass
class umlsimp_Operation(TypedElement):

    pass
class umlsimp_Property(TypedElement):

    def __init__(self, visibility: str, Property: "umlsimp_Class" = None, properties: "umlsimp_Class" = None):
        self.visibility = visibility
        self.Property = Property
        self.properties = properties
        
    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def properties(self):
        return self.__properties

    @properties.setter
    def properties(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlsimp_Property__properties", None)
        self.__properties = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Class6"):
                opp_val = getattr(old_value, "Class6", None)
                if opp_val == self:
                    setattr(old_value, "Class6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Class6"):
                opp_val = getattr(value, "Class6", None)
                setattr(value, "Class6", self)

    @property
    def Property(self):
        return self.__Property

    @Property.setter
    def Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlsimp_Property__Property", None)
        self.__Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "class"):
                opp_val = getattr(old_value, "class", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "class"):
                opp_val = getattr(value, "class", None)
                if opp_val is None:
                    setattr(value, "class", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ModelElement:

    pass
class umlsimp_TypedElement(ModelElement):

    pass
class umlsimp_Class(ModelElement):

    pass
class umlsimp_DataType(ModelElement):

    pass
class umlsimp_ModelElement(ABC):

    def __init__(self, name: str, umlsimp_ModelElement: "umlsimp_Model" = None):
        self.name = name
        self.umlsimp_ModelElement = umlsimp_ModelElement
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def umlsimp_ModelElement(self):
        return self.__umlsimp_ModelElement

    @umlsimp_ModelElement.setter
    def umlsimp_ModelElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_umlsimp_ModelElement__umlsimp_ModelElement", None)
        self.__umlsimp_ModelElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "umlsimp_Model"):
                opp_val = getattr(old_value, "umlsimp_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "umlsimp_Model"):
                opp_val = getattr(value, "umlsimp_Model", None)
                if opp_val is None:
                    setattr(value, "umlsimp_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
