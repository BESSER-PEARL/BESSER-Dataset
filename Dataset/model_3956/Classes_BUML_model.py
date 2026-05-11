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
VisibilityKind: Enumeration = Enumeration(
    name="VisibilityKind",
    literals={
            EnumerationLiteral(name="package"),
			EnumerationLiteral(name="public"),
			EnumerationLiteral(name="private"),
			EnumerationLiteral(name="protected")
    }
)

AggregationKind: Enumeration = Enumeration(
    name="AggregationKind",
    literals={
            EnumerationLiteral(name="none"),
			EnumerationLiteral(name="shared"),
			EnumerationLiteral(name="composite")
    }
)

# Classes
Classes_Kernel_Element = Class(name="Classes_Kernel_Element", is_abstract=True)
Comment = Class(name="Comment")
Element = Class(name="Element")
Classes_Kernel_NamedElement = Class(name="Classes_Kernel_NamedElement", is_abstract=True)
Namespace = Class(name="Namespace")
Dependency = Class(name="Dependency")
Classes_Kernel_Namespace = Class(name="Classes_Kernel_Namespace")
NamedElement = Class(name="NamedElement")
PackageableElement = Class(name="PackageableElement")
Package = Class(name="Package")
Classes_Kernel_Package = Class(name="Classes_Kernel_Package")
Kernel_Namespace = Class(name="Kernel_Namespace")
Kernel_PackageableElement = Class(name="Kernel_PackageableElement")
Type = Class(name="Type")
PackageMerge = Class(name="PackageMerge")
Classes_Kernel_Comment = Class(name="Classes_Kernel_Comment")
Classes_Kernel_Relationship = Class(name="Classes_Kernel_Relationship", is_abstract=True)
ElementImport = Class(name="ElementImport")
PackageImport = Class(name="PackageImport")
Constraint = Class(name="Constraint")
Classes_Kernel_PackageableElement = Class(name="Classes_Kernel_PackageableElement")
Classes_Kernel_ElementImport = Class(name="Classes_Kernel_ElementImport")
DirectedRelationship = Class(name="DirectedRelationship")
Classes_Kernel_PackageImport = Class(name="Classes_Kernel_PackageImport")
Slot = Class(name="Slot")
InstanceSpecification = Class(name="InstanceSpecification")
Classes_Kernel_TypedElement = Class(name="Classes_Kernel_TypedElement", is_abstract=True)
Classes_Kernel_Type = Class(name="Classes_Kernel_Type", is_abstract=True)
Classes_Kernel_Expression = Class(name="Classes_Kernel_Expression")
Classes_Kernel_OpaqueExpression = Class(name="Classes_Kernel_OpaqueExpression")
Classes_Kernel_LiteralSpecification = Class(name="Classes_Kernel_LiteralSpecification", is_abstract=True)
Classes_Kernel_LiteralNull = Class(name="Classes_Kernel_LiteralNull")
LiteralSpecification = Class(name="LiteralSpecification")
Classes_Kernel_LiteralBoolean = Class(name="Classes_Kernel_LiteralBoolean")
Classes_Kernel_LiteralInteger = Class(name="Classes_Kernel_LiteralInteger")
Classes_Kernel_DirectedRelationship = Class(name="Classes_Kernel_DirectedRelationship", is_abstract=True)
Relationship = Class(name="Relationship")
Classes_Kernel_MultiplicityElement = Class(name="Classes_Kernel_MultiplicityElement", is_abstract=True)
ValueSpecification = Class(name="ValueSpecification")
Classes_Kernel_ValueSpecification = Class(name="Classes_Kernel_ValueSpecification", is_abstract=True)
Kernel_TypedElement = Class(name="Kernel_TypedElement")
MultiplicityElement = Class(name="MultiplicityElement")
Classes_Kernel_Slot = Class(name="Classes_Kernel_Slot")
StructuralFeature = Class(name="StructuralFeature")
Classes_Kernel_RedefinableElement = Class(name="Classes_Kernel_RedefinableElement", is_abstract=True)
RedefinableElement = Class(name="RedefinableElement")
Classes_Kernel_Classifier = Class(name="Classes_Kernel_Classifier", is_abstract=True)
Kernel_RedefinableElement = Class(name="Kernel_RedefinableElement")
Kernel_Type = Class(name="Kernel_Type")
Feature = Class(name="Feature")
Property_ = Class(name="Property")
Classes_Kernel_LiteralReal = Class(name="Classes_Kernel_LiteralReal")
Classes_Kernel_LiteralString = Class(name="Classes_Kernel_LiteralString")
Classes_Kernel_LiteralUnilimitedNatural = Class(name="Classes_Kernel_LiteralUnilimitedNatural")
Classes_Kernel_InstanceValue = Class(name="Classes_Kernel_InstanceValue")
Classes_Kernel_InstanceSpecification = Class(name="Classes_Kernel_InstanceSpecification")
Classifier = Class(name="Classifier")
Classes_Kernel_Constraint = Class(name="Classes_Kernel_Constraint")
Kernel_MultiplicityElement = Class(name="Kernel_MultiplicityElement")
Classes_Kernel_Property = Class(name="Classes_Kernel_Property")
Class_ = Class(name="Class")
Association = Class(name="Association")
Generalization_ = Class(name="Generalization_")
Substitution = Class(name="Substitution")
GeneralizationSet = Class(name="GeneralizationSet")
Classes_Kernel_Feature = Class(name="Classes_Kernel_Feature", is_abstract=True)
Classes_Kernel_StructuralFeature = Class(name="Classes_Kernel_StructuralFeature", is_abstract=True)
Kernel_Feature = Class(name="Kernel_Feature")
Classes_Kernel_Parameter = Class(name="Classes_Kernel_Parameter")
TypedElement = Class(name="TypedElement")
BehavioralFeature = Class(name="BehavioralFeature")
Classes_Kernel_Operation = Class(name="Classes_Kernel_Operation")
DataType = Class(name="DataType")
Interface = Class(name="Interface")
Classes_Kernel_Generalization = Class(name="Classes_Kernel_Generalization_")
Classes_Kernel_BehavioralFeature = Class(name="Classes_Kernel_BehavioralFeature", is_abstract=True)
Parameter_ = Class(name="Parameter")
Classes_Kernel_DataType = Class(name="Classes_Kernel_DataType")
Classes_Kernel_PrimitiveType = Class(name="Classes_Kernel_PrimitiveType")
Classes_Kernel_Enumeration = Class(name="Classes_Kernel_Enumeration")
EnumerationLiteral = Class(name="EnumerationLiteral")
Classes_Kernel_EnumerationLiteral = Class(name="Classes_Kernel_EnumerationLiteral")
Enumeration_ = Class(name="Enumeration")
Classes_Kernel_PackageMerge = Class(name="Classes_Kernel_PackageMerge")
Classes_Kernel_Class = Class(name="Classes_Kernel_Class")
Operation = Class(name="Operation")
Classes_Kernel_Association = Class(name="Classes_Kernel_Association")
Kernel_Relationship = Class(name="Kernel_Relationship")
Kernel_Classifier = Class(name="Kernel_Classifier")
Classes_Interfaces_InterfaceRealization = Class(name="Classes_Interfaces_InterfaceRealization")
BehavioredClassifier = Class(name="BehavioredClassifier")
Classes_Interfaces_BehavioredClassifier = Class(name="Classes_Interfaces_BehavioredClassifier", is_abstract=True)
InterfaceRealization = Class(name="InterfaceRealization")
Classes_AssociationClasses_AssociationClass = Class(name="Classes_AssociationClasses_AssociationClass")
Kernel_Class = Class(name="Kernel_Class")
Kernel_Association = Class(name="Kernel_Association")
Classes_PowerTypes_GeneralizationSet = Class(name="Classes_PowerTypes_GeneralizationSet")
Classes_Dependencies_Dependency = Class(name="Classes_Dependencies_Dependency")
Kernel_DirectedRelationship = Class(name="Kernel_DirectedRelationship")
Classes_Dependencies_Usage = Class(name="Classes_Dependencies_Usage")
Classes_Dependencies_Abstraction = Class(name="Classes_Dependencies_Abstraction")
OpaqueExpression = Class(name="OpaqueExpression")
Classes_Dependencies_Realization = Class(name="Classes_Dependencies_Realization")
Abstraction = Class(name="Abstraction")
Classes_Dependencies_Substitution = Class(name="Classes_Dependencies_Substitution")
Realization = Class(name="Realization")
Classes_Interfaces_Interface = Class(name="Classes_Interfaces_Interface")

# Classes_Kernel_Element class attributes and methods

# Comment class attributes and methods

# Element class attributes and methods

# Classes_Kernel_NamedElement class attributes and methods
Classes_Kernel_NamedElement_name: Property = Property(name="name", type=StringType)
Classes_Kernel_NamedElement_qualifiedName: Property = Property(name="qualifiedName", type=StringType)
Classes_Kernel_NamedElement_visibility: Property = Property(name="visibility", type=StringType)
Classes_Kernel_NamedElement.attributes={Classes_Kernel_NamedElement_qualifiedName, Classes_Kernel_NamedElement_name, Classes_Kernel_NamedElement_visibility}

# Namespace class attributes and methods

# Dependency class attributes and methods

# Classes_Kernel_Namespace class attributes and methods

# NamedElement class attributes and methods

# PackageableElement class attributes and methods

# Package class attributes and methods

# Classes_Kernel_Package class attributes and methods
Classes_Kernel_Package_URI: Property = Property(name="URI", type=StringType)
Classes_Kernel_Package.attributes={Classes_Kernel_Package_URI}

# Kernel_Namespace class attributes and methods

# Kernel_PackageableElement class attributes and methods

# Type class attributes and methods

# PackageMerge class attributes and methods

# Classes_Kernel_Comment class attributes and methods
Classes_Kernel_Comment_body: Property = Property(name="body", type=StringType)
Classes_Kernel_Comment.attributes={Classes_Kernel_Comment_body}

# Classes_Kernel_Relationship class attributes and methods

# ElementImport class attributes and methods

# PackageImport class attributes and methods

# Constraint class attributes and methods

# Classes_Kernel_PackageableElement class attributes and methods

# Classes_Kernel_ElementImport class attributes and methods
Classes_Kernel_ElementImport_visibility: Property = Property(name="visibility", type=StringType)
Classes_Kernel_ElementImport_alias: Property = Property(name="alias", type=StringType)
Classes_Kernel_ElementImport.attributes={Classes_Kernel_ElementImport_alias, Classes_Kernel_ElementImport_visibility}

# DirectedRelationship class attributes and methods

# Classes_Kernel_PackageImport class attributes and methods
Classes_Kernel_PackageImport_visibility: Property = Property(name="visibility", type=StringType)
Classes_Kernel_PackageImport.attributes={Classes_Kernel_PackageImport_visibility}

# Slot class attributes and methods

# InstanceSpecification class attributes and methods

# Classes_Kernel_TypedElement class attributes and methods

# Classes_Kernel_Type class attributes and methods

# Classes_Kernel_Expression class attributes and methods
Classes_Kernel_Expression_symbol: Property = Property(name="symbol", type=StringType)
Classes_Kernel_Expression.attributes={Classes_Kernel_Expression_symbol}

# Classes_Kernel_OpaqueExpression class attributes and methods
Classes_Kernel_OpaqueExpression_body: Property = Property(name="body", type=StringType)
Classes_Kernel_OpaqueExpression_language: Property = Property(name="language", type=StringType)
Classes_Kernel_OpaqueExpression.attributes={Classes_Kernel_OpaqueExpression_body, Classes_Kernel_OpaqueExpression_language}

# Classes_Kernel_LiteralSpecification class attributes and methods

# Classes_Kernel_LiteralNull class attributes and methods

# LiteralSpecification class attributes and methods

# Classes_Kernel_LiteralBoolean class attributes and methods

# Classes_Kernel_LiteralInteger class attributes and methods

# Classes_Kernel_DirectedRelationship class attributes and methods

# Relationship class attributes and methods

# Classes_Kernel_MultiplicityElement class attributes and methods
Classes_Kernel_MultiplicityElement_isOrdered: Property = Property(name="isOrdered", type=BooleanType)
Classes_Kernel_MultiplicityElement_isUnique: Property = Property(name="isUnique", type=BooleanType)
Classes_Kernel_MultiplicityElement_upper: Property = Property(name="upper", type=IntegerType)
Classes_Kernel_MultiplicityElement_lower: Property = Property(name="lower", type=IntegerType)
Classes_Kernel_MultiplicityElement.attributes={Classes_Kernel_MultiplicityElement_upper, Classes_Kernel_MultiplicityElement_lower, Classes_Kernel_MultiplicityElement_isUnique, Classes_Kernel_MultiplicityElement_isOrdered}

# ValueSpecification class attributes and methods

# Classes_Kernel_ValueSpecification class attributes and methods

# Kernel_TypedElement class attributes and methods

# MultiplicityElement class attributes and methods

# Classes_Kernel_Slot class attributes and methods

# StructuralFeature class attributes and methods

# Classes_Kernel_RedefinableElement class attributes and methods
Classes_Kernel_RedefinableElement_isLeaf: Property = Property(name="isLeaf", type=BooleanType)
Classes_Kernel_RedefinableElement.attributes={Classes_Kernel_RedefinableElement_isLeaf}

# RedefinableElement class attributes and methods

# Classes_Kernel_Classifier class attributes and methods
Classes_Kernel_Classifier_isAbstract: Property = Property(name="isAbstract", type=BooleanType)
Classes_Kernel_Classifier_isFinalSpecialization: Property = Property(name="isFinalSpecialization", type=BooleanType)
Classes_Kernel_Classifier.attributes={Classes_Kernel_Classifier_isAbstract, Classes_Kernel_Classifier_isFinalSpecialization}

# Kernel_RedefinableElement class attributes and methods

# Kernel_Type class attributes and methods

# Feature class attributes and methods

# Property class attributes and methods

# Classes_Kernel_LiteralReal class attributes and methods

# Classes_Kernel_LiteralString class attributes and methods

# Classes_Kernel_LiteralUnilimitedNatural class attributes and methods

# Classes_Kernel_InstanceValue class attributes and methods

# Classes_Kernel_InstanceSpecification class attributes and methods

# Classifier class attributes and methods

# Classes_Kernel_Constraint class attributes and methods

# Kernel_MultiplicityElement class attributes and methods

# Classes_Kernel_Property class attributes and methods
Classes_Kernel_Property_isDerived: Property = Property(name="isDerived", type=BooleanType)
Classes_Kernel_Property_isDerivedUnion: Property = Property(name="isDerivedUnion", type=BooleanType)
Classes_Kernel_Property_default: Property = Property(name="default", type=StringType)
Classes_Kernel_Property_isComposite: Property = Property(name="isComposite", type=BooleanType)
Classes_Kernel_Property_isID: Property = Property(name="isID", type=BooleanType)
Classes_Kernel_Property_aggregation: Property = Property(name="aggregation", type=StringType)
Classes_Kernel_Property.attributes={Classes_Kernel_Property_aggregation, Classes_Kernel_Property_default, Classes_Kernel_Property_isDerivedUnion, Classes_Kernel_Property_isID, Classes_Kernel_Property_isDerived, Classes_Kernel_Property_isComposite}

# Class class attributes and methods

# Association class attributes and methods

# Generalization_ class attributes and methods

# Substitution class attributes and methods

# GeneralizationSet class attributes and methods

# Classes_Kernel_Feature class attributes and methods
Classes_Kernel_Feature_isStatic: Property = Property(name="isStatic", type=BooleanType)
Classes_Kernel_Feature.attributes={Classes_Kernel_Feature_isStatic}

# Classes_Kernel_StructuralFeature class attributes and methods
Classes_Kernel_StructuralFeature_isReadOnly: Property = Property(name="isReadOnly", type=BooleanType)
Classes_Kernel_StructuralFeature.attributes={Classes_Kernel_StructuralFeature_isReadOnly}

# Kernel_Feature class attributes and methods

# Classes_Kernel_Parameter class attributes and methods
Classes_Kernel_Parameter_default: Property = Property(name="default", type=StringType)
Classes_Kernel_Parameter.attributes={Classes_Kernel_Parameter_default}

# TypedElement class attributes and methods

# BehavioralFeature class attributes and methods

# Classes_Kernel_Operation class attributes and methods
Classes_Kernel_Operation_isQuery: Property = Property(name="isQuery", type=BooleanType)
Classes_Kernel_Operation_isOrdered: Property = Property(name="isOrdered", type=BooleanType)
Classes_Kernel_Operation_isUnique: Property = Property(name="isUnique", type=BooleanType)
Classes_Kernel_Operation_upper: Property = Property(name="upper", type=IntegerType)
Classes_Kernel_Operation_lower: Property = Property(name="lower", type=IntegerType)
Classes_Kernel_Operation.attributes={Classes_Kernel_Operation_upper, Classes_Kernel_Operation_isOrdered, Classes_Kernel_Operation_lower, Classes_Kernel_Operation_isQuery, Classes_Kernel_Operation_isUnique}

# DataType class attributes and methods

# Interface class attributes and methods

# Classes_Kernel_Generalization class attributes and methods
Classes_Kernel_Generalization_isSubstitutable: Property = Property(name="isSubstitutable", type=BooleanType)
Classes_Kernel_Generalization.attributes={Classes_Kernel_Generalization_isSubstitutable}

# Classes_Kernel_BehavioralFeature class attributes and methods

# Parameter class attributes and methods

# Classes_Kernel_DataType class attributes and methods

# Classes_Kernel_PrimitiveType class attributes and methods

# Classes_Kernel_Enumeration class attributes and methods

# EnumerationLiteral class attributes and methods

# Classes_Kernel_EnumerationLiteral class attributes and methods

# Enumeration class attributes and methods

# Classes_Kernel_PackageMerge class attributes and methods

# Classes_Kernel_Class class attributes and methods

# Operation class attributes and methods

# Classes_Kernel_Association class attributes and methods
Classes_Kernel_Association_isDerived: Property = Property(name="isDerived", type=BooleanType)
Classes_Kernel_Association.attributes={Classes_Kernel_Association_isDerived}

# Kernel_Relationship class attributes and methods

# Kernel_Classifier class attributes and methods

# Classes_Interfaces_InterfaceRealization class attributes and methods

# BehavioredClassifier class attributes and methods

# Classes_Interfaces_BehavioredClassifier class attributes and methods

# InterfaceRealization class attributes and methods

# Classes_AssociationClasses_AssociationClass class attributes and methods

# Kernel_Class class attributes and methods

# Kernel_Association class attributes and methods

# Classes_PowerTypes_GeneralizationSet class attributes and methods
Classes_PowerTypes_GeneralizationSet_isCovering: Property = Property(name="isCovering", type=BooleanType)
Classes_PowerTypes_GeneralizationSet_isDisjoint: Property = Property(name="isDisjoint", type=BooleanType)
Classes_PowerTypes_GeneralizationSet.attributes={Classes_PowerTypes_GeneralizationSet_isCovering, Classes_PowerTypes_GeneralizationSet_isDisjoint}

# Classes_Dependencies_Dependency class attributes and methods

# Kernel_DirectedRelationship class attributes and methods

# Classes_Dependencies_Usage class attributes and methods

# Classes_Dependencies_Abstraction class attributes and methods

# OpaqueExpression class attributes and methods

# Classes_Dependencies_Realization class attributes and methods

# Abstraction class attributes and methods

# Classes_Dependencies_Substitution class attributes and methods

# Realization class attributes and methods

# Classes_Interfaces_Interface class attributes and methods

# Relationships
ownedComment0: BinaryAssociation = BinaryAssociation(
    name="ownedComment0",
    ends={
        Property(name="Comment", type=Classes_Kernel_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="owningElement", type=Comment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedElement1: BinaryAssociation = BinaryAssociation(
    name="ownedElement1",
    ends={
        Property(name="Element", type=Classes_Kernel_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=Element, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owner2: BinaryAssociation = BinaryAssociation(
    name="owner2",
    ends={
        Property(name="Element3", type=Classes_Kernel_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedElement", type=Element, multiplicity=Multiplicity(0, 1))
    }
)
namespace4: BinaryAssociation = BinaryAssociation(
    name="namespace4",
    ends={
        Property(name="Namespace", type=Classes_Kernel_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedMember", type=Namespace, multiplicity=Multiplicity(0, 1))
    }
)
clientDependency5: BinaryAssociation = BinaryAssociation(
    name="clientDependency5",
    ends={
        Property(name="Dependency", type=Classes_Kernel_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="client", type=Dependency, multiplicity=Multiplicity(0, 9999))
    }
)
importedMember6: BinaryAssociation = BinaryAssociation(
    name="importedMember6",
    ends={
        Property(name="PackageableElement", type=Classes_Kernel_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Kernel_Namespace", type=PackageableElement, multiplicity=Multiplicity(0, 9999))
    }
)
importedPackage19: BinaryAssociation = BinaryAssociation(
    name="importedPackage19",
    ends={
        Property(name="Package", type=Classes_Kernel_PackageImport, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Kernel_PackageImport", type=Package, multiplicity=Multiplicity(1, 1))
    }
)
importingNamespace20: BinaryAssociation = BinaryAssociation(
    name="importingNamespace20",
    ends={
        Property(name="Namespace21", type=Classes_Kernel_PackageImport, multiplicity=Multiplicity(1, 1)),
        Property(name="packageImport", type=Namespace, multiplicity=Multiplicity(1, 1))
    }
)
nestedPackage22: BinaryAssociation = BinaryAssociation(
    name="nestedPackage22",
    ends={
        Property(name="Package23", type=Classes_Kernel_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="nestingPackage", type=Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nestingPackage24: BinaryAssociation = BinaryAssociation(
    name="nestingPackage24",
    ends={
        Property(name="Package25", type=Classes_Kernel_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="nestedPackage", type=Package, multiplicity=Multiplicity(0, 1))
    }
)
packagedElement26: BinaryAssociation = BinaryAssociation(
    name="packagedElement26",
    ends={
        Property(name="PackageableElement27", type=Classes_Kernel_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Kernel_Package", type=PackageableElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedType28: BinaryAssociation = BinaryAssociation(
    name="ownedType28",
    ends={
        Property(name="Type", type=Classes_Kernel_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="package", type=Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packageMerge29: BinaryAssociation = BinaryAssociation(
    name="packageMerge29",
    ends={
        Property(name="PackageMerge", type=Classes_Kernel_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="receivingPackage", type=PackageMerge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningElement30: BinaryAssociation = BinaryAssociation(
    name="owningElement30",
    ends={
        Property(name="Element31", type=Classes_Kernel_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedComment", type=Element, multiplicity=Multiplicity(0, 1))
    }
)
annotatedElement32: BinaryAssociation = BinaryAssociation(
    name="annotatedElement32",
    ends={
        Property(name="Element33", type=Classes_Kernel_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Kernel_Comment", type=Element, multiplicity=Multiplicity(0, 9999))
    }
)
member7: BinaryAssociation = BinaryAssociation(
    name="member7",
    ends={
        Property(name="NamedElement", type=Classes_Kernel_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Kernel_Namespace8", type=NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
ownedMember9: BinaryAssociation = BinaryAssociation(
    name="ownedMember9",
    ends={
        Property(name="NamedElement10", type=Classes_Kernel_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="namespace", type=NamedElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elementImport11: BinaryAssociation = BinaryAssociation(
    name="elementImport11",
    ends={
        Property(name="ElementImport", type=Classes_Kernel_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="importingNamespace", type=ElementImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packageImport12: BinaryAssociation = BinaryAssociation(
    name="packageImport12",
    ends={
        Property(name="PackageImport", type=Classes_Kernel_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="importingNamespace13", type=PackageImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedRule14: BinaryAssociation = BinaryAssociation(
    name="ownedRule14",
    ends={
        Property(name="Constraint", type=Classes_Kernel_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="context", type=Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
importedElement15: BinaryAssociation = BinaryAssociation(
    name="importedElement15",
    ends={
        Property(name="PackageableElement16", type=Classes_Kernel_ElementImport, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Kernel_ElementImport", type=PackageableElement, multiplicity=Multiplicity(1, 1))
    }
)
importingNamespace17: BinaryAssociation = BinaryAssociation(
    name="importingNamespace17",
    ends={
        Property(name="Namespace18", type=Classes_Kernel_ElementImport, multiplicity=Multiplicity(1, 1)),
        Property(name="elementImport", type=Namespace, multiplicity=Multiplicity(1, 1))
    }
)
owningLower45: BinaryAssociation = BinaryAssociation(
    name="owningLower45",
    ends={
        Property(name="MultiplicityElement46", type=Classes_Kernel_ValueSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="lowerValue", type=MultiplicityElement, multiplicity=Multiplicity(0, 1))
    }
)
owningConstraint47: BinaryAssociation = BinaryAssociation(
    name="owningConstraint47",
    ends={
        Property(name="Constraint48", type=Classes_Kernel_ValueSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="specification", type=Constraint, multiplicity=Multiplicity(0, 1))
    }
)
owningSlot49: BinaryAssociation = BinaryAssociation(
    name="owningSlot49",
    ends={
        Property(name="Slot", type=Classes_Kernel_ValueSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="value", type=Slot, multiplicity=Multiplicity(0, 1))
    }
)
owningInstanceSpec50: BinaryAssociation = BinaryAssociation(
    name="owningInstanceSpec50",
    ends={
        Property(name="InstanceSpecification", type=Classes_Kernel_ValueSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="specification51", type=InstanceSpecification, multiplicity=Multiplicity(0, 1))
    }
)
type52: BinaryAssociation = BinaryAssociation(
    name="type52",
    ends={
        Property(name="Type53", type=Classes_Kernel_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Kernel_TypedElement", type=Type, multiplicity=Multiplicity(0, 1))
    }
)
package54: BinaryAssociation = BinaryAssociation(
    name="package54",
    ends={
        Property(name="Package55", type=Classes_Kernel_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedType", type=Package, multiplicity=Multiplicity(0, 1))
    }
)
operand56: BinaryAssociation = BinaryAssociation(
    name="operand56",
    ends={
        Property(name="ValueSpecification57", type=Classes_Kernel_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Kernel_Expression", type=ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
relatedElement34: BinaryAssociation = BinaryAssociation(
    name="relatedElement34",
    ends={
        Property(name="Element35", type=Classes_Kernel_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Kernel_Relationship", type=Element, multiplicity=Multiplicity(1, 9999))
    }
)
target36: BinaryAssociation = BinaryAssociation(
    name="target36",
    ends={
        Property(name="Element37", type=Classes_Kernel_DirectedRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Kernel_DirectedRelationship", type=Element, multiplicity=Multiplicity(1, 9999))
    }
)
source38: BinaryAssociation = BinaryAssociation(
    name="source38",
    ends={
        Property(name="Element40", type=Classes_Kernel_DirectedRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Kernel_DirectedRelationship39", type=Element, multiplicity=Multiplicity(1, 9999))
    }
)
upperValue41: BinaryAssociation = BinaryAssociation(
    name="upperValue41",
    ends={
        Property(name="ValueSpecification", type=Classes_Kernel_MultiplicityElement, multiplicity=Multiplicity(1, 1)),
        Property(name="owningUpper", type=ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lowerValue42: BinaryAssociation = BinaryAssociation(
    name="lowerValue42",
    ends={
        Property(name="ValueSpecification43", type=Classes_Kernel_MultiplicityElement, multiplicity=Multiplicity(1, 1)),
        Property(name="owningLower", type=ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
owningUpper44: BinaryAssociation = BinaryAssociation(
    name="owningUpper44",
    ends={
        Property(name="MultiplicityElement", type=Classes_Kernel_ValueSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="upperValue", type=MultiplicityElement, multiplicity=Multiplicity(0, 1))
    }
)
owningInstace71: BinaryAssociation = BinaryAssociation(
    name="owningInstace71",
    ends={
        Property(name="InstanceSpecification72", type=Classes_Kernel_Slot, multiplicity=Multiplicity(1, 1)),
        Property(name="slot", type=InstanceSpecification, multiplicity=Multiplicity(1, 1))
    }
)
value73: BinaryAssociation = BinaryAssociation(
    name="value73",
    ends={
        Property(name="ValueSpecification74", type=Classes_Kernel_Slot, multiplicity=Multiplicity(1, 1)),
        Property(name="owningSlot", type=ValueSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
definingFeature75: BinaryAssociation = BinaryAssociation(
    name="definingFeature75",
    ends={
        Property(name="StructuralFeature", type=Classes_Kernel_Slot, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Kernel_Slot", type=StructuralFeature, multiplicity=Multiplicity(1, 1))
    }
)
redefinedElement76: BinaryAssociation = BinaryAssociation(
    name="redefinedElement76",
    ends={
        Property(name="RedefinableElement", type=Classes_Kernel_RedefinableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Kernel_RedefinableElement", type=RedefinableElement, multiplicity=Multiplicity(0, 9999))
    }
)
redefinitionContext77: BinaryAssociation = BinaryAssociation(
    name="redefinitionContext77",
    ends={
        Property(name="Classifier79", type=Classes_Kernel_RedefinableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Kernel_RedefinableElement78", type=Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
inheritedMember80: BinaryAssociation = BinaryAssociation(
    name="inheritedMember80",
    ends={
        Property(name="NamedElement81", type=Classes_Kernel_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Kernel_Classifier", type=NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
feature82: BinaryAssociation = BinaryAssociation(
    name="feature82",
    ends={
        Property(name="Feature", type=Classes_Kernel_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="featuringClassifier", type=Feature, multiplicity=Multiplicity(0, 9999))
    }
)
attribute83: BinaryAssociation = BinaryAssociation(
    name="attribute83",
    ends={
        Property(name="Property", type=Classes_Kernel_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Kernel_Classifier84", type=Property_, multiplicity=Multiplicity(0, 9999))
    }
)
instance58: BinaryAssociation = BinaryAssociation(
    name="instance58",
    ends={
        Property(name="InstanceSpecification59", type=Classes_Kernel_InstanceValue, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Kernel_InstanceValue", type=InstanceSpecification, multiplicity=Multiplicity(1, 1))
    }
)
slot60: BinaryAssociation = BinaryAssociation(
    name="slot60",
    ends={
        Property(name="Slot61", type=Classes_Kernel_InstanceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="owningInstace", type=Slot, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specification62: BinaryAssociation = BinaryAssociation(
    name="specification62",
    ends={
        Property(name="ValueSpecification63", type=Classes_Kernel_InstanceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="owningInstanceSpec", type=ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
classifier64: BinaryAssociation = BinaryAssociation(
    name="classifier64",
    ends={
        Property(name="Classifier", type=Classes_Kernel_InstanceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Kernel_InstanceSpecification", type=Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
context65: BinaryAssociation = BinaryAssociation(
    name="context65",
    ends={
        Property(name="Namespace66", type=Classes_Kernel_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedRule", type=Namespace, multiplicity=Multiplicity(0, 1))
    }
)
constrainedElement67: BinaryAssociation = BinaryAssociation(
    name="constrainedElement67",
    ends={
        Property(name="Element68", type=Classes_Kernel_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Kernel_Constraint", type=Element, multiplicity=Multiplicity(0, 9999))
    }
)
specification69: BinaryAssociation = BinaryAssociation(
    name="specification69",
    ends={
        Property(name="ValueSpecification70", type=Classes_Kernel_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="owningConstraint", type=ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
class_96: BinaryAssociation = BinaryAssociation(
    name="class_96",
    ends={
        Property(name="Class", type=Classes_Kernel_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedAttribute", type=Class_, multiplicity=Multiplicity(0, 1))
    }
)
redefinedProperty97: BinaryAssociation = BinaryAssociation(
    name="redefinedProperty97",
    ends={
        Property(name="Property98", type=Classes_Kernel_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Kernel_Property", type=Property_, multiplicity=Multiplicity(0, 9999))
    }
)
defaultValue99: BinaryAssociation = BinaryAssociation(
    name="defaultValue99",
    ends={
        Property(name="ValueSpecification101", type=Classes_Kernel_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Kernel_Property100", type=ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
opposite102: BinaryAssociation = BinaryAssociation(
    name="opposite102",
    ends={
        Property(name="Property104", type=Classes_Kernel_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Kernel_Property103", type=Property_, multiplicity=Multiplicity(0, 1))
    }
)
subsettedProperty105: BinaryAssociation = BinaryAssociation(
    name="subsettedProperty105",
    ends={
        Property(name="Property107", type=Classes_Kernel_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Kernel_Property106", type=Property_, multiplicity=Multiplicity(0, 1))
    }
)
association108: BinaryAssociation = BinaryAssociation(
    name="association108",
    ends={
        Property(name="Association", type=Classes_Kernel_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="memberEnd", type=Association, multiplicity=Multiplicity(0, 1))
    }
)
owningAssociation109: BinaryAssociation = BinaryAssociation(
    name="owningAssociation109",
    ends={
        Property(name="Association110", type=Classes_Kernel_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedEnd", type=Association, multiplicity=Multiplicity(0, 1))
    }
)
redefinedClassifier85: BinaryAssociation = BinaryAssociation(
    name="redefinedClassifier85",
    ends={
        Property(name="Classifier87", type=Classes_Kernel_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Kernel_Classifier86", type=Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
general88: BinaryAssociation = BinaryAssociation(
    name="general88",
    ends={
        Property(name="Classifier90", type=Classes_Kernel_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Kernel_Classifier89", type=Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
generalization91: BinaryAssociation = BinaryAssociation(
    name="generalization91",
    ends={
        Property(name="Generalization_", type=Classes_Kernel_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="specific", type=Generalization_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
substitution92: BinaryAssociation = BinaryAssociation(
    name="substitution92",
    ends={
        Property(name="Substitution", type=Classes_Kernel_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="substitutingClassifier", type=Substitution, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
powertypeExtent93: BinaryAssociation = BinaryAssociation(
    name="powertypeExtent93",
    ends={
        Property(name="GeneralizationSet", type=Classes_Kernel_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="powertype", type=GeneralizationSet, multiplicity=Multiplicity(0, 9999))
    }
)
featuringClassifier94: BinaryAssociation = BinaryAssociation(
    name="featuringClassifier94",
    ends={
        Property(name="Classifier95", type=Classes_Kernel_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="feature", type=Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
raisedException127: BinaryAssociation = BinaryAssociation(
    name="raisedException127",
    ends={
        Property(name="Type129", type=Classes_Kernel_BehavioralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Kernel_BehavioralFeature128", type=Type, multiplicity=Multiplicity(0, 1))
    }
)
ownedFormalParam130: BinaryAssociation = BinaryAssociation(
    name="ownedFormalParam130",
    ends={
        Property(name="BehavioralFeature", type=Classes_Kernel_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Kernel_Parameter", type=BehavioralFeature, multiplicity=Multiplicity(0, 1))
    }
)
defaultValue131: BinaryAssociation = BinaryAssociation(
    name="defaultValue131",
    ends={
        Property(name="ValueSpecification133", type=Classes_Kernel_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Kernel_Parameter132", type=ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type134: BinaryAssociation = BinaryAssociation(
    name="type134",
    ends={
        Property(name="Type135", type=Classes_Kernel_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Kernel_Operation", type=Type, multiplicity=Multiplicity(0, 1))
    }
)
precondition136: BinaryAssociation = BinaryAssociation(
    name="precondition136",
    ends={
        Property(name="Constraint138", type=Classes_Kernel_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Kernel_Operation137", type=Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bodyCondition139: BinaryAssociation = BinaryAssociation(
    name="bodyCondition139",
    ends={
        Property(name="Constraint141", type=Classes_Kernel_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Kernel_Operation140", type=Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
postcondition142: BinaryAssociation = BinaryAssociation(
    name="postcondition142",
    ends={
        Property(name="Constraint144", type=Classes_Kernel_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Kernel_Operation143", type=Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
class_145: BinaryAssociation = BinaryAssociation(
    name="class_145",
    ends={
        Property(name="Class146", type=Classes_Kernel_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedOperation", type=Class_, multiplicity=Multiplicity(0, 1))
    }
)
dataType147: BinaryAssociation = BinaryAssociation(
    name="dataType147",
    ends={
        Property(name="DataType149", type=Classes_Kernel_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedOperation148", type=DataType, multiplicity=Multiplicity(0, 1))
    }
)
dataType111: BinaryAssociation = BinaryAssociation(
    name="dataType111",
    ends={
        Property(name="DataType", type=Classes_Kernel_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedAttribute112", type=DataType, multiplicity=Multiplicity(0, 1))
    }
)
interface113: BinaryAssociation = BinaryAssociation(
    name="interface113",
    ends={
        Property(name="Interface", type=Classes_Kernel_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedAttribute114", type=Interface, multiplicity=Multiplicity(0, 1))
    }
)
qualifier115: BinaryAssociation = BinaryAssociation(
    name="qualifier115",
    ends={
        Property(name="Property116", type=Classes_Kernel_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="associationEnd", type=Property_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
associationEnd117: BinaryAssociation = BinaryAssociation(
    name="associationEnd117",
    ends={
        Property(name="Property118", type=Classes_Kernel_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="qualifier", type=Property_, multiplicity=Multiplicity(0, 1))
    }
)
general119: BinaryAssociation = BinaryAssociation(
    name="general119",
    ends={
        Property(name="Classifier120", type=Classes_Kernel_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Kernel_Generalization", type=Classifier, multiplicity=Multiplicity(1, 1))
    }
)
specific121: BinaryAssociation = BinaryAssociation(
    name="specific121",
    ends={
        Property(name="Classifier122", type=Classes_Kernel_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="generalization", type=Classifier, multiplicity=Multiplicity(1, 1))
    }
)
generalizationSet123: BinaryAssociation = BinaryAssociation(
    name="generalizationSet123",
    ends={
        Property(name="GeneralizationSet125", type=Classes_Kernel_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="generalization124", type=GeneralizationSet, multiplicity=Multiplicity(0, 9999))
    }
)
ownedParameter126: BinaryAssociation = BinaryAssociation(
    name="ownedParameter126",
    ends={
        Property(name="Parameter", type=Classes_Kernel_BehavioralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Kernel_BehavioralFeature", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
memberEnd164: BinaryAssociation = BinaryAssociation(
    name="memberEnd164",
    ends={
        Property(name="Property165", type=Classes_Kernel_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="association", type=Property_, multiplicity=Multiplicity(2, 9999))
    }
)
ownedEnd166: BinaryAssociation = BinaryAssociation(
    name="ownedEnd166",
    ends={
        Property(name="Property167", type=Classes_Kernel_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="owningAssociation", type=Property_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedAttribute168: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute168",
    ends={
        Property(name="Property169", type=Classes_Kernel_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="dataType", type=Property_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedOperation170: BinaryAssociation = BinaryAssociation(
    name="ownedOperation170",
    ends={
        Property(name="Operation172", type=Classes_Kernel_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="dataType171", type=Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedLiteral173: BinaryAssociation = BinaryAssociation(
    name="ownedLiteral173",
    ends={
        Property(name="EnumerationLiteral", type=Classes_Kernel_Enumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="enumeration", type=EnumerationLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enumeration174: BinaryAssociation = BinaryAssociation(
    name="enumeration174",
    ends={
        Property(name="Enumeration", type=Classes_Kernel_EnumerationLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedLiteral", type=Enumeration_, multiplicity=Multiplicity(1, 1))
    }
)
receivingPackage175: BinaryAssociation = BinaryAssociation(
    name="receivingPackage175",
    ends={
        Property(name="Package176", type=Classes_Kernel_PackageMerge, multiplicity=Multiplicity(1, 1)),
        Property(name="packageMerge", type=Package, multiplicity=Multiplicity(1, 1))
    }
)
interface150: BinaryAssociation = BinaryAssociation(
    name="interface150",
    ends={
        Property(name="Interface152", type=Classes_Kernel_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedOperation151", type=Interface, multiplicity=Multiplicity(0, 1))
    }
)
nestedClassifier153: BinaryAssociation = BinaryAssociation(
    name="nestedClassifier153",
    ends={
        Property(name="Classifier154", type=Classes_Kernel_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Kernel_Class", type=Classifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedOperation155: BinaryAssociation = BinaryAssociation(
    name="ownedOperation155",
    ends={
        Property(name="Operation", type=Classes_Kernel_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="class_", type=Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superClass156: BinaryAssociation = BinaryAssociation(
    name="superClass156",
    ends={
        Property(name="Class158", type=Classes_Kernel_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Kernel_Class157", type=Class_, multiplicity=Multiplicity(0, 9999))
    }
)
ownedAttribute159: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute159",
    ends={
        Property(name="Property161", type=Classes_Kernel_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="class_160", type=Property_, multiplicity=Multiplicity(0, 9999))
    }
)
navigableOwnedEnd162: BinaryAssociation = BinaryAssociation(
    name="navigableOwnedEnd162",
    ends={
        Property(name="Property163", type=Classes_Kernel_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Kernel_Association", type=Property_, multiplicity=Multiplicity(0, 9999))
    }
)
nestedClassifier188: BinaryAssociation = BinaryAssociation(
    name="nestedClassifier188",
    ends={
        Property(name="Classifier189", type=Classes_Interfaces_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Interfaces_Interface", type=Classifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
redefinedInterface190: BinaryAssociation = BinaryAssociation(
    name="redefinedInterface190",
    ends={
        Property(name="Interface192", type=Classes_Interfaces_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Interfaces_Interface191", type=Interface, multiplicity=Multiplicity(0, 9999))
    }
)
ownedAttribute193: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute193",
    ends={
        Property(name="Property194", type=Classes_Interfaces_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="interface", type=Property_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedOperation195: BinaryAssociation = BinaryAssociation(
    name="ownedOperation195",
    ends={
        Property(name="Operation197", type=Classes_Interfaces_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="interface196", type=Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
implementingClassifier198: BinaryAssociation = BinaryAssociation(
    name="implementingClassifier198",
    ends={
        Property(name="BehavioredClassifier", type=Classes_Interfaces_InterfaceRealization, multiplicity=Multiplicity(1, 1)),
        Property(name="interfaceRealization", type=BehavioredClassifier, multiplicity=Multiplicity(1, 1))
    }
)
contract199: BinaryAssociation = BinaryAssociation(
    name="contract199",
    ends={
        Property(name="Interface200", type=Classes_Interfaces_InterfaceRealization, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Interfaces_InterfaceRealization", type=Interface, multiplicity=Multiplicity(1, 1))
    }
)
interfaceRealization201: BinaryAssociation = BinaryAssociation(
    name="interfaceRealization201",
    ends={
        Property(name="InterfaceRealization", type=Classes_Interfaces_BehavioredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="implementingClassifier", type=InterfaceRealization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
powertype202: BinaryAssociation = BinaryAssociation(
    name="powertype202",
    ends={
        Property(name="Classifier203", type=Classes_PowerTypes_GeneralizationSet, multiplicity=Multiplicity(1, 1)),
        Property(name="powertypeExtent", type=Classifier, multiplicity=Multiplicity(0, 1))
    }
)
mergedPackage177: BinaryAssociation = BinaryAssociation(
    name="mergedPackage177",
    ends={
        Property(name="Package178", type=Classes_Kernel_PackageMerge, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Kernel_PackageMerge", type=Package, multiplicity=Multiplicity(1, 1))
    }
)
client179: BinaryAssociation = BinaryAssociation(
    name="client179",
    ends={
        Property(name="NamedElement180", type=Classes_Dependencies_Dependency, multiplicity=Multiplicity(1, 1)),
        Property(name="clientDependency", type=NamedElement, multiplicity=Multiplicity(1, 9999))
    }
)
supplier181: BinaryAssociation = BinaryAssociation(
    name="supplier181",
    ends={
        Property(name="NamedElement182", type=Classes_Dependencies_Dependency, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Dependencies_Dependency", type=NamedElement, multiplicity=Multiplicity(1, 9999))
    }
)
mapping183: BinaryAssociation = BinaryAssociation(
    name="mapping183",
    ends={
        Property(name="OpaqueExpression", type=Classes_Dependencies_Abstraction, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Dependencies_Abstraction", type=OpaqueExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
substitutingClassifier184: BinaryAssociation = BinaryAssociation(
    name="substitutingClassifier184",
    ends={
        Property(name="Classifier185", type=Classes_Dependencies_Substitution, multiplicity=Multiplicity(1, 1)),
        Property(name="substitution", type=Classifier, multiplicity=Multiplicity(1, 1))
    }
)
contract186: BinaryAssociation = BinaryAssociation(
    name="contract186",
    ends={
        Property(name="Classifier187", type=Classes_Dependencies_Substitution, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Dependencies_Substitution", type=Classifier, multiplicity=Multiplicity(1, 1))
    }
)
generalization204: BinaryAssociation = BinaryAssociation(
    name="generalization204",
    ends={
        Property(name="Generalization205", type=Classes_PowerTypes_GeneralizationSet, multiplicity=Multiplicity(1, 1)),
        Property(name="generalizationSet", type=Generalization_, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_Classes_Kernel_NamedElement_Element = Generalization(general=Element, specific=Classes_Kernel_NamedElement)
gen_Classes_Kernel_Namespace_NamedElement = Generalization(general=NamedElement, specific=Classes_Kernel_Namespace)
gen_Classes_Kernel_Package_Kernel_Namespace = Generalization(general=Kernel_Namespace, specific=Classes_Kernel_Package)
gen_Classes_Kernel_Package_Kernel_PackageableElement = Generalization(general=Kernel_PackageableElement, specific=Classes_Kernel_Package)
gen_Classes_Kernel_Comment_Element = Generalization(general=Element, specific=Classes_Kernel_Comment)
gen_Classes_Kernel_Relationship_Element = Generalization(general=Element, specific=Classes_Kernel_Relationship)
gen_Classes_Kernel_PackageableElement_NamedElement = Generalization(general=NamedElement, specific=Classes_Kernel_PackageableElement)
gen_Classes_Kernel_ElementImport_DirectedRelationship = Generalization(general=DirectedRelationship, specific=Classes_Kernel_ElementImport)
gen_Classes_Kernel_PackageImport_DirectedRelationship = Generalization(general=DirectedRelationship, specific=Classes_Kernel_PackageImport)
gen_Classes_Kernel_TypedElement_NamedElement = Generalization(general=NamedElement, specific=Classes_Kernel_TypedElement)
gen_Classes_Kernel_Type_PackageableElement = Generalization(general=PackageableElement, specific=Classes_Kernel_Type)
gen_Classes_Kernel_Expression_ValueSpecification = Generalization(general=ValueSpecification, specific=Classes_Kernel_Expression)
gen_Classes_Kernel_OpaqueExpression_ValueSpecification = Generalization(general=ValueSpecification, specific=Classes_Kernel_OpaqueExpression)
gen_Classes_Kernel_LiteralSpecification_ValueSpecification = Generalization(general=ValueSpecification, specific=Classes_Kernel_LiteralSpecification)
gen_Classes_Kernel_LiteralNull_LiteralSpecification = Generalization(general=LiteralSpecification, specific=Classes_Kernel_LiteralNull)
gen_Classes_Kernel_LiteralBoolean_LiteralSpecification = Generalization(general=LiteralSpecification, specific=Classes_Kernel_LiteralBoolean)
gen_Classes_Kernel_LiteralInteger_LiteralSpecification = Generalization(general=LiteralSpecification, specific=Classes_Kernel_LiteralInteger)
gen_Classes_Kernel_DirectedRelationship_Relationship = Generalization(general=Relationship, specific=Classes_Kernel_DirectedRelationship)
gen_Classes_Kernel_MultiplicityElement_Element = Generalization(general=Element, specific=Classes_Kernel_MultiplicityElement)
gen_Classes_Kernel_ValueSpecification_Kernel_TypedElement = Generalization(general=Kernel_TypedElement, specific=Classes_Kernel_ValueSpecification)
gen_Classes_Kernel_ValueSpecification_Kernel_PackageableElement = Generalization(general=Kernel_PackageableElement, specific=Classes_Kernel_ValueSpecification)
gen_Classes_Kernel_Slot_Element = Generalization(general=Element, specific=Classes_Kernel_Slot)
gen_Classes_Kernel_RedefinableElement_NamedElement = Generalization(general=NamedElement, specific=Classes_Kernel_RedefinableElement)
gen_Classes_Kernel_Classifier_Kernel_RedefinableElement = Generalization(general=Kernel_RedefinableElement, specific=Classes_Kernel_Classifier)
gen_Classes_Kernel_Classifier_Kernel_Namespace = Generalization(general=Kernel_Namespace, specific=Classes_Kernel_Classifier)
gen_Classes_Kernel_Classifier_Kernel_Type = Generalization(general=Kernel_Type, specific=Classes_Kernel_Classifier)
gen_Classes_Kernel_LiteralReal_LiteralSpecification = Generalization(general=LiteralSpecification, specific=Classes_Kernel_LiteralReal)
gen_Classes_Kernel_LiteralString_LiteralSpecification = Generalization(general=LiteralSpecification, specific=Classes_Kernel_LiteralString)
gen_Classes_Kernel_LiteralUnilimitedNatural_LiteralSpecification = Generalization(general=LiteralSpecification, specific=Classes_Kernel_LiteralUnilimitedNatural)
gen_Classes_Kernel_InstanceSpecification_PackageableElement = Generalization(general=PackageableElement, specific=Classes_Kernel_InstanceSpecification)
gen_Classes_Kernel_Constraint_PackageableElement = Generalization(general=PackageableElement, specific=Classes_Kernel_Constraint)
gen_Classes_Kernel_StructuralFeature_Kernel_MultiplicityElement = Generalization(general=Kernel_MultiplicityElement, specific=Classes_Kernel_StructuralFeature)
gen_Classes_Kernel_StructuralFeature_Kernel_TypedElement = Generalization(general=Kernel_TypedElement, specific=Classes_Kernel_StructuralFeature)
gen_Classes_Kernel_Property_StructuralFeature = Generalization(general=StructuralFeature, specific=Classes_Kernel_Property)
gen_Classes_Kernel_Feature_RedefinableElement = Generalization(general=RedefinableElement, specific=Classes_Kernel_Feature)
gen_Classes_Kernel_StructuralFeature_Kernel_Feature = Generalization(general=Kernel_Feature, specific=Classes_Kernel_StructuralFeature)
gen_Classes_Kernel_Parameter_TypedElement = Generalization(general=TypedElement, specific=Classes_Kernel_Parameter)
gen_Classes_Kernel_Operation_BehavioralFeature = Generalization(general=BehavioralFeature, specific=Classes_Kernel_Operation)
gen_Classes_Kernel_Generalization_DirectedRelationship = Generalization(general=DirectedRelationship, specific=Classes_Kernel_Generalization)
gen_Classes_Kernel_BehavioralFeature_Kernel_Feature = Generalization(general=Kernel_Feature, specific=Classes_Kernel_BehavioralFeature)
gen_Classes_Kernel_BehavioralFeature_Kernel_Namespace = Generalization(general=Kernel_Namespace, specific=Classes_Kernel_BehavioralFeature)
gen_Classes_Kernel_DataType_Classifier = Generalization(general=Classifier, specific=Classes_Kernel_DataType)
gen_Classes_Kernel_PrimitiveType_DataType = Generalization(general=DataType, specific=Classes_Kernel_PrimitiveType)
gen_Classes_Kernel_Enumeration_DataType = Generalization(general=DataType, specific=Classes_Kernel_Enumeration)
gen_Classes_Kernel_EnumerationLiteral_InstanceSpecification = Generalization(general=InstanceSpecification, specific=Classes_Kernel_EnumerationLiteral)
gen_Classes_Kernel_PackageMerge_DirectedRelationship = Generalization(general=DirectedRelationship, specific=Classes_Kernel_PackageMerge)
gen_Classes_Kernel_Class_Classifier = Generalization(general=Classifier, specific=Classes_Kernel_Class)
gen_Classes_Kernel_Association_Kernel_Relationship = Generalization(general=Kernel_Relationship, specific=Classes_Kernel_Association)
gen_Classes_Kernel_Association_Kernel_Classifier = Generalization(general=Kernel_Classifier, specific=Classes_Kernel_Association)
gen_Classes_Interfaces_InterfaceRealization_Realization = Generalization(general=Realization, specific=Classes_Interfaces_InterfaceRealization)
gen_Classes_Interfaces_BehavioredClassifier_Classifier = Generalization(general=Classifier, specific=Classes_Interfaces_BehavioredClassifier)
gen_Classes_AssociationClasses_AssociationClass_Kernel_Class = Generalization(general=Kernel_Class, specific=Classes_AssociationClasses_AssociationClass)
gen_Classes_AssociationClasses_AssociationClass_Kernel_Association = Generalization(general=Kernel_Association, specific=Classes_AssociationClasses_AssociationClass)
gen_Classes_PowerTypes_GeneralizationSet_PackageableElement = Generalization(general=PackageableElement, specific=Classes_PowerTypes_GeneralizationSet)
gen_Classes_Dependencies_Dependency_Kernel_PackageableElement = Generalization(general=Kernel_PackageableElement, specific=Classes_Dependencies_Dependency)
gen_Classes_Dependencies_Dependency_Kernel_DirectedRelationship = Generalization(general=Kernel_DirectedRelationship, specific=Classes_Dependencies_Dependency)
gen_Classes_Dependencies_Usage_Dependency = Generalization(general=Dependency, specific=Classes_Dependencies_Usage)
gen_Classes_Dependencies_Abstraction_Dependency = Generalization(general=Dependency, specific=Classes_Dependencies_Abstraction)
gen_Classes_Dependencies_Realization_Abstraction = Generalization(general=Abstraction, specific=Classes_Dependencies_Realization)
gen_Classes_Dependencies_Substitution_Realization = Generalization(general=Realization, specific=Classes_Dependencies_Substitution)
gen_Classes_Interfaces_Interface_Classifier = Generalization(general=Classifier, specific=Classes_Interfaces_Interface)

# Domain Model
domain_model = DomainModel(
    name="Classes",
    types={Classes_Kernel_Element, Comment, Element, Classes_Kernel_NamedElement, Namespace, Dependency, Classes_Kernel_Namespace, NamedElement, PackageableElement, Package, Classes_Kernel_Package, Kernel_Namespace, Kernel_PackageableElement, Type, PackageMerge, Classes_Kernel_Comment, Classes_Kernel_Relationship, ElementImport, PackageImport, Constraint, Classes_Kernel_PackageableElement, Classes_Kernel_ElementImport, DirectedRelationship, Classes_Kernel_PackageImport, Slot, InstanceSpecification, Classes_Kernel_TypedElement, Classes_Kernel_Type, Classes_Kernel_Expression, Classes_Kernel_OpaqueExpression, Classes_Kernel_LiteralSpecification, Classes_Kernel_LiteralNull, LiteralSpecification, Classes_Kernel_LiteralBoolean, Classes_Kernel_LiteralInteger, Classes_Kernel_DirectedRelationship, Relationship, Classes_Kernel_MultiplicityElement, ValueSpecification, Classes_Kernel_ValueSpecification, Kernel_TypedElement, MultiplicityElement, Classes_Kernel_Slot, StructuralFeature, Classes_Kernel_RedefinableElement, RedefinableElement, Classes_Kernel_Classifier, Kernel_RedefinableElement, Kernel_Type, Feature, Property_, Classes_Kernel_LiteralReal, Classes_Kernel_LiteralString, Classes_Kernel_LiteralUnilimitedNatural, Classes_Kernel_InstanceValue, Classes_Kernel_InstanceSpecification, Classifier, Classes_Kernel_Constraint, Kernel_MultiplicityElement, Classes_Kernel_Property, Class_, Association, Generalization_, Substitution, GeneralizationSet, Classes_Kernel_Feature, Classes_Kernel_StructuralFeature, Kernel_Feature, Classes_Kernel_Parameter, TypedElement, BehavioralFeature, Classes_Kernel_Operation, DataType, Interface, Classes_Kernel_Generalization, Classes_Kernel_BehavioralFeature, Parameter_, Classes_Kernel_DataType, Classes_Kernel_PrimitiveType, Classes_Kernel_Enumeration, EnumerationLiteral, Classes_Kernel_EnumerationLiteral, Enumeration_, Classes_Kernel_PackageMerge, Classes_Kernel_Class, Operation, Classes_Kernel_Association, Kernel_Relationship, Kernel_Classifier, Classes_Interfaces_InterfaceRealization, BehavioredClassifier, Classes_Interfaces_BehavioredClassifier, InterfaceRealization, Classes_AssociationClasses_AssociationClass, Kernel_Class, Kernel_Association, Classes_PowerTypes_GeneralizationSet, Classes_Dependencies_Dependency, Kernel_DirectedRelationship, Classes_Dependencies_Usage, Classes_Dependencies_Abstraction, OpaqueExpression, Classes_Dependencies_Realization, Abstraction, Classes_Dependencies_Substitution, Realization, Classes_Interfaces_Interface, VisibilityKind, AggregationKind},
    associations={ownedComment0, ownedElement1, owner2, namespace4, clientDependency5, importedMember6, importedPackage19, importingNamespace20, nestedPackage22, nestingPackage24, packagedElement26, ownedType28, packageMerge29, owningElement30, annotatedElement32, member7, ownedMember9, elementImport11, packageImport12, ownedRule14, importedElement15, importingNamespace17, owningLower45, owningConstraint47, owningSlot49, owningInstanceSpec50, type52, package54, operand56, relatedElement34, target36, source38, upperValue41, lowerValue42, owningUpper44, owningInstace71, value73, definingFeature75, redefinedElement76, redefinitionContext77, inheritedMember80, feature82, attribute83, instance58, slot60, specification62, classifier64, context65, constrainedElement67, specification69, class_96, redefinedProperty97, defaultValue99, opposite102, subsettedProperty105, association108, owningAssociation109, redefinedClassifier85, general88, generalization91, substitution92, powertypeExtent93, featuringClassifier94, raisedException127, ownedFormalParam130, defaultValue131, type134, precondition136, bodyCondition139, postcondition142, class_145, dataType147, dataType111, interface113, qualifier115, associationEnd117, general119, specific121, generalizationSet123, ownedParameter126, memberEnd164, ownedEnd166, ownedAttribute168, ownedOperation170, ownedLiteral173, enumeration174, receivingPackage175, interface150, nestedClassifier153, ownedOperation155, superClass156, ownedAttribute159, navigableOwnedEnd162, nestedClassifier188, redefinedInterface190, ownedAttribute193, ownedOperation195, implementingClassifier198, contract199, interfaceRealization201, powertype202, mergedPackage177, client179, supplier181, mapping183, substitutingClassifier184, contract186, generalization204},
    generalizations={gen_Classes_Kernel_NamedElement_Element, gen_Classes_Kernel_Namespace_NamedElement, gen_Classes_Kernel_Package_Kernel_Namespace, gen_Classes_Kernel_Package_Kernel_PackageableElement, gen_Classes_Kernel_Comment_Element, gen_Classes_Kernel_Relationship_Element, gen_Classes_Kernel_PackageableElement_NamedElement, gen_Classes_Kernel_ElementImport_DirectedRelationship, gen_Classes_Kernel_PackageImport_DirectedRelationship, gen_Classes_Kernel_TypedElement_NamedElement, gen_Classes_Kernel_Type_PackageableElement, gen_Classes_Kernel_Expression_ValueSpecification, gen_Classes_Kernel_OpaqueExpression_ValueSpecification, gen_Classes_Kernel_LiteralSpecification_ValueSpecification, gen_Classes_Kernel_LiteralNull_LiteralSpecification, gen_Classes_Kernel_LiteralBoolean_LiteralSpecification, gen_Classes_Kernel_LiteralInteger_LiteralSpecification, gen_Classes_Kernel_DirectedRelationship_Relationship, gen_Classes_Kernel_MultiplicityElement_Element, gen_Classes_Kernel_ValueSpecification_Kernel_TypedElement, gen_Classes_Kernel_ValueSpecification_Kernel_PackageableElement, gen_Classes_Kernel_Slot_Element, gen_Classes_Kernel_RedefinableElement_NamedElement, gen_Classes_Kernel_Classifier_Kernel_RedefinableElement, gen_Classes_Kernel_Classifier_Kernel_Namespace, gen_Classes_Kernel_Classifier_Kernel_Type, gen_Classes_Kernel_LiteralReal_LiteralSpecification, gen_Classes_Kernel_LiteralString_LiteralSpecification, gen_Classes_Kernel_LiteralUnilimitedNatural_LiteralSpecification, gen_Classes_Kernel_InstanceSpecification_PackageableElement, gen_Classes_Kernel_Constraint_PackageableElement, gen_Classes_Kernel_StructuralFeature_Kernel_MultiplicityElement, gen_Classes_Kernel_StructuralFeature_Kernel_TypedElement, gen_Classes_Kernel_Property_StructuralFeature, gen_Classes_Kernel_Feature_RedefinableElement, gen_Classes_Kernel_StructuralFeature_Kernel_Feature, gen_Classes_Kernel_Parameter_TypedElement, gen_Classes_Kernel_Operation_BehavioralFeature, gen_Classes_Kernel_Generalization_DirectedRelationship, gen_Classes_Kernel_BehavioralFeature_Kernel_Feature, gen_Classes_Kernel_BehavioralFeature_Kernel_Namespace, gen_Classes_Kernel_DataType_Classifier, gen_Classes_Kernel_PrimitiveType_DataType, gen_Classes_Kernel_Enumeration_DataType, gen_Classes_Kernel_EnumerationLiteral_InstanceSpecification, gen_Classes_Kernel_PackageMerge_DirectedRelationship, gen_Classes_Kernel_Class_Classifier, gen_Classes_Kernel_Association_Kernel_Relationship, gen_Classes_Kernel_Association_Kernel_Classifier, gen_Classes_Interfaces_InterfaceRealization_Realization, gen_Classes_Interfaces_BehavioredClassifier_Classifier, gen_Classes_AssociationClasses_AssociationClass_Kernel_Class, gen_Classes_AssociationClasses_AssociationClass_Kernel_Association, gen_Classes_PowerTypes_GeneralizationSet_PackageableElement, gen_Classes_Dependencies_Dependency_Kernel_PackageableElement, gen_Classes_Dependencies_Dependency_Kernel_DirectedRelationship, gen_Classes_Dependencies_Usage_Dependency, gen_Classes_Dependencies_Abstraction_Dependency, gen_Classes_Dependencies_Realization_Abstraction, gen_Classes_Dependencies_Substitution_Realization, gen_Classes_Interfaces_Interface_Classifier},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)