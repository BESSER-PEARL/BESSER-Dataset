from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class AggregationKind(Enum):
    none = "none"
    aggregate = "aggregate"
    composite = "composite"
class ChangeableKind(Enum):
    changeable = "changeable"
    frozen = "frozen"
    addOnly = "addOnly"
class ParameterDirectionKind(Enum):
    in_ = "in_"
    inout = "inout"
    out = "out"
    return_ = "return_"
class ScopeKind(Enum):
    instance = "instance"
    classifier = "classifier"
class OrderingKind(Enum):
    unordered = "unordered"
    ordered = "ordered"
class VisibilityKind(Enum):
    public = "public"
    protected = "protected"
    private = "private"
    package = "package"
class PseudostateKind(Enum):
    choice = "choice"
    deepHistory = "deepHistory"
    fork = "fork"
    initial = "initial"
    join = "join"
    junction = "junction"
    shallowHistory = "shallowHistory"
class CallConcurrencyKind(Enum):
    sequential = "sequential"
    guarded = "guarded"
    concurrent = "concurrent"


############################################
# Definition of Classes
############################################

class Binding:

    pass
class TagDefinition:

    pass
class foundation_core_TemplateArgument:

    pass
class TypeExpression:

    pass
class DataType:

    pass
class foundation_core_Enumeration(DataType):

    pass
class foundation_core_ProgrammingLanguageDataType(DataType):

    pass
class foundation_core_Primitive(DataType):

    pass
class foundation_core_TemplateParameter:

    pass
class foundation_core_ElementResidence:

    def __init__(self, visibility: str, elementResidence: "ModelElement" = None, residentElement: "Component" = None):
        self.visibility = visibility
        self.elementResidence = elementResidence
        self.residentElement = residentElement
        
        pass
    @property
    def visibility(self):
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility


    @property
    def elementResidence(self):
        return self.__elementResidence

    @elementResidence.setter
    def elementResidence(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_ElementResidence__elementResidence", None)
        self.__elementResidence = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ModelElement102"):
                opp_val = getattr(old_value, "ModelElement102", None)
                if opp_val == self:
                    setattr(old_value, "ModelElement102", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ModelElement102"):
                opp_val = getattr(value, "ModelElement102", None)
                setattr(value, "ModelElement102", self)

    @property
    def residentElement(self):
        return self.__residentElement

    @residentElement.setter
    def residentElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_ElementResidence__residentElement", None)
        self.__residentElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Component104"):
                opp_val = getattr(old_value, "Component104", None)
                if opp_val == self:
                    setattr(old_value, "Component104", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Component104"):
                opp_val = getattr(value, "Component104", None)
                setattr(value, "Component104", self)

class Enumeration:

    pass
class EnumerationLiteral:

    pass
class Artifact:

    pass
class Node:

    pass
class TemplateArgument:

    pass
class MappingExpression:

    pass
class core_Association:

    pass
class core_Class:

    pass
class foundation_core_AssociationClass(core_Association, core_Class):

    pass
class Component:

    pass
class GeneralizableElement:

    pass
class foundation_core_Stereotype(GeneralizableElement):

    def __init__(self, icon: str, baseClass: str, owner115: set["TagDefinition"] = None, stereotype: set["ModelElement"] = None, constrainedStereotype: set["Constraint"] = None, GeneralizableElement79: "foundation_core_Generalization_" = None, GeneralizableElement: "foundation_core_Generalization_" = None):
        self.icon = icon
        self.baseClass = baseClass
        self.owner115 = owner115 if owner115 is not None else set()
        self.stereotype = stereotype if stereotype is not None else set()
        self.constrainedStereotype = constrainedStereotype if constrainedStereotype is not None else set()
        
        pass
    @property
    def icon(self):
        return self.__icon

    @icon.setter
    def icon(self, icon: str):
        self.__icon = icon


    @property
    def baseClass(self):
        return self.__baseClass

    @baseClass.setter
    def baseClass(self, baseClass: str):
        self.__baseClass = baseClass


    @property
    def constrainedStereotype(self):
        return self.__constrainedStereotype

    @constrainedStereotype.setter
    def constrainedStereotype(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_Stereotype__constrainedStereotype", None)
        self.__constrainedStereotype = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Constraint119"):
                    opp_val = getattr(item, "Constraint119", None)
                    
                    if opp_val == self:
                        setattr(item, "Constraint119", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Constraint119"):
                    opp_val = getattr(item, "Constraint119", None)
                    
                    setattr(item, "Constraint119", self)
                    

    @property
    def stereotype(self):
        return self.__stereotype

    @stereotype.setter
    def stereotype(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_Stereotype__stereotype", None)
        self.__stereotype = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ModelElement117"):
                    opp_val = getattr(item, "ModelElement117", None)
                    
                    if opp_val == self:
                        setattr(item, "ModelElement117", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ModelElement117"):
                    opp_val = getattr(item, "ModelElement117", None)
                    
                    setattr(item, "ModelElement117", self)
                    

    @property
    def owner115(self):
        return self.__owner115

    @owner115.setter
    def owner115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_Stereotype__owner115", None)
        self.__owner115 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TagDefinition"):
                    opp_val = getattr(item, "TagDefinition", None)
                    
                    if opp_val == self:
                        setattr(item, "TagDefinition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TagDefinition"):
                    opp_val = getattr(item, "TagDefinition", None)
                    
                    setattr(item, "TagDefinition", self)
                    

class Relationship:

    pass
class foundation_core_Flow(Relationship):

    pass
class foundation_core_Dependency(Relationship):

    pass
class foundation_core_Generalization_(Relationship):

    def __init__(self, discriminator: str, powertypeRange: "Classifier" = None, generalization: "GeneralizableElement" = None, specialization: "GeneralizableElement" = None):
        self.discriminator = discriminator
        self.powertypeRange = powertypeRange
        self.generalization = generalization
        self.specialization = specialization
        
        pass
    @property
    def discriminator(self):
        return self.__discriminator

    @discriminator.setter
    def discriminator(self, discriminator: str):
        self.__discriminator = discriminator


    @property
    def powertypeRange(self):
        return self.__powertypeRange

    @powertypeRange.setter
    def powertypeRange(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_Generalization___powertypeRange", None)
        self.__powertypeRange = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Classifier81"):
                opp_val = getattr(old_value, "Classifier81", None)
                if opp_val == self:
                    setattr(old_value, "Classifier81", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Classifier81"):
                opp_val = getattr(value, "Classifier81", None)
                setattr(value, "Classifier81", self)

    @property
    def generalization(self):
        return self.__generalization

    @generalization.setter
    def generalization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_Generalization___generalization", None)
        self.__generalization = value
        
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
    def specialization(self):
        return self.__specialization

    @specialization.setter
    def specialization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_Generalization___specialization", None)
        self.__specialization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GeneralizableElement79"):
                opp_val = getattr(old_value, "GeneralizableElement79", None)
                if opp_val == self:
                    setattr(old_value, "GeneralizableElement79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GeneralizableElement79"):
                opp_val = getattr(value, "GeneralizableElement79", None)
                setattr(value, "GeneralizableElement79", self)

class Operation:

    pass
class ProcedureExpression:

    pass
class CallEvent:

    pass
class CallAction:

    pass
class Method:

    pass
class BehavioralFeature:

    pass
class foundation_core_Method(BehavioralFeature):

    pass
class foundation_core_Operation(BehavioralFeature):

    def __init__(self, concurrency: str, isRoot: str, isLeaf: str, isAbstract: str, specification: str, specification64: set["Method"] = None, operation: set["CallAction"] = None, operation67: set["CallEvent"] = None, representedOperation: set["Collaboration"] = None, BehavioralFeature: "foundation_core_Parameter" = None):
        self.concurrency = concurrency
        self.isRoot = isRoot
        self.isLeaf = isLeaf
        self.isAbstract = isAbstract
        self.specification = specification
        self.specification64 = specification64 if specification64 is not None else set()
        self.operation = operation if operation is not None else set()
        self.operation67 = operation67 if operation67 is not None else set()
        self.representedOperation = representedOperation if representedOperation is not None else set()
        
        pass
    @property
    def concurrency(self):
        return self.__concurrency

    @concurrency.setter
    def concurrency(self, concurrency: str):
        self.__concurrency = concurrency


    @property
    def isLeaf(self):
        return self.__isLeaf

    @isLeaf.setter
    def isLeaf(self, isLeaf: str):
        self.__isLeaf = isLeaf


    @property
    def isRoot(self):
        return self.__isRoot

    @isRoot.setter
    def isRoot(self, isRoot: str):
        self.__isRoot = isRoot


    @property
    def specification(self):
        return self.__specification

    @specification.setter
    def specification(self, specification: str):
        self.__specification = specification


    @property
    def isAbstract(self):
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: str):
        self.__isAbstract = isAbstract


    @property
    def operation(self):
        return self.__operation

    @operation.setter
    def operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_Operation__operation", None)
        self.__operation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CallAction"):
                    opp_val = getattr(item, "CallAction", None)
                    
                    if opp_val == self:
                        setattr(item, "CallAction", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CallAction"):
                    opp_val = getattr(item, "CallAction", None)
                    
                    setattr(item, "CallAction", self)
                    

    @property
    def operation67(self):
        return self.__operation67

    @operation67.setter
    def operation67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_Operation__operation67", None)
        self.__operation67 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CallEvent"):
                    opp_val = getattr(item, "CallEvent", None)
                    
                    if opp_val == self:
                        setattr(item, "CallEvent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CallEvent"):
                    opp_val = getattr(item, "CallEvent", None)
                    
                    setattr(item, "CallEvent", self)
                    

    @property
    def specification64(self):
        return self.__specification64

    @specification64.setter
    def specification64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_Operation__specification64", None)
        self.__specification64 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Method"):
                    opp_val = getattr(item, "Method", None)
                    
                    if opp_val == self:
                        setattr(item, "Method", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Method"):
                    opp_val = getattr(item, "Method", None)
                    
                    setattr(item, "Method", self)
                    

    @property
    def representedOperation(self):
        return self.__representedOperation

    @representedOperation.setter
    def representedOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_Operation__representedOperation", None)
        self.__representedOperation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Collaboration69"):
                    opp_val = getattr(item, "Collaboration69", None)
                    
                    if opp_val == self:
                        setattr(item, "Collaboration69", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Collaboration69"):
                    opp_val = getattr(item, "Collaboration69", None)
                    
                    setattr(item, "Collaboration69", self)
                    

class Signal:

    pass
class AssociationEndRole:

    pass
class core_Relationship:

    pass
class BooleanExpression:

    pass
class Attribute:

    pass
class Association:

    pass
class AssociationEnd:

    pass
class Parameter:

    pass
class StructuralFeature:

    pass
class foundation_core_Attribute(StructuralFeature):

    pass
class Feature:

    pass
class foundation_core_BehavioralFeature(Feature):

    def __init__(self, isQuery: str, behavioralFeature: set["Parameter"] = None, context62: set["Signal"] = None, Feature: "foundation_core_Classifier" = None):
        self.isQuery = isQuery
        self.behavioralFeature = behavioralFeature if behavioralFeature is not None else set()
        self.context62 = context62 if context62 is not None else set()
        
        pass
    @property
    def isQuery(self):
        return self.__isQuery

    @isQuery.setter
    def isQuery(self, isQuery: str):
        self.__isQuery = isQuery


    @property
    def behavioralFeature(self):
        return self.__behavioralFeature

    @behavioralFeature.setter
    def behavioralFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_BehavioralFeature__behavioralFeature", None)
        self.__behavioralFeature = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Parameter60"):
                    opp_val = getattr(item, "Parameter60", None)
                    
                    if opp_val == self:
                        setattr(item, "Parameter60", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Parameter60"):
                    opp_val = getattr(item, "Parameter60", None)
                    
                    setattr(item, "Parameter60", self)
                    

    @property
    def context62(self):
        return self.__context62

    @context62.setter
    def context62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_BehavioralFeature__context62", None)
        self.__context62 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Signal"):
                    opp_val = getattr(item, "Signal", None)
                    
                    if opp_val == self:
                        setattr(item, "Signal", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Signal"):
                    opp_val = getattr(item, "Signal", None)
                    
                    setattr(item, "Signal", self)
                    

class core_Namespace:

    pass
class core_GeneralizableElement:

    pass
class foundation_core_Association(core_Relationship, core_GeneralizableElement):

    pass
class foundation_core_Classifier(core_GeneralizableElement, core_Namespace):

    pass
class Generalization_:

    pass
class foundation_core_StructuralFeature(Feature):

    def __init__(self, changeability: str, targetScope: str, ordering: str, foundation_core_StructuralFeature: "Multiplicity_" = None, typedFeature: "Classifier" = None, Feature: "foundation_core_Classifier" = None):
        self.changeability = changeability
        self.targetScope = targetScope
        self.ordering = ordering
        self.foundation_core_StructuralFeature = foundation_core_StructuralFeature
        self.typedFeature = typedFeature
        
        pass
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
    def changeability(self):
        return self.__changeability

    @changeability.setter
    def changeability(self, changeability: str):
        self.__changeability = changeability


    @property
    def foundation_core_StructuralFeature(self):
        return self.__foundation_core_StructuralFeature

    @foundation_core_StructuralFeature.setter
    def foundation_core_StructuralFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_StructuralFeature__foundation_core_StructuralFeature", None)
        self.__foundation_core_StructuralFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Multiplicity36"):
                opp_val = getattr(old_value, "Multiplicity36", None)
                if opp_val == self:
                    setattr(old_value, "Multiplicity36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Multiplicity36"):
                opp_val = getattr(value, "Multiplicity36", None)
                setattr(value, "Multiplicity36", self)

    @property
    def typedFeature(self):
        return self.__typedFeature

    @typedFeature.setter
    def typedFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_StructuralFeature__typedFeature", None)
        self.__typedFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Classifier38"):
                opp_val = getattr(old_value, "Classifier38", None)
                if opp_val == self:
                    setattr(old_value, "Classifier38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Classifier38"):
                opp_val = getattr(value, "Classifier38", None)
                setattr(value, "Classifier38", self)

class Classifier:

    pass
class foundation_core_DataType(Classifier):

    pass
class foundation_core_Artifact(Classifier):

    pass
class foundation_core_Node(Classifier):

    pass
class foundation_core_Component(Classifier):

    pass
class foundation_core_Interface(Classifier):

    pass
class foundation_core_Class(Classifier):

    def __init__(self, isActive: str, Classifier38: "foundation_core_StructuralFeature" = None, Classifier81: "foundation_core_Generalization_" = None, Classifier: "foundation_core_Feature" = None, Classifier46: "foundation_core_AssociationEnd" = None, Classifier74: "foundation_core_Parameter" = None, Classifier44: "foundation_core_AssociationEnd" = None):
        self.isActive = isActive
        
        pass
    @property
    def isActive(self):
        return self.__isActive

    @isActive.setter
    def isActive(self, isActive: str):
        self.__isActive = isActive


class Collaboration:

    pass
class CreateAction:

    pass
class Comment:

    pass
class Flow:

    pass
class PresentationElement:

    pass
class Constraint:

    pass
class Dependency:

    pass
class foundation_core_Binding(Dependency):

    pass
class foundation_core_Permission(Dependency):

    pass
class foundation_core_Usage(Dependency):

    pass
class foundation_core_Abstraction(Dependency):

    pass
class Namespace:

    pass
class Element:

    pass
class foundation_core_PresentationElement(Element):

    pass
class foundation_core_ModelElement(Element):

    def __init__(self, name: str, visibility: str, isSpecification: str, annotatedElement: set["Comment"] = None, resident: set["ElementResidence"] = None, template: set["TemplateParameter"] = None, extendedElement: set["Stereotype"] = None, modelElement: set["TaggedValue"] = None, referenceValue: set["TaggedValue"] = None, context: set["StateMachine"] = None, ownedElement: "Namespace" = None, client: set["Dependency"] = None, constrainedElement: set["Constraint"] = None, supplier: set["Dependency"] = None, subject: set["PresentationElement"] = None, target: set["Flow"] = None, source: set["Flow"] = None):
        self.name = name
        self.visibility = visibility
        self.isSpecification = isSpecification
        self.annotatedElement = annotatedElement if annotatedElement is not None else set()
        self.resident = resident if resident is not None else set()
        self.template = template if template is not None else set()
        self.extendedElement = extendedElement if extendedElement is not None else set()
        self.modelElement = modelElement if modelElement is not None else set()
        self.referenceValue = referenceValue if referenceValue is not None else set()
        self.context = context if context is not None else set()
        self.ownedElement = ownedElement
        self.client = client if client is not None else set()
        self.constrainedElement = constrainedElement if constrainedElement is not None else set()
        self.supplier = supplier if supplier is not None else set()
        self.subject = subject if subject is not None else set()
        self.target = target if target is not None else set()
        self.source = source if source is not None else set()
        
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
    def referenceValue(self):
        return self.__referenceValue

    @referenceValue.setter
    def referenceValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_ModelElement__referenceValue", None)
        self.__referenceValue = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TaggedValue17"):
                    opp_val = getattr(item, "TaggedValue17", None)
                    
                    if opp_val == self:
                        setattr(item, "TaggedValue17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TaggedValue17"):
                    opp_val = getattr(item, "TaggedValue17", None)
                    
                    setattr(item, "TaggedValue17", self)
                    

    @property
    def modelElement(self):
        return self.__modelElement

    @modelElement.setter
    def modelElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_ModelElement__modelElement", None)
        self.__modelElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TaggedValue"):
                    opp_val = getattr(item, "TaggedValue", None)
                    
                    if opp_val == self:
                        setattr(item, "TaggedValue", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TaggedValue"):
                    opp_val = getattr(item, "TaggedValue", None)
                    
                    setattr(item, "TaggedValue", self)
                    

    @property
    def template(self):
        return self.__template

    @template.setter
    def template(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_ModelElement__template", None)
        self.__template = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TemplateParameter"):
                    opp_val = getattr(item, "TemplateParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "TemplateParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TemplateParameter"):
                    opp_val = getattr(item, "TemplateParameter", None)
                    
                    setattr(item, "TemplateParameter", self)
                    

    @property
    def subject(self):
        return self.__subject

    @subject.setter
    def subject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_ModelElement__subject", None)
        self.__subject = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PresentationElement"):
                    opp_val = getattr(item, "PresentationElement", None)
                    
                    if opp_val == self:
                        setattr(item, "PresentationElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PresentationElement"):
                    opp_val = getattr(item, "PresentationElement", None)
                    
                    setattr(item, "PresentationElement", self)
                    

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_ModelElement__source", None)
        self.__source = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Flow10"):
                    opp_val = getattr(item, "Flow10", None)
                    
                    if opp_val == self:
                        setattr(item, "Flow10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Flow10"):
                    opp_val = getattr(item, "Flow10", None)
                    
                    setattr(item, "Flow10", self)
                    

    @property
    def constrainedElement(self):
        return self.__constrainedElement

    @constrainedElement.setter
    def constrainedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_ModelElement__constrainedElement", None)
        self.__constrainedElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Constraint"):
                    opp_val = getattr(item, "Constraint", None)
                    
                    if opp_val == self:
                        setattr(item, "Constraint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Constraint"):
                    opp_val = getattr(item, "Constraint", None)
                    
                    setattr(item, "Constraint", self)
                    

    @property
    def client(self):
        return self.__client

    @client.setter
    def client(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_ModelElement__client", None)
        self.__client = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Dependency"):
                    opp_val = getattr(item, "Dependency", None)
                    
                    if opp_val == self:
                        setattr(item, "Dependency", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Dependency"):
                    opp_val = getattr(item, "Dependency", None)
                    
                    setattr(item, "Dependency", self)
                    

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_ModelElement__target", None)
        self.__target = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Flow"):
                    opp_val = getattr(item, "Flow", None)
                    
                    if opp_val == self:
                        setattr(item, "Flow", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Flow"):
                    opp_val = getattr(item, "Flow", None)
                    
                    setattr(item, "Flow", self)
                    

    @property
    def extendedElement(self):
        return self.__extendedElement

    @extendedElement.setter
    def extendedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_ModelElement__extendedElement", None)
        self.__extendedElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Stereotype"):
                    opp_val = getattr(item, "Stereotype", None)
                    
                    if opp_val == self:
                        setattr(item, "Stereotype", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Stereotype"):
                    opp_val = getattr(item, "Stereotype", None)
                    
                    setattr(item, "Stereotype", self)
                    

    @property
    def context(self):
        return self.__context

    @context.setter
    def context(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_ModelElement__context", None)
        self.__context = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StateMachine"):
                    opp_val = getattr(item, "StateMachine", None)
                    
                    if opp_val == self:
                        setattr(item, "StateMachine", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StateMachine"):
                    opp_val = getattr(item, "StateMachine", None)
                    
                    setattr(item, "StateMachine", self)
                    

    @property
    def supplier(self):
        return self.__supplier

    @supplier.setter
    def supplier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_ModelElement__supplier", None)
        self.__supplier = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Dependency6"):
                    opp_val = getattr(item, "Dependency6", None)
                    
                    if opp_val == self:
                        setattr(item, "Dependency6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Dependency6"):
                    opp_val = getattr(item, "Dependency6", None)
                    
                    setattr(item, "Dependency6", self)
                    

    @property
    def resident(self):
        return self.__resident

    @resident.setter
    def resident(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_ModelElement__resident", None)
        self.__resident = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ElementResidence"):
                    opp_val = getattr(item, "ElementResidence", None)
                    
                    if opp_val == self:
                        setattr(item, "ElementResidence", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ElementResidence"):
                    opp_val = getattr(item, "ElementResidence", None)
                    
                    setattr(item, "ElementResidence", self)
                    

    @property
    def ownedElement(self):
        return self.__ownedElement

    @ownedElement.setter
    def ownedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_ModelElement__ownedElement", None)
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

    @property
    def annotatedElement(self):
        return self.__annotatedElement

    @annotatedElement.setter
    def annotatedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_ModelElement__annotatedElement", None)
        self.__annotatedElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Comment"):
                    opp_val = getattr(item, "Comment", None)
                    
                    if opp_val == self:
                        setattr(item, "Comment", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Comment"):
                    opp_val = getattr(item, "Comment", None)
                    
                    setattr(item, "Comment", self)
                    

class ModelElement:

    pass
class foundation_core_Comment(ModelElement):

    def __init__(self, body: str, comment: set["ModelElement"] = None, ModelElement108: "foundation_core_TemplateParameter" = None, ModelElement111: "foundation_core_TemplateParameter" = None, ModelElement117: "foundation_core_Stereotype" = None, ModelElement83: "foundation_core_Dependency" = None, ModelElement88: "foundation_core_PresentationElement" = None, ModelElement132: "foundation_core_TaggedValue" = None, ModelElement102: "foundation_core_ElementResidence" = None, ModelElement100: "foundation_core_Flow" = None, ModelElement98: "foundation_core_Flow" = None, ModelElement49: "foundation_core_Constraint" = None, ModelElement96: "foundation_core_Comment" = None, ModelElement128: "foundation_core_TaggedValue" = None, ModelElement106: "foundation_core_TemplateParameter" = None, ModelElement: "foundation_core_Namespace" = None, ModelElement138: "foundation_core_TemplateArgument" = None, ModelElement85: "foundation_core_Dependency" = None):
        self.body = body
        self.comment = comment if comment is not None else set()
        
        pass
    @property
    def body(self):
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body


    @property
    def comment(self):
        return self.__comment

    @comment.setter
    def comment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_Comment__comment", None)
        self.__comment = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ModelElement96"):
                    opp_val = getattr(item, "ModelElement96", None)
                    
                    if opp_val == self:
                        setattr(item, "ModelElement96", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ModelElement96"):
                    opp_val = getattr(item, "ModelElement96", None)
                    
                    setattr(item, "ModelElement96", self)
                    

class foundation_core_AssociationEnd(ModelElement):

    def __init__(self, isNavigable: str, ordering: str, aggregation: str, targetScope: str, changeability: str, foundation_core_AssociationEnd: "Multiplicity_" = None, connection: "Association" = None, associationEnd: set["Attribute"] = None, association: "Classifier" = None, specifiedEnd: set["Classifier"] = None, ModelElement108: "foundation_core_TemplateParameter" = None, ModelElement111: "foundation_core_TemplateParameter" = None, ModelElement117: "foundation_core_Stereotype" = None, ModelElement83: "foundation_core_Dependency" = None, ModelElement88: "foundation_core_PresentationElement" = None, ModelElement132: "foundation_core_TaggedValue" = None, ModelElement102: "foundation_core_ElementResidence" = None, ModelElement100: "foundation_core_Flow" = None, ModelElement98: "foundation_core_Flow" = None, ModelElement49: "foundation_core_Constraint" = None, ModelElement96: "foundation_core_Comment" = None, ModelElement128: "foundation_core_TaggedValue" = None, ModelElement106: "foundation_core_TemplateParameter" = None, ModelElement: "foundation_core_Namespace" = None, ModelElement138: "foundation_core_TemplateArgument" = None, ModelElement85: "foundation_core_Dependency" = None):
        self.isNavigable = isNavigable
        self.ordering = ordering
        self.aggregation = aggregation
        self.targetScope = targetScope
        self.changeability = changeability
        self.foundation_core_AssociationEnd = foundation_core_AssociationEnd
        self.connection = connection
        self.associationEnd = associationEnd if associationEnd is not None else set()
        self.association = association
        self.specifiedEnd = specifiedEnd if specifiedEnd is not None else set()
        
        pass
    @property
    def ordering(self):
        return self.__ordering

    @ordering.setter
    def ordering(self, ordering: str):
        self.__ordering = ordering


    @property
    def targetScope(self):
        return self.__targetScope

    @targetScope.setter
    def targetScope(self, targetScope: str):
        self.__targetScope = targetScope


    @property
    def isNavigable(self):
        return self.__isNavigable

    @isNavigable.setter
    def isNavigable(self, isNavigable: str):
        self.__isNavigable = isNavigable


    @property
    def aggregation(self):
        return self.__aggregation

    @aggregation.setter
    def aggregation(self, aggregation: str):
        self.__aggregation = aggregation


    @property
    def changeability(self):
        return self.__changeability

    @changeability.setter
    def changeability(self, changeability: str):
        self.__changeability = changeability


    @property
    def foundation_core_AssociationEnd(self):
        return self.__foundation_core_AssociationEnd

    @foundation_core_AssociationEnd.setter
    def foundation_core_AssociationEnd(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_AssociationEnd__foundation_core_AssociationEnd", None)
        self.__foundation_core_AssociationEnd = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Multiplicity40"):
                opp_val = getattr(old_value, "Multiplicity40", None)
                if opp_val == self:
                    setattr(old_value, "Multiplicity40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Multiplicity40"):
                opp_val = getattr(value, "Multiplicity40", None)
                setattr(value, "Multiplicity40", self)

    @property
    def associationEnd(self):
        return self.__associationEnd

    @associationEnd.setter
    def associationEnd(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_AssociationEnd__associationEnd", None)
        self.__associationEnd = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Attribute"):
                    opp_val = getattr(item, "Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Attribute"):
                    opp_val = getattr(item, "Attribute", None)
                    
                    setattr(item, "Attribute", self)
                    

    @property
    def association(self):
        return self.__association

    @association.setter
    def association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_AssociationEnd__association", None)
        self.__association = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Classifier44"):
                opp_val = getattr(old_value, "Classifier44", None)
                if opp_val == self:
                    setattr(old_value, "Classifier44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Classifier44"):
                opp_val = getattr(value, "Classifier44", None)
                setattr(value, "Classifier44", self)

    @property
    def connection(self):
        return self.__connection

    @connection.setter
    def connection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_AssociationEnd__connection", None)
        self.__connection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Association"):
                opp_val = getattr(old_value, "Association", None)
                if opp_val == self:
                    setattr(old_value, "Association", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Association"):
                opp_val = getattr(value, "Association", None)
                setattr(value, "Association", self)

    @property
    def specifiedEnd(self):
        return self.__specifiedEnd

    @specifiedEnd.setter
    def specifiedEnd(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_AssociationEnd__specifiedEnd", None)
        self.__specifiedEnd = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Classifier46"):
                    opp_val = getattr(item, "Classifier46", None)
                    
                    if opp_val == self:
                        setattr(item, "Classifier46", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Classifier46"):
                    opp_val = getattr(item, "Classifier46", None)
                    
                    setattr(item, "Classifier46", self)
                    

class foundation_core_Relationship(ModelElement):

    pass
class foundation_core_EnumerationLiteral(ModelElement):

    pass
class foundation_core_Constraint(ModelElement):

    pass
class foundation_core_Parameter(ModelElement):

    def __init__(self, kind: str, foundation_core_Parameter: "Expression" = None, parameter: "BehavioralFeature" = None, typedParameter: "Classifier" = None, ModelElement108: "foundation_core_TemplateParameter" = None, ModelElement111: "foundation_core_TemplateParameter" = None, ModelElement117: "foundation_core_Stereotype" = None, ModelElement83: "foundation_core_Dependency" = None, ModelElement88: "foundation_core_PresentationElement" = None, ModelElement132: "foundation_core_TaggedValue" = None, ModelElement102: "foundation_core_ElementResidence" = None, ModelElement100: "foundation_core_Flow" = None, ModelElement98: "foundation_core_Flow" = None, ModelElement49: "foundation_core_Constraint" = None, ModelElement96: "foundation_core_Comment" = None, ModelElement128: "foundation_core_TaggedValue" = None, ModelElement106: "foundation_core_TemplateParameter" = None, ModelElement: "foundation_core_Namespace" = None, ModelElement138: "foundation_core_TemplateArgument" = None, ModelElement85: "foundation_core_Dependency" = None):
        self.kind = kind
        self.foundation_core_Parameter = foundation_core_Parameter
        self.parameter = parameter
        self.typedParameter = typedParameter
        
        pass
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


    @property
    def foundation_core_Parameter(self):
        return self.__foundation_core_Parameter

    @foundation_core_Parameter.setter
    def foundation_core_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_Parameter__foundation_core_Parameter", None)
        self.__foundation_core_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Expression71"):
                opp_val = getattr(old_value, "Expression71", None)
                if opp_val == self:
                    setattr(old_value, "Expression71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Expression71"):
                opp_val = getattr(value, "Expression71", None)
                setattr(value, "Expression71", self)

    @property
    def typedParameter(self):
        return self.__typedParameter

    @typedParameter.setter
    def typedParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_Parameter__typedParameter", None)
        self.__typedParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Classifier74"):
                opp_val = getattr(old_value, "Classifier74", None)
                if opp_val == self:
                    setattr(old_value, "Classifier74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Classifier74"):
                opp_val = getattr(value, "Classifier74", None)
                setattr(value, "Classifier74", self)

    @property
    def parameter(self):
        return self.__parameter

    @parameter.setter
    def parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_Parameter__parameter", None)
        self.__parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BehavioralFeature"):
                opp_val = getattr(old_value, "BehavioralFeature", None)
                if opp_val == self:
                    setattr(old_value, "BehavioralFeature", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BehavioralFeature"):
                opp_val = getattr(value, "BehavioralFeature", None)
                setattr(value, "BehavioralFeature", self)

class foundation_core_Feature(ModelElement):

    def __init__(self, ownerScope: str, feature: "Classifier" = None, ModelElement108: "foundation_core_TemplateParameter" = None, ModelElement111: "foundation_core_TemplateParameter" = None, ModelElement117: "foundation_core_Stereotype" = None, ModelElement83: "foundation_core_Dependency" = None, ModelElement88: "foundation_core_PresentationElement" = None, ModelElement132: "foundation_core_TaggedValue" = None, ModelElement102: "foundation_core_ElementResidence" = None, ModelElement100: "foundation_core_Flow" = None, ModelElement98: "foundation_core_Flow" = None, ModelElement49: "foundation_core_Constraint" = None, ModelElement96: "foundation_core_Comment" = None, ModelElement128: "foundation_core_TaggedValue" = None, ModelElement106: "foundation_core_TemplateParameter" = None, ModelElement: "foundation_core_Namespace" = None, ModelElement138: "foundation_core_TemplateArgument" = None, ModelElement85: "foundation_core_Dependency" = None):
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
        old_value = getattr(self, f"_foundation_core_Feature__feature", None)
        self.__feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Classifier"):
                opp_val = getattr(old_value, "Classifier", None)
                if opp_val == self:
                    setattr(old_value, "Classifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Classifier"):
                opp_val = getattr(value, "Classifier", None)
                setattr(value, "Classifier", self)

class foundation_core_Namespace(ModelElement):

    pass
class foundation_core_GeneralizableElement(ModelElement):

    def __init__(self, isRoot: str, isLeaf: str, isAbstract: str, child: set["Generalization_"] = None, parent: set["Generalization_"] = None, ModelElement108: "foundation_core_TemplateParameter" = None, ModelElement111: "foundation_core_TemplateParameter" = None, ModelElement117: "foundation_core_Stereotype" = None, ModelElement83: "foundation_core_Dependency" = None, ModelElement88: "foundation_core_PresentationElement" = None, ModelElement132: "foundation_core_TaggedValue" = None, ModelElement102: "foundation_core_ElementResidence" = None, ModelElement100: "foundation_core_Flow" = None, ModelElement98: "foundation_core_Flow" = None, ModelElement49: "foundation_core_Constraint" = None, ModelElement96: "foundation_core_Comment" = None, ModelElement128: "foundation_core_TaggedValue" = None, ModelElement106: "foundation_core_TemplateParameter" = None, ModelElement: "foundation_core_Namespace" = None, ModelElement138: "foundation_core_TemplateArgument" = None, ModelElement85: "foundation_core_Dependency" = None):
        self.isRoot = isRoot
        self.isLeaf = isLeaf
        self.isAbstract = isAbstract
        self.child = child if child is not None else set()
        self.parent = parent if parent is not None else set()
        
        pass
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
    def isAbstract(self):
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: str):
        self.__isAbstract = isAbstract


    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_GeneralizableElement__parent", None)
        self.__parent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Generalization21"):
                    opp_val = getattr(item, "Generalization21", None)
                    
                    if opp_val == self:
                        setattr(item, "Generalization21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Generalization21"):
                    opp_val = getattr(item, "Generalization21", None)
                    
                    setattr(item, "Generalization21", self)
                    

    @property
    def child(self):
        return self.__child

    @child.setter
    def child(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_GeneralizableElement__child", None)
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
                    

class StateMachine:

    pass
class TaggedValue:

    pass
class Stereotype:

    pass
class TemplateParameter:

    pass
class ElementResidence:

    pass
class foundation_data_types_Expression:

    def __init__(self, body: str, language: str):
        self.body = body
        self.language = language
        
        pass
    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language


    @property
    def body(self):
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body


class Multiplicity_:

    pass
class foundation_data_types_MultiplicityRange:

    def __init__(self, lower: str, upper: str, range: "Multiplicity_" = None):
        self.lower = lower
        self.upper = upper
        self.range = range
        
        pass
    @property
    def lower(self):
        return self.__lower

    @lower.setter
    def lower(self, lower: str):
        self.__lower = lower


    @property
    def upper(self):
        return self.__upper

    @upper.setter
    def upper(self, upper: str):
        self.__upper = upper


    @property
    def range(self):
        return self.__range

    @range.setter
    def range(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_data_types_MultiplicityRange__range", None)
        self.__range = value
        
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

class MultiplicityRange:

    pass
class foundation_data_types_Multiplicity_:

    pass
class foundation_core_Element(ABC):

    pass
class Expression:

    pass
class foundation_data_types_IterationExpression(Expression):

    pass
class foundation_data_types_ProcedureExpression(Expression):

    pass
class foundation_data_types_TypeExpression(Expression):

    pass
class foundation_data_types_TimeExpression(Expression):

    pass
class foundation_data_types_MappingExpression(Expression):

    pass
class foundation_data_types_ActionExpression(Expression):

    pass
class foundation_data_types_ArgListsExpression(Expression):

    pass
class foundation_data_types_ObjectSetExpression(Expression):

    pass
class foundation_data_types_BooleanExpression(Expression):

    pass
class foundation_core_TaggedValue(ModelElement):

    def __init__(self, dataValue: str, referenceTag: set["ModelElement"] = None, taggedValue: "ModelElement" = None, typedValue: "TagDefinition" = None, ModelElement108: "foundation_core_TemplateParameter" = None, ModelElement111: "foundation_core_TemplateParameter" = None, ModelElement117: "foundation_core_Stereotype" = None, ModelElement83: "foundation_core_Dependency" = None, ModelElement88: "foundation_core_PresentationElement" = None, ModelElement132: "foundation_core_TaggedValue" = None, ModelElement102: "foundation_core_ElementResidence" = None, ModelElement100: "foundation_core_Flow" = None, ModelElement98: "foundation_core_Flow" = None, ModelElement49: "foundation_core_Constraint" = None, ModelElement96: "foundation_core_Comment" = None, ModelElement128: "foundation_core_TaggedValue" = None, ModelElement106: "foundation_core_TemplateParameter" = None, ModelElement: "foundation_core_Namespace" = None, ModelElement138: "foundation_core_TemplateArgument" = None, ModelElement85: "foundation_core_Dependency" = None):
        self.dataValue = dataValue
        self.referenceTag = referenceTag if referenceTag is not None else set()
        self.taggedValue = taggedValue
        self.typedValue = typedValue
        
        pass
    @property
    def dataValue(self):
        return self.__dataValue

    @dataValue.setter
    def dataValue(self, dataValue: str):
        self.__dataValue = dataValue


    @property
    def referenceTag(self):
        return self.__referenceTag

    @referenceTag.setter
    def referenceTag(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_TaggedValue__referenceTag", None)
        self.__referenceTag = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ModelElement132"):
                    opp_val = getattr(item, "ModelElement132", None)
                    
                    if opp_val == self:
                        setattr(item, "ModelElement132", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ModelElement132"):
                    opp_val = getattr(item, "ModelElement132", None)
                    
                    setattr(item, "ModelElement132", self)
                    

    @property
    def typedValue(self):
        return self.__typedValue

    @typedValue.setter
    def typedValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_TaggedValue__typedValue", None)
        self.__typedValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TagDefinition130"):
                opp_val = getattr(old_value, "TagDefinition130", None)
                if opp_val == self:
                    setattr(old_value, "TagDefinition130", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TagDefinition130"):
                opp_val = getattr(value, "TagDefinition130", None)
                setattr(value, "TagDefinition130", self)

    @property
    def taggedValue(self):
        return self.__taggedValue

    @taggedValue.setter
    def taggedValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_TaggedValue__taggedValue", None)
        self.__taggedValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ModelElement128"):
                opp_val = getattr(old_value, "ModelElement128", None)
                if opp_val == self:
                    setattr(old_value, "ModelElement128", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ModelElement128"):
                opp_val = getattr(value, "ModelElement128", None)
                setattr(value, "ModelElement128", self)

class foundation_core_TagDefinition(ModelElement):

    def __init__(self, tagType: str, foundation_core_TagDefinition: "Multiplicity_" = None, definedTag: "Stereotype" = None, type125: set["TaggedValue"] = None, ModelElement108: "foundation_core_TemplateParameter" = None, ModelElement111: "foundation_core_TemplateParameter" = None, ModelElement117: "foundation_core_Stereotype" = None, ModelElement83: "foundation_core_Dependency" = None, ModelElement88: "foundation_core_PresentationElement" = None, ModelElement132: "foundation_core_TaggedValue" = None, ModelElement102: "foundation_core_ElementResidence" = None, ModelElement100: "foundation_core_Flow" = None, ModelElement98: "foundation_core_Flow" = None, ModelElement49: "foundation_core_Constraint" = None, ModelElement96: "foundation_core_Comment" = None, ModelElement128: "foundation_core_TaggedValue" = None, ModelElement106: "foundation_core_TemplateParameter" = None, ModelElement: "foundation_core_Namespace" = None, ModelElement138: "foundation_core_TemplateArgument" = None, ModelElement85: "foundation_core_Dependency" = None):
        self.tagType = tagType
        self.foundation_core_TagDefinition = foundation_core_TagDefinition
        self.definedTag = definedTag
        self.type125 = type125 if type125 is not None else set()
        
        pass
    @property
    def tagType(self):
        return self.__tagType

    @tagType.setter
    def tagType(self, tagType: str):
        self.__tagType = tagType


    @property
    def definedTag(self):
        return self.__definedTag

    @definedTag.setter
    def definedTag(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_TagDefinition__definedTag", None)
        self.__definedTag = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Stereotype123"):
                opp_val = getattr(old_value, "Stereotype123", None)
                if opp_val == self:
                    setattr(old_value, "Stereotype123", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Stereotype123"):
                opp_val = getattr(value, "Stereotype123", None)
                setattr(value, "Stereotype123", self)

    @property
    def foundation_core_TagDefinition(self):
        return self.__foundation_core_TagDefinition

    @foundation_core_TagDefinition.setter
    def foundation_core_TagDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_TagDefinition__foundation_core_TagDefinition", None)
        self.__foundation_core_TagDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Multiplicity121"):
                opp_val = getattr(old_value, "Multiplicity121", None)
                if opp_val == self:
                    setattr(old_value, "Multiplicity121", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Multiplicity121"):
                opp_val = getattr(value, "Multiplicity121", None)
                setattr(value, "Multiplicity121", self)

    @property
    def type125(self):
        return self.__type125

    @type125.setter
    def type125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_foundation_core_TagDefinition__type125", None)
        self.__type125 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TaggedValue126"):
                    opp_val = getattr(item, "TaggedValue126", None)
                    
                    if opp_val == self:
                        setattr(item, "TaggedValue126", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TaggedValue126"):
                    opp_val = getattr(item, "TaggedValue126", None)
                    
                    setattr(item, "TaggedValue126", self)
                    
