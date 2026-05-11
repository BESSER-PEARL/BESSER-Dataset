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
smif_types_Type = Class(name="smif_types_Type", is_abstract=True)
lexicalscope_LexicalScope = Class(name="lexicalscope_LexicalScope")
toplevel_Context = Class(name="toplevel_Context")
Thing = Class(name="Thing")
PropertyType = Class(name="PropertyType")
PatternOfType = Class(name="PatternOfType")
CoveringConstraint = Class(name="CoveringConstraint")
GeneralizationConstraint = Class(name="GeneralizationConstraint")
MultiplicityConstraint = Class(name="MultiplicityConstraint")
PropertyTypeConstraint = Class(name="PropertyTypeConstraint")
RecordType = Class(name="RecordType")
smif_Repository = Class(name="smif_Repository")
LexicalScope = Class(name="LexicalScope")
smif_situations_SituationType = Class(name="smif_situations_SituationType")
EntityType = Class(name="EntityType")
smif_situations_Situation = Class(name="smif_situations_Situation", is_abstract=True)
toplevel_Proposition = Class(name="toplevel_Proposition")
toplevel_TemporalEntity = Class(name="toplevel_TemporalEntity")
PatternMatch = Class(name="PatternMatch")
smif_situations_ActualSituation = Class(name="smif_situations_ActualSituation")
toplevel_ActualEntity = Class(name="toplevel_ActualEntity")
situations_Situation = Class(name="situations_Situation")
smif_values_QuantityKind = Class(name="smif_values_QuantityKind")
ValueType = Class(name="ValueType")
smif_values_UnitType = Class(name="smif_values_UnitType")
Definition = Class(name="Definition")
SystemOfUnits = Class(name="SystemOfUnits")
smif_values_BaseUnitType = Class(name="smif_values_BaseUnitType")
UnitType = Class(name="UnitType")
smif_values_ValueType = Class(name="smif_values_ValueType")
ExpressionContext = Class(name="ExpressionContext")
MatchEnd = Class(name="MatchEnd")
RepresentationRule = Class(name="RepresentationRule")
smif_types_IntersectionType = Class(name="smif_types_IntersectionType")
Type = Class(name="Type")
smif_types_UnionType = Class(name="smif_types_UnionType")
smif_types_EntityType = Class(name="smif_types_EntityType")
smif_values_UnitValue = Class(name="smif_values_UnitValue", is_abstract=True)
Value = Class(name="Value")
smif_values_ScalarQuantity = Class(name="smif_values_ScalarQuantity", is_abstract=True)
UnitValue = Class(name="UnitValue")
smif_identifiers_UniqueIdentifier = Class(name="smif_identifiers_UniqueIdentifier", is_abstract=True)
Identifier = Class(name="Identifier")
Namespace = Class(name="Namespace")
smif_identifiers_IRIIdentifier = Class(name="smif_identifiers_IRIIdentifier")
TechnicalIdentifier = Class(name="TechnicalIdentifier")
smif_identifiers_Term = Class(name="smif_identifiers_Term")
identifiers_Name = Class(name="identifiers_Name")
identifiers_UniqueTextIdentifier = Class(name="identifiers_UniqueTextIdentifier")
smif_identifiers_UniqueTextIdentifier = Class(name="smif_identifiers_UniqueTextIdentifier")
smif_values_Value = Class(name="smif_values_Value")
smif_values_SystemOfUnits = Class(name="smif_values_SystemOfUnits")
Context = Class(name="Context")
smif_values_StructuredValueType = Class(name="smif_values_StructuredValueType")
values_ValueType = Class(name="values_ValueType")
properties_PropertyOwnerType = Class(name="properties_PropertyOwnerType")
smif_values_StructuredValue = Class(name="smif_values_StructuredValue")
values_Value = Class(name="values_Value")
properties_PropertyOwner = Class(name="properties_PropertyOwner")
smif_expressions_FunctionType = Class(name="smif_expressions_FunctionType")
expressions_ExpressionContext = Class(name="expressions_ExpressionContext")
ExpressionNode = Class(name="ExpressionNode")
FunctionCall = Class(name="FunctionCall")
smif_expressions_ConstantReference = Class(name="smif_expressions_ConstantReference")
smif_expressions_ExpressionNode = Class(name="smif_expressions_ExpressionNode", is_abstract=True)
Evaluation = Class(name="Evaluation")
FunctionType = Class(name="FunctionType")
smif_expressions_FunctionCall = Class(name="smif_expressions_FunctionCall")
expressions_ExpressionNode = Class(name="expressions_ExpressionNode")
smif_expressions_Traversal = Class(name="smif_expressions_Traversal")
identifiers_UniqueIdentifier = Class(name="identifiers_UniqueIdentifier")
identifiers_TextIdentifier = Class(name="identifiers_TextIdentifier")
smif_identifiers_Identifier = Class(name="smif_identifiers_Identifier")
IdentifiableEntity = Class(name="IdentifiableEntity")
smif_identifiers_Namespace = Class(name="smif_identifiers_Namespace")
UniqueIdentifier = Class(name="UniqueIdentifier")
smif_identifiers_TextIdentifier = Class(name="smif_identifiers_TextIdentifier")
smif_identifiers_Name = Class(name="smif_identifiers_Name")
TextIdentifier = Class(name="TextIdentifier")
smif_identifiers_TechnicalIdentifier = Class(name="smif_identifiers_TechnicalIdentifier")
UniqueTextIdentifier = Class(name="UniqueTextIdentifier")
smif_relationships_Relationship = Class(name="smif_relationships_Relationship")
situations_ActualSituation = Class(name="situations_ActualSituation")
smif_relationships_RelationshipType = Class(name="smif_relationships_RelationshipType")
situations_SituationType = Class(name="situations_SituationType")
smif_constraints_Rule = Class(name="smif_constraints_Rule", is_abstract=True)
Proposition = Class(name="Proposition")
Rule = Class(name="Rule")
smif_constraints_MultiplicityConstraint = Class(name="smif_constraints_MultiplicityConstraint")
TypeConstraint = Class(name="TypeConstraint")
smif_expressions_ObjectOperationType = Class(name="smif_expressions_ObjectOperationType")
smif_expressions_Equality = Class(name="smif_expressions_Equality")
smif_expressions_Evaluation = Class(name="smif_expressions_Evaluation")
smif_expressions_ExpressionContext = Class(name="smif_expressions_ExpressionContext", is_abstract=True)
smif_constraints_GeneralizationConstraint = Class(name="smif_constraints_GeneralizationConstraint")
smif_constraints_PropertyConstraint = Class(name="smif_constraints_PropertyConstraint", is_abstract=True)
smif_constraints_PropertyTransitivityConstraint = Class(name="smif_constraints_PropertyTransitivityConstraint")
PropertyConstraint = Class(name="PropertyConstraint")
smif_constraints_PropertyTypeConstraint = Class(name="smif_constraints_PropertyTypeConstraint")
smif_constraints_CoveringConstraint = Class(name="smif_constraints_CoveringConstraint")
smif_constraints_FacetClassificationConstraint = Class(name="smif_constraints_FacetClassificationConstraint")
smif_constraints_Conditional = Class(name="smif_constraints_Conditional", is_abstract=True)
smif_constraints_UniquenessConstraint = Class(name="smif_constraints_UniquenessConstraint")
smif_constraints_ConditionalRule = Class(name="smif_constraints_ConditionalRule")
constraints_Rule = Class(name="constraints_Rule")
constraints_Conditional = Class(name="constraints_Conditional")
smif_constraints_TypeConstraint = Class(name="smif_constraints_TypeConstraint", is_abstract=True)
smif_constraints_Equivalent = Class(name="smif_constraints_Equivalent")
smif_constraints_Disjoint = Class(name="smif_constraints_Disjoint")
smif_constraints_Enumerated = Class(name="smif_constraints_Enumerated")
Metadata = Class(name="Metadata")
Name = Class(name="Name")
Record = Class(name="Record")
InformationSource = Class(name="InformationSource")
PropertyBinding = Class(name="PropertyBinding")
smif_toplevel_Thing = Class(name="smif_toplevel_Thing", is_abstract=True)
ConstantReference = Class(name="ConstantReference")
smif_toplevel_IdentifiableEntity = Class(name="smif_toplevel_IdentifiableEntity")
Statement = Class(name="Statement")
LexicalReference = Class(name="LexicalReference")
smif_toplevel_Proposition = Class(name="smif_toplevel_Proposition", is_abstract=True)
PropositionVariable = Class(name="PropositionVariable")
smif_toplevel_ActualEntity = Class(name="smif_toplevel_ActualEntity")
TemporalEntity = Class(name="TemporalEntity")
smif_toplevel_TemporalEntity = Class(name="smif_toplevel_TemporalEntity", is_abstract=True)
smif_patterns_Pattern = Class(name="smif_patterns_Pattern")
PatternVariable = Class(name="PatternVariable")
smif_patterns_PatternVariable = Class(name="smif_patterns_PatternVariable")
properties_OwnedPropertyType = Class(name="properties_OwnedPropertyType")
Equality = Class(name="Equality")
smif_toplevel_Context = Class(name="smif_toplevel_Context", is_abstract=True)
Mapping = Class(name="Mapping")
smif_patterns_PropositionVariable = Class(name="smif_patterns_PropositionVariable")
smif_patterns_ExpressionVariable = Class(name="smif_patterns_ExpressionVariable")
patterns_PatternVariable = Class(name="patterns_PatternVariable")
patterns_Computed = Class(name="patterns_Computed")
smif_patterns_PartVariable = Class(name="smif_patterns_PartVariable")
TypePatternVariable = Class(name="TypePatternVariable")
smif_patterns_FocusVariable = Class(name="smif_patterns_FocusVariable")
smif_patterns_TypePatternVariable = Class(name="smif_patterns_TypePatternVariable", is_abstract=True)
smif_patterns_PatternOfType = Class(name="smif_patterns_PatternOfType")
smif_patterns_PatternMatch = Class(name="smif_patterns_PatternMatch")
ActualSituation = Class(name="ActualSituation")
Pattern = Class(name="Pattern")
smif_patterns_VariableBinding = Class(name="smif_patterns_VariableBinding")
OwnedPropertyBinding = Class(name="OwnedPropertyBinding")
smif_patterns_Computed = Class(name="smif_patterns_Computed", is_abstract=True)
smif_mapping_MatchRule = Class(name="smif_mapping_MatchRule")
smif_mapping_MatchEnd = Class(name="smif_mapping_MatchEnd")
MatchRule = Class(name="MatchRule")
smif_mapping_Mapping = Class(name="smif_mapping_Mapping")
patterns_Pattern = Class(name="patterns_Pattern")
VariableBinding = Class(name="VariableBinding")
Situation = Class(name="Situation")
smif_mapping_Facade = Class(name="smif_mapping_Facade")
smif_mapping_ComputedFacade = Class(name="smif_mapping_ComputedFacade", is_abstract=True)
Facade = Class(name="Facade")
smif_mapping_RepresentationRule = Class(name="smif_mapping_RepresentationRule")
ConditionalRule = Class(name="ConditionalRule")
smif_lexicalscope_Model = Class(name="smif_lexicalscope_Model")
Package = Class(name="Package")
smif_lexicalscope_LexicalScope = Class(name="smif_lexicalscope_LexicalScope")
smif_lexicalscope_LexicalReference = Class(name="smif_lexicalscope_LexicalReference")
smif_lexicalscope_Package = Class(name="smif_lexicalscope_Package")
Prefix = Class(name="Prefix")
smif_lexicalscope_MOFPackage = Class(name="smif_lexicalscope_MOFPackage")
smif_lexicalscope_LogicalPackage = Class(name="smif_lexicalscope_LogicalPackage")
smif_lexicalscope_PhysicalPackage = Class(name="smif_lexicalscope_PhysicalPackage")
smif_lexicalscope_MappingPackage = Class(name="smif_lexicalscope_MappingPackage")
smif_lexicalscope_Prefix = Class(name="smif_lexicalscope_Prefix")
smif_associations_AssociationType = Class(name="smif_associations_AssociationType")
PropertyOwnerType = Class(name="PropertyOwnerType")
smif_associations_Association = Class(name="smif_associations_Association")
smif_metadata_Statement = Class(name="smif_metadata_Statement")
smif_metadata_InformationSource = Class(name="smif_metadata_InformationSource")
metadata_Metadata = Class(name="metadata_Metadata")
smif_metadata_Metadata = Class(name="smif_metadata_Metadata")
smif_lexicalscope_Include = Class(name="smif_lexicalscope_Include")
IRIIdentifier = Class(name="IRIIdentifier")
Term = Class(name="Term")
smif_metadata_Definition = Class(name="smif_metadata_Definition")
smif_properties_PropertyType = Class(name="smif_properties_PropertyType", is_abstract=True)
Traversal = Class(name="Traversal")
ObjectOperationType = Class(name="ObjectOperationType")
UniquenessConstraint = Class(name="UniquenessConstraint")
smif_properties_CharacteristicType = Class(name="smif_properties_CharacteristicType")
properties_PropertyType = Class(name="properties_PropertyType")
smif_properties_CharacteristicBinding = Class(name="smif_properties_CharacteristicBinding")
properties_PropertyBinding = Class(name="properties_PropertyBinding")
smif_properties_AnnotationProperty = Class(name="smif_properties_AnnotationProperty")
CharacteristicType = Class(name="CharacteristicType")
smif_properties_OwnedPropertyType = Class(name="smif_properties_OwnedPropertyType")
smif_properties_PropertyOwnerType = Class(name="smif_properties_PropertyOwnerType", is_abstract=True)
smif_properties_OwnedPropertyBinding = Class(name="smif_properties_OwnedPropertyBinding")
smif_properties_PropertyOwner = Class(name="smif_properties_PropertyOwner", is_abstract=True)
smif_facets_FacetOfEntity = Class(name="smif_facets_FacetOfEntity")
Relationship = Class(name="Relationship")
smif_facets_Phase = Class(name="smif_facets_Phase")
facets_Facet = Class(name="facets_Facet")
smif_facets_Role = Class(name="smif_facets_Role")
Facet = Class(name="Facet")
smif_properties_PropertyBinding = Class(name="smif_properties_PropertyBinding", is_abstract=True)
smif_records_Record = Class(name="smif_records_Record")
smif_records_RecordType = Class(name="smif_records_RecordType")
smif_facets_Facet = Class(name="smif_facets_Facet")
smif_facets_Category = Class(name="smif_facets_Category")

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

# smif_Repository class attributes and methods

# LexicalScope class attributes and methods

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
smif_values_UnitType.attributes={smif_values_UnitType_offset, smif_values_UnitType_ratio, smif_values_UnitType_symbol}

# Definition class attributes and methods

# SystemOfUnits class attributes and methods

# smif_values_BaseUnitType class attributes and methods

# UnitType class attributes and methods

# smif_values_ValueType class attributes and methods

# ExpressionContext class attributes and methods

# MatchEnd class attributes and methods

# RepresentationRule class attributes and methods

# smif_types_IntersectionType class attributes and methods

# Type class attributes and methods

# smif_types_UnionType class attributes and methods

# smif_types_EntityType class attributes and methods

# smif_values_UnitValue class attributes and methods
smif_values_UnitValue_hasValue: Property = Property(name="hasValue", type=StringType)
smif_values_UnitValue.attributes={smif_values_UnitValue_hasValue}

# Value class attributes and methods

# smif_values_ScalarQuantity class attributes and methods
smif_values_ScalarQuantity__unnamed_ScalarQuantity: Property = Property(name="_unnamed_ScalarQuantity", type=StringType)
smif_values_ScalarQuantity.attributes={smif_values_ScalarQuantity__unnamed_ScalarQuantity}

# UnitValue class attributes and methods

# smif_identifiers_UniqueIdentifier class attributes and methods

# Identifier class attributes and methods

# Namespace class attributes and methods

# smif_identifiers_IRIIdentifier class attributes and methods

# TechnicalIdentifier class attributes and methods

# smif_identifiers_Term class attributes and methods

# identifiers_Name class attributes and methods

# identifiers_UniqueTextIdentifier class attributes and methods

# smif_identifiers_UniqueTextIdentifier class attributes and methods

# smif_values_Value class attributes and methods

# smif_values_SystemOfUnits class attributes and methods

# Context class attributes and methods

# smif_values_StructuredValueType class attributes and methods

# values_ValueType class attributes and methods

# properties_PropertyOwnerType class attributes and methods

# smif_values_StructuredValue class attributes and methods

# values_Value class attributes and methods

# properties_PropertyOwner class attributes and methods

# smif_expressions_FunctionType class attributes and methods

# expressions_ExpressionContext class attributes and methods

# ExpressionNode class attributes and methods

# FunctionCall class attributes and methods

# smif_expressions_ConstantReference class attributes and methods

# smif_expressions_ExpressionNode class attributes and methods
smif_expressions_ExpressionNode_expressionText: Property = Property(name="expressionText", type=StringType)
smif_expressions_ExpressionNode_expressionTextLanguage: Property = Property(name="expressionTextLanguage", type=StringType)
smif_expressions_ExpressionNode.attributes={smif_expressions_ExpressionNode_expressionTextLanguage, smif_expressions_ExpressionNode_expressionText}

# Evaluation class attributes and methods

# FunctionType class attributes and methods

# smif_expressions_FunctionCall class attributes and methods

# expressions_ExpressionNode class attributes and methods

# smif_expressions_Traversal class attributes and methods
smif_expressions_Traversal_traverseToRelation: Property = Property(name="traverseToRelation", type=StringType)
smif_expressions_Traversal_inverse: Property = Property(name="inverse", type=StringType)
smif_expressions_Traversal.attributes={smif_expressions_Traversal_traverseToRelation, smif_expressions_Traversal_inverse}

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

# smif_relationships_Relationship class attributes and methods

# situations_ActualSituation class attributes and methods

# smif_relationships_RelationshipType class attributes and methods

# situations_SituationType class attributes and methods

# smif_constraints_Rule class attributes and methods

# Proposition class attributes and methods

# Rule class attributes and methods

# smif_constraints_MultiplicityConstraint class attributes and methods
smif_constraints_MultiplicityConstraint_mininumNumber: Property = Property(name="mininumNumber", type=StringType)
smif_constraints_MultiplicityConstraint_maximumNumber: Property = Property(name="maximumNumber", type=StringType)
smif_constraints_MultiplicityConstraint_atOnce: Property = Property(name="atOnce", type=StringType)
smif_constraints_MultiplicityConstraint_isSufficent: Property = Property(name="isSufficent", type=StringType)
smif_constraints_MultiplicityConstraint.attributes={smif_constraints_MultiplicityConstraint_atOnce, smif_constraints_MultiplicityConstraint_mininumNumber, smif_constraints_MultiplicityConstraint_maximumNumber, smif_constraints_MultiplicityConstraint_isSufficent}

# TypeConstraint class attributes and methods

# smif_expressions_ObjectOperationType class attributes and methods

# smif_expressions_Equality class attributes and methods

# smif_expressions_Evaluation class attributes and methods

# smif_expressions_ExpressionContext class attributes and methods

# smif_constraints_GeneralizationConstraint class attributes and methods
smif_constraints_GeneralizationConstraint_redefines: Property = Property(name="redefines", type=StringType)
smif_constraints_GeneralizationConstraint.attributes={smif_constraints_GeneralizationConstraint_redefines}

# smif_constraints_PropertyConstraint class attributes and methods

# smif_constraints_PropertyTransitivityConstraint class attributes and methods

# PropertyConstraint class attributes and methods

# smif_constraints_PropertyTypeConstraint class attributes and methods
smif_constraints_PropertyTypeConstraint_prerequisiteType: Property = Property(name="prerequisiteType", type=StringType)
smif_constraints_PropertyTypeConstraint.attributes={smif_constraints_PropertyTypeConstraint_prerequisiteType}

# smif_constraints_CoveringConstraint class attributes and methods

# smif_constraints_FacetClassificationConstraint class attributes and methods

# smif_constraints_Conditional class attributes and methods

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

# Metadata class attributes and methods

# Name class attributes and methods

# Record class attributes and methods

# InformationSource class attributes and methods

# PropertyBinding class attributes and methods

# smif_toplevel_Thing class attributes and methods

# ConstantReference class attributes and methods

# smif_toplevel_IdentifiableEntity class attributes and methods

# Statement class attributes and methods

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

# smif_toplevel_Context class attributes and methods

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

# Pattern class attributes and methods

# smif_patterns_VariableBinding class attributes and methods

# OwnedPropertyBinding class attributes and methods

# smif_patterns_Computed class attributes and methods

# smif_mapping_MatchRule class attributes and methods
smif_mapping_MatchRule_coerce: Property = Property(name="coerce", type=StringType)
smif_mapping_MatchRule.attributes={smif_mapping_MatchRule_coerce}

# smif_mapping_MatchEnd class attributes and methods

# MatchRule class attributes and methods

# smif_mapping_Mapping class attributes and methods
smif_mapping_Mapping_strength: Property = Property(name="strength", type=StringType)
smif_mapping_Mapping.attributes={smif_mapping_Mapping_strength}

# patterns_Pattern class attributes and methods

# VariableBinding class attributes and methods

# Situation class attributes and methods

# smif_mapping_Facade class attributes and methods

# smif_mapping_ComputedFacade class attributes and methods
smif_mapping_ComputedFacade_m_push: Method = Method(name="push", parameters={}, type=StringType)
smif_mapping_ComputedFacade_m_pull: Method = Method(name="pull", parameters={}, type=StringType)
smif_mapping_ComputedFacade.methods={smif_mapping_ComputedFacade_m_pull, smif_mapping_ComputedFacade_m_push}

# Facade class attributes and methods

# smif_mapping_RepresentationRule class attributes and methods
smif_mapping_RepresentationRule_mapAll: Property = Property(name="mapAll", type=StringType)
smif_mapping_RepresentationRule.attributes={smif_mapping_RepresentationRule_mapAll}

# ConditionalRule class attributes and methods

# smif_lexicalscope_Model class attributes and methods

# Package class attributes and methods

# smif_lexicalscope_LexicalScope class attributes and methods

# smif_lexicalscope_LexicalReference class attributes and methods

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

# smif_metadata_Statement class attributes and methods

# smif_metadata_InformationSource class attributes and methods

# metadata_Metadata class attributes and methods

# smif_metadata_Metadata class attributes and methods

# smif_lexicalscope_Include class attributes and methods

# IRIIdentifier class attributes and methods

# Term class attributes and methods

# smif_metadata_Definition class attributes and methods
smif_metadata_Definition_textDefinition: Property = Property(name="textDefinition", type=StringType)
smif_metadata_Definition_summaryDescription: Property = Property(name="summaryDescription", type=StringType)
smif_metadata_Definition.attributes={smif_metadata_Definition_summaryDescription, smif_metadata_Definition_textDefinition}

# smif_properties_PropertyType class attributes and methods

# Traversal class attributes and methods

# ObjectOperationType class attributes and methods

# UniquenessConstraint class attributes and methods

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

# smif_properties_PropertyBinding class attributes and methods

# smif_records_Record class attributes and methods

# smif_records_RecordType class attributes and methods

# smif_facets_Facet class attributes and methods

# smif_facets_Category class attributes and methods

# Relationships
categorizes1: BinaryAssociation = BinaryAssociation(
    name="categorizes1",
    ends={
        Property(name="Thing", type=smif_types_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="hasType", type=Thing, multiplicity=Multiplicity(0, 9999))
    }
)
hasProperty2: BinaryAssociation = BinaryAssociation(
    name="hasProperty2",
    ends={
        Property(name="PropertyType", type=smif_types_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="propertyOf", type=PropertyType, multiplicity=Multiplicity(0, 9999))
    }
)
assertsPattern3: BinaryAssociation = BinaryAssociation(
    name="assertsPattern3",
    ends={
        Property(name="PatternOfType", type=smif_types_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="subjectType", type=PatternOfType, multiplicity=Multiplicity(0, 9999))
    }
)
hasCovering4: BinaryAssociation = BinaryAssociation(
    name="hasCovering4",
    ends={
        Property(name="CoveringConstraint", type=smif_types_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="isCoveredBy", type=CoveringConstraint, multiplicity=Multiplicity(0, 9999))
    }
)
hasSpecialization5: BinaryAssociation = BinaryAssociation(
    name="hasSpecialization5",
    ends={
        Property(name="GeneralizationConstraint", type=smif_types_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="hasGeneral", type=GeneralizationConstraint, multiplicity=Multiplicity(0, 9999))
    }
)
hasMultiplicity6: BinaryAssociation = BinaryAssociation(
    name="hasMultiplicity6",
    ends={
        Property(name="MultiplicityConstraint", type=smif_types_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="multiplicityOf", type=MultiplicityConstraint, multiplicity=Multiplicity(0, 9999))
    }
)
propertiesOfType7: BinaryAssociation = BinaryAssociation(
    name="propertiesOfType7",
    ends={
        Property(name="PropertyTypeConstraint", type=smif_types_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="isOfType", type=PropertyTypeConstraint, multiplicity=Multiplicity(0, 9999))
    }
)
recordingTypes8: BinaryAssociation = BinaryAssociation(
    name="recordingTypes8",
    ends={
        Property(name="RecordType", type=smif_types_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="aboutType", type=RecordType, multiplicity=Multiplicity(0, 9999))
    }
)
lexicalScope0: BinaryAssociation = BinaryAssociation(
    name="lexicalScope0",
    ends={
        Property(name="LexicalScope", type=smif_Repository, multiplicity=Multiplicity(1, 1)),
        Property(name="smif_Repository", type=LexicalScope, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
matchedBy18: BinaryAssociation = BinaryAssociation(
    name="matchedBy18",
    ends={
        Property(name="PatternMatch", type=smif_situations_Situation, multiplicity=Multiplicity(1, 1)),
        Property(name="matches", type=PatternMatch, multiplicity=Multiplicity(0, 9999))
    }
)
unitReference19: BinaryAssociation = BinaryAssociation(
    name="unitReference19",
    ends={
        Property(name="Definition", type=smif_values_UnitType, multiplicity=Multiplicity(1, 1)),
        Property(name="smif_values_UnitType", type=Definition, multiplicity=Multiplicity(0, 1))
    }
)
definedWithinSystem20: BinaryAssociation = BinaryAssociation(
    name="definedWithinSystem20",
    ends={
        Property(name="SystemOfUnits", type=smif_values_UnitType, multiplicity=Multiplicity(1, 1)),
        Property(name="unitOfSystem", type=SystemOfUnits, multiplicity=Multiplicity(0, 1))
    }
)
hasGeneralization9: BinaryAssociation = BinaryAssociation(
    name="hasGeneralization9",
    ends={
        Property(name="GeneralizationConstraint10", type=smif_types_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="hasSpecific", type=GeneralizationConstraint, multiplicity=Multiplicity(0, 9999))
    }
)
returnedBy11: BinaryAssociation = BinaryAssociation(
    name="returnedBy11",
    ends={
        Property(name="ExpressionContext", type=smif_types_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="resultingType", type=ExpressionContext, multiplicity=Multiplicity(0, 9999))
    }
)
respectOf12: BinaryAssociation = BinaryAssociation(
    name="respectOf12",
    ends={
        Property(name="MultiplicityConstraint13", type=smif_types_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="withRespectTo", type=MultiplicityConstraint, multiplicity=Multiplicity(0, 9999))
    }
)
assertedBy14: BinaryAssociation = BinaryAssociation(
    name="assertedBy14",
    ends={
        Property(name="MatchEnd", type=smif_types_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="assertedType", type=MatchEnd, multiplicity=Multiplicity(0, 9999))
    }
)
conceptRule15: BinaryAssociation = BinaryAssociation(
    name="conceptRule15",
    ends={
        Property(name="RepresentationRule", type=smif_types_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="representedType", type=RepresentationRule, multiplicity=Multiplicity(1, 1))
    }
)
representsRule16: BinaryAssociation = BinaryAssociation(
    name="representsRule16",
    ends={
        Property(name="RepresentationRule17", type=smif_types_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="representedBy", type=RepresentationRule, multiplicity=Multiplicity(1, 1))
    }
)
uniqueWithin22: BinaryAssociation = BinaryAssociation(
    name="uniqueWithin22",
    ends={
        Property(name="Namespace", type=smif_identifiers_UniqueIdentifier, multiplicity=Multiplicity(1, 1)),
        Property(name="scopesIdentifier", type=Namespace, multiplicity=Multiplicity(1, 1))
    }
)
unitOfSystem21: BinaryAssociation = BinaryAssociation(
    name="unitOfSystem21",
    ends={
        Property(name="UnitType", type=smif_values_SystemOfUnits, multiplicity=Multiplicity(1, 1)),
        Property(name="definedWithinSystem", type=UnitType, multiplicity=Multiplicity(0, 9999))
    }
)
implementedBy29: BinaryAssociation = BinaryAssociation(
    name="implementedBy29",
    ends={
        Property(name="ExpressionNode", type=smif_expressions_FunctionType, multiplicity=Multiplicity(1, 1)),
        Property(name="implements", type=ExpressionNode, multiplicity=Multiplicity(0, 1))
    }
)
isUsedBy30: BinaryAssociation = BinaryAssociation(
    name="isUsedBy30",
    ends={
        Property(name="FunctionCall", type=smif_expressions_FunctionType, multiplicity=Multiplicity(1, 1)),
        Property(name="calls", type=FunctionCall, multiplicity=Multiplicity(0, 9999))
    }
)
hasValue31: BinaryAssociation = BinaryAssociation(
    name="hasValue31",
    ends={
        Property(name="Thing32", type=smif_expressions_ConstantReference, multiplicity=Multiplicity(1, 1)),
        Property(name="referencedBy", type=Thing, multiplicity=Multiplicity(1, 1))
    }
)
evaluatedBy33: BinaryAssociation = BinaryAssociation(
    name="evaluatedBy33",
    ends={
        Property(name="Evaluation", type=smif_expressions_ExpressionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="evaluates", type=Evaluation, multiplicity=Multiplicity(0, 9999))
    }
)
implements34: BinaryAssociation = BinaryAssociation(
    name="implements34",
    ends={
        Property(name="FunctionType", type=smif_expressions_ExpressionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="implementedBy", type=FunctionType, multiplicity=Multiplicity(0, 1))
    }
)
calls35: BinaryAssociation = BinaryAssociation(
    name="calls35",
    ends={
        Property(name="FunctionType36", type=smif_expressions_FunctionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="isUsedBy", type=FunctionType, multiplicity=Multiplicity(1, 1))
    }
)
identifies23: BinaryAssociation = BinaryAssociation(
    name="identifies23",
    ends={
        Property(name="IdentifiableEntity", type=smif_identifiers_Identifier, multiplicity=Multiplicity(1, 1)),
        Property(name="identifiedBy", type=IdentifiableEntity, multiplicity=Multiplicity(1, 1))
    }
)
preferredFor24: BinaryAssociation = BinaryAssociation(
    name="preferredFor24",
    ends={
        Property(name="IdentifiableEntity25", type=smif_identifiers_Identifier, multiplicity=Multiplicity(1, 1)),
        Property(name="hasPreferred", type=IdentifiableEntity, multiplicity=Multiplicity(0, 1))
    }
)
scopesIdentifier26: BinaryAssociation = BinaryAssociation(
    name="scopesIdentifier26",
    ends={
        Property(name="UniqueIdentifier", type=smif_identifiers_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="uniqueWithin", type=UniqueIdentifier, multiplicity=Multiplicity(0, 9999))
    }
)
names27: BinaryAssociation = BinaryAssociation(
    name="names27",
    ends={
        Property(name="IdentifiableEntity28", type=smif_identifiers_Name, multiplicity=Multiplicity(1, 1)),
        Property(name="hasName", type=IdentifiableEntity, multiplicity=Multiplicity(1, 9999))
    }
)
evaluatesIn45: BinaryAssociation = BinaryAssociation(
    name="evaluatesIn45",
    ends={
        Property(name="Context", type=smif_expressions_ExpressionContext, multiplicity=Multiplicity(1, 1)),
        Property(name="contextualizesExpress", type=Context, multiplicity=Multiplicity(0, 1))
    }
)
resultingType46: BinaryAssociation = BinaryAssociation(
    name="resultingType46",
    ends={
        Property(name="Type", type=smif_expressions_ExpressionContext, multiplicity=Multiplicity(1, 1)),
        Property(name="returnedBy", type=Type, multiplicity=Multiplicity(1, 9999))
    }
)
constrains47: BinaryAssociation = BinaryAssociation(
    name="constrains47",
    ends={
        Property(name="IdentifiableEntity48", type=smif_constraints_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="constrainedBy", type=IdentifiableEntity, multiplicity=Multiplicity(0, 9999))
    }
)
subsumes49: BinaryAssociation = BinaryAssociation(
    name="subsumes49",
    ends={
        Property(name="Rule", type=smif_constraints_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="subsumedBy", type=Rule, multiplicity=Multiplicity(0, 9999))
    }
)
subsumedBy50: BinaryAssociation = BinaryAssociation(
    name="subsumedBy50",
    ends={
        Property(name="Rule51", type=smif_constraints_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="subsumes", type=Rule, multiplicity=Multiplicity(0, 9999))
    }
)
withRespectTo52: BinaryAssociation = BinaryAssociation(
    name="withRespectTo52",
    ends={
        Property(name="Type53", type=smif_constraints_MultiplicityConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="respectOf", type=Type, multiplicity=Multiplicity(0, 9999))
    }
)
traversesThrough37: BinaryAssociation = BinaryAssociation(
    name="traversesThrough37",
    ends={
        Property(name="PropertyType38", type=smif_expressions_Traversal, multiplicity=Multiplicity(1, 1)),
        Property(name="traversedBy", type=PropertyType, multiplicity=Multiplicity(1, 9999))
    }
)
receiver39: BinaryAssociation = BinaryAssociation(
    name="receiver39",
    ends={
        Property(name="PropertyType40", type=smif_expressions_ObjectOperationType, multiplicity=Multiplicity(1, 1)),
        Property(name="receivedBy", type=PropertyType, multiplicity=Multiplicity(1, 1))
    }
)
hasEqual41: BinaryAssociation = BinaryAssociation(
    name="hasEqual41",
    ends={
        Property(name="Thing42", type=smif_expressions_Equality, multiplicity=Multiplicity(1, 1)),
        Property(name="hasEquality", type=Thing, multiplicity=Multiplicity(1, 9999))
    }
)
evaluates43: BinaryAssociation = BinaryAssociation(
    name="evaluates43",
    ends={
        Property(name="ExpressionNode44", type=smif_expressions_Evaluation, multiplicity=Multiplicity(1, 1)),
        Property(name="evaluatedBy", type=ExpressionNode, multiplicity=Multiplicity(1, 1))
    }
)
hasGeneral58: BinaryAssociation = BinaryAssociation(
    name="hasGeneral58",
    ends={
        Property(name="Type59", type=smif_constraints_GeneralizationConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="hasSpecialization", type=Type, multiplicity=Multiplicity(1, 1))
    }
)
hasSpecific60: BinaryAssociation = BinaryAssociation(
    name="hasSpecific60",
    ends={
        Property(name="Type61", type=smif_constraints_GeneralizationConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="hasGeneralization", type=Type, multiplicity=Multiplicity(1, 1))
    }
)
isOfType62: BinaryAssociation = BinaryAssociation(
    name="isOfType62",
    ends={
        Property(name="Type63", type=smif_constraints_PropertyTypeConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="propertiesOfType", type=Type, multiplicity=Multiplicity(1, 1))
    }
)
isCoveredBy64: BinaryAssociation = BinaryAssociation(
    name="isCoveredBy64",
    ends={
        Property(name="Type65", type=smif_constraints_CoveringConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="hasCovering", type=Type, multiplicity=Multiplicity(0, 9999))
    }
)
multiplicityOf54: BinaryAssociation = BinaryAssociation(
    name="multiplicityOf54",
    ends={
        Property(name="Type55", type=smif_constraints_MultiplicityConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="hasMultiplicity", type=Type, multiplicity=Multiplicity(1, 1))
    }
)
condition66: BinaryAssociation = BinaryAssociation(
    name="condition66",
    ends={
        Property(name="ExpressionNode67", type=smif_constraints_Conditional, multiplicity=Multiplicity(1, 1)),
        Property(name="smif_constraints_Conditional", type=ExpressionNode, multiplicity=Multiplicity(0, 1))
    }
)
hasUnique56: BinaryAssociation = BinaryAssociation(
    name="hasUnique56",
    ends={
        Property(name="PropertyType57", type=smif_constraints_UniquenessConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="hasUniquenessConstraint", type=PropertyType, multiplicity=Multiplicity(1, 9999))
    }
)
definedBy70: BinaryAssociation = BinaryAssociation(
    name="definedBy70",
    ends={
        Property(name="Definition71", type=smif_toplevel_IdentifiableEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="definesEntity", type=Definition, multiplicity=Multiplicity(0, 9999))
    }
)
identifiedBy72: BinaryAssociation = BinaryAssociation(
    name="identifiedBy72",
    ends={
        Property(name="Identifier73", type=smif_toplevel_IdentifiableEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="identifies", type=Identifier, multiplicity=Multiplicity(0, 9999))
    }
)
hasMetadata74: BinaryAssociation = BinaryAssociation(
    name="hasMetadata74",
    ends={
        Property(name="Metadata", type=smif_toplevel_IdentifiableEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="metadataAbout", type=Metadata, multiplicity=Multiplicity(0, 9999))
    }
)
hasName75: BinaryAssociation = BinaryAssociation(
    name="hasName75",
    ends={
        Property(name="Name", type=smif_toplevel_IdentifiableEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="names", type=Name, multiplicity=Multiplicity(0, 9999))
    }
)
hasRecord76: BinaryAssociation = BinaryAssociation(
    name="hasRecord76",
    ends={
        Property(name="Record", type=smif_toplevel_IdentifiableEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="about", type=Record, multiplicity=Multiplicity(0, 9999))
    }
)
constrainedBy77: BinaryAssociation = BinaryAssociation(
    name="constrainedBy77",
    ends={
        Property(name="Rule78", type=smif_toplevel_IdentifiableEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="constrains", type=Rule, multiplicity=Multiplicity(0, 9999))
    }
)
hasAuthoritativeSource79: BinaryAssociation = BinaryAssociation(
    name="hasAuthoritativeSource79",
    ends={
        Property(name="InformationSource", type=smif_toplevel_IdentifiableEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="madeStatement", type=InformationSource, multiplicity=Multiplicity(0, 9999))
    }
)
hasBinding80: BinaryAssociation = BinaryAssociation(
    name="hasBinding80",
    ends={
        Property(name="PropertyBinding", type=smif_toplevel_IdentifiableEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="boundTo", type=PropertyBinding, multiplicity=Multiplicity(0, 9999))
    }
)
definedIn81: BinaryAssociation = BinaryAssociation(
    name="definedIn81",
    ends={
        Property(name="LexicalScope82", type=smif_toplevel_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="smif_toplevel_Thing", type=LexicalScope, multiplicity=Multiplicity(1, 1))
    }
)
inContextOf83: BinaryAssociation = BinaryAssociation(
    name="inContextOf83",
    ends={
        Property(name="Context84", type=smif_toplevel_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="contextualizes", type=Context, multiplicity=Multiplicity(1, 9999))
    }
)
hasType85: BinaryAssociation = BinaryAssociation(
    name="hasType85",
    ends={
        Property(name="Type86", type=smif_toplevel_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="categorizes", type=Type, multiplicity=Multiplicity(1, 9999))
    }
)
statedBy87: BinaryAssociation = BinaryAssociation(
    name="statedBy87",
    ends={
        Property(name="LexicalScope88", type=smif_toplevel_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="states", type=LexicalScope, multiplicity=Multiplicity(0, 1))
    }
)
referencedBy89: BinaryAssociation = BinaryAssociation(
    name="referencedBy89",
    ends={
        Property(name="ConstantReference", type=smif_toplevel_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="hasValue", type=ConstantReference, multiplicity=Multiplicity(0, 9999))
    }
)
wasStatedIn68: BinaryAssociation = BinaryAssociation(
    name="wasStatedIn68",
    ends={
        Property(name="Statement", type=smif_toplevel_IdentifiableEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="resultedIn", type=Statement, multiplicity=Multiplicity(0, 9999))
    }
)
hasPreferred69: BinaryAssociation = BinaryAssociation(
    name="hasPreferred69",
    ends={
        Property(name="Identifier", type=smif_toplevel_IdentifiableEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="preferredFor", type=Identifier, multiplicity=Multiplicity(0, 1))
    }
)
asserts93: BinaryAssociation = BinaryAssociation(
    name="asserts93",
    ends={
        Property(name="Proposition", type=smif_toplevel_Context, multiplicity=Multiplicity(1, 1)),
        Property(name="holdsWithin", type=Proposition, multiplicity=Multiplicity(0, 9999))
    }
)
contextualizes94: BinaryAssociation = BinaryAssociation(
    name="contextualizes94",
    ends={
        Property(name="Thing95", type=smif_toplevel_Context, multiplicity=Multiplicity(1, 1)),
        Property(name="inContextOf", type=Thing, multiplicity=Multiplicity(0, 9999))
    }
)
negates96: BinaryAssociation = BinaryAssociation(
    name="negates96",
    ends={
        Property(name="Proposition97", type=smif_toplevel_Context, multiplicity=Multiplicity(1, 1)),
        Property(name="negatedWithin", type=Proposition, multiplicity=Multiplicity(0, 9999))
    }
)
contextualizesExpress98: BinaryAssociation = BinaryAssociation(
    name="contextualizesExpress98",
    ends={
        Property(name="ExpressionContext99", type=smif_toplevel_Context, multiplicity=Multiplicity(1, 1)),
        Property(name="evaluatesIn", type=ExpressionContext, multiplicity=Multiplicity(0, 9999))
    }
)
referencedByLR100: BinaryAssociation = BinaryAssociation(
    name="referencedByLR100",
    ends={
        Property(name="LexicalReference", type=smif_toplevel_Context, multiplicity=Multiplicity(1, 1)),
        Property(name="referencedScope", type=LexicalReference, multiplicity=Multiplicity(0, 9999))
    }
)
holdsWithin101: BinaryAssociation = BinaryAssociation(
    name="holdsWithin101",
    ends={
        Property(name="Context102", type=smif_toplevel_Proposition, multiplicity=Multiplicity(1, 1)),
        Property(name="asserts", type=Context, multiplicity=Multiplicity(0, 9999))
    }
)
negatedWithin103: BinaryAssociation = BinaryAssociation(
    name="negatedWithin103",
    ends={
        Property(name="Context104", type=smif_toplevel_Proposition, multiplicity=Multiplicity(1, 1)),
        Property(name="negates", type=Context, multiplicity=Multiplicity(0, 9999))
    }
)
qualifiedWithin105: BinaryAssociation = BinaryAssociation(
    name="qualifiedWithin105",
    ends={
        Property(name="PropositionVariable", type=smif_toplevel_Proposition, multiplicity=Multiplicity(1, 1)),
        Property(name="qualifies", type=PropositionVariable, multiplicity=Multiplicity(0, 1))
    }
)
ownsVariable106: BinaryAssociation = BinaryAssociation(
    name="ownsVariable106",
    ends={
        Property(name="PatternVariable", type=smif_patterns_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="hasOwningPattern", type=PatternVariable, multiplicity=Multiplicity(0, 9999))
    }
)
satisfiedBy107: BinaryAssociation = BinaryAssociation(
    name="satisfiedBy107",
    ends={
        Property(name="PatternMatch108", type=smif_patterns_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="satisfies", type=PatternMatch, multiplicity=Multiplicity(0, 9999))
    }
)
hasEquality90: BinaryAssociation = BinaryAssociation(
    name="hasEquality90",
    ends={
        Property(name="Equality", type=smif_toplevel_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="hasEqual", type=Equality, multiplicity=Multiplicity(0, 9999))
    }
)
boundIn91: BinaryAssociation = BinaryAssociation(
    name="boundIn91",
    ends={
        Property(name="PropertyBinding92", type=smif_toplevel_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="binds", type=PropertyBinding, multiplicity=Multiplicity(0, 9999))
    }
)
mapsTo112: BinaryAssociation = BinaryAssociation(
    name="mapsTo112",
    ends={
        Property(name="MatchEnd113", type=smif_patterns_PatternVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="mapsVariable", type=MatchEnd, multiplicity=Multiplicity(0, 9999))
    }
)
subsets114: BinaryAssociation = BinaryAssociation(
    name="subsets114",
    ends={
        Property(name="PatternVariable115", type=smif_patterns_PatternVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="hasSubset", type=PatternVariable, multiplicity=Multiplicity(0, 9999))
    }
)
excludedBy116: BinaryAssociation = BinaryAssociation(
    name="excludedBy116",
    ends={
        Property(name="PatternVariable117", type=smif_patterns_PatternVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="excludes", type=PatternVariable, multiplicity=Multiplicity(0, 9999))
    }
)
excludes118: BinaryAssociation = BinaryAssociation(
    name="excludes118",
    ends={
        Property(name="PatternVariable119", type=smif_patterns_PatternVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="excludedBy", type=PatternVariable, multiplicity=Multiplicity(0, 9999))
    }
)
referenceMapping120: BinaryAssociation = BinaryAssociation(
    name="referenceMapping120",
    ends={
        Property(name="Mapping", type=smif_patterns_PatternVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="referenceFocus", type=Mapping, multiplicity=Multiplicity(0, 1))
    }
)
concreteMapping121: BinaryAssociation = BinaryAssociation(
    name="concreteMapping121",
    ends={
        Property(name="Mapping122", type=smif_patterns_PatternVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="concreteFocus", type=Mapping, multiplicity=Multiplicity(0, 1))
    }
)
qualifies123: BinaryAssociation = BinaryAssociation(
    name="qualifies123",
    ends={
        Property(name="Proposition124", type=smif_patterns_PropositionVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="qualifiedWithin", type=Proposition, multiplicity=Multiplicity(1, 1))
    }
)
subjectType125: BinaryAssociation = BinaryAssociation(
    name="subjectType125",
    ends={
        Property(name="Type126", type=smif_patterns_PatternOfType, multiplicity=Multiplicity(1, 1)),
        Property(name="assertsPattern", type=Type, multiplicity=Multiplicity(1, 1))
    }
)
hasOwningPattern109: BinaryAssociation = BinaryAssociation(
    name="hasOwningPattern109",
    ends={
        Property(name="Pattern", type=smif_patterns_PatternVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="ownsVariable", type=Pattern, multiplicity=Multiplicity(1, 1))
    }
)
hasSubset110: BinaryAssociation = BinaryAssociation(
    name="hasSubset110",
    ends={
        Property(name="PatternVariable111", type=smif_patterns_PatternVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="subsets", type=PatternVariable, multiplicity=Multiplicity(0, 9999))
    }
)
_unnamed_VariableBinding131: BinaryAssociation = BinaryAssociation(
    name="_unnamed_VariableBinding131",
    ends={
        Property(name="PatternMatch132", type=smif_patterns_VariableBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="_unnamed_PatternMatch", type=PatternMatch, multiplicity=Multiplicity(1, 1))
    }
)
computation133: BinaryAssociation = BinaryAssociation(
    name="computation133",
    ends={
        Property(name="ExpressionNode134", type=smif_patterns_Computed, multiplicity=Multiplicity(1, 1)),
        Property(name="smif_patterns_Computed", type=ExpressionNode, multiplicity=Multiplicity(0, 1))
    }
)
concreteEnd135: BinaryAssociation = BinaryAssociation(
    name="concreteEnd135",
    ends={
        Property(name="MatchEnd136", type=smif_mapping_MatchRule, multiplicity=Multiplicity(1, 1)),
        Property(name="matchFrom", type=MatchEnd, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
referenceEnd137: BinaryAssociation = BinaryAssociation(
    name="referenceEnd137",
    ends={
        Property(name="MatchEnd138", type=smif_mapping_MatchRule, multiplicity=Multiplicity(1, 1)),
        Property(name="matchTo", type=MatchEnd, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
mapRuleOf139: BinaryAssociation = BinaryAssociation(
    name="mapRuleOf139",
    ends={
        Property(name="Mapping140", type=smif_mapping_MatchRule, multiplicity=Multiplicity(1, 1)),
        Property(name="hasMapRule", type=Mapping, multiplicity=Multiplicity(1, 1))
    }
)
assertedType141: BinaryAssociation = BinaryAssociation(
    name="assertedType141",
    ends={
        Property(name="Type142", type=smif_mapping_MatchEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="assertedBy", type=Type, multiplicity=Multiplicity(0, 9999))
    }
)
mapsVariable143: BinaryAssociation = BinaryAssociation(
    name="mapsVariable143",
    ends={
        Property(name="PatternVariable144", type=smif_mapping_MatchEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="mapsTo", type=PatternVariable, multiplicity=Multiplicity(1, 1))
    }
)
matchFrom145: BinaryAssociation = BinaryAssociation(
    name="matchFrom145",
    ends={
        Property(name="MatchRule", type=smif_mapping_MatchEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="concreteEnd", type=MatchRule, multiplicity=Multiplicity(0, 1))
    }
)
matchTo146: BinaryAssociation = BinaryAssociation(
    name="matchTo146",
    ends={
        Property(name="MatchRule147", type=smif_mapping_MatchEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="referenceEnd", type=MatchRule, multiplicity=Multiplicity(0, 1))
    }
)
_unnamed_PatternMatch127: BinaryAssociation = BinaryAssociation(
    name="_unnamed_PatternMatch127",
    ends={
        Property(name="VariableBinding", type=smif_patterns_PatternMatch, multiplicity=Multiplicity(1, 1)),
        Property(name="_unnamed_VariableBinding", type=VariableBinding, multiplicity=Multiplicity(0, 9999))
    }
)
satisfies128: BinaryAssociation = BinaryAssociation(
    name="satisfies128",
    ends={
        Property(name="Pattern129", type=smif_patterns_PatternMatch, multiplicity=Multiplicity(1, 1)),
        Property(name="satisfiedBy", type=Pattern, multiplicity=Multiplicity(1, 1))
    }
)
matches130: BinaryAssociation = BinaryAssociation(
    name="matches130",
    ends={
        Property(name="Situation", type=smif_patterns_PatternMatch, multiplicity=Multiplicity(1, 1)),
        Property(name="matchedBy", type=Situation, multiplicity=Multiplicity(1, 1))
    }
)
referenceFocus152: BinaryAssociation = BinaryAssociation(
    name="referenceFocus152",
    ends={
        Property(name="PatternVariable153", type=smif_mapping_Mapping, multiplicity=Multiplicity(1, 1)),
        Property(name="referenceMapping", type=PatternVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
representedBy154: BinaryAssociation = BinaryAssociation(
    name="representedBy154",
    ends={
        Property(name="Type155", type=smif_mapping_RepresentationRule, multiplicity=Multiplicity(1, 1)),
        Property(name="representsRule", type=Type, multiplicity=Multiplicity(1, 1))
    }
)
representedType156: BinaryAssociation = BinaryAssociation(
    name="representedType156",
    ends={
        Property(name="Type157", type=smif_mapping_RepresentationRule, multiplicity=Multiplicity(1, 1)),
        Property(name="conceptRule", type=Type, multiplicity=Multiplicity(1, 9999))
    }
)
defines158: BinaryAssociation = BinaryAssociation(
    name="defines158",
    ends={
        Property(name="Thing159", type=smif_lexicalscope_LexicalScope, multiplicity=Multiplicity(1, 1)),
        Property(name="smif_lexicalscope_LexicalScope", type=Thing, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
references160: BinaryAssociation = BinaryAssociation(
    name="references160",
    ends={
        Property(name="LexicalReference161", type=smif_lexicalscope_LexicalScope, multiplicity=Multiplicity(1, 1)),
        Property(name="extendsScope", type=LexicalReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
states162: BinaryAssociation = BinaryAssociation(
    name="states162",
    ends={
        Property(name="Thing163", type=smif_lexicalscope_LexicalScope, multiplicity=Multiplicity(1, 1)),
        Property(name="statedBy", type=Thing, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referencedScope164: BinaryAssociation = BinaryAssociation(
    name="referencedScope164",
    ends={
        Property(name="Context165", type=smif_lexicalscope_LexicalReference, multiplicity=Multiplicity(1, 1)),
        Property(name="referencedByLR", type=Context, multiplicity=Multiplicity(1, 1))
    }
)
concreteFocus148: BinaryAssociation = BinaryAssociation(
    name="concreteFocus148",
    ends={
        Property(name="PatternVariable149", type=smif_mapping_Mapping, multiplicity=Multiplicity(1, 1)),
        Property(name="concreteMapping", type=PatternVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
hasMapRule150: BinaryAssociation = BinaryAssociation(
    name="hasMapRule150",
    ends={
        Property(name="MatchRule151", type=smif_mapping_Mapping, multiplicity=Multiplicity(1, 1)),
        Property(name="mapRuleOf", type=MatchRule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hasPrefix168: BinaryAssociation = BinaryAssociation(
    name="hasPrefix168",
    ends={
        Property(name="Prefix", type=smif_lexicalscope_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="prefixOf", type=Prefix, multiplicity=Multiplicity(0, 1))
    }
)
prefixOf169: BinaryAssociation = BinaryAssociation(
    name="prefixOf169",
    ends={
        Property(name="Package", type=smif_lexicalscope_Prefix, multiplicity=Multiplicity(1, 1)),
        Property(name="hasPrefix", type=Package, multiplicity=Multiplicity(1, 1))
    }
)
statementDateAndTime170: BinaryAssociation = BinaryAssociation(
    name="statementDateAndTime170",
    ends={
        Property(name="ValueType", type=smif_metadata_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="smif_metadata_Statement", type=ValueType, multiplicity=Multiplicity(1, 1))
    }
)
version171: BinaryAssociation = BinaryAssociation(
    name="version171",
    ends={
        Property(name="ValueType173", type=smif_metadata_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="smif_metadata_Statement172", type=ValueType, multiplicity=Multiplicity(1, 1))
    }
)
transactionId174: BinaryAssociation = BinaryAssociation(
    name="transactionId174",
    ends={
        Property(name="ValueType176", type=smif_metadata_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="smif_metadata_Statement175", type=ValueType, multiplicity=Multiplicity(1, 1))
    }
)
resultedIn177: BinaryAssociation = BinaryAssociation(
    name="resultedIn177",
    ends={
        Property(name="IdentifiableEntity178", type=smif_metadata_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="wasStatedIn", type=IdentifiableEntity, multiplicity=Multiplicity(1, 1))
    }
)
madeStatement179: BinaryAssociation = BinaryAssociation(
    name="madeStatement179",
    ends={
        Property(name="IdentifiableEntity180", type=smif_metadata_InformationSource, multiplicity=Multiplicity(1, 1)),
        Property(name="hasAuthoritativeSource", type=IdentifiableEntity, multiplicity=Multiplicity(1, 9999))
    }
)
extendsScope166: BinaryAssociation = BinaryAssociation(
    name="extendsScope166",
    ends={
        Property(name="LexicalScope167", type=smif_lexicalscope_LexicalReference, multiplicity=Multiplicity(1, 1)),
        Property(name="references", type=LexicalScope, multiplicity=Multiplicity(1, 1))
    }
)
externalReference183: BinaryAssociation = BinaryAssociation(
    name="externalReference183",
    ends={
        Property(name="IRIIdentifier", type=smif_metadata_Definition, multiplicity=Multiplicity(1, 1)),
        Property(name="smif_metadata_Definition", type=IRIIdentifier, multiplicity=Multiplicity(1, 1))
    }
)
externalTerm184: BinaryAssociation = BinaryAssociation(
    name="externalTerm184",
    ends={
        Property(name="Term", type=smif_metadata_Definition, multiplicity=Multiplicity(1, 1)),
        Property(name="smif_metadata_Definition185", type=Term, multiplicity=Multiplicity(1, 1))
    }
)
definesEntity186: BinaryAssociation = BinaryAssociation(
    name="definesEntity186",
    ends={
        Property(name="IdentifiableEntity187", type=smif_metadata_Definition, multiplicity=Multiplicity(1, 1)),
        Property(name="definedBy", type=IdentifiableEntity, multiplicity=Multiplicity(1, 1))
    }
)
metadataAbout181: BinaryAssociation = BinaryAssociation(
    name="metadataAbout181",
    ends={
        Property(name="IdentifiableEntity182", type=smif_metadata_Metadata, multiplicity=Multiplicity(1, 1)),
        Property(name="hasMetadata", type=IdentifiableEntity, multiplicity=Multiplicity(0, 9999))
    }
)
binds188: BinaryAssociation = BinaryAssociation(
    name="binds188",
    ends={
        Property(name="boundIn", type=Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="Thing189", type=smif_properties_PropertyBinding, multiplicity=Multiplicity(1, 1))
    }
)
boundBy190: BinaryAssociation = BinaryAssociation(
    name="boundBy190",
    ends={
        Property(name="PropertyType191", type=smif_properties_PropertyBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="hasBindingProperty", type=PropertyType, multiplicity=Multiplicity(1, 1))
    }
)
boundTo192: BinaryAssociation = BinaryAssociation(
    name="boundTo192",
    ends={
        Property(name="IdentifiableEntity193", type=smif_properties_PropertyBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="hasBinding", type=IdentifiableEntity, multiplicity=Multiplicity(1, 1))
    }
)
propertyOf194: BinaryAssociation = BinaryAssociation(
    name="propertyOf194",
    ends={
        Property(name="Type195", type=smif_properties_PropertyType, multiplicity=Multiplicity(1, 1)),
        Property(name="hasProperty", type=Type, multiplicity=Multiplicity(0, 1))
    }
)
traversedBy196: BinaryAssociation = BinaryAssociation(
    name="traversedBy196",
    ends={
        Property(name="Traversal", type=smif_properties_PropertyType, multiplicity=Multiplicity(1, 1)),
        Property(name="traversesThrough", type=Traversal, multiplicity=Multiplicity(0, 9999))
    }
)
receivedBy197: BinaryAssociation = BinaryAssociation(
    name="receivedBy197",
    ends={
        Property(name="ObjectOperationType", type=smif_properties_PropertyType, multiplicity=Multiplicity(1, 1)),
        Property(name="receiver", type=ObjectOperationType, multiplicity=Multiplicity(0, 9999))
    }
)
hasUniquenessConstraint198: BinaryAssociation = BinaryAssociation(
    name="hasUniquenessConstraint198",
    ends={
        Property(name="UniquenessConstraint", type=smif_properties_PropertyType, multiplicity=Multiplicity(1, 1)),
        Property(name="hasUnique", type=UniquenessConstraint, multiplicity=Multiplicity(0, 9999))
    }
)
hasBindingProperty199: BinaryAssociation = BinaryAssociation(
    name="hasBindingProperty199",
    ends={
        Property(name="PropertyBinding200", type=smif_properties_PropertyType, multiplicity=Multiplicity(1, 1)),
        Property(name="boundBy", type=PropertyBinding, multiplicity=Multiplicity(0, 9999))
    }
)
about201: BinaryAssociation = BinaryAssociation(
    name="about201",
    ends={
        Property(name="IdentifiableEntity202", type=smif_records_Record, multiplicity=Multiplicity(1, 1)),
        Property(name="hasRecord", type=IdentifiableEntity, multiplicity=Multiplicity(0, 9999))
    }
)
aboutType203: BinaryAssociation = BinaryAssociation(
    name="aboutType203",
    ends={
        Property(name="Type204", type=smif_records_RecordType, multiplicity=Multiplicity(1, 1)),
        Property(name="recordingTypes", type=Type, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_smif_types_Type_lexicalscope_LexicalScope = Generalization(general=lexicalscope_LexicalScope, specific=smif_types_Type)
gen_smif_types_Type_toplevel_Context = Generalization(general=toplevel_Context, specific=smif_types_Type)
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
gen_smif_types_IntersectionType_Type = Generalization(general=Type, specific=smif_types_IntersectionType)
gen_smif_types_UnionType_Type = Generalization(general=Type, specific=smif_types_UnionType)
gen_smif_types_EntityType_Type = Generalization(general=Type, specific=smif_types_EntityType)
gen_smif_values_UnitValue_Value = Generalization(general=Value, specific=smif_values_UnitValue)
gen_smif_values_ScalarQuantity_UnitValue = Generalization(general=UnitValue, specific=smif_values_ScalarQuantity)
gen_smif_identifiers_UniqueIdentifier_Identifier = Generalization(general=Identifier, specific=smif_identifiers_UniqueIdentifier)
gen_smif_identifiers_IRIIdentifier_TechnicalIdentifier = Generalization(general=TechnicalIdentifier, specific=smif_identifiers_IRIIdentifier)
gen_smif_identifiers_Term_identifiers_Name = Generalization(general=identifiers_Name, specific=smif_identifiers_Term)
gen_smif_identifiers_Term_identifiers_UniqueTextIdentifier = Generalization(general=identifiers_UniqueTextIdentifier, specific=smif_identifiers_Term)
gen_smif_values_ValueType_Type = Generalization(general=Type, specific=smif_values_ValueType)
gen_smif_values_Value_Thing = Generalization(general=Thing, specific=smif_values_Value)
gen_smif_values_SystemOfUnits_Context = Generalization(general=Context, specific=smif_values_SystemOfUnits)
gen_smif_values_StructuredValueType_values_ValueType = Generalization(general=values_ValueType, specific=smif_values_StructuredValueType)
gen_smif_values_StructuredValueType_properties_PropertyOwnerType = Generalization(general=properties_PropertyOwnerType, specific=smif_values_StructuredValueType)
gen_smif_values_StructuredValue_values_Value = Generalization(general=values_Value, specific=smif_values_StructuredValue)
gen_smif_values_StructuredValue_properties_PropertyOwner = Generalization(general=properties_PropertyOwner, specific=smif_values_StructuredValue)
gen_smif_expressions_FunctionType_properties_PropertyOwnerType = Generalization(general=properties_PropertyOwnerType, specific=smif_expressions_FunctionType)
gen_smif_expressions_FunctionType_expressions_ExpressionContext = Generalization(general=expressions_ExpressionContext, specific=smif_expressions_FunctionType)
gen_smif_expressions_ConstantReference_ExpressionNode = Generalization(general=ExpressionNode, specific=smif_expressions_ConstantReference)
gen_smif_expressions_ExpressionNode_ExpressionContext = Generalization(general=ExpressionContext, specific=smif_expressions_ExpressionNode)
gen_smif_expressions_FunctionCall_expressions_ExpressionNode = Generalization(general=expressions_ExpressionNode, specific=smif_expressions_FunctionCall)
gen_smif_expressions_FunctionCall_properties_PropertyOwner = Generalization(general=properties_PropertyOwner, specific=smif_expressions_FunctionCall)
gen_smif_expressions_Traversal_expressions_ExpressionNode = Generalization(general=expressions_ExpressionNode, specific=smif_expressions_Traversal)
gen_smif_expressions_Traversal_properties_PropertyOwner = Generalization(general=properties_PropertyOwner, specific=smif_expressions_Traversal)
gen_smif_identifiers_UniqueTextIdentifier_identifiers_UniqueIdentifier = Generalization(general=identifiers_UniqueIdentifier, specific=smif_identifiers_UniqueTextIdentifier)
gen_smif_identifiers_UniqueTextIdentifier_identifiers_TextIdentifier = Generalization(general=identifiers_TextIdentifier, specific=smif_identifiers_UniqueTextIdentifier)
gen_smif_identifiers_Identifier_Value = Generalization(general=Value, specific=smif_identifiers_Identifier)
gen_smif_identifiers_Namespace_Context = Generalization(general=Context, specific=smif_identifiers_Namespace)
gen_smif_identifiers_TextIdentifier_Identifier = Generalization(general=Identifier, specific=smif_identifiers_TextIdentifier)
gen_smif_identifiers_Name_TextIdentifier = Generalization(general=TextIdentifier, specific=smif_identifiers_Name)
gen_smif_identifiers_TechnicalIdentifier_UniqueTextIdentifier = Generalization(general=UniqueTextIdentifier, specific=smif_identifiers_TechnicalIdentifier)
gen_smif_relationships_Relationship_situations_ActualSituation = Generalization(general=situations_ActualSituation, specific=smif_relationships_Relationship)
gen_smif_relationships_Relationship_properties_PropertyOwner = Generalization(general=properties_PropertyOwner, specific=smif_relationships_Relationship)
gen_smif_relationships_RelationshipType_situations_SituationType = Generalization(general=situations_SituationType, specific=smif_relationships_RelationshipType)
gen_smif_relationships_RelationshipType_properties_PropertyOwnerType = Generalization(general=properties_PropertyOwnerType, specific=smif_relationships_RelationshipType)
gen_smif_constraints_Rule_Proposition = Generalization(general=Proposition, specific=smif_constraints_Rule)
gen_smif_constraints_MultiplicityConstraint_TypeConstraint = Generalization(general=TypeConstraint, specific=smif_constraints_MultiplicityConstraint)
gen_smif_expressions_ObjectOperationType_FunctionType = Generalization(general=FunctionType, specific=smif_expressions_ObjectOperationType)
gen_smif_expressions_Equality_ExpressionNode = Generalization(general=ExpressionNode, specific=smif_expressions_Equality)
gen_smif_expressions_Evaluation_ExpressionContext = Generalization(general=ExpressionContext, specific=smif_expressions_Evaluation)
gen_smif_expressions_ExpressionContext_IdentifiableEntity = Generalization(general=IdentifiableEntity, specific=smif_expressions_ExpressionContext)
gen_smif_constraints_GeneralizationConstraint_TypeConstraint = Generalization(general=TypeConstraint, specific=smif_constraints_GeneralizationConstraint)
gen_smif_constraints_PropertyConstraint_Rule = Generalization(general=Rule, specific=smif_constraints_PropertyConstraint)
gen_smif_constraints_PropertyTransitivityConstraint_PropertyConstraint = Generalization(general=PropertyConstraint, specific=smif_constraints_PropertyTransitivityConstraint)
gen_smif_constraints_PropertyTypeConstraint_PropertyConstraint = Generalization(general=PropertyConstraint, specific=smif_constraints_PropertyTypeConstraint)
gen_smif_constraints_CoveringConstraint_TypeConstraint = Generalization(general=TypeConstraint, specific=smif_constraints_CoveringConstraint)
gen_smif_constraints_FacetClassificationConstraint_GeneralizationConstraint = Generalization(general=GeneralizationConstraint, specific=smif_constraints_FacetClassificationConstraint)
gen_smif_constraints_UniquenessConstraint_TypeConstraint = Generalization(general=TypeConstraint, specific=smif_constraints_UniquenessConstraint)
gen_smif_constraints_ConditionalRule_constraints_Rule = Generalization(general=constraints_Rule, specific=smif_constraints_ConditionalRule)
gen_smif_constraints_ConditionalRule_constraints_Conditional = Generalization(general=constraints_Conditional, specific=smif_constraints_ConditionalRule)
gen_smif_constraints_TypeConstraint_Rule = Generalization(general=Rule, specific=smif_constraints_TypeConstraint)
gen_smif_constraints_Equivalent_Rule = Generalization(general=Rule, specific=smif_constraints_Equivalent)
gen_smif_constraints_Disjoint_Rule = Generalization(general=Rule, specific=smif_constraints_Disjoint)
gen_smif_constraints_Enumerated_Rule = Generalization(general=Rule, specific=smif_constraints_Enumerated)
gen_smif_toplevel_IdentifiableEntity_Thing = Generalization(general=Thing, specific=smif_toplevel_IdentifiableEntity)
gen_smif_toplevel_Proposition_IdentifiableEntity = Generalization(general=IdentifiableEntity, specific=smif_toplevel_Proposition)
gen_smif_toplevel_ActualEntity_TemporalEntity = Generalization(general=TemporalEntity, specific=smif_toplevel_ActualEntity)
gen_smif_toplevel_TemporalEntity_IdentifiableEntity = Generalization(general=IdentifiableEntity, specific=smif_toplevel_TemporalEntity)
gen_smif_patterns_Pattern_situations_SituationType = Generalization(general=situations_SituationType, specific=smif_patterns_Pattern)
gen_smif_patterns_Pattern_situations_Situation = Generalization(general=situations_Situation, specific=smif_patterns_Pattern)
gen_smif_patterns_Pattern_lexicalscope_LexicalScope = Generalization(general=lexicalscope_LexicalScope, specific=smif_patterns_Pattern)
gen_smif_patterns_Pattern_properties_PropertyOwner = Generalization(general=properties_PropertyOwner, specific=smif_patterns_Pattern)
gen_smif_patterns_PatternVariable_properties_OwnedPropertyType = Generalization(general=properties_OwnedPropertyType, specific=smif_patterns_PatternVariable)
gen_smif_patterns_PatternVariable_constraints_Conditional = Generalization(general=constraints_Conditional, specific=smif_patterns_PatternVariable)
gen_smif_toplevel_Context_IdentifiableEntity = Generalization(general=IdentifiableEntity, specific=smif_toplevel_Context)
gen_smif_patterns_PropositionVariable_PatternVariable = Generalization(general=PatternVariable, specific=smif_patterns_PropositionVariable)
gen_smif_patterns_ExpressionVariable_patterns_PatternVariable = Generalization(general=patterns_PatternVariable, specific=smif_patterns_ExpressionVariable)
gen_smif_patterns_ExpressionVariable_patterns_Computed = Generalization(general=patterns_Computed, specific=smif_patterns_ExpressionVariable)
gen_smif_patterns_PartVariable_TypePatternVariable = Generalization(general=TypePatternVariable, specific=smif_patterns_PartVariable)
gen_smif_patterns_FocusVariable_TypePatternVariable = Generalization(general=TypePatternVariable, specific=smif_patterns_FocusVariable)
gen_smif_patterns_TypePatternVariable_PatternVariable = Generalization(general=PatternVariable, specific=smif_patterns_TypePatternVariable)
gen_smif_patterns_PatternOfType_Pattern = Generalization(general=Pattern, specific=smif_patterns_PatternOfType)
gen_smif_patterns_PatternMatch_ActualSituation = Generalization(general=ActualSituation, specific=smif_patterns_PatternMatch)
gen_smif_patterns_VariableBinding_OwnedPropertyBinding = Generalization(general=OwnedPropertyBinding, specific=smif_patterns_VariableBinding)
gen_smif_mapping_MatchRule_Rule = Generalization(general=Rule, specific=smif_mapping_MatchRule)
gen_smif_mapping_MatchEnd_constraints_Conditional = Generalization(general=constraints_Conditional, specific=smif_mapping_MatchEnd)
gen_smif_mapping_MatchEnd_patterns_Computed = Generalization(general=patterns_Computed, specific=smif_mapping_MatchEnd)
gen_smif_mapping_Mapping_patterns_Pattern = Generalization(general=patterns_Pattern, specific=smif_mapping_Mapping)
gen_smif_mapping_Facade_RecordType = Generalization(general=RecordType, specific=smif_mapping_Facade)
gen_smif_mapping_ComputedFacade_Facade = Generalization(general=Facade, specific=smif_mapping_ComputedFacade)
gen_smif_mapping_RepresentationRule_ConditionalRule = Generalization(general=ConditionalRule, specific=smif_mapping_RepresentationRule)
gen_smif_lexicalscope_Model_Package = Generalization(general=Package, specific=smif_lexicalscope_Model)
gen_smif_lexicalscope_LexicalScope_Namespace = Generalization(general=Namespace, specific=smif_lexicalscope_LexicalScope)
gen_smif_mapping_Mapping_constraints_Rule = Generalization(general=constraints_Rule, specific=smif_mapping_Mapping)
gen_smif_lexicalscope_LexicalReference_Context = Generalization(general=Context, specific=smif_lexicalscope_LexicalReference)
gen_smif_lexicalscope_Package_LexicalScope = Generalization(general=LexicalScope, specific=smif_lexicalscope_Package)
gen_smif_lexicalscope_MOFPackage_Package = Generalization(general=Package, specific=smif_lexicalscope_MOFPackage)
gen_smif_lexicalscope_LogicalPackage_Package = Generalization(general=Package, specific=smif_lexicalscope_LogicalPackage)
gen_smif_lexicalscope_PhysicalPackage_Package = Generalization(general=Package, specific=smif_lexicalscope_PhysicalPackage)
gen_smif_lexicalscope_MappingPackage_Package = Generalization(general=Package, specific=smif_lexicalscope_MappingPackage)
gen_smif_lexicalscope_Prefix_UniqueTextIdentifier = Generalization(general=UniqueTextIdentifier, specific=smif_lexicalscope_Prefix)
gen_smif_associations_AssociationType_PropertyOwnerType = Generalization(general=PropertyOwnerType, specific=smif_associations_AssociationType)
gen_smif_associations_Association_properties_PropertyOwner = Generalization(general=properties_PropertyOwner, specific=smif_associations_Association)
gen_smif_associations_Association_toplevel_Proposition = Generalization(general=toplevel_Proposition, specific=smif_associations_Association)
gen_smif_metadata_Statement_Metadata = Generalization(general=Metadata, specific=smif_metadata_Statement)
gen_smif_metadata_InformationSource_toplevel_ActualEntity = Generalization(general=toplevel_ActualEntity, specific=smif_metadata_InformationSource)
gen_smif_metadata_InformationSource_metadata_Metadata = Generalization(general=metadata_Metadata, specific=smif_metadata_InformationSource)
gen_smif_metadata_Metadata_Record = Generalization(general=Record, specific=smif_metadata_Metadata)
gen_smif_lexicalscope_Include_LexicalReference = Generalization(general=LexicalReference, specific=smif_lexicalscope_Include)
gen_smif_metadata_Definition_Metadata = Generalization(general=Metadata, specific=smif_metadata_Definition)
gen_smif_properties_PropertyType_Type = Generalization(general=Type, specific=smif_properties_PropertyType)
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
gen_smif_properties_PropertyBinding_Thing = Generalization(general=Thing, specific=smif_properties_PropertyBinding)
gen_smif_records_Record_situations_ActualSituation = Generalization(general=situations_ActualSituation, specific=smif_records_Record)
gen_smif_records_Record_properties_PropertyOwner = Generalization(general=properties_PropertyOwner, specific=smif_records_Record)
gen_smif_records_RecordType_situations_SituationType = Generalization(general=situations_SituationType, specific=smif_records_RecordType)
gen_smif_records_RecordType_properties_PropertyOwnerType = Generalization(general=properties_PropertyOwnerType, specific=smif_records_RecordType)
gen_smif_facets_Facet_Type = Generalization(general=Type, specific=smif_facets_Facet)
gen_smif_facets_Category_Facet = Generalization(general=Facet, specific=smif_facets_Category)

# Domain Model
domain_model = DomainModel(
    name="smif",
    types={smif_types_Type, lexicalscope_LexicalScope, toplevel_Context, Thing, PropertyType, PatternOfType, CoveringConstraint, GeneralizationConstraint, MultiplicityConstraint, PropertyTypeConstraint, RecordType, smif_Repository, LexicalScope, smif_situations_SituationType, EntityType, smif_situations_Situation, toplevel_Proposition, toplevel_TemporalEntity, PatternMatch, smif_situations_ActualSituation, toplevel_ActualEntity, situations_Situation, smif_values_QuantityKind, ValueType, smif_values_UnitType, Definition, SystemOfUnits, smif_values_BaseUnitType, UnitType, smif_values_ValueType, ExpressionContext, MatchEnd, RepresentationRule, smif_types_IntersectionType, Type, smif_types_UnionType, smif_types_EntityType, smif_values_UnitValue, Value, smif_values_ScalarQuantity, UnitValue, smif_identifiers_UniqueIdentifier, Identifier, Namespace, smif_identifiers_IRIIdentifier, TechnicalIdentifier, smif_identifiers_Term, identifiers_Name, identifiers_UniqueTextIdentifier, smif_identifiers_UniqueTextIdentifier, smif_values_Value, smif_values_SystemOfUnits, Context, smif_values_StructuredValueType, values_ValueType, properties_PropertyOwnerType, smif_values_StructuredValue, values_Value, properties_PropertyOwner, smif_expressions_FunctionType, expressions_ExpressionContext, ExpressionNode, FunctionCall, smif_expressions_ConstantReference, smif_expressions_ExpressionNode, Evaluation, FunctionType, smif_expressions_FunctionCall, expressions_ExpressionNode, smif_expressions_Traversal, identifiers_UniqueIdentifier, identifiers_TextIdentifier, smif_identifiers_Identifier, IdentifiableEntity, smif_identifiers_Namespace, UniqueIdentifier, smif_identifiers_TextIdentifier, smif_identifiers_Name, TextIdentifier, smif_identifiers_TechnicalIdentifier, UniqueTextIdentifier, smif_relationships_Relationship, situations_ActualSituation, smif_relationships_RelationshipType, situations_SituationType, smif_constraints_Rule, Proposition, Rule, smif_constraints_MultiplicityConstraint, TypeConstraint, smif_expressions_ObjectOperationType, smif_expressions_Equality, smif_expressions_Evaluation, smif_expressions_ExpressionContext, smif_constraints_GeneralizationConstraint, smif_constraints_PropertyConstraint, smif_constraints_PropertyTransitivityConstraint, PropertyConstraint, smif_constraints_PropertyTypeConstraint, smif_constraints_CoveringConstraint, smif_constraints_FacetClassificationConstraint, smif_constraints_Conditional, smif_constraints_UniquenessConstraint, smif_constraints_ConditionalRule, constraints_Rule, constraints_Conditional, smif_constraints_TypeConstraint, smif_constraints_Equivalent, smif_constraints_Disjoint, smif_constraints_Enumerated, Metadata, Name, Record, InformationSource, PropertyBinding, smif_toplevel_Thing, ConstantReference, smif_toplevel_IdentifiableEntity, Statement, LexicalReference, smif_toplevel_Proposition, PropositionVariable, smif_toplevel_ActualEntity, TemporalEntity, smif_toplevel_TemporalEntity, smif_patterns_Pattern, PatternVariable, smif_patterns_PatternVariable, properties_OwnedPropertyType, Equality, smif_toplevel_Context, Mapping, smif_patterns_PropositionVariable, smif_patterns_ExpressionVariable, patterns_PatternVariable, patterns_Computed, smif_patterns_PartVariable, TypePatternVariable, smif_patterns_FocusVariable, smif_patterns_TypePatternVariable, smif_patterns_PatternOfType, smif_patterns_PatternMatch, ActualSituation, Pattern, smif_patterns_VariableBinding, OwnedPropertyBinding, smif_patterns_Computed, smif_mapping_MatchRule, smif_mapping_MatchEnd, MatchRule, smif_mapping_Mapping, patterns_Pattern, VariableBinding, Situation, smif_mapping_Facade, smif_mapping_ComputedFacade, Facade, smif_mapping_RepresentationRule, ConditionalRule, smif_lexicalscope_Model, Package, smif_lexicalscope_LexicalScope, smif_lexicalscope_LexicalReference, smif_lexicalscope_Package, Prefix, smif_lexicalscope_MOFPackage, smif_lexicalscope_LogicalPackage, smif_lexicalscope_PhysicalPackage, smif_lexicalscope_MappingPackage, smif_lexicalscope_Prefix, smif_associations_AssociationType, PropertyOwnerType, smif_associations_Association, smif_metadata_Statement, smif_metadata_InformationSource, metadata_Metadata, smif_metadata_Metadata, smif_lexicalscope_Include, IRIIdentifier, Term, smif_metadata_Definition, smif_properties_PropertyType, Traversal, ObjectOperationType, UniquenessConstraint, smif_properties_CharacteristicType, properties_PropertyType, smif_properties_CharacteristicBinding, properties_PropertyBinding, smif_properties_AnnotationProperty, CharacteristicType, smif_properties_OwnedPropertyType, smif_properties_PropertyOwnerType, smif_properties_OwnedPropertyBinding, smif_properties_PropertyOwner, smif_facets_FacetOfEntity, Relationship, smif_facets_Phase, facets_Facet, smif_facets_Role, Facet, smif_properties_PropertyBinding, smif_records_Record, smif_records_RecordType, smif_facets_Facet, smif_facets_Category, VariableQualification, AssertionStrength},
    associations={categorizes1, hasProperty2, assertsPattern3, hasCovering4, hasSpecialization5, hasMultiplicity6, propertiesOfType7, recordingTypes8, lexicalScope0, matchedBy18, unitReference19, definedWithinSystem20, hasGeneralization9, returnedBy11, respectOf12, assertedBy14, conceptRule15, representsRule16, uniqueWithin22, unitOfSystem21, implementedBy29, isUsedBy30, hasValue31, evaluatedBy33, implements34, calls35, identifies23, preferredFor24, scopesIdentifier26, names27, evaluatesIn45, resultingType46, constrains47, subsumes49, subsumedBy50, withRespectTo52, traversesThrough37, receiver39, hasEqual41, evaluates43, hasGeneral58, hasSpecific60, isOfType62, isCoveredBy64, multiplicityOf54, condition66, hasUnique56, definedBy70, identifiedBy72, hasMetadata74, hasName75, hasRecord76, constrainedBy77, hasAuthoritativeSource79, hasBinding80, definedIn81, inContextOf83, hasType85, statedBy87, referencedBy89, wasStatedIn68, hasPreferred69, asserts93, contextualizes94, negates96, contextualizesExpress98, referencedByLR100, holdsWithin101, negatedWithin103, qualifiedWithin105, ownsVariable106, satisfiedBy107, hasEquality90, boundIn91, mapsTo112, subsets114, excludedBy116, excludes118, referenceMapping120, concreteMapping121, qualifies123, subjectType125, hasOwningPattern109, hasSubset110, _unnamed_VariableBinding131, computation133, concreteEnd135, referenceEnd137, mapRuleOf139, assertedType141, mapsVariable143, matchFrom145, matchTo146, _unnamed_PatternMatch127, satisfies128, matches130, referenceFocus152, representedBy154, representedType156, defines158, references160, states162, referencedScope164, concreteFocus148, hasMapRule150, hasPrefix168, prefixOf169, statementDateAndTime170, version171, transactionId174, resultedIn177, madeStatement179, extendsScope166, externalReference183, externalTerm184, definesEntity186, metadataAbout181, binds188, boundBy190, boundTo192, propertyOf194, traversedBy196, receivedBy197, hasUniquenessConstraint198, hasBindingProperty199, about201, aboutType203},
    generalizations={gen_smif_types_Type_lexicalscope_LexicalScope, gen_smif_types_Type_toplevel_Context, gen_smif_situations_SituationType_EntityType, gen_smif_situations_Situation_toplevel_Proposition, gen_smif_situations_Situation_toplevel_TemporalEntity, gen_smif_situations_Situation_toplevel_Context, gen_smif_situations_Situation_lexicalscope_LexicalScope, gen_smif_situations_ActualSituation_toplevel_ActualEntity, gen_smif_situations_ActualSituation_situations_Situation, gen_smif_values_QuantityKind_ValueType, gen_smif_values_UnitType_ValueType, gen_smif_values_BaseUnitType_UnitType, gen_smif_types_IntersectionType_Type, gen_smif_types_UnionType_Type, gen_smif_types_EntityType_Type, gen_smif_values_UnitValue_Value, gen_smif_values_ScalarQuantity_UnitValue, gen_smif_identifiers_UniqueIdentifier_Identifier, gen_smif_identifiers_IRIIdentifier_TechnicalIdentifier, gen_smif_identifiers_Term_identifiers_Name, gen_smif_identifiers_Term_identifiers_UniqueTextIdentifier, gen_smif_values_ValueType_Type, gen_smif_values_Value_Thing, gen_smif_values_SystemOfUnits_Context, gen_smif_values_StructuredValueType_values_ValueType, gen_smif_values_StructuredValueType_properties_PropertyOwnerType, gen_smif_values_StructuredValue_values_Value, gen_smif_values_StructuredValue_properties_PropertyOwner, gen_smif_expressions_FunctionType_properties_PropertyOwnerType, gen_smif_expressions_FunctionType_expressions_ExpressionContext, gen_smif_expressions_ConstantReference_ExpressionNode, gen_smif_expressions_ExpressionNode_ExpressionContext, gen_smif_expressions_FunctionCall_expressions_ExpressionNode, gen_smif_expressions_FunctionCall_properties_PropertyOwner, gen_smif_expressions_Traversal_expressions_ExpressionNode, gen_smif_expressions_Traversal_properties_PropertyOwner, gen_smif_identifiers_UniqueTextIdentifier_identifiers_UniqueIdentifier, gen_smif_identifiers_UniqueTextIdentifier_identifiers_TextIdentifier, gen_smif_identifiers_Identifier_Value, gen_smif_identifiers_Namespace_Context, gen_smif_identifiers_TextIdentifier_Identifier, gen_smif_identifiers_Name_TextIdentifier, gen_smif_identifiers_TechnicalIdentifier_UniqueTextIdentifier, gen_smif_relationships_Relationship_situations_ActualSituation, gen_smif_relationships_Relationship_properties_PropertyOwner, gen_smif_relationships_RelationshipType_situations_SituationType, gen_smif_relationships_RelationshipType_properties_PropertyOwnerType, gen_smif_constraints_Rule_Proposition, gen_smif_constraints_MultiplicityConstraint_TypeConstraint, gen_smif_expressions_ObjectOperationType_FunctionType, gen_smif_expressions_Equality_ExpressionNode, gen_smif_expressions_Evaluation_ExpressionContext, gen_smif_expressions_ExpressionContext_IdentifiableEntity, gen_smif_constraints_GeneralizationConstraint_TypeConstraint, gen_smif_constraints_PropertyConstraint_Rule, gen_smif_constraints_PropertyTransitivityConstraint_PropertyConstraint, gen_smif_constraints_PropertyTypeConstraint_PropertyConstraint, gen_smif_constraints_CoveringConstraint_TypeConstraint, gen_smif_constraints_FacetClassificationConstraint_GeneralizationConstraint, gen_smif_constraints_UniquenessConstraint_TypeConstraint, gen_smif_constraints_ConditionalRule_constraints_Rule, gen_smif_constraints_ConditionalRule_constraints_Conditional, gen_smif_constraints_TypeConstraint_Rule, gen_smif_constraints_Equivalent_Rule, gen_smif_constraints_Disjoint_Rule, gen_smif_constraints_Enumerated_Rule, gen_smif_toplevel_IdentifiableEntity_Thing, gen_smif_toplevel_Proposition_IdentifiableEntity, gen_smif_toplevel_ActualEntity_TemporalEntity, gen_smif_toplevel_TemporalEntity_IdentifiableEntity, gen_smif_patterns_Pattern_situations_SituationType, gen_smif_patterns_Pattern_situations_Situation, gen_smif_patterns_Pattern_lexicalscope_LexicalScope, gen_smif_patterns_Pattern_properties_PropertyOwner, gen_smif_patterns_PatternVariable_properties_OwnedPropertyType, gen_smif_patterns_PatternVariable_constraints_Conditional, gen_smif_toplevel_Context_IdentifiableEntity, gen_smif_patterns_PropositionVariable_PatternVariable, gen_smif_patterns_ExpressionVariable_patterns_PatternVariable, gen_smif_patterns_ExpressionVariable_patterns_Computed, gen_smif_patterns_PartVariable_TypePatternVariable, gen_smif_patterns_FocusVariable_TypePatternVariable, gen_smif_patterns_TypePatternVariable_PatternVariable, gen_smif_patterns_PatternOfType_Pattern, gen_smif_patterns_PatternMatch_ActualSituation, gen_smif_patterns_VariableBinding_OwnedPropertyBinding, gen_smif_mapping_MatchRule_Rule, gen_smif_mapping_MatchEnd_constraints_Conditional, gen_smif_mapping_MatchEnd_patterns_Computed, gen_smif_mapping_Mapping_patterns_Pattern, gen_smif_mapping_Facade_RecordType, gen_smif_mapping_ComputedFacade_Facade, gen_smif_mapping_RepresentationRule_ConditionalRule, gen_smif_lexicalscope_Model_Package, gen_smif_lexicalscope_LexicalScope_Namespace, gen_smif_mapping_Mapping_constraints_Rule, gen_smif_lexicalscope_LexicalReference_Context, gen_smif_lexicalscope_Package_LexicalScope, gen_smif_lexicalscope_MOFPackage_Package, gen_smif_lexicalscope_LogicalPackage_Package, gen_smif_lexicalscope_PhysicalPackage_Package, gen_smif_lexicalscope_MappingPackage_Package, gen_smif_lexicalscope_Prefix_UniqueTextIdentifier, gen_smif_associations_AssociationType_PropertyOwnerType, gen_smif_associations_Association_properties_PropertyOwner, gen_smif_associations_Association_toplevel_Proposition, gen_smif_metadata_Statement_Metadata, gen_smif_metadata_InformationSource_toplevel_ActualEntity, gen_smif_metadata_InformationSource_metadata_Metadata, gen_smif_metadata_Metadata_Record, gen_smif_lexicalscope_Include_LexicalReference, gen_smif_metadata_Definition_Metadata, gen_smif_properties_PropertyType_Type, gen_smif_properties_CharacteristicType_properties_PropertyType, gen_smif_properties_CharacteristicType_situations_SituationType, gen_smif_properties_CharacteristicBinding_properties_PropertyBinding, gen_smif_properties_CharacteristicBinding_situations_ActualSituation, gen_smif_properties_AnnotationProperty_CharacteristicType, gen_smif_properties_OwnedPropertyType_PropertyType, gen_smif_properties_PropertyOwnerType_Type, gen_smif_properties_OwnedPropertyBinding_PropertyBinding, gen_smif_properties_PropertyOwner_Thing, gen_smif_facets_FacetOfEntity_Relationship, gen_smif_facets_Phase_facets_Facet, gen_smif_facets_Phase_situations_SituationType, gen_smif_facets_Role_Facet, gen_smif_properties_PropertyBinding_Thing, gen_smif_records_Record_situations_ActualSituation, gen_smif_records_Record_properties_PropertyOwner, gen_smif_records_RecordType_situations_SituationType, gen_smif_records_RecordType_properties_PropertyOwnerType, gen_smif_facets_Facet_Type, gen_smif_facets_Category_Facet},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)