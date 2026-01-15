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
            EnumerationLiteral(name="public"),
			EnumerationLiteral(name="private"),
			EnumerationLiteral(name="protected"),
			EnumerationLiteral(name="package")
    }
)

AggregationKind: Enumeration = Enumeration(
    name="AggregationKind",
    literals={
            EnumerationLiteral(name="composite"),
			EnumerationLiteral(name="none"),
			EnumerationLiteral(name="shared")
    }
)

# Classes
RefOntoUML_Comment = Class(name="RefOntoUML::Comment")
Element = Class(name="Element")
RefOntoUML_Element = Class(name="RefOntoUML::Element", is_abstract=True)
EModelElement = Class(name="EModelElement")
RefOntoUML_Package = Class(name="RefOntoUML::Package")
Namespace = Class(name="Namespace")
PackageableElement = Class(name="PackageableElement")
RefOntoUML_PackageableElement = Class(name="RefOntoUML::PackageableElement", is_abstract=True)
RefOntoUML_Type = Class(name="RefOntoUML::Type", is_abstract=True)
RefOntoUML_PackageMerge = Class(name="RefOntoUML::PackageMerge")
NamedElement = Class(name="NamedElement")
RefOntoUML_NamedElement = Class(name="RefOntoUML::NamedElement", is_abstract=True)
RefOntoUML_StringExpression = Class(name="RefOntoUML::StringExpression")
DirectedRelationship = Class(name="DirectedRelationship")
RefOntoUML_Dependency = Class(name="RefOntoUML::Dependency")
RefOntoUML_Namespace = Class(name="RefOntoUML::Namespace", is_abstract=True)
RefOntoUML_Relationship = Class(name="RefOntoUML::Relationship", is_abstract=True)
RefOntoUML_DirectedRelationship = Class(name="RefOntoUML::DirectedRelationship", is_abstract=True)
Relationship = Class(name="Relationship")
RefOntoUML_Constraintx = Class(name="RefOntoUML::Constraintx")
RefOntoUML_ElementImport = Class(name="RefOntoUML::ElementImport")
RefOntoUML_PackageImport = Class(name="RefOntoUML::PackageImport")
RefOntoUML_ValueSpecification = Class(name="RefOntoUML::ValueSpecification", is_abstract=True)
TypedElement = Class(name="TypedElement")
RefOntoUML_TypedElement = Class(name="RefOntoUML::TypedElement", is_abstract=True)
RefOntoUML_Association = Class(name="RefOntoUML::Association")
Classifier = Class(name="Classifier")
RefOntoUML_Classifier = Class(name="RefOntoUML::Classifier", is_abstract=True)
RedefinableElement = Class(name="RedefinableElement")
Type = Class(name="Type")
RefOntoUML_Property = Class(name="RefOntoUML::Property")
RefOntoUML_Generalization = Class(name="RefOntoUML::Generalization")
RefOntoUML_GeneralizationSet = Class(name="RefOntoUML::GeneralizationSet")
RefOntoUML_Feature = Class(name="RefOntoUML::Feature", is_abstract=True)
RefOntoUML_RedefinableElement = Class(name="RefOntoUML::RedefinableElement", is_abstract=True)
RefOntoUML_OpaqueExpression = Class(name="RefOntoUML::OpaqueExpression")
ValueSpecification = Class(name="ValueSpecification")
RefOntoUML_MultiplicityElement = Class(name="RefOntoUML::MultiplicityElement", is_abstract=True)
StructuralFeature = Class(name="StructuralFeature")
RefOntoUML_Class = Class(name="RefOntoUML::Class")
RefOntoUML_DataType = Class(name="RefOntoUML::DataType")
RefOntoUML_Model = Class(name="RefOntoUML::Model")
Package = Class(name="Package")
RefOntoUML_StructuralFeature = Class(name="RefOntoUML::StructuralFeature", is_abstract=True)
Feature = Class(name="Feature")
MultiplicityElement = Class(name="MultiplicityElement")
Expression = Class(name="Expression")
RefOntoUML_Expression = Class(name="RefOntoUML::Expression")
RefOntoUML_InstanceSpecification = Class(name="RefOntoUML::InstanceSpecification")
RefOntoUML_Slot = Class(name="RefOntoUML::Slot")
RefOntoUML_EnumerationLiteral = Class(name="RefOntoUML::EnumerationLiteral")
InstanceSpecification = Class(name="InstanceSpecification")
RefOntoUML_LiteralSpecification = Class(name="RefOntoUML::LiteralSpecification", is_abstract=True)
RefOntoUML_Enumeration = Class(name="RefOntoUML::Enumeration")
DataType = Class(name="DataType")
RefOntoUML_ReferenceStructure = Class(name="RefOntoUML::ReferenceStructure", is_abstract=True)
RefOntoUML_ReferenceRegion = Class(name="RefOntoUML::ReferenceRegion", is_abstract=True)
RefOntoUML_NominalStructure = Class(name="RefOntoUML::NominalStructure")
ReferenceStructure = Class(name="ReferenceStructure")
RefOntoUML_MeasurementEnumeration = Class(name="RefOntoUML::MeasurementEnumeration")
Enumeration_ = Class(name="Enumeration")
RefOntoUML_MeasurementStructure = Class(name="RefOntoUML::MeasurementStructure", is_abstract=True)
RefOntoUML_MeasurementLiteral = Class(name="RefOntoUML::MeasurementLiteral")
EnumerationLiteral = Class(name="EnumerationLiteral")
RefOntoUML_MeasurementRegion = Class(name="RefOntoUML::MeasurementRegion", is_abstract=True)
RefOntoUML_PrimitiveType = Class(name="RefOntoUML::PrimitiveType")
RefOntoUML_MeasurementDomain = Class(name="RefOntoUML::MeasurementDomain")
RefOntoUML_BasicMeasurementRegion = Class(name="RefOntoUML::BasicMeasurementRegion", is_abstract=True)
RefOntoUML_StringNominalStructure = Class(name="RefOntoUML::StringNominalStructure")
NominalStructure = Class(name="NominalStructure")
RefOntoUML_MeasurementDimension = Class(name="RefOntoUML::MeasurementDimension", is_abstract=True)
MeasurementStructure = Class(name="MeasurementStructure")
RefOntoUML_DecimalIntervalDimension = Class(name="RefOntoUML::DecimalIntervalDimension")
RefOntoUML_OrdinalDimension = Class(name="RefOntoUML::OrdinalDimension", is_abstract=True)
MeasurementDimension = Class(name="MeasurementDimension")
RefOntoUML_IntegerOrdinalDimension = Class(name="RefOntoUML::IntegerOrdinalDimension")
OrdinalDimension = Class(name="OrdinalDimension")
RefOntoUML_DecimalOrdinalDimension = Class(name="RefOntoUML::DecimalOrdinalDimension")
RefOntoUML_IntervalDimension = Class(name="RefOntoUML::IntervalDimension", is_abstract=True)
RefOntoUML_IntegerIntervalDimension = Class(name="RefOntoUML::IntegerIntervalDimension")
IntervalDimension = Class(name="IntervalDimension")
RefOntoUML_DecimalRationalDimension = Class(name="RefOntoUML::DecimalRationalDimension")
RefOntoUML_RationalDimension = Class(name="RefOntoUML::RationalDimension", is_abstract=True)
RefOntoUML_IntegerRationalDimension = Class(name="RefOntoUML::IntegerRationalDimension")
RationalDimension = Class(name="RationalDimension")
ReferenceRegion = Class(name="ReferenceRegion")
MeasurementRegion = Class(name="MeasurementRegion")
RefOntoUML_DecimalMeasurementRegion = Class(name="RefOntoUML::DecimalMeasurementRegion")
BasicMeasurementRegion = Class(name="BasicMeasurementRegion")
LiteralDecimal = Class(name="LiteralDecimal")
RefOntoUML_IntegerMeasurementRegion = Class(name="RefOntoUML::IntegerMeasurementRegion")
LiteralInteger = Class(name="LiteralInteger")
RefOntoUML_ComposedMeasurementRegion = Class(name="RefOntoUML::ComposedMeasurementRegion")
RefOntoUML_NominalRegion = Class(name="RefOntoUML::NominalRegion", is_abstract=True)
RefOntoUML_StringNominalRegion = Class(name="RefOntoUML::StringNominalRegion")
NominalRegion = Class(name="NominalRegion")
LiteralString = Class(name="LiteralString")
RefOntoUML_LiteralInteger = Class(name="RefOntoUML::LiteralInteger")
LiteralSpecification = Class(name="LiteralSpecification")
RefOntoUML_LiteralDecimal = Class(name="RefOntoUML::LiteralDecimal")
RefOntoUML_LiteralString = Class(name="RefOntoUML::LiteralString")
RefOntoUML_InstanceValue = Class(name="RefOntoUML::InstanceValue")
RefOntoUML_LiteralBoolean = Class(name="RefOntoUML::LiteralBoolean")
RefOntoUML_LiteralNull = Class(name="RefOntoUML::LiteralNull")
RefOntoUML_MixinClass = Class(name="RefOntoUML::MixinClass", is_abstract=True)
RefOntoUML_LiteralUnlimitedNatural = Class(name="RefOntoUML::LiteralUnlimitedNatural")
RefOntoUML_ObjectClass = Class(name="RefOntoUML::ObjectClass", is_abstract=True)
Class_ = Class(name="Class")
RefOntoUML_MomentClass = Class(name="RefOntoUML::MomentClass", is_abstract=True)
RefOntoUML_SortalClass = Class(name="RefOntoUML::SortalClass", is_abstract=True)
ObjectClass = Class(name="ObjectClass")
RefOntoUML_Phase = Class(name="RefOntoUML::Phase")
AntiRigidSortalClass = Class(name="AntiRigidSortalClass")
RefOntoUML_RigidSortalClass = Class(name="RefOntoUML::RigidSortalClass", is_abstract=True)
SortalClass = Class(name="SortalClass")
RefOntoUML_AntiRigidSortalClass = Class(name="RefOntoUML::AntiRigidSortalClass", is_abstract=True)
RefOntoUML_SubstanceSortal = Class(name="RefOntoUML::SubstanceSortal", is_abstract=True)
RigidSortalClass = Class(name="RigidSortalClass")
RefOntoUML_SubKind = Class(name="RefOntoUML::SubKind")
RefOntoUML_Kind = Class(name="RefOntoUML::Kind")
SubstanceSortal = Class(name="SubstanceSortal")
RefOntoUML_Quantity = Class(name="RefOntoUML::Quantity")
RefOntoUML_Collective = Class(name="RefOntoUML::Collective")
RefOntoUML_Role = Class(name="RefOntoUML::Role")
RefOntoUML_RigidMixinClass = Class(name="RefOntoUML::RigidMixinClass", is_abstract=True)
MixinClass = Class(name="MixinClass")
RefOntoUML_NonRigidMixinClass = Class(name="RefOntoUML::NonRigidMixinClass", is_abstract=True)
RefOntoUML_Category = Class(name="RefOntoUML::Category")
RigidMixinClass = Class(name="RigidMixinClass")
RefOntoUML_AntiRigidMixinClass = Class(name="RefOntoUML::AntiRigidMixinClass", is_abstract=True)
NonRigidMixinClass = Class(name="NonRigidMixinClass")
RefOntoUML_SemiRigidMixinClass = Class(name="RefOntoUML::SemiRigidMixinClass", is_abstract=True)
RefOntoUML_RoleMixin = Class(name="RefOntoUML::RoleMixin")
AntiRigidMixinClass = Class(name="AntiRigidMixinClass")
RefOntoUML_NominalQuality = Class(name="RefOntoUML::NominalQuality")
RefOntoUML_NonPerceivableQuality = Class(name="RefOntoUML::NonPerceivableQuality")
MeasurableQuality = Class(name="MeasurableQuality")
RefOntoUML_PerceivableQuality = Class(name="RefOntoUML::PerceivableQuality")
RefOntoUML_Mixin = Class(name="RefOntoUML::Mixin")
SemiRigidMixinClass = Class(name="SemiRigidMixinClass")
RefOntoUML_IntrinsicMomentClass = Class(name="RefOntoUML::IntrinsicMomentClass", is_abstract=True)
MomentClass = Class(name="MomentClass")
RefOntoUML_Mode = Class(name="RefOntoUML::Mode")
IntrinsicMomentClass = Class(name="IntrinsicMomentClass")
RefOntoUML_Quality = Class(name="RefOntoUML::Quality", is_abstract=True)
RefOntoUML_MeasurableQuality = Class(name="RefOntoUML::MeasurableQuality", is_abstract=True)
Quality = Class(name="Quality")
RefOntoUML_Relator = Class(name="RefOntoUML::Relator")
RefOntoUML_DirectedBinaryAssociation = Class(name="RefOntoUML::DirectedBinaryAssociation", is_abstract=True)
Association = Class(name="Association")
RefOntoUML_Meronymic = Class(name="RefOntoUML::Meronymic", is_abstract=True)
DirectedBinaryAssociation = Class(name="DirectedBinaryAssociation")
RefOntoUML_componentOf = Class(name="RefOntoUML::componentOf")
RefOntoUML_subQuantityOf = Class(name="RefOntoUML::subQuantityOf")
Meronymic = Class(name="Meronymic")
RefOntoUML_subCollectionOf = Class(name="RefOntoUML::subCollectionOf")
RefOntoUML_memberOf = Class(name="RefOntoUML::memberOf")
RefOntoUML_DependencyRelationship = Class(name="RefOntoUML::DependencyRelationship", is_abstract=True)
RefOntoUML_Characterization = Class(name="RefOntoUML::Characterization")
DependencyRelationship = Class(name="DependencyRelationship")
RefOntoUML_Mediation = Class(name="RefOntoUML::Mediation")
RefOntoUML_FormalAssociation = Class(name="RefOntoUML::FormalAssociation")
RefOntoUML_Derivation = Class(name="RefOntoUML::Derivation")
RefOntoUML_Structuration = Class(name="RefOntoUML::Structuration")
RefOntoUML_MaterialAssociation = Class(name="RefOntoUML::MaterialAssociation")

# RefOntoUML_Comment class attributes and methods
RefOntoUML_Comment_body: Property = Property(name="body", type=StringType)
RefOntoUML_Comment.attributes={RefOntoUML_Comment_body}

# Element class attributes and methods

# RefOntoUML_Element class attributes and methods
RefOntoUML_Element_m_not_own_self: Method = Method(name="not_own_self", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
RefOntoUML_Element_m_destroy: Method = Method(name="destroy", parameters={})
RefOntoUML_Element_m_hasKeyword: Method = Method(name="hasKeyword", parameters={Parameter(name='keyword')}, type=StringType)
RefOntoUML_Element_m_getKeywords: Method = Method(name="getKeywords", parameters={}, type=StringType)
RefOntoUML_Element_m_addKeyword: Method = Method(name="addKeyword", parameters={Parameter(name='keyword')}, type=StringType)
RefOntoUML_Element_m_removeKeyword: Method = Method(name="removeKeyword", parameters={Parameter(name='keyword')}, type=StringType)
RefOntoUML_Element_m_getNearestPackage: Method = Method(name="getNearestPackage", parameters={}, type=StringType)
RefOntoUML_Element_m_getModel: Method = Method(name="getModel", parameters={}, type=StringType)
RefOntoUML_Element_m_getApplicableStereotype: Method = Method(name="getApplicableStereotype", parameters={Parameter(name='qualifiedName')})
RefOntoUML_Element_m_has_owner: Method = Method(name="has_owner", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
RefOntoUML_Element_m_getRequiredStereotype: Method = Method(name="getRequiredStereotype", parameters={Parameter(name='qualifiedName')})
RefOntoUML_Element_m_getAppliedStereotype: Method = Method(name="getAppliedStereotype", parameters={Parameter(name='qualifiedName')})
RefOntoUML_Element_m_createEAnnotation: Method = Method(name="createEAnnotation", parameters={Parameter(name='source')}, type=StringType)
RefOntoUML_Element_m_getRelationships: Method = Method(name="getRelationships", parameters={}, type=StringType)
RefOntoUML_Element_m_getRelationships: Method = Method(name="getRelationships", parameters={Parameter(name='eClass')}, type=StringType)
RefOntoUML_Element_m_getStereotypeApplications: Method = Method(name="getStereotypeApplications", parameters={}, type=StringType)
RefOntoUML_Element_m_getTargetDirectedRelationships: Method = Method(name="getTargetDirectedRelationships", parameters={Parameter(name='eClass')}, type=StringType)
RefOntoUML_Element_m_allOwnedElements: Method = Method(name="allOwnedElements", parameters={}, type=Element)
RefOntoUML_Element_m_mustBeOwned: Method = Method(name="mustBeOwned", parameters={}, type=StringType)
RefOntoUML_Element_m_getSourceDirectedRelationships: Method = Method(name="getSourceDirectedRelationships", parameters={}, type=StringType)
RefOntoUML_Element_m_getSourceDirectedRelationships: Method = Method(name="getSourceDirectedRelationships", parameters={Parameter(name='eClass')}, type=StringType)
RefOntoUML_Element_m_getTargetDirectedRelationships: Method = Method(name="getTargetDirectedRelationships", parameters={}, type=StringType)
RefOntoUML_Element.methods={RefOntoUML_Element_m_createEAnnotation, RefOntoUML_Element_m_getRequiredStereotype, RefOntoUML_Element_m_has_owner, RefOntoUML_Element_m_getSourceDirectedRelationships, RefOntoUML_Element_m_getKeywords, RefOntoUML_Element_m_getRelationships, RefOntoUML_Element_m_destroy, RefOntoUML_Element_m_removeKeyword, RefOntoUML_Element_m_getRelationships, RefOntoUML_Element_m_getSourceDirectedRelationships, RefOntoUML_Element_m_getNearestPackage, RefOntoUML_Element_m_getAppliedStereotype, RefOntoUML_Element_m_allOwnedElements, RefOntoUML_Element_m_getTargetDirectedRelationships, RefOntoUML_Element_m_mustBeOwned, RefOntoUML_Element_m_addKeyword, RefOntoUML_Element_m_not_own_self, RefOntoUML_Element_m_getStereotypeApplications, RefOntoUML_Element_m_getModel, RefOntoUML_Element_m_hasKeyword, RefOntoUML_Element_m_getApplicableStereotype, RefOntoUML_Element_m_getTargetDirectedRelationships}

# EModelElement class attributes and methods

# RefOntoUML_Package class attributes and methods
RefOntoUML_Package_m_elements_public_or_private: Method = Method(name="elements_public_or_private", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
RefOntoUML_Package_m_createOwnedClass: Method = Method(name="createOwnedClass", parameters={Parameter(name='isAbstract'), Parameter(name='name')}, type=StringType)
RefOntoUML_Package_m_createOwnedEnumeration: Method = Method(name="createOwnedEnumeration", parameters={Parameter(name='name')}, type=StringType)
RefOntoUML_Package_m_getAppliedProfile: Method = Method(name="getAppliedProfile", parameters={Parameter(name='qualifiedName')})
RefOntoUML_Package_m_getAppliedProfile: Method = Method(name="getAppliedProfile", parameters={Parameter(name='qualifiedName'), Parameter(name='recurse')})
RefOntoUML_Package_m_isModelLibrary: Method = Method(name="isModelLibrary", parameters={}, type=StringType)
RefOntoUML_Package_m_visibleMembers: Method = Method(name="visibleMembers", parameters={}, type=PackageableElement)
RefOntoUML_Package_m_makesVisible: Method = Method(name="makesVisible", parameters={Parameter(name='el')}, type=StringType)
RefOntoUML_Package_m_createOwnedPrimitiveType: Method = Method(name="createOwnedPrimitiveType", parameters={Parameter(name='name')}, type=StringType)
RefOntoUML_Package_m_createOwnedInterface: Method = Method(name="createOwnedInterface", parameters={Parameter(name='name')})
RefOntoUML_Package.methods={RefOntoUML_Package_m_createOwnedClass, RefOntoUML_Package_m_visibleMembers, RefOntoUML_Package_m_getAppliedProfile, RefOntoUML_Package_m_isModelLibrary, RefOntoUML_Package_m_makesVisible, RefOntoUML_Package_m_createOwnedEnumeration, RefOntoUML_Package_m_createOwnedInterface, RefOntoUML_Package_m_createOwnedPrimitiveType, RefOntoUML_Package_m_elements_public_or_private, RefOntoUML_Package_m_getAppliedProfile}

# Namespace class attributes and methods

# PackageableElement class attributes and methods

# RefOntoUML_PackageableElement class attributes and methods

# RefOntoUML_Type class attributes and methods
RefOntoUML_Type_m_createAssociation: Method = Method(name="createAssociation", parameters={Parameter(name='end2Upper'), Parameter(name='end1Name'), Parameter(name='end1Lower'), Parameter(name='end1IsNavigable'), Parameter(name='end2Name'), Parameter(name='end2Lower'), Parameter(name='end2IsNavigable'), Parameter(name='end1Upper'), Parameter(name='end2Aggregation'), Parameter(name='end1Aggregation'), Parameter(name='end1Type')}, type=StringType)
RefOntoUML_Type_m_getAssociations: Method = Method(name="getAssociations", parameters={}, type=StringType)
RefOntoUML_Type_m_conformsTo: Method = Method(name="conformsTo", parameters={Parameter(name='other')}, type=StringType)
RefOntoUML_Type.methods={RefOntoUML_Type_m_conformsTo, RefOntoUML_Type_m_createAssociation, RefOntoUML_Type_m_getAssociations}

# RefOntoUML_PackageMerge class attributes and methods

# NamedElement class attributes and methods

# RefOntoUML_NamedElement class attributes and methods
RefOntoUML_NamedElement_name: Property = Property(name="name", type=StringType)
RefOntoUML_NamedElement_visibility: Property = Property(name="visibility", type=StringType)
RefOntoUML_NamedElement_qualifiedName: Property = Property(name="qualifiedName", type=StringType)
RefOntoUML_NamedElement_m_has_qualified_name: Method = Method(name="has_qualified_name", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
RefOntoUML_NamedElement_m_visibility_needs_ownership: Method = Method(name="visibility_needs_ownership", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
RefOntoUML_NamedElement_m_has_no_qualified_name: Method = Method(name="has_no_qualified_name", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
RefOntoUML_NamedElement_m_allNamespaces: Method = Method(name="allNamespaces", parameters={}, type=Namespace)
RefOntoUML_NamedElement_m_isDistinguishableFrom: Method = Method(name="isDistinguishableFrom", parameters={Parameter(name='n'), Parameter(name='ns')}, type=StringType)
RefOntoUML_NamedElement_m_createDependency: Method = Method(name="createDependency", parameters={Parameter(name='supplier')}, type=StringType)
RefOntoUML_NamedElement_m_getLabel: Method = Method(name="getLabel", parameters={}, type=StringType)
RefOntoUML_NamedElement_m_getLabel: Method = Method(name="getLabel", parameters={Parameter(name='localize')}, type=StringType)
RefOntoUML_NamedElement_m_createUsage: Method = Method(name="createUsage", parameters={Parameter(name='supplier')})
RefOntoUML_NamedElement_m_getQualifiedName: Method = Method(name="getQualifiedName", parameters={}, type=StringType)
RefOntoUML_NamedElement_m_separator: Method = Method(name="separator", parameters={}, type=StringType)
RefOntoUML_NamedElement_m_allOwningPackages: Method = Method(name="allOwningPackages", parameters={}, type=StringType)
RefOntoUML_NamedElement.attributes={RefOntoUML_NamedElement_visibility, RefOntoUML_NamedElement_qualifiedName, RefOntoUML_NamedElement_name}
RefOntoUML_NamedElement.methods={RefOntoUML_NamedElement_m_getQualifiedName, RefOntoUML_NamedElement_m_getLabel, RefOntoUML_NamedElement_m_isDistinguishableFrom, RefOntoUML_NamedElement_m_has_qualified_name, RefOntoUML_NamedElement_m_allNamespaces, RefOntoUML_NamedElement_m_visibility_needs_ownership, RefOntoUML_NamedElement_m_allOwningPackages, RefOntoUML_NamedElement_m_createDependency, RefOntoUML_NamedElement_m_has_no_qualified_name, RefOntoUML_NamedElement_m_separator, RefOntoUML_NamedElement_m_createUsage, RefOntoUML_NamedElement_m_getLabel}

# RefOntoUML_StringExpression class attributes and methods
RefOntoUML_StringExpression_m_subexpressions: Method = Method(name="subexpressions", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
RefOntoUML_StringExpression_m_operands: Method = Method(name="operands", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
RefOntoUML_StringExpression.methods={RefOntoUML_StringExpression_m_subexpressions, RefOntoUML_StringExpression_m_operands}

# DirectedRelationship class attributes and methods

# RefOntoUML_Dependency class attributes and methods

# RefOntoUML_Namespace class attributes and methods
RefOntoUML_Namespace_m_getImportedElements: Method = Method(name="getImportedElements", parameters={}, type=PackageableElement)
RefOntoUML_Namespace_m_getImportedPackages: Method = Method(name="getImportedPackages", parameters={}, type=StringType)
RefOntoUML_Namespace_m_members_distinguishable: Method = Method(name="members_distinguishable", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
RefOntoUML_Namespace_m_createElementImport: Method = Method(name="createElementImport", parameters={Parameter(name='visibility'), Parameter(name='element')}, type=StringType)
RefOntoUML_Namespace_m_createPackageImport: Method = Method(name="createPackageImport", parameters={Parameter(name='visibility'), Parameter(name='package_')}, type=StringType)
RefOntoUML_Namespace_m_getImportedMembers: Method = Method(name="getImportedMembers", parameters={}, type=PackageableElement)
RefOntoUML_Namespace_m_getNamesOfMember: Method = Method(name="getNamesOfMember", parameters={Parameter(name='element')}, type=StringType)
RefOntoUML_Namespace_m_membersAreDistinguishable: Method = Method(name="membersAreDistinguishable", parameters={}, type=StringType)
RefOntoUML_Namespace_m_importMembers: Method = Method(name="importMembers", parameters={Parameter(name='imps')}, type=PackageableElement)
RefOntoUML_Namespace_m_excludeCollisions: Method = Method(name="excludeCollisions", parameters={Parameter(name='imps')}, type=PackageableElement)
RefOntoUML_Namespace.methods={RefOntoUML_Namespace_m_membersAreDistinguishable, RefOntoUML_Namespace_m_getImportedPackages, RefOntoUML_Namespace_m_getNamesOfMember, RefOntoUML_Namespace_m_members_distinguishable, RefOntoUML_Namespace_m_importMembers, RefOntoUML_Namespace_m_createElementImport, RefOntoUML_Namespace_m_excludeCollisions, RefOntoUML_Namespace_m_getImportedMembers, RefOntoUML_Namespace_m_getImportedElements, RefOntoUML_Namespace_m_createPackageImport}

# RefOntoUML_Relationship class attributes and methods

# RefOntoUML_DirectedRelationship class attributes and methods

# Relationship class attributes and methods

# RefOntoUML_Constraintx class attributes and methods
RefOntoUML_Constraintx_m_no_side_effects: Method = Method(name="no_side_effects", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
RefOntoUML_Constraintx_m_not_apply_to_self: Method = Method(name="not_apply_to_self", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
RefOntoUML_Constraintx_m_value_specification_boolean: Method = Method(name="value_specification_boolean", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
RefOntoUML_Constraintx_m_boolean_value: Method = Method(name="boolean_value", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
RefOntoUML_Constraintx_m_not_applied_to_self: Method = Method(name="not_applied_to_self", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
RefOntoUML_Constraintx.methods={RefOntoUML_Constraintx_m_not_applied_to_self, RefOntoUML_Constraintx_m_no_side_effects, RefOntoUML_Constraintx_m_boolean_value, RefOntoUML_Constraintx_m_value_specification_boolean, RefOntoUML_Constraintx_m_not_apply_to_self}

# RefOntoUML_ElementImport class attributes and methods
RefOntoUML_ElementImport_visibility: Property = Property(name="visibility", type=StringType)
RefOntoUML_ElementImport_alias: Property = Property(name="alias", type=StringType)
RefOntoUML_ElementImport_m_imported_element_is_public: Method = Method(name="imported_element_is_public", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
RefOntoUML_ElementImport_m_visibility_public_or_private: Method = Method(name="visibility_public_or_private", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
RefOntoUML_ElementImport_m_getName: Method = Method(name="getName", parameters={}, type=StringType)
RefOntoUML_ElementImport.attributes={RefOntoUML_ElementImport_visibility, RefOntoUML_ElementImport_alias}
RefOntoUML_ElementImport.methods={RefOntoUML_ElementImport_m_getName, RefOntoUML_ElementImport_m_visibility_public_or_private, RefOntoUML_ElementImport_m_imported_element_is_public}

# RefOntoUML_PackageImport class attributes and methods
RefOntoUML_PackageImport_visibility: Property = Property(name="visibility", type=StringType)
RefOntoUML_PackageImport_m_public_or_private: Method = Method(name="public_or_private", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
RefOntoUML_PackageImport.attributes={RefOntoUML_PackageImport_visibility}
RefOntoUML_PackageImport.methods={RefOntoUML_PackageImport_m_public_or_private}

# RefOntoUML_ValueSpecification class attributes and methods
RefOntoUML_ValueSpecification_m_isComputable: Method = Method(name="isComputable", parameters={}, type=StringType)
RefOntoUML_ValueSpecification_m_integerValue: Method = Method(name="integerValue", parameters={}, type=StringType)
RefOntoUML_ValueSpecification_m_booleanValue: Method = Method(name="booleanValue", parameters={}, type=StringType)
RefOntoUML_ValueSpecification_m_stringValue: Method = Method(name="stringValue", parameters={}, type=StringType)
RefOntoUML_ValueSpecification_m_unlimitedValue: Method = Method(name="unlimitedValue", parameters={}, type=StringType)
RefOntoUML_ValueSpecification_m_isNull: Method = Method(name="isNull", parameters={}, type=StringType)
RefOntoUML_ValueSpecification.methods={RefOntoUML_ValueSpecification_m_stringValue, RefOntoUML_ValueSpecification_m_integerValue, RefOntoUML_ValueSpecification_m_unlimitedValue, RefOntoUML_ValueSpecification_m_isComputable, RefOntoUML_ValueSpecification_m_booleanValue, RefOntoUML_ValueSpecification_m_isNull}

# TypedElement class attributes and methods

# RefOntoUML_TypedElement class attributes and methods

# RefOntoUML_Association class attributes and methods
RefOntoUML_Association_isDerived: Property = Property(name="isDerived", type=StringType)
RefOntoUML_Association_m_isBinary: Method = Method(name="isBinary", parameters={}, type=StringType)
RefOntoUML_Association_m_getEndTypes: Method = Method(name="getEndTypes", parameters={}, type=StringType)
RefOntoUML_Association_m_specialized_end_number: Method = Method(name="specialized_end_number", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
RefOntoUML_Association_m_specialized_end_types: Method = Method(name="specialized_end_types", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
RefOntoUML_Association_m_binary_associations: Method = Method(name="binary_associations", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
RefOntoUML_Association_m_association_ends: Method = Method(name="association_ends", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
RefOntoUML_Association.attributes={RefOntoUML_Association_isDerived}
RefOntoUML_Association.methods={RefOntoUML_Association_m_specialized_end_number, RefOntoUML_Association_m_association_ends, RefOntoUML_Association_m_binary_associations, RefOntoUML_Association_m_specialized_end_types, RefOntoUML_Association_m_isBinary, RefOntoUML_Association_m_getEndTypes}

# Classifier class attributes and methods

# RefOntoUML_Classifier class attributes and methods
RefOntoUML_Classifier_isAbstract: Property = Property(name="isAbstract", type=StringType)
RefOntoUML_Classifier_m_getAllAttributes: Method = Method(name="getAllAttributes", parameters={}, type=StringType)
RefOntoUML_Classifier_m_no_cycles_in_generalization: Method = Method(name="no_cycles_in_generalization", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
RefOntoUML_Classifier_m_generalization_hierarchies: Method = Method(name="generalization_hierarchies", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
RefOntoUML_Classifier_m_specialize_type: Method = Method(name="specialize_type", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
RefOntoUML_Classifier_m_maps_to_generalization_set: Method = Method(name="maps_to_generalization_set", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
RefOntoUML_Classifier_m_inherit: Method = Method(name="inherit", parameters={Parameter(name='inhs')}, type=NamedElement)
RefOntoUML_Classifier_m_maySpecializeType: Method = Method(name="maySpecializeType", parameters={Parameter(name='c')}, type=StringType)
RefOntoUML_Classifier_m_allParents: Method = Method(name="allParents", parameters={}, type=Classifier)
RefOntoUML_Classifier_m_getGenerals: Method = Method(name="getGenerals", parameters={}, type=Classifier)
RefOntoUML_Classifier_m_getInheritedMembers: Method = Method(name="getInheritedMembers", parameters={}, type=NamedElement)
RefOntoUML_Classifier_m_allFeatures: Method = Method(name="allFeatures", parameters={}, type=StringType)
RefOntoUML_Classifier_m_parents: Method = Method(name="parents", parameters={}, type=Classifier)
RefOntoUML_Classifier_m_inheritableMembers: Method = Method(name="inheritableMembers", parameters={Parameter(name='c')}, type=NamedElement)
RefOntoUML_Classifier_m_hasVisibilityOf: Method = Method(name="hasVisibilityOf", parameters={Parameter(name='n')}, type=StringType)
RefOntoUML_Classifier_m_conformsTo: Method = Method(name="conformsTo", parameters={Parameter(name='other')}, type=StringType)
RefOntoUML_Classifier_m_allChildren: Method = Method(name="allChildren", parameters={}, type=Classifier)
RefOntoUML_Classifier_m_partitions: Method = Method(name="partitions", parameters={}, type=StringType)
RefOntoUML_Classifier_m_hasKindAncestor: Method = Method(name="hasKindAncestor", parameters={}, type=BooleanType)
RefOntoUML_Classifier_m_hasQuantityAncestor: Method = Method(name="hasQuantityAncestor", parameters={}, type=BooleanType)
RefOntoUML_Classifier_m_hasCollectiveAncestor: Method = Method(name="hasCollectiveAncestor", parameters={}, type=BooleanType)
RefOntoUML_Classifier_m_hasKindOffspring: Method = Method(name="hasKindOffspring", parameters={}, type=BooleanType)
RefOntoUML_Classifier_m_hasQuantityOffspring: Method = Method(name="hasQuantityOffspring", parameters={}, type=BooleanType)
RefOntoUML_Classifier_m_hasCollectiveOffspring: Method = Method(name="hasCollectiveOffspring", parameters={}, type=BooleanType)
RefOntoUML_Classifier_m_hasFunctionalComplexInstances: Method = Method(name="hasFunctionalComplexInstances", parameters={}, type=BooleanType)
RefOntoUML_Classifier_m_hasQuantityInstances: Method = Method(name="hasQuantityInstances", parameters={}, type=BooleanType)
RefOntoUML_Classifier_m_hasCollectiveInstances: Method = Method(name="hasCollectiveInstances", parameters={}, type=BooleanType)
RefOntoUML_Classifier_m_children: Method = Method(name="children", parameters={}, type=Classifier)
RefOntoUML_Classifier.attributes={RefOntoUML_Classifier_isAbstract}
RefOntoUML_Classifier.methods={RefOntoUML_Classifier_m_getInheritedMembers, RefOntoUML_Classifier_m_maps_to_generalization_set, RefOntoUML_Classifier_m_children, RefOntoUML_Classifier_m_hasQuantityAncestor, RefOntoUML_Classifier_m_allChildren, RefOntoUML_Classifier_m_hasCollectiveAncestor, RefOntoUML_Classifier_m_hasVisibilityOf, RefOntoUML_Classifier_m_hasQuantityOffspring, RefOntoUML_Classifier_m_hasCollectiveOffspring, RefOntoUML_Classifier_m_inherit, RefOntoUML_Classifier_m_partitions, RefOntoUML_Classifier_m_hasKindOffspring, RefOntoUML_Classifier_m_specialize_type, RefOntoUML_Classifier_m_allParents, RefOntoUML_Classifier_m_hasKindAncestor, RefOntoUML_Classifier_m_hasCollectiveInstances, RefOntoUML_Classifier_m_getAllAttributes, RefOntoUML_Classifier_m_inheritableMembers, RefOntoUML_Classifier_m_no_cycles_in_generalization, RefOntoUML_Classifier_m_hasQuantityInstances, RefOntoUML_Classifier_m_maySpecializeType, RefOntoUML_Classifier_m_generalization_hierarchies, RefOntoUML_Classifier_m_conformsTo, RefOntoUML_Classifier_m_hasFunctionalComplexInstances, RefOntoUML_Classifier_m_parents, RefOntoUML_Classifier_m_getGenerals, RefOntoUML_Classifier_m_allFeatures}

# RedefinableElement class attributes and methods

# Type class attributes and methods

# RefOntoUML_Property class attributes and methods
RefOntoUML_Property_isDerived: Property = Property(name="isDerived", type=StringType)
RefOntoUML_Property_isDerivedUnion: Property = Property(name="isDerivedUnion", type=StringType)
RefOntoUML_Property_default: Property = Property(name="default", type=StringType)
RefOntoUML_Property_aggregation: Property = Property(name="aggregation", type=StringType)
RefOntoUML_Property_isComposite: Property = Property(name="isComposite", type=StringType)
RefOntoUML_Property_m_redefined_property_inherited: Method = Method(name="redefined_property_inherited", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
RefOntoUML_Property_m_subsetting_rules: Method = Method(name="subsetting_rules", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
RefOntoUML_Property_m_multiplicity_of_composite: Method = Method(name="multiplicity_of_composite", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
RefOntoUML_Property_m_subsetting_context_conforms: Method = Method(name="subsetting_context_conforms", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
RefOntoUML_Property_m_derived_union_is_read_only: Method = Method(name="derived_union_is_read_only", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
RefOntoUML_Property_m_navigable_readonly: Method = Method(name="navigable_readonly", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
RefOntoUML_Property_m_derived_union_is_derived: Method = Method(name="derived_union_is_derived", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
RefOntoUML_Property_m_getDefault: Method = Method(name="getDefault", parameters={}, type=StringType)
RefOntoUML_Property_m_isSetDefault: Method = Method(name="isSetDefault", parameters={}, type=StringType)
RefOntoUML_Property_m_setDefault: Method = Method(name="setDefault", parameters={Parameter(name='newDefault')})
RefOntoUML_Property_m_subsetted_property_names: Method = Method(name="subsetted_property_names", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
RefOntoUML_Property_m_deployment_target: Method = Method(name="deployment_target", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
RefOntoUML_Property_m_binding_to_attribute: Method = Method(name="binding_to_attribute", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
RefOntoUML_Property_m_setStringDefaultValue: Method = Method(name="setStringDefaultValue", parameters={Parameter(name='value')})
RefOntoUML_Property_m_setUnlimitedNaturalDefaultValue: Method = Method(name="setUnlimitedNaturalDefaultValue", parameters={Parameter(name='value')})
RefOntoUML_Property_m_setIsComposite: Method = Method(name="setIsComposite", parameters={Parameter(name='newIsComposite')})
RefOntoUML_Property_m_setNullDefaultValue: Method = Method(name="setNullDefaultValue", parameters={})
RefOntoUML_Property_m_isAttribute: Method = Method(name="isAttribute", parameters={Parameter(name='p')}, type=StringType)
RefOntoUML_Property_m_setOpposite: Method = Method(name="setOpposite", parameters={Parameter(name='newOpposite')})
RefOntoUML_Property_m_unsetDefault: Method = Method(name="unsetDefault", parameters={})
RefOntoUML_Property_m_setIsNavigable: Method = Method(name="setIsNavigable", parameters={Parameter(name='isNavigable')})
RefOntoUML_Property_m_getOtherEnd: Method = Method(name="getOtherEnd", parameters={}, type=StringType)
RefOntoUML_Property_m_setBooleanDefaultValue: Method = Method(name="setBooleanDefaultValue", parameters={Parameter(name='value')})
RefOntoUML_Property_m_setIntegerDefaultValue: Method = Method(name="setIntegerDefaultValue", parameters={Parameter(name='value')})
RefOntoUML_Property_m_getOpposite: Method = Method(name="getOpposite", parameters={}, type=StringType)
RefOntoUML_Property_m_isComposite: Method = Method(name="isComposite", parameters={}, type=StringType)
RefOntoUML_Property_m_subsettingContext: Method = Method(name="subsettingContext", parameters={}, type=Type)
RefOntoUML_Property_m_isNavigable: Method = Method(name="isNavigable", parameters={}, type=StringType)
RefOntoUML_Property.attributes={RefOntoUML_Property_isComposite, RefOntoUML_Property_isDerived, RefOntoUML_Property_isDerivedUnion, RefOntoUML_Property_aggregation, RefOntoUML_Property_default}
RefOntoUML_Property.methods={RefOntoUML_Property_m_setDefault, RefOntoUML_Property_m_multiplicity_of_composite, RefOntoUML_Property_m_setOpposite, RefOntoUML_Property_m_isSetDefault, RefOntoUML_Property_m_unsetDefault, RefOntoUML_Property_m_setIsNavigable, RefOntoUML_Property_m_setIsComposite, RefOntoUML_Property_m_isComposite, RefOntoUML_Property_m_subsettingContext, RefOntoUML_Property_m_getOpposite, RefOntoUML_Property_m_setNullDefaultValue, RefOntoUML_Property_m_isAttribute, RefOntoUML_Property_m_setBooleanDefaultValue, RefOntoUML_Property_m_derived_union_is_read_only, RefOntoUML_Property_m_setUnlimitedNaturalDefaultValue, RefOntoUML_Property_m_binding_to_attribute, RefOntoUML_Property_m_subsetting_rules, RefOntoUML_Property_m_subsetted_property_names, RefOntoUML_Property_m_setIntegerDefaultValue, RefOntoUML_Property_m_navigable_readonly, RefOntoUML_Property_m_isNavigable, RefOntoUML_Property_m_redefined_property_inherited, RefOntoUML_Property_m_setStringDefaultValue, RefOntoUML_Property_m_subsetting_context_conforms, RefOntoUML_Property_m_getOtherEnd, RefOntoUML_Property_m_deployment_target, RefOntoUML_Property_m_getDefault, RefOntoUML_Property_m_derived_union_is_derived}

# RefOntoUML_Generalization class attributes and methods
RefOntoUML_Generalization_isSubstitutable: Property = Property(name="isSubstitutable", type=StringType)
RefOntoUML_Generalization_m_generalization_same_classifier: Method = Method(name="generalization_same_classifier", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
RefOntoUML_Generalization.attributes={RefOntoUML_Generalization_isSubstitutable}
RefOntoUML_Generalization.methods={RefOntoUML_Generalization_m_generalization_same_classifier}

# RefOntoUML_GeneralizationSet class attributes and methods
RefOntoUML_GeneralizationSet_isCovering: Property = Property(name="isCovering", type=StringType)
RefOntoUML_GeneralizationSet_isDisjoint: Property = Property(name="isDisjoint", type=StringType)
RefOntoUML_GeneralizationSet_m_parent: Method = Method(name="parent", parameters={}, type=Classifier)
RefOntoUML_GeneralizationSet_m_children: Method = Method(name="children", parameters={}, type=Classifier)
RefOntoUML_GeneralizationSet_m_generalization_same_classifier: Method = Method(name="generalization_same_classifier", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
RefOntoUML_GeneralizationSet_m_maps_to_generalization_set: Method = Method(name="maps_to_generalization_set", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
RefOntoUML_GeneralizationSet.attributes={RefOntoUML_GeneralizationSet_isDisjoint, RefOntoUML_GeneralizationSet_isCovering}
RefOntoUML_GeneralizationSet.methods={RefOntoUML_GeneralizationSet_m_generalization_same_classifier, RefOntoUML_GeneralizationSet_m_parent, RefOntoUML_GeneralizationSet_m_children, RefOntoUML_GeneralizationSet_m_maps_to_generalization_set}

# RefOntoUML_Feature class attributes and methods
RefOntoUML_Feature_isStatic: Property = Property(name="isStatic", type=StringType)
RefOntoUML_Feature.attributes={RefOntoUML_Feature_isStatic}

# RefOntoUML_RedefinableElement class attributes and methods
RefOntoUML_RedefinableElement_isLeaf: Property = Property(name="isLeaf", type=StringType)
RefOntoUML_RedefinableElement_m_isRedefinitionContextValid: Method = Method(name="isRedefinitionContextValid", parameters={Parameter(name='redefined')}, type=StringType)
RefOntoUML_RedefinableElement_m_redefinition_context_valid: Method = Method(name="redefinition_context_valid", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
RefOntoUML_RedefinableElement_m_redefinition_consistent: Method = Method(name="redefinition_consistent", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
RefOntoUML_RedefinableElement_m_isConsistentWith: Method = Method(name="isConsistentWith", parameters={Parameter(name='redefinee')}, type=StringType)
RefOntoUML_RedefinableElement.attributes={RefOntoUML_RedefinableElement_isLeaf}
RefOntoUML_RedefinableElement.methods={RefOntoUML_RedefinableElement_m_isRedefinitionContextValid, RefOntoUML_RedefinableElement_m_isConsistentWith, RefOntoUML_RedefinableElement_m_redefinition_context_valid, RefOntoUML_RedefinableElement_m_redefinition_consistent}

# RefOntoUML_OpaqueExpression class attributes and methods
RefOntoUML_OpaqueExpression_body: Property = Property(name="body", type=StringType)
RefOntoUML_OpaqueExpression_language: Property = Property(name="language", type=StringType)
RefOntoUML_OpaqueExpression_m_getResult: Method = Method(name="getResult", parameters={})
RefOntoUML_OpaqueExpression_m_value: Method = Method(name="value", parameters={}, type=StringType)
RefOntoUML_OpaqueExpression_m_isIntegral: Method = Method(name="isIntegral", parameters={}, type=StringType)
RefOntoUML_OpaqueExpression_m_isPositive: Method = Method(name="isPositive", parameters={}, type=StringType)
RefOntoUML_OpaqueExpression_m_language_body_size: Method = Method(name="language_body_size", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
RefOntoUML_OpaqueExpression_m_only_return_result_parameters: Method = Method(name="only_return_result_parameters", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
RefOntoUML_OpaqueExpression_m_one_return_result_parameter: Method = Method(name="one_return_result_parameter", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
RefOntoUML_OpaqueExpression_m_isNonNegative: Method = Method(name="isNonNegative", parameters={}, type=StringType)
RefOntoUML_OpaqueExpression.attributes={RefOntoUML_OpaqueExpression_body, RefOntoUML_OpaqueExpression_language}
RefOntoUML_OpaqueExpression.methods={RefOntoUML_OpaqueExpression_m_getResult, RefOntoUML_OpaqueExpression_m_isPositive, RefOntoUML_OpaqueExpression_m_isNonNegative, RefOntoUML_OpaqueExpression_m_value, RefOntoUML_OpaqueExpression_m_language_body_size, RefOntoUML_OpaqueExpression_m_one_return_result_parameter, RefOntoUML_OpaqueExpression_m_only_return_result_parameters, RefOntoUML_OpaqueExpression_m_isIntegral}

# ValueSpecification class attributes and methods

# RefOntoUML_MultiplicityElement class attributes and methods
RefOntoUML_MultiplicityElement_isOrdered: Property = Property(name="isOrdered", type=StringType)
RefOntoUML_MultiplicityElement_isUnique: Property = Property(name="isUnique", type=StringType)
RefOntoUML_MultiplicityElement_upper: Property = Property(name="upper", type=StringType)
RefOntoUML_MultiplicityElement_lower: Property = Property(name="lower", type=StringType)
RefOntoUML_MultiplicityElement_m_value_specification_no_side_effects: Method = Method(name="value_specification_no_side_effects", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
RefOntoUML_MultiplicityElement_m_lower_ge_0: Method = Method(name="lower_ge_0", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
RefOntoUML_MultiplicityElement_m_upper_ge_lower: Method = Method(name="upper_ge_lower", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
RefOntoUML_MultiplicityElement_m_includesCardinality: Method = Method(name="includesCardinality", parameters={Parameter(name='C')}, type=StringType)
RefOntoUML_MultiplicityElement_m_includesMultiplicity: Method = Method(name="includesMultiplicity", parameters={Parameter(name='M')}, type=StringType)
RefOntoUML_MultiplicityElement_m_lowerBound: Method = Method(name="lowerBound", parameters={}, type=StringType)
RefOntoUML_MultiplicityElement_m_value_specification_constant: Method = Method(name="value_specification_constant", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
RefOntoUML_MultiplicityElement_m_setLower: Method = Method(name="setLower", parameters={Parameter(name='newLower')})
RefOntoUML_MultiplicityElement_m_setUpper: Method = Method(name="setUpper", parameters={Parameter(name='newUpper')})
RefOntoUML_MultiplicityElement_m_getLower: Method = Method(name="getLower", parameters={}, type=StringType)
RefOntoUML_MultiplicityElement_m_getUpper: Method = Method(name="getUpper", parameters={}, type=StringType)
RefOntoUML_MultiplicityElement_m_isMultivalued: Method = Method(name="isMultivalued", parameters={}, type=StringType)
RefOntoUML_MultiplicityElement_m_upperBound: Method = Method(name="upperBound", parameters={}, type=StringType)
RefOntoUML_MultiplicityElement_m_compatibleWith: Method = Method(name="compatibleWith", parameters={Parameter(name='other')}, type=StringType)
RefOntoUML_MultiplicityElement_m_is: Method = Method(name="is", parameters={Parameter(name='lowerbound'), Parameter(name='upperbound')}, type=StringType)
RefOntoUML_MultiplicityElement.attributes={RefOntoUML_MultiplicityElement_isOrdered, RefOntoUML_MultiplicityElement_lower, RefOntoUML_MultiplicityElement_upper, RefOntoUML_MultiplicityElement_isUnique}
RefOntoUML_MultiplicityElement.methods={RefOntoUML_MultiplicityElement_m_value_specification_constant, RefOntoUML_MultiplicityElement_m_getUpper, RefOntoUML_MultiplicityElement_m_isMultivalued, RefOntoUML_MultiplicityElement_m_value_specification_no_side_effects, RefOntoUML_MultiplicityElement_m_getLower, RefOntoUML_MultiplicityElement_m_compatibleWith, RefOntoUML_MultiplicityElement_m_setLower, RefOntoUML_MultiplicityElement_m_upper_ge_lower, RefOntoUML_MultiplicityElement_m_is, RefOntoUML_MultiplicityElement_m_setUpper, RefOntoUML_MultiplicityElement_m_includesCardinality, RefOntoUML_MultiplicityElement_m_includesMultiplicity, RefOntoUML_MultiplicityElement_m_upperBound, RefOntoUML_MultiplicityElement_m_lowerBound, RefOntoUML_MultiplicityElement_m_lower_ge_0}

# StructuralFeature class attributes and methods

# RefOntoUML_Class class attributes and methods
RefOntoUML_Class_isActive: Property = Property(name="isActive", type=StringType)
RefOntoUML_Class_m_createOwnedOperation: Method = Method(name="createOwnedOperation", parameters={Parameter(name='returnType'), Parameter(name='parameterTypes'), Parameter(name='name'), Parameter(name='parameterNames')})
RefOntoUML_Class_m_passive_class: Method = Method(name="passive_class", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
RefOntoUML_Class_m_isMetaclass: Method = Method(name="isMetaclass", parameters={}, type=StringType)
RefOntoUML_Class.attributes={RefOntoUML_Class_isActive}
RefOntoUML_Class.methods={RefOntoUML_Class_m_isMetaclass, RefOntoUML_Class_m_passive_class, RefOntoUML_Class_m_createOwnedOperation}

# RefOntoUML_DataType class attributes and methods
RefOntoUML_DataType_m_createOwnedOperation: Method = Method(name="createOwnedOperation", parameters={Parameter(name='parameterTypes'), Parameter(name='returnType'), Parameter(name='name'), Parameter(name='parameterNames')})
RefOntoUML_DataType_m_createOwnedAttribute: Method = Method(name="createOwnedAttribute", parameters={Parameter(name='type'), Parameter(name='lower'), Parameter(name='upper'), Parameter(name='name')}, type=StringType)
RefOntoUML_DataType.methods={RefOntoUML_DataType_m_createOwnedAttribute, RefOntoUML_DataType_m_createOwnedOperation}

# RefOntoUML_Model class attributes and methods
RefOntoUML_Model_viewpoint: Property = Property(name="viewpoint", type=StringType)
RefOntoUML_Model_m_isMetamodel: Method = Method(name="isMetamodel", parameters={}, type=StringType)
RefOntoUML_Model.attributes={RefOntoUML_Model_viewpoint}
RefOntoUML_Model.methods={RefOntoUML_Model_m_isMetamodel}

# Package class attributes and methods

# RefOntoUML_StructuralFeature class attributes and methods
RefOntoUML_StructuralFeature_isReadOnly: Property = Property(name="isReadOnly", type=StringType)
RefOntoUML_StructuralFeature.attributes={RefOntoUML_StructuralFeature_isReadOnly}

# Feature class attributes and methods

# MultiplicityElement class attributes and methods

# Expression class attributes and methods

# RefOntoUML_Expression class attributes and methods
RefOntoUML_Expression_symbol: Property = Property(name="symbol", type=StringType)
RefOntoUML_Expression.attributes={RefOntoUML_Expression_symbol}

# RefOntoUML_InstanceSpecification class attributes and methods
RefOntoUML_InstanceSpecification_m_structural_feature: Method = Method(name="structural_feature", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
RefOntoUML_InstanceSpecification_m_defining_feature: Method = Method(name="defining_feature", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
RefOntoUML_InstanceSpecification_m_deployment_target: Method = Method(name="deployment_target", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
RefOntoUML_InstanceSpecification_m_deployment_artifact: Method = Method(name="deployment_artifact", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
RefOntoUML_InstanceSpecification.methods={RefOntoUML_InstanceSpecification_m_deployment_artifact, RefOntoUML_InstanceSpecification_m_defining_feature, RefOntoUML_InstanceSpecification_m_structural_feature, RefOntoUML_InstanceSpecification_m_deployment_target}

# RefOntoUML_Slot class attributes and methods

# RefOntoUML_EnumerationLiteral class attributes and methods

# InstanceSpecification class attributes and methods

# RefOntoUML_LiteralSpecification class attributes and methods

# RefOntoUML_Enumeration class attributes and methods

# DataType class attributes and methods

# RefOntoUML_ReferenceStructure class attributes and methods

# RefOntoUML_ReferenceRegion class attributes and methods

# RefOntoUML_NominalStructure class attributes and methods

# ReferenceStructure class attributes and methods

# RefOntoUML_MeasurementEnumeration class attributes and methods

# Enumeration class attributes and methods

# RefOntoUML_MeasurementStructure class attributes and methods

# RefOntoUML_MeasurementLiteral class attributes and methods

# EnumerationLiteral class attributes and methods

# RefOntoUML_MeasurementRegion class attributes and methods

# RefOntoUML_PrimitiveType class attributes and methods

# RefOntoUML_MeasurementDomain class attributes and methods
RefOntoUML_MeasurementDomain_m_isScientific: Method = Method(name="isScientific", parameters={}, type=StringType)
RefOntoUML_MeasurementDomain.methods={RefOntoUML_MeasurementDomain_m_isScientific}

# RefOntoUML_BasicMeasurementRegion class attributes and methods

# RefOntoUML_StringNominalStructure class attributes and methods

# NominalStructure class attributes and methods

# RefOntoUML_MeasurementDimension class attributes and methods
RefOntoUML_MeasurementDimension_unitOfMeasure: Property = Property(name="unitOfMeasure", type=StringType)
RefOntoUML_MeasurementDimension_m_isNonBoundary: Method = Method(name="isNonBoundary", parameters={}, type=StringType)
RefOntoUML_MeasurementDimension_m_isOneBoundary: Method = Method(name="isOneBoundary", parameters={}, type=StringType)
RefOntoUML_MeasurementDimension_m_isCircular: Method = Method(name="isCircular", parameters={}, type=StringType)
RefOntoUML_MeasurementDimension.attributes={RefOntoUML_MeasurementDimension_unitOfMeasure}
RefOntoUML_MeasurementDimension.methods={RefOntoUML_MeasurementDimension_m_isNonBoundary, RefOntoUML_MeasurementDimension_m_isCircular, RefOntoUML_MeasurementDimension_m_isOneBoundary}

# MeasurementStructure class attributes and methods

# RefOntoUML_DecimalIntervalDimension class attributes and methods

# RefOntoUML_OrdinalDimension class attributes and methods

# MeasurementDimension class attributes and methods

# RefOntoUML_IntegerOrdinalDimension class attributes and methods

# OrdinalDimension class attributes and methods

# RefOntoUML_DecimalOrdinalDimension class attributes and methods

# RefOntoUML_IntervalDimension class attributes and methods

# RefOntoUML_IntegerIntervalDimension class attributes and methods

# IntervalDimension class attributes and methods

# RefOntoUML_DecimalRationalDimension class attributes and methods

# RefOntoUML_RationalDimension class attributes and methods

# RefOntoUML_IntegerRationalDimension class attributes and methods

# RationalDimension class attributes and methods

# ReferenceRegion class attributes and methods

# MeasurementRegion class attributes and methods

# RefOntoUML_DecimalMeasurementRegion class attributes and methods

# BasicMeasurementRegion class attributes and methods

# LiteralDecimal class attributes and methods

# RefOntoUML_IntegerMeasurementRegion class attributes and methods

# LiteralInteger class attributes and methods

# RefOntoUML_ComposedMeasurementRegion class attributes and methods

# RefOntoUML_NominalRegion class attributes and methods

# RefOntoUML_StringNominalRegion class attributes and methods

# NominalRegion class attributes and methods

# LiteralString class attributes and methods

# RefOntoUML_LiteralInteger class attributes and methods
RefOntoUML_LiteralInteger_value: Property = Property(name="value", type=StringType)
RefOntoUML_LiteralInteger.attributes={RefOntoUML_LiteralInteger_value}

# LiteralSpecification class attributes and methods

# RefOntoUML_LiteralDecimal class attributes and methods
RefOntoUML_LiteralDecimal_value: Property = Property(name="value", type=StringType)
RefOntoUML_LiteralDecimal_m_decimalValue: Method = Method(name="decimalValue", parameters={}, type=StringType)
RefOntoUML_LiteralDecimal.attributes={RefOntoUML_LiteralDecimal_value}
RefOntoUML_LiteralDecimal.methods={RefOntoUML_LiteralDecimal_m_decimalValue}

# RefOntoUML_LiteralString class attributes and methods
RefOntoUML_LiteralString_value: Property = Property(name="value", type=StringType)
RefOntoUML_LiteralString.attributes={RefOntoUML_LiteralString_value}

# RefOntoUML_InstanceValue class attributes and methods

# RefOntoUML_LiteralBoolean class attributes and methods
RefOntoUML_LiteralBoolean_value: Property = Property(name="value", type=StringType)
RefOntoUML_LiteralBoolean.attributes={RefOntoUML_LiteralBoolean_value}

# RefOntoUML_LiteralNull class attributes and methods

# RefOntoUML_MixinClass class attributes and methods

# RefOntoUML_LiteralUnlimitedNatural class attributes and methods
RefOntoUML_LiteralUnlimitedNatural_value: Property = Property(name="value", type=StringType)
RefOntoUML_LiteralUnlimitedNatural.attributes={RefOntoUML_LiteralUnlimitedNatural_value}

# RefOntoUML_ObjectClass class attributes and methods

# Class class attributes and methods

# RefOntoUML_MomentClass class attributes and methods

# RefOntoUML_SortalClass class attributes and methods

# ObjectClass class attributes and methods

# RefOntoUML_Phase class attributes and methods

# AntiRigidSortalClass class attributes and methods

# RefOntoUML_RigidSortalClass class attributes and methods

# SortalClass class attributes and methods

# RefOntoUML_AntiRigidSortalClass class attributes and methods
RefOntoUML_AntiRigidSortalClass_m_rigidParent: Method = Method(name="rigidParent", parameters={}, type=StringType)
RefOntoUML_AntiRigidSortalClass.methods={RefOntoUML_AntiRigidSortalClass_m_rigidParent}

# RefOntoUML_SubstanceSortal class attributes and methods

# RigidSortalClass class attributes and methods

# RefOntoUML_SubKind class attributes and methods

# RefOntoUML_Kind class attributes and methods

# SubstanceSortal class attributes and methods

# RefOntoUML_Quantity class attributes and methods

# RefOntoUML_Collective class attributes and methods
RefOntoUML_Collective_isExtensional: Property = Property(name="isExtensional", type=BooleanType)
RefOntoUML_Collective.attributes={RefOntoUML_Collective_isExtensional}

# RefOntoUML_Role class attributes and methods
RefOntoUML_Role_m_mediation: Method = Method(name="mediation", parameters={}, type=StringType)
RefOntoUML_Role_m_relator: Method = Method(name="relator", parameters={}, type=StringType)
RefOntoUML_Role.methods={RefOntoUML_Role_m_mediation, RefOntoUML_Role_m_relator}

# RefOntoUML_RigidMixinClass class attributes and methods

# MixinClass class attributes and methods

# RefOntoUML_NonRigidMixinClass class attributes and methods

# RefOntoUML_Category class attributes and methods

# RigidMixinClass class attributes and methods

# RefOntoUML_AntiRigidMixinClass class attributes and methods

# NonRigidMixinClass class attributes and methods

# RefOntoUML_SemiRigidMixinClass class attributes and methods

# RefOntoUML_RoleMixin class attributes and methods
RefOntoUML_RoleMixin_m_relator: Method = Method(name="relator", parameters={}, type=StringType)
RefOntoUML_RoleMixin_m_roles: Method = Method(name="roles", parameters={}, type=StringType)
RefOntoUML_RoleMixin_m_rigidSortals: Method = Method(name="rigidSortals", parameters={}, type=RigidSortalClass)
RefOntoUML_RoleMixin_m_mediation: Method = Method(name="mediation", parameters={}, type=StringType)
RefOntoUML_RoleMixin.methods={RefOntoUML_RoleMixin_m_relator, RefOntoUML_RoleMixin_m_mediation, RefOntoUML_RoleMixin_m_roles, RefOntoUML_RoleMixin_m_rigidSortals}

# AntiRigidMixinClass class attributes and methods

# RefOntoUML_NominalQuality class attributes and methods

# RefOntoUML_NonPerceivableQuality class attributes and methods

# MeasurableQuality class attributes and methods

# RefOntoUML_PerceivableQuality class attributes and methods

# RefOntoUML_Mixin class attributes and methods

# SemiRigidMixinClass class attributes and methods

# RefOntoUML_IntrinsicMomentClass class attributes and methods
RefOntoUML_IntrinsicMomentClass_m_characterization: Method = Method(name="characterization", parameters={}, type=StringType)
RefOntoUML_IntrinsicMomentClass_m_characterized: Method = Method(name="characterized", parameters={}, type=Classifier)
RefOntoUML_IntrinsicMomentClass.methods={RefOntoUML_IntrinsicMomentClass_m_characterized, RefOntoUML_IntrinsicMomentClass_m_characterization}

# MomentClass class attributes and methods

# RefOntoUML_Mode class attributes and methods

# IntrinsicMomentClass class attributes and methods

# RefOntoUML_Quality class attributes and methods

# RefOntoUML_MeasurableQuality class attributes and methods

# Quality class attributes and methods

# RefOntoUML_Relator class attributes and methods
RefOntoUML_Relator_m_mediations: Method = Method(name="mediations", parameters={}, type=StringType)
RefOntoUML_Relator_m_mediated: Method = Method(name="mediated", parameters={}, type=Classifier)
RefOntoUML_Relator.methods={RefOntoUML_Relator_m_mediations, RefOntoUML_Relator_m_mediated}

# RefOntoUML_DirectedBinaryAssociation class attributes and methods
RefOntoUML_DirectedBinaryAssociation_m_sourceEnd: Method = Method(name="sourceEnd", parameters={}, type=StringType)
RefOntoUML_DirectedBinaryAssociation_m_targetEnd: Method = Method(name="targetEnd", parameters={}, type=StringType)
RefOntoUML_DirectedBinaryAssociation.methods={RefOntoUML_DirectedBinaryAssociation_m_sourceEnd, RefOntoUML_DirectedBinaryAssociation_m_targetEnd}

# Association class attributes and methods

# RefOntoUML_Meronymic class attributes and methods
RefOntoUML_Meronymic_isShareable: Property = Property(name="isShareable", type=BooleanType)
RefOntoUML_Meronymic_isEssential: Property = Property(name="isEssential", type=BooleanType)
RefOntoUML_Meronymic_isInseparable: Property = Property(name="isInseparable", type=BooleanType)
RefOntoUML_Meronymic_isImmutablePart: Property = Property(name="isImmutablePart", type=BooleanType)
RefOntoUML_Meronymic_isImmutableWhole: Property = Property(name="isImmutableWhole", type=BooleanType)
RefOntoUML_Meronymic_m_wholeEnd: Method = Method(name="wholeEnd", parameters={}, type=StringType)
RefOntoUML_Meronymic_m_partEnd: Method = Method(name="partEnd", parameters={}, type=StringType)
RefOntoUML_Meronymic_m_whole: Method = Method(name="whole", parameters={}, type=Classifier)
RefOntoUML_Meronymic_m_part: Method = Method(name="part", parameters={}, type=Classifier)
RefOntoUML_Meronymic.attributes={RefOntoUML_Meronymic_isImmutableWhole, RefOntoUML_Meronymic_isInseparable, RefOntoUML_Meronymic_isImmutablePart, RefOntoUML_Meronymic_isEssential, RefOntoUML_Meronymic_isShareable}
RefOntoUML_Meronymic.methods={RefOntoUML_Meronymic_m_part, RefOntoUML_Meronymic_m_wholeEnd, RefOntoUML_Meronymic_m_partEnd, RefOntoUML_Meronymic_m_whole}

# DirectedBinaryAssociation class attributes and methods

# RefOntoUML_componentOf class attributes and methods

# RefOntoUML_subQuantityOf class attributes and methods

# Meronymic class attributes and methods

# RefOntoUML_subCollectionOf class attributes and methods

# RefOntoUML_memberOf class attributes and methods

# RefOntoUML_DependencyRelationship class attributes and methods

# RefOntoUML_Characterization class attributes and methods
RefOntoUML_Characterization_m_characterizingEnd: Method = Method(name="characterizingEnd", parameters={}, type=StringType)
RefOntoUML_Characterization_m_characterizedEnd: Method = Method(name="characterizedEnd", parameters={}, type=StringType)
RefOntoUML_Characterization_m_characterizing: Method = Method(name="characterizing", parameters={}, type=Classifier)
RefOntoUML_Characterization_m_characterized: Method = Method(name="characterized", parameters={}, type=Classifier)
RefOntoUML_Characterization.methods={RefOntoUML_Characterization_m_characterized, RefOntoUML_Characterization_m_characterizing, RefOntoUML_Characterization_m_characterizingEnd, RefOntoUML_Characterization_m_characterizedEnd}

# DependencyRelationship class attributes and methods

# RefOntoUML_Mediation class attributes and methods
RefOntoUML_Mediation_m_relatorEnd: Method = Method(name="relatorEnd", parameters={}, type=StringType)
RefOntoUML_Mediation_m_mediatedEnd: Method = Method(name="mediatedEnd", parameters={}, type=StringType)
RefOntoUML_Mediation_m_relator: Method = Method(name="relator", parameters={}, type=Classifier)
RefOntoUML_Mediation_m_mediated: Method = Method(name="mediated", parameters={}, type=Classifier)
RefOntoUML_Mediation.methods={RefOntoUML_Mediation_m_relator, RefOntoUML_Mediation_m_mediated, RefOntoUML_Mediation_m_mediatedEnd, RefOntoUML_Mediation_m_relatorEnd}

# RefOntoUML_FormalAssociation class attributes and methods

# RefOntoUML_Derivation class attributes and methods
RefOntoUML_Derivation_m_materialEnd: Method = Method(name="materialEnd", parameters={}, type=StringType)
RefOntoUML_Derivation_m_relatorEnd: Method = Method(name="relatorEnd", parameters={}, type=StringType)
RefOntoUML_Derivation_m_relator: Method = Method(name="relator", parameters={}, type=Classifier)
RefOntoUML_Derivation_m_material: Method = Method(name="material", parameters={}, type=Classifier)
RefOntoUML_Derivation.methods={RefOntoUML_Derivation_m_relator, RefOntoUML_Derivation_m_relatorEnd, RefOntoUML_Derivation_m_material, RefOntoUML_Derivation_m_materialEnd}

# RefOntoUML_Structuration class attributes and methods
RefOntoUML_Structuration_m_structuredEnd: Method = Method(name="structuredEnd", parameters={}, type=StringType)
RefOntoUML_Structuration_m_structuring: Method = Method(name="structuring", parameters={}, type=Classifier)
RefOntoUML_Structuration_m_structured: Method = Method(name="structured", parameters={}, type=Classifier)
RefOntoUML_Structuration_m_structuringEnd: Method = Method(name="structuringEnd", parameters={}, type=StringType)
RefOntoUML_Structuration.methods={RefOntoUML_Structuration_m_structuringEnd, RefOntoUML_Structuration_m_structuring, RefOntoUML_Structuration_m_structured, RefOntoUML_Structuration_m_structuredEnd}

# RefOntoUML_MaterialAssociation class attributes and methods

# Relationships
annotatedElement0: BinaryAssociation = BinaryAssociation(
    name="annotatedElement0",
    ends={
        Property(name="RefOntoUML_Element", type=RefOntoUML_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="RefOntoUML_Comment", type=RefOntoUML_Element, multiplicity=Multiplicity(0, 9999))
    }
)
ownedElement2: BinaryAssociation = BinaryAssociation(
    name="ownedElement2",
    ends={
        Property(name="Element", type=RefOntoUML_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=RefOntoUML_Element, multiplicity=Multiplicity(0, 9999))
    }
)
owner4: BinaryAssociation = BinaryAssociation(
    name="owner4",
    ends={
        Property(name="Element5", type=RefOntoUML_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedElement", type=RefOntoUML_Element, multiplicity=Multiplicity(0, 1))
    }
)
ownedComment6: BinaryAssociation = BinaryAssociation(
    name="ownedComment6",
    ends={
        Property(name="RefOntoUML_Comment8", type=RefOntoUML_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="RefOntoUML_Element7", type=RefOntoUML_Comment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packagedElement11: BinaryAssociation = BinaryAssociation(
    name="packagedElement11",
    ends={
        Property(name="RefOntoUML_PackageableElement", type=RefOntoUML_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="RefOntoUML_Package", type=RefOntoUML_PackageableElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nestedPackage13: BinaryAssociation = BinaryAssociation(
    name="nestedPackage13",
    ends={
        Property(name="Package", type=RefOntoUML_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="nestingPackage", type=RefOntoUML_Package, multiplicity=Multiplicity(0, 9999))
    }
)
ownedType9: BinaryAssociation = BinaryAssociation(
    name="ownedType9",
    ends={
        Property(name="Type", type=RefOntoUML_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="package", type=RefOntoUML_Type, multiplicity=Multiplicity(0, 9999))
    }
)
packageMerge10: BinaryAssociation = BinaryAssociation(
    name="packageMerge10",
    ends={
        Property(name="PackageMerge", type=RefOntoUML_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="receivingPackage", type=RefOntoUML_PackageMerge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nestingPackage15: BinaryAssociation = BinaryAssociation(
    name="nestingPackage15",
    ends={
        Property(name="Package16", type=RefOntoUML_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="nestedPackage", type=RefOntoUML_Package, multiplicity=Multiplicity(0, 1))
    }
)
nameExpression19: BinaryAssociation = BinaryAssociation(
    name="nameExpression19",
    ends={
        Property(name="RefOntoUML_StringExpression", type=RefOntoUML_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="RefOntoUML_NamedElement", type=RefOntoUML_StringExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
clientDependency17: BinaryAssociation = BinaryAssociation(
    name="clientDependency17",
    ends={
        Property(name="Dependency", type=RefOntoUML_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="client", type=RefOntoUML_Dependency, multiplicity=Multiplicity(0, 9999))
    }
)
namespace18: BinaryAssociation = BinaryAssociation(
    name="namespace18",
    ends={
        Property(name="Namespace", type=RefOntoUML_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedMember", type=RefOntoUML_Namespace, multiplicity=Multiplicity(0, 1))
    }
)
supplier20: BinaryAssociation = BinaryAssociation(
    name="supplier20",
    ends={
        Property(name="RefOntoUML_NamedElement21", type=RefOntoUML_Dependency, multiplicity=Multiplicity(1, 1)),
        Property(name="RefOntoUML_Dependency", type=RefOntoUML_NamedElement, multiplicity=Multiplicity(1, 9999))
    }
)
client22: BinaryAssociation = BinaryAssociation(
    name="client22",
    ends={
        Property(name="NamedElement", type=RefOntoUML_Dependency, multiplicity=Multiplicity(1, 1)),
        Property(name="clientDependency", type=RefOntoUML_NamedElement, multiplicity=Multiplicity(1, 9999))
    }
)
source23: BinaryAssociation = BinaryAssociation(
    name="source23",
    ends={
        Property(name="RefOntoUML_Element24", type=RefOntoUML_DirectedRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="RefOntoUML_DirectedRelationship", type=RefOntoUML_Element, multiplicity=Multiplicity(1, 9999))
    }
)
target25: BinaryAssociation = BinaryAssociation(
    name="target25",
    ends={
        Property(name="RefOntoUML_Element27", type=RefOntoUML_DirectedRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="RefOntoUML_DirectedRelationship26", type=RefOntoUML_Element, multiplicity=Multiplicity(1, 9999))
    }
)
relatedElement28: BinaryAssociation = BinaryAssociation(
    name="relatedElement28",
    ends={
        Property(name="RefOntoUML_Element29", type=RefOntoUML_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="RefOntoUML_Relationship", type=RefOntoUML_Element, multiplicity=Multiplicity(1, 9999))
    }
)
ownedRule33: BinaryAssociation = BinaryAssociation(
    name="ownedRule33",
    ends={
        Property(name="Constraintx", type=RefOntoUML_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="context", type=RefOntoUML_Constraintx, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elementImport30: BinaryAssociation = BinaryAssociation(
    name="elementImport30",
    ends={
        Property(name="ElementImport", type=RefOntoUML_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="importingNamespace", type=RefOntoUML_ElementImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packageImport31: BinaryAssociation = BinaryAssociation(
    name="packageImport31",
    ends={
        Property(name="PackageImport", type=RefOntoUML_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="importingNamespace32", type=RefOntoUML_PackageImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
member34: BinaryAssociation = BinaryAssociation(
    name="member34",
    ends={
        Property(name="RefOntoUML_NamedElement35", type=RefOntoUML_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="RefOntoUML_Namespace", type=RefOntoUML_NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
importedMember36: BinaryAssociation = BinaryAssociation(
    name="importedMember36",
    ends={
        Property(name="RefOntoUML_PackageableElement38", type=RefOntoUML_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="RefOntoUML_Namespace37", type=RefOntoUML_PackageableElement, multiplicity=Multiplicity(0, 9999))
    }
)
ownedMember39: BinaryAssociation = BinaryAssociation(
    name="ownedMember39",
    ends={
        Property(name="NamedElement40", type=RefOntoUML_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="namespace", type=RefOntoUML_NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
importedPackage45: BinaryAssociation = BinaryAssociation(
    name="importedPackage45",
    ends={
        Property(name="RefOntoUML_Package46", type=RefOntoUML_PackageImport, multiplicity=Multiplicity(1, 1)),
        Property(name="RefOntoUML_PackageImport", type=RefOntoUML_Package, multiplicity=Multiplicity(1, 1))
    }
)
importedElement41: BinaryAssociation = BinaryAssociation(
    name="importedElement41",
    ends={
        Property(name="RefOntoUML_PackageableElement42", type=RefOntoUML_ElementImport, multiplicity=Multiplicity(1, 1)),
        Property(name="RefOntoUML_ElementImport", type=RefOntoUML_PackageableElement, multiplicity=Multiplicity(1, 1))
    }
)
importingNamespace43: BinaryAssociation = BinaryAssociation(
    name="importingNamespace43",
    ends={
        Property(name="Namespace44", type=RefOntoUML_ElementImport, multiplicity=Multiplicity(1, 1)),
        Property(name="elementImport", type=RefOntoUML_Namespace, multiplicity=Multiplicity(1, 1))
    }
)
importingNamespace47: BinaryAssociation = BinaryAssociation(
    name="importingNamespace47",
    ends={
        Property(name="Namespace48", type=RefOntoUML_PackageImport, multiplicity=Multiplicity(1, 1)),
        Property(name="packageImport", type=RefOntoUML_Namespace, multiplicity=Multiplicity(1, 1))
    }
)
constrainedElement49: BinaryAssociation = BinaryAssociation(
    name="constrainedElement49",
    ends={
        Property(name="RefOntoUML_Element50", type=RefOntoUML_Constraintx, multiplicity=Multiplicity(1, 1)),
        Property(name="RefOntoUML_Constraintx", type=RefOntoUML_Element, multiplicity=Multiplicity(0, 9999))
    }
)
specification51: BinaryAssociation = BinaryAssociation(
    name="specification51",
    ends={
        Property(name="RefOntoUML_ValueSpecification", type=RefOntoUML_Constraintx, multiplicity=Multiplicity(1, 1)),
        Property(name="RefOntoUML_Constraintx52", type=RefOntoUML_ValueSpecification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
context53: BinaryAssociation = BinaryAssociation(
    name="context53",
    ends={
        Property(name="Namespace54", type=RefOntoUML_Constraintx, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedRule", type=RefOntoUML_Namespace, multiplicity=Multiplicity(0, 1))
    }
)
type55: BinaryAssociation = BinaryAssociation(
    name="type55",
    ends={
        Property(name="RefOntoUML_Type", type=RefOntoUML_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="RefOntoUML_TypedElement", type=RefOntoUML_Type, multiplicity=Multiplicity(0, 1))
    }
)
package56: BinaryAssociation = BinaryAssociation(
    name="package56",
    ends={
        Property(name="Package57", type=RefOntoUML_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedType", type=RefOntoUML_Package, multiplicity=Multiplicity(0, 1))
    }
)
ownedEnd58: BinaryAssociation = BinaryAssociation(
    name="ownedEnd58",
    ends={
        Property(name="Property", type=RefOntoUML_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="owningAssociation", type=RefOntoUML_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
memberEnd59: BinaryAssociation = BinaryAssociation(
    name="memberEnd59",
    ends={
        Property(name="Property60", type=RefOntoUML_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="association", type=RefOntoUML_Property, multiplicity=Multiplicity(2, 9999))
    }
)
endType61: BinaryAssociation = BinaryAssociation(
    name="endType61",
    ends={
        Property(name="RefOntoUML_Type62", type=RefOntoUML_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="RefOntoUML_Association", type=RefOntoUML_Type, multiplicity=Multiplicity(1, 9999))
    }
)
navigableOwnedEnd63: BinaryAssociation = BinaryAssociation(
    name="navigableOwnedEnd63",
    ends={
        Property(name="RefOntoUML_Property", type=RefOntoUML_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="RefOntoUML_Association64", type=RefOntoUML_Property, multiplicity=Multiplicity(0, 9999))
    }
)
general74: BinaryAssociation = BinaryAssociation(
    name="general74",
    ends={
        Property(name="RefOntoUML_Classifier75", type=RefOntoUML_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="RefOntoUML_Classifier73", type=RefOntoUML_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
generalization65: BinaryAssociation = BinaryAssociation(
    name="generalization65",
    ends={
        Property(name="Generalization", type=RefOntoUML_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="specific", type=RefOntoUML_Generalization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
powertypeExtent66: BinaryAssociation = BinaryAssociation(
    name="powertypeExtent66",
    ends={
        Property(name="GeneralizationSet", type=RefOntoUML_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="powertype", type=RefOntoUML_GeneralizationSet, multiplicity=Multiplicity(0, 9999))
    }
)
feature67: BinaryAssociation = BinaryAssociation(
    name="feature67",
    ends={
        Property(name="Feature", type=RefOntoUML_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="featuringClassifier", type=RefOntoUML_Feature, multiplicity=Multiplicity(0, 9999))
    }
)
inheritedMember68: BinaryAssociation = BinaryAssociation(
    name="inheritedMember68",
    ends={
        Property(name="RefOntoUML_NamedElement69", type=RefOntoUML_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="RefOntoUML_Classifier", type=RefOntoUML_NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
redefinedClassifier71: BinaryAssociation = BinaryAssociation(
    name="redefinedClassifier71",
    ends={
        Property(name="RefOntoUML_Classifier72", type=RefOntoUML_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="RefOntoUML_Classifier70", type=RefOntoUML_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
attribute76: BinaryAssociation = BinaryAssociation(
    name="attribute76",
    ends={
        Property(name="RefOntoUML_Property78", type=RefOntoUML_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="RefOntoUML_Classifier77", type=RefOntoUML_Property, multiplicity=Multiplicity(0, 9999))
    }
)
general84: BinaryAssociation = BinaryAssociation(
    name="general84",
    ends={
        Property(name="RefOntoUML_Classifier85", type=RefOntoUML_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="RefOntoUML_Generalization", type=RefOntoUML_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
redefinedElement80: BinaryAssociation = BinaryAssociation(
    name="redefinedElement80",
    ends={
        Property(name="RefOntoUML_RedefinableElement", type=RefOntoUML_RedefinableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="RefOntoUML_RedefinableElement79", type=RefOntoUML_RedefinableElement, multiplicity=Multiplicity(0, 9999))
    }
)
redefinitionContext81: BinaryAssociation = BinaryAssociation(
    name="redefinitionContext81",
    ends={
        Property(name="RefOntoUML_Classifier83", type=RefOntoUML_RedefinableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="RefOntoUML_RedefinableElement82", type=RefOntoUML_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
generalizationSet86: BinaryAssociation = BinaryAssociation(
    name="generalizationSet86",
    ends={
        Property(name="GeneralizationSet87", type=RefOntoUML_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="generalization", type=RefOntoUML_GeneralizationSet, multiplicity=Multiplicity(0, 9999))
    }
)
specific88: BinaryAssociation = BinaryAssociation(
    name="specific88",
    ends={
        Property(name="Classifier", type=RefOntoUML_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="generalization89", type=RefOntoUML_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
featuringClassifier94: BinaryAssociation = BinaryAssociation(
    name="featuringClassifier94",
    ends={
        Property(name="Classifier95", type=RefOntoUML_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="feature", type=RefOntoUML_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
powertype90: BinaryAssociation = BinaryAssociation(
    name="powertype90",
    ends={
        Property(name="Classifier91", type=RefOntoUML_GeneralizationSet, multiplicity=Multiplicity(1, 1)),
        Property(name="powertypeExtent", type=RefOntoUML_Classifier, multiplicity=Multiplicity(0, 1))
    }
)
generalization92: BinaryAssociation = BinaryAssociation(
    name="generalization92",
    ends={
        Property(name="Generalization93", type=RefOntoUML_GeneralizationSet, multiplicity=Multiplicity(1, 1)),
        Property(name="generalizationSet", type=RefOntoUML_Generalization, multiplicity=Multiplicity(0, 9999))
    }
)
upperValue96: BinaryAssociation = BinaryAssociation(
    name="upperValue96",
    ends={
        Property(name="RefOntoUML_ValueSpecification97", type=RefOntoUML_MultiplicityElement, multiplicity=Multiplicity(1, 1)),
        Property(name="RefOntoUML_MultiplicityElement", type=RefOntoUML_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lowerValue98: BinaryAssociation = BinaryAssociation(
    name="lowerValue98",
    ends={
        Property(name="RefOntoUML_ValueSpecification100", type=RefOntoUML_MultiplicityElement, multiplicity=Multiplicity(1, 1)),
        Property(name="RefOntoUML_MultiplicityElement99", type=RefOntoUML_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
class101: BinaryAssociation = BinaryAssociation(
    name="class101",
    ends={
        Property(name="Class", type=RefOntoUML_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedAttribute", type=RefOntoUML_Class, multiplicity=Multiplicity(0, 1))
    }
)
datatype102: BinaryAssociation = BinaryAssociation(
    name="datatype102",
    ends={
        Property(name="DataType", type=RefOntoUML_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedAttribute103", type=RefOntoUML_DataType, multiplicity=Multiplicity(0, 1))
    }
)
opposite112: BinaryAssociation = BinaryAssociation(
    name="opposite112",
    ends={
        Property(name="RefOntoUML_Property113", type=RefOntoUML_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="RefOntoUML_Property111", type=RefOntoUML_Property, multiplicity=Multiplicity(0, 1))
    }
)
redefinedProperty105: BinaryAssociation = BinaryAssociation(
    name="redefinedProperty105",
    ends={
        Property(name="RefOntoUML_Property106", type=RefOntoUML_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="RefOntoUML_Property104", type=RefOntoUML_Property, multiplicity=Multiplicity(0, 9999))
    }
)
owningAssociation107: BinaryAssociation = BinaryAssociation(
    name="owningAssociation107",
    ends={
        Property(name="Association", type=RefOntoUML_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedEnd", type=RefOntoUML_Association, multiplicity=Multiplicity(0, 1))
    }
)
defaultValue108: BinaryAssociation = BinaryAssociation(
    name="defaultValue108",
    ends={
        Property(name="RefOntoUML_ValueSpecification110", type=RefOntoUML_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="RefOntoUML_Property109", type=RefOntoUML_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subsettedProperty115: BinaryAssociation = BinaryAssociation(
    name="subsettedProperty115",
    ends={
        Property(name="RefOntoUML_Property116", type=RefOntoUML_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="RefOntoUML_Property114", type=RefOntoUML_Property, multiplicity=Multiplicity(0, 9999))
    }
)
association117: BinaryAssociation = BinaryAssociation(
    name="association117",
    ends={
        Property(name="Association118", type=RefOntoUML_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="memberEnd", type=RefOntoUML_Association, multiplicity=Multiplicity(0, 1))
    }
)
ownedAttribute124: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute124",
    ends={
        Property(name="class", type=RefOntoUML_Property, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="Property125", type=RefOntoUML_Class, multiplicity=Multiplicity(1, 1))
    }
)
nestedClassifier119: BinaryAssociation = BinaryAssociation(
    name="nestedClassifier119",
    ends={
        Property(name="RefOntoUML_Classifier120", type=RefOntoUML_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="RefOntoUML_Class", type=RefOntoUML_Classifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superClass122: BinaryAssociation = BinaryAssociation(
    name="superClass122",
    ends={
        Property(name="RefOntoUML_Class123", type=RefOntoUML_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="RefOntoUML_Class121", type=RefOntoUML_Class, multiplicity=Multiplicity(0, 9999))
    }
)
ownedAttribute126: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute126",
    ends={
        Property(name="Property127", type=RefOntoUML_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="datatype", type=RefOntoUML_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mergedPackage135: BinaryAssociation = BinaryAssociation(
    name="mergedPackage135",
    ends={
        Property(name="RefOntoUML_Package136", type=RefOntoUML_PackageMerge, multiplicity=Multiplicity(1, 1)),
        Property(name="RefOntoUML_PackageMerge", type=RefOntoUML_Package, multiplicity=Multiplicity(1, 1))
    }
)
subExpression129: BinaryAssociation = BinaryAssociation(
    name="subExpression129",
    ends={
        Property(name="StringExpression", type=RefOntoUML_StringExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="owningExpression", type=RefOntoUML_StringExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningExpression131: BinaryAssociation = BinaryAssociation(
    name="owningExpression131",
    ends={
        Property(name="StringExpression132", type=RefOntoUML_StringExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="subExpression", type=RefOntoUML_StringExpression, multiplicity=Multiplicity(0, 1))
    }
)
operand133: BinaryAssociation = BinaryAssociation(
    name="operand133",
    ends={
        Property(name="RefOntoUML_ValueSpecification134", type=RefOntoUML_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="RefOntoUML_Expression", type=RefOntoUML_ValueSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
receivingPackage137: BinaryAssociation = BinaryAssociation(
    name="receivingPackage137",
    ends={
        Property(name="Package138", type=RefOntoUML_PackageMerge, multiplicity=Multiplicity(1, 1)),
        Property(name="packageMerge", type=RefOntoUML_Package, multiplicity=Multiplicity(1, 1))
    }
)
classifier139: BinaryAssociation = BinaryAssociation(
    name="classifier139",
    ends={
        Property(name="RefOntoUML_Classifier140", type=RefOntoUML_InstanceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="RefOntoUML_InstanceSpecification", type=RefOntoUML_Classifier, multiplicity=Multiplicity(0, 9999))
    }
)
slot141: BinaryAssociation = BinaryAssociation(
    name="slot141",
    ends={
        Property(name="Slot", type=RefOntoUML_InstanceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="owningInstance", type=RefOntoUML_Slot, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedLiteral150: BinaryAssociation = BinaryAssociation(
    name="ownedLiteral150",
    ends={
        Property(name="EnumerationLiteral", type=RefOntoUML_Enumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="enumeration", type=RefOntoUML_EnumerationLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specification142: BinaryAssociation = BinaryAssociation(
    name="specification142",
    ends={
        Property(name="RefOntoUML_ValueSpecification144", type=RefOntoUML_InstanceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="RefOntoUML_InstanceSpecification143", type=RefOntoUML_ValueSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
definingFeature145: BinaryAssociation = BinaryAssociation(
    name="definingFeature145",
    ends={
        Property(name="RefOntoUML_StructuralFeature", type=RefOntoUML_Slot, multiplicity=Multiplicity(1, 1)),
        Property(name="RefOntoUML_Slot", type=RefOntoUML_StructuralFeature, multiplicity=Multiplicity(1, 1))
    }
)
value146: BinaryAssociation = BinaryAssociation(
    name="value146",
    ends={
        Property(name="RefOntoUML_ValueSpecification148", type=RefOntoUML_Slot, multiplicity=Multiplicity(1, 1)),
        Property(name="RefOntoUML_Slot147", type=RefOntoUML_ValueSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningInstance149: BinaryAssociation = BinaryAssociation(
    name="owningInstance149",
    ends={
        Property(name="InstanceSpecification", type=RefOntoUML_Slot, multiplicity=Multiplicity(1, 1)),
        Property(name="slot", type=RefOntoUML_InstanceSpecification, multiplicity=Multiplicity(1, 1))
    }
)
ownedRegions154: BinaryAssociation = BinaryAssociation(
    name="ownedRegions154",
    ends={
        Property(name="ReferenceRegion", type=RefOntoUML_ReferenceStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="structure", type=RefOntoUML_ReferenceRegion, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enumeration151: BinaryAssociation = BinaryAssociation(
    name="enumeration151",
    ends={
        Property(name="Enumeration", type=RefOntoUML_EnumerationLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedLiteral", type=RefOntoUML_Enumeration, multiplicity=Multiplicity(0, 1))
    }
)
groundingStructure152: BinaryAssociation = BinaryAssociation(
    name="groundingStructure152",
    ends={
        Property(name="MeasurementStructure", type=RefOntoUML_MeasurementEnumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="groundedEnumeration", type=RefOntoUML_MeasurementStructure, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
groundingRegion153: BinaryAssociation = BinaryAssociation(
    name="groundingRegion153",
    ends={
        Property(name="MeasurementRegion", type=RefOntoUML_MeasurementLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="groundedLiteral", type=RefOntoUML_MeasurementRegion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
domain156: BinaryAssociation = BinaryAssociation(
    name="domain156",
    ends={
        Property(name="MeasurementDomain", type=RefOntoUML_MeasurementDimension, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedDimensions", type=RefOntoUML_MeasurementDomain, multiplicity=Multiplicity(0, 1))
    }
)
lowerBound157: BinaryAssociation = BinaryAssociation(
    name="lowerBound157",
    ends={
        Property(name="RefOntoUML_BasicMeasurementRegion", type=RefOntoUML_MeasurementDimension, multiplicity=Multiplicity(1, 1)),
        Property(name="RefOntoUML_MeasurementDimension", type=RefOntoUML_BasicMeasurementRegion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
groundedEnumeration155: BinaryAssociation = BinaryAssociation(
    name="groundedEnumeration155",
    ends={
        Property(name="MeasurementEnumeration", type=RefOntoUML_MeasurementStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="groundingStructure", type=RefOntoUML_MeasurementEnumeration, multiplicity=Multiplicity(0, 1))
    }
)
upperBound158: BinaryAssociation = BinaryAssociation(
    name="upperBound158",
    ends={
        Property(name="RefOntoUML_BasicMeasurementRegion160", type=RefOntoUML_MeasurementDimension, multiplicity=Multiplicity(1, 1)),
        Property(name="RefOntoUML_MeasurementDimension159", type=RefOntoUML_BasicMeasurementRegion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
structure164: BinaryAssociation = BinaryAssociation(
    name="structure164",
    ends={
        Property(name="ReferenceStructure", type=RefOntoUML_ReferenceRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedRegions", type=RefOntoUML_ReferenceStructure, multiplicity=Multiplicity(0, 1))
    }
)
groundedLiteral165: BinaryAssociation = BinaryAssociation(
    name="groundedLiteral165",
    ends={
        Property(name="MeasurementLiteral", type=RefOntoUML_MeasurementRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="groundingRegion", type=RefOntoUML_MeasurementLiteral, multiplicity=Multiplicity(0, 1))
    }
)
ownedDimensions161: BinaryAssociation = BinaryAssociation(
    name="ownedDimensions161",
    ends={
        Property(name="MeasurementDimension", type=RefOntoUML_MeasurementDomain, multiplicity=Multiplicity(1, 1)),
        Property(name="domain", type=RefOntoUML_MeasurementDimension, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
compositionRule162: BinaryAssociation = BinaryAssociation(
    name="compositionRule162",
    ends={
        Property(name="RefOntoUML_Expression163", type=RefOntoUML_MeasurementDomain, multiplicity=Multiplicity(1, 1)),
        Property(name="RefOntoUML_MeasurementDomain", type=RefOntoUML_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedRegions166: BinaryAssociation = BinaryAssociation(
    name="ownedRegions166",
    ends={
        Property(name="RefOntoUML_BasicMeasurementRegion167", type=RefOntoUML_ComposedMeasurementRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="RefOntoUML_ComposedMeasurementRegion", type=RefOntoUML_BasicMeasurementRegion, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
instance168: BinaryAssociation = BinaryAssociation(
    name="instance168",
    ends={
        Property(name="RefOntoUML_InstanceSpecification169", type=RefOntoUML_InstanceValue, multiplicity=Multiplicity(1, 1)),
        Property(name="RefOntoUML_InstanceValue", type=RefOntoUML_InstanceSpecification, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_RefOntoUML_Comment_Element = Generalization(general=Element, specific=RefOntoUML_Comment)
gen_RefOntoUML_Element_EModelElement = Generalization(general=EModelElement, specific=RefOntoUML_Element)
gen_RefOntoUML_Package_Namespace = Generalization(general=Namespace, specific=RefOntoUML_Package)
gen_RefOntoUML_Package_PackageableElement = Generalization(general=PackageableElement, specific=RefOntoUML_Package)
gen_RefOntoUML_PackageableElement_NamedElement = Generalization(general=NamedElement, specific=RefOntoUML_PackageableElement)
gen_RefOntoUML_NamedElement_Element = Generalization(general=Element, specific=RefOntoUML_NamedElement)
gen_RefOntoUML_Dependency_PackageableElement = Generalization(general=PackageableElement, specific=RefOntoUML_Dependency)
gen_RefOntoUML_Dependency_DirectedRelationship = Generalization(general=DirectedRelationship, specific=RefOntoUML_Dependency)
gen_RefOntoUML_Relationship_Element = Generalization(general=Element, specific=RefOntoUML_Relationship)
gen_RefOntoUML_DirectedRelationship_Relationship = Generalization(general=Relationship, specific=RefOntoUML_DirectedRelationship)
gen_RefOntoUML_Namespace_NamedElement = Generalization(general=NamedElement, specific=RefOntoUML_Namespace)
gen_RefOntoUML_ElementImport_DirectedRelationship = Generalization(general=DirectedRelationship, specific=RefOntoUML_ElementImport)
gen_RefOntoUML_PackageImport_DirectedRelationship = Generalization(general=DirectedRelationship, specific=RefOntoUML_PackageImport)
gen_RefOntoUML_Constraintx_PackageableElement = Generalization(general=PackageableElement, specific=RefOntoUML_Constraintx)
gen_RefOntoUML_ValueSpecification_PackageableElement = Generalization(general=PackageableElement, specific=RefOntoUML_ValueSpecification)
gen_RefOntoUML_ValueSpecification_TypedElement = Generalization(general=TypedElement, specific=RefOntoUML_ValueSpecification)
gen_RefOntoUML_TypedElement_NamedElement = Generalization(general=NamedElement, specific=RefOntoUML_TypedElement)
gen_RefOntoUML_Type_PackageableElement = Generalization(general=PackageableElement, specific=RefOntoUML_Type)
gen_RefOntoUML_Association_Classifier = Generalization(general=Classifier, specific=RefOntoUML_Association)
gen_RefOntoUML_Association_Relationship = Generalization(general=Relationship, specific=RefOntoUML_Association)
gen_RefOntoUML_Classifier_Namespace = Generalization(general=Namespace, specific=RefOntoUML_Classifier)
gen_RefOntoUML_Classifier_RedefinableElement = Generalization(general=RedefinableElement, specific=RefOntoUML_Classifier)
gen_RefOntoUML_Classifier_Type = Generalization(general=Type, specific=RefOntoUML_Classifier)
gen_RefOntoUML_RedefinableElement_NamedElement = Generalization(general=NamedElement, specific=RefOntoUML_RedefinableElement)
gen_RefOntoUML_Generalization_DirectedRelationship = Generalization(general=DirectedRelationship, specific=RefOntoUML_Generalization)
gen_RefOntoUML_GeneralizationSet_PackageableElement = Generalization(general=PackageableElement, specific=RefOntoUML_GeneralizationSet)
gen_RefOntoUML_OpaqueExpression_ValueSpecification = Generalization(general=ValueSpecification, specific=RefOntoUML_OpaqueExpression)
gen_RefOntoUML_Feature_RedefinableElement = Generalization(general=RedefinableElement, specific=RefOntoUML_Feature)
gen_RefOntoUML_MultiplicityElement_Element = Generalization(general=Element, specific=RefOntoUML_MultiplicityElement)
gen_RefOntoUML_Property_StructuralFeature = Generalization(general=StructuralFeature, specific=RefOntoUML_Property)
gen_RefOntoUML_Class_Classifier = Generalization(general=Classifier, specific=RefOntoUML_Class)
gen_RefOntoUML_Model_Package = Generalization(general=Package, specific=RefOntoUML_Model)
gen_RefOntoUML_DataType_Classifier = Generalization(general=Classifier, specific=RefOntoUML_DataType)
gen_RefOntoUML_StructuralFeature_Feature = Generalization(general=Feature, specific=RefOntoUML_StructuralFeature)
gen_RefOntoUML_StructuralFeature_TypedElement = Generalization(general=TypedElement, specific=RefOntoUML_StructuralFeature)
gen_RefOntoUML_StructuralFeature_MultiplicityElement = Generalization(general=MultiplicityElement, specific=RefOntoUML_StructuralFeature)
gen_RefOntoUML_StringExpression_Expression = Generalization(general=Expression, specific=RefOntoUML_StringExpression)
gen_RefOntoUML_Expression_ValueSpecification = Generalization(general=ValueSpecification, specific=RefOntoUML_Expression)
gen_RefOntoUML_PackageMerge_DirectedRelationship = Generalization(general=DirectedRelationship, specific=RefOntoUML_PackageMerge)
gen_RefOntoUML_InstanceSpecification_PackageableElement = Generalization(general=PackageableElement, specific=RefOntoUML_InstanceSpecification)
gen_RefOntoUML_EnumerationLiteral_InstanceSpecification = Generalization(general=InstanceSpecification, specific=RefOntoUML_EnumerationLiteral)
gen_RefOntoUML_Slot_Element = Generalization(general=Element, specific=RefOntoUML_Slot)
gen_RefOntoUML_LiteralSpecification_ValueSpecification = Generalization(general=ValueSpecification, specific=RefOntoUML_LiteralSpecification)
gen_RefOntoUML_Enumeration_DataType = Generalization(general=DataType, specific=RefOntoUML_Enumeration)
gen_RefOntoUML_ReferenceStructure_DataType = Generalization(general=DataType, specific=RefOntoUML_ReferenceStructure)
gen_RefOntoUML_NominalStructure_ReferenceStructure = Generalization(general=ReferenceStructure, specific=RefOntoUML_NominalStructure)
gen_RefOntoUML_MeasurementEnumeration_Enumeration = Generalization(general=Enumeration_, specific=RefOntoUML_MeasurementEnumeration)
gen_RefOntoUML_MeasurementLiteral_EnumerationLiteral = Generalization(general=EnumerationLiteral, specific=RefOntoUML_MeasurementLiteral)
gen_RefOntoUML_PrimitiveType_DataType = Generalization(general=DataType, specific=RefOntoUML_PrimitiveType)
gen_RefOntoUML_StringNominalStructure_NominalStructure = Generalization(general=NominalStructure, specific=RefOntoUML_StringNominalStructure)
gen_RefOntoUML_MeasurementStructure_ReferenceStructure = Generalization(general=ReferenceStructure, specific=RefOntoUML_MeasurementStructure)
gen_RefOntoUML_MeasurementDimension_MeasurementStructure = Generalization(general=MeasurementStructure, specific=RefOntoUML_MeasurementDimension)
gen_RefOntoUML_DecimalIntervalDimension_IntervalDimension = Generalization(general=IntervalDimension, specific=RefOntoUML_DecimalIntervalDimension)
gen_RefOntoUML_OrdinalDimension_MeasurementDimension = Generalization(general=MeasurementDimension, specific=RefOntoUML_OrdinalDimension)
gen_RefOntoUML_IntegerOrdinalDimension_OrdinalDimension = Generalization(general=OrdinalDimension, specific=RefOntoUML_IntegerOrdinalDimension)
gen_RefOntoUML_DecimalOrdinalDimension_OrdinalDimension = Generalization(general=OrdinalDimension, specific=RefOntoUML_DecimalOrdinalDimension)
gen_RefOntoUML_IntervalDimension_MeasurementDimension = Generalization(general=MeasurementDimension, specific=RefOntoUML_IntervalDimension)
gen_RefOntoUML_IntegerIntervalDimension_IntervalDimension = Generalization(general=IntervalDimension, specific=RefOntoUML_IntegerIntervalDimension)
gen_RefOntoUML_DecimalRationalDimension_RationalDimension = Generalization(general=RationalDimension, specific=RefOntoUML_DecimalRationalDimension)
gen_RefOntoUML_RationalDimension_MeasurementDimension = Generalization(general=MeasurementDimension, specific=RefOntoUML_RationalDimension)
gen_RefOntoUML_IntegerRationalDimension_RationalDimension = Generalization(general=RationalDimension, specific=RefOntoUML_IntegerRationalDimension)
gen_RefOntoUML_MeasurementRegion_ReferenceRegion = Generalization(general=ReferenceRegion, specific=RefOntoUML_MeasurementRegion)
gen_RefOntoUML_BasicMeasurementRegion_MeasurementRegion = Generalization(general=MeasurementRegion, specific=RefOntoUML_BasicMeasurementRegion)
gen_RefOntoUML_MeasurementDomain_MeasurementStructure = Generalization(general=MeasurementStructure, specific=RefOntoUML_MeasurementDomain)
gen_RefOntoUML_ReferenceRegion_ValueSpecification = Generalization(general=ValueSpecification, specific=RefOntoUML_ReferenceRegion)
gen_RefOntoUML_DecimalMeasurementRegion_BasicMeasurementRegion = Generalization(general=BasicMeasurementRegion, specific=RefOntoUML_DecimalMeasurementRegion)
gen_RefOntoUML_DecimalMeasurementRegion_LiteralDecimal = Generalization(general=LiteralDecimal, specific=RefOntoUML_DecimalMeasurementRegion)
gen_RefOntoUML_IntegerMeasurementRegion_BasicMeasurementRegion = Generalization(general=BasicMeasurementRegion, specific=RefOntoUML_IntegerMeasurementRegion)
gen_RefOntoUML_IntegerMeasurementRegion_LiteralInteger = Generalization(general=LiteralInteger, specific=RefOntoUML_IntegerMeasurementRegion)
gen_RefOntoUML_ComposedMeasurementRegion_MeasurementRegion = Generalization(general=MeasurementRegion, specific=RefOntoUML_ComposedMeasurementRegion)
gen_RefOntoUML_NominalRegion_ReferenceRegion = Generalization(general=ReferenceRegion, specific=RefOntoUML_NominalRegion)
gen_RefOntoUML_StringNominalRegion_NominalRegion = Generalization(general=NominalRegion, specific=RefOntoUML_StringNominalRegion)
gen_RefOntoUML_StringNominalRegion_LiteralString = Generalization(general=LiteralString, specific=RefOntoUML_StringNominalRegion)
gen_RefOntoUML_LiteralInteger_LiteralSpecification = Generalization(general=LiteralSpecification, specific=RefOntoUML_LiteralInteger)
gen_RefOntoUML_LiteralDecimal_LiteralSpecification = Generalization(general=LiteralSpecification, specific=RefOntoUML_LiteralDecimal)
gen_RefOntoUML_LiteralString_LiteralSpecification = Generalization(general=LiteralSpecification, specific=RefOntoUML_LiteralString)
gen_RefOntoUML_InstanceValue_ValueSpecification = Generalization(general=ValueSpecification, specific=RefOntoUML_InstanceValue)
gen_RefOntoUML_LiteralBoolean_LiteralSpecification = Generalization(general=LiteralSpecification, specific=RefOntoUML_LiteralBoolean)
gen_RefOntoUML_LiteralNull_LiteralSpecification = Generalization(general=LiteralSpecification, specific=RefOntoUML_LiteralNull)
gen_RefOntoUML_MixinClass_ObjectClass = Generalization(general=ObjectClass, specific=RefOntoUML_MixinClass)
gen_RefOntoUML_LiteralUnlimitedNatural_LiteralSpecification = Generalization(general=LiteralSpecification, specific=RefOntoUML_LiteralUnlimitedNatural)
gen_RefOntoUML_ObjectClass_Class = Generalization(general=Class_, specific=RefOntoUML_ObjectClass)
gen_RefOntoUML_MomentClass_Class = Generalization(general=Class_, specific=RefOntoUML_MomentClass)
gen_RefOntoUML_SortalClass_ObjectClass = Generalization(general=ObjectClass, specific=RefOntoUML_SortalClass)
gen_RefOntoUML_Phase_AntiRigidSortalClass = Generalization(general=AntiRigidSortalClass, specific=RefOntoUML_Phase)
gen_RefOntoUML_RigidSortalClass_SortalClass = Generalization(general=SortalClass, specific=RefOntoUML_RigidSortalClass)
gen_RefOntoUML_AntiRigidSortalClass_SortalClass = Generalization(general=SortalClass, specific=RefOntoUML_AntiRigidSortalClass)
gen_RefOntoUML_SubstanceSortal_RigidSortalClass = Generalization(general=RigidSortalClass, specific=RefOntoUML_SubstanceSortal)
gen_RefOntoUML_SubKind_RigidSortalClass = Generalization(general=RigidSortalClass, specific=RefOntoUML_SubKind)
gen_RefOntoUML_Kind_SubstanceSortal = Generalization(general=SubstanceSortal, specific=RefOntoUML_Kind)
gen_RefOntoUML_Quantity_SubstanceSortal = Generalization(general=SubstanceSortal, specific=RefOntoUML_Quantity)
gen_RefOntoUML_Collective_SubstanceSortal = Generalization(general=SubstanceSortal, specific=RefOntoUML_Collective)
gen_RefOntoUML_Role_AntiRigidSortalClass = Generalization(general=AntiRigidSortalClass, specific=RefOntoUML_Role)
gen_RefOntoUML_RigidMixinClass_MixinClass = Generalization(general=MixinClass, specific=RefOntoUML_RigidMixinClass)
gen_RefOntoUML_NonRigidMixinClass_MixinClass = Generalization(general=MixinClass, specific=RefOntoUML_NonRigidMixinClass)
gen_RefOntoUML_Category_RigidMixinClass = Generalization(general=RigidMixinClass, specific=RefOntoUML_Category)
gen_RefOntoUML_AntiRigidMixinClass_NonRigidMixinClass = Generalization(general=NonRigidMixinClass, specific=RefOntoUML_AntiRigidMixinClass)
gen_RefOntoUML_SemiRigidMixinClass_NonRigidMixinClass = Generalization(general=NonRigidMixinClass, specific=RefOntoUML_SemiRigidMixinClass)
gen_RefOntoUML_RoleMixin_AntiRigidMixinClass = Generalization(general=AntiRigidMixinClass, specific=RefOntoUML_RoleMixin)
gen_RefOntoUML_NominalQuality_Quality = Generalization(general=Quality, specific=RefOntoUML_NominalQuality)
gen_RefOntoUML_NonPerceivableQuality_MeasurableQuality = Generalization(general=MeasurableQuality, specific=RefOntoUML_NonPerceivableQuality)
gen_RefOntoUML_PerceivableQuality_MeasurableQuality = Generalization(general=MeasurableQuality, specific=RefOntoUML_PerceivableQuality)
gen_RefOntoUML_Mixin_SemiRigidMixinClass = Generalization(general=SemiRigidMixinClass, specific=RefOntoUML_Mixin)
gen_RefOntoUML_IntrinsicMomentClass_MomentClass = Generalization(general=MomentClass, specific=RefOntoUML_IntrinsicMomentClass)
gen_RefOntoUML_Mode_IntrinsicMomentClass = Generalization(general=IntrinsicMomentClass, specific=RefOntoUML_Mode)
gen_RefOntoUML_Quality_IntrinsicMomentClass = Generalization(general=IntrinsicMomentClass, specific=RefOntoUML_Quality)
gen_RefOntoUML_MeasurableQuality_Quality = Generalization(general=Quality, specific=RefOntoUML_MeasurableQuality)
gen_RefOntoUML_Relator_MomentClass = Generalization(general=MomentClass, specific=RefOntoUML_Relator)
gen_RefOntoUML_DirectedBinaryAssociation_Association = Generalization(general=Association, specific=RefOntoUML_DirectedBinaryAssociation)
gen_RefOntoUML_Meronymic_DirectedBinaryAssociation = Generalization(general=DirectedBinaryAssociation, specific=RefOntoUML_Meronymic)
gen_RefOntoUML_componentOf_Meronymic = Generalization(general=Meronymic, specific=RefOntoUML_componentOf)
gen_RefOntoUML_subQuantityOf_Meronymic = Generalization(general=Meronymic, specific=RefOntoUML_subQuantityOf)
gen_RefOntoUML_subCollectionOf_Meronymic = Generalization(general=Meronymic, specific=RefOntoUML_subCollectionOf)
gen_RefOntoUML_memberOf_Meronymic = Generalization(general=Meronymic, specific=RefOntoUML_memberOf)
gen_RefOntoUML_DependencyRelationship_DirectedBinaryAssociation = Generalization(general=DirectedBinaryAssociation, specific=RefOntoUML_DependencyRelationship)
gen_RefOntoUML_Characterization_DependencyRelationship = Generalization(general=DependencyRelationship, specific=RefOntoUML_Characterization)
gen_RefOntoUML_Mediation_DependencyRelationship = Generalization(general=DependencyRelationship, specific=RefOntoUML_Mediation)
gen_RefOntoUML_FormalAssociation_Association = Generalization(general=Association, specific=RefOntoUML_FormalAssociation)
gen_RefOntoUML_Derivation_DependencyRelationship = Generalization(general=DependencyRelationship, specific=RefOntoUML_Derivation)
gen_RefOntoUML_Structuration_DependencyRelationship = Generalization(general=DependencyRelationship, specific=RefOntoUML_Structuration)
gen_RefOntoUML_MaterialAssociation_Association = Generalization(general=Association, specific=RefOntoUML_MaterialAssociation)

# Domain Model
domain_model = DomainModel(
    name="RefOntoUML",
    types={RefOntoUML_Comment, Element, RefOntoUML_Element, EModelElement, RefOntoUML_Package, Namespace, PackageableElement, RefOntoUML_PackageableElement, RefOntoUML_Type, RefOntoUML_PackageMerge, NamedElement, RefOntoUML_NamedElement, RefOntoUML_StringExpression, DirectedRelationship, RefOntoUML_Dependency, RefOntoUML_Namespace, RefOntoUML_Relationship, RefOntoUML_DirectedRelationship, Relationship, RefOntoUML_Constraintx, RefOntoUML_ElementImport, RefOntoUML_PackageImport, RefOntoUML_ValueSpecification, TypedElement, RefOntoUML_TypedElement, RefOntoUML_Association, Classifier, RefOntoUML_Classifier, RedefinableElement, Type, RefOntoUML_Property, RefOntoUML_Generalization, RefOntoUML_GeneralizationSet, RefOntoUML_Feature, RefOntoUML_RedefinableElement, RefOntoUML_OpaqueExpression, ValueSpecification, RefOntoUML_MultiplicityElement, StructuralFeature, RefOntoUML_Class, RefOntoUML_DataType, RefOntoUML_Model, Package, RefOntoUML_StructuralFeature, Feature, MultiplicityElement, Expression, RefOntoUML_Expression, RefOntoUML_InstanceSpecification, RefOntoUML_Slot, RefOntoUML_EnumerationLiteral, InstanceSpecification, RefOntoUML_LiteralSpecification, RefOntoUML_Enumeration, DataType, RefOntoUML_ReferenceStructure, RefOntoUML_ReferenceRegion, RefOntoUML_NominalStructure, ReferenceStructure, RefOntoUML_MeasurementEnumeration, Enumeration_, RefOntoUML_MeasurementStructure, RefOntoUML_MeasurementLiteral, EnumerationLiteral, RefOntoUML_MeasurementRegion, RefOntoUML_PrimitiveType, RefOntoUML_MeasurementDomain, RefOntoUML_BasicMeasurementRegion, RefOntoUML_StringNominalStructure, NominalStructure, RefOntoUML_MeasurementDimension, MeasurementStructure, RefOntoUML_DecimalIntervalDimension, RefOntoUML_OrdinalDimension, MeasurementDimension, RefOntoUML_IntegerOrdinalDimension, OrdinalDimension, RefOntoUML_DecimalOrdinalDimension, RefOntoUML_IntervalDimension, RefOntoUML_IntegerIntervalDimension, IntervalDimension, RefOntoUML_DecimalRationalDimension, RefOntoUML_RationalDimension, RefOntoUML_IntegerRationalDimension, RationalDimension, ReferenceRegion, MeasurementRegion, RefOntoUML_DecimalMeasurementRegion, BasicMeasurementRegion, LiteralDecimal, RefOntoUML_IntegerMeasurementRegion, LiteralInteger, RefOntoUML_ComposedMeasurementRegion, RefOntoUML_NominalRegion, RefOntoUML_StringNominalRegion, NominalRegion, LiteralString, RefOntoUML_LiteralInteger, LiteralSpecification, RefOntoUML_LiteralDecimal, RefOntoUML_LiteralString, RefOntoUML_InstanceValue, RefOntoUML_LiteralBoolean, RefOntoUML_LiteralNull, RefOntoUML_MixinClass, RefOntoUML_LiteralUnlimitedNatural, RefOntoUML_ObjectClass, Class_, RefOntoUML_MomentClass, RefOntoUML_SortalClass, ObjectClass, RefOntoUML_Phase, AntiRigidSortalClass, RefOntoUML_RigidSortalClass, SortalClass, RefOntoUML_AntiRigidSortalClass, RefOntoUML_SubstanceSortal, RigidSortalClass, RefOntoUML_SubKind, RefOntoUML_Kind, SubstanceSortal, RefOntoUML_Quantity, RefOntoUML_Collective, RefOntoUML_Role, RefOntoUML_RigidMixinClass, MixinClass, RefOntoUML_NonRigidMixinClass, RefOntoUML_Category, RigidMixinClass, RefOntoUML_AntiRigidMixinClass, NonRigidMixinClass, RefOntoUML_SemiRigidMixinClass, RefOntoUML_RoleMixin, AntiRigidMixinClass, RefOntoUML_NominalQuality, RefOntoUML_NonPerceivableQuality, MeasurableQuality, RefOntoUML_PerceivableQuality, RefOntoUML_Mixin, SemiRigidMixinClass, RefOntoUML_IntrinsicMomentClass, MomentClass, RefOntoUML_Mode, IntrinsicMomentClass, RefOntoUML_Quality, RefOntoUML_MeasurableQuality, Quality, RefOntoUML_Relator, RefOntoUML_DirectedBinaryAssociation, Association, RefOntoUML_Meronymic, DirectedBinaryAssociation, RefOntoUML_componentOf, RefOntoUML_subQuantityOf, Meronymic, RefOntoUML_subCollectionOf, RefOntoUML_memberOf, RefOntoUML_DependencyRelationship, RefOntoUML_Characterization, DependencyRelationship, RefOntoUML_Mediation, RefOntoUML_FormalAssociation, RefOntoUML_Derivation, RefOntoUML_Structuration, RefOntoUML_MaterialAssociation, VisibilityKind, AggregationKind},
    associations={annotatedElement0, ownedElement2, owner4, ownedComment6, packagedElement11, nestedPackage13, ownedType9, packageMerge10, nestingPackage15, nameExpression19, clientDependency17, namespace18, supplier20, client22, source23, target25, relatedElement28, ownedRule33, elementImport30, packageImport31, member34, importedMember36, ownedMember39, importedPackage45, importedElement41, importingNamespace43, importingNamespace47, constrainedElement49, specification51, context53, type55, package56, ownedEnd58, memberEnd59, endType61, navigableOwnedEnd63, general74, generalization65, powertypeExtent66, feature67, inheritedMember68, redefinedClassifier71, attribute76, general84, redefinedElement80, redefinitionContext81, generalizationSet86, specific88, featuringClassifier94, powertype90, generalization92, upperValue96, lowerValue98, class101, datatype102, opposite112, redefinedProperty105, owningAssociation107, defaultValue108, subsettedProperty115, association117, ownedAttribute124, nestedClassifier119, superClass122, ownedAttribute126, mergedPackage135, subExpression129, owningExpression131, operand133, receivingPackage137, classifier139, slot141, ownedLiteral150, specification142, definingFeature145, value146, owningInstance149, ownedRegions154, enumeration151, groundingStructure152, groundingRegion153, domain156, lowerBound157, groundedEnumeration155, upperBound158, structure164, groundedLiteral165, ownedDimensions161, compositionRule162, ownedRegions166, instance168},
    generalizations={gen_RefOntoUML_Comment_Element, gen_RefOntoUML_Element_EModelElement, gen_RefOntoUML_Package_Namespace, gen_RefOntoUML_Package_PackageableElement, gen_RefOntoUML_PackageableElement_NamedElement, gen_RefOntoUML_NamedElement_Element, gen_RefOntoUML_Dependency_PackageableElement, gen_RefOntoUML_Dependency_DirectedRelationship, gen_RefOntoUML_Relationship_Element, gen_RefOntoUML_DirectedRelationship_Relationship, gen_RefOntoUML_Namespace_NamedElement, gen_RefOntoUML_ElementImport_DirectedRelationship, gen_RefOntoUML_PackageImport_DirectedRelationship, gen_RefOntoUML_Constraintx_PackageableElement, gen_RefOntoUML_ValueSpecification_PackageableElement, gen_RefOntoUML_ValueSpecification_TypedElement, gen_RefOntoUML_TypedElement_NamedElement, gen_RefOntoUML_Type_PackageableElement, gen_RefOntoUML_Association_Classifier, gen_RefOntoUML_Association_Relationship, gen_RefOntoUML_Classifier_Namespace, gen_RefOntoUML_Classifier_RedefinableElement, gen_RefOntoUML_Classifier_Type, gen_RefOntoUML_RedefinableElement_NamedElement, gen_RefOntoUML_Generalization_DirectedRelationship, gen_RefOntoUML_GeneralizationSet_PackageableElement, gen_RefOntoUML_OpaqueExpression_ValueSpecification, gen_RefOntoUML_Feature_RedefinableElement, gen_RefOntoUML_MultiplicityElement_Element, gen_RefOntoUML_Property_StructuralFeature, gen_RefOntoUML_Class_Classifier, gen_RefOntoUML_Model_Package, gen_RefOntoUML_DataType_Classifier, gen_RefOntoUML_StructuralFeature_Feature, gen_RefOntoUML_StructuralFeature_TypedElement, gen_RefOntoUML_StructuralFeature_MultiplicityElement, gen_RefOntoUML_StringExpression_Expression, gen_RefOntoUML_Expression_ValueSpecification, gen_RefOntoUML_PackageMerge_DirectedRelationship, gen_RefOntoUML_InstanceSpecification_PackageableElement, gen_RefOntoUML_EnumerationLiteral_InstanceSpecification, gen_RefOntoUML_Slot_Element, gen_RefOntoUML_LiteralSpecification_ValueSpecification, gen_RefOntoUML_Enumeration_DataType, gen_RefOntoUML_ReferenceStructure_DataType, gen_RefOntoUML_NominalStructure_ReferenceStructure, gen_RefOntoUML_MeasurementEnumeration_Enumeration, gen_RefOntoUML_MeasurementLiteral_EnumerationLiteral, gen_RefOntoUML_PrimitiveType_DataType, gen_RefOntoUML_StringNominalStructure_NominalStructure, gen_RefOntoUML_MeasurementStructure_ReferenceStructure, gen_RefOntoUML_MeasurementDimension_MeasurementStructure, gen_RefOntoUML_DecimalIntervalDimension_IntervalDimension, gen_RefOntoUML_OrdinalDimension_MeasurementDimension, gen_RefOntoUML_IntegerOrdinalDimension_OrdinalDimension, gen_RefOntoUML_DecimalOrdinalDimension_OrdinalDimension, gen_RefOntoUML_IntervalDimension_MeasurementDimension, gen_RefOntoUML_IntegerIntervalDimension_IntervalDimension, gen_RefOntoUML_DecimalRationalDimension_RationalDimension, gen_RefOntoUML_RationalDimension_MeasurementDimension, gen_RefOntoUML_IntegerRationalDimension_RationalDimension, gen_RefOntoUML_MeasurementRegion_ReferenceRegion, gen_RefOntoUML_BasicMeasurementRegion_MeasurementRegion, gen_RefOntoUML_MeasurementDomain_MeasurementStructure, gen_RefOntoUML_ReferenceRegion_ValueSpecification, gen_RefOntoUML_DecimalMeasurementRegion_BasicMeasurementRegion, gen_RefOntoUML_DecimalMeasurementRegion_LiteralDecimal, gen_RefOntoUML_IntegerMeasurementRegion_BasicMeasurementRegion, gen_RefOntoUML_IntegerMeasurementRegion_LiteralInteger, gen_RefOntoUML_ComposedMeasurementRegion_MeasurementRegion, gen_RefOntoUML_NominalRegion_ReferenceRegion, gen_RefOntoUML_StringNominalRegion_NominalRegion, gen_RefOntoUML_StringNominalRegion_LiteralString, gen_RefOntoUML_LiteralInteger_LiteralSpecification, gen_RefOntoUML_LiteralDecimal_LiteralSpecification, gen_RefOntoUML_LiteralString_LiteralSpecification, gen_RefOntoUML_InstanceValue_ValueSpecification, gen_RefOntoUML_LiteralBoolean_LiteralSpecification, gen_RefOntoUML_LiteralNull_LiteralSpecification, gen_RefOntoUML_MixinClass_ObjectClass, gen_RefOntoUML_LiteralUnlimitedNatural_LiteralSpecification, gen_RefOntoUML_ObjectClass_Class, gen_RefOntoUML_MomentClass_Class, gen_RefOntoUML_SortalClass_ObjectClass, gen_RefOntoUML_Phase_AntiRigidSortalClass, gen_RefOntoUML_RigidSortalClass_SortalClass, gen_RefOntoUML_AntiRigidSortalClass_SortalClass, gen_RefOntoUML_SubstanceSortal_RigidSortalClass, gen_RefOntoUML_SubKind_RigidSortalClass, gen_RefOntoUML_Kind_SubstanceSortal, gen_RefOntoUML_Quantity_SubstanceSortal, gen_RefOntoUML_Collective_SubstanceSortal, gen_RefOntoUML_Role_AntiRigidSortalClass, gen_RefOntoUML_RigidMixinClass_MixinClass, gen_RefOntoUML_NonRigidMixinClass_MixinClass, gen_RefOntoUML_Category_RigidMixinClass, gen_RefOntoUML_AntiRigidMixinClass_NonRigidMixinClass, gen_RefOntoUML_SemiRigidMixinClass_NonRigidMixinClass, gen_RefOntoUML_RoleMixin_AntiRigidMixinClass, gen_RefOntoUML_NominalQuality_Quality, gen_RefOntoUML_NonPerceivableQuality_MeasurableQuality, gen_RefOntoUML_PerceivableQuality_MeasurableQuality, gen_RefOntoUML_Mixin_SemiRigidMixinClass, gen_RefOntoUML_IntrinsicMomentClass_MomentClass, gen_RefOntoUML_Mode_IntrinsicMomentClass, gen_RefOntoUML_Quality_IntrinsicMomentClass, gen_RefOntoUML_MeasurableQuality_Quality, gen_RefOntoUML_Relator_MomentClass, gen_RefOntoUML_DirectedBinaryAssociation_Association, gen_RefOntoUML_Meronymic_DirectedBinaryAssociation, gen_RefOntoUML_componentOf_Meronymic, gen_RefOntoUML_subQuantityOf_Meronymic, gen_RefOntoUML_subCollectionOf_Meronymic, gen_RefOntoUML_memberOf_Meronymic, gen_RefOntoUML_DependencyRelationship_DirectedBinaryAssociation, gen_RefOntoUML_Characterization_DependencyRelationship, gen_RefOntoUML_Mediation_DependencyRelationship, gen_RefOntoUML_FormalAssociation_Association, gen_RefOntoUML_Derivation_DependencyRelationship, gen_RefOntoUML_Structuration_DependencyRelationship, gen_RefOntoUML_MaterialAssociation_Association},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)