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

# Classes
ClassesProv_Element = Class(name="ClassesProv::Element", is_abstract=True)
ClassesProv_NamedElement = Class(name="ClassesProv::NamedElement", is_abstract=True)
Element = Class(name="Element")
ClassesProv_ElementImport = Class(name="ClassesProv::ElementImport")
ClassesProv_PackageImport = Class(name="ClassesProv::PackageImport")
ClassesProv_Constraint = Class(name="ClassesProv::Constraint")
DirectedRelationship = Class(name="DirectedRelationship")
ClassesProv_Package = Class(name="ClassesProv::Package")
Namespace = Class(name="Namespace")
PackageableElement = Class(name="PackageableElement")
ClassesProv_Namespace = Class(name="ClassesProv::Namespace")
ClassesProv_Dependency = Class(name="ClassesProv::Dependency")
NamedElement = Class(name="NamedElement")
ClassesProv_PackageableElement = Class(name="ClassesProv::PackageableElement")
ClassesProv_DirectedRelationship = Class(name="ClassesProv::DirectedRelationship", is_abstract=True)
Relationship = Class(name="Relationship")
ClassesProv_MultiplicityElement = Class(name="ClassesProv::MultiplicityElement", is_abstract=True)
ClassesProv_ValueSpecification = Class(name="ClassesProv::ValueSpecification", is_abstract=True)
TypedElement = Class(name="TypedElement")
ClassesProv_Slot = Class(name="ClassesProv::Slot")
ClassesProv_InstanceSpecification = Class(name="ClassesProv::InstanceSpecification")
ClassesProv_TypedElement = Class(name="ClassesProv::TypedElement", is_abstract=True)
ClassesProv_Type = Class(name="ClassesProv::Type", is_abstract=True)
ClassesProv_PackageMerge = Class(name="ClassesProv::PackageMerge")
ClassesProv_Relationship = Class(name="ClassesProv::Relationship", is_abstract=True)
ClassesProv_LiteralSpecification = Class(name="ClassesProv::LiteralSpecification", is_abstract=True)
ClassesProv_LiteralNull = Class(name="ClassesProv::LiteralNull")
LiteralSpecification = Class(name="LiteralSpecification")
ClassesProv_LiteralBoolean = Class(name="ClassesProv::LiteralBoolean")
ClassesProv_LiteralInteger = Class(name="ClassesProv::LiteralInteger")
ClassesProv_LiteralReal = Class(name="ClassesProv::LiteralReal")
ClassesProv_LiteralString = Class(name="ClassesProv::LiteralString")
ClassesProv_LiteralUnilimitedNatural = Class(name="ClassesProv::LiteralUnilimitedNatural")
ClassesProv_InstanceValue = Class(name="ClassesProv::InstanceValue")
ClassesProv_Classifier = Class(name="ClassesProv::Classifier", is_abstract=True)
ClassesProv_StructuralFeature = Class(name="ClassesProv::StructuralFeature", is_abstract=True)
ClassesProv_RedefinableElement = Class(name="ClassesProv::RedefinableElement", is_abstract=True)
ClassesProv_Expression = Class(name="ClassesProv::Expression")
ValueSpecification = Class(name="ValueSpecification")
ClassesProv_OpaqueExpression = Class(name="ClassesProv::OpaqueExpression")
ClassesProv_Feature = Class(name="ClassesProv::Feature", is_abstract=True)
ClassesProv_Property = Class(name="ClassesProv::Property")
ClassesProv_Generalization = Class(name="ClassesProv::Generalization")
ClassesProv_Substitution = Class(name="ClassesProv::Substitution")
ClassesProv_GeneralizationSet = Class(name="ClassesProv::GeneralizationSet")
Feature = Class(name="Feature")
MultiplicityElement = Class(name="MultiplicityElement")
StructuralFeature = Class(name="StructuralFeature")
ClassesProv_Class = Class(name="ClassesProv::Class")
RedefinableElement = Class(name="RedefinableElement")
Type = Class(name="Type")
ClassesProv_Association = Class(name="ClassesProv::Association")
ClassesProv_DataType = Class(name="ClassesProv::DataType")
ClassesProv_Interface = Class(name="ClassesProv::Interface")
ClassesProv_BehavioralFeature = Class(name="ClassesProv::BehavioralFeature", is_abstract=True)
ClassesProv_Parameter = Class(name="ClassesProv::Parameter")
ClassesProv_Operation = Class(name="ClassesProv::Operation")
BehavioralFeature = Class(name="BehavioralFeature")
Classifier = Class(name="Classifier")
ClassesProv_EnumerationLiteral = Class(name="ClassesProv::EnumerationLiteral")
InstanceSpecification = Class(name="InstanceSpecification")
ClassesProv_Usage = Class(name="ClassesProv::Usage")
Dependency = Class(name="Dependency")
ClassesProv_Abstraction = Class(name="ClassesProv::Abstraction")
ClassesProv_Realization = Class(name="ClassesProv::Realization")
Abstraction = Class(name="Abstraction")
Realization = Class(name="Realization")
ClassesProv_InterfaceRealization = Class(name="ClassesProv::InterfaceRealization")
ClassesProv_PrimitiveType = Class(name="ClassesProv::PrimitiveType")
DataType = Class(name="DataType")
ClassesProv_Enumeration = Class(name="ClassesProv::Enumeration")
ClassesProv_AssociationClass = Class(name="ClassesProv::AssociationClass")
Class_ = Class(name="Class")
Association = Class(name="Association")

# ClassesProv_Element class attributes and methods

# ClassesProv_NamedElement class attributes and methods
ClassesProv_NamedElement_name: Property = Property(name="name", type=StringType)
ClassesProv_NamedElement_qualifiedName: Property = Property(name="qualifiedName", type=StringType)
ClassesProv_NamedElement.attributes={ClassesProv_NamedElement_name, ClassesProv_NamedElement_qualifiedName}

# Element class attributes and methods

# ClassesProv_ElementImport class attributes and methods
ClassesProv_ElementImport_alias: Property = Property(name="alias", type=StringType)
ClassesProv_ElementImport.attributes={ClassesProv_ElementImport_alias}

# ClassesProv_PackageImport class attributes and methods

# ClassesProv_Constraint class attributes and methods

# DirectedRelationship class attributes and methods

# ClassesProv_Package class attributes and methods
ClassesProv_Package_URI: Property = Property(name="URI", type=StringType)
ClassesProv_Package.attributes={ClassesProv_Package_URI}

# Namespace class attributes and methods

# PackageableElement class attributes and methods

# ClassesProv_Namespace class attributes and methods

# ClassesProv_Dependency class attributes and methods

# NamedElement class attributes and methods

# ClassesProv_PackageableElement class attributes and methods

# ClassesProv_DirectedRelationship class attributes and methods

# Relationship class attributes and methods

# ClassesProv_MultiplicityElement class attributes and methods
ClassesProv_MultiplicityElement_isOrdered: Property = Property(name="isOrdered", type=BooleanType)
ClassesProv_MultiplicityElement_isUnique: Property = Property(name="isUnique", type=BooleanType)
ClassesProv_MultiplicityElement_upper: Property = Property(name="upper", type=IntegerType)
ClassesProv_MultiplicityElement_lower: Property = Property(name="lower", type=IntegerType)
ClassesProv_MultiplicityElement.attributes={ClassesProv_MultiplicityElement_upper, ClassesProv_MultiplicityElement_isUnique, ClassesProv_MultiplicityElement_isOrdered, ClassesProv_MultiplicityElement_lower}

# ClassesProv_ValueSpecification class attributes and methods

# TypedElement class attributes and methods

# ClassesProv_Slot class attributes and methods

# ClassesProv_InstanceSpecification class attributes and methods

# ClassesProv_TypedElement class attributes and methods

# ClassesProv_Type class attributes and methods

# ClassesProv_PackageMerge class attributes and methods

# ClassesProv_Relationship class attributes and methods

# ClassesProv_LiteralSpecification class attributes and methods

# ClassesProv_LiteralNull class attributes and methods

# LiteralSpecification class attributes and methods

# ClassesProv_LiteralBoolean class attributes and methods

# ClassesProv_LiteralInteger class attributes and methods

# ClassesProv_LiteralReal class attributes and methods

# ClassesProv_LiteralString class attributes and methods

# ClassesProv_LiteralUnilimitedNatural class attributes and methods

# ClassesProv_InstanceValue class attributes and methods

# ClassesProv_Classifier class attributes and methods
ClassesProv_Classifier_isFinalSpecialization: Property = Property(name="isFinalSpecialization", type=BooleanType)
ClassesProv_Classifier_isAbstract: Property = Property(name="isAbstract", type=BooleanType)
ClassesProv_Classifier.attributes={ClassesProv_Classifier_isAbstract, ClassesProv_Classifier_isFinalSpecialization}

# ClassesProv_StructuralFeature class attributes and methods
ClassesProv_StructuralFeature_isReadOnly: Property = Property(name="isReadOnly", type=BooleanType)
ClassesProv_StructuralFeature.attributes={ClassesProv_StructuralFeature_isReadOnly}

# ClassesProv_RedefinableElement class attributes and methods
ClassesProv_RedefinableElement_isLeaf: Property = Property(name="isLeaf", type=BooleanType)
ClassesProv_RedefinableElement.attributes={ClassesProv_RedefinableElement_isLeaf}

# ClassesProv_Expression class attributes and methods
ClassesProv_Expression_symbol: Property = Property(name="symbol", type=StringType)
ClassesProv_Expression.attributes={ClassesProv_Expression_symbol}

# ValueSpecification class attributes and methods

# ClassesProv_OpaqueExpression class attributes and methods
ClassesProv_OpaqueExpression_body: Property = Property(name="body", type=StringType)
ClassesProv_OpaqueExpression_language: Property = Property(name="language", type=StringType)
ClassesProv_OpaqueExpression.attributes={ClassesProv_OpaqueExpression_body, ClassesProv_OpaqueExpression_language}

# ClassesProv_Feature class attributes and methods
ClassesProv_Feature_isStatic: Property = Property(name="isStatic", type=BooleanType)
ClassesProv_Feature.attributes={ClassesProv_Feature_isStatic}

# ClassesProv_Property class attributes and methods
ClassesProv_Property_isDerived: Property = Property(name="isDerived", type=BooleanType)
ClassesProv_Property_isDerivedUnion: Property = Property(name="isDerivedUnion", type=BooleanType)
ClassesProv_Property_default: Property = Property(name="default", type=StringType)
ClassesProv_Property_isComposite: Property = Property(name="isComposite", type=BooleanType)
ClassesProv_Property_isID: Property = Property(name="isID", type=BooleanType)
ClassesProv_Property.attributes={ClassesProv_Property_isDerivedUnion, ClassesProv_Property_isDerived, ClassesProv_Property_isID, ClassesProv_Property_default, ClassesProv_Property_isComposite}

# ClassesProv_Generalization class attributes and methods
ClassesProv_Generalization_isSubstitutable: Property = Property(name="isSubstitutable", type=BooleanType)
ClassesProv_Generalization.attributes={ClassesProv_Generalization_isSubstitutable}

# ClassesProv_Substitution class attributes and methods

# ClassesProv_GeneralizationSet class attributes and methods
ClassesProv_GeneralizationSet_isCovering: Property = Property(name="isCovering", type=BooleanType)
ClassesProv_GeneralizationSet_isDisjoint: Property = Property(name="isDisjoint", type=BooleanType)
ClassesProv_GeneralizationSet.attributes={ClassesProv_GeneralizationSet_isDisjoint, ClassesProv_GeneralizationSet_isCovering}

# Feature class attributes and methods

# MultiplicityElement class attributes and methods

# StructuralFeature class attributes and methods

# ClassesProv_Class class attributes and methods

# RedefinableElement class attributes and methods

# Type class attributes and methods

# ClassesProv_Association class attributes and methods
ClassesProv_Association_isDerived: Property = Property(name="isDerived", type=BooleanType)
ClassesProv_Association.attributes={ClassesProv_Association_isDerived}

# ClassesProv_DataType class attributes and methods

# ClassesProv_Interface class attributes and methods

# ClassesProv_BehavioralFeature class attributes and methods

# ClassesProv_Parameter class attributes and methods
ClassesProv_Parameter_default: Property = Property(name="default", type=StringType)
ClassesProv_Parameter.attributes={ClassesProv_Parameter_default}

# ClassesProv_Operation class attributes and methods
ClassesProv_Operation_isQuery: Property = Property(name="isQuery", type=BooleanType)
ClassesProv_Operation_isOrdered: Property = Property(name="isOrdered", type=BooleanType)
ClassesProv_Operation_isUnique: Property = Property(name="isUnique", type=BooleanType)
ClassesProv_Operation_upper: Property = Property(name="upper", type=IntegerType)
ClassesProv_Operation_lower: Property = Property(name="lower", type=IntegerType)
ClassesProv_Operation.attributes={ClassesProv_Operation_isQuery, ClassesProv_Operation_isUnique, ClassesProv_Operation_upper, ClassesProv_Operation_isOrdered, ClassesProv_Operation_lower}

# BehavioralFeature class attributes and methods

# Classifier class attributes and methods

# ClassesProv_EnumerationLiteral class attributes and methods

# InstanceSpecification class attributes and methods

# ClassesProv_Usage class attributes and methods

# Dependency class attributes and methods

# ClassesProv_Abstraction class attributes and methods

# ClassesProv_Realization class attributes and methods

# Abstraction class attributes and methods

# Realization class attributes and methods

# ClassesProv_InterfaceRealization class attributes and methods

# ClassesProv_PrimitiveType class attributes and methods

# DataType class attributes and methods

# ClassesProv_Enumeration class attributes and methods

# ClassesProv_AssociationClass class attributes and methods

# Class class attributes and methods

# Association class attributes and methods

# Relationships
ownedElement1: BinaryAssociation = BinaryAssociation(
    name="ownedElement1",
    ends={
        Property(name="ClassesProv_Element", type=ClassesProv_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_Element0", type=ClassesProv_Element, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owner3: BinaryAssociation = BinaryAssociation(
    name="owner3",
    ends={
        Property(name="ClassesProv_Element4", type=ClassesProv_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_Element2", type=ClassesProv_Element, multiplicity=Multiplicity(0, 1))
    }
)
ownedMember13: BinaryAssociation = BinaryAssociation(
    name="ownedMember13",
    ends={
        Property(name="ClassesProv_NamedElement15", type=ClassesProv_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_Namespace14", type=ClassesProv_NamedElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elementImport16: BinaryAssociation = BinaryAssociation(
    name="elementImport16",
    ends={
        Property(name="ClassesProv_ElementImport", type=ClassesProv_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_Namespace17", type=ClassesProv_ElementImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packageImport18: BinaryAssociation = BinaryAssociation(
    name="packageImport18",
    ends={
        Property(name="ClassesProv_PackageImport", type=ClassesProv_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_Namespace19", type=ClassesProv_PackageImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedRule20: BinaryAssociation = BinaryAssociation(
    name="ownedRule20",
    ends={
        Property(name="ClassesProv_Constraint", type=ClassesProv_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_Namespace21", type=ClassesProv_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
importedElement22: BinaryAssociation = BinaryAssociation(
    name="importedElement22",
    ends={
        Property(name="ClassesProv_PackageableElement24", type=ClassesProv_ElementImport, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_ElementImport23", type=ClassesProv_PackageableElement, multiplicity=Multiplicity(1, 1))
    }
)
importingNamespace25: BinaryAssociation = BinaryAssociation(
    name="importingNamespace25",
    ends={
        Property(name="ClassesProv_Namespace27", type=ClassesProv_ElementImport, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_ElementImport26", type=ClassesProv_Namespace, multiplicity=Multiplicity(1, 1))
    }
)
importedPackage28: BinaryAssociation = BinaryAssociation(
    name="importedPackage28",
    ends={
        Property(name="ClassesProv_Package", type=ClassesProv_PackageImport, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_PackageImport29", type=ClassesProv_Package, multiplicity=Multiplicity(1, 1))
    }
)
importingNamespace30: BinaryAssociation = BinaryAssociation(
    name="importingNamespace30",
    ends={
        Property(name="ClassesProv_Namespace32", type=ClassesProv_PackageImport, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_PackageImport31", type=ClassesProv_Namespace, multiplicity=Multiplicity(1, 1))
    }
)
nestedPackage34: BinaryAssociation = BinaryAssociation(
    name="nestedPackage34",
    ends={
        Property(name="ClassesProv_Package35", type=ClassesProv_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_Package33", type=ClassesProv_Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nestingPackage37: BinaryAssociation = BinaryAssociation(
    name="nestingPackage37",
    ends={
        Property(name="ClassesProv_Package38", type=ClassesProv_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_Package36", type=ClassesProv_Package, multiplicity=Multiplicity(0, 1))
    }
)
packagedElement39: BinaryAssociation = BinaryAssociation(
    name="packagedElement39",
    ends={
        Property(name="ClassesProv_PackageableElement41", type=ClassesProv_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_Package40", type=ClassesProv_PackageableElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
namespace5: BinaryAssociation = BinaryAssociation(
    name="namespace5",
    ends={
        Property(name="ClassesProv_Namespace", type=ClassesProv_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_NamedElement", type=ClassesProv_Namespace, multiplicity=Multiplicity(0, 1))
    }
)
clientDependency6: BinaryAssociation = BinaryAssociation(
    name="clientDependency6",
    ends={
        Property(name="ClassesProv_Dependency", type=ClassesProv_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_NamedElement7", type=ClassesProv_Dependency, multiplicity=Multiplicity(0, 9999))
    }
)
importedMember8: BinaryAssociation = BinaryAssociation(
    name="importedMember8",
    ends={
        Property(name="ClassesProv_PackageableElement", type=ClassesProv_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_Namespace9", type=ClassesProv_PackageableElement, multiplicity=Multiplicity(0, 9999))
    }
)
member10: BinaryAssociation = BinaryAssociation(
    name="member10",
    ends={
        Property(name="ClassesProv_NamedElement12", type=ClassesProv_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_Namespace11", type=ClassesProv_NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
target48: BinaryAssociation = BinaryAssociation(
    name="target48",
    ends={
        Property(name="ClassesProv_Element49", type=ClassesProv_DirectedRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_DirectedRelationship", type=ClassesProv_Element, multiplicity=Multiplicity(1, 9999))
    }
)
source50: BinaryAssociation = BinaryAssociation(
    name="source50",
    ends={
        Property(name="ClassesProv_Element52", type=ClassesProv_DirectedRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_DirectedRelationship51", type=ClassesProv_Element, multiplicity=Multiplicity(1, 9999))
    }
)
upperValue53: BinaryAssociation = BinaryAssociation(
    name="upperValue53",
    ends={
        Property(name="ClassesProv_ValueSpecification", type=ClassesProv_MultiplicityElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_MultiplicityElement", type=ClassesProv_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lowerValue54: BinaryAssociation = BinaryAssociation(
    name="lowerValue54",
    ends={
        Property(name="ClassesProv_ValueSpecification56", type=ClassesProv_MultiplicityElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_MultiplicityElement55", type=ClassesProv_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
owningUpper57: BinaryAssociation = BinaryAssociation(
    name="owningUpper57",
    ends={
        Property(name="ClassesProv_MultiplicityElement59", type=ClassesProv_ValueSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_ValueSpecification58", type=ClassesProv_MultiplicityElement, multiplicity=Multiplicity(0, 1))
    }
)
owningLower60: BinaryAssociation = BinaryAssociation(
    name="owningLower60",
    ends={
        Property(name="ClassesProv_MultiplicityElement62", type=ClassesProv_ValueSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_ValueSpecification61", type=ClassesProv_MultiplicityElement, multiplicity=Multiplicity(0, 1))
    }
)
owningConstraint63: BinaryAssociation = BinaryAssociation(
    name="owningConstraint63",
    ends={
        Property(name="ClassesProv_Constraint65", type=ClassesProv_ValueSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_ValueSpecification64", type=ClassesProv_Constraint, multiplicity=Multiplicity(0, 1))
    }
)
owningSlot66: BinaryAssociation = BinaryAssociation(
    name="owningSlot66",
    ends={
        Property(name="ClassesProv_Slot", type=ClassesProv_ValueSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_ValueSpecification67", type=ClassesProv_Slot, multiplicity=Multiplicity(0, 1))
    }
)
owningInstanceSpec68: BinaryAssociation = BinaryAssociation(
    name="owningInstanceSpec68",
    ends={
        Property(name="ClassesProv_InstanceSpecification", type=ClassesProv_ValueSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_ValueSpecification69", type=ClassesProv_InstanceSpecification, multiplicity=Multiplicity(0, 1))
    }
)
type70: BinaryAssociation = BinaryAssociation(
    name="type70",
    ends={
        Property(name="ClassesProv_Type71", type=ClassesProv_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_TypedElement", type=ClassesProv_Type, multiplicity=Multiplicity(0, 1))
    }
)
package72: BinaryAssociation = BinaryAssociation(
    name="package72",
    ends={
        Property(name="ClassesProv_Package74", type=ClassesProv_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_Type73", type=ClassesProv_Package, multiplicity=Multiplicity(0, 1))
    }
)
ownedType42: BinaryAssociation = BinaryAssociation(
    name="ownedType42",
    ends={
        Property(name="ClassesProv_Type", type=ClassesProv_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_Package43", type=ClassesProv_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packageMerge44: BinaryAssociation = BinaryAssociation(
    name="packageMerge44",
    ends={
        Property(name="ClassesProv_PackageMerge", type=ClassesProv_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_Package45", type=ClassesProv_PackageMerge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relatedElement46: BinaryAssociation = BinaryAssociation(
    name="relatedElement46",
    ends={
        Property(name="ClassesProv_Element47", type=ClassesProv_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_Relationship", type=ClassesProv_Element, multiplicity=Multiplicity(1, 9999))
    }
)
instance77: BinaryAssociation = BinaryAssociation(
    name="instance77",
    ends={
        Property(name="ClassesProv_InstanceSpecification78", type=ClassesProv_InstanceValue, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_InstanceValue", type=ClassesProv_InstanceSpecification, multiplicity=Multiplicity(1, 1))
    }
)
slot79: BinaryAssociation = BinaryAssociation(
    name="slot79",
    ends={
        Property(name="ClassesProv_Slot81", type=ClassesProv_InstanceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_InstanceSpecification80", type=ClassesProv_Slot, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specification82: BinaryAssociation = BinaryAssociation(
    name="specification82",
    ends={
        Property(name="ClassesProv_ValueSpecification84", type=ClassesProv_InstanceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_InstanceSpecification83", type=ClassesProv_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
classifier85: BinaryAssociation = BinaryAssociation(
    name="classifier85",
    ends={
        Property(name="ClassesProv_Classifier", type=ClassesProv_InstanceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_InstanceSpecification86", type=ClassesProv_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
context87: BinaryAssociation = BinaryAssociation(
    name="context87",
    ends={
        Property(name="ClassesProv_Namespace89", type=ClassesProv_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_Constraint88", type=ClassesProv_Namespace, multiplicity=Multiplicity(0, 1))
    }
)
constrainedElement90: BinaryAssociation = BinaryAssociation(
    name="constrainedElement90",
    ends={
        Property(name="ClassesProv_Element92", type=ClassesProv_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_Constraint91", type=ClassesProv_Element, multiplicity=Multiplicity(0, 9999))
    }
)
specification93: BinaryAssociation = BinaryAssociation(
    name="specification93",
    ends={
        Property(name="ClassesProv_ValueSpecification95", type=ClassesProv_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_Constraint94", type=ClassesProv_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
owningInstace96: BinaryAssociation = BinaryAssociation(
    name="owningInstace96",
    ends={
        Property(name="ClassesProv_InstanceSpecification98", type=ClassesProv_Slot, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_Slot97", type=ClassesProv_InstanceSpecification, multiplicity=Multiplicity(1, 1))
    }
)
value99: BinaryAssociation = BinaryAssociation(
    name="value99",
    ends={
        Property(name="ClassesProv_ValueSpecification101", type=ClassesProv_Slot, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_Slot100", type=ClassesProv_ValueSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
definingFeature102: BinaryAssociation = BinaryAssociation(
    name="definingFeature102",
    ends={
        Property(name="ClassesProv_StructuralFeature", type=ClassesProv_Slot, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_Slot103", type=ClassesProv_StructuralFeature, multiplicity=Multiplicity(1, 1))
    }
)
redefinedElement105: BinaryAssociation = BinaryAssociation(
    name="redefinedElement105",
    ends={
        Property(name="ClassesProv_RedefinableElement", type=ClassesProv_RedefinableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_RedefinableElement104", type=ClassesProv_RedefinableElement, multiplicity=Multiplicity(0, 9999))
    }
)
operand75: BinaryAssociation = BinaryAssociation(
    name="operand75",
    ends={
        Property(name="ClassesProv_ValueSpecification76", type=ClassesProv_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_Expression", type=ClassesProv_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
inheritedMember109: BinaryAssociation = BinaryAssociation(
    name="inheritedMember109",
    ends={
        Property(name="ClassesProv_NamedElement111", type=ClassesProv_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_Classifier110", type=ClassesProv_NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
feature112: BinaryAssociation = BinaryAssociation(
    name="feature112",
    ends={
        Property(name="ClassesProv_Feature", type=ClassesProv_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_Classifier113", type=ClassesProv_Feature, multiplicity=Multiplicity(0, 9999))
    }
)
attribute114: BinaryAssociation = BinaryAssociation(
    name="attribute114",
    ends={
        Property(name="ClassesProv_Property", type=ClassesProv_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_Classifier115", type=ClassesProv_Property, multiplicity=Multiplicity(0, 9999))
    }
)
redefinedClassifier117: BinaryAssociation = BinaryAssociation(
    name="redefinedClassifier117",
    ends={
        Property(name="ClassesProv_Classifier118", type=ClassesProv_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_Classifier116", type=ClassesProv_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
general120: BinaryAssociation = BinaryAssociation(
    name="general120",
    ends={
        Property(name="ClassesProv_Classifier121", type=ClassesProv_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_Classifier119", type=ClassesProv_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
generalization122: BinaryAssociation = BinaryAssociation(
    name="generalization122",
    ends={
        Property(name="ClassesProv_Generalization", type=ClassesProv_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_Classifier123", type=ClassesProv_Generalization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
substitution124: BinaryAssociation = BinaryAssociation(
    name="substitution124",
    ends={
        Property(name="ClassesProv_Substitution", type=ClassesProv_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_Classifier125", type=ClassesProv_Substitution, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
powertypeExtent126: BinaryAssociation = BinaryAssociation(
    name="powertypeExtent126",
    ends={
        Property(name="ClassesProv_GeneralizationSet", type=ClassesProv_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_Classifier127", type=ClassesProv_GeneralizationSet, multiplicity=Multiplicity(0, 9999))
    }
)
featuringClassifier128: BinaryAssociation = BinaryAssociation(
    name="featuringClassifier128",
    ends={
        Property(name="ClassesProv_Classifier130", type=ClassesProv_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_Feature129", type=ClassesProv_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
class131: BinaryAssociation = BinaryAssociation(
    name="class131",
    ends={
        Property(name="ClassesProv_Class", type=ClassesProv_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_Property132", type=ClassesProv_Class, multiplicity=Multiplicity(0, 1))
    }
)
redefinitionContext106: BinaryAssociation = BinaryAssociation(
    name="redefinitionContext106",
    ends={
        Property(name="ClassesProv_Classifier108", type=ClassesProv_RedefinableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_RedefinableElement107", type=ClassesProv_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
subsettedProperty143: BinaryAssociation = BinaryAssociation(
    name="subsettedProperty143",
    ends={
        Property(name="ClassesProv_Property144", type=ClassesProv_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_Property142", type=ClassesProv_Property, multiplicity=Multiplicity(0, 1))
    }
)
association145: BinaryAssociation = BinaryAssociation(
    name="association145",
    ends={
        Property(name="ClassesProv_Association", type=ClassesProv_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_Property146", type=ClassesProv_Association, multiplicity=Multiplicity(0, 1))
    }
)
owningAssociation147: BinaryAssociation = BinaryAssociation(
    name="owningAssociation147",
    ends={
        Property(name="ClassesProv_Association149", type=ClassesProv_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_Property148", type=ClassesProv_Association, multiplicity=Multiplicity(0, 1))
    }
)
dataType150: BinaryAssociation = BinaryAssociation(
    name="dataType150",
    ends={
        Property(name="ClassesProv_DataType", type=ClassesProv_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_Property151", type=ClassesProv_DataType, multiplicity=Multiplicity(0, 1))
    }
)
interface152: BinaryAssociation = BinaryAssociation(
    name="interface152",
    ends={
        Property(name="ClassesProv_Interface", type=ClassesProv_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_Property153", type=ClassesProv_Interface, multiplicity=Multiplicity(0, 1))
    }
)
qualifier155: BinaryAssociation = BinaryAssociation(
    name="qualifier155",
    ends={
        Property(name="ClassesProv_Property156", type=ClassesProv_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_Property154", type=ClassesProv_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
associationEnd158: BinaryAssociation = BinaryAssociation(
    name="associationEnd158",
    ends={
        Property(name="ClassesProv_Property159", type=ClassesProv_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_Property157", type=ClassesProv_Property, multiplicity=Multiplicity(0, 1))
    }
)
general160: BinaryAssociation = BinaryAssociation(
    name="general160",
    ends={
        Property(name="ClassesProv_Classifier162", type=ClassesProv_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_Generalization161", type=ClassesProv_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
specific163: BinaryAssociation = BinaryAssociation(
    name="specific163",
    ends={
        Property(name="ClassesProv_Classifier165", type=ClassesProv_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_Generalization164", type=ClassesProv_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
generalizationSet166: BinaryAssociation = BinaryAssociation(
    name="generalizationSet166",
    ends={
        Property(name="ClassesProv_GeneralizationSet168", type=ClassesProv_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_Generalization167", type=ClassesProv_GeneralizationSet, multiplicity=Multiplicity(0, 9999))
    }
)
ownedParameter169: BinaryAssociation = BinaryAssociation(
    name="ownedParameter169",
    ends={
        Property(name="ClassesProv_Parameter", type=ClassesProv_BehavioralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_BehavioralFeature", type=ClassesProv_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
raisedException170: BinaryAssociation = BinaryAssociation(
    name="raisedException170",
    ends={
        Property(name="ClassesProv_Type172", type=ClassesProv_BehavioralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_BehavioralFeature171", type=ClassesProv_Type, multiplicity=Multiplicity(0, 1))
    }
)
ownedFormalParam173: BinaryAssociation = BinaryAssociation(
    name="ownedFormalParam173",
    ends={
        Property(name="ClassesProv_BehavioralFeature175", type=ClassesProv_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_Parameter174", type=ClassesProv_BehavioralFeature, multiplicity=Multiplicity(0, 1))
    }
)
defaultValue176: BinaryAssociation = BinaryAssociation(
    name="defaultValue176",
    ends={
        Property(name="ClassesProv_ValueSpecification178", type=ClassesProv_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_Parameter177", type=ClassesProv_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
redefinedProperty134: BinaryAssociation = BinaryAssociation(
    name="redefinedProperty134",
    ends={
        Property(name="ClassesProv_Property135", type=ClassesProv_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_Property133", type=ClassesProv_Property, multiplicity=Multiplicity(0, 9999))
    }
)
defaultValue136: BinaryAssociation = BinaryAssociation(
    name="defaultValue136",
    ends={
        Property(name="ClassesProv_ValueSpecification138", type=ClassesProv_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_Property137", type=ClassesProv_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
opposite140: BinaryAssociation = BinaryAssociation(
    name="opposite140",
    ends={
        Property(name="ClassesProv_Property141", type=ClassesProv_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_Property139", type=ClassesProv_Property, multiplicity=Multiplicity(0, 1))
    }
)
type179: BinaryAssociation = BinaryAssociation(
    name="type179",
    ends={
        Property(name="ClassesProv_Type180", type=ClassesProv_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_Operation", type=ClassesProv_Type, multiplicity=Multiplicity(0, 1))
    }
)
precondition181: BinaryAssociation = BinaryAssociation(
    name="precondition181",
    ends={
        Property(name="ClassesProv_Constraint183", type=ClassesProv_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_Operation182", type=ClassesProv_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bodyCondition184: BinaryAssociation = BinaryAssociation(
    name="bodyCondition184",
    ends={
        Property(name="ClassesProv_Constraint186", type=ClassesProv_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_Operation185", type=ClassesProv_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
postcondition187: BinaryAssociation = BinaryAssociation(
    name="postcondition187",
    ends={
        Property(name="ClassesProv_Constraint189", type=ClassesProv_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_Operation188", type=ClassesProv_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
class190: BinaryAssociation = BinaryAssociation(
    name="class190",
    ends={
        Property(name="ClassesProv_Class192", type=ClassesProv_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_Operation191", type=ClassesProv_Class, multiplicity=Multiplicity(0, 1))
    }
)
dataType193: BinaryAssociation = BinaryAssociation(
    name="dataType193",
    ends={
        Property(name="ClassesProv_DataType195", type=ClassesProv_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_Operation194", type=ClassesProv_DataType, multiplicity=Multiplicity(0, 1))
    }
)
interface196: BinaryAssociation = BinaryAssociation(
    name="interface196",
    ends={
        Property(name="ClassesProv_Interface198", type=ClassesProv_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_Operation197", type=ClassesProv_Interface, multiplicity=Multiplicity(0, 1))
    }
)
nestedClassifier199: BinaryAssociation = BinaryAssociation(
    name="nestedClassifier199",
    ends={
        Property(name="ClassesProv_Classifier201", type=ClassesProv_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_Class200", type=ClassesProv_Classifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedOperation202: BinaryAssociation = BinaryAssociation(
    name="ownedOperation202",
    ends={
        Property(name="ClassesProv_Operation204", type=ClassesProv_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_Class203", type=ClassesProv_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superClass206: BinaryAssociation = BinaryAssociation(
    name="superClass206",
    ends={
        Property(name="ClassesProv_Class207", type=ClassesProv_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_Class205", type=ClassesProv_Class, multiplicity=Multiplicity(0, 9999))
    }
)
ownedAttribute208: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute208",
    ends={
        Property(name="ClassesProv_Property210", type=ClassesProv_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_Class209", type=ClassesProv_Property, multiplicity=Multiplicity(0, 9999))
    }
)
navigableOwnedEnd211: BinaryAssociation = BinaryAssociation(
    name="navigableOwnedEnd211",
    ends={
        Property(name="ClassesProv_Property213", type=ClassesProv_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_Association212", type=ClassesProv_Property, multiplicity=Multiplicity(0, 9999))
    }
)
memberEnd214: BinaryAssociation = BinaryAssociation(
    name="memberEnd214",
    ends={
        Property(name="ClassesProv_Property216", type=ClassesProv_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_Association215", type=ClassesProv_Property, multiplicity=Multiplicity(2, 9999))
    }
)
ownedEnd217: BinaryAssociation = BinaryAssociation(
    name="ownedEnd217",
    ends={
        Property(name="ClassesProv_Property219", type=ClassesProv_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_Association218", type=ClassesProv_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedAttribute220: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute220",
    ends={
        Property(name="ClassesProv_Property222", type=ClassesProv_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_DataType221", type=ClassesProv_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedLiteral226: BinaryAssociation = BinaryAssociation(
    name="ownedLiteral226",
    ends={
        Property(name="ClassesProv_EnumerationLiteral", type=ClassesProv_Enumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_Enumeration", type=ClassesProv_EnumerationLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enumeration227: BinaryAssociation = BinaryAssociation(
    name="enumeration227",
    ends={
        Property(name="ClassesProv_Enumeration229", type=ClassesProv_EnumerationLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_EnumerationLiteral228", type=ClassesProv_Enumeration, multiplicity=Multiplicity(1, 1))
    }
)
receivingPackage230: BinaryAssociation = BinaryAssociation(
    name="receivingPackage230",
    ends={
        Property(name="ClassesProv_Package232", type=ClassesProv_PackageMerge, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_PackageMerge231", type=ClassesProv_Package, multiplicity=Multiplicity(1, 1))
    }
)
mergedPackage233: BinaryAssociation = BinaryAssociation(
    name="mergedPackage233",
    ends={
        Property(name="ClassesProv_Package235", type=ClassesProv_PackageMerge, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_PackageMerge234", type=ClassesProv_Package, multiplicity=Multiplicity(1, 1))
    }
)
client236: BinaryAssociation = BinaryAssociation(
    name="client236",
    ends={
        Property(name="ClassesProv_NamedElement238", type=ClassesProv_Dependency, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_Dependency237", type=ClassesProv_NamedElement, multiplicity=Multiplicity(1, 9999))
    }
)
supplier239: BinaryAssociation = BinaryAssociation(
    name="supplier239",
    ends={
        Property(name="ClassesProv_NamedElement241", type=ClassesProv_Dependency, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_Dependency240", type=ClassesProv_NamedElement, multiplicity=Multiplicity(1, 9999))
    }
)
mapping242: BinaryAssociation = BinaryAssociation(
    name="mapping242",
    ends={
        Property(name="ClassesProv_OpaqueExpression", type=ClassesProv_Abstraction, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_Abstraction", type=ClassesProv_OpaqueExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
substitutingClassifier243: BinaryAssociation = BinaryAssociation(
    name="substitutingClassifier243",
    ends={
        Property(name="ClassesProv_Classifier245", type=ClassesProv_Substitution, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_Substitution244", type=ClassesProv_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
contract246: BinaryAssociation = BinaryAssociation(
    name="contract246",
    ends={
        Property(name="ClassesProv_Classifier248", type=ClassesProv_Substitution, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_Substitution247", type=ClassesProv_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
ownedOperation223: BinaryAssociation = BinaryAssociation(
    name="ownedOperation223",
    ends={
        Property(name="ClassesProv_Operation225", type=ClassesProv_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_DataType224", type=ClassesProv_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contract261: BinaryAssociation = BinaryAssociation(
    name="contract261",
    ends={
        Property(name="ClassesProv_Interface262", type=ClassesProv_InterfaceRealization, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_InterfaceRealization", type=ClassesProv_Interface, multiplicity=Multiplicity(1, 1))
    }
)
powertype263: BinaryAssociation = BinaryAssociation(
    name="powertype263",
    ends={
        Property(name="ClassesProv_Classifier265", type=ClassesProv_GeneralizationSet, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_GeneralizationSet264", type=ClassesProv_Classifier, multiplicity=Multiplicity(0, 1))
    }
)
generalization266: BinaryAssociation = BinaryAssociation(
    name="generalization266",
    ends={
        Property(name="ClassesProv_Generalization268", type=ClassesProv_GeneralizationSet, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_GeneralizationSet267", type=ClassesProv_Generalization, multiplicity=Multiplicity(0, 9999))
    }
)
nestedClassifier249: BinaryAssociation = BinaryAssociation(
    name="nestedClassifier249",
    ends={
        Property(name="ClassesProv_Classifier251", type=ClassesProv_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_Interface250", type=ClassesProv_Classifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
redefinedInterface253: BinaryAssociation = BinaryAssociation(
    name="redefinedInterface253",
    ends={
        Property(name="ClassesProv_Interface254", type=ClassesProv_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_Interface252", type=ClassesProv_Interface, multiplicity=Multiplicity(0, 9999))
    }
)
ownedAttribute255: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute255",
    ends={
        Property(name="ClassesProv_Property257", type=ClassesProv_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_Interface256", type=ClassesProv_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedOperation258: BinaryAssociation = BinaryAssociation(
    name="ownedOperation258",
    ends={
        Property(name="ClassesProv_Operation260", type=ClassesProv_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassesProv_Interface259", type=ClassesProv_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_ClassesProv_NamedElement_Element = Generalization(general=Element, specific=ClassesProv_NamedElement)
gen_ClassesProv_PackageableElement_NamedElement = Generalization(general=NamedElement, specific=ClassesProv_PackageableElement)
gen_ClassesProv_ElementImport_DirectedRelationship = Generalization(general=DirectedRelationship, specific=ClassesProv_ElementImport)
gen_ClassesProv_PackageImport_DirectedRelationship = Generalization(general=DirectedRelationship, specific=ClassesProv_PackageImport)
gen_ClassesProv_Package_Namespace = Generalization(general=Namespace, specific=ClassesProv_Package)
gen_ClassesProv_Package_PackageableElement = Generalization(general=PackageableElement, specific=ClassesProv_Package)
gen_ClassesProv_Namespace_NamedElement = Generalization(general=NamedElement, specific=ClassesProv_Namespace)
gen_ClassesProv_DirectedRelationship_Relationship = Generalization(general=Relationship, specific=ClassesProv_DirectedRelationship)
gen_ClassesProv_MultiplicityElement_Element = Generalization(general=Element, specific=ClassesProv_MultiplicityElement)
gen_ClassesProv_ValueSpecification_TypedElement = Generalization(general=TypedElement, specific=ClassesProv_ValueSpecification)
gen_ClassesProv_ValueSpecification_PackageableElement = Generalization(general=PackageableElement, specific=ClassesProv_ValueSpecification)
gen_ClassesProv_TypedElement_NamedElement = Generalization(general=NamedElement, specific=ClassesProv_TypedElement)
gen_ClassesProv_Type_PackageableElement = Generalization(general=PackageableElement, specific=ClassesProv_Type)
gen_ClassesProv_Relationship_Element = Generalization(general=Element, specific=ClassesProv_Relationship)
gen_ClassesProv_LiteralSpecification_ValueSpecification = Generalization(general=ValueSpecification, specific=ClassesProv_LiteralSpecification)
gen_ClassesProv_LiteralNull_LiteralSpecification = Generalization(general=LiteralSpecification, specific=ClassesProv_LiteralNull)
gen_ClassesProv_LiteralBoolean_LiteralSpecification = Generalization(general=LiteralSpecification, specific=ClassesProv_LiteralBoolean)
gen_ClassesProv_LiteralInteger_LiteralSpecification = Generalization(general=LiteralSpecification, specific=ClassesProv_LiteralInteger)
gen_ClassesProv_LiteralReal_LiteralSpecification = Generalization(general=LiteralSpecification, specific=ClassesProv_LiteralReal)
gen_ClassesProv_LiteralString_LiteralSpecification = Generalization(general=LiteralSpecification, specific=ClassesProv_LiteralString)
gen_ClassesProv_LiteralUnilimitedNatural_LiteralSpecification = Generalization(general=LiteralSpecification, specific=ClassesProv_LiteralUnilimitedNatural)
gen_ClassesProv_InstanceSpecification_PackageableElement = Generalization(general=PackageableElement, specific=ClassesProv_InstanceSpecification)
gen_ClassesProv_Constraint_PackageableElement = Generalization(general=PackageableElement, specific=ClassesProv_Constraint)
gen_ClassesProv_Slot_Element = Generalization(general=Element, specific=ClassesProv_Slot)
gen_ClassesProv_RedefinableElement_NamedElement = Generalization(general=NamedElement, specific=ClassesProv_RedefinableElement)
gen_ClassesProv_Expression_ValueSpecification = Generalization(general=ValueSpecification, specific=ClassesProv_Expression)
gen_ClassesProv_OpaqueExpression_ValueSpecification = Generalization(general=ValueSpecification, specific=ClassesProv_OpaqueExpression)
gen_ClassesProv_Feature_RedefinableElement = Generalization(general=RedefinableElement, specific=ClassesProv_Feature)
gen_ClassesProv_StructuralFeature_Feature = Generalization(general=Feature, specific=ClassesProv_StructuralFeature)
gen_ClassesProv_StructuralFeature_MultiplicityElement = Generalization(general=MultiplicityElement, specific=ClassesProv_StructuralFeature)
gen_ClassesProv_StructuralFeature_TypedElement = Generalization(general=TypedElement, specific=ClassesProv_StructuralFeature)
gen_ClassesProv_Property_StructuralFeature = Generalization(general=StructuralFeature, specific=ClassesProv_Property)
gen_ClassesProv_Classifier_RedefinableElement = Generalization(general=RedefinableElement, specific=ClassesProv_Classifier)
gen_ClassesProv_Classifier_Namespace = Generalization(general=Namespace, specific=ClassesProv_Classifier)
gen_ClassesProv_Classifier_Type = Generalization(general=Type, specific=ClassesProv_Classifier)
gen_ClassesProv_Generalization_DirectedRelationship = Generalization(general=DirectedRelationship, specific=ClassesProv_Generalization)
gen_ClassesProv_BehavioralFeature_Feature = Generalization(general=Feature, specific=ClassesProv_BehavioralFeature)
gen_ClassesProv_BehavioralFeature_Namespace = Generalization(general=Namespace, specific=ClassesProv_BehavioralFeature)
gen_ClassesProv_Parameter_TypedElement = Generalization(general=TypedElement, specific=ClassesProv_Parameter)
gen_ClassesProv_Operation_BehavioralFeature = Generalization(general=BehavioralFeature, specific=ClassesProv_Operation)
gen_ClassesProv_Class_Classifier = Generalization(general=Classifier, specific=ClassesProv_Class)
gen_ClassesProv_Association_Relationship = Generalization(general=Relationship, specific=ClassesProv_Association)
gen_ClassesProv_Association_Classifier = Generalization(general=Classifier, specific=ClassesProv_Association)
gen_ClassesProv_DataType_Classifier = Generalization(general=Classifier, specific=ClassesProv_DataType)
gen_ClassesProv_EnumerationLiteral_InstanceSpecification = Generalization(general=InstanceSpecification, specific=ClassesProv_EnumerationLiteral)
gen_ClassesProv_PackageMerge_DirectedRelationship = Generalization(general=DirectedRelationship, specific=ClassesProv_PackageMerge)
gen_ClassesProv_Dependency_PackageableElement = Generalization(general=PackageableElement, specific=ClassesProv_Dependency)
gen_ClassesProv_Dependency_DirectedRelationship = Generalization(general=DirectedRelationship, specific=ClassesProv_Dependency)
gen_ClassesProv_Usage_Dependency = Generalization(general=Dependency, specific=ClassesProv_Usage)
gen_ClassesProv_Abstraction_Dependency = Generalization(general=Dependency, specific=ClassesProv_Abstraction)
gen_ClassesProv_Realization_Abstraction = Generalization(general=Abstraction, specific=ClassesProv_Realization)
gen_ClassesProv_Substitution_Realization = Generalization(general=Realization, specific=ClassesProv_Substitution)
gen_ClassesProv_InterfaceRealization_Realization = Generalization(general=Realization, specific=ClassesProv_InterfaceRealization)
gen_ClassesProv_PrimitiveType_DataType = Generalization(general=DataType, specific=ClassesProv_PrimitiveType)
gen_ClassesProv_Enumeration_DataType = Generalization(general=DataType, specific=ClassesProv_Enumeration)
gen_ClassesProv_AssociationClass_Class = Generalization(general=Class_, specific=ClassesProv_AssociationClass)
gen_ClassesProv_AssociationClass_Association = Generalization(general=Association, specific=ClassesProv_AssociationClass)
gen_ClassesProv_GeneralizationSet_PackageableElement = Generalization(general=PackageableElement, specific=ClassesProv_GeneralizationSet)
gen_ClassesProv_Interface_Classifier = Generalization(general=Classifier, specific=ClassesProv_Interface)

# Domain Model
domain_model = DomainModel(
    name="ClassesProv",
    types={ClassesProv_Element, ClassesProv_NamedElement, Element, ClassesProv_ElementImport, ClassesProv_PackageImport, ClassesProv_Constraint, DirectedRelationship, ClassesProv_Package, Namespace, PackageableElement, ClassesProv_Namespace, ClassesProv_Dependency, NamedElement, ClassesProv_PackageableElement, ClassesProv_DirectedRelationship, Relationship, ClassesProv_MultiplicityElement, ClassesProv_ValueSpecification, TypedElement, ClassesProv_Slot, ClassesProv_InstanceSpecification, ClassesProv_TypedElement, ClassesProv_Type, ClassesProv_PackageMerge, ClassesProv_Relationship, ClassesProv_LiteralSpecification, ClassesProv_LiteralNull, LiteralSpecification, ClassesProv_LiteralBoolean, ClassesProv_LiteralInteger, ClassesProv_LiteralReal, ClassesProv_LiteralString, ClassesProv_LiteralUnilimitedNatural, ClassesProv_InstanceValue, ClassesProv_Classifier, ClassesProv_StructuralFeature, ClassesProv_RedefinableElement, ClassesProv_Expression, ValueSpecification, ClassesProv_OpaqueExpression, ClassesProv_Feature, ClassesProv_Property, ClassesProv_Generalization, ClassesProv_Substitution, ClassesProv_GeneralizationSet, Feature, MultiplicityElement, StructuralFeature, ClassesProv_Class, RedefinableElement, Type, ClassesProv_Association, ClassesProv_DataType, ClassesProv_Interface, ClassesProv_BehavioralFeature, ClassesProv_Parameter, ClassesProv_Operation, BehavioralFeature, Classifier, ClassesProv_EnumerationLiteral, InstanceSpecification, ClassesProv_Usage, Dependency, ClassesProv_Abstraction, ClassesProv_Realization, Abstraction, Realization, ClassesProv_InterfaceRealization, ClassesProv_PrimitiveType, DataType, ClassesProv_Enumeration, ClassesProv_AssociationClass, Class_, Association},
    associations={ownedElement1, owner3, ownedMember13, elementImport16, packageImport18, ownedRule20, importedElement22, importingNamespace25, importedPackage28, importingNamespace30, nestedPackage34, nestingPackage37, packagedElement39, namespace5, clientDependency6, importedMember8, member10, target48, source50, upperValue53, lowerValue54, owningUpper57, owningLower60, owningConstraint63, owningSlot66, owningInstanceSpec68, type70, package72, ownedType42, packageMerge44, relatedElement46, instance77, slot79, specification82, classifier85, context87, constrainedElement90, specification93, owningInstace96, value99, definingFeature102, redefinedElement105, operand75, inheritedMember109, feature112, attribute114, redefinedClassifier117, general120, generalization122, substitution124, powertypeExtent126, featuringClassifier128, class131, redefinitionContext106, subsettedProperty143, association145, owningAssociation147, dataType150, interface152, qualifier155, associationEnd158, general160, specific163, generalizationSet166, ownedParameter169, raisedException170, ownedFormalParam173, defaultValue176, redefinedProperty134, defaultValue136, opposite140, type179, precondition181, bodyCondition184, postcondition187, class190, dataType193, interface196, nestedClassifier199, ownedOperation202, superClass206, ownedAttribute208, navigableOwnedEnd211, memberEnd214, ownedEnd217, ownedAttribute220, ownedLiteral226, enumeration227, receivingPackage230, mergedPackage233, client236, supplier239, mapping242, substitutingClassifier243, contract246, ownedOperation223, contract261, powertype263, generalization266, nestedClassifier249, redefinedInterface253, ownedAttribute255, ownedOperation258},
    generalizations={gen_ClassesProv_NamedElement_Element, gen_ClassesProv_PackageableElement_NamedElement, gen_ClassesProv_ElementImport_DirectedRelationship, gen_ClassesProv_PackageImport_DirectedRelationship, gen_ClassesProv_Package_Namespace, gen_ClassesProv_Package_PackageableElement, gen_ClassesProv_Namespace_NamedElement, gen_ClassesProv_DirectedRelationship_Relationship, gen_ClassesProv_MultiplicityElement_Element, gen_ClassesProv_ValueSpecification_TypedElement, gen_ClassesProv_ValueSpecification_PackageableElement, gen_ClassesProv_TypedElement_NamedElement, gen_ClassesProv_Type_PackageableElement, gen_ClassesProv_Relationship_Element, gen_ClassesProv_LiteralSpecification_ValueSpecification, gen_ClassesProv_LiteralNull_LiteralSpecification, gen_ClassesProv_LiteralBoolean_LiteralSpecification, gen_ClassesProv_LiteralInteger_LiteralSpecification, gen_ClassesProv_LiteralReal_LiteralSpecification, gen_ClassesProv_LiteralString_LiteralSpecification, gen_ClassesProv_LiteralUnilimitedNatural_LiteralSpecification, gen_ClassesProv_InstanceSpecification_PackageableElement, gen_ClassesProv_Constraint_PackageableElement, gen_ClassesProv_Slot_Element, gen_ClassesProv_RedefinableElement_NamedElement, gen_ClassesProv_Expression_ValueSpecification, gen_ClassesProv_OpaqueExpression_ValueSpecification, gen_ClassesProv_Feature_RedefinableElement, gen_ClassesProv_StructuralFeature_Feature, gen_ClassesProv_StructuralFeature_MultiplicityElement, gen_ClassesProv_StructuralFeature_TypedElement, gen_ClassesProv_Property_StructuralFeature, gen_ClassesProv_Classifier_RedefinableElement, gen_ClassesProv_Classifier_Namespace, gen_ClassesProv_Classifier_Type, gen_ClassesProv_Generalization_DirectedRelationship, gen_ClassesProv_BehavioralFeature_Feature, gen_ClassesProv_BehavioralFeature_Namespace, gen_ClassesProv_Parameter_TypedElement, gen_ClassesProv_Operation_BehavioralFeature, gen_ClassesProv_Class_Classifier, gen_ClassesProv_Association_Relationship, gen_ClassesProv_Association_Classifier, gen_ClassesProv_DataType_Classifier, gen_ClassesProv_EnumerationLiteral_InstanceSpecification, gen_ClassesProv_PackageMerge_DirectedRelationship, gen_ClassesProv_Dependency_PackageableElement, gen_ClassesProv_Dependency_DirectedRelationship, gen_ClassesProv_Usage_Dependency, gen_ClassesProv_Abstraction_Dependency, gen_ClassesProv_Realization_Abstraction, gen_ClassesProv_Substitution_Realization, gen_ClassesProv_InterfaceRealization_Realization, gen_ClassesProv_PrimitiveType_DataType, gen_ClassesProv_Enumeration_DataType, gen_ClassesProv_AssociationClass_Class, gen_ClassesProv_AssociationClass_Association, gen_ClassesProv_GeneralizationSet_PackageableElement, gen_ClassesProv_Interface_Classifier},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)