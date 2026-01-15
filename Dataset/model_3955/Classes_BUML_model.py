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
Classes_Kernel_Element = Class(name="Classes::Kernel::Element", is_abstract=True)
Comment = Class(name="Comment")
ElementImport = Class(name="ElementImport")
PackageImport = Class(name="PackageImport")
Constraint = Class(name="Constraint")
Classes_Kernel_PackageableElement = Class(name="Classes::Kernel::PackageableElement")
Classes_Kernel_ElementImport = Class(name="Classes::Kernel::ElementImport")
DirectedRelationship = Class(name="DirectedRelationship")
Element = Class(name="Element")
Classes_Kernel_NamedElement = Class(name="Classes::Kernel::NamedElement", is_abstract=True)
Namespace = Class(name="Namespace")
Dependency = Class(name="Dependency")
Classes_Kernel_Namespace = Class(name="Classes::Kernel::Namespace")
NamedElement = Class(name="NamedElement")
PackageableElement = Class(name="PackageableElement")
Classes_Kernel_Relationship = Class(name="Classes::Kernel::Relationship", is_abstract=True)
Classes_Kernel_DirectedRelationship = Class(name="Classes::Kernel::DirectedRelationship", is_abstract=True)
Relationship = Class(name="Relationship")
Classes_Kernel_MultiplicityElement = Class(name="Classes::Kernel::MultiplicityElement", is_abstract=True)
Classes_Kernel_PackageImport = Class(name="Classes::Kernel::PackageImport")
Package = Class(name="Package")
Classes_Kernel_Package = Class(name="Classes::Kernel::Package")
Kernel_Namespace = Class(name="Kernel::Namespace")
Kernel_PackageableElement = Class(name="Kernel::PackageableElement")
Type = Class(name="Type")
PackageMerge = Class(name="PackageMerge")
Classes_Kernel_Comment = Class(name="Classes::Kernel::Comment")
Classes_Kernel_Expression = Class(name="Classes::Kernel::Expression")
Classes_Kernel_OpaqueExpression = Class(name="Classes::Kernel::OpaqueExpression")
Classes_Kernel_LiteralSpecification = Class(name="Classes::Kernel::LiteralSpecification", is_abstract=True)
Classes_Kernel_LiteralNull = Class(name="Classes::Kernel::LiteralNull")
LiteralSpecification = Class(name="LiteralSpecification")
Classes_Kernel_LiteralBoolean = Class(name="Classes::Kernel::LiteralBoolean")
Classes_Kernel_LiteralInteger = Class(name="Classes::Kernel::LiteralInteger")
ValueSpecification = Class(name="ValueSpecification")
Classes_Kernel_ValueSpecification = Class(name="Classes::Kernel::ValueSpecification", is_abstract=True)
Kernel_TypedElement = Class(name="Kernel::TypedElement")
MultiplicityElement = Class(name="MultiplicityElement")
Slot = Class(name="Slot")
InstanceSpecification = Class(name="InstanceSpecification")
Classes_Kernel_TypedElement = Class(name="Classes::Kernel::TypedElement", is_abstract=True)
Classes_Kernel_Type = Class(name="Classes::Kernel::Type", is_abstract=True)
StructuralFeature = Class(name="StructuralFeature")
Classes_Kernel_RedefinableElement = Class(name="Classes::Kernel::RedefinableElement", is_abstract=True)
RedefinableElement = Class(name="RedefinableElement")
Classes_Kernel_Classifier = Class(name="Classes::Kernel::Classifier", is_abstract=True)
Kernel_RedefinableElement = Class(name="Kernel::RedefinableElement")
Kernel_Type = Class(name="Kernel::Type")
Classes_Kernel_LiteralReal = Class(name="Classes::Kernel::LiteralReal")
Classes_Kernel_LiteralString = Class(name="Classes::Kernel::LiteralString")
Classes_Kernel_LiteralUnilimitedNatural = Class(name="Classes::Kernel::LiteralUnilimitedNatural")
Classes_Kernel_InstanceValue = Class(name="Classes::Kernel::InstanceValue")
Classes_Kernel_InstanceSpecification = Class(name="Classes::Kernel::InstanceSpecification")
Classifier = Class(name="Classifier")
Classes_Kernel_Constraint = Class(name="Classes::Kernel::Constraint")
Classes_Kernel_Slot = Class(name="Classes::Kernel::Slot")
Association = Class(name="Association")
Feature = Class(name="Feature")
Property_ = Class(name="Property")
Generalization = Class(name="Generalization")
Substitution = Class(name="Substitution")
GeneralizationSet = Class(name="GeneralizationSet")
Classes_Kernel_Feature = Class(name="Classes::Kernel::Feature", is_abstract=True)
Classes_Kernel_StructuralFeature = Class(name="Classes::Kernel::StructuralFeature", is_abstract=True)
Kernel_Feature = Class(name="Kernel::Feature")
Kernel_MultiplicityElement = Class(name="Kernel::MultiplicityElement")
Classes_Kernel_Property = Class(name="Classes::Kernel::Property")
Class_ = Class(name="Class")
Classes_Kernel_Operation = Class(name="Classes::Kernel::Operation")
DataType = Class(name="DataType")
Interface = Class(name="Interface")
Classes_Kernel_Generalization = Class(name="Classes::Kernel::Generalization")
Classes_Kernel_BehavioralFeature = Class(name="Classes::Kernel::BehavioralFeature", is_abstract=True)
Parameter_ = Class(name="Parameter")
Classes_Kernel_Parameter = Class(name="Classes::Kernel::Parameter")
TypedElement = Class(name="TypedElement")
BehavioralFeature = Class(name="BehavioralFeature")
Classes_Kernel_PrimitiveType = Class(name="Classes::Kernel::PrimitiveType")
Classes_Kernel_Enumeration = Class(name="Classes::Kernel::Enumeration")
EnumerationLiteral = Class(name="EnumerationLiteral")
Classes_Kernel_EnumerationLiteral = Class(name="Classes::Kernel::EnumerationLiteral")
Enumeration_ = Class(name="Enumeration")
Classes_Kernel_Class = Class(name="Classes::Kernel::Class")
Operation = Class(name="Operation")
Classes_Kernel_Association = Class(name="Classes::Kernel::Association")
Kernel_Relationship = Class(name="Kernel::Relationship")
Kernel_Classifier = Class(name="Kernel::Classifier")
Classes_Kernel_DataType = Class(name="Classes::Kernel::DataType")
Classes_Interfaces_Interface = Class(name="Classes::Interfaces::Interface")
Classes_Interfaces_InterfaceRealization = Class(name="Classes::Interfaces::InterfaceRealization")
Classes_Kernel_PackageMerge = Class(name="Classes::Kernel::PackageMerge")
Classes_Dependencies_Dependency = Class(name="Classes::Dependencies::Dependency")
Kernel_DirectedRelationship = Class(name="Kernel::DirectedRelationship")
Classes_Dependencies_Usage = Class(name="Classes::Dependencies::Usage")
Classes_Dependencies_Abstraction = Class(name="Classes::Dependencies::Abstraction")
OpaqueExpression = Class(name="OpaqueExpression")
Classes_Dependencies_Realization = Class(name="Classes::Dependencies::Realization")
Abstraction = Class(name="Abstraction")
Classes_Dependencies_Substitution = Class(name="Classes::Dependencies::Substitution")
Realization = Class(name="Realization")
BehavioredClassifier = Class(name="BehavioredClassifier")
Classes_Interfaces_BehavioredClassifier = Class(name="Classes::Interfaces::BehavioredClassifier", is_abstract=True)
InterfaceRealization = Class(name="InterfaceRealization")
Classes_AssociationClasses_AssociationClass = Class(name="Classes::AssociationClasses::AssociationClass")
Kernel_Class = Class(name="Kernel::Class")
Kernel_Association = Class(name="Kernel::Association")
Classes_PowerTypes_GeneralizationSet = Class(name="Classes::PowerTypes::GeneralizationSet")

# Classes_Kernel_Element class attributes and methods

# Comment class attributes and methods

# ElementImport class attributes and methods

# PackageImport class attributes and methods

# Constraint class attributes and methods

# Classes_Kernel_PackageableElement class attributes and methods

# Classes_Kernel_ElementImport class attributes and methods
Classes_Kernel_ElementImport_visibility: Property = Property(name="visibility", type=StringType)
Classes_Kernel_ElementImport_alias: Property = Property(name="alias", type=StringType)
Classes_Kernel_ElementImport.attributes={Classes_Kernel_ElementImport_alias, Classes_Kernel_ElementImport_visibility}

# DirectedRelationship class attributes and methods

# Element class attributes and methods

# Classes_Kernel_NamedElement class attributes and methods
Classes_Kernel_NamedElement_name: Property = Property(name="name", type=StringType)
Classes_Kernel_NamedElement_qualifiedName: Property = Property(name="qualifiedName", type=StringType)
Classes_Kernel_NamedElement_visibility: Property = Property(name="visibility", type=StringType)
Classes_Kernel_NamedElement.attributes={Classes_Kernel_NamedElement_visibility, Classes_Kernel_NamedElement_name, Classes_Kernel_NamedElement_qualifiedName}

# Namespace class attributes and methods

# Dependency class attributes and methods

# Classes_Kernel_Namespace class attributes and methods

# NamedElement class attributes and methods

# PackageableElement class attributes and methods

# Classes_Kernel_Relationship class attributes and methods

# Classes_Kernel_DirectedRelationship class attributes and methods

# Relationship class attributes and methods

# Classes_Kernel_MultiplicityElement class attributes and methods
Classes_Kernel_MultiplicityElement_isOrdered: Property = Property(name="isOrdered", type=BooleanType)
Classes_Kernel_MultiplicityElement_isUnique: Property = Property(name="isUnique", type=BooleanType)
Classes_Kernel_MultiplicityElement_upper: Property = Property(name="upper", type=IntegerType)
Classes_Kernel_MultiplicityElement_lower: Property = Property(name="lower", type=IntegerType)
Classes_Kernel_MultiplicityElement.attributes={Classes_Kernel_MultiplicityElement_lower, Classes_Kernel_MultiplicityElement_upper, Classes_Kernel_MultiplicityElement_isUnique, Classes_Kernel_MultiplicityElement_isOrdered}

# Classes_Kernel_PackageImport class attributes and methods
Classes_Kernel_PackageImport_visibility: Property = Property(name="visibility", type=StringType)
Classes_Kernel_PackageImport.attributes={Classes_Kernel_PackageImport_visibility}

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

# Classes_Kernel_Expression class attributes and methods
Classes_Kernel_Expression_symbol: Property = Property(name="symbol", type=StringType)
Classes_Kernel_Expression.attributes={Classes_Kernel_Expression_symbol}

# Classes_Kernel_OpaqueExpression class attributes and methods
Classes_Kernel_OpaqueExpression_body: Property = Property(name="body", type=StringType)
Classes_Kernel_OpaqueExpression_language: Property = Property(name="language", type=StringType)
Classes_Kernel_OpaqueExpression.attributes={Classes_Kernel_OpaqueExpression_language, Classes_Kernel_OpaqueExpression_body}

# Classes_Kernel_LiteralSpecification class attributes and methods

# Classes_Kernel_LiteralNull class attributes and methods

# LiteralSpecification class attributes and methods

# Classes_Kernel_LiteralBoolean class attributes and methods

# Classes_Kernel_LiteralInteger class attributes and methods

# ValueSpecification class attributes and methods

# Classes_Kernel_ValueSpecification class attributes and methods

# Kernel_TypedElement class attributes and methods

# MultiplicityElement class attributes and methods

# Slot class attributes and methods

# InstanceSpecification class attributes and methods

# Classes_Kernel_TypedElement class attributes and methods

# Classes_Kernel_Type class attributes and methods

# StructuralFeature class attributes and methods

# Classes_Kernel_RedefinableElement class attributes and methods
Classes_Kernel_RedefinableElement_isLeaf: Property = Property(name="isLeaf", type=BooleanType)
Classes_Kernel_RedefinableElement.attributes={Classes_Kernel_RedefinableElement_isLeaf}

# RedefinableElement class attributes and methods

# Classes_Kernel_Classifier class attributes and methods
Classes_Kernel_Classifier_isAbstract: Property = Property(name="isAbstract", type=BooleanType)
Classes_Kernel_Classifier_isFinalSpecialization: Property = Property(name="isFinalSpecialization", type=BooleanType)
Classes_Kernel_Classifier.attributes={Classes_Kernel_Classifier_isFinalSpecialization, Classes_Kernel_Classifier_isAbstract}

# Kernel_RedefinableElement class attributes and methods

# Kernel_Type class attributes and methods

# Classes_Kernel_LiteralReal class attributes and methods

# Classes_Kernel_LiteralString class attributes and methods

# Classes_Kernel_LiteralUnilimitedNatural class attributes and methods

# Classes_Kernel_InstanceValue class attributes and methods

# Classes_Kernel_InstanceSpecification class attributes and methods

# Classifier class attributes and methods

# Classes_Kernel_Constraint class attributes and methods

# Classes_Kernel_Slot class attributes and methods

# Association class attributes and methods

# Feature class attributes and methods

# Property class attributes and methods

# Generalization class attributes and methods

# Substitution class attributes and methods

# GeneralizationSet class attributes and methods

# Classes_Kernel_Feature class attributes and methods
Classes_Kernel_Feature_isStatic: Property = Property(name="isStatic", type=BooleanType)
Classes_Kernel_Feature.attributes={Classes_Kernel_Feature_isStatic}

# Classes_Kernel_StructuralFeature class attributes and methods
Classes_Kernel_StructuralFeature_isReadOnly: Property = Property(name="isReadOnly", type=BooleanType)
Classes_Kernel_StructuralFeature.attributes={Classes_Kernel_StructuralFeature_isReadOnly}

# Kernel_Feature class attributes and methods

# Kernel_MultiplicityElement class attributes and methods

# Classes_Kernel_Property class attributes and methods
Classes_Kernel_Property_default: Property = Property(name="default", type=StringType)
Classes_Kernel_Property_isComposite: Property = Property(name="isComposite", type=BooleanType)
Classes_Kernel_Property_isID: Property = Property(name="isID", type=BooleanType)
Classes_Kernel_Property_aggregation: Property = Property(name="aggregation", type=StringType)
Classes_Kernel_Property_isDerived: Property = Property(name="isDerived", type=BooleanType)
Classes_Kernel_Property_isDerivedUnion: Property = Property(name="isDerivedUnion", type=BooleanType)
Classes_Kernel_Property.attributes={Classes_Kernel_Property_default, Classes_Kernel_Property_aggregation, Classes_Kernel_Property_isDerived, Classes_Kernel_Property_isDerivedUnion, Classes_Kernel_Property_isComposite, Classes_Kernel_Property_isID}

# Class class attributes and methods

# Classes_Kernel_Operation class attributes and methods
Classes_Kernel_Operation_isQuery: Property = Property(name="isQuery", type=BooleanType)
Classes_Kernel_Operation_isOrdered: Property = Property(name="isOrdered", type=BooleanType)
Classes_Kernel_Operation_isUnique: Property = Property(name="isUnique", type=BooleanType)
Classes_Kernel_Operation_upper: Property = Property(name="upper", type=IntegerType)
Classes_Kernel_Operation_lower: Property = Property(name="lower", type=IntegerType)
Classes_Kernel_Operation.attributes={Classes_Kernel_Operation_lower, Classes_Kernel_Operation_upper, Classes_Kernel_Operation_isQuery, Classes_Kernel_Operation_isOrdered, Classes_Kernel_Operation_isUnique}

# DataType class attributes and methods

# Interface class attributes and methods

# Classes_Kernel_Generalization class attributes and methods
Classes_Kernel_Generalization_isSubstitutable: Property = Property(name="isSubstitutable", type=BooleanType)
Classes_Kernel_Generalization.attributes={Classes_Kernel_Generalization_isSubstitutable}

# Classes_Kernel_BehavioralFeature class attributes and methods

# Parameter class attributes and methods

# Classes_Kernel_Parameter class attributes and methods
Classes_Kernel_Parameter_default: Property = Property(name="default", type=StringType)
Classes_Kernel_Parameter.attributes={Classes_Kernel_Parameter_default}

# TypedElement class attributes and methods

# BehavioralFeature class attributes and methods

# Classes_Kernel_PrimitiveType class attributes and methods

# Classes_Kernel_Enumeration class attributes and methods

# EnumerationLiteral class attributes and methods

# Classes_Kernel_EnumerationLiteral class attributes and methods

# Enumeration class attributes and methods

# Classes_Kernel_Class class attributes and methods

# Operation class attributes and methods

# Classes_Kernel_Association class attributes and methods
Classes_Kernel_Association_isDerived: Property = Property(name="isDerived", type=BooleanType)
Classes_Kernel_Association.attributes={Classes_Kernel_Association_isDerived}

# Kernel_Relationship class attributes and methods

# Kernel_Classifier class attributes and methods

# Classes_Kernel_DataType class attributes and methods

# Classes_Interfaces_Interface class attributes and methods

# Classes_Interfaces_InterfaceRealization class attributes and methods

# Classes_Kernel_PackageMerge class attributes and methods

# Classes_Dependencies_Dependency class attributes and methods

# Kernel_DirectedRelationship class attributes and methods

# Classes_Dependencies_Usage class attributes and methods

# Classes_Dependencies_Abstraction class attributes and methods

# OpaqueExpression class attributes and methods

# Classes_Dependencies_Realization class attributes and methods

# Abstraction class attributes and methods

# Classes_Dependencies_Substitution class attributes and methods

# Realization class attributes and methods

# BehavioredClassifier class attributes and methods

# Classes_Interfaces_BehavioredClassifier class attributes and methods

# InterfaceRealization class attributes and methods

# Classes_AssociationClasses_AssociationClass class attributes and methods

# Kernel_Class class attributes and methods

# Kernel_Association class attributes and methods

# Classes_PowerTypes_GeneralizationSet class attributes and methods
Classes_PowerTypes_GeneralizationSet_isCovering: Property = Property(name="isCovering", type=BooleanType)
Classes_PowerTypes_GeneralizationSet_isDisjoint: Property = Property(name="isDisjoint", type=BooleanType)
Classes_PowerTypes_GeneralizationSet.attributes={Classes_PowerTypes_GeneralizationSet_isDisjoint, Classes_PowerTypes_GeneralizationSet_isCovering}

# Relationships
ownedComment0: BinaryAssociation = BinaryAssociation(
    name="ownedComment0",
    ends={
        Property(name="Kernel", type=Classes_Kernel_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="Comment", type=Comment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elementImport15: BinaryAssociation = BinaryAssociation(
    name="elementImport15",
    ends={
        Property(name="Kernel16", type=Classes_Kernel_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="ElementImport", type=ElementImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packageImport17: BinaryAssociation = BinaryAssociation(
    name="packageImport17",
    ends={
        Property(name="Kernel18", type=Classes_Kernel_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="PackageImport", type=PackageImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedRule19: BinaryAssociation = BinaryAssociation(
    name="ownedRule19",
    ends={
        Property(name="Kernel20", type=Classes_Kernel_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="Constraint", type=Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
importedElement21: BinaryAssociation = BinaryAssociation(
    name="importedElement21",
    ends={
        Property(name="PackageableElement22", type=Classes_Kernel_ElementImport, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Kernel_ElementImport", type=PackageableElement, multiplicity=Multiplicity(1, 1))
    }
)
ownedElement1: BinaryAssociation = BinaryAssociation(
    name="ownedElement1",
    ends={
        Property(name="Kernel2", type=Classes_Kernel_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="Element", type=Element, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owner3: BinaryAssociation = BinaryAssociation(
    name="owner3",
    ends={
        Property(name="Kernel5", type=Classes_Kernel_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="Element4", type=Element, multiplicity=Multiplicity(0, 1))
    }
)
namespace6: BinaryAssociation = BinaryAssociation(
    name="namespace6",
    ends={
        Property(name="Kernel7", type=Classes_Kernel_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="Namespace", type=Namespace, multiplicity=Multiplicity(0, 1))
    }
)
clientDependency8: BinaryAssociation = BinaryAssociation(
    name="clientDependency8",
    ends={
        Property(name="Dependencies", type=Classes_Kernel_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="Dependency", type=Dependency, multiplicity=Multiplicity(0, 9999))
    }
)
importedMember9: BinaryAssociation = BinaryAssociation(
    name="importedMember9",
    ends={
        Property(name="PackageableElement", type=Classes_Kernel_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Kernel_Namespace", type=PackageableElement, multiplicity=Multiplicity(0, 9999))
    }
)
member10: BinaryAssociation = BinaryAssociation(
    name="member10",
    ends={
        Property(name="NamedElement", type=Classes_Kernel_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Kernel_Namespace11", type=NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
ownedMember12: BinaryAssociation = BinaryAssociation(
    name="ownedMember12",
    ends={
        Property(name="Kernel14", type=Classes_Kernel_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="NamedElement13", type=NamedElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotatedElement45: BinaryAssociation = BinaryAssociation(
    name="annotatedElement45",
    ends={
        Property(name="Classes_Kernel_Comment", type=Element, multiplicity=Multiplicity(0, 9999)),
        Property(name="Element46", type=Classes_Kernel_Comment, multiplicity=Multiplicity(1, 1))
    }
)
relatedElement47: BinaryAssociation = BinaryAssociation(
    name="relatedElement47",
    ends={
        Property(name="Element48", type=Classes_Kernel_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Kernel_Relationship", type=Element, multiplicity=Multiplicity(1, 9999))
    }
)
target49: BinaryAssociation = BinaryAssociation(
    name="target49",
    ends={
        Property(name="Element50", type=Classes_Kernel_DirectedRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Kernel_DirectedRelationship", type=Element, multiplicity=Multiplicity(1, 9999))
    }
)
source51: BinaryAssociation = BinaryAssociation(
    name="source51",
    ends={
        Property(name="Element53", type=Classes_Kernel_DirectedRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Kernel_DirectedRelationship52", type=Element, multiplicity=Multiplicity(1, 9999))
    }
)
importingNamespace23: BinaryAssociation = BinaryAssociation(
    name="importingNamespace23",
    ends={
        Property(name="Kernel25", type=Classes_Kernel_ElementImport, multiplicity=Multiplicity(1, 1)),
        Property(name="Namespace24", type=Namespace, multiplicity=Multiplicity(1, 1))
    }
)
importedPackage26: BinaryAssociation = BinaryAssociation(
    name="importedPackage26",
    ends={
        Property(name="Package", type=Classes_Kernel_PackageImport, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Kernel_PackageImport", type=Package, multiplicity=Multiplicity(1, 1))
    }
)
importingNamespace27: BinaryAssociation = BinaryAssociation(
    name="importingNamespace27",
    ends={
        Property(name="Kernel29", type=Classes_Kernel_PackageImport, multiplicity=Multiplicity(1, 1)),
        Property(name="Namespace28", type=Namespace, multiplicity=Multiplicity(1, 1))
    }
)
nestedPackage30: BinaryAssociation = BinaryAssociation(
    name="nestedPackage30",
    ends={
        Property(name="Kernel32", type=Classes_Kernel_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="Package31", type=Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nestingPackage33: BinaryAssociation = BinaryAssociation(
    name="nestingPackage33",
    ends={
        Property(name="Kernel35", type=Classes_Kernel_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="Package34", type=Package, multiplicity=Multiplicity(0, 1))
    }
)
packagedElement36: BinaryAssociation = BinaryAssociation(
    name="packagedElement36",
    ends={
        Property(name="PackageableElement37", type=Classes_Kernel_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Kernel_Package", type=PackageableElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedType38: BinaryAssociation = BinaryAssociation(
    name="ownedType38",
    ends={
        Property(name="Kernel39", type=Classes_Kernel_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="Type", type=Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packageMerge40: BinaryAssociation = BinaryAssociation(
    name="packageMerge40",
    ends={
        Property(name="Kernel41", type=Classes_Kernel_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="PackageMerge", type=PackageMerge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningElement42: BinaryAssociation = BinaryAssociation(
    name="owningElement42",
    ends={
        Property(name="Kernel44", type=Classes_Kernel_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="Element43", type=Element, multiplicity=Multiplicity(0, 1))
    }
)
package73: BinaryAssociation = BinaryAssociation(
    name="package73",
    ends={
        Property(name="Kernel75", type=Classes_Kernel_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="Package74", type=Package, multiplicity=Multiplicity(0, 1))
    }
)
operand76: BinaryAssociation = BinaryAssociation(
    name="operand76",
    ends={
        Property(name="ValueSpecification77", type=Classes_Kernel_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Kernel_Expression", type=ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
upperValue54: BinaryAssociation = BinaryAssociation(
    name="upperValue54",
    ends={
        Property(name="Kernel55", type=Classes_Kernel_MultiplicityElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ValueSpecification", type=ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lowerValue56: BinaryAssociation = BinaryAssociation(
    name="lowerValue56",
    ends={
        Property(name="Kernel58", type=Classes_Kernel_MultiplicityElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ValueSpecification57", type=ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
owningUpper59: BinaryAssociation = BinaryAssociation(
    name="owningUpper59",
    ends={
        Property(name="Kernel60", type=Classes_Kernel_ValueSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="MultiplicityElement", type=MultiplicityElement, multiplicity=Multiplicity(0, 1))
    }
)
owningLower61: BinaryAssociation = BinaryAssociation(
    name="owningLower61",
    ends={
        Property(name="Kernel63", type=Classes_Kernel_ValueSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="MultiplicityElement62", type=MultiplicityElement, multiplicity=Multiplicity(0, 1))
    }
)
owningConstraint64: BinaryAssociation = BinaryAssociation(
    name="owningConstraint64",
    ends={
        Property(name="Kernel66", type=Classes_Kernel_ValueSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="Constraint65", type=Constraint, multiplicity=Multiplicity(0, 1))
    }
)
owningSlot67: BinaryAssociation = BinaryAssociation(
    name="owningSlot67",
    ends={
        Property(name="Kernel68", type=Classes_Kernel_ValueSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="Slot", type=Slot, multiplicity=Multiplicity(0, 1))
    }
)
owningInstanceSpec69: BinaryAssociation = BinaryAssociation(
    name="owningInstanceSpec69",
    ends={
        Property(name="Kernel70", type=Classes_Kernel_ValueSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="InstanceSpecification", type=InstanceSpecification, multiplicity=Multiplicity(0, 1))
    }
)
type71: BinaryAssociation = BinaryAssociation(
    name="type71",
    ends={
        Property(name="Type72", type=Classes_Kernel_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Kernel_TypedElement", type=Type, multiplicity=Multiplicity(0, 1))
    }
)
definingFeature101: BinaryAssociation = BinaryAssociation(
    name="definingFeature101",
    ends={
        Property(name="StructuralFeature", type=Classes_Kernel_Slot, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Kernel_Slot", type=StructuralFeature, multiplicity=Multiplicity(1, 1))
    }
)
redefinedElement102: BinaryAssociation = BinaryAssociation(
    name="redefinedElement102",
    ends={
        Property(name="RedefinableElement", type=Classes_Kernel_RedefinableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Kernel_RedefinableElement", type=RedefinableElement, multiplicity=Multiplicity(0, 9999))
    }
)
redefinitionContext103: BinaryAssociation = BinaryAssociation(
    name="redefinitionContext103",
    ends={
        Property(name="Classifier105", type=Classes_Kernel_RedefinableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Kernel_RedefinableElement104", type=Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
instance78: BinaryAssociation = BinaryAssociation(
    name="instance78",
    ends={
        Property(name="InstanceSpecification79", type=Classes_Kernel_InstanceValue, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Kernel_InstanceValue", type=InstanceSpecification, multiplicity=Multiplicity(1, 1))
    }
)
slot80: BinaryAssociation = BinaryAssociation(
    name="slot80",
    ends={
        Property(name="Kernel82", type=Classes_Kernel_InstanceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="Slot81", type=Slot, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specification83: BinaryAssociation = BinaryAssociation(
    name="specification83",
    ends={
        Property(name="Kernel85", type=Classes_Kernel_InstanceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="ValueSpecification84", type=ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
classifier86: BinaryAssociation = BinaryAssociation(
    name="classifier86",
    ends={
        Property(name="Classifier", type=Classes_Kernel_InstanceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Kernel_InstanceSpecification", type=Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
context87: BinaryAssociation = BinaryAssociation(
    name="context87",
    ends={
        Property(name="Kernel89", type=Classes_Kernel_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="Namespace88", type=Namespace, multiplicity=Multiplicity(0, 1))
    }
)
constrainedElement90: BinaryAssociation = BinaryAssociation(
    name="constrainedElement90",
    ends={
        Property(name="Element91", type=Classes_Kernel_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Kernel_Constraint", type=Element, multiplicity=Multiplicity(0, 9999))
    }
)
specification92: BinaryAssociation = BinaryAssociation(
    name="specification92",
    ends={
        Property(name="Kernel94", type=Classes_Kernel_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="ValueSpecification93", type=ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
owningInstace95: BinaryAssociation = BinaryAssociation(
    name="owningInstace95",
    ends={
        Property(name="Kernel97", type=Classes_Kernel_Slot, multiplicity=Multiplicity(1, 1)),
        Property(name="InstanceSpecification96", type=InstanceSpecification, multiplicity=Multiplicity(1, 1))
    }
)
value98: BinaryAssociation = BinaryAssociation(
    name="value98",
    ends={
        Property(name="Kernel100", type=Classes_Kernel_Slot, multiplicity=Multiplicity(1, 1)),
        Property(name="ValueSpecification99", type=ValueSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
redefinedProperty128: BinaryAssociation = BinaryAssociation(
    name="redefinedProperty128",
    ends={
        Property(name="Property129", type=Classes_Kernel_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Kernel_Property", type=Property_, multiplicity=Multiplicity(0, 9999))
    }
)
defaultValue130: BinaryAssociation = BinaryAssociation(
    name="defaultValue130",
    ends={
        Property(name="ValueSpecification132", type=Classes_Kernel_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Kernel_Property131", type=ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
opposite133: BinaryAssociation = BinaryAssociation(
    name="opposite133",
    ends={
        Property(name="Property135", type=Classes_Kernel_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Kernel_Property134", type=Property_, multiplicity=Multiplicity(0, 1))
    }
)
subsettedProperty136: BinaryAssociation = BinaryAssociation(
    name="subsettedProperty136",
    ends={
        Property(name="Property138", type=Classes_Kernel_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Kernel_Property137", type=Property_, multiplicity=Multiplicity(0, 1))
    }
)
association139: BinaryAssociation = BinaryAssociation(
    name="association139",
    ends={
        Property(name="Kernel140", type=Classes_Kernel_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="Association", type=Association, multiplicity=Multiplicity(0, 1))
    }
)
inheritedMember106: BinaryAssociation = BinaryAssociation(
    name="inheritedMember106",
    ends={
        Property(name="NamedElement107", type=Classes_Kernel_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Kernel_Classifier", type=NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
feature108: BinaryAssociation = BinaryAssociation(
    name="feature108",
    ends={
        Property(name="Kernel109", type=Classes_Kernel_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="Feature", type=Feature, multiplicity=Multiplicity(0, 9999))
    }
)
attribute110: BinaryAssociation = BinaryAssociation(
    name="attribute110",
    ends={
        Property(name="Property", type=Classes_Kernel_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Kernel_Classifier111", type=Property_, multiplicity=Multiplicity(0, 9999))
    }
)
redefinedClassifier112: BinaryAssociation = BinaryAssociation(
    name="redefinedClassifier112",
    ends={
        Property(name="Classifier114", type=Classes_Kernel_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Kernel_Classifier113", type=Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
general115: BinaryAssociation = BinaryAssociation(
    name="general115",
    ends={
        Property(name="Classifier117", type=Classes_Kernel_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Kernel_Classifier116", type=Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
generalization118: BinaryAssociation = BinaryAssociation(
    name="generalization118",
    ends={
        Property(name="Kernel119", type=Classes_Kernel_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="Generalization", type=Generalization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
substitution120: BinaryAssociation = BinaryAssociation(
    name="substitution120",
    ends={
        Property(name="Dependencies121", type=Classes_Kernel_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="Substitution", type=Substitution, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
powertypeExtent122: BinaryAssociation = BinaryAssociation(
    name="powertypeExtent122",
    ends={
        Property(name="PowerTypes", type=Classes_Kernel_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="GeneralizationSet", type=GeneralizationSet, multiplicity=Multiplicity(0, 9999))
    }
)
featuringClassifier123: BinaryAssociation = BinaryAssociation(
    name="featuringClassifier123",
    ends={
        Property(name="Kernel125", type=Classes_Kernel_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="Classifier124", type=Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
class126: BinaryAssociation = BinaryAssociation(
    name="class126",
    ends={
        Property(name="Kernel127", type=Classes_Kernel_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="Class", type=Class_, multiplicity=Multiplicity(0, 1))
    }
)
type169: BinaryAssociation = BinaryAssociation(
    name="type169",
    ends={
        Property(name="Type170", type=Classes_Kernel_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Kernel_Operation", type=Type, multiplicity=Multiplicity(0, 1))
    }
)
precondition171: BinaryAssociation = BinaryAssociation(
    name="precondition171",
    ends={
        Property(name="Constraint173", type=Classes_Kernel_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Kernel_Operation172", type=Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bodyCondition174: BinaryAssociation = BinaryAssociation(
    name="bodyCondition174",
    ends={
        Property(name="Constraint176", type=Classes_Kernel_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Kernel_Operation175", type=Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
postcondition177: BinaryAssociation = BinaryAssociation(
    name="postcondition177",
    ends={
        Property(name="Constraint179", type=Classes_Kernel_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Kernel_Operation178", type=Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningAssociation141: BinaryAssociation = BinaryAssociation(
    name="owningAssociation141",
    ends={
        Property(name="Kernel143", type=Classes_Kernel_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="Association142", type=Association, multiplicity=Multiplicity(0, 1))
    }
)
dataType144: BinaryAssociation = BinaryAssociation(
    name="dataType144",
    ends={
        Property(name="Kernel145", type=Classes_Kernel_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="DataType", type=DataType, multiplicity=Multiplicity(0, 1))
    }
)
interface146: BinaryAssociation = BinaryAssociation(
    name="interface146",
    ends={
        Property(name="Interfaces", type=Classes_Kernel_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="Interface", type=Interface, multiplicity=Multiplicity(0, 1))
    }
)
qualifier147: BinaryAssociation = BinaryAssociation(
    name="qualifier147",
    ends={
        Property(name="Kernel149", type=Classes_Kernel_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="Property148", type=Property_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
associationEnd150: BinaryAssociation = BinaryAssociation(
    name="associationEnd150",
    ends={
        Property(name="Kernel152", type=Classes_Kernel_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="Property151", type=Property_, multiplicity=Multiplicity(0, 1))
    }
)
general153: BinaryAssociation = BinaryAssociation(
    name="general153",
    ends={
        Property(name="Classifier154", type=Classes_Kernel_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Kernel_Generalization", type=Classifier, multiplicity=Multiplicity(1, 1))
    }
)
specific155: BinaryAssociation = BinaryAssociation(
    name="specific155",
    ends={
        Property(name="Kernel157", type=Classes_Kernel_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="Classifier156", type=Classifier, multiplicity=Multiplicity(1, 1))
    }
)
generalizationSet158: BinaryAssociation = BinaryAssociation(
    name="generalizationSet158",
    ends={
        Property(name="PowerTypes160", type=Classes_Kernel_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="GeneralizationSet159", type=GeneralizationSet, multiplicity=Multiplicity(0, 9999))
    }
)
ownedParameter161: BinaryAssociation = BinaryAssociation(
    name="ownedParameter161",
    ends={
        Property(name="Parameter", type=Classes_Kernel_BehavioralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Kernel_BehavioralFeature", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
raisedException162: BinaryAssociation = BinaryAssociation(
    name="raisedException162",
    ends={
        Property(name="Type164", type=Classes_Kernel_BehavioralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Kernel_BehavioralFeature163", type=Type, multiplicity=Multiplicity(0, 1))
    }
)
ownedFormalParam165: BinaryAssociation = BinaryAssociation(
    name="ownedFormalParam165",
    ends={
        Property(name="BehavioralFeature", type=Classes_Kernel_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Kernel_Parameter", type=BehavioralFeature, multiplicity=Multiplicity(0, 1))
    }
)
defaultValue166: BinaryAssociation = BinaryAssociation(
    name="defaultValue166",
    ends={
        Property(name="ValueSpecification168", type=Classes_Kernel_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Kernel_Parameter167", type=ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedAttribute207: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute207",
    ends={
        Property(name="Kernel209", type=Classes_Kernel_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="Property208", type=Property_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedOperation210: BinaryAssociation = BinaryAssociation(
    name="ownedOperation210",
    ends={
        Property(name="Kernel212", type=Classes_Kernel_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="Operation211", type=Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedLiteral213: BinaryAssociation = BinaryAssociation(
    name="ownedLiteral213",
    ends={
        Property(name="Kernel214", type=Classes_Kernel_Enumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="EnumerationLiteral", type=EnumerationLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
class180: BinaryAssociation = BinaryAssociation(
    name="class180",
    ends={
        Property(name="Kernel182", type=Classes_Kernel_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="Class181", type=Class_, multiplicity=Multiplicity(0, 1))
    }
)
dataType183: BinaryAssociation = BinaryAssociation(
    name="dataType183",
    ends={
        Property(name="Kernel185", type=Classes_Kernel_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="DataType184", type=DataType, multiplicity=Multiplicity(0, 1))
    }
)
interface186: BinaryAssociation = BinaryAssociation(
    name="interface186",
    ends={
        Property(name="Interfaces188", type=Classes_Kernel_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="Interface187", type=Interface, multiplicity=Multiplicity(0, 1))
    }
)
nestedClassifier189: BinaryAssociation = BinaryAssociation(
    name="nestedClassifier189",
    ends={
        Property(name="Classifier190", type=Classes_Kernel_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Kernel_Class", type=Classifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedOperation191: BinaryAssociation = BinaryAssociation(
    name="ownedOperation191",
    ends={
        Property(name="Kernel192", type=Classes_Kernel_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="Operation", type=Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superClass193: BinaryAssociation = BinaryAssociation(
    name="superClass193",
    ends={
        Property(name="Class195", type=Classes_Kernel_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Kernel_Class194", type=Class_, multiplicity=Multiplicity(0, 9999))
    }
)
ownedAttribute196: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute196",
    ends={
        Property(name="Kernel198", type=Classes_Kernel_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="Property197", type=Property_, multiplicity=Multiplicity(0, 9999))
    }
)
navigableOwnedEnd199: BinaryAssociation = BinaryAssociation(
    name="navigableOwnedEnd199",
    ends={
        Property(name="Property200", type=Classes_Kernel_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Kernel_Association", type=Property_, multiplicity=Multiplicity(0, 9999))
    }
)
memberEnd201: BinaryAssociation = BinaryAssociation(
    name="memberEnd201",
    ends={
        Property(name="Kernel203", type=Classes_Kernel_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="Property202", type=Property_, multiplicity=Multiplicity(2, 9999))
    }
)
ownedEnd204: BinaryAssociation = BinaryAssociation(
    name="ownedEnd204",
    ends={
        Property(name="Kernel206", type=Classes_Kernel_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="Property205", type=Property_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nestedClassifier233: BinaryAssociation = BinaryAssociation(
    name="nestedClassifier233",
    ends={
        Property(name="Classifier234", type=Classes_Interfaces_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Interfaces_Interface", type=Classifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
redefinedInterface235: BinaryAssociation = BinaryAssociation(
    name="redefinedInterface235",
    ends={
        Property(name="Interface237", type=Classes_Interfaces_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Interfaces_Interface236", type=Interface, multiplicity=Multiplicity(0, 9999))
    }
)
ownedAttribute238: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute238",
    ends={
        Property(name="Kernel240", type=Classes_Interfaces_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="Property239", type=Property_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedOperation241: BinaryAssociation = BinaryAssociation(
    name="ownedOperation241",
    ends={
        Property(name="Kernel243", type=Classes_Interfaces_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="Operation242", type=Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enumeration215: BinaryAssociation = BinaryAssociation(
    name="enumeration215",
    ends={
        Property(name="Kernel216", type=Classes_Kernel_EnumerationLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="Enumeration", type=Enumeration_, multiplicity=Multiplicity(1, 1))
    }
)
receivingPackage217: BinaryAssociation = BinaryAssociation(
    name="receivingPackage217",
    ends={
        Property(name="Kernel219", type=Classes_Kernel_PackageMerge, multiplicity=Multiplicity(1, 1)),
        Property(name="Package218", type=Package, multiplicity=Multiplicity(1, 1))
    }
)
mergedPackage220: BinaryAssociation = BinaryAssociation(
    name="mergedPackage220",
    ends={
        Property(name="Package221", type=Classes_Kernel_PackageMerge, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Kernel_PackageMerge", type=Package, multiplicity=Multiplicity(1, 1))
    }
)
client222: BinaryAssociation = BinaryAssociation(
    name="client222",
    ends={
        Property(name="Kernel224", type=Classes_Dependencies_Dependency, multiplicity=Multiplicity(1, 1)),
        Property(name="NamedElement223", type=NamedElement, multiplicity=Multiplicity(1, 9999))
    }
)
supplier225: BinaryAssociation = BinaryAssociation(
    name="supplier225",
    ends={
        Property(name="NamedElement226", type=Classes_Dependencies_Dependency, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Dependencies_Dependency", type=NamedElement, multiplicity=Multiplicity(1, 9999))
    }
)
mapping227: BinaryAssociation = BinaryAssociation(
    name="mapping227",
    ends={
        Property(name="OpaqueExpression", type=Classes_Dependencies_Abstraction, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Dependencies_Abstraction", type=OpaqueExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
substitutingClassifier228: BinaryAssociation = BinaryAssociation(
    name="substitutingClassifier228",
    ends={
        Property(name="Kernel230", type=Classes_Dependencies_Substitution, multiplicity=Multiplicity(1, 1)),
        Property(name="Classifier229", type=Classifier, multiplicity=Multiplicity(1, 1))
    }
)
contract231: BinaryAssociation = BinaryAssociation(
    name="contract231",
    ends={
        Property(name="Classifier232", type=Classes_Dependencies_Substitution, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Dependencies_Substitution", type=Classifier, multiplicity=Multiplicity(1, 1))
    }
)
implementingClassifier244: BinaryAssociation = BinaryAssociation(
    name="implementingClassifier244",
    ends={
        Property(name="Interfaces245", type=Classes_Interfaces_InterfaceRealization, multiplicity=Multiplicity(1, 1)),
        Property(name="BehavioredClassifier", type=BehavioredClassifier, multiplicity=Multiplicity(1, 1))
    }
)
contract246: BinaryAssociation = BinaryAssociation(
    name="contract246",
    ends={
        Property(name="Interface247", type=Classes_Interfaces_InterfaceRealization, multiplicity=Multiplicity(1, 1)),
        Property(name="Classes_Interfaces_InterfaceRealization", type=Interface, multiplicity=Multiplicity(1, 1))
    }
)
interfaceRealization248: BinaryAssociation = BinaryAssociation(
    name="interfaceRealization248",
    ends={
        Property(name="Interfaces249", type=Classes_Interfaces_BehavioredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="InterfaceRealization", type=InterfaceRealization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
powertype250: BinaryAssociation = BinaryAssociation(
    name="powertype250",
    ends={
        Property(name="Kernel252", type=Classes_PowerTypes_GeneralizationSet, multiplicity=Multiplicity(1, 1)),
        Property(name="Classifier251", type=Classifier, multiplicity=Multiplicity(0, 1))
    }
)
generalization253: BinaryAssociation = BinaryAssociation(
    name="generalization253",
    ends={
        Property(name="Kernel255", type=Classes_PowerTypes_GeneralizationSet, multiplicity=Multiplicity(1, 1)),
        Property(name="Generalization254", type=Generalization, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_Classes_Kernel_PackageableElement_NamedElement = Generalization(general=NamedElement, specific=Classes_Kernel_PackageableElement)
gen_Classes_Kernel_ElementImport_DirectedRelationship = Generalization(general=DirectedRelationship, specific=Classes_Kernel_ElementImport)
gen_Classes_Kernel_NamedElement_Element = Generalization(general=Element, specific=Classes_Kernel_NamedElement)
gen_Classes_Kernel_Namespace_NamedElement = Generalization(general=NamedElement, specific=Classes_Kernel_Namespace)
gen_Classes_Kernel_Relationship_Element = Generalization(general=Element, specific=Classes_Kernel_Relationship)
gen_Classes_Kernel_DirectedRelationship_Relationship = Generalization(general=Relationship, specific=Classes_Kernel_DirectedRelationship)
gen_Classes_Kernel_MultiplicityElement_Element = Generalization(general=Element, specific=Classes_Kernel_MultiplicityElement)
gen_Classes_Kernel_PackageImport_DirectedRelationship = Generalization(general=DirectedRelationship, specific=Classes_Kernel_PackageImport)
gen_Classes_Kernel_Package_Kernel_Namespace = Generalization(general=Kernel_Namespace, specific=Classes_Kernel_Package)
gen_Classes_Kernel_Package_Kernel_PackageableElement = Generalization(general=Kernel_PackageableElement, specific=Classes_Kernel_Package)
gen_Classes_Kernel_Comment_Element = Generalization(general=Element, specific=Classes_Kernel_Comment)
gen_Classes_Kernel_Expression_ValueSpecification = Generalization(general=ValueSpecification, specific=Classes_Kernel_Expression)
gen_Classes_Kernel_OpaqueExpression_ValueSpecification = Generalization(general=ValueSpecification, specific=Classes_Kernel_OpaqueExpression)
gen_Classes_Kernel_LiteralSpecification_ValueSpecification = Generalization(general=ValueSpecification, specific=Classes_Kernel_LiteralSpecification)
gen_Classes_Kernel_LiteralNull_LiteralSpecification = Generalization(general=LiteralSpecification, specific=Classes_Kernel_LiteralNull)
gen_Classes_Kernel_LiteralBoolean_LiteralSpecification = Generalization(general=LiteralSpecification, specific=Classes_Kernel_LiteralBoolean)
gen_Classes_Kernel_LiteralInteger_LiteralSpecification = Generalization(general=LiteralSpecification, specific=Classes_Kernel_LiteralInteger)
gen_Classes_Kernel_ValueSpecification_Kernel_TypedElement = Generalization(general=Kernel_TypedElement, specific=Classes_Kernel_ValueSpecification)
gen_Classes_Kernel_ValueSpecification_Kernel_PackageableElement = Generalization(general=Kernel_PackageableElement, specific=Classes_Kernel_ValueSpecification)
gen_Classes_Kernel_TypedElement_NamedElement = Generalization(general=NamedElement, specific=Classes_Kernel_TypedElement)
gen_Classes_Kernel_Type_PackageableElement = Generalization(general=PackageableElement, specific=Classes_Kernel_Type)
gen_Classes_Kernel_RedefinableElement_NamedElement = Generalization(general=NamedElement, specific=Classes_Kernel_RedefinableElement)
gen_Classes_Kernel_Classifier_Kernel_RedefinableElement = Generalization(general=Kernel_RedefinableElement, specific=Classes_Kernel_Classifier)
gen_Classes_Kernel_Classifier_Kernel_Namespace = Generalization(general=Kernel_Namespace, specific=Classes_Kernel_Classifier)
gen_Classes_Kernel_Classifier_Kernel_Type = Generalization(general=Kernel_Type, specific=Classes_Kernel_Classifier)
gen_Classes_Kernel_LiteralReal_LiteralSpecification = Generalization(general=LiteralSpecification, specific=Classes_Kernel_LiteralReal)
gen_Classes_Kernel_LiteralString_LiteralSpecification = Generalization(general=LiteralSpecification, specific=Classes_Kernel_LiteralString)
gen_Classes_Kernel_LiteralUnilimitedNatural_LiteralSpecification = Generalization(general=LiteralSpecification, specific=Classes_Kernel_LiteralUnilimitedNatural)
gen_Classes_Kernel_InstanceSpecification_PackageableElement = Generalization(general=PackageableElement, specific=Classes_Kernel_InstanceSpecification)
gen_Classes_Kernel_Constraint_PackageableElement = Generalization(general=PackageableElement, specific=Classes_Kernel_Constraint)
gen_Classes_Kernel_Slot_Element = Generalization(general=Element, specific=Classes_Kernel_Slot)
gen_Classes_Kernel_Feature_RedefinableElement = Generalization(general=RedefinableElement, specific=Classes_Kernel_Feature)
gen_Classes_Kernel_StructuralFeature_Kernel_Feature = Generalization(general=Kernel_Feature, specific=Classes_Kernel_StructuralFeature)
gen_Classes_Kernel_StructuralFeature_Kernel_MultiplicityElement = Generalization(general=Kernel_MultiplicityElement, specific=Classes_Kernel_StructuralFeature)
gen_Classes_Kernel_StructuralFeature_Kernel_TypedElement = Generalization(general=Kernel_TypedElement, specific=Classes_Kernel_StructuralFeature)
gen_Classes_Kernel_Property_StructuralFeature = Generalization(general=StructuralFeature, specific=Classes_Kernel_Property)
gen_Classes_Kernel_Operation_BehavioralFeature = Generalization(general=BehavioralFeature, specific=Classes_Kernel_Operation)
gen_Classes_Kernel_Generalization_DirectedRelationship = Generalization(general=DirectedRelationship, specific=Classes_Kernel_Generalization)
gen_Classes_Kernel_BehavioralFeature_Kernel_Feature = Generalization(general=Kernel_Feature, specific=Classes_Kernel_BehavioralFeature)
gen_Classes_Kernel_BehavioralFeature_Kernel_Namespace = Generalization(general=Kernel_Namespace, specific=Classes_Kernel_BehavioralFeature)
gen_Classes_Kernel_Parameter_TypedElement = Generalization(general=TypedElement, specific=Classes_Kernel_Parameter)
gen_Classes_Kernel_PrimitiveType_DataType = Generalization(general=DataType, specific=Classes_Kernel_PrimitiveType)
gen_Classes_Kernel_Enumeration_DataType = Generalization(general=DataType, specific=Classes_Kernel_Enumeration)
gen_Classes_Kernel_EnumerationLiteral_InstanceSpecification = Generalization(general=InstanceSpecification, specific=Classes_Kernel_EnumerationLiteral)
gen_Classes_Kernel_Class_Classifier = Generalization(general=Classifier, specific=Classes_Kernel_Class)
gen_Classes_Kernel_Association_Kernel_Relationship = Generalization(general=Kernel_Relationship, specific=Classes_Kernel_Association)
gen_Classes_Kernel_Association_Kernel_Classifier = Generalization(general=Kernel_Classifier, specific=Classes_Kernel_Association)
gen_Classes_Kernel_DataType_Classifier = Generalization(general=Classifier, specific=Classes_Kernel_DataType)
gen_Classes_Interfaces_Interface_Classifier = Generalization(general=Classifier, specific=Classes_Interfaces_Interface)
gen_Classes_Interfaces_InterfaceRealization_Realization = Generalization(general=Realization, specific=Classes_Interfaces_InterfaceRealization)
gen_Classes_Kernel_PackageMerge_DirectedRelationship = Generalization(general=DirectedRelationship, specific=Classes_Kernel_PackageMerge)
gen_Classes_Dependencies_Dependency_Kernel_PackageableElement = Generalization(general=Kernel_PackageableElement, specific=Classes_Dependencies_Dependency)
gen_Classes_Dependencies_Dependency_Kernel_DirectedRelationship = Generalization(general=Kernel_DirectedRelationship, specific=Classes_Dependencies_Dependency)
gen_Classes_Dependencies_Usage_Dependency = Generalization(general=Dependency, specific=Classes_Dependencies_Usage)
gen_Classes_Dependencies_Abstraction_Dependency = Generalization(general=Dependency, specific=Classes_Dependencies_Abstraction)
gen_Classes_Dependencies_Realization_Abstraction = Generalization(general=Abstraction, specific=Classes_Dependencies_Realization)
gen_Classes_Dependencies_Substitution_Realization = Generalization(general=Realization, specific=Classes_Dependencies_Substitution)
gen_Classes_Interfaces_BehavioredClassifier_Classifier = Generalization(general=Classifier, specific=Classes_Interfaces_BehavioredClassifier)
gen_Classes_AssociationClasses_AssociationClass_Kernel_Class = Generalization(general=Kernel_Class, specific=Classes_AssociationClasses_AssociationClass)
gen_Classes_AssociationClasses_AssociationClass_Kernel_Association = Generalization(general=Kernel_Association, specific=Classes_AssociationClasses_AssociationClass)
gen_Classes_PowerTypes_GeneralizationSet_PackageableElement = Generalization(general=PackageableElement, specific=Classes_PowerTypes_GeneralizationSet)

# Domain Model
domain_model = DomainModel(
    name="Classes",
    types={Classes_Kernel_Element, Comment, ElementImport, PackageImport, Constraint, Classes_Kernel_PackageableElement, Classes_Kernel_ElementImport, DirectedRelationship, Element, Classes_Kernel_NamedElement, Namespace, Dependency, Classes_Kernel_Namespace, NamedElement, PackageableElement, Classes_Kernel_Relationship, Classes_Kernel_DirectedRelationship, Relationship, Classes_Kernel_MultiplicityElement, Classes_Kernel_PackageImport, Package, Classes_Kernel_Package, Kernel_Namespace, Kernel_PackageableElement, Type, PackageMerge, Classes_Kernel_Comment, Classes_Kernel_Expression, Classes_Kernel_OpaqueExpression, Classes_Kernel_LiteralSpecification, Classes_Kernel_LiteralNull, LiteralSpecification, Classes_Kernel_LiteralBoolean, Classes_Kernel_LiteralInteger, ValueSpecification, Classes_Kernel_ValueSpecification, Kernel_TypedElement, MultiplicityElement, Slot, InstanceSpecification, Classes_Kernel_TypedElement, Classes_Kernel_Type, StructuralFeature, Classes_Kernel_RedefinableElement, RedefinableElement, Classes_Kernel_Classifier, Kernel_RedefinableElement, Kernel_Type, Classes_Kernel_LiteralReal, Classes_Kernel_LiteralString, Classes_Kernel_LiteralUnilimitedNatural, Classes_Kernel_InstanceValue, Classes_Kernel_InstanceSpecification, Classifier, Classes_Kernel_Constraint, Classes_Kernel_Slot, Association, Feature, Property_, Generalization, Substitution, GeneralizationSet, Classes_Kernel_Feature, Classes_Kernel_StructuralFeature, Kernel_Feature, Kernel_MultiplicityElement, Classes_Kernel_Property, Class_, Classes_Kernel_Operation, DataType, Interface, Classes_Kernel_Generalization, Classes_Kernel_BehavioralFeature, Parameter_, Classes_Kernel_Parameter, TypedElement, BehavioralFeature, Classes_Kernel_PrimitiveType, Classes_Kernel_Enumeration, EnumerationLiteral, Classes_Kernel_EnumerationLiteral, Enumeration_, Classes_Kernel_Class, Operation, Classes_Kernel_Association, Kernel_Relationship, Kernel_Classifier, Classes_Kernel_DataType, Classes_Interfaces_Interface, Classes_Interfaces_InterfaceRealization, Classes_Kernel_PackageMerge, Classes_Dependencies_Dependency, Kernel_DirectedRelationship, Classes_Dependencies_Usage, Classes_Dependencies_Abstraction, OpaqueExpression, Classes_Dependencies_Realization, Abstraction, Classes_Dependencies_Substitution, Realization, BehavioredClassifier, Classes_Interfaces_BehavioredClassifier, InterfaceRealization, Classes_AssociationClasses_AssociationClass, Kernel_Class, Kernel_Association, Classes_PowerTypes_GeneralizationSet, VisibilityKind, AggregationKind},
    associations={ownedComment0, elementImport15, packageImport17, ownedRule19, importedElement21, ownedElement1, owner3, namespace6, clientDependency8, importedMember9, member10, ownedMember12, annotatedElement45, relatedElement47, target49, source51, importingNamespace23, importedPackage26, importingNamespace27, nestedPackage30, nestingPackage33, packagedElement36, ownedType38, packageMerge40, owningElement42, package73, operand76, upperValue54, lowerValue56, owningUpper59, owningLower61, owningConstraint64, owningSlot67, owningInstanceSpec69, type71, definingFeature101, redefinedElement102, redefinitionContext103, instance78, slot80, specification83, classifier86, context87, constrainedElement90, specification92, owningInstace95, value98, redefinedProperty128, defaultValue130, opposite133, subsettedProperty136, association139, inheritedMember106, feature108, attribute110, redefinedClassifier112, general115, generalization118, substitution120, powertypeExtent122, featuringClassifier123, class126, type169, precondition171, bodyCondition174, postcondition177, owningAssociation141, dataType144, interface146, qualifier147, associationEnd150, general153, specific155, generalizationSet158, ownedParameter161, raisedException162, ownedFormalParam165, defaultValue166, ownedAttribute207, ownedOperation210, ownedLiteral213, class180, dataType183, interface186, nestedClassifier189, ownedOperation191, superClass193, ownedAttribute196, navigableOwnedEnd199, memberEnd201, ownedEnd204, nestedClassifier233, redefinedInterface235, ownedAttribute238, ownedOperation241, enumeration215, receivingPackage217, mergedPackage220, client222, supplier225, mapping227, substitutingClassifier228, contract231, implementingClassifier244, contract246, interfaceRealization248, powertype250, generalization253},
    generalizations={gen_Classes_Kernel_PackageableElement_NamedElement, gen_Classes_Kernel_ElementImport_DirectedRelationship, gen_Classes_Kernel_NamedElement_Element, gen_Classes_Kernel_Namespace_NamedElement, gen_Classes_Kernel_Relationship_Element, gen_Classes_Kernel_DirectedRelationship_Relationship, gen_Classes_Kernel_MultiplicityElement_Element, gen_Classes_Kernel_PackageImport_DirectedRelationship, gen_Classes_Kernel_Package_Kernel_Namespace, gen_Classes_Kernel_Package_Kernel_PackageableElement, gen_Classes_Kernel_Comment_Element, gen_Classes_Kernel_Expression_ValueSpecification, gen_Classes_Kernel_OpaqueExpression_ValueSpecification, gen_Classes_Kernel_LiteralSpecification_ValueSpecification, gen_Classes_Kernel_LiteralNull_LiteralSpecification, gen_Classes_Kernel_LiteralBoolean_LiteralSpecification, gen_Classes_Kernel_LiteralInteger_LiteralSpecification, gen_Classes_Kernel_ValueSpecification_Kernel_TypedElement, gen_Classes_Kernel_ValueSpecification_Kernel_PackageableElement, gen_Classes_Kernel_TypedElement_NamedElement, gen_Classes_Kernel_Type_PackageableElement, gen_Classes_Kernel_RedefinableElement_NamedElement, gen_Classes_Kernel_Classifier_Kernel_RedefinableElement, gen_Classes_Kernel_Classifier_Kernel_Namespace, gen_Classes_Kernel_Classifier_Kernel_Type, gen_Classes_Kernel_LiteralReal_LiteralSpecification, gen_Classes_Kernel_LiteralString_LiteralSpecification, gen_Classes_Kernel_LiteralUnilimitedNatural_LiteralSpecification, gen_Classes_Kernel_InstanceSpecification_PackageableElement, gen_Classes_Kernel_Constraint_PackageableElement, gen_Classes_Kernel_Slot_Element, gen_Classes_Kernel_Feature_RedefinableElement, gen_Classes_Kernel_StructuralFeature_Kernel_Feature, gen_Classes_Kernel_StructuralFeature_Kernel_MultiplicityElement, gen_Classes_Kernel_StructuralFeature_Kernel_TypedElement, gen_Classes_Kernel_Property_StructuralFeature, gen_Classes_Kernel_Operation_BehavioralFeature, gen_Classes_Kernel_Generalization_DirectedRelationship, gen_Classes_Kernel_BehavioralFeature_Kernel_Feature, gen_Classes_Kernel_BehavioralFeature_Kernel_Namespace, gen_Classes_Kernel_Parameter_TypedElement, gen_Classes_Kernel_PrimitiveType_DataType, gen_Classes_Kernel_Enumeration_DataType, gen_Classes_Kernel_EnumerationLiteral_InstanceSpecification, gen_Classes_Kernel_Class_Classifier, gen_Classes_Kernel_Association_Kernel_Relationship, gen_Classes_Kernel_Association_Kernel_Classifier, gen_Classes_Kernel_DataType_Classifier, gen_Classes_Interfaces_Interface_Classifier, gen_Classes_Interfaces_InterfaceRealization_Realization, gen_Classes_Kernel_PackageMerge_DirectedRelationship, gen_Classes_Dependencies_Dependency_Kernel_PackageableElement, gen_Classes_Dependencies_Dependency_Kernel_DirectedRelationship, gen_Classes_Dependencies_Usage_Dependency, gen_Classes_Dependencies_Abstraction_Dependency, gen_Classes_Dependencies_Realization_Abstraction, gen_Classes_Dependencies_Substitution_Realization, gen_Classes_Interfaces_BehavioredClassifier_Classifier, gen_Classes_AssociationClasses_AssociationClass_Kernel_Class, gen_Classes_AssociationClasses_AssociationClass_Kernel_Association, gen_Classes_PowerTypes_GeneralizationSet_PackageableElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)