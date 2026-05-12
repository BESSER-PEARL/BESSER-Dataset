from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class AggregationKind(Enum):
    ak_none = "ak_none"
    ak_aggregate = "ak_aggregate"
    ak_composite = "ak_composite"
class ScopeKind(Enum):
    sk_instance = "sk_instance"
    sk_classifier = "sk_classifier"
class OrderingKind(Enum):
    ok_unordered = "ok_unordered"
    ok_ordered = "ok_ordered"
class VisibilityKind(Enum):
    vk_public = "vk_public"
    vk_protected = "vk_protected"
    vk_private = "vk_private"
    vk_package = "vk_package"
class ChangeableKind(Enum):
    ck_changeable = "ck_changeable"
    ck_frozen = "ck_frozen"
    ck_addOnly = "ck_addOnly"


############################################
# Definition of Classes
############################################

class Data_Types_MultiplicityRange:

    def __init__(self, lower: str, upper: str, range: "Multiplicity_" = None):
        self.lower = lower
        self.upper = upper
        self.range = range
        
        pass
    @property
    def upper(self):
        return self.__upper

    @upper.setter
    def upper(self, upper: str):
        self.__upper = upper


    @property
    def lower(self):
        return self.__lower

    @lower.setter
    def lower(self, lower: str):
        self.__lower = lower


    @property
    def range(self):
        return self.__range

    @range.setter
    def range(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Data_Types_MultiplicityRange__range", None)
        self.__range = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Multiplicity88"):
                opp_val = getattr(old_value, "Multiplicity88", None)
                if opp_val == self:
                    setattr(old_value, "Multiplicity88", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Multiplicity88"):
                opp_val = getattr(value, "Multiplicity88", None)
                setattr(value, "Multiplicity88", self)

class MultiplicityRange:

    pass
class Data_Types_Multiplicity_:

    pass
class Data_Types_Expression:

    def __init__(self, language: str, body: str):
        self.language = language
        self.body = body
        
        pass
    @property
    def body(self):
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body


    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language


class Expression:

    pass
class Data_Types_BooleanExpression(Expression):

    pass
class StructuralFeature:

    pass
class Core_Attribute(StructuralFeature):

    pass
class Multiplicity_:

    pass
class Generalization_:

    pass
class Feature:

    pass
class Core_StructuralFeature(Feature):

    def __init__(self, targetScope: str, ordering: str, changeability: str, Core_StructuralFeature: "Classifier" = None, Core_StructuralFeature62: "Multiplicity_" = None, Feature: "Core_Classifier" = None):
        self.targetScope = targetScope
        self.ordering = ordering
        self.changeability = changeability
        self.Core_StructuralFeature = Core_StructuralFeature
        self.Core_StructuralFeature62 = Core_StructuralFeature62
        
        pass
    @property
    def changeability(self):
        return self.__changeability

    @changeability.setter
    def changeability(self, changeability: str):
        self.__changeability = changeability


    @property
    def targetScope(self):
        return self.__targetScope

    @targetScope.setter
    def targetScope(self, targetScope: str):
        self.__targetScope = targetScope


    @property
    def ordering(self):
        return self.__ordering

    @ordering.setter
    def ordering(self, ordering: str):
        self.__ordering = ordering


    @property
    def Core_StructuralFeature(self):
        return self.__Core_StructuralFeature

    @Core_StructuralFeature.setter
    def Core_StructuralFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_StructuralFeature__Core_StructuralFeature", None)
        self.__Core_StructuralFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Classifier60"):
                opp_val = getattr(old_value, "Classifier60", None)
                if opp_val == self:
                    setattr(old_value, "Classifier60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Classifier60"):
                opp_val = getattr(value, "Classifier60", None)
                setattr(value, "Classifier60", self)

    @property
    def Core_StructuralFeature62(self):
        return self.__Core_StructuralFeature62

    @Core_StructuralFeature62.setter
    def Core_StructuralFeature62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_StructuralFeature__Core_StructuralFeature62", None)
        self.__Core_StructuralFeature62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Multiplicity"):
                opp_val = getattr(old_value, "Multiplicity", None)
                if opp_val == self:
                    setattr(old_value, "Multiplicity", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Multiplicity"):
                opp_val = getattr(value, "Multiplicity", None)
                setattr(value, "Multiplicity", self)

class GeneralizableElement:

    pass
class BooleanExpression:

    pass
class UseCase:

    pass
class Namespace:

    pass
class Core_Classifier(Namespace, GeneralizableElement):

    pass
class Element:

    pass
class Core_ModelElement(Element):

    def __init__(self, name: str, visibility: str, isSpecification: str, ownedElement: "Namespace" = None):
        self.name = name
        self.visibility = visibility
        self.isSpecification = isSpecification
        self.ownedElement = ownedElement
        
        pass
    @property
    def visibility(self):
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility


    @property
    def isSpecification(self):
        return self.__isSpecification

    @isSpecification.setter
    def isSpecification(self, isSpecification: str):
        self.__isSpecification = isSpecification


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def ownedElement(self):
        return self.__ownedElement

    @ownedElement.setter
    def ownedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_ModelElement__ownedElement", None)
        self.__ownedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Namespace"):
                opp_val = getattr(old_value, "Namespace", None)
                if opp_val == self:
                    setattr(old_value, "Namespace", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Namespace"):
                opp_val = getattr(value, "Namespace", None)
                setattr(value, "Namespace", self)

class Core_Element(ABC):

    pass
class AssociationEnd:

    pass
class ExtensionPoint:

    pass
class Extend:

    pass
class Include:

    pass
class NodeInstance:

    pass
class Relationship:

    pass
class Core_Generalization_(Relationship):

    def __init__(self, discriminator: str, Core_Generalization: "GeneralizableElement" = None, powertypeRange: "Classifier" = None, generalization: "GeneralizableElement" = None):
        self.discriminator = discriminator
        self.Core_Generalization = Core_Generalization
        self.powertypeRange = powertypeRange
        self.generalization = generalization
        
        pass
    @property
    def discriminator(self):
        return self.__discriminator

    @discriminator.setter
    def discriminator(self, discriminator: str):
        self.__discriminator = discriminator


    @property
    def Core_Generalization(self):
        return self.__Core_Generalization

    @Core_Generalization.setter
    def Core_Generalization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_Generalization___Core_Generalization", None)
        self.__Core_Generalization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GeneralizableElement"):
                opp_val = getattr(old_value, "GeneralizableElement", None)
                if opp_val == self:
                    setattr(old_value, "GeneralizableElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GeneralizableElement"):
                opp_val = getattr(value, "GeneralizableElement", None)
                setattr(value, "GeneralizableElement", self)

    @property
    def powertypeRange(self):
        return self.__powertypeRange

    @powertypeRange.setter
    def powertypeRange(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_Generalization___powertypeRange", None)
        self.__powertypeRange = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Classifier83"):
                opp_val = getattr(old_value, "Classifier83", None)
                if opp_val == self:
                    setattr(old_value, "Classifier83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Classifier83"):
                opp_val = getattr(value, "Classifier83", None)
                setattr(value, "Classifier83", self)

    @property
    def generalization(self):
        return self.__generalization

    @generalization.setter
    def generalization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_Generalization___generalization", None)
        self.__generalization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GeneralizableElement85"):
                opp_val = getattr(old_value, "GeneralizableElement85", None)
                if opp_val == self:
                    setattr(old_value, "GeneralizableElement85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GeneralizableElement85"):
                opp_val = getattr(value, "GeneralizableElement85", None)
                setattr(value, "GeneralizableElement85", self)

class Use_Cases_Include(Relationship):

    pass
class Core_Association(Relationship, GeneralizableElement):

    pass
class Use_Cases_Extend(Relationship):

    pass
class Association:

    pass
class Attribute:

    pass
class ModelElement:

    pass
class Core_Relationship(ModelElement):

    pass
class Core_Namespace(ModelElement):

    pass
class Common_Behavior_LinkEnd(ModelElement):

    pass
class Core_Feature(ModelElement):

    def __init__(self, ownerScope: str, feature: "Classifier" = None, ModelElement: "Core_Namespace" = None):
        self.ownerScope = ownerScope
        self.feature = feature
        
        pass
    @property
    def ownerScope(self):
        return self.__ownerScope

    @ownerScope.setter
    def ownerScope(self, ownerScope: str):
        self.__ownerScope = ownerScope


    @property
    def feature(self):
        return self.__feature

    @feature.setter
    def feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_Feature__feature", None)
        self.__feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Classifier58"):
                opp_val = getattr(old_value, "Classifier58", None)
                if opp_val == self:
                    setattr(old_value, "Classifier58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Classifier58"):
                opp_val = getattr(value, "Classifier58", None)
                setattr(value, "Classifier58", self)

class Core_GeneralizableElement(ModelElement):

    def __init__(self, isRoot: str, isLeaf: str, isAbstract: str, child: set["Generalization_"] = None, ModelElement: "Core_Namespace" = None):
        self.isRoot = isRoot
        self.isLeaf = isLeaf
        self.isAbstract = isAbstract
        self.child = child if child is not None else set()
        
        pass
    @property
    def isAbstract(self):
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: str):
        self.__isAbstract = isAbstract


    @property
    def isRoot(self):
        return self.__isRoot

    @isRoot.setter
    def isRoot(self, isRoot: str):
        self.__isRoot = isRoot


    @property
    def isLeaf(self):
        return self.__isLeaf

    @isLeaf.setter
    def isLeaf(self, isLeaf: str):
        self.__isLeaf = isLeaf


    @property
    def child(self):
        return self.__child

    @child.setter
    def child(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_GeneralizableElement__child", None)
        self.__child = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Generalization_"):
                    opp_val = getattr(item, "Generalization_", None)
                    
                    if opp_val == self:
                        setattr(item, "Generalization_", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Generalization_"):
                    opp_val = getattr(item, "Generalization_", None)
                    
                    setattr(item, "Generalization_", self)
                    

class Common_Behavior_Link(ModelElement):

    pass
class Core_AssociationEnd(ModelElement):

    def __init__(self, changeability: str, isNavigable: str, ordering: str, aggregation: str, targetScope: str, Core_AssociationEnd74: "Multiplicity_" = None, connection64: "Association" = None, Core_AssociationEnd: set["Classifier"] = None, Core_AssociationEnd69: "Classifier" = None, associationEnd: set["Attribute"] = None, ModelElement: "Core_Namespace" = None):
        self.changeability = changeability
        self.isNavigable = isNavigable
        self.ordering = ordering
        self.aggregation = aggregation
        self.targetScope = targetScope
        self.Core_AssociationEnd74 = Core_AssociationEnd74
        self.connection64 = connection64
        self.Core_AssociationEnd = Core_AssociationEnd if Core_AssociationEnd is not None else set()
        self.Core_AssociationEnd69 = Core_AssociationEnd69
        self.associationEnd = associationEnd if associationEnd is not None else set()
        
        pass
    @property
    def targetScope(self):
        return self.__targetScope

    @targetScope.setter
    def targetScope(self, targetScope: str):
        self.__targetScope = targetScope


    @property
    def aggregation(self):
        return self.__aggregation

    @aggregation.setter
    def aggregation(self, aggregation: str):
        self.__aggregation = aggregation


    @property
    def isNavigable(self):
        return self.__isNavigable

    @isNavigable.setter
    def isNavigable(self, isNavigable: str):
        self.__isNavigable = isNavigable


    @property
    def changeability(self):
        return self.__changeability

    @changeability.setter
    def changeability(self, changeability: str):
        self.__changeability = changeability


    @property
    def ordering(self):
        return self.__ordering

    @ordering.setter
    def ordering(self, ordering: str):
        self.__ordering = ordering


    @property
    def Core_AssociationEnd74(self):
        return self.__Core_AssociationEnd74

    @Core_AssociationEnd74.setter
    def Core_AssociationEnd74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_AssociationEnd__Core_AssociationEnd74", None)
        self.__Core_AssociationEnd74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Multiplicity75"):
                opp_val = getattr(old_value, "Multiplicity75", None)
                if opp_val == self:
                    setattr(old_value, "Multiplicity75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Multiplicity75"):
                opp_val = getattr(value, "Multiplicity75", None)
                setattr(value, "Multiplicity75", self)

    @property
    def Core_AssociationEnd(self):
        return self.__Core_AssociationEnd

    @Core_AssociationEnd.setter
    def Core_AssociationEnd(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_AssociationEnd__Core_AssociationEnd", None)
        self.__Core_AssociationEnd = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Classifier67"):
                    opp_val = getattr(item, "Classifier67", None)
                    
                    if opp_val == self:
                        setattr(item, "Classifier67", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Classifier67"):
                    opp_val = getattr(item, "Classifier67", None)
                    
                    setattr(item, "Classifier67", self)
                    

    @property
    def associationEnd(self):
        return self.__associationEnd

    @associationEnd.setter
    def associationEnd(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_AssociationEnd__associationEnd", None)
        self.__associationEnd = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Attribute72"):
                    opp_val = getattr(item, "Attribute72", None)
                    
                    if opp_val == self:
                        setattr(item, "Attribute72", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Attribute72"):
                    opp_val = getattr(item, "Attribute72", None)
                    
                    setattr(item, "Attribute72", self)
                    

    @property
    def Core_AssociationEnd69(self):
        return self.__Core_AssociationEnd69

    @Core_AssociationEnd69.setter
    def Core_AssociationEnd69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_AssociationEnd__Core_AssociationEnd69", None)
        self.__Core_AssociationEnd69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Classifier70"):
                opp_val = getattr(old_value, "Classifier70", None)
                if opp_val == self:
                    setattr(old_value, "Classifier70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Classifier70"):
                opp_val = getattr(value, "Classifier70", None)
                setattr(value, "Classifier70", self)

    @property
    def connection64(self):
        return self.__connection64

    @connection64.setter
    def connection64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Core_AssociationEnd__connection64", None)
        self.__connection64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Association65"):
                opp_val = getattr(old_value, "Association65", None)
                if opp_val == self:
                    setattr(old_value, "Association65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Association65"):
                opp_val = getattr(value, "Association65", None)
                setattr(value, "Association65", self)

class Use_Cases_ExtensionPoint(ModelElement):

    def __init__(self, location: str, extensionPoint: "UseCase" = None, ModelElement: "Core_Namespace" = None):
        self.location = location
        self.extensionPoint = extensionPoint
        
        pass
    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location


    @property
    def extensionPoint(self):
        return self.__extensionPoint

    @extensionPoint.setter
    def extensionPoint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Use_Cases_ExtensionPoint__extensionPoint", None)
        self.__extensionPoint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UseCase50"):
                opp_val = getattr(old_value, "UseCase50", None)
                if opp_val == self:
                    setattr(old_value, "UseCase50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UseCase50"):
                opp_val = getattr(value, "UseCase50", None)
                setattr(value, "UseCase50", self)

class Common_Behavior_AttributeLink(ModelElement):

    pass
class Common_Behavior_Instance(ModelElement):

    pass
class Link:

    pass
class AttributeLink:

    pass
class ComponentInstance:

    pass
class Classifier:

    pass
class Use_Cases_Actor(Classifier):

    pass
class Use_Cases_UseCase(Classifier):

    pass
class LinkEnd:

    pass
class Instance:

    pass
class Use_Cases_UseCaseInstance(Instance):

    pass
class Common_Behavior_ComponentInstance(Instance):

    pass
class Common_Behavior_NodeInstance(Instance):

    pass