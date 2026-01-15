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

class StructuredClassifier:

    pass
class uml_EncapsulatedClassifier(StructuredClassifier):

    pass
class uml_EModelElement(ABC):

    pass
class EModelElement:

    pass
class uml_Element(EModelElement):

    pass
class Classifier:

    pass
class uml_StructuredClassifier(Classifier):

    pass
class TypedElement:

    pass
class Relationship:

    pass
class uml_DirectedRelationship(Relationship):

    pass
class uml_BehavioredClassifier(Classifier):

    pass
class BehavioralFeature:

    pass
class Package:

    pass
class uml_Model(Package):

    pass
class MultiplicityElement:

    pass
class BehavioredClassifier:

    pass
class EncapsulatedClassifier:

    pass
class uml_Class(EncapsulatedClassifier, BehavioredClassifier):

    pass
class Class:

    pass
class uml_Behavior(Class):

    pass
class Feature:

    pass
class uml_StructuralFeature(Feature, TypedElement, MultiplicityElement):

    pass
class Type:

    pass
class Namespace:

    pass
class uml_BehavioralFeature(Feature, Namespace):

    pass
class TemplateableElement:

    pass
class DeploymentTarget:

    pass
class ConnectableElement:

    pass
class uml_Parameter(ConnectableElement, MultiplicityElement):

    pass
class StructuralFeature:

    pass
class uml_Property(DeploymentTarget, StructuralFeature, ConnectableElement):

    pass
class DirectedRelationship:

    pass
class uml_Generalization(DirectedRelationship):

    pass
class PackageableElement:

    pass
class uml_Type(PackageableElement):

    pass
class uml_Package(PackageableElement, TemplateableElement, Namespace):

    pass
class uml_Dependency(PackageableElement, DirectedRelationship):

    pass
class ParameterableElement:

    pass
class uml_Operation(TemplateableElement, BehavioralFeature, ParameterableElement):

    pass
class uml_ConnectableElement(TypedElement, ParameterableElement):

    pass
class NamedElement:

    pass
class uml_RedefinableElement(NamedElement):

    pass
class uml_DeploymentTarget(NamedElement):

    pass
class uml_TypedElement(NamedElement):

    pass
class uml_Namespace(NamedElement):

    pass
class uml_PackageableElement(NamedElement, ParameterableElement):

    pass
class Element:

    pass
class uml_MultiplicityElement(Element):

    pass
class uml_Relationship(Element):

    pass
class uml_ParameterableElement(Element):

    pass
class uml_TemplateableElement(Element):

    pass
class uml_NamedElement(Element):

    def __init__(self, name: str, visibility: str, uml_NamedElement: "uml_Dependency" = None):
        self.name = name
        self.visibility = visibility
        self.uml_NamedElement = uml_NamedElement
        
    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def uml_NamedElement(self):
        return self.__uml_NamedElement

    @uml_NamedElement.setter
    def uml_NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_NamedElement__uml_NamedElement", None)
        self.__uml_NamedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Dependency"):
                opp_val = getattr(old_value, "uml_Dependency", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Dependency"):
                opp_val = getattr(value, "uml_Dependency", None)
                if opp_val is None:
                    setattr(value, "uml_Dependency", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class RedefinableElement:

    pass
class uml_Classifier(TemplateableElement, Type, Namespace, RedefinableElement):

    def __init__(self, isAbstract: str, Classifier: "uml_Generalization" = None, specific: set["uml_Generalization"] = None, uml_Classifier: "uml_Generalization" = None, uml_Classifier6: "uml_Class" = None):
        self.isAbstract = isAbstract
        self.Classifier = Classifier
        self.specific = specific if specific is not None else set()
        self.uml_Classifier = uml_Classifier
        self.uml_Classifier6 = uml_Classifier6
        
    @property
    def isAbstract(self) -> str:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: str):
        self.__isAbstract = isAbstract

    @property
    def uml_Classifier(self):
        return self.__uml_Classifier

    @uml_Classifier.setter
    def uml_Classifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Classifier__uml_Classifier", None)
        self.__uml_Classifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Generalization"):
                opp_val = getattr(old_value, "uml_Generalization", None)
                if opp_val == self:
                    setattr(old_value, "uml_Generalization", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Generalization"):
                opp_val = getattr(value, "uml_Generalization", None)
                setattr(value, "uml_Generalization", self)

    @property
    def Classifier(self):
        return self.__Classifier

    @Classifier.setter
    def Classifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Classifier__Classifier", None)
        self.__Classifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "generalization"):
                opp_val = getattr(old_value, "generalization", None)
                if opp_val == self:
                    setattr(old_value, "generalization", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "generalization"):
                opp_val = getattr(value, "generalization", None)
                setattr(value, "generalization", self)

    @property
    def uml_Classifier6(self):
        return self.__uml_Classifier6

    @uml_Classifier6.setter
    def uml_Classifier6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Classifier__uml_Classifier6", None)
        self.__uml_Classifier6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uml_Class5"):
                opp_val = getattr(old_value, "uml_Class5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uml_Class5"):
                opp_val = getattr(value, "uml_Class5", None)
                if opp_val is None:
                    setattr(value, "uml_Class5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def specific(self):
        return self.__specific

    @specific.setter
    def specific(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uml_Classifier__specific", None)
        self.__specific = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Generalization"):
                    opp_val = getattr(item, "Generalization", None)
                    
                    if opp_val == self:
                        setattr(item, "Generalization", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Generalization"):
                    opp_val = getattr(item, "Generalization", None)
                    
                    setattr(item, "Generalization", self)
                    

class uml_Feature(RedefinableElement):

    pass