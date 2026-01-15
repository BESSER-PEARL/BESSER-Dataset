from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ScopeKind(Enum):
    instance = "instance"
    classifier = "classifier"
class AggregationKind(Enum):
    none = "none"
    shared = "shared"
    composite = "composite"


############################################
# Definition of Classes
############################################

class StructuralFeature:

    pass
class uml_15_to_20_associationEndToProperty_StructuralFeature(ABC):

    def __init__(self, isStatic: bool):
        self.isStatic = isStatic
        
    @property
    def isStatic(self) -> bool:
        return self.__isStatic

    @isStatic.setter
    def isStatic(self, isStatic: bool):
        self.__isStatic = isStatic

class uml_15_to_20_associationEndToProperty_Operation(StructuralFeature):

    pass
class uml_15_to_20_associationEndToProperty_Property(StructuralFeature):

    pass
class uml_15_to_20_associationEndToProperty_Association:

    pass
class uml_15_to_20_associationEndToProperty_Class:

    pass
class uml_15_to_20_associationEndToProperty_Model:

    pass