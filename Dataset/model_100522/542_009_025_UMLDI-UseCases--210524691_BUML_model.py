####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata
)

# Enumerations
AggregationKind: Enumeration = Enumeration(
    name="AggregationKind",
    literals={
            EnumerationLiteral(name="ak_none"),
			EnumerationLiteral(name="ak_aggregate"),
			EnumerationLiteral(name="ak_composite")
    }
)

ChangeableKind: Enumeration = Enumeration(
    name="ChangeableKind",
    literals={
            EnumerationLiteral(name="ck_changeable"),
			EnumerationLiteral(name="ck_frozen"),
			EnumerationLiteral(name="ck_addOnly")
    }
)

OrderingKind: Enumeration = Enumeration(
    name="OrderingKind",
    literals={
            EnumerationLiteral(name="ok_unordered"),
			EnumerationLiteral(name="ok_ordered")
    }
)

ScopeKind: Enumeration = Enumeration(
    name="ScopeKind",
    literals={
            EnumerationLiteral(name="sk_instance"),
			EnumerationLiteral(name="sk_classifier")
    }
)

VisibilityKind: Enumeration = Enumeration(
    name="VisibilityKind",
    literals={
            EnumerationLiteral(name="vk_public"),
			EnumerationLiteral(name="vk_protected"),
			EnumerationLiteral(name="vk_private"),
			EnumerationLiteral(name="vk_package")
    }
)

# Classes
Instance = Class(name="Instance")
LinkEnd = Class(name="LinkEnd")
Classifier = Class(name="Classifier")
ComponentInstance = Class(name="ComponentInstance")
AttributeLink = Class(name="AttributeLink")
Link = Class(name="Link")
Common_Behavior_Instance = Class(name="Common_Behavior_Instance", is_abstract=True)
ModelElement = Class(name="ModelElement")
Attribute = Class(name="Attribute")
Common_Behavior_Link = Class(name="Common_Behavior_Link")
Association = Class(name="Association")
Common_Behavior_LinkEnd = Class(name="Common_Behavior_LinkEnd")
Common_Behavior_AttributeLink = Class(name="Common_Behavior_AttributeLink")
Common_Behavior_ComponentInstance = Class(name="Common_Behavior_ComponentInstance")
Use_Cases_UseCaseInstance = Class(name="Use_Cases_UseCaseInstance")
Use_Cases_Extend = Class(name="Use_Cases_Extend")
Relationship = Class(name="Relationship")
NodeInstance = Class(name="NodeInstance")
Common_Behavior_NodeInstance = Class(name="Common_Behavior_NodeInstance")
Use_Cases_UseCase = Class(name="Use_Cases_UseCase")
Include = Class(name="Include")
Extend = Class(name="Extend")
ExtensionPoint = Class(name="ExtensionPoint")
AssociationEnd = Class(name="AssociationEnd")
Use_Cases_Actor = Class(name="Use_Cases_Actor")
Core_Element = Class(name="Core_Element", is_abstract=True)
Core_ModelElement = Class(name="Core_ModelElement", is_abstract=True)
Element = Class(name="Element")
Namespace = Class(name="Namespace")
UseCase = Class(name="UseCase")
BooleanExpression = Class(name="BooleanExpression")
Use_Cases_Include = Class(name="Use_Cases_Include")
Use_Cases_ExtensionPoint = Class(name="Use_Cases_ExtensionPoint")
Core_Classifier = Class(name="Core_Classifier", is_abstract=True)
GeneralizableElement = Class(name="GeneralizableElement")
Feature = Class(name="Feature")
Core_GeneralizableElement = Class(name="Core_GeneralizableElement", is_abstract=True)
Generalization_ = Class(name="Generalization_")
Core_Namespace = Class(name="Core_Namespace", is_abstract=True)
Core_AssociationEnd = Class(name="Core_AssociationEnd")
Core_Feature = Class(name="Core_Feature", is_abstract=True)
Core_StructuralFeature = Class(name="Core_StructuralFeature", is_abstract=True)
Multiplicity_ = Class(name="Multiplicity_")
Core_Relationship = Class(name="Core_Relationship", is_abstract=True)
Core_Association = Class(name="Core_Association")
Core_Attribute = Class(name="Core_Attribute")
StructuralFeature = Class(name="StructuralFeature")
Expression = Class(name="Expression")
Core_Generalization = Class(name="Core_Generalization_")
Data_Types_Expression = Class(name="Data_Types_Expression")
Data_Types_Multiplicity = Class(name="Data_Types_Multiplicity_")
MultiplicityRange = Class(name="MultiplicityRange")
Data_Types_MultiplicityRange = Class(name="Data_Types_MultiplicityRange")
Data_Types_BooleanExpression = Class(name="Data_Types_BooleanExpression")

# Instance class attributes and methods

# LinkEnd class attributes and methods

# Classifier class attributes and methods

# ComponentInstance class attributes and methods

# AttributeLink class attributes and methods

# Link class attributes and methods

# Common_Behavior_Instance class attributes and methods

# ModelElement class attributes and methods

# Attribute class attributes and methods

# Common_Behavior_Link class attributes and methods

# Association class attributes and methods

# Common_Behavior_LinkEnd class attributes and methods

# Common_Behavior_AttributeLink class attributes and methods

# Common_Behavior_ComponentInstance class attributes and methods

# Use_Cases_UseCaseInstance class attributes and methods

# Use_Cases_Extend class attributes and methods

# Relationship class attributes and methods

# NodeInstance class attributes and methods

# Common_Behavior_NodeInstance class attributes and methods

# Use_Cases_UseCase class attributes and methods

# Include class attributes and methods

# Extend class attributes and methods

# ExtensionPoint class attributes and methods

# AssociationEnd class attributes and methods

# Use_Cases_Actor class attributes and methods

# Core_Element class attributes and methods

# Core_ModelElement class attributes and methods
Core_ModelElement_name: Property = Property(name="name", type=StringType)
Core_ModelElement_visibility: Property = Property(name="visibility", type=StringType)
Core_ModelElement_isSpecification: Property = Property(name="isSpecification", type=StringType)
Core_ModelElement.attributes={Core_ModelElement_visibility, Core_ModelElement_isSpecification, Core_ModelElement_name}

# Element class attributes and methods

# Namespace class attributes and methods

# UseCase class attributes and methods

# BooleanExpression class attributes and methods

# Use_Cases_Include class attributes and methods

# Use_Cases_ExtensionPoint class attributes and methods
Use_Cases_ExtensionPoint_location: Property = Property(name="location", type=StringType)
Use_Cases_ExtensionPoint.attributes={Use_Cases_ExtensionPoint_location}

# Core_Classifier class attributes and methods

# GeneralizableElement class attributes and methods

# Feature class attributes and methods

# Core_GeneralizableElement class attributes and methods
Core_GeneralizableElement_isRoot: Property = Property(name="isRoot", type=StringType)
Core_GeneralizableElement_isLeaf: Property = Property(name="isLeaf", type=StringType)
Core_GeneralizableElement_isAbstract: Property = Property(name="isAbstract", type=StringType)
Core_GeneralizableElement.attributes={Core_GeneralizableElement_isAbstract, Core_GeneralizableElement_isRoot, Core_GeneralizableElement_isLeaf}

# Generalization_ class attributes and methods

# Core_Namespace class attributes and methods

# Core_AssociationEnd class attributes and methods
Core_AssociationEnd_changeability: Property = Property(name="changeability", type=StringType)
Core_AssociationEnd_isNavigable: Property = Property(name="isNavigable", type=StringType)
Core_AssociationEnd_ordering: Property = Property(name="ordering", type=StringType)
Core_AssociationEnd_aggregation: Property = Property(name="aggregation", type=StringType)
Core_AssociationEnd_targetScope: Property = Property(name="targetScope", type=StringType)
Core_AssociationEnd.attributes={Core_AssociationEnd_changeability, Core_AssociationEnd_aggregation, Core_AssociationEnd_isNavigable, Core_AssociationEnd_ordering, Core_AssociationEnd_targetScope}

# Core_Feature class attributes and methods
Core_Feature_ownerScope: Property = Property(name="ownerScope", type=StringType)
Core_Feature.attributes={Core_Feature_ownerScope}

# Core_StructuralFeature class attributes and methods
Core_StructuralFeature_targetScope: Property = Property(name="targetScope", type=StringType)
Core_StructuralFeature_ordering: Property = Property(name="ordering", type=StringType)
Core_StructuralFeature_changeability: Property = Property(name="changeability", type=StringType)
Core_StructuralFeature.attributes={Core_StructuralFeature_changeability, Core_StructuralFeature_ordering, Core_StructuralFeature_targetScope}

# Multiplicity_ class attributes and methods

# Core_Relationship class attributes and methods

# Core_Association class attributes and methods

# Core_Attribute class attributes and methods

# StructuralFeature class attributes and methods

# Expression class attributes and methods

# Core_Generalization class attributes and methods
Core_Generalization_discriminator: Property = Property(name="discriminator", type=StringType)
Core_Generalization.attributes={Core_Generalization_discriminator}

# Data_Types_Expression class attributes and methods
Data_Types_Expression_language: Property = Property(name="language", type=StringType)
Data_Types_Expression_body: Property = Property(name="body", type=StringType)
Data_Types_Expression.attributes={Data_Types_Expression_language, Data_Types_Expression_body}

# Data_Types_Multiplicity class attributes and methods

# MultiplicityRange class attributes and methods

# Data_Types_MultiplicityRange class attributes and methods
Data_Types_MultiplicityRange_lower: Property = Property(name="lower", type=StringType)
Data_Types_MultiplicityRange_upper: Property = Property(name="upper", type=StringType)
Data_Types_MultiplicityRange.attributes={Data_Types_MultiplicityRange_lower, Data_Types_MultiplicityRange_upper}

# Data_Types_BooleanExpression class attributes and methods

# Relationships
ownedInstance0: BinaryAssociation = BinaryAssociation(
    name="ownedInstance0",
    ends={
        Property(name="Instance", type=Common_Behavior_Instance, multiplicity=Multiplicity(1, 1)),
        Property(name="Common_Behavior_Instance", type=Instance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
linkEnd1: BinaryAssociation = BinaryAssociation(
    name="linkEnd1",
    ends={
        Property(name="LinkEnd", type=Common_Behavior_Instance, multiplicity=Multiplicity(1, 1)),
        Property(name="instance", type=LinkEnd, multiplicity=Multiplicity(0, 9999))
    }
)
classifier2: BinaryAssociation = BinaryAssociation(
    name="classifier2",
    ends={
        Property(name="Classifier", type=Common_Behavior_Instance, multiplicity=Multiplicity(1, 1)),
        Property(name="Common_Behavior_Instance3", type=Classifier, multiplicity=Multiplicity(1, 9999))
    }
)
componentInstance4: BinaryAssociation = BinaryAssociation(
    name="componentInstance4",
    ends={
        Property(name="ComponentInstance", type=Common_Behavior_Instance, multiplicity=Multiplicity(1, 1)),
        Property(name="resident", type=ComponentInstance, multiplicity=Multiplicity(0, 1))
    }
)
slot5: BinaryAssociation = BinaryAssociation(
    name="slot5",
    ends={
        Property(name="AttributeLink", type=Common_Behavior_Instance, multiplicity=Multiplicity(1, 1)),
        Property(name="instance6", type=AttributeLink, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedLink7: BinaryAssociation = BinaryAssociation(
    name="ownedLink7",
    ends={
        Property(name="Link", type=Common_Behavior_Instance, multiplicity=Multiplicity(1, 1)),
        Property(name="Common_Behavior_Instance8", type=Link, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
linkEnd13: BinaryAssociation = BinaryAssociation(
    name="linkEnd13",
    ends={
        Property(name="LinkEnd14", type=Common_Behavior_AttributeLink, multiplicity=Multiplicity(1, 1)),
        Property(name="qualifiedValue", type=LinkEnd, multiplicity=Multiplicity(0, 1))
    }
)
attribute15: BinaryAssociation = BinaryAssociation(
    name="attribute15",
    ends={
        Property(name="Attribute", type=Common_Behavior_AttributeLink, multiplicity=Multiplicity(1, 1)),
        Property(name="Common_Behavior_AttributeLink16", type=Attribute, multiplicity=Multiplicity(1, 1))
    }
)
association17: BinaryAssociation = BinaryAssociation(
    name="association17",
    ends={
        Property(name="Association", type=Common_Behavior_Link, multiplicity=Multiplicity(1, 1)),
        Property(name="Common_Behavior_Link", type=Association, multiplicity=Multiplicity(1, 1))
    }
)
connection18: BinaryAssociation = BinaryAssociation(
    name="connection18",
    ends={
        Property(name="LinkEnd19", type=Common_Behavior_Link, multiplicity=Multiplicity(1, 1)),
        Property(name="link", type=LinkEnd, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
link20: BinaryAssociation = BinaryAssociation(
    name="link20",
    ends={
        Property(name="Link21", type=Common_Behavior_LinkEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="connection", type=Link, multiplicity=Multiplicity(1, 1))
    }
)
instance9: BinaryAssociation = BinaryAssociation(
    name="instance9",
    ends={
        Property(name="Instance10", type=Common_Behavior_AttributeLink, multiplicity=Multiplicity(1, 1)),
        Property(name="slot", type=Instance, multiplicity=Multiplicity(0, 1))
    }
)
value11: BinaryAssociation = BinaryAssociation(
    name="value11",
    ends={
        Property(name="Instance12", type=Common_Behavior_AttributeLink, multiplicity=Multiplicity(1, 1)),
        Property(name="Common_Behavior_AttributeLink", type=Instance, multiplicity=Multiplicity(1, 1))
    }
)
resident28: BinaryAssociation = BinaryAssociation(
    name="resident28",
    ends={
        Property(name="Instance29", type=Common_Behavior_ComponentInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="componentInstance", type=Instance, multiplicity=Multiplicity(0, 9999))
    }
)
extensionPoint37: BinaryAssociation = BinaryAssociation(
    name="extensionPoint37",
    ends={
        Property(name="ExtensionPoint38", type=Use_Cases_Extend, multiplicity=Multiplicity(1, 1)),
        Property(name="Use_Cases_Extend", type=ExtensionPoint, multiplicity=Multiplicity(1, 9999))
    }
)
nodeInstance30: BinaryAssociation = BinaryAssociation(
    name="nodeInstance30",
    ends={
        Property(name="NodeInstance", type=Common_Behavior_ComponentInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="resident31", type=NodeInstance, multiplicity=Multiplicity(0, 1))
    }
)
resident32: BinaryAssociation = BinaryAssociation(
    name="resident32",
    ends={
        Property(name="ComponentInstance33", type=Common_Behavior_NodeInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="nodeInstance", type=ComponentInstance, multiplicity=Multiplicity(0, 9999))
    }
)
include34: BinaryAssociation = BinaryAssociation(
    name="include34",
    ends={
        Property(name="Include", type=Use_Cases_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="base", type=Include, multiplicity=Multiplicity(0, 9999))
    }
)
qualifiedValue22: BinaryAssociation = BinaryAssociation(
    name="qualifiedValue22",
    ends={
        Property(name="AttributeLink23", type=Common_Behavior_LinkEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="linkEnd", type=AttributeLink, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extend35: BinaryAssociation = BinaryAssociation(
    name="extend35",
    ends={
        Property(name="Extend", type=Use_Cases_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="extension", type=Extend, multiplicity=Multiplicity(0, 9999))
    }
)
instance24: BinaryAssociation = BinaryAssociation(
    name="instance24",
    ends={
        Property(name="Instance26", type=Common_Behavior_LinkEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="linkEnd25", type=Instance, multiplicity=Multiplicity(1, 1))
    }
)
extensionPoint36: BinaryAssociation = BinaryAssociation(
    name="extensionPoint36",
    ends={
        Property(name="ExtensionPoint", type=Use_Cases_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="useCase", type=ExtensionPoint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
associationEnd27: BinaryAssociation = BinaryAssociation(
    name="associationEnd27",
    ends={
        Property(name="AssociationEnd", type=Common_Behavior_LinkEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="Common_Behavior_LinkEnd", type=AssociationEnd, multiplicity=Multiplicity(1, 1))
    }
)
namespace51: BinaryAssociation = BinaryAssociation(
    name="namespace51",
    ends={
        Property(name="Namespace", type=Core_ModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedElement", type=Namespace, multiplicity=Multiplicity(0, 1))
    }
)
extension39: BinaryAssociation = BinaryAssociation(
    name="extension39",
    ends={
        Property(name="UseCase", type=Use_Cases_Extend, multiplicity=Multiplicity(1, 1)),
        Property(name="extend", type=UseCase, multiplicity=Multiplicity(1, 1))
    }
)
base40: BinaryAssociation = BinaryAssociation(
    name="base40",
    ends={
        Property(name="UseCase42", type=Use_Cases_Extend, multiplicity=Multiplicity(1, 1)),
        Property(name="Use_Cases_Extend41", type=UseCase, multiplicity=Multiplicity(1, 1))
    }
)
condition43: BinaryAssociation = BinaryAssociation(
    name="condition43",
    ends={
        Property(name="BooleanExpression", type=Use_Cases_Extend, multiplicity=Multiplicity(1, 1)),
        Property(name="Use_Cases_Extend44", type=BooleanExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
addition45: BinaryAssociation = BinaryAssociation(
    name="addition45",
    ends={
        Property(name="UseCase46", type=Use_Cases_Include, multiplicity=Multiplicity(1, 1)),
        Property(name="Use_Cases_Include", type=UseCase, multiplicity=Multiplicity(1, 1))
    }
)
base47: BinaryAssociation = BinaryAssociation(
    name="base47",
    ends={
        Property(name="UseCase48", type=Use_Cases_Include, multiplicity=Multiplicity(1, 1)),
        Property(name="include", type=UseCase, multiplicity=Multiplicity(1, 1))
    }
)
useCase49: BinaryAssociation = BinaryAssociation(
    name="useCase49",
    ends={
        Property(name="UseCase50", type=Use_Cases_ExtensionPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="extensionPoint", type=UseCase, multiplicity=Multiplicity(1, 1))
    }
)
powertypeRange54: BinaryAssociation = BinaryAssociation(
    name="powertypeRange54",
    ends={
        Property(name="Generalization55", type=Core_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="powertype", type=Generalization_, multiplicity=Multiplicity(0, 9999))
    }
)
generalization52: BinaryAssociation = BinaryAssociation(
    name="generalization52",
    ends={
        Property(name="Generalization_", type=Core_GeneralizableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="child", type=Generalization_, multiplicity=Multiplicity(0, 9999))
    }
)
ownedElement53: BinaryAssociation = BinaryAssociation(
    name="ownedElement53",
    ends={
        Property(name="ModelElement", type=Core_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="namespace", type=ModelElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
association63: BinaryAssociation = BinaryAssociation(
    name="association63",
    ends={
        Property(name="Association65", type=Core_AssociationEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="connection64", type=Association, multiplicity=Multiplicity(1, 1))
    }
)
feature56: BinaryAssociation = BinaryAssociation(
    name="feature56",
    ends={
        Property(name="Feature", type=Core_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owner57: BinaryAssociation = BinaryAssociation(
    name="owner57",
    ends={
        Property(name="Classifier58", type=Core_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="feature", type=Classifier, multiplicity=Multiplicity(0, 1))
    }
)
type59: BinaryAssociation = BinaryAssociation(
    name="type59",
    ends={
        Property(name="Classifier60", type=Core_StructuralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="Core_StructuralFeature", type=Classifier, multiplicity=Multiplicity(1, 1))
    }
)
multiplicity61: BinaryAssociation = BinaryAssociation(
    name="multiplicity61",
    ends={
        Property(name="Multiplicity", type=Core_StructuralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="Core_StructuralFeature62", type=Multiplicity_, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
connection76: BinaryAssociation = BinaryAssociation(
    name="connection76",
    ends={
        Property(name="AssociationEnd77", type=Core_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="association", type=AssociationEnd, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
specification66: BinaryAssociation = BinaryAssociation(
    name="specification66",
    ends={
        Property(name="Classifier67", type=Core_AssociationEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="Core_AssociationEnd", type=Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
participant68: BinaryAssociation = BinaryAssociation(
    name="participant68",
    ends={
        Property(name="Classifier70", type=Core_AssociationEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="Core_AssociationEnd69", type=Classifier, multiplicity=Multiplicity(1, 1))
    }
)
qualifier71: BinaryAssociation = BinaryAssociation(
    name="qualifier71",
    ends={
        Property(name="Attribute72", type=Core_AssociationEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="associationEnd", type=Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
multiplicity73: BinaryAssociation = BinaryAssociation(
    name="multiplicity73",
    ends={
        Property(name="Multiplicity75", type=Core_AssociationEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="Core_AssociationEnd74", type=Multiplicity_, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
associationEnd78: BinaryAssociation = BinaryAssociation(
    name="associationEnd78",
    ends={
        Property(name="AssociationEnd79", type=Core_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="qualifier", type=AssociationEnd, multiplicity=Multiplicity(0, 1))
    }
)
initialValue80: BinaryAssociation = BinaryAssociation(
    name="initialValue80",
    ends={
        Property(name="Expression", type=Core_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="Core_Attribute", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parent81: BinaryAssociation = BinaryAssociation(
    name="parent81",
    ends={
        Property(name="GeneralizableElement", type=Core_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="Core_Generalization", type=GeneralizableElement, multiplicity=Multiplicity(1, 1))
    }
)
powertype82: BinaryAssociation = BinaryAssociation(
    name="powertype82",
    ends={
        Property(name="Classifier83", type=Core_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="powertypeRange", type=Classifier, multiplicity=Multiplicity(0, 1))
    }
)
child84: BinaryAssociation = BinaryAssociation(
    name="child84",
    ends={
        Property(name="GeneralizableElement85", type=Core_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="generalization", type=GeneralizableElement, multiplicity=Multiplicity(1, 1))
    }
)
multiplicity87: BinaryAssociation = BinaryAssociation(
    name="multiplicity87",
    ends={
        Property(name="Multiplicity88", type=Data_Types_MultiplicityRange, multiplicity=Multiplicity(1, 1)),
        Property(name="range", type=Multiplicity_, multiplicity=Multiplicity(1, 1))
    }
)
range86: BinaryAssociation = BinaryAssociation(
    name="range86",
    ends={
        Property(name="MultiplicityRange", type=Data_Types_Multiplicity, multiplicity=Multiplicity(1, 1)),
        Property(name="multiplicity", type=MultiplicityRange, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)

# Generalizations
gen_Common_Behavior_Instance_ModelElement = Generalization(general=ModelElement, specific=Common_Behavior_Instance)
gen_Common_Behavior_Link_ModelElement = Generalization(general=ModelElement, specific=Common_Behavior_Link)
gen_Common_Behavior_LinkEnd_ModelElement = Generalization(general=ModelElement, specific=Common_Behavior_LinkEnd)
gen_Common_Behavior_AttributeLink_ModelElement = Generalization(general=ModelElement, specific=Common_Behavior_AttributeLink)
gen_Common_Behavior_ComponentInstance_Instance = Generalization(general=Instance, specific=Common_Behavior_ComponentInstance)
gen_Use_Cases_UseCaseInstance_Instance = Generalization(general=Instance, specific=Use_Cases_UseCaseInstance)
gen_Use_Cases_Extend_Relationship = Generalization(general=Relationship, specific=Use_Cases_Extend)
gen_Common_Behavior_NodeInstance_Instance = Generalization(general=Instance, specific=Common_Behavior_NodeInstance)
gen_Use_Cases_UseCase_Classifier = Generalization(general=Classifier, specific=Use_Cases_UseCase)
gen_Use_Cases_Actor_Classifier = Generalization(general=Classifier, specific=Use_Cases_Actor)
gen_Core_ModelElement_Element = Generalization(general=Element, specific=Core_ModelElement)
gen_Use_Cases_Include_Relationship = Generalization(general=Relationship, specific=Use_Cases_Include)
gen_Use_Cases_ExtensionPoint_ModelElement = Generalization(general=ModelElement, specific=Use_Cases_ExtensionPoint)
gen_Core_Classifier_GeneralizableElement = Generalization(general=GeneralizableElement, specific=Core_Classifier)
gen_Core_Classifier_Namespace = Generalization(general=Namespace, specific=Core_Classifier)
gen_Core_GeneralizableElement_ModelElement = Generalization(general=ModelElement, specific=Core_GeneralizableElement)
gen_Core_Namespace_ModelElement = Generalization(general=ModelElement, specific=Core_Namespace)
gen_Core_AssociationEnd_ModelElement = Generalization(general=ModelElement, specific=Core_AssociationEnd)
gen_Core_Feature_ModelElement = Generalization(general=ModelElement, specific=Core_Feature)
gen_Core_StructuralFeature_Feature = Generalization(general=Feature, specific=Core_StructuralFeature)
gen_Core_Relationship_ModelElement = Generalization(general=ModelElement, specific=Core_Relationship)
gen_Core_Association_GeneralizableElement = Generalization(general=GeneralizableElement, specific=Core_Association)
gen_Core_Association_Relationship = Generalization(general=Relationship, specific=Core_Association)
gen_Core_Attribute_StructuralFeature = Generalization(general=StructuralFeature, specific=Core_Attribute)
gen_Core_Generalization_Relationship = Generalization(general=Relationship, specific=Core_Generalization)
gen_Data_Types_BooleanExpression_Expression = Generalization(general=Expression, specific=Data_Types_BooleanExpression)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={Instance, LinkEnd, Classifier, ComponentInstance, AttributeLink, Link, Common_Behavior_Instance, ModelElement, Attribute, Common_Behavior_Link, Association, Common_Behavior_LinkEnd, Common_Behavior_AttributeLink, Common_Behavior_ComponentInstance, Use_Cases_UseCaseInstance, Use_Cases_Extend, Relationship, NodeInstance, Common_Behavior_NodeInstance, Use_Cases_UseCase, Include, Extend, ExtensionPoint, AssociationEnd, Use_Cases_Actor, Core_Element, Core_ModelElement, Element, Namespace, UseCase, BooleanExpression, Use_Cases_Include, Use_Cases_ExtensionPoint, Core_Classifier, GeneralizableElement, Feature, Core_GeneralizableElement, Generalization_, Core_Namespace, Core_AssociationEnd, Core_Feature, Core_StructuralFeature, Multiplicity_, Core_Relationship, Core_Association, Core_Attribute, StructuralFeature, Expression, Core_Generalization, Data_Types_Expression, Data_Types_Multiplicity, MultiplicityRange, Data_Types_MultiplicityRange, Data_Types_BooleanExpression, AggregationKind, ChangeableKind, OrderingKind, ScopeKind, VisibilityKind},
    associations={ownedInstance0, linkEnd1, classifier2, componentInstance4, slot5, ownedLink7, linkEnd13, attribute15, association17, connection18, link20, instance9, value11, resident28, extensionPoint37, nodeInstance30, resident32, include34, qualifiedValue22, extend35, instance24, extensionPoint36, associationEnd27, namespace51, extension39, base40, condition43, addition45, base47, useCase49, powertypeRange54, generalization52, ownedElement53, association63, feature56, owner57, type59, multiplicity61, connection76, specification66, participant68, qualifier71, multiplicity73, associationEnd78, initialValue80, parent81, powertype82, child84, multiplicity87, range86},
    generalizations={gen_Common_Behavior_Instance_ModelElement, gen_Common_Behavior_Link_ModelElement, gen_Common_Behavior_LinkEnd_ModelElement, gen_Common_Behavior_AttributeLink_ModelElement, gen_Common_Behavior_ComponentInstance_Instance, gen_Use_Cases_UseCaseInstance_Instance, gen_Use_Cases_Extend_Relationship, gen_Common_Behavior_NodeInstance_Instance, gen_Use_Cases_UseCase_Classifier, gen_Use_Cases_Actor_Classifier, gen_Core_ModelElement_Element, gen_Use_Cases_Include_Relationship, gen_Use_Cases_ExtensionPoint_ModelElement, gen_Core_Classifier_GeneralizableElement, gen_Core_Classifier_Namespace, gen_Core_GeneralizableElement_ModelElement, gen_Core_Namespace_ModelElement, gen_Core_AssociationEnd_ModelElement, gen_Core_Feature_ModelElement, gen_Core_StructuralFeature_Feature, gen_Core_Relationship_ModelElement, gen_Core_Association_GeneralizableElement, gen_Core_Association_Relationship, gen_Core_Attribute_StructuralFeature, gen_Core_Generalization_Relationship, gen_Data_Types_BooleanExpression_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)