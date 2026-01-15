from datetime import datetime, date, time
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

class UML2_Property:

    def __init__(self, aggregation: str, UML2_Property: "UML2_Association" = None):
        self.aggregation = aggregation
        self.UML2_Property = UML2_Property
        
    @property
    def aggregation(self) -> str:
        return self.__aggregation

    @aggregation.setter
    def aggregation(self, aggregation: str):
        self.__aggregation = aggregation

    @property
    def UML2_Property(self):
        return self.__UML2_Property

    @UML2_Property.setter
    def UML2_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Property__UML2_Property", None)
        self.__UML2_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Association"):
                opp_val = getattr(old_value, "UML2_Association", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Association"):
                opp_val = getattr(value, "UML2_Association", None)
                if opp_val is None:
                    setattr(value, "UML2_Association", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UML2_Association:

    pass
class Property:

    pass
class UML2_ExtensionEnd(Property):

    pass
class UML2_Port(Property):

    pass
class Association:

    pass
class UML2_Extension(Association):

    pass
class UML2_AssociationClass(Association):

    pass
class UML2_CommunicationPath(Association):

    pass