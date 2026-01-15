from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class VisibilityKind(Enum):
    public = "public"
    private = "private"
    protected = "protected"
    package = "package"


############################################
# Definition of Classes
############################################

class OO_concept_Dependency:

    pass
class Class:

    pass
class OO_concept_Behavior(Class):

    pass
class Feature:

    pass
class OO_concept_StructuralFeature(Feature):

    pass
class OO_concept_BehavioralFeature(Feature):

    pass
class NamedElement:

    pass
class OO_concept_TypedElement(NamedElement):

    pass
class OO_concept_Type(NamedElement):

    pass
class PackageableElement:

    pass
class OO_concept_Package(NamedElement, PackageableElement):

    pass
class OO_concept_PackageableElement(ABC):

    pass
class OO_concept_Generalization:

    pass
class StructuralFeature:

    pass
class OO_concept_Feature(NamedElement):

    pass
class BehavioralFeature:

    pass
class TypedElement:

    pass
class OO_concept_Parameter(TypedElement):

    pass
class Package:

    pass
class OO_concept_Model(Package):

    pass
class OO_concept_NamedElement(ABC):

    def __init__(self, name: str, isAbstract: bool, visibility: str, OO_concept_NamedElement: "OO_concept_Dependency" = None, OO_concept_NamedElement14: "OO_concept_Dependency" = None):
        self.name = name
        self.isAbstract = isAbstract
        self.visibility = visibility
        self.OO_concept_NamedElement = OO_concept_NamedElement
        self.OO_concept_NamedElement14 = OO_concept_NamedElement14
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def isAbstract(self) -> bool:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: bool):
        self.__isAbstract = isAbstract

    @property
    def OO_concept_NamedElement(self):
        return self.__OO_concept_NamedElement

    @OO_concept_NamedElement.setter
    def OO_concept_NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OO_concept_NamedElement__OO_concept_NamedElement", None)
        self.__OO_concept_NamedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OO_concept_Dependency"):
                opp_val = getattr(old_value, "OO_concept_Dependency", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OO_concept_Dependency"):
                opp_val = getattr(value, "OO_concept_Dependency", None)
                if opp_val is None:
                    setattr(value, "OO_concept_Dependency", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def OO_concept_NamedElement14(self):
        return self.__OO_concept_NamedElement14

    @OO_concept_NamedElement14.setter
    def OO_concept_NamedElement14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OO_concept_NamedElement__OO_concept_NamedElement14", None)
        self.__OO_concept_NamedElement14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OO_concept_Dependency13"):
                opp_val = getattr(old_value, "OO_concept_Dependency13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OO_concept_Dependency13"):
                opp_val = getattr(value, "OO_concept_Dependency13", None)
                if opp_val is None:
                    setattr(value, "OO_concept_Dependency13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class OO_concept_Classifier(ABC):

    pass
class OO_concept_Property(TypedElement, StructuralFeature):

    pass
class OO_concept_Operation(TypedElement, BehavioralFeature):

    pass
class Type:

    pass
class Classifier:

    pass
class OO_concept_Class(Classifier, PackageableElement, Type):

    pass