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
VariableQualification: Enumeration = Enumeration(
    name="VariableQualification",
    literals={
            EnumerationLiteral(name="Select"),
			EnumerationLiteral(name="Optional"),
			EnumerationLiteral(name="Assert"),
			EnumerationLiteral(name="Negate"),
			EnumerationLiteral(name="ExactlyOne"),
			EnumerationLiteral(name="ThereExists"),
			EnumerationLiteral(name="All")
    }
)

AssertionStrength: Enumeration = Enumeration(
    name="AssertionStrength",
    literals={
            EnumerationLiteral(name="Global"),
			EnumerationLiteral(name="Local")
    }
)

# Classes
smif_Repository = Class(name="smif::Repository")
LexicalScope = Class(name="LexicalScope")
smif_types_Type = Class(name="smif::types::Type", is_abstract=True)
lexicalscope_LexicalScope = Class(name="lexicalscope::LexicalScope")
toplevel_Context = Class(name="toplevel::Context")
Thing = Class(name="Thing")
PropertyType = Class(name="PropertyType")
PatternOfType = Class(name="PatternOfType")
CoveringConstraint = Class(name="CoveringConstraint")
GeneralizationConstraint = Class(name="GeneralizationConstraint")
MultiplicityConstraint = Class(name="MultiplicityConstraint")
PropertyTypeConstraint = Class(name="PropertyTypeConstraint")
RecordType = Class(name="RecordType")
ExpressionContext = Class(name="ExpressionContext")
smif_types_IntersectionType = Class(name="smif::types::IntersectionType")
Type = Class(name="Type")
smif_types_UnionType = Class(name="smif::types::UnionType")
smif_types_EntityType = Class(name="smif::types::EntityType")
smif_situations_SituationType = Class(name="smif::situations::SituationType")
EntityType = Class(name="EntityType")
smif_situations_Situation = Class(name="smif::situations::Situation", is_abstract=True)
toplevel_Proposition = Class(name="toplevel::Proposition")
toplevel_TemporalEntity = Class(name="toplevel::TemporalEntity")
PatternMatch = Class(name="PatternMatch")
smif_situations_ActualSituation = Class(name="smif::situations::ActualSituation")
toplevel_ActualEntity = Class(name="toplevel::ActualEntity")
situations_Situation = Class(name="situations::Situation")
smif_values_QuantityKind = Class(name="smif::values::QuantityKind")
ValueType = Class(name="ValueType")
smif_values_UnitType = Class(name="smif::values::UnitType")
Definition = Class(name="Definition")
SystemOfUnits = Class(name="SystemOfUnits")
smif_values_BaseUnitType = Class(name="smif::values::BaseUnitType")
UnitType = Class(name="UnitType")
smif_values_ValueType = Class(name="smif::values::ValueType")
smif_values_Value = Class(name="smif::values::Value")
smif_values_SystemOfUnits = Class(name="smif::values::SystemOfUnits")
Context = Class(name="Context")
smif_values_StructuredValueType = Class(name="smif::values::StructuredValueType")
values_ValueType = Class(name="values::ValueType")
properties_PropertyOwnerType = Class(name="properties::PropertyOwnerType")
smif_values_StructuredValue = Class(name="smif::values::StructuredValue")
values_Value = Class(name="values::Value")
properties_PropertyOwner = Class(name="properties::PropertyOwner")
MatchEnd = Class(name="MatchEnd")
RepresentationRule = Class(name="RepresentationRule")
smif_identifiers_UniqueIdentifier = Class(name="smif::identifiers::UniqueIdentifier", is_abstract=True)
Identifier = Class(name="Identifier")
Namespace = Class(name="Namespace")
smif_identifiers_IRIIdentifier = Class(name="smif::identifiers::IRIIdentifier")
TechnicalIdentifier = Class(name="TechnicalIdentifier")
smif_identifiers_Term = Class(name="smif::identifiers::Term")
identifiers_Name = Class(name="identifiers::Name")
identifiers_UniqueTextIdentifier = Class(name="identifiers::UniqueTextIdentifier")
smif_identifiers_UniqueTextIdentifier = Class(name="smif::identifiers::UniqueTextIdentifier")
identifiers_UniqueIdentifier = Class(name="identifiers::UniqueIdentifier")
identifiers_TextIdentifier = Class(name="identifiers::TextIdentifier")
smif_identifiers_Identifier = Class(name="smif::identifiers::Identifier")
IdentifiableEntity = Class(name="IdentifiableEntity")
smif_identifiers_Namespace = Class(name="smif::identifiers::Namespace")
UniqueIdentifier = Class(name="UniqueIdentifier")
smif_identifiers_TextIdentifier = Class(name="smif::identifiers::TextIdentifier")
smif_identifiers_Name = Class(name="smif::identifiers::Name")
TextIdentifier = Class(name="TextIdentifier")
smif_identifiers_TechnicalIdentifier = Class(name="smif::identifiers::TechnicalIdentifier")
UniqueTextIdentifier = Class(name="UniqueTextIdentifier")
smif_expressions_FunctionType = Class(name="smif::expressions::FunctionType")
expressions_ExpressionContext = Class(name="expressions::ExpressionContext")
ExpressionNode = Class(name="ExpressionNode")
FunctionCall = Class(name="FunctionCall")
smif_values_UnitValue = Class(name="smif::values::UnitValue", is_abstract=True)
Value = Class(name="Value")
smif_values_ScalarQuantity = Class(name="smif::values::ScalarQuantity", is_abstract=True)
UnitValue = Class(name="UnitValue")
Evaluation = Class(name="Evaluation")
FunctionType = Class(name="FunctionType")
smif_expressions_FunctionCall = Class(name="smif::expressions::FunctionCall")
expressions_ExpressionNode = Class(name="expressions::ExpressionNode")
smif_expressions_Traversal = Class(name="smif::expressions::Traversal")
smif_expressions_ObjectOperationType = Class(name="smif::expressions::ObjectOperationType")
smif_expressions_Equality = Class(name="smif::expressions::Equality")
smif_expressions_Evaluation = Class(name="smif::expressions::Evaluation")
smif_expressions_ExpressionContext = Class(name="smif::expressions::ExpressionContext", is_abstract=True)
smif_relationships_Relationship = Class(name="smif::relationships::Relationship")
situations_ActualSituation = Class(name="situations::ActualSituation")
smif_expressions_ConstantReference = Class(name="smif::expressions::ConstantReference")
smif_expressions_ExpressionNode = Class(name="smif::expressions::ExpressionNode", is_abstract=True)
smif_constraints_MultiplicityConstraint = Class(name="smif::constraints::MultiplicityConstraint")
TypeConstraint = Class(name="TypeConstraint")
smif_constraints_UniquenessConstraint = Class(name="smif::constraints::UniquenessConstraint")
smif_constraints_ConditionalRule = Class(name="smif::constraints::ConditionalRule")
constraints_Rule = Class(name="constraints::Rule")
constraints_Conditional = Class(name="constraints::Conditional")
smif_constraints_TypeConstraint = Class(name="smif::constraints::TypeConstraint", is_abstract=True)
smif_constraints_Equivalent = Class(name="smif::constraints::Equivalent")
smif_constraints_Disjoint = Class(name="smif::constraints::Disjoint")
smif_constraints_Enumerated = Class(name="smif::constraints::Enumerated")
smif_constraints_GeneralizationConstraint = Class(name="smif::constraints::GeneralizationConstraint")
smif_constraints_PropertyConstraint = Class(name="smif::constraints::PropertyConstraint", is_abstract=True)
smif_constraints_PropertyTransitivityConstraint = Class(name="smif::constraints::PropertyTransitivityConstraint")
PropertyConstraint = Class(name="PropertyConstraint")
smif_constraints_PropertyTypeConstraint = Class(name="smif::constraints::PropertyTypeConstraint")
smif_relationships_RelationshipType = Class(name="smif::relationships::RelationshipType")
situations_SituationType = Class(name="situations::SituationType")
smif_constraints_Rule = Class(name="smif::constraints::Rule", is_abstract=True)
Proposition = Class(name="Proposition")
Rule = Class(name="Rule")
smif_toplevel_IdentifiableEntity = Class(name="smif::toplevel::IdentifiableEntity")
Statement = Class(name="Statement")
Metadata = Class(name="Metadata")
Name = Class(name="Name")
Record = Class(name="Record")
InformationSource = Class(name="InformationSource")
PropertyBinding = Class(name="PropertyBinding")
smif_toplevel_Thing = Class(name="smif::toplevel::Thing", is_abstract=True)
ConstantReference = Class(name="ConstantReference")
smif_constraints_CoveringConstraint = Class(name="smif::constraints::CoveringConstraint")
smif_constraints_FacetClassificationConstraint = Class(name="smif::constraints::FacetClassificationConstraint")
smif_constraints_Conditional = Class(name="smif::constraints::Conditional", is_abstract=True)
smif_toplevel_Context = Class(name="smif::toplevel::Context", is_abstract=True)
LexicalReference = Class(name="LexicalReference")
smif_toplevel_Proposition = Class(name="smif::toplevel::Proposition", is_abstract=True)
PropositionVariable = Class(name="PropositionVariable")
smif_toplevel_ActualEntity = Class(name="smif::toplevel::ActualEntity")
TemporalEntity = Class(name="TemporalEntity")
smif_toplevel_TemporalEntity = Class(name="smif::toplevel::TemporalEntity", is_abstract=True)
smif_patterns_Pattern = Class(name="smif::patterns::Pattern")
PatternVariable = Class(name="PatternVariable")
smif_patterns_PatternVariable = Class(name="smif::patterns::PatternVariable")
properties_OwnedPropertyType = Class(name="properties::OwnedPropertyType")
Equality = Class(name="Equality")
Mapping = Class(name="Mapping")
smif_patterns_PropositionVariable = Class(name="smif::patterns::PropositionVariable")
smif_patterns_ExpressionVariable = Class(name="smif::patterns::ExpressionVariable")
patterns_PatternVariable = Class(name="patterns::PatternVariable")
patterns_Computed = Class(name="patterns::Computed")
smif_patterns_PartVariable = Class(name="smif::patterns::PartVariable")
TypePatternVariable = Class(name="TypePatternVariable")
smif_patterns_FocusVariable = Class(name="smif::patterns::FocusVariable")
smif_patterns_TypePatternVariable = Class(name="smif::patterns::TypePatternVariable", is_abstract=True)
smif_patterns_PatternOfType = Class(name="smif::patterns::PatternOfType")
smif_patterns_PatternMatch = Class(name="smif::patterns::PatternMatch")
ActualSituation = Class(name="ActualSituation")
VariableBinding = Class(name="VariableBinding")
Pattern = Class(name="Pattern")
smif_mapping_MatchRule = Class(name="smif::mapping::MatchRule")
smif_mapping_MatchEnd = Class(name="smif::mapping::MatchEnd")
MatchRule = Class(name="MatchRule")
smif_mapping_Mapping = Class(name="smif::mapping::Mapping")
patterns_Pattern = Class(name="patterns::Pattern")
smif_mapping_Facade = Class(name="smif::mapping::Facade")
smif_mapping_ComputedFacade = Class(name="smif::mapping::ComputedFacade", is_abstract=True)
Facade = Class(name="Facade")
Situation = Class(name="Situation")
smif_patterns_VariableBinding = Class(name="smif::patterns::VariableBinding")
OwnedPropertyBinding = Class(name="OwnedPropertyBinding")
smif_patterns_Computed = Class(name="smif::patterns::Computed", is_abstract=True)
smif_lexicalscope_Model = Class(name="smif::lexicalscope::Model")
Package = Class(name="Package")
smif_lexicalscope_LexicalScope = Class(name="smif::lexicalscope::LexicalScope")
smif_lexicalscope_LexicalReference = Class(name="smif::lexicalscope::LexicalReference")
smif_lexicalscope_Include = Class(name="smif::lexicalscope::Include")
smif_lexicalscope_Package = Class(name="smif::lexicalscope::Package")
Prefix = Class(name="Prefix")
smif_lexicalscope_MOFPackage = Class(name="smif::lexicalscope::MOFPackage")
smif_lexicalscope_LogicalPackage = Class(name="smif::lexicalscope::LogicalPackage")
smif_lexicalscope_PhysicalPackage = Class(name="smif::lexicalscope::PhysicalPackage")
smif_lexicalscope_MappingPackage = Class(name="smif::lexicalscope::MappingPackage")
smif_lexicalscope_Prefix = Class(name="smif::lexicalscope::Prefix")
smif_associations_AssociationType = Class(name="smif::associations::AssociationType")
PropertyOwnerType = Class(name="PropertyOwnerType")
smif_associations_Association = Class(name="smif::associations::Association")
smif_mapping_RepresentationRule = Class(name="smif::mapping::RepresentationRule")
ConditionalRule = Class(name="ConditionalRule")
smif_metadata_InformationSource = Class(name="smif::metadata::InformationSource")
metadata_Metadata = Class(name="metadata::Metadata")
smif_metadata_Metadata = Class(name="smif::metadata::Metadata")
smif_metadata_Definition = Class(name="smif::metadata::Definition")
IRIIdentifier = Class(name="IRIIdentifier")
Term = Class(name="Term")
smif_properties_PropertyBinding = Class(name="smif::properties::PropertyBinding", is_abstract=True)
smif_properties_PropertyType = Class(name="smif::properties::PropertyType", is_abstract=True)
smif_metadata_Statement = Class(name="smif::metadata::Statement")
smif_properties_CharacteristicType = Class(name="smif::properties::CharacteristicType")
properties_PropertyType = Class(name="properties::PropertyType")
smif_properties_CharacteristicBinding = Class(name="smif::properties::CharacteristicBinding")
properties_PropertyBinding = Class(name="properties::PropertyBinding")
smif_properties_AnnotationProperty = Class(name="smif::properties::AnnotationProperty")
CharacteristicType = Class(name="CharacteristicType")
smif_properties_OwnedPropertyType = Class(name="smif::properties::OwnedPropertyType")
smif_properties_PropertyOwnerType = Class(name="smif::properties::PropertyOwnerType", is_abstract=True)
smif_properties_OwnedPropertyBinding = Class(name="smif::properties::OwnedPropertyBinding")
smif_properties_PropertyOwner = Class(name="smif::properties::PropertyOwner", is_abstract=True)
smif_facets_FacetOfEntity = Class(name="smif::facets::FacetOfEntity")
Relationship = Class(name="Relationship")
smif_facets_Phase = Class(name="smif::facets::Phase")
facets_Facet = Class(name="facets::Facet")
smif_facets_Role = Class(name="smif::facets::Role")
Facet = Class(name="Facet")
smif_facets_Facet = Class(name="smif::facets::Facet")
smif_facets_Category = Class(name="smif::facets::Category")
smif_records_Record = Class(name="smif::records::Record")
smif_records_RecordType = Class(name="smif::records::RecordType")
Traversal = Class(name="Traversal")
ObjectOperationType = Class(name="ObjectOperationType")
UniquenessConstraint = Class(name="UniquenessConstraint")

# smif_Repository class attributes and methods

# LexicalScope class attributes and methods

# smif_types_Type class attributes and methods

# lexicalscope_LexicalScope class attributes and methods

# toplevel_Context class attributes and methods

# Thing class attributes and methods

# PropertyType class attributes and methods

# PatternOfType class attributes and methods

# CoveringConstraint class attributes and methods

# GeneralizationConstraint class attributes and methods

# MultiplicityConstraint class attributes and methods

# PropertyTypeConstraint class attributes and methods

# RecordType class attributes and methods

# ExpressionContext class attributes and methods

# smif_types_IntersectionType class attributes and methods

# Type class attributes and methods

# smif_types_UnionType class attributes and methods

# smif_types_EntityType class attributes and methods

# smif_situations_SituationType class attributes and methods

# EntityType class attributes and methods

# smif_situations_Situation class attributes and methods

# toplevel_Proposition class attributes and methods

# toplevel_TemporalEntity class attributes and methods

# PatternMatch class attributes and methods

# smif_situations_ActualSituation class attributes and methods

# toplevel_ActualEntity class attributes and methods

# situations_Situation class attributes and methods

# smif_values_QuantityKind class attributes and methods

# ValueType class attributes and methods

# smif_values_UnitType class attributes and methods
smif_values_UnitType_ratio: Property = Property(name="ratio", type=StringType)
smif_values_UnitType_offset: Property = Property(name="offset", type=StringType)
smif_values_UnitType_symbol: Property = Property(name="symbol", type=StringType)
smif_values_UnitType.attributes={smif_values_UnitType_offset, smif_values_UnitType_symbol, smif_values_UnitType_ratio}

# Definition class attributes and methods

# SystemOfUnits class attributes and methods

# smif_values_BaseUnitType class attributes and methods

# UnitType class attributes and methods

# smif_values_ValueType class attributes and methods

# smif_values_Value class attributes and methods

# smif_values_SystemOfUnits class attributes and methods

# Context class attributes and methods

# smif_values_StructuredValueType class attributes and methods

# values_ValueType class attributes and methods

# properties_PropertyOwnerType class attributes and methods

# smif_values_StructuredValue class attributes and methods

# values_Value class attributes and methods

# properties_PropertyOwner class attributes and methods

# MatchEnd class attributes and methods

# RepresentationRule class attributes and methods

# smif_identifiers_UniqueIdentifier class attributes and methods

# Identifier class attributes and methods

# Namespace class attributes and methods

# smif_identifiers_IRIIdentifier class attributes and methods

# TechnicalIdentifier class attributes and methods

# smif_identifiers_Term class attributes and methods

# identifiers_Name class attributes and methods

# identifiers_UniqueTextIdentifier class attributes and methods

# smif_identifiers_UniqueTextIdentifier class attributes and methods

# identifiers_UniqueIdentifier class attributes and methods

# identifiers_TextIdentifier class attributes and methods

# smif_identifiers_Identifier class attributes and methods

# IdentifiableEntity class attributes and methods

# smif_identifiers_Namespace class attributes and methods

# UniqueIdentifier class attributes and methods

# smif_identifiers_TextIdentifier class attributes and methods
smif_identifiers_TextIdentifier_value: Property = Property(name="value", type=StringType)
smif_identifiers_TextIdentifier.attributes={smif_identifiers_TextIdentifier_value}

# smif_identifiers_Name class attributes and methods

# TextIdentifier class attributes and methods

# smif_identifiers_TechnicalIdentifier class attributes and methods

# UniqueTextIdentifier class attributes and methods

# smif_expressions_FunctionType class attributes and methods

# expressions_ExpressionContext class attributes and methods

# ExpressionNode class attributes and methods

# FunctionCall class attributes and methods

# smif_values_UnitValue class attributes and methods
smif_values_UnitValue_hasValue: Property = Property(name="hasValue", type=StringType)
smif_values_UnitValue.attributes={smif_values_UnitValue_hasValue}

# Value class attributes and methods

# smif_values_ScalarQuantity class attributes and methods
smif_values_ScalarQuantity__unnamed_ScalarQuantity: Property = Property(name="_unnamed_ScalarQuantity", type=StringType)
smif_values_ScalarQuantity.attributes={smif_values_ScalarQuantity__unnamed_ScalarQuantity}

# UnitValue class attributes and methods

# Evaluation class attributes and methods

# FunctionType class attributes and methods

# smif_expressions_FunctionCall class attributes and methods

# expressions_ExpressionNode class attributes and methods

# smif_expressions_Traversal class attributes and methods
smif_expressions_Traversal_traverseToRelation: Property = Property(name="traverseToRelation", type=StringType)
smif_expressions_Traversal_inverse: Property = Property(name="inverse", type=StringType)
smif_expressions_Traversal.attributes={smif_expressions_Traversal_inverse, smif_expressions_Traversal_traverseToRelation}

# smif_expressions_ObjectOperationType class attributes and methods

# smif_expressions_Equality class attributes and methods

# smif_expressions_Evaluation class attributes and methods

# smif_expressions_ExpressionContext class attributes and methods

# smif_relationships_Relationship class attributes and methods

# situations_ActualSituation class attributes and methods

# smif_expressions_ConstantReference class attributes and methods

# smif_expressions_ExpressionNode class attributes and methods
smif_expressions_ExpressionNode_expressionText: Property = Property(name="expressionText", type=StringType)
smif_expressions_ExpressionNode_expressionTextLanguage: Property = Property(name="expressionTextLanguage", type=StringType)
smif_expressions_ExpressionNode.attributes={smif_expressions_ExpressionNode_expressionText, smif_expressions_ExpressionNode_expressionTextLanguage}

# smif_constraints_MultiplicityConstraint class attributes and methods
smif_constraints_MultiplicityConstraint_mininumNumber: Property = Property(name="mininumNumber", type=StringType)
smif_constraints_MultiplicityConstraint_maximumNumber: Property = Property(name="maximumNumber", type=StringType)
smif_constraints_MultiplicityConstraint_atOnce: Property = Property(name="atOnce", type=StringType)
smif_constraints_MultiplicityConstraint_isSufficent: Property = Property(name="isSufficent", type=StringType)
smif_constraints_MultiplicityConstraint.attributes={smif_constraints_MultiplicityConstraint_maximumNumber, smif_constraints_MultiplicityConstraint_mininumNumber, smif_constraints_MultiplicityConstraint_atOnce, smif_constraints_MultiplicityConstraint_isSufficent}

# TypeConstraint class attributes and methods

# smif_constraints_UniquenessConstraint class attributes and methods
smif_constraints_UniquenessConstraint_isPrimaryIdentity: Property = Property(name="isPrimaryIdentity", type=StringType)
smif_constraints_UniquenessConstraint.attributes={smif_constraints_UniquenessConstraint_isPrimaryIdentity}

# smif_constraints_ConditionalRule class attributes and methods

# constraints_Rule class attributes and methods

# constraints_Conditional class attributes and methods

# smif_constraints_TypeConstraint class attributes and methods

# smif_constraints_Equivalent class attributes and methods

# smif_constraints_Disjoint class attributes and methods

# smif_constraints_Enumerated class attributes and methods

# smif_constraints_GeneralizationConstraint class attributes and methods
smif_constraints_GeneralizationConstraint_redefines: Property = Property(name="redefines", type=StringType)
smif_constraints_GeneralizationConstraint.attributes={smif_constraints_GeneralizationConstraint_redefines}

# smif_constraints_PropertyConstraint class attributes and methods

# smif_constraints_PropertyTransitivityConstraint class attributes and methods

# PropertyConstraint class attributes and methods

# smif_constraints_PropertyTypeConstraint class attributes and methods
smif_constraints_PropertyTypeConstraint_prerequisiteType: Property = Property(name="prerequisiteType", type=StringType)
smif_constraints_PropertyTypeConstraint.attributes={smif_constraints_PropertyTypeConstraint_prerequisiteType}

# smif_relationships_RelationshipType class attributes and methods

# situations_SituationType class attributes and methods

# smif_constraints_Rule class attributes and methods

# Proposition class attributes and methods

# Rule class attributes and methods

# smif_toplevel_IdentifiableEntity class attributes and methods

# Statement class attributes and methods

# Metadata class attributes and methods

# Name class attributes and methods

# Record class attributes and methods

# InformationSource class attributes and methods

# PropertyBinding class attributes and methods

# smif_toplevel_Thing class attributes and methods

# ConstantReference class attributes and methods

# smif_constraints_CoveringConstraint class attributes and methods

# smif_constraints_FacetClassificationConstraint class attributes and methods

# smif_constraints_Conditional class attributes and methods

# smif_toplevel_Context class attributes and methods

# LexicalReference class attributes and methods

# smif_toplevel_Proposition class attributes and methods

# PropositionVariable class attributes and methods

# smif_toplevel_ActualEntity class attributes and methods

# TemporalEntity class attributes and methods

# smif_toplevel_TemporalEntity class attributes and methods

# smif_patterns_Pattern class attributes and methods

# PatternVariable class attributes and methods

# smif_patterns_PatternVariable class attributes and methods
smif_patterns_PatternVariable_qualification: Property = Property(name="qualification", type=StringType)
smif_patterns_PatternVariable_explicit: Property = Property(name="explicit", type=StringType)
smif_patterns_PatternVariable.attributes={smif_patterns_PatternVariable_qualification, smif_patterns_PatternVariable_explicit}

# properties_OwnedPropertyType class attributes and methods

# Equality class attributes and methods

# Mapping class attributes and methods

# smif_patterns_PropositionVariable class attributes and methods

# smif_patterns_ExpressionVariable class attributes and methods

# patterns_PatternVariable class attributes and methods

# patterns_Computed class attributes and methods

# smif_patterns_PartVariable class attributes and methods
smif_patterns_PartVariable_isBoundaryPart: Property = Property(name="isBoundaryPart", type=StringType)
smif_patterns_PartVariable.attributes={smif_patterns_PartVariable_isBoundaryPart}

# TypePatternVariable class attributes and methods

# smif_patterns_FocusVariable class attributes and methods

# smif_patterns_TypePatternVariable class attributes and methods

# smif_patterns_PatternOfType class attributes and methods

# smif_patterns_PatternMatch class attributes and methods

# ActualSituation class attributes and methods

# VariableBinding class attributes and methods

# Pattern class attributes and methods

# smif_mapping_MatchRule class attributes and methods
smif_mapping_MatchRule_coerce: Property = Property(name="coerce", type=StringType)
smif_mapping_MatchRule.attributes={smif_mapping_MatchRule_coerce}

# smif_mapping_MatchEnd class attributes and methods

# MatchRule class attributes and methods

# smif_mapping_Mapping class attributes and methods
smif_mapping_Mapping_strength: Property = Property(name="strength", type=StringType)
smif_mapping_Mapping.attributes={smif_mapping_Mapping_strength}

# patterns_Pattern class attributes and methods

# smif_mapping_Facade class attributes and methods

# smif_mapping_ComputedFacade class attributes and methods
smif_mapping_ComputedFacade_m_push: Method = Method(name="push", parameters={}, type=StringType)
smif_mapping_ComputedFacade_m_pull: Method = Method(name="pull", parameters={}, type=StringType)
smif_mapping_ComputedFacade.methods={smif_mapping_ComputedFacade_m_pull, smif_mapping_ComputedFacade_m_push}

# Facade class attributes and methods

# Situation class attributes and methods

# smif_patterns_VariableBinding class attributes and methods

# OwnedPropertyBinding class attributes and methods

# smif_patterns_Computed class attributes and methods

# smif_lexicalscope_Model class attributes and methods

# Package class attributes and methods

# smif_lexicalscope_LexicalScope class attributes and methods

# smif_lexicalscope_LexicalReference class attributes and methods

# smif_lexicalscope_Include class attributes and methods

# smif_lexicalscope_Package class attributes and methods

# Prefix class attributes and methods

# smif_lexicalscope_MOFPackage class attributes and methods

# smif_lexicalscope_LogicalPackage class attributes and methods

# smif_lexicalscope_PhysicalPackage class attributes and methods

# smif_lexicalscope_MappingPackage class attributes and methods

# smif_lexicalscope_Prefix class attributes and methods

# smif_associations_AssociationType class attributes and methods

# PropertyOwnerType class attributes and methods

# smif_associations_Association class attributes and methods

# smif_mapping_RepresentationRule class attributes and methods
smif_mapping_RepresentationRule_mapAll: Property = Property(name="mapAll", type=StringType)
smif_mapping_RepresentationRule.attributes={smif_mapping_RepresentationRule_mapAll}

# ConditionalRule class attributes and methods

# smif_metadata_InformationSource class attributes and methods

# metadata_Metadata class attributes and methods

# smif_metadata_Metadata class attributes and methods

# smif_metadata_Definition class attributes and methods
smif_metadata_Definition_textDefinition: Property = Property(name="textDefinition", type=StringType)
smif_metadata_Definition_summaryDescription: Property = Property(name="summaryDescription", type=StringType)
smif_metadata_Definition.attributes={smif_metadata_Definition_summaryDescription, smif_metadata_Definition_textDefinition}

# IRIIdentifier class attributes and methods

# Term class attributes and methods

# smif_properties_PropertyBinding class attributes and methods

# smif_properties_PropertyType class attributes and methods

# smif_metadata_Statement class attributes and methods

# smif_properties_CharacteristicType class attributes and methods

# properties_PropertyType class attributes and methods

# smif_properties_CharacteristicBinding class attributes and methods

# properties_PropertyBinding class attributes and methods

# smif_properties_AnnotationProperty class attributes and methods

# CharacteristicType class attributes and methods

# smif_properties_OwnedPropertyType class attributes and methods

# smif_properties_PropertyOwnerType class attributes and methods

# smif_properties_OwnedPropertyBinding class attributes and methods

# smif_properties_PropertyOwner class attributes and methods

# smif_facets_FacetOfEntity class attributes and methods

# Relationship class attributes and methods

# smif_facets_Phase class attributes and methods

# facets_Facet class attributes and methods

# smif_facets_Role class attributes and methods

# Facet class attributes and methods

# smif_facets_Facet class attributes and methods

# smif_facets_Category class attributes and methods

# smif_records_Record class attributes and methods

# smif_records_RecordType class attributes and methods

# Traversal class attributes and methods

# ObjectOperationType class attributes and methods

# UniquenessConstraint class attributes and methods

# Relationships
lexicalScope0: BinaryAssociation = BinaryAssociation(
    name="lexicalScope0",
    ends={
        Property(name="LexicalScope", type=smif_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="smif_Repository", type=LexicalScope, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
categorizes1: BinaryAssociation = BinaryAssociation(
    name="categorizes1",
    ends={
        Property(name="toplevel", type=smif_types_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="Thing", type=Thing, multiplicity=Multiplicity(0, 9999))
    }
)
hasProperty2: BinaryAssociation = BinaryAssociation(
    name="hasProperty2",
    ends={
        Property(name="properties", type=smif_types_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="PropertyType", type=PropertyType, multiplicity=Multiplicity(0, 9999))
    }
)
assertsPattern3: BinaryAssociation = BinaryAssociation(
    name="assertsPattern3",
    ends={
        Property(name="patterns", type=smif_types_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="PatternOfType", type=PatternOfType, multiplicity=Multiplicity(0, 9999))
    }
)
hasCovering4: BinaryAssociation = BinaryAssociation(
    name="hasCovering4",
    ends={
        Property(name="constraints", type=smif_types_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="CoveringConstraint", type=CoveringConstraint, multiplicity=Multiplicity(0, 9999))
    }
)
hasSpecialization5: BinaryAssociation = BinaryAssociation(
    name="hasSpecialization5",
    ends={
        Property(name="constraints6", type=smif_types_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="GeneralizationConstraint", type=GeneralizationConstraint, multiplicity=Multiplicity(0, 9999))
    }
)
hasMultiplicity7: BinaryAssociation = BinaryAssociation(
    name="hasMultiplicity7",
    ends={
        Property(name="constraints8", type=smif_types_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="MultiplicityConstraint", type=MultiplicityConstraint, multiplicity=Multiplicity(0, 9999))
    }
)
propertiesOfType9: BinaryAssociation = BinaryAssociation(
    name="propertiesOfType9",
    ends={
        Property(name="constraints10", type=smif_types_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="PropertyTypeConstraint", type=PropertyTypeConstraint, multiplicity=Multiplicity(0, 9999))
    }
)
recordingTypes11: BinaryAssociation = BinaryAssociation(
    name="recordingTypes11",
    ends={
        Property(name="records", type=smif_types_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="RecordType", type=RecordType, multiplicity=Multiplicity(0, 9999))
    }
)
hasGeneralization12: BinaryAssociation = BinaryAssociation(
    name="hasGeneralization12",
    ends={
        Property(name="constraints14", type=smif_types_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="GeneralizationConstraint13", type=GeneralizationConstraint, multiplicity=Multiplicity(0, 9999))
    }
)
returnedBy15: BinaryAssociation = BinaryAssociation(
    name="returnedBy15",
    ends={
        Property(name="expressions", type=smif_types_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="ExpressionContext", type=ExpressionContext, multiplicity=Multiplicity(0, 9999))
    }
)
matchedBy25: BinaryAssociation = BinaryAssociation(
    name="matchedBy25",
    ends={
        Property(name="patterns26", type=smif_situations_Situation, multiplicity=Multiplicity(1, 1)),
        Property(name="PatternMatch", type=PatternMatch, multiplicity=Multiplicity(0, 9999))
    }
)
unitReference27: BinaryAssociation = BinaryAssociation(
    name="unitReference27",
    ends={
        Property(name="Definition", type=smif_values_UnitType, multiplicity=Multiplicity(1, 1)),
        Property(name="smif_values_UnitType", type=Definition, multiplicity=Multiplicity(0, 1))
    }
)
definedWithinSystem28: BinaryAssociation = BinaryAssociation(
    name="definedWithinSystem28",
    ends={
        Property(name="values", type=smif_values_UnitType, multiplicity=Multiplicity(1, 1)),
        Property(name="SystemOfUnits", type=SystemOfUnits, multiplicity=Multiplicity(0, 1))
    }
)
unitOfSystem29: BinaryAssociation = BinaryAssociation(
    name="unitOfSystem29",
    ends={
        Property(name="values30", type=smif_values_SystemOfUnits, multiplicity=Multiplicity(1, 1)),
        Property(name="UnitType", type=UnitType, multiplicity=Multiplicity(0, 9999))
    }
)
respectOf16: BinaryAssociation = BinaryAssociation(
    name="respectOf16",
    ends={
        Property(name="constraints18", type=smif_types_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="MultiplicityConstraint17", type=MultiplicityConstraint, multiplicity=Multiplicity(0, 9999))
    }
)
assertedBy19: BinaryAssociation = BinaryAssociation(
    name="assertedBy19",
    ends={
        Property(name="mapping", type=smif_types_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="MatchEnd", type=MatchEnd, multiplicity=Multiplicity(0, 9999))
    }
)
conceptRule20: BinaryAssociation = BinaryAssociation(
    name="conceptRule20",
    ends={
        Property(name="mapping21", type=smif_types_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="RepresentationRule", type=RepresentationRule, multiplicity=Multiplicity(1, 1))
    }
)
representsRule22: BinaryAssociation = BinaryAssociation(
    name="representsRule22",
    ends={
        Property(name="mapping24", type=smif_types_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="RepresentationRule23", type=RepresentationRule, multiplicity=Multiplicity(1, 1))
    }
)
uniqueWithin31: BinaryAssociation = BinaryAssociation(
    name="uniqueWithin31",
    ends={
        Property(name="identifiers", type=smif_identifiers_UniqueIdentifier, multiplicity=Multiplicity(1, 1)),
        Property(name="Namespace", type=Namespace, multiplicity=Multiplicity(1, 1))
    }
)
identifies32: BinaryAssociation = BinaryAssociation(
    name="identifies32",
    ends={
        Property(name="toplevel33", type=smif_identifiers_Identifier, multiplicity=Multiplicity(1, 1)),
        Property(name="IdentifiableEntity", type=IdentifiableEntity, multiplicity=Multiplicity(1, 1))
    }
)
preferredFor34: BinaryAssociation = BinaryAssociation(
    name="preferredFor34",
    ends={
        Property(name="toplevel36", type=smif_identifiers_Identifier, multiplicity=Multiplicity(1, 1)),
        Property(name="IdentifiableEntity35", type=IdentifiableEntity, multiplicity=Multiplicity(0, 1))
    }
)
scopesIdentifier37: BinaryAssociation = BinaryAssociation(
    name="scopesIdentifier37",
    ends={
        Property(name="identifiers38", type=smif_identifiers_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="UniqueIdentifier", type=UniqueIdentifier, multiplicity=Multiplicity(0, 9999))
    }
)
names39: BinaryAssociation = BinaryAssociation(
    name="names39",
    ends={
        Property(name="toplevel41", type=smif_identifiers_Name, multiplicity=Multiplicity(1, 1)),
        Property(name="IdentifiableEntity40", type=IdentifiableEntity, multiplicity=Multiplicity(1, 9999))
    }
)
implementedBy42: BinaryAssociation = BinaryAssociation(
    name="implementedBy42",
    ends={
        Property(name="expressions43", type=smif_expressions_FunctionType, multiplicity=Multiplicity(1, 1)),
        Property(name="ExpressionNode", type=ExpressionNode, multiplicity=Multiplicity(0, 1))
    }
)
evaluatedBy49: BinaryAssociation = BinaryAssociation(
    name="evaluatedBy49",
    ends={
        Property(name="expressions50", type=smif_expressions_ExpressionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="Evaluation", type=Evaluation, multiplicity=Multiplicity(0, 9999))
    }
)
implements51: BinaryAssociation = BinaryAssociation(
    name="implements51",
    ends={
        Property(name="expressions52", type=smif_expressions_ExpressionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="FunctionType", type=FunctionType, multiplicity=Multiplicity(0, 1))
    }
)
calls53: BinaryAssociation = BinaryAssociation(
    name="calls53",
    ends={
        Property(name="expressions55", type=smif_expressions_FunctionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="FunctionType54", type=FunctionType, multiplicity=Multiplicity(1, 1))
    }
)
traversesThrough56: BinaryAssociation = BinaryAssociation(
    name="traversesThrough56",
    ends={
        Property(name="properties58", type=smif_expressions_Traversal, multiplicity=Multiplicity(1, 1)),
        Property(name="PropertyType57", type=PropertyType, multiplicity=Multiplicity(1, 9999))
    }
)
receiver59: BinaryAssociation = BinaryAssociation(
    name="receiver59",
    ends={
        Property(name="properties61", type=smif_expressions_ObjectOperationType, multiplicity=Multiplicity(1, 1)),
        Property(name="PropertyType60", type=PropertyType, multiplicity=Multiplicity(1, 1))
    }
)
hasEqual62: BinaryAssociation = BinaryAssociation(
    name="hasEqual62",
    ends={
        Property(name="toplevel64", type=smif_expressions_Equality, multiplicity=Multiplicity(1, 1)),
        Property(name="Thing63", type=Thing, multiplicity=Multiplicity(1, 9999))
    }
)
evaluates65: BinaryAssociation = BinaryAssociation(
    name="evaluates65",
    ends={
        Property(name="expressions67", type=smif_expressions_Evaluation, multiplicity=Multiplicity(1, 1)),
        Property(name="ExpressionNode66", type=ExpressionNode, multiplicity=Multiplicity(1, 1))
    }
)
evaluatesIn68: BinaryAssociation = BinaryAssociation(
    name="evaluatesIn68",
    ends={
        Property(name="toplevel69", type=smif_expressions_ExpressionContext, multiplicity=Multiplicity(1, 1)),
        Property(name="Context", type=Context, multiplicity=Multiplicity(0, 1))
    }
)
resultingType70: BinaryAssociation = BinaryAssociation(
    name="resultingType70",
    ends={
        Property(name="types", type=smif_expressions_ExpressionContext, multiplicity=Multiplicity(1, 1)),
        Property(name="Type", type=Type, multiplicity=Multiplicity(1, 9999))
    }
)
isUsedBy44: BinaryAssociation = BinaryAssociation(
    name="isUsedBy44",
    ends={
        Property(name="expressions45", type=smif_expressions_FunctionType, multiplicity=Multiplicity(1, 1)),
        Property(name="FunctionCall", type=FunctionCall, multiplicity=Multiplicity(0, 9999))
    }
)
hasValue46: BinaryAssociation = BinaryAssociation(
    name="hasValue46",
    ends={
        Property(name="toplevel48", type=smif_expressions_ConstantReference, multiplicity=Multiplicity(1, 1)),
        Property(name="Thing47", type=Thing, multiplicity=Multiplicity(1, 1))
    }
)
subsumedBy76: BinaryAssociation = BinaryAssociation(
    name="subsumedBy76",
    ends={
        Property(name="constraints78", type=smif_constraints_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="Rule77", type=Rule, multiplicity=Multiplicity(0, 9999))
    }
)
withRespectTo79: BinaryAssociation = BinaryAssociation(
    name="withRespectTo79",
    ends={
        Property(name="types81", type=smif_constraints_MultiplicityConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="Type80", type=Type, multiplicity=Multiplicity(0, 9999))
    }
)
multiplicityOf82: BinaryAssociation = BinaryAssociation(
    name="multiplicityOf82",
    ends={
        Property(name="types84", type=smif_constraints_MultiplicityConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="Type83", type=Type, multiplicity=Multiplicity(1, 1))
    }
)
hasUnique85: BinaryAssociation = BinaryAssociation(
    name="hasUnique85",
    ends={
        Property(name="properties87", type=smif_constraints_UniquenessConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="PropertyType86", type=PropertyType, multiplicity=Multiplicity(1, 9999))
    }
)
hasGeneral88: BinaryAssociation = BinaryAssociation(
    name="hasGeneral88",
    ends={
        Property(name="types90", type=smif_constraints_GeneralizationConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="Type89", type=Type, multiplicity=Multiplicity(1, 1))
    }
)
hasSpecific91: BinaryAssociation = BinaryAssociation(
    name="hasSpecific91",
    ends={
        Property(name="types93", type=smif_constraints_GeneralizationConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="Type92", type=Type, multiplicity=Multiplicity(1, 1))
    }
)
isOfType94: BinaryAssociation = BinaryAssociation(
    name="isOfType94",
    ends={
        Property(name="types96", type=smif_constraints_PropertyTypeConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="Type95", type=Type, multiplicity=Multiplicity(1, 1))
    }
)
constrains71: BinaryAssociation = BinaryAssociation(
    name="constrains71",
    ends={
        Property(name="toplevel73", type=smif_constraints_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="IdentifiableEntity72", type=IdentifiableEntity, multiplicity=Multiplicity(0, 9999))
    }
)
subsumes74: BinaryAssociation = BinaryAssociation(
    name="subsumes74",
    ends={
        Property(name="constraints75", type=smif_constraints_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="Rule", type=Rule, multiplicity=Multiplicity(0, 9999))
    }
)
wasStatedIn102: BinaryAssociation = BinaryAssociation(
    name="wasStatedIn102",
    ends={
        Property(name="metadata", type=smif_toplevel_IdentifiableEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="Statement", type=Statement, multiplicity=Multiplicity(0, 9999))
    }
)
hasPreferred103: BinaryAssociation = BinaryAssociation(
    name="hasPreferred103",
    ends={
        Property(name="identifiers104", type=smif_toplevel_IdentifiableEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="Identifier", type=Identifier, multiplicity=Multiplicity(0, 1))
    }
)
definedBy105: BinaryAssociation = BinaryAssociation(
    name="definedBy105",
    ends={
        Property(name="metadata107", type=smif_toplevel_IdentifiableEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="Definition106", type=Definition, multiplicity=Multiplicity(0, 9999))
    }
)
identifiedBy108: BinaryAssociation = BinaryAssociation(
    name="identifiedBy108",
    ends={
        Property(name="identifiers110", type=smif_toplevel_IdentifiableEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="Identifier109", type=Identifier, multiplicity=Multiplicity(0, 9999))
    }
)
hasMetadata111: BinaryAssociation = BinaryAssociation(
    name="hasMetadata111",
    ends={
        Property(name="metadata112", type=smif_toplevel_IdentifiableEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="Metadata", type=Metadata, multiplicity=Multiplicity(0, 9999))
    }
)
hasName113: BinaryAssociation = BinaryAssociation(
    name="hasName113",
    ends={
        Property(name="identifiers114", type=smif_toplevel_IdentifiableEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="Name", type=Name, multiplicity=Multiplicity(0, 9999))
    }
)
hasRecord115: BinaryAssociation = BinaryAssociation(
    name="hasRecord115",
    ends={
        Property(name="records116", type=smif_toplevel_IdentifiableEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="Record", type=Record, multiplicity=Multiplicity(0, 9999))
    }
)
constrainedBy117: BinaryAssociation = BinaryAssociation(
    name="constrainedBy117",
    ends={
        Property(name="constraints119", type=smif_toplevel_IdentifiableEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="Rule118", type=Rule, multiplicity=Multiplicity(0, 9999))
    }
)
hasAuthoritativeSource120: BinaryAssociation = BinaryAssociation(
    name="hasAuthoritativeSource120",
    ends={
        Property(name="metadata121", type=smif_toplevel_IdentifiableEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="InformationSource", type=InformationSource, multiplicity=Multiplicity(0, 9999))
    }
)
hasBinding122: BinaryAssociation = BinaryAssociation(
    name="hasBinding122",
    ends={
        Property(name="properties123", type=smif_toplevel_IdentifiableEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="PropertyBinding", type=PropertyBinding, multiplicity=Multiplicity(0, 9999))
    }
)
definedIn124: BinaryAssociation = BinaryAssociation(
    name="definedIn124",
    ends={
        Property(name="LexicalScope125", type=smif_toplevel_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="smif_toplevel_Thing", type=LexicalScope, multiplicity=Multiplicity(1, 1))
    }
)
inContextOf126: BinaryAssociation = BinaryAssociation(
    name="inContextOf126",
    ends={
        Property(name="toplevel128", type=smif_toplevel_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="Context127", type=Context, multiplicity=Multiplicity(1, 9999))
    }
)
hasType129: BinaryAssociation = BinaryAssociation(
    name="hasType129",
    ends={
        Property(name="types131", type=smif_toplevel_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="Type130", type=Type, multiplicity=Multiplicity(1, 9999))
    }
)
statedBy132: BinaryAssociation = BinaryAssociation(
    name="statedBy132",
    ends={
        Property(name="lexicalscope", type=smif_toplevel_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="LexicalScope133", type=LexicalScope, multiplicity=Multiplicity(0, 1))
    }
)
referencedBy134: BinaryAssociation = BinaryAssociation(
    name="referencedBy134",
    ends={
        Property(name="expressions135", type=smif_toplevel_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="ConstantReference", type=ConstantReference, multiplicity=Multiplicity(0, 9999))
    }
)
isCoveredBy97: BinaryAssociation = BinaryAssociation(
    name="isCoveredBy97",
    ends={
        Property(name="types99", type=smif_constraints_CoveringConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="Type98", type=Type, multiplicity=Multiplicity(0, 9999))
    }
)
condition100: BinaryAssociation = BinaryAssociation(
    name="condition100",
    ends={
        Property(name="ExpressionNode101", type=smif_constraints_Conditional, multiplicity=Multiplicity(1, 1)),
        Property(name="smif_constraints_Conditional", type=ExpressionNode, multiplicity=Multiplicity(0, 1))
    }
)
asserts141: BinaryAssociation = BinaryAssociation(
    name="asserts141",
    ends={
        Property(name="toplevel142", type=smif_toplevel_Context, multiplicity=Multiplicity(1, 1)),
        Property(name="Proposition", type=Proposition, multiplicity=Multiplicity(0, 9999))
    }
)
contextualizes143: BinaryAssociation = BinaryAssociation(
    name="contextualizes143",
    ends={
        Property(name="toplevel145", type=smif_toplevel_Context, multiplicity=Multiplicity(1, 1)),
        Property(name="Thing144", type=Thing, multiplicity=Multiplicity(0, 9999))
    }
)
negates146: BinaryAssociation = BinaryAssociation(
    name="negates146",
    ends={
        Property(name="toplevel148", type=smif_toplevel_Context, multiplicity=Multiplicity(1, 1)),
        Property(name="Proposition147", type=Proposition, multiplicity=Multiplicity(0, 9999))
    }
)
contextualizesExpress149: BinaryAssociation = BinaryAssociation(
    name="contextualizesExpress149",
    ends={
        Property(name="expressions151", type=smif_toplevel_Context, multiplicity=Multiplicity(1, 1)),
        Property(name="ExpressionContext150", type=ExpressionContext, multiplicity=Multiplicity(0, 9999))
    }
)
referencedByLR152: BinaryAssociation = BinaryAssociation(
    name="referencedByLR152",
    ends={
        Property(name="lexicalscope153", type=smif_toplevel_Context, multiplicity=Multiplicity(1, 1)),
        Property(name="LexicalReference", type=LexicalReference, multiplicity=Multiplicity(0, 9999))
    }
)
holdsWithin154: BinaryAssociation = BinaryAssociation(
    name="holdsWithin154",
    ends={
        Property(name="toplevel156", type=smif_toplevel_Proposition, multiplicity=Multiplicity(1, 1)),
        Property(name="Context155", type=Context, multiplicity=Multiplicity(0, 9999))
    }
)
negatedWithin157: BinaryAssociation = BinaryAssociation(
    name="negatedWithin157",
    ends={
        Property(name="toplevel159", type=smif_toplevel_Proposition, multiplicity=Multiplicity(1, 1)),
        Property(name="Context158", type=Context, multiplicity=Multiplicity(0, 9999))
    }
)
qualifiedWithin160: BinaryAssociation = BinaryAssociation(
    name="qualifiedWithin160",
    ends={
        Property(name="patterns161", type=smif_toplevel_Proposition, multiplicity=Multiplicity(1, 1)),
        Property(name="PropositionVariable", type=PropositionVariable, multiplicity=Multiplicity(0, 1))
    }
)
ownsVariable162: BinaryAssociation = BinaryAssociation(
    name="ownsVariable162",
    ends={
        Property(name="patterns163", type=smif_patterns_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="PatternVariable", type=PatternVariable, multiplicity=Multiplicity(0, 9999))
    }
)
satisfiedBy164: BinaryAssociation = BinaryAssociation(
    name="satisfiedBy164",
    ends={
        Property(name="patterns166", type=smif_patterns_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="PatternMatch165", type=PatternMatch, multiplicity=Multiplicity(0, 9999))
    }
)
hasEquality136: BinaryAssociation = BinaryAssociation(
    name="hasEquality136",
    ends={
        Property(name="expressions137", type=smif_toplevel_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="Equality", type=Equality, multiplicity=Multiplicity(0, 9999))
    }
)
boundIn138: BinaryAssociation = BinaryAssociation(
    name="boundIn138",
    ends={
        Property(name="properties140", type=smif_toplevel_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="PropertyBinding139", type=PropertyBinding, multiplicity=Multiplicity(0, 9999))
    }
)
subsets175: BinaryAssociation = BinaryAssociation(
    name="subsets175",
    ends={
        Property(name="patterns177", type=smif_patterns_PatternVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="PatternVariable176", type=PatternVariable, multiplicity=Multiplicity(0, 9999))
    }
)
excludedBy178: BinaryAssociation = BinaryAssociation(
    name="excludedBy178",
    ends={
        Property(name="patterns180", type=smif_patterns_PatternVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="PatternVariable179", type=PatternVariable, multiplicity=Multiplicity(0, 9999))
    }
)
excludes181: BinaryAssociation = BinaryAssociation(
    name="excludes181",
    ends={
        Property(name="patterns183", type=smif_patterns_PatternVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="PatternVariable182", type=PatternVariable, multiplicity=Multiplicity(0, 9999))
    }
)
referenceMapping184: BinaryAssociation = BinaryAssociation(
    name="referenceMapping184",
    ends={
        Property(name="mapping185", type=smif_patterns_PatternVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="Mapping", type=Mapping, multiplicity=Multiplicity(0, 1))
    }
)
concreteMapping186: BinaryAssociation = BinaryAssociation(
    name="concreteMapping186",
    ends={
        Property(name="mapping188", type=smif_patterns_PatternVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="Mapping187", type=Mapping, multiplicity=Multiplicity(0, 1))
    }
)
qualifies189: BinaryAssociation = BinaryAssociation(
    name="qualifies189",
    ends={
        Property(name="toplevel191", type=smif_patterns_PropositionVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="Proposition190", type=Proposition, multiplicity=Multiplicity(1, 1))
    }
)
subjectType192: BinaryAssociation = BinaryAssociation(
    name="subjectType192",
    ends={
        Property(name="types194", type=smif_patterns_PatternOfType, multiplicity=Multiplicity(1, 1)),
        Property(name="Type193", type=Type, multiplicity=Multiplicity(1, 1))
    }
)
_unnamed_PatternMatch195: BinaryAssociation = BinaryAssociation(
    name="_unnamed_PatternMatch195",
    ends={
        Property(name="patterns196", type=smif_patterns_PatternMatch, multiplicity=Multiplicity(1, 1)),
        Property(name="VariableBinding", type=VariableBinding, multiplicity=Multiplicity(0, 9999))
    }
)
satisfies197: BinaryAssociation = BinaryAssociation(
    name="satisfies197",
    ends={
        Property(name="patterns199", type=smif_patterns_PatternMatch, multiplicity=Multiplicity(1, 1)),
        Property(name="Pattern198", type=Pattern, multiplicity=Multiplicity(1, 1))
    }
)
hasOwningPattern167: BinaryAssociation = BinaryAssociation(
    name="hasOwningPattern167",
    ends={
        Property(name="patterns168", type=smif_patterns_PatternVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="Pattern", type=Pattern, multiplicity=Multiplicity(1, 1))
    }
)
hasSubset169: BinaryAssociation = BinaryAssociation(
    name="hasSubset169",
    ends={
        Property(name="patterns171", type=smif_patterns_PatternVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="PatternVariable170", type=PatternVariable, multiplicity=Multiplicity(0, 9999))
    }
)
mapsTo172: BinaryAssociation = BinaryAssociation(
    name="mapsTo172",
    ends={
        Property(name="mapping174", type=smif_patterns_PatternVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="MatchEnd173", type=MatchEnd, multiplicity=Multiplicity(0, 9999))
    }
)
concreteEnd206: BinaryAssociation = BinaryAssociation(
    name="concreteEnd206",
    ends={
        Property(name="mapping208", type=smif_mapping_MatchRule, multiplicity=Multiplicity(1, 1)),
        Property(name="MatchEnd207", type=MatchEnd, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
referenceEnd209: BinaryAssociation = BinaryAssociation(
    name="referenceEnd209",
    ends={
        Property(name="mapping211", type=smif_mapping_MatchRule, multiplicity=Multiplicity(1, 1)),
        Property(name="MatchEnd210", type=MatchEnd, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
mapRuleOf212: BinaryAssociation = BinaryAssociation(
    name="mapRuleOf212",
    ends={
        Property(name="mapping214", type=smif_mapping_MatchRule, multiplicity=Multiplicity(1, 1)),
        Property(name="Mapping213", type=Mapping, multiplicity=Multiplicity(1, 1))
    }
)
assertedType215: BinaryAssociation = BinaryAssociation(
    name="assertedType215",
    ends={
        Property(name="types217", type=smif_mapping_MatchEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="Type216", type=Type, multiplicity=Multiplicity(0, 9999))
    }
)
mapsVariable218: BinaryAssociation = BinaryAssociation(
    name="mapsVariable218",
    ends={
        Property(name="patterns220", type=smif_mapping_MatchEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="PatternVariable219", type=PatternVariable, multiplicity=Multiplicity(1, 1))
    }
)
matchFrom221: BinaryAssociation = BinaryAssociation(
    name="matchFrom221",
    ends={
        Property(name="mapping222", type=smif_mapping_MatchEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="MatchRule", type=MatchRule, multiplicity=Multiplicity(0, 1))
    }
)
matchTo223: BinaryAssociation = BinaryAssociation(
    name="matchTo223",
    ends={
        Property(name="mapping225", type=smif_mapping_MatchEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="MatchRule224", type=MatchRule, multiplicity=Multiplicity(0, 1))
    }
)
concreteFocus226: BinaryAssociation = BinaryAssociation(
    name="concreteFocus226",
    ends={
        Property(name="patterns228", type=smif_mapping_Mapping, multiplicity=Multiplicity(1, 1)),
        Property(name="PatternVariable227", type=PatternVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
hasMapRule229: BinaryAssociation = BinaryAssociation(
    name="hasMapRule229",
    ends={
        Property(name="mapping231", type=smif_mapping_Mapping, multiplicity=Multiplicity(1, 1)),
        Property(name="MatchRule230", type=MatchRule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referenceFocus232: BinaryAssociation = BinaryAssociation(
    name="referenceFocus232",
    ends={
        Property(name="patterns234", type=smif_mapping_Mapping, multiplicity=Multiplicity(1, 1)),
        Property(name="PatternVariable233", type=PatternVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
matches200: BinaryAssociation = BinaryAssociation(
    name="matches200",
    ends={
        Property(name="situations", type=smif_patterns_PatternMatch, multiplicity=Multiplicity(1, 1)),
        Property(name="Situation", type=Situation, multiplicity=Multiplicity(1, 1))
    }
)
_unnamed_VariableBinding201: BinaryAssociation = BinaryAssociation(
    name="_unnamed_VariableBinding201",
    ends={
        Property(name="patterns203", type=smif_patterns_VariableBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="PatternMatch202", type=PatternMatch, multiplicity=Multiplicity(1, 1))
    }
)
computation204: BinaryAssociation = BinaryAssociation(
    name="computation204",
    ends={
        Property(name="ExpressionNode205", type=smif_patterns_Computed, multiplicity=Multiplicity(1, 1)),
        Property(name="smif_patterns_Computed", type=ExpressionNode, multiplicity=Multiplicity(0, 1))
    }
)
defines241: BinaryAssociation = BinaryAssociation(
    name="defines241",
    ends={
        Property(name="Thing242", type=smif_lexicalscope_LexicalScope, multiplicity=Multiplicity(1, 1)),
        Property(name="smif_lexicalscope_LexicalScope", type=Thing, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
references243: BinaryAssociation = BinaryAssociation(
    name="references243",
    ends={
        Property(name="lexicalscope245", type=smif_lexicalscope_LexicalScope, multiplicity=Multiplicity(1, 1)),
        Property(name="LexicalReference244", type=LexicalReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
states246: BinaryAssociation = BinaryAssociation(
    name="states246",
    ends={
        Property(name="toplevel248", type=smif_lexicalscope_LexicalScope, multiplicity=Multiplicity(1, 1)),
        Property(name="Thing247", type=Thing, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referencedScope249: BinaryAssociation = BinaryAssociation(
    name="referencedScope249",
    ends={
        Property(name="toplevel251", type=smif_lexicalscope_LexicalReference, multiplicity=Multiplicity(1, 1)),
        Property(name="Context250", type=Context, multiplicity=Multiplicity(1, 1))
    }
)
extendsScope252: BinaryAssociation = BinaryAssociation(
    name="extendsScope252",
    ends={
        Property(name="lexicalscope254", type=smif_lexicalscope_LexicalReference, multiplicity=Multiplicity(1, 1)),
        Property(name="LexicalScope253", type=LexicalScope, multiplicity=Multiplicity(1, 1))
    }
)
hasPrefix255: BinaryAssociation = BinaryAssociation(
    name="hasPrefix255",
    ends={
        Property(name="lexicalscope256", type=smif_lexicalscope_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="Prefix", type=Prefix, multiplicity=Multiplicity(0, 1))
    }
)
prefixOf257: BinaryAssociation = BinaryAssociation(
    name="prefixOf257",
    ends={
        Property(name="lexicalscope258", type=smif_lexicalscope_Prefix, multiplicity=Multiplicity(1, 1)),
        Property(name="Package", type=Package, multiplicity=Multiplicity(1, 1))
    }
)
representedBy235: BinaryAssociation = BinaryAssociation(
    name="representedBy235",
    ends={
        Property(name="types237", type=smif_mapping_RepresentationRule, multiplicity=Multiplicity(1, 1)),
        Property(name="Type236", type=Type, multiplicity=Multiplicity(1, 1))
    }
)
representedType238: BinaryAssociation = BinaryAssociation(
    name="representedType238",
    ends={
        Property(name="types240", type=smif_mapping_RepresentationRule, multiplicity=Multiplicity(1, 1)),
        Property(name="Type239", type=Type, multiplicity=Multiplicity(1, 9999))
    }
)
resultedIn266: BinaryAssociation = BinaryAssociation(
    name="resultedIn266",
    ends={
        Property(name="toplevel268", type=smif_metadata_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="IdentifiableEntity267", type=IdentifiableEntity, multiplicity=Multiplicity(1, 1))
    }
)
madeStatement269: BinaryAssociation = BinaryAssociation(
    name="madeStatement269",
    ends={
        Property(name="toplevel271", type=smif_metadata_InformationSource, multiplicity=Multiplicity(1, 1)),
        Property(name="IdentifiableEntity270", type=IdentifiableEntity, multiplicity=Multiplicity(1, 9999))
    }
)
metadataAbout272: BinaryAssociation = BinaryAssociation(
    name="metadataAbout272",
    ends={
        Property(name="toplevel274", type=smif_metadata_Metadata, multiplicity=Multiplicity(1, 1)),
        Property(name="IdentifiableEntity273", type=IdentifiableEntity, multiplicity=Multiplicity(0, 9999))
    }
)
externalReference275: BinaryAssociation = BinaryAssociation(
    name="externalReference275",
    ends={
        Property(name="IRIIdentifier", type=smif_metadata_Definition, multiplicity=Multiplicity(1, 1)),
        Property(name="smif_metadata_Definition", type=IRIIdentifier, multiplicity=Multiplicity(1, 1))
    }
)
externalTerm276: BinaryAssociation = BinaryAssociation(
    name="externalTerm276",
    ends={
        Property(name="Term", type=smif_metadata_Definition, multiplicity=Multiplicity(1, 1)),
        Property(name="smif_metadata_Definition277", type=Term, multiplicity=Multiplicity(1, 1))
    }
)
definesEntity278: BinaryAssociation = BinaryAssociation(
    name="definesEntity278",
    ends={
        Property(name="toplevel280", type=smif_metadata_Definition, multiplicity=Multiplicity(1, 1)),
        Property(name="IdentifiableEntity279", type=IdentifiableEntity, multiplicity=Multiplicity(1, 1))
    }
)
binds281: BinaryAssociation = BinaryAssociation(
    name="binds281",
    ends={
        Property(name="toplevel283", type=smif_properties_PropertyBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="Thing282", type=Thing, multiplicity=Multiplicity(1, 1))
    }
)
boundBy284: BinaryAssociation = BinaryAssociation(
    name="boundBy284",
    ends={
        Property(name="properties286", type=smif_properties_PropertyBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="PropertyType285", type=PropertyType, multiplicity=Multiplicity(1, 1))
    }
)
boundTo287: BinaryAssociation = BinaryAssociation(
    name="boundTo287",
    ends={
        Property(name="toplevel289", type=smif_properties_PropertyBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="IdentifiableEntity288", type=IdentifiableEntity, multiplicity=Multiplicity(1, 1))
    }
)
statementDateAndTime259: BinaryAssociation = BinaryAssociation(
    name="statementDateAndTime259",
    ends={
        Property(name="ValueType", type=smif_metadata_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="smif_metadata_Statement", type=ValueType, multiplicity=Multiplicity(1, 1))
    }
)
version260: BinaryAssociation = BinaryAssociation(
    name="version260",
    ends={
        Property(name="ValueType262", type=smif_metadata_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="smif_metadata_Statement261", type=ValueType, multiplicity=Multiplicity(1, 1))
    }
)
transactionId263: BinaryAssociation = BinaryAssociation(
    name="transactionId263",
    ends={
        Property(name="ValueType265", type=smif_metadata_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="smif_metadata_Statement264", type=ValueType, multiplicity=Multiplicity(1, 1))
    }
)
hasBindingProperty299: BinaryAssociation = BinaryAssociation(
    name="hasBindingProperty299",
    ends={
        Property(name="properties301", type=smif_properties_PropertyType, multiplicity=Multiplicity(1, 1)),
        Property(name="PropertyBinding300", type=PropertyBinding, multiplicity=Multiplicity(0, 9999))
    }
)
about302: BinaryAssociation = BinaryAssociation(
    name="about302",
    ends={
        Property(name="toplevel304", type=smif_records_Record, multiplicity=Multiplicity(1, 1)),
        Property(name="IdentifiableEntity303", type=IdentifiableEntity, multiplicity=Multiplicity(0, 9999))
    }
)
aboutType305: BinaryAssociation = BinaryAssociation(
    name="aboutType305",
    ends={
        Property(name="types307", type=smif_records_RecordType, multiplicity=Multiplicity(1, 1)),
        Property(name="Type306", type=Type, multiplicity=Multiplicity(0, 1))
    }
)
propertyOf290: BinaryAssociation = BinaryAssociation(
    name="propertyOf290",
    ends={
        Property(name="types292", type=smif_properties_PropertyType, multiplicity=Multiplicity(1, 1)),
        Property(name="Type291", type=Type, multiplicity=Multiplicity(0, 1))
    }
)
traversedBy293: BinaryAssociation = BinaryAssociation(
    name="traversedBy293",
    ends={
        Property(name="expressions294", type=smif_properties_PropertyType, multiplicity=Multiplicity(1, 1)),
        Property(name="Traversal", type=Traversal, multiplicity=Multiplicity(0, 9999))
    }
)
receivedBy295: BinaryAssociation = BinaryAssociation(
    name="receivedBy295",
    ends={
        Property(name="expressions296", type=smif_properties_PropertyType, multiplicity=Multiplicity(1, 1)),
        Property(name="ObjectOperationType", type=ObjectOperationType, multiplicity=Multiplicity(0, 9999))
    }
)
hasUniquenessConstraint297: BinaryAssociation = BinaryAssociation(
    name="hasUniquenessConstraint297",
    ends={
        Property(name="constraints298", type=smif_properties_PropertyType, multiplicity=Multiplicity(1, 1)),
        Property(name="UniquenessConstraint", type=UniquenessConstraint, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_smif_types_Type_lexicalscope_LexicalScope = Generalization(general=lexicalscope_LexicalScope, specific=smif_types_Type)
gen_smif_types_Type_toplevel_Context = Generalization(general=toplevel_Context, specific=smif_types_Type)
gen_smif_types_IntersectionType_Type = Generalization(general=Type, specific=smif_types_IntersectionType)
gen_smif_types_UnionType_Type = Generalization(general=Type, specific=smif_types_UnionType)
gen_smif_types_EntityType_Type = Generalization(general=Type, specific=smif_types_EntityType)
gen_smif_situations_SituationType_EntityType = Generalization(general=EntityType, specific=smif_situations_SituationType)
gen_smif_situations_Situation_toplevel_Proposition = Generalization(general=toplevel_Proposition, specific=smif_situations_Situation)
gen_smif_situations_Situation_toplevel_TemporalEntity = Generalization(general=toplevel_TemporalEntity, specific=smif_situations_Situation)
gen_smif_situations_Situation_toplevel_Context = Generalization(general=toplevel_Context, specific=smif_situations_Situation)
gen_smif_situations_Situation_lexicalscope_LexicalScope = Generalization(general=lexicalscope_LexicalScope, specific=smif_situations_Situation)
gen_smif_situations_ActualSituation_toplevel_ActualEntity = Generalization(general=toplevel_ActualEntity, specific=smif_situations_ActualSituation)
gen_smif_situations_ActualSituation_situations_Situation = Generalization(general=situations_Situation, specific=smif_situations_ActualSituation)
gen_smif_values_QuantityKind_ValueType = Generalization(general=ValueType, specific=smif_values_QuantityKind)
gen_smif_values_UnitType_ValueType = Generalization(general=ValueType, specific=smif_values_UnitType)
gen_smif_values_BaseUnitType_UnitType = Generalization(general=UnitType, specific=smif_values_BaseUnitType)
gen_smif_values_ValueType_Type = Generalization(general=Type, specific=smif_values_ValueType)
gen_smif_values_Value_Thing = Generalization(general=Thing, specific=smif_values_Value)
gen_smif_values_SystemOfUnits_Context = Generalization(general=Context, specific=smif_values_SystemOfUnits)
gen_smif_values_StructuredValueType_values_ValueType = Generalization(general=values_ValueType, specific=smif_values_StructuredValueType)
gen_smif_values_StructuredValueType_properties_PropertyOwnerType = Generalization(general=properties_PropertyOwnerType, specific=smif_values_StructuredValueType)
gen_smif_values_StructuredValue_values_Value = Generalization(general=values_Value, specific=smif_values_StructuredValue)
gen_smif_identifiers_UniqueIdentifier_Identifier = Generalization(general=Identifier, specific=smif_identifiers_UniqueIdentifier)
gen_smif_identifiers_IRIIdentifier_TechnicalIdentifier = Generalization(general=TechnicalIdentifier, specific=smif_identifiers_IRIIdentifier)
gen_smif_identifiers_Term_identifiers_Name = Generalization(general=identifiers_Name, specific=smif_identifiers_Term)
gen_smif_identifiers_Term_identifiers_UniqueTextIdentifier = Generalization(general=identifiers_UniqueTextIdentifier, specific=smif_identifiers_Term)
gen_smif_identifiers_UniqueTextIdentifier_identifiers_UniqueIdentifier = Generalization(general=identifiers_UniqueIdentifier, specific=smif_identifiers_UniqueTextIdentifier)
gen_smif_identifiers_UniqueTextIdentifier_identifiers_TextIdentifier = Generalization(general=identifiers_TextIdentifier, specific=smif_identifiers_UniqueTextIdentifier)
gen_smif_identifiers_Identifier_Value = Generalization(general=Value, specific=smif_identifiers_Identifier)
gen_smif_identifiers_Namespace_Context = Generalization(general=Context, specific=smif_identifiers_Namespace)
gen_smif_identifiers_TextIdentifier_Identifier = Generalization(general=Identifier, specific=smif_identifiers_TextIdentifier)
gen_smif_identifiers_Name_TextIdentifier = Generalization(general=TextIdentifier, specific=smif_identifiers_Name)
gen_smif_identifiers_TechnicalIdentifier_UniqueTextIdentifier = Generalization(general=UniqueTextIdentifier, specific=smif_identifiers_TechnicalIdentifier)
gen_smif_expressions_FunctionType_properties_PropertyOwnerType = Generalization(general=properties_PropertyOwnerType, specific=smif_expressions_FunctionType)
gen_smif_expressions_FunctionType_expressions_ExpressionContext = Generalization(general=expressions_ExpressionContext, specific=smif_expressions_FunctionType)
gen_smif_values_StructuredValue_properties_PropertyOwner = Generalization(general=properties_PropertyOwner, specific=smif_values_StructuredValue)
gen_smif_values_UnitValue_Value = Generalization(general=Value, specific=smif_values_UnitValue)
gen_smif_values_ScalarQuantity_UnitValue = Generalization(general=UnitValue, specific=smif_values_ScalarQuantity)
gen_smif_expressions_FunctionCall_expressions_ExpressionNode = Generalization(general=expressions_ExpressionNode, specific=smif_expressions_FunctionCall)
gen_smif_expressions_FunctionCall_properties_PropertyOwner = Generalization(general=properties_PropertyOwner, specific=smif_expressions_FunctionCall)
gen_smif_expressions_Traversal_expressions_ExpressionNode = Generalization(general=expressions_ExpressionNode, specific=smif_expressions_Traversal)
gen_smif_expressions_Traversal_properties_PropertyOwner = Generalization(general=properties_PropertyOwner, specific=smif_expressions_Traversal)
gen_smif_expressions_ObjectOperationType_FunctionType = Generalization(general=FunctionType, specific=smif_expressions_ObjectOperationType)
gen_smif_expressions_Equality_ExpressionNode = Generalization(general=ExpressionNode, specific=smif_expressions_Equality)
gen_smif_expressions_Evaluation_ExpressionContext = Generalization(general=ExpressionContext, specific=smif_expressions_Evaluation)
gen_smif_expressions_ExpressionContext_IdentifiableEntity = Generalization(general=IdentifiableEntity, specific=smif_expressions_ExpressionContext)
gen_smif_relationships_Relationship_situations_ActualSituation = Generalization(general=situations_ActualSituation, specific=smif_relationships_Relationship)
gen_smif_expressions_ConstantReference_ExpressionNode = Generalization(general=ExpressionNode, specific=smif_expressions_ConstantReference)
gen_smif_expressions_ExpressionNode_ExpressionContext = Generalization(general=ExpressionContext, specific=smif_expressions_ExpressionNode)
gen_smif_constraints_MultiplicityConstraint_TypeConstraint = Generalization(general=TypeConstraint, specific=smif_constraints_MultiplicityConstraint)
gen_smif_constraints_UniquenessConstraint_TypeConstraint = Generalization(general=TypeConstraint, specific=smif_constraints_UniquenessConstraint)
gen_smif_constraints_ConditionalRule_constraints_Rule = Generalization(general=constraints_Rule, specific=smif_constraints_ConditionalRule)
gen_smif_constraints_ConditionalRule_constraints_Conditional = Generalization(general=constraints_Conditional, specific=smif_constraints_ConditionalRule)
gen_smif_constraints_TypeConstraint_Rule = Generalization(general=Rule, specific=smif_constraints_TypeConstraint)
gen_smif_constraints_Equivalent_Rule = Generalization(general=Rule, specific=smif_constraints_Equivalent)
gen_smif_constraints_Disjoint_Rule = Generalization(general=Rule, specific=smif_constraints_Disjoint)
gen_smif_constraints_Enumerated_Rule = Generalization(general=Rule, specific=smif_constraints_Enumerated)
gen_smif_constraints_GeneralizationConstraint_TypeConstraint = Generalization(general=TypeConstraint, specific=smif_constraints_GeneralizationConstraint)
gen_smif_constraints_PropertyConstraint_Rule = Generalization(general=Rule, specific=smif_constraints_PropertyConstraint)
gen_smif_constraints_PropertyTransitivityConstraint_PropertyConstraint = Generalization(general=PropertyConstraint, specific=smif_constraints_PropertyTransitivityConstraint)
gen_smif_constraints_PropertyTypeConstraint_PropertyConstraint = Generalization(general=PropertyConstraint, specific=smif_constraints_PropertyTypeConstraint)
gen_smif_relationships_Relationship_properties_PropertyOwner = Generalization(general=properties_PropertyOwner, specific=smif_relationships_Relationship)
gen_smif_relationships_RelationshipType_situations_SituationType = Generalization(general=situations_SituationType, specific=smif_relationships_RelationshipType)
gen_smif_relationships_RelationshipType_properties_PropertyOwnerType = Generalization(general=properties_PropertyOwnerType, specific=smif_relationships_RelationshipType)
gen_smif_constraints_Rule_Proposition = Generalization(general=Proposition, specific=smif_constraints_Rule)
gen_smif_toplevel_IdentifiableEntity_Thing = Generalization(general=Thing, specific=smif_toplevel_IdentifiableEntity)
gen_smif_constraints_CoveringConstraint_TypeConstraint = Generalization(general=TypeConstraint, specific=smif_constraints_CoveringConstraint)
gen_smif_constraints_FacetClassificationConstraint_GeneralizationConstraint = Generalization(general=GeneralizationConstraint, specific=smif_constraints_FacetClassificationConstraint)
gen_smif_toplevel_Context_IdentifiableEntity = Generalization(general=IdentifiableEntity, specific=smif_toplevel_Context)
gen_smif_toplevel_Proposition_IdentifiableEntity = Generalization(general=IdentifiableEntity, specific=smif_toplevel_Proposition)
gen_smif_toplevel_ActualEntity_TemporalEntity = Generalization(general=TemporalEntity, specific=smif_toplevel_ActualEntity)
gen_smif_toplevel_TemporalEntity_IdentifiableEntity = Generalization(general=IdentifiableEntity, specific=smif_toplevel_TemporalEntity)
gen_smif_patterns_Pattern_situations_SituationType = Generalization(general=situations_SituationType, specific=smif_patterns_Pattern)
gen_smif_patterns_Pattern_situations_Situation = Generalization(general=situations_Situation, specific=smif_patterns_Pattern)
gen_smif_patterns_Pattern_lexicalscope_LexicalScope = Generalization(general=lexicalscope_LexicalScope, specific=smif_patterns_Pattern)
gen_smif_patterns_Pattern_properties_PropertyOwner = Generalization(general=properties_PropertyOwner, specific=smif_patterns_Pattern)
gen_smif_patterns_PatternVariable_properties_OwnedPropertyType = Generalization(general=properties_OwnedPropertyType, specific=smif_patterns_PatternVariable)
gen_smif_patterns_PropositionVariable_PatternVariable = Generalization(general=PatternVariable, specific=smif_patterns_PropositionVariable)
gen_smif_patterns_ExpressionVariable_patterns_PatternVariable = Generalization(general=patterns_PatternVariable, specific=smif_patterns_ExpressionVariable)
gen_smif_patterns_ExpressionVariable_patterns_Computed = Generalization(general=patterns_Computed, specific=smif_patterns_ExpressionVariable)
gen_smif_patterns_PartVariable_TypePatternVariable = Generalization(general=TypePatternVariable, specific=smif_patterns_PartVariable)
gen_smif_patterns_FocusVariable_TypePatternVariable = Generalization(general=TypePatternVariable, specific=smif_patterns_FocusVariable)
gen_smif_patterns_TypePatternVariable_PatternVariable = Generalization(general=PatternVariable, specific=smif_patterns_TypePatternVariable)
gen_smif_patterns_PatternOfType_Pattern = Generalization(general=Pattern, specific=smif_patterns_PatternOfType)
gen_smif_patterns_PatternMatch_ActualSituation = Generalization(general=ActualSituation, specific=smif_patterns_PatternMatch)
gen_smif_patterns_PatternVariable_constraints_Conditional = Generalization(general=constraints_Conditional, specific=smif_patterns_PatternVariable)
gen_smif_mapping_MatchRule_Rule = Generalization(general=Rule, specific=smif_mapping_MatchRule)
gen_smif_mapping_MatchEnd_constraints_Conditional = Generalization(general=constraints_Conditional, specific=smif_mapping_MatchEnd)
gen_smif_mapping_MatchEnd_patterns_Computed = Generalization(general=patterns_Computed, specific=smif_mapping_MatchEnd)
gen_smif_mapping_Mapping_patterns_Pattern = Generalization(general=patterns_Pattern, specific=smif_mapping_Mapping)
gen_smif_mapping_Mapping_constraints_Rule = Generalization(general=constraints_Rule, specific=smif_mapping_Mapping)
gen_smif_mapping_Facade_RecordType = Generalization(general=RecordType, specific=smif_mapping_Facade)
gen_smif_mapping_ComputedFacade_Facade = Generalization(general=Facade, specific=smif_mapping_ComputedFacade)
gen_smif_patterns_VariableBinding_OwnedPropertyBinding = Generalization(general=OwnedPropertyBinding, specific=smif_patterns_VariableBinding)
gen_smif_lexicalscope_Model_Package = Generalization(general=Package, specific=smif_lexicalscope_Model)
gen_smif_lexicalscope_LexicalScope_Namespace = Generalization(general=Namespace, specific=smif_lexicalscope_LexicalScope)
gen_smif_lexicalscope_LexicalReference_Context = Generalization(general=Context, specific=smif_lexicalscope_LexicalReference)
gen_smif_lexicalscope_Include_LexicalReference = Generalization(general=LexicalReference, specific=smif_lexicalscope_Include)
gen_smif_lexicalscope_Package_LexicalScope = Generalization(general=LexicalScope, specific=smif_lexicalscope_Package)
gen_smif_lexicalscope_MOFPackage_Package = Generalization(general=Package, specific=smif_lexicalscope_MOFPackage)
gen_smif_lexicalscope_LogicalPackage_Package = Generalization(general=Package, specific=smif_lexicalscope_LogicalPackage)
gen_smif_lexicalscope_PhysicalPackage_Package = Generalization(general=Package, specific=smif_lexicalscope_PhysicalPackage)
gen_smif_lexicalscope_MappingPackage_Package = Generalization(general=Package, specific=smif_lexicalscope_MappingPackage)
gen_smif_lexicalscope_Prefix_UniqueTextIdentifier = Generalization(general=UniqueTextIdentifier, specific=smif_lexicalscope_Prefix)
gen_smif_associations_AssociationType_PropertyOwnerType = Generalization(general=PropertyOwnerType, specific=smif_associations_AssociationType)
gen_smif_associations_Association_properties_PropertyOwner = Generalization(general=properties_PropertyOwner, specific=smif_associations_Association)
gen_smif_associations_Association_toplevel_Proposition = Generalization(general=toplevel_Proposition, specific=smif_associations_Association)
gen_smif_mapping_RepresentationRule_ConditionalRule = Generalization(general=ConditionalRule, specific=smif_mapping_RepresentationRule)
gen_smif_metadata_InformationSource_toplevel_ActualEntity = Generalization(general=toplevel_ActualEntity, specific=smif_metadata_InformationSource)
gen_smif_metadata_InformationSource_metadata_Metadata = Generalization(general=metadata_Metadata, specific=smif_metadata_InformationSource)
gen_smif_metadata_Metadata_Record = Generalization(general=Record, specific=smif_metadata_Metadata)
gen_smif_metadata_Definition_Metadata = Generalization(general=Metadata, specific=smif_metadata_Definition)
gen_smif_properties_PropertyBinding_Thing = Generalization(general=Thing, specific=smif_properties_PropertyBinding)
gen_smif_properties_PropertyType_Type = Generalization(general=Type, specific=smif_properties_PropertyType)
gen_smif_metadata_Statement_Metadata = Generalization(general=Metadata, specific=smif_metadata_Statement)
gen_smif_properties_CharacteristicType_properties_PropertyType = Generalization(general=properties_PropertyType, specific=smif_properties_CharacteristicType)
gen_smif_properties_CharacteristicType_situations_SituationType = Generalization(general=situations_SituationType, specific=smif_properties_CharacteristicType)
gen_smif_properties_CharacteristicBinding_properties_PropertyBinding = Generalization(general=properties_PropertyBinding, specific=smif_properties_CharacteristicBinding)
gen_smif_properties_CharacteristicBinding_situations_ActualSituation = Generalization(general=situations_ActualSituation, specific=smif_properties_CharacteristicBinding)
gen_smif_properties_AnnotationProperty_CharacteristicType = Generalization(general=CharacteristicType, specific=smif_properties_AnnotationProperty)
gen_smif_properties_OwnedPropertyType_PropertyType = Generalization(general=PropertyType, specific=smif_properties_OwnedPropertyType)
gen_smif_properties_PropertyOwnerType_Type = Generalization(general=Type, specific=smif_properties_PropertyOwnerType)
gen_smif_properties_OwnedPropertyBinding_PropertyBinding = Generalization(general=PropertyBinding, specific=smif_properties_OwnedPropertyBinding)
gen_smif_properties_PropertyOwner_Thing = Generalization(general=Thing, specific=smif_properties_PropertyOwner)
gen_smif_facets_FacetOfEntity_Relationship = Generalization(general=Relationship, specific=smif_facets_FacetOfEntity)
gen_smif_facets_Phase_facets_Facet = Generalization(general=facets_Facet, specific=smif_facets_Phase)
gen_smif_facets_Phase_situations_SituationType = Generalization(general=situations_SituationType, specific=smif_facets_Phase)
gen_smif_facets_Role_Facet = Generalization(general=Facet, specific=smif_facets_Role)
gen_smif_facets_Facet_Type = Generalization(general=Type, specific=smif_facets_Facet)
gen_smif_facets_Category_Facet = Generalization(general=Facet, specific=smif_facets_Category)
gen_smif_records_Record_situations_ActualSituation = Generalization(general=situations_ActualSituation, specific=smif_records_Record)
gen_smif_records_Record_properties_PropertyOwner = Generalization(general=properties_PropertyOwner, specific=smif_records_Record)
gen_smif_records_RecordType_situations_SituationType = Generalization(general=situations_SituationType, specific=smif_records_RecordType)
gen_smif_records_RecordType_properties_PropertyOwnerType = Generalization(general=properties_PropertyOwnerType, specific=smif_records_RecordType)

# Domain Model
domain_model = DomainModel(
    name="smif",
    types={smif_Repository, LexicalScope, smif_types_Type, lexicalscope_LexicalScope, toplevel_Context, Thing, PropertyType, PatternOfType, CoveringConstraint, GeneralizationConstraint, MultiplicityConstraint, PropertyTypeConstraint, RecordType, ExpressionContext, smif_types_IntersectionType, Type, smif_types_UnionType, smif_types_EntityType, smif_situations_SituationType, EntityType, smif_situations_Situation, toplevel_Proposition, toplevel_TemporalEntity, PatternMatch, smif_situations_ActualSituation, toplevel_ActualEntity, situations_Situation, smif_values_QuantityKind, ValueType, smif_values_UnitType, Definition, SystemOfUnits, smif_values_BaseUnitType, UnitType, smif_values_ValueType, smif_values_Value, smif_values_SystemOfUnits, Context, smif_values_StructuredValueType, values_ValueType, properties_PropertyOwnerType, smif_values_StructuredValue, values_Value, properties_PropertyOwner, MatchEnd, RepresentationRule, smif_identifiers_UniqueIdentifier, Identifier, Namespace, smif_identifiers_IRIIdentifier, TechnicalIdentifier, smif_identifiers_Term, identifiers_Name, identifiers_UniqueTextIdentifier, smif_identifiers_UniqueTextIdentifier, identifiers_UniqueIdentifier, identifiers_TextIdentifier, smif_identifiers_Identifier, IdentifiableEntity, smif_identifiers_Namespace, UniqueIdentifier, smif_identifiers_TextIdentifier, smif_identifiers_Name, TextIdentifier, smif_identifiers_TechnicalIdentifier, UniqueTextIdentifier, smif_expressions_FunctionType, expressions_ExpressionContext, ExpressionNode, FunctionCall, smif_values_UnitValue, Value, smif_values_ScalarQuantity, UnitValue, Evaluation, FunctionType, smif_expressions_FunctionCall, expressions_ExpressionNode, smif_expressions_Traversal, smif_expressions_ObjectOperationType, smif_expressions_Equality, smif_expressions_Evaluation, smif_expressions_ExpressionContext, smif_relationships_Relationship, situations_ActualSituation, smif_expressions_ConstantReference, smif_expressions_ExpressionNode, smif_constraints_MultiplicityConstraint, TypeConstraint, smif_constraints_UniquenessConstraint, smif_constraints_ConditionalRule, constraints_Rule, constraints_Conditional, smif_constraints_TypeConstraint, smif_constraints_Equivalent, smif_constraints_Disjoint, smif_constraints_Enumerated, smif_constraints_GeneralizationConstraint, smif_constraints_PropertyConstraint, smif_constraints_PropertyTransitivityConstraint, PropertyConstraint, smif_constraints_PropertyTypeConstraint, smif_relationships_RelationshipType, situations_SituationType, smif_constraints_Rule, Proposition, Rule, smif_toplevel_IdentifiableEntity, Statement, Metadata, Name, Record, InformationSource, PropertyBinding, smif_toplevel_Thing, ConstantReference, smif_constraints_CoveringConstraint, smif_constraints_FacetClassificationConstraint, smif_constraints_Conditional, smif_toplevel_Context, LexicalReference, smif_toplevel_Proposition, PropositionVariable, smif_toplevel_ActualEntity, TemporalEntity, smif_toplevel_TemporalEntity, smif_patterns_Pattern, PatternVariable, smif_patterns_PatternVariable, properties_OwnedPropertyType, Equality, Mapping, smif_patterns_PropositionVariable, smif_patterns_ExpressionVariable, patterns_PatternVariable, patterns_Computed, smif_patterns_PartVariable, TypePatternVariable, smif_patterns_FocusVariable, smif_patterns_TypePatternVariable, smif_patterns_PatternOfType, smif_patterns_PatternMatch, ActualSituation, VariableBinding, Pattern, smif_mapping_MatchRule, smif_mapping_MatchEnd, MatchRule, smif_mapping_Mapping, patterns_Pattern, smif_mapping_Facade, smif_mapping_ComputedFacade, Facade, Situation, smif_patterns_VariableBinding, OwnedPropertyBinding, smif_patterns_Computed, smif_lexicalscope_Model, Package, smif_lexicalscope_LexicalScope, smif_lexicalscope_LexicalReference, smif_lexicalscope_Include, smif_lexicalscope_Package, Prefix, smif_lexicalscope_MOFPackage, smif_lexicalscope_LogicalPackage, smif_lexicalscope_PhysicalPackage, smif_lexicalscope_MappingPackage, smif_lexicalscope_Prefix, smif_associations_AssociationType, PropertyOwnerType, smif_associations_Association, smif_mapping_RepresentationRule, ConditionalRule, smif_metadata_InformationSource, metadata_Metadata, smif_metadata_Metadata, smif_metadata_Definition, IRIIdentifier, Term, smif_properties_PropertyBinding, smif_properties_PropertyType, smif_metadata_Statement, smif_properties_CharacteristicType, properties_PropertyType, smif_properties_CharacteristicBinding, properties_PropertyBinding, smif_properties_AnnotationProperty, CharacteristicType, smif_properties_OwnedPropertyType, smif_properties_PropertyOwnerType, smif_properties_OwnedPropertyBinding, smif_properties_PropertyOwner, smif_facets_FacetOfEntity, Relationship, smif_facets_Phase, facets_Facet, smif_facets_Role, Facet, smif_facets_Facet, smif_facets_Category, smif_records_Record, smif_records_RecordType, Traversal, ObjectOperationType, UniquenessConstraint, VariableQualification, AssertionStrength},
    associations={lexicalScope0, categorizes1, hasProperty2, assertsPattern3, hasCovering4, hasSpecialization5, hasMultiplicity7, propertiesOfType9, recordingTypes11, hasGeneralization12, returnedBy15, matchedBy25, unitReference27, definedWithinSystem28, unitOfSystem29, respectOf16, assertedBy19, conceptRule20, representsRule22, uniqueWithin31, identifies32, preferredFor34, scopesIdentifier37, names39, implementedBy42, evaluatedBy49, implements51, calls53, traversesThrough56, receiver59, hasEqual62, evaluates65, evaluatesIn68, resultingType70, isUsedBy44, hasValue46, subsumedBy76, withRespectTo79, multiplicityOf82, hasUnique85, hasGeneral88, hasSpecific91, isOfType94, constrains71, subsumes74, wasStatedIn102, hasPreferred103, definedBy105, identifiedBy108, hasMetadata111, hasName113, hasRecord115, constrainedBy117, hasAuthoritativeSource120, hasBinding122, definedIn124, inContextOf126, hasType129, statedBy132, referencedBy134, isCoveredBy97, condition100, asserts141, contextualizes143, negates146, contextualizesExpress149, referencedByLR152, holdsWithin154, negatedWithin157, qualifiedWithin160, ownsVariable162, satisfiedBy164, hasEquality136, boundIn138, subsets175, excludedBy178, excludes181, referenceMapping184, concreteMapping186, qualifies189, subjectType192, _unnamed_PatternMatch195, satisfies197, hasOwningPattern167, hasSubset169, mapsTo172, concreteEnd206, referenceEnd209, mapRuleOf212, assertedType215, mapsVariable218, matchFrom221, matchTo223, concreteFocus226, hasMapRule229, referenceFocus232, matches200, _unnamed_VariableBinding201, computation204, defines241, references243, states246, referencedScope249, extendsScope252, hasPrefix255, prefixOf257, representedBy235, representedType238, resultedIn266, madeStatement269, metadataAbout272, externalReference275, externalTerm276, definesEntity278, binds281, boundBy284, boundTo287, statementDateAndTime259, version260, transactionId263, hasBindingProperty299, about302, aboutType305, propertyOf290, traversedBy293, receivedBy295, hasUniquenessConstraint297},
    generalizations={gen_smif_types_Type_lexicalscope_LexicalScope, gen_smif_types_Type_toplevel_Context, gen_smif_types_IntersectionType_Type, gen_smif_types_UnionType_Type, gen_smif_types_EntityType_Type, gen_smif_situations_SituationType_EntityType, gen_smif_situations_Situation_toplevel_Proposition, gen_smif_situations_Situation_toplevel_TemporalEntity, gen_smif_situations_Situation_toplevel_Context, gen_smif_situations_Situation_lexicalscope_LexicalScope, gen_smif_situations_ActualSituation_toplevel_ActualEntity, gen_smif_situations_ActualSituation_situations_Situation, gen_smif_values_QuantityKind_ValueType, gen_smif_values_UnitType_ValueType, gen_smif_values_BaseUnitType_UnitType, gen_smif_values_ValueType_Type, gen_smif_values_Value_Thing, gen_smif_values_SystemOfUnits_Context, gen_smif_values_StructuredValueType_values_ValueType, gen_smif_values_StructuredValueType_properties_PropertyOwnerType, gen_smif_values_StructuredValue_values_Value, gen_smif_identifiers_UniqueIdentifier_Identifier, gen_smif_identifiers_IRIIdentifier_TechnicalIdentifier, gen_smif_identifiers_Term_identifiers_Name, gen_smif_identifiers_Term_identifiers_UniqueTextIdentifier, gen_smif_identifiers_UniqueTextIdentifier_identifiers_UniqueIdentifier, gen_smif_identifiers_UniqueTextIdentifier_identifiers_TextIdentifier, gen_smif_identifiers_Identifier_Value, gen_smif_identifiers_Namespace_Context, gen_smif_identifiers_TextIdentifier_Identifier, gen_smif_identifiers_Name_TextIdentifier, gen_smif_identifiers_TechnicalIdentifier_UniqueTextIdentifier, gen_smif_expressions_FunctionType_properties_PropertyOwnerType, gen_smif_expressions_FunctionType_expressions_ExpressionContext, gen_smif_values_StructuredValue_properties_PropertyOwner, gen_smif_values_UnitValue_Value, gen_smif_values_ScalarQuantity_UnitValue, gen_smif_expressions_FunctionCall_expressions_ExpressionNode, gen_smif_expressions_FunctionCall_properties_PropertyOwner, gen_smif_expressions_Traversal_expressions_ExpressionNode, gen_smif_expressions_Traversal_properties_PropertyOwner, gen_smif_expressions_ObjectOperationType_FunctionType, gen_smif_expressions_Equality_ExpressionNode, gen_smif_expressions_Evaluation_ExpressionContext, gen_smif_expressions_ExpressionContext_IdentifiableEntity, gen_smif_relationships_Relationship_situations_ActualSituation, gen_smif_expressions_ConstantReference_ExpressionNode, gen_smif_expressions_ExpressionNode_ExpressionContext, gen_smif_constraints_MultiplicityConstraint_TypeConstraint, gen_smif_constraints_UniquenessConstraint_TypeConstraint, gen_smif_constraints_ConditionalRule_constraints_Rule, gen_smif_constraints_ConditionalRule_constraints_Conditional, gen_smif_constraints_TypeConstraint_Rule, gen_smif_constraints_Equivalent_Rule, gen_smif_constraints_Disjoint_Rule, gen_smif_constraints_Enumerated_Rule, gen_smif_constraints_GeneralizationConstraint_TypeConstraint, gen_smif_constraints_PropertyConstraint_Rule, gen_smif_constraints_PropertyTransitivityConstraint_PropertyConstraint, gen_smif_constraints_PropertyTypeConstraint_PropertyConstraint, gen_smif_relationships_Relationship_properties_PropertyOwner, gen_smif_relationships_RelationshipType_situations_SituationType, gen_smif_relationships_RelationshipType_properties_PropertyOwnerType, gen_smif_constraints_Rule_Proposition, gen_smif_toplevel_IdentifiableEntity_Thing, gen_smif_constraints_CoveringConstraint_TypeConstraint, gen_smif_constraints_FacetClassificationConstraint_GeneralizationConstraint, gen_smif_toplevel_Context_IdentifiableEntity, gen_smif_toplevel_Proposition_IdentifiableEntity, gen_smif_toplevel_ActualEntity_TemporalEntity, gen_smif_toplevel_TemporalEntity_IdentifiableEntity, gen_smif_patterns_Pattern_situations_SituationType, gen_smif_patterns_Pattern_situations_Situation, gen_smif_patterns_Pattern_lexicalscope_LexicalScope, gen_smif_patterns_Pattern_properties_PropertyOwner, gen_smif_patterns_PatternVariable_properties_OwnedPropertyType, gen_smif_patterns_PropositionVariable_PatternVariable, gen_smif_patterns_ExpressionVariable_patterns_PatternVariable, gen_smif_patterns_ExpressionVariable_patterns_Computed, gen_smif_patterns_PartVariable_TypePatternVariable, gen_smif_patterns_FocusVariable_TypePatternVariable, gen_smif_patterns_TypePatternVariable_PatternVariable, gen_smif_patterns_PatternOfType_Pattern, gen_smif_patterns_PatternMatch_ActualSituation, gen_smif_patterns_PatternVariable_constraints_Conditional, gen_smif_mapping_MatchRule_Rule, gen_smif_mapping_MatchEnd_constraints_Conditional, gen_smif_mapping_MatchEnd_patterns_Computed, gen_smif_mapping_Mapping_patterns_Pattern, gen_smif_mapping_Mapping_constraints_Rule, gen_smif_mapping_Facade_RecordType, gen_smif_mapping_ComputedFacade_Facade, gen_smif_patterns_VariableBinding_OwnedPropertyBinding, gen_smif_lexicalscope_Model_Package, gen_smif_lexicalscope_LexicalScope_Namespace, gen_smif_lexicalscope_LexicalReference_Context, gen_smif_lexicalscope_Include_LexicalReference, gen_smif_lexicalscope_Package_LexicalScope, gen_smif_lexicalscope_MOFPackage_Package, gen_smif_lexicalscope_LogicalPackage_Package, gen_smif_lexicalscope_PhysicalPackage_Package, gen_smif_lexicalscope_MappingPackage_Package, gen_smif_lexicalscope_Prefix_UniqueTextIdentifier, gen_smif_associations_AssociationType_PropertyOwnerType, gen_smif_associations_Association_properties_PropertyOwner, gen_smif_associations_Association_toplevel_Proposition, gen_smif_mapping_RepresentationRule_ConditionalRule, gen_smif_metadata_InformationSource_toplevel_ActualEntity, gen_smif_metadata_InformationSource_metadata_Metadata, gen_smif_metadata_Metadata_Record, gen_smif_metadata_Definition_Metadata, gen_smif_properties_PropertyBinding_Thing, gen_smif_properties_PropertyType_Type, gen_smif_metadata_Statement_Metadata, gen_smif_properties_CharacteristicType_properties_PropertyType, gen_smif_properties_CharacteristicType_situations_SituationType, gen_smif_properties_CharacteristicBinding_properties_PropertyBinding, gen_smif_properties_CharacteristicBinding_situations_ActualSituation, gen_smif_properties_AnnotationProperty_CharacteristicType, gen_smif_properties_OwnedPropertyType_PropertyType, gen_smif_properties_PropertyOwnerType_Type, gen_smif_properties_OwnedPropertyBinding_PropertyBinding, gen_smif_properties_PropertyOwner_Thing, gen_smif_facets_FacetOfEntity_Relationship, gen_smif_facets_Phase_facets_Facet, gen_smif_facets_Phase_situations_SituationType, gen_smif_facets_Role_Facet, gen_smif_facets_Facet_Type, gen_smif_facets_Category_Facet, gen_smif_records_Record_situations_ActualSituation, gen_smif_records_Record_properties_PropertyOwner, gen_smif_records_RecordType_situations_SituationType, gen_smif_records_RecordType_properties_PropertyOwnerType},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)