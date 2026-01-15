from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class StructuredClassifier:

    pass
class UMLMM_EncapsulatedClassifier(StructuredClassifier):

    pass
class MultiplicityElement:

    pass
class TypedElement:

    pass
class UMLMM_EModelElement(ABC):

    pass
class EModelElement:

    pass
class UMLMM_Element(EModelElement):

    pass
class BehavioralFeature:

    pass
class Element:

    pass
class UMLMM_MultiplicityElement(Element):

    pass
class UMLMM_ParameterableElement(Element):

    pass
class UMLMM_NamedElement(Element):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class ParameterableElement:

    pass
class UMLMM_ConnectableElement(TypedElement, ParameterableElement):

    pass
class NamedElement:

    pass
class UMLMM_DeploymentTarget(NamedElement):

    pass
class UMLMM_TypedElement(NamedElement):

    pass
class UMLMM_Namespace(NamedElement):

    pass
class Realization:

    pass
class UMLMM_InterfaceRealization(Realization):

    pass
class Type:

    pass
class RedefinableElement:

    pass
class DeploymentTarget:

    pass
class ConnectableElement:

    pass
class StructuralFeature:

    pass
class UMLMM_Property(StructuralFeature, ConnectableElement, DeploymentTarget):

    pass
class UMLMM_Relationship(Element):

    pass
class Relationship:

    pass
class UMLMM_DirectedRelationship(Relationship):

    pass
class Dependency:

    pass
class UMLMM_Abstraction(Dependency):

    pass
class Abstraction:

    pass
class UMLMM_Realization(Abstraction):

    pass
class UMLMM_Feature(RedefinableElement):

    pass
class Feature:

    pass
class UMLMM_StructuralFeature(TypedElement, Feature, MultiplicityElement):

    pass
class UMLMM_RedefinableElement(NamedElement):

    pass
class UMLMM_TemplateableElement(Element):

    pass
class UMLMM_PackageableElement(NamedElement, ParameterableElement):

    pass
class TemplateableElement:

    pass
class PackageableElement:

    pass
class UMLMM_Type(PackageableElement):

    pass
class Namespace:

    pass
class UMLMM_BehavioralFeature(Namespace, Feature):

    pass
class UMLMM_Package(Namespace, TemplateableElement, PackageableElement):

    pass
class UMLMM_Classifier(Type, Namespace, TemplateableElement, RedefinableElement):

    def __init__(self, isAbstract: str, UMLMM_Classifier: "UMLMM_Generalization" = None, UMLMM_Classifier5: set["UMLMM_Generalization"] = None):
        self.isAbstract = isAbstract
        self.UMLMM_Classifier = UMLMM_Classifier
        self.UMLMM_Classifier5 = UMLMM_Classifier5 if UMLMM_Classifier5 is not None else set()
        
    @property
    def isAbstract(self) -> str:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: str):
        self.__isAbstract = isAbstract

    @property
    def UMLMM_Classifier(self):
        return self.__UMLMM_Classifier

    @UMLMM_Classifier.setter
    def UMLMM_Classifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLMM_Classifier__UMLMM_Classifier", None)
        self.__UMLMM_Classifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UMLMM_Generalization"):
                opp_val = getattr(old_value, "UMLMM_Generalization", None)
                if opp_val == self:
                    setattr(old_value, "UMLMM_Generalization", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UMLMM_Generalization"):
                opp_val = getattr(value, "UMLMM_Generalization", None)
                setattr(value, "UMLMM_Generalization", self)

    @property
    def UMLMM_Classifier5(self):
        return self.__UMLMM_Classifier5

    @UMLMM_Classifier5.setter
    def UMLMM_Classifier5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLMM_Classifier__UMLMM_Classifier5", None)
        self.__UMLMM_Classifier5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UMLMM_Generalization6"):
                    opp_val = getattr(item, "UMLMM_Generalization6", None)
                    
                    if opp_val == self:
                        setattr(item, "UMLMM_Generalization6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UMLMM_Generalization6"):
                    opp_val = getattr(item, "UMLMM_Generalization6", None)
                    
                    setattr(item, "UMLMM_Generalization6", self)
                    

class DirectedRelationship:

    pass
class UMLMM_Dependency(DirectedRelationship, PackageableElement):

    pass
class UMLMM_Generalization(DirectedRelationship):

    pass
class UMLMM_Operation(TemplateableElement, ParameterableElement, BehavioralFeature):

    pass
class BehavioredClassifier:

    pass
class EncapsulatedClassifier:

    pass
class UMLMM_Class(EncapsulatedClassifier, BehavioredClassifier):

    pass
class Package:

    pass
class UMLMM_Model(Package):

    pass
class Classifier:

    pass
class UMLMM_StructuredClassifier(Classifier):

    pass
class UMLMM_BehavioredClassifier(Classifier):

    pass
class UMLMM_Interface(Classifier):

    pass