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

    def __init__(self, isComposite: bool, aggregation: str):
        self.isComposite = isComposite
        self.aggregation = aggregation
        
    @property
    def isComposite(self) -> bool:
        return self.__isComposite

    @isComposite.setter
    def isComposite(self, isComposite: bool):
        self.__isComposite = isComposite

    @property
    def aggregation(self) -> str:
        return self.__aggregation

    @aggregation.setter
    def aggregation(self, aggregation: str):
        self.__aggregation = aggregation

class Property:

    pass
class UML2_Port(Property):

    pass
class UML2_ExtensionEnd(Property):

    pass