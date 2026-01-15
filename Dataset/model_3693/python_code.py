from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class AggregationKind(Enum):
    composite = "composite"
    none = "none"
    shared = "shared"


############################################
# Definition of Classes
############################################

class UML2WithID_Element(ABC):

    def __init__(self, ID: str):
        self.ID = ID
        
    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

class Property:

    pass
class Element:

    pass
class UML2WithID_Port(Property, Element):

    pass
class UML2WithID_Association(Element):

    pass
class UML2WithID_Property(Element):

    def __init__(self, aggregation: str, UML2WithID_Property: "UML2WithID_Association" = None):
        self.aggregation = aggregation
        self.UML2WithID_Property = UML2WithID_Property
        
    @property
    def aggregation(self) -> str:
        return self.__aggregation

    @aggregation.setter
    def aggregation(self, aggregation: str):
        self.__aggregation = aggregation

    @property
    def UML2WithID_Property(self):
        return self.__UML2WithID_Property

    @UML2WithID_Property.setter
    def UML2WithID_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Property__UML2WithID_Property", None)
        self.__UML2WithID_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_Association"):
                opp_val = getattr(old_value, "UML2WithID_Association", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_Association"):
                opp_val = getattr(value, "UML2WithID_Association", None)
                if opp_val is None:
                    setattr(value, "UML2WithID_Association", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UML2WithID_ExtensionEnd(Property, Element):

    pass
class Association:

    pass
class UML2WithID_AssociationClass(Association, Element):

    pass
class UML2WithID_CommunicationPath(Association, Element):

    pass
class UML2WithID_Extension(Association, Element):

    pass