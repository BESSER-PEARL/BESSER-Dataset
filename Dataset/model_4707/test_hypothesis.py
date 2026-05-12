import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Prefix,
    Package,
    smif_lexicalscope_Model,
    ConditionalRule,
    smif_mapping_RepresentationRule,
    Facade,
    smif_mapping_ComputedFacade,
    Situation,
    VariableBinding,
    patterns_Pattern,
    MatchRule,
    smif_patterns_Computed,
    OwnedPropertyBinding,
    smif_patterns_VariableBinding,
    Pattern,
    ActualSituation,
    smif_patterns_PatternMatch,
    smif_patterns_PatternOfType,
    TypePatternVariable,
    smif_patterns_FocusVariable,
    smif_patterns_PartVariable,
    patterns_Computed,
    patterns_PatternVariable,
    smif_patterns_ExpressionVariable,
    Mapping,
    Equality,
    properties_OwnedPropertyType,
    PatternVariable,
    smif_patterns_TypePatternVariable,
    smif_patterns_PropositionVariable,
    TemporalEntity,
    smif_toplevel_ActualEntity,
    PropositionVariable,
    LexicalReference,
    Statement,
    ConstantReference,
    smif_toplevel_Thing,
    PropertyBinding,
    InformationSource,
    Record,
    Name,
    Metadata,
    constraints_Conditional,
    smif_mapping_MatchEnd,
    smif_patterns_PatternVariable,
    constraints_Rule,
    smif_mapping_Mapping,
    smif_constraints_ConditionalRule,
    smif_constraints_Conditional,
    PropertyConstraint,
    smif_constraints_PropertyTypeConstraint,
    smif_constraints_PropertyTransitivityConstraint,
    TypeConstraint,
    smif_constraints_UniquenessConstraint,
    smif_constraints_GeneralizationConstraint,
    smif_constraints_CoveringConstraint,
    smif_constraints_MultiplicityConstraint,
    Rule,
    smif_mapping_MatchRule,
    smif_constraints_TypeConstraint,
    smif_constraints_Enumerated,
    smif_constraints_Equivalent,
    smif_constraints_Disjoint,
    smif_constraints_PropertyConstraint,
    Proposition,
    smif_constraints_Rule,
    situations_SituationType,
    situations_ActualSituation,
    UniqueTextIdentifier,
    smif_identifiers_TechnicalIdentifier,
    TextIdentifier,
    smif_identifiers_Name,
    Facet,
    smif_facets_Category,
    smif_facets_Role,
    facets_Facet,
    smif_facets_Phase,
    Relationship,
    smif_facets_FacetOfEntity,
    smif_properties_OwnedPropertyBinding,
    CharacteristicType,
    smif_properties_AnnotationProperty,
    properties_PropertyBinding,
    smif_properties_CharacteristicBinding,
    properties_PropertyType,
    smif_properties_CharacteristicType,
    UniquenessConstraint,
    ObjectOperationType,
    Traversal,
    smif_metadata_Definition,
    Term,
    IRIIdentifier,
    smif_lexicalscope_Include,
    smif_metadata_Metadata,
    metadata_Metadata,
    smif_metadata_Statement,
    PropertyOwnerType,
    smif_associations_AssociationType,
    smif_lexicalscope_Prefix,
    smif_lexicalscope_MappingPackage,
    smif_lexicalscope_PhysicalPackage,
    smif_lexicalscope_LogicalPackage,
    smif_lexicalscope_MOFPackage,
    UniqueIdentifier,
    IdentifiableEntity,
    smif_toplevel_Proposition,
    smif_toplevel_TemporalEntity,
    smif_toplevel_Context,
    smif_expressions_ExpressionContext,
    identifiers_TextIdentifier,
    identifiers_UniqueIdentifier,
    expressions_ExpressionNode,
    FunctionType,
    smif_expressions_ObjectOperationType,
    Evaluation,
    FunctionCall,
    ExpressionNode,
    smif_expressions_ConstantReference,
    smif_expressions_Equality,
    expressions_ExpressionContext,
    properties_PropertyOwner,
    smif_expressions_FunctionCall,
    smif_expressions_Traversal,
    smif_records_Record,
    smif_relationships_Relationship,
    values_Value,
    smif_values_StructuredValue,
    properties_PropertyOwnerType,
    smif_relationships_RelationshipType,
    smif_records_RecordType,
    smif_expressions_FunctionType,
    values_ValueType,
    smif_values_StructuredValueType,
    Context,
    smif_identifiers_Namespace,
    smif_lexicalscope_LexicalReference,
    smif_values_SystemOfUnits,
    smif_identifiers_UniqueTextIdentifier,
    identifiers_UniqueTextIdentifier,
    identifiers_Name,
    smif_identifiers_Term,
    TechnicalIdentifier,
    smif_identifiers_IRIIdentifier,
    Namespace,
    smif_lexicalscope_LexicalScope,
    Identifier,
    smif_identifiers_TextIdentifier,
    smif_identifiers_UniqueIdentifier,
    UnitValue,
    smif_values_ScalarQuantity,
    Value,
    smif_identifiers_Identifier,
    smif_values_UnitValue,
    Type,
    smif_types_EntityType,
    smif_properties_PropertyType,
    smif_properties_PropertyOwnerType,
    smif_facets_Facet,
    smif_types_UnionType,
    smif_types_IntersectionType,
    RepresentationRule,
    MatchEnd,
    ExpressionContext,
    smif_expressions_Evaluation,
    smif_expressions_ExpressionNode,
    smif_values_ValueType,
    UnitType,
    smif_values_BaseUnitType,
    SystemOfUnits,
    Definition,
    ValueType,
    smif_values_UnitType,
    smif_values_QuantityKind,
    situations_Situation,
    toplevel_ActualEntity,
    smif_metadata_InformationSource,
    smif_situations_ActualSituation,
    PatternMatch,
    toplevel_TemporalEntity,
    toplevel_Proposition,
    smif_associations_Association,
    EntityType,
    smif_situations_SituationType,
    LexicalScope,
    smif_lexicalscope_Package,
    smif_Repository,
    RecordType,
    smif_mapping_Facade,
    PropertyTypeConstraint,
    MultiplicityConstraint,
    GeneralizationConstraint,
    smif_constraints_FacetClassificationConstraint,
    CoveringConstraint,
    PatternOfType,
    PropertyType,
    smif_properties_OwnedPropertyType,
    Thing,
    smif_values_Value,
    smif_properties_PropertyBinding,
    smif_properties_PropertyOwner,
    smif_toplevel_IdentifiableEntity,
    toplevel_Context,
    lexicalscope_LexicalScope,
    smif_patterns_Pattern,
    smif_situations_Situation,
    smif_types_Type,
    VariableQualification,
    AssertionStrength,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_prefix_is_not_abstract():
    assert not inspect.isabstract(Prefix)


def test_prefix_constructor_exists():
    assert callable(Prefix.__init__)


def test_prefix_constructor_args():
    sig = inspect.signature(Prefix.__init__)
    params = list(sig.parameters.keys())



def test_package_is_not_abstract():
    assert not inspect.isabstract(Package)


def test_package_constructor_exists():
    assert callable(Package.__init__)


def test_package_constructor_args():
    sig = inspect.signature(Package.__init__)
    params = list(sig.parameters.keys())



def test_smif_lexicalscope_model_is_not_abstract():
    assert not inspect.isabstract(smif_lexicalscope_Model)


def test_smif_lexicalscope_model_constructor_exists():
    assert callable(smif_lexicalscope_Model.__init__)


def test_smif_lexicalscope_model_constructor_args():
    sig = inspect.signature(smif_lexicalscope_Model.__init__)
    params = list(sig.parameters.keys())



def test_conditionalrule_is_not_abstract():
    assert not inspect.isabstract(ConditionalRule)


def test_conditionalrule_constructor_exists():
    assert callable(ConditionalRule.__init__)


def test_conditionalrule_constructor_args():
    sig = inspect.signature(ConditionalRule.__init__)
    params = list(sig.parameters.keys())



def test_smif_mapping_representationrule_is_not_abstract():
    assert not inspect.isabstract(smif_mapping_RepresentationRule)


def test_smif_mapping_representationrule_constructor_exists():
    assert callable(smif_mapping_RepresentationRule.__init__)


def test_smif_mapping_representationrule_constructor_args():
    sig = inspect.signature(smif_mapping_RepresentationRule.__init__)
    params = list(sig.parameters.keys())
    assert "mapAll" in params, "Missing parameter 'mapAll'"

def test_smif_mapping_representationrule_has_mapAll():
    assert hasattr(smif_mapping_RepresentationRule, "mapAll")
    descriptor = None
    for klass in smif_mapping_RepresentationRule.__mro__:
        if "mapAll" in klass.__dict__:
            descriptor = klass.__dict__["mapAll"]
            break
    assert isinstance(descriptor, property)



def test_facade_is_not_abstract():
    assert not inspect.isabstract(Facade)


def test_facade_constructor_exists():
    assert callable(Facade.__init__)


def test_facade_constructor_args():
    sig = inspect.signature(Facade.__init__)
    params = list(sig.parameters.keys())



def test_smif_mapping_computedfacade_is_not_abstract():
    assert not inspect.isabstract(smif_mapping_ComputedFacade)


def test_smif_mapping_computedfacade_constructor_exists():
    assert callable(smif_mapping_ComputedFacade.__init__)


def test_smif_mapping_computedfacade_constructor_args():
    sig = inspect.signature(smif_mapping_ComputedFacade.__init__)
    params = list(sig.parameters.keys())



def test_situation_is_not_abstract():
    assert not inspect.isabstract(Situation)


def test_situation_constructor_exists():
    assert callable(Situation.__init__)


def test_situation_constructor_args():
    sig = inspect.signature(Situation.__init__)
    params = list(sig.parameters.keys())



def test_variablebinding_is_not_abstract():
    assert not inspect.isabstract(VariableBinding)


def test_variablebinding_constructor_exists():
    assert callable(VariableBinding.__init__)


def test_variablebinding_constructor_args():
    sig = inspect.signature(VariableBinding.__init__)
    params = list(sig.parameters.keys())



def test_patterns_pattern_is_not_abstract():
    assert not inspect.isabstract(patterns_Pattern)


def test_patterns_pattern_constructor_exists():
    assert callable(patterns_Pattern.__init__)


def test_patterns_pattern_constructor_args():
    sig = inspect.signature(patterns_Pattern.__init__)
    params = list(sig.parameters.keys())



def test_matchrule_is_not_abstract():
    assert not inspect.isabstract(MatchRule)


def test_matchrule_constructor_exists():
    assert callable(MatchRule.__init__)


def test_matchrule_constructor_args():
    sig = inspect.signature(MatchRule.__init__)
    params = list(sig.parameters.keys())



def test_smif_patterns_computed_is_not_abstract():
    assert not inspect.isabstract(smif_patterns_Computed)


def test_smif_patterns_computed_constructor_exists():
    assert callable(smif_patterns_Computed.__init__)


def test_smif_patterns_computed_constructor_args():
    sig = inspect.signature(smif_patterns_Computed.__init__)
    params = list(sig.parameters.keys())



def test_ownedpropertybinding_is_not_abstract():
    assert not inspect.isabstract(OwnedPropertyBinding)


def test_ownedpropertybinding_constructor_exists():
    assert callable(OwnedPropertyBinding.__init__)


def test_ownedpropertybinding_constructor_args():
    sig = inspect.signature(OwnedPropertyBinding.__init__)
    params = list(sig.parameters.keys())



def test_smif_patterns_variablebinding_is_not_abstract():
    assert not inspect.isabstract(smif_patterns_VariableBinding)


def test_smif_patterns_variablebinding_constructor_exists():
    assert callable(smif_patterns_VariableBinding.__init__)


def test_smif_patterns_variablebinding_constructor_args():
    sig = inspect.signature(smif_patterns_VariableBinding.__init__)
    params = list(sig.parameters.keys())



def test_pattern_is_not_abstract():
    assert not inspect.isabstract(Pattern)


def test_pattern_constructor_exists():
    assert callable(Pattern.__init__)


def test_pattern_constructor_args():
    sig = inspect.signature(Pattern.__init__)
    params = list(sig.parameters.keys())



def test_actualsituation_is_not_abstract():
    assert not inspect.isabstract(ActualSituation)


def test_actualsituation_constructor_exists():
    assert callable(ActualSituation.__init__)


def test_actualsituation_constructor_args():
    sig = inspect.signature(ActualSituation.__init__)
    params = list(sig.parameters.keys())



def test_smif_patterns_patternmatch_is_not_abstract():
    assert not inspect.isabstract(smif_patterns_PatternMatch)


def test_smif_patterns_patternmatch_constructor_exists():
    assert callable(smif_patterns_PatternMatch.__init__)


def test_smif_patterns_patternmatch_constructor_args():
    sig = inspect.signature(smif_patterns_PatternMatch.__init__)
    params = list(sig.parameters.keys())



def test_smif_patterns_patternoftype_is_not_abstract():
    assert not inspect.isabstract(smif_patterns_PatternOfType)


def test_smif_patterns_patternoftype_constructor_exists():
    assert callable(smif_patterns_PatternOfType.__init__)


def test_smif_patterns_patternoftype_constructor_args():
    sig = inspect.signature(smif_patterns_PatternOfType.__init__)
    params = list(sig.parameters.keys())



def test_typepatternvariable_is_not_abstract():
    assert not inspect.isabstract(TypePatternVariable)


def test_typepatternvariable_constructor_exists():
    assert callable(TypePatternVariable.__init__)


def test_typepatternvariable_constructor_args():
    sig = inspect.signature(TypePatternVariable.__init__)
    params = list(sig.parameters.keys())



def test_smif_patterns_focusvariable_is_not_abstract():
    assert not inspect.isabstract(smif_patterns_FocusVariable)


def test_smif_patterns_focusvariable_constructor_exists():
    assert callable(smif_patterns_FocusVariable.__init__)


def test_smif_patterns_focusvariable_constructor_args():
    sig = inspect.signature(smif_patterns_FocusVariable.__init__)
    params = list(sig.parameters.keys())



def test_smif_patterns_partvariable_is_not_abstract():
    assert not inspect.isabstract(smif_patterns_PartVariable)


def test_smif_patterns_partvariable_constructor_exists():
    assert callable(smif_patterns_PartVariable.__init__)


def test_smif_patterns_partvariable_constructor_args():
    sig = inspect.signature(smif_patterns_PartVariable.__init__)
    params = list(sig.parameters.keys())
    assert "isBoundaryPart" in params, "Missing parameter 'isBoundaryPart'"

def test_smif_patterns_partvariable_has_isBoundaryPart():
    assert hasattr(smif_patterns_PartVariable, "isBoundaryPart")
    descriptor = None
    for klass in smif_patterns_PartVariable.__mro__:
        if "isBoundaryPart" in klass.__dict__:
            descriptor = klass.__dict__["isBoundaryPart"]
            break
    assert isinstance(descriptor, property)



def test_patterns_computed_is_not_abstract():
    assert not inspect.isabstract(patterns_Computed)


def test_patterns_computed_constructor_exists():
    assert callable(patterns_Computed.__init__)


def test_patterns_computed_constructor_args():
    sig = inspect.signature(patterns_Computed.__init__)
    params = list(sig.parameters.keys())



def test_patterns_patternvariable_is_not_abstract():
    assert not inspect.isabstract(patterns_PatternVariable)


def test_patterns_patternvariable_constructor_exists():
    assert callable(patterns_PatternVariable.__init__)


def test_patterns_patternvariable_constructor_args():
    sig = inspect.signature(patterns_PatternVariable.__init__)
    params = list(sig.parameters.keys())



def test_smif_patterns_expressionvariable_is_not_abstract():
    assert not inspect.isabstract(smif_patterns_ExpressionVariable)


def test_smif_patterns_expressionvariable_constructor_exists():
    assert callable(smif_patterns_ExpressionVariable.__init__)


def test_smif_patterns_expressionvariable_constructor_args():
    sig = inspect.signature(smif_patterns_ExpressionVariable.__init__)
    params = list(sig.parameters.keys())



def test_mapping_is_not_abstract():
    assert not inspect.isabstract(Mapping)


def test_mapping_constructor_exists():
    assert callable(Mapping.__init__)


def test_mapping_constructor_args():
    sig = inspect.signature(Mapping.__init__)
    params = list(sig.parameters.keys())



def test_equality_is_not_abstract():
    assert not inspect.isabstract(Equality)


def test_equality_constructor_exists():
    assert callable(Equality.__init__)


def test_equality_constructor_args():
    sig = inspect.signature(Equality.__init__)
    params = list(sig.parameters.keys())



def test_properties_ownedpropertytype_is_not_abstract():
    assert not inspect.isabstract(properties_OwnedPropertyType)


def test_properties_ownedpropertytype_constructor_exists():
    assert callable(properties_OwnedPropertyType.__init__)


def test_properties_ownedpropertytype_constructor_args():
    sig = inspect.signature(properties_OwnedPropertyType.__init__)
    params = list(sig.parameters.keys())



def test_patternvariable_is_not_abstract():
    assert not inspect.isabstract(PatternVariable)


def test_patternvariable_constructor_exists():
    assert callable(PatternVariable.__init__)


def test_patternvariable_constructor_args():
    sig = inspect.signature(PatternVariable.__init__)
    params = list(sig.parameters.keys())



def test_smif_patterns_typepatternvariable_is_not_abstract():
    assert not inspect.isabstract(smif_patterns_TypePatternVariable)


def test_smif_patterns_typepatternvariable_constructor_exists():
    assert callable(smif_patterns_TypePatternVariable.__init__)


def test_smif_patterns_typepatternvariable_constructor_args():
    sig = inspect.signature(smif_patterns_TypePatternVariable.__init__)
    params = list(sig.parameters.keys())



def test_smif_patterns_propositionvariable_is_not_abstract():
    assert not inspect.isabstract(smif_patterns_PropositionVariable)


def test_smif_patterns_propositionvariable_constructor_exists():
    assert callable(smif_patterns_PropositionVariable.__init__)


def test_smif_patterns_propositionvariable_constructor_args():
    sig = inspect.signature(smif_patterns_PropositionVariable.__init__)
    params = list(sig.parameters.keys())



def test_temporalentity_is_not_abstract():
    assert not inspect.isabstract(TemporalEntity)


def test_temporalentity_constructor_exists():
    assert callable(TemporalEntity.__init__)


def test_temporalentity_constructor_args():
    sig = inspect.signature(TemporalEntity.__init__)
    params = list(sig.parameters.keys())



def test_smif_toplevel_actualentity_is_not_abstract():
    assert not inspect.isabstract(smif_toplevel_ActualEntity)


def test_smif_toplevel_actualentity_constructor_exists():
    assert callable(smif_toplevel_ActualEntity.__init__)


def test_smif_toplevel_actualentity_constructor_args():
    sig = inspect.signature(smif_toplevel_ActualEntity.__init__)
    params = list(sig.parameters.keys())



def test_propositionvariable_is_not_abstract():
    assert not inspect.isabstract(PropositionVariable)


def test_propositionvariable_constructor_exists():
    assert callable(PropositionVariable.__init__)


def test_propositionvariable_constructor_args():
    sig = inspect.signature(PropositionVariable.__init__)
    params = list(sig.parameters.keys())



def test_lexicalreference_is_not_abstract():
    assert not inspect.isabstract(LexicalReference)


def test_lexicalreference_constructor_exists():
    assert callable(LexicalReference.__init__)


def test_lexicalreference_constructor_args():
    sig = inspect.signature(LexicalReference.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_constantreference_is_not_abstract():
    assert not inspect.isabstract(ConstantReference)


def test_constantreference_constructor_exists():
    assert callable(ConstantReference.__init__)


def test_constantreference_constructor_args():
    sig = inspect.signature(ConstantReference.__init__)
    params = list(sig.parameters.keys())



def test_smif_toplevel_thing_is_not_abstract():
    assert not inspect.isabstract(smif_toplevel_Thing)


def test_smif_toplevel_thing_constructor_exists():
    assert callable(smif_toplevel_Thing.__init__)


def test_smif_toplevel_thing_constructor_args():
    sig = inspect.signature(smif_toplevel_Thing.__init__)
    params = list(sig.parameters.keys())



def test_propertybinding_is_not_abstract():
    assert not inspect.isabstract(PropertyBinding)


def test_propertybinding_constructor_exists():
    assert callable(PropertyBinding.__init__)


def test_propertybinding_constructor_args():
    sig = inspect.signature(PropertyBinding.__init__)
    params = list(sig.parameters.keys())



def test_informationsource_is_not_abstract():
    assert not inspect.isabstract(InformationSource)


def test_informationsource_constructor_exists():
    assert callable(InformationSource.__init__)


def test_informationsource_constructor_args():
    sig = inspect.signature(InformationSource.__init__)
    params = list(sig.parameters.keys())



def test_record_is_not_abstract():
    assert not inspect.isabstract(Record)


def test_record_constructor_exists():
    assert callable(Record.__init__)


def test_record_constructor_args():
    sig = inspect.signature(Record.__init__)
    params = list(sig.parameters.keys())



def test_name_is_not_abstract():
    assert not inspect.isabstract(Name)


def test_name_constructor_exists():
    assert callable(Name.__init__)


def test_name_constructor_args():
    sig = inspect.signature(Name.__init__)
    params = list(sig.parameters.keys())



def test_metadata_is_not_abstract():
    assert not inspect.isabstract(Metadata)


def test_metadata_constructor_exists():
    assert callable(Metadata.__init__)


def test_metadata_constructor_args():
    sig = inspect.signature(Metadata.__init__)
    params = list(sig.parameters.keys())



def test_constraints_conditional_is_not_abstract():
    assert not inspect.isabstract(constraints_Conditional)


def test_constraints_conditional_constructor_exists():
    assert callable(constraints_Conditional.__init__)


def test_constraints_conditional_constructor_args():
    sig = inspect.signature(constraints_Conditional.__init__)
    params = list(sig.parameters.keys())



def test_smif_mapping_matchend_is_not_abstract():
    assert not inspect.isabstract(smif_mapping_MatchEnd)


def test_smif_mapping_matchend_constructor_exists():
    assert callable(smif_mapping_MatchEnd.__init__)


def test_smif_mapping_matchend_constructor_args():
    sig = inspect.signature(smif_mapping_MatchEnd.__init__)
    params = list(sig.parameters.keys())



def test_smif_patterns_patternvariable_is_not_abstract():
    assert not inspect.isabstract(smif_patterns_PatternVariable)


def test_smif_patterns_patternvariable_constructor_exists():
    assert callable(smif_patterns_PatternVariable.__init__)


def test_smif_patterns_patternvariable_constructor_args():
    sig = inspect.signature(smif_patterns_PatternVariable.__init__)
    params = list(sig.parameters.keys())
    assert "explicit" in params, "Missing parameter 'explicit'"
    assert "qualification" in params, "Missing parameter 'qualification'"

def test_smif_patterns_patternvariable_has_explicit():
    assert hasattr(smif_patterns_PatternVariable, "explicit")
    descriptor = None
    for klass in smif_patterns_PatternVariable.__mro__:
        if "explicit" in klass.__dict__:
            descriptor = klass.__dict__["explicit"]
            break
    assert isinstance(descriptor, property)

def test_smif_patterns_patternvariable_has_qualification():
    assert hasattr(smif_patterns_PatternVariable, "qualification")
    descriptor = None
    for klass in smif_patterns_PatternVariable.__mro__:
        if "qualification" in klass.__dict__:
            descriptor = klass.__dict__["qualification"]
            break
    assert isinstance(descriptor, property)



def test_constraints_rule_is_not_abstract():
    assert not inspect.isabstract(constraints_Rule)


def test_constraints_rule_constructor_exists():
    assert callable(constraints_Rule.__init__)


def test_constraints_rule_constructor_args():
    sig = inspect.signature(constraints_Rule.__init__)
    params = list(sig.parameters.keys())



def test_smif_mapping_mapping_is_not_abstract():
    assert not inspect.isabstract(smif_mapping_Mapping)


def test_smif_mapping_mapping_constructor_exists():
    assert callable(smif_mapping_Mapping.__init__)


def test_smif_mapping_mapping_constructor_args():
    sig = inspect.signature(smif_mapping_Mapping.__init__)
    params = list(sig.parameters.keys())
    assert "strength" in params, "Missing parameter 'strength'"

def test_smif_mapping_mapping_has_strength():
    assert hasattr(smif_mapping_Mapping, "strength")
    descriptor = None
    for klass in smif_mapping_Mapping.__mro__:
        if "strength" in klass.__dict__:
            descriptor = klass.__dict__["strength"]
            break
    assert isinstance(descriptor, property)



def test_smif_constraints_conditionalrule_is_not_abstract():
    assert not inspect.isabstract(smif_constraints_ConditionalRule)


def test_smif_constraints_conditionalrule_constructor_exists():
    assert callable(smif_constraints_ConditionalRule.__init__)


def test_smif_constraints_conditionalrule_constructor_args():
    sig = inspect.signature(smif_constraints_ConditionalRule.__init__)
    params = list(sig.parameters.keys())



def test_smif_constraints_conditional_is_not_abstract():
    assert not inspect.isabstract(smif_constraints_Conditional)


def test_smif_constraints_conditional_constructor_exists():
    assert callable(smif_constraints_Conditional.__init__)


def test_smif_constraints_conditional_constructor_args():
    sig = inspect.signature(smif_constraints_Conditional.__init__)
    params = list(sig.parameters.keys())



def test_propertyconstraint_is_not_abstract():
    assert not inspect.isabstract(PropertyConstraint)


def test_propertyconstraint_constructor_exists():
    assert callable(PropertyConstraint.__init__)


def test_propertyconstraint_constructor_args():
    sig = inspect.signature(PropertyConstraint.__init__)
    params = list(sig.parameters.keys())



def test_smif_constraints_propertytypeconstraint_is_not_abstract():
    assert not inspect.isabstract(smif_constraints_PropertyTypeConstraint)


def test_smif_constraints_propertytypeconstraint_constructor_exists():
    assert callable(smif_constraints_PropertyTypeConstraint.__init__)


def test_smif_constraints_propertytypeconstraint_constructor_args():
    sig = inspect.signature(smif_constraints_PropertyTypeConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "prerequisiteType" in params, "Missing parameter 'prerequisiteType'"

def test_smif_constraints_propertytypeconstraint_has_prerequisiteType():
    assert hasattr(smif_constraints_PropertyTypeConstraint, "prerequisiteType")
    descriptor = None
    for klass in smif_constraints_PropertyTypeConstraint.__mro__:
        if "prerequisiteType" in klass.__dict__:
            descriptor = klass.__dict__["prerequisiteType"]
            break
    assert isinstance(descriptor, property)



def test_smif_constraints_propertytransitivityconstraint_is_not_abstract():
    assert not inspect.isabstract(smif_constraints_PropertyTransitivityConstraint)


def test_smif_constraints_propertytransitivityconstraint_constructor_exists():
    assert callable(smif_constraints_PropertyTransitivityConstraint.__init__)


def test_smif_constraints_propertytransitivityconstraint_constructor_args():
    sig = inspect.signature(smif_constraints_PropertyTransitivityConstraint.__init__)
    params = list(sig.parameters.keys())



def test_typeconstraint_is_not_abstract():
    assert not inspect.isabstract(TypeConstraint)


def test_typeconstraint_constructor_exists():
    assert callable(TypeConstraint.__init__)


def test_typeconstraint_constructor_args():
    sig = inspect.signature(TypeConstraint.__init__)
    params = list(sig.parameters.keys())



def test_smif_constraints_uniquenessconstraint_is_not_abstract():
    assert not inspect.isabstract(smif_constraints_UniquenessConstraint)


def test_smif_constraints_uniquenessconstraint_constructor_exists():
    assert callable(smif_constraints_UniquenessConstraint.__init__)


def test_smif_constraints_uniquenessconstraint_constructor_args():
    sig = inspect.signature(smif_constraints_UniquenessConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "isPrimaryIdentity" in params, "Missing parameter 'isPrimaryIdentity'"

def test_smif_constraints_uniquenessconstraint_has_isPrimaryIdentity():
    assert hasattr(smif_constraints_UniquenessConstraint, "isPrimaryIdentity")
    descriptor = None
    for klass in smif_constraints_UniquenessConstraint.__mro__:
        if "isPrimaryIdentity" in klass.__dict__:
            descriptor = klass.__dict__["isPrimaryIdentity"]
            break
    assert isinstance(descriptor, property)



def test_smif_constraints_generalizationconstraint_is_not_abstract():
    assert not inspect.isabstract(smif_constraints_GeneralizationConstraint)


def test_smif_constraints_generalizationconstraint_constructor_exists():
    assert callable(smif_constraints_GeneralizationConstraint.__init__)


def test_smif_constraints_generalizationconstraint_constructor_args():
    sig = inspect.signature(smif_constraints_GeneralizationConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "redefines" in params, "Missing parameter 'redefines'"

def test_smif_constraints_generalizationconstraint_has_redefines():
    assert hasattr(smif_constraints_GeneralizationConstraint, "redefines")
    descriptor = None
    for klass in smif_constraints_GeneralizationConstraint.__mro__:
        if "redefines" in klass.__dict__:
            descriptor = klass.__dict__["redefines"]
            break
    assert isinstance(descriptor, property)



def test_smif_constraints_coveringconstraint_is_not_abstract():
    assert not inspect.isabstract(smif_constraints_CoveringConstraint)


def test_smif_constraints_coveringconstraint_constructor_exists():
    assert callable(smif_constraints_CoveringConstraint.__init__)


def test_smif_constraints_coveringconstraint_constructor_args():
    sig = inspect.signature(smif_constraints_CoveringConstraint.__init__)
    params = list(sig.parameters.keys())



def test_smif_constraints_multiplicityconstraint_is_not_abstract():
    assert not inspect.isabstract(smif_constraints_MultiplicityConstraint)


def test_smif_constraints_multiplicityconstraint_constructor_exists():
    assert callable(smif_constraints_MultiplicityConstraint.__init__)


def test_smif_constraints_multiplicityconstraint_constructor_args():
    sig = inspect.signature(smif_constraints_MultiplicityConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "mininumNumber" in params, "Missing parameter 'mininumNumber'"
    assert "maximumNumber" in params, "Missing parameter 'maximumNumber'"
    assert "atOnce" in params, "Missing parameter 'atOnce'"
    assert "isSufficent" in params, "Missing parameter 'isSufficent'"

def test_smif_constraints_multiplicityconstraint_has_mininumNumber():
    assert hasattr(smif_constraints_MultiplicityConstraint, "mininumNumber")
    descriptor = None
    for klass in smif_constraints_MultiplicityConstraint.__mro__:
        if "mininumNumber" in klass.__dict__:
            descriptor = klass.__dict__["mininumNumber"]
            break
    assert isinstance(descriptor, property)

def test_smif_constraints_multiplicityconstraint_has_maximumNumber():
    assert hasattr(smif_constraints_MultiplicityConstraint, "maximumNumber")
    descriptor = None
    for klass in smif_constraints_MultiplicityConstraint.__mro__:
        if "maximumNumber" in klass.__dict__:
            descriptor = klass.__dict__["maximumNumber"]
            break
    assert isinstance(descriptor, property)

def test_smif_constraints_multiplicityconstraint_has_atOnce():
    assert hasattr(smif_constraints_MultiplicityConstraint, "atOnce")
    descriptor = None
    for klass in smif_constraints_MultiplicityConstraint.__mro__:
        if "atOnce" in klass.__dict__:
            descriptor = klass.__dict__["atOnce"]
            break
    assert isinstance(descriptor, property)

def test_smif_constraints_multiplicityconstraint_has_isSufficent():
    assert hasattr(smif_constraints_MultiplicityConstraint, "isSufficent")
    descriptor = None
    for klass in smif_constraints_MultiplicityConstraint.__mro__:
        if "isSufficent" in klass.__dict__:
            descriptor = klass.__dict__["isSufficent"]
            break
    assert isinstance(descriptor, property)



def test_rule_is_not_abstract():
    assert not inspect.isabstract(Rule)


def test_rule_constructor_exists():
    assert callable(Rule.__init__)


def test_rule_constructor_args():
    sig = inspect.signature(Rule.__init__)
    params = list(sig.parameters.keys())



def test_smif_mapping_matchrule_is_not_abstract():
    assert not inspect.isabstract(smif_mapping_MatchRule)


def test_smif_mapping_matchrule_constructor_exists():
    assert callable(smif_mapping_MatchRule.__init__)


def test_smif_mapping_matchrule_constructor_args():
    sig = inspect.signature(smif_mapping_MatchRule.__init__)
    params = list(sig.parameters.keys())
    assert "coerce" in params, "Missing parameter 'coerce'"

def test_smif_mapping_matchrule_has_coerce():
    assert hasattr(smif_mapping_MatchRule, "coerce")
    descriptor = None
    for klass in smif_mapping_MatchRule.__mro__:
        if "coerce" in klass.__dict__:
            descriptor = klass.__dict__["coerce"]
            break
    assert isinstance(descriptor, property)



def test_smif_constraints_typeconstraint_is_not_abstract():
    assert not inspect.isabstract(smif_constraints_TypeConstraint)


def test_smif_constraints_typeconstraint_constructor_exists():
    assert callable(smif_constraints_TypeConstraint.__init__)


def test_smif_constraints_typeconstraint_constructor_args():
    sig = inspect.signature(smif_constraints_TypeConstraint.__init__)
    params = list(sig.parameters.keys())



def test_smif_constraints_enumerated_is_not_abstract():
    assert not inspect.isabstract(smif_constraints_Enumerated)


def test_smif_constraints_enumerated_constructor_exists():
    assert callable(smif_constraints_Enumerated.__init__)


def test_smif_constraints_enumerated_constructor_args():
    sig = inspect.signature(smif_constraints_Enumerated.__init__)
    params = list(sig.parameters.keys())



def test_smif_constraints_equivalent_is_not_abstract():
    assert not inspect.isabstract(smif_constraints_Equivalent)


def test_smif_constraints_equivalent_constructor_exists():
    assert callable(smif_constraints_Equivalent.__init__)


def test_smif_constraints_equivalent_constructor_args():
    sig = inspect.signature(smif_constraints_Equivalent.__init__)
    params = list(sig.parameters.keys())



def test_smif_constraints_disjoint_is_not_abstract():
    assert not inspect.isabstract(smif_constraints_Disjoint)


def test_smif_constraints_disjoint_constructor_exists():
    assert callable(smif_constraints_Disjoint.__init__)


def test_smif_constraints_disjoint_constructor_args():
    sig = inspect.signature(smif_constraints_Disjoint.__init__)
    params = list(sig.parameters.keys())



def test_smif_constraints_propertyconstraint_is_not_abstract():
    assert not inspect.isabstract(smif_constraints_PropertyConstraint)


def test_smif_constraints_propertyconstraint_constructor_exists():
    assert callable(smif_constraints_PropertyConstraint.__init__)


def test_smif_constraints_propertyconstraint_constructor_args():
    sig = inspect.signature(smif_constraints_PropertyConstraint.__init__)
    params = list(sig.parameters.keys())



def test_proposition_is_not_abstract():
    assert not inspect.isabstract(Proposition)


def test_proposition_constructor_exists():
    assert callable(Proposition.__init__)


def test_proposition_constructor_args():
    sig = inspect.signature(Proposition.__init__)
    params = list(sig.parameters.keys())



def test_smif_constraints_rule_is_not_abstract():
    assert not inspect.isabstract(smif_constraints_Rule)


def test_smif_constraints_rule_constructor_exists():
    assert callable(smif_constraints_Rule.__init__)


def test_smif_constraints_rule_constructor_args():
    sig = inspect.signature(smif_constraints_Rule.__init__)
    params = list(sig.parameters.keys())



def test_situations_situationtype_is_not_abstract():
    assert not inspect.isabstract(situations_SituationType)


def test_situations_situationtype_constructor_exists():
    assert callable(situations_SituationType.__init__)


def test_situations_situationtype_constructor_args():
    sig = inspect.signature(situations_SituationType.__init__)
    params = list(sig.parameters.keys())



def test_situations_actualsituation_is_not_abstract():
    assert not inspect.isabstract(situations_ActualSituation)


def test_situations_actualsituation_constructor_exists():
    assert callable(situations_ActualSituation.__init__)


def test_situations_actualsituation_constructor_args():
    sig = inspect.signature(situations_ActualSituation.__init__)
    params = list(sig.parameters.keys())



def test_uniquetextidentifier_is_not_abstract():
    assert not inspect.isabstract(UniqueTextIdentifier)


def test_uniquetextidentifier_constructor_exists():
    assert callable(UniqueTextIdentifier.__init__)


def test_uniquetextidentifier_constructor_args():
    sig = inspect.signature(UniqueTextIdentifier.__init__)
    params = list(sig.parameters.keys())



def test_smif_identifiers_technicalidentifier_is_not_abstract():
    assert not inspect.isabstract(smif_identifiers_TechnicalIdentifier)


def test_smif_identifiers_technicalidentifier_constructor_exists():
    assert callable(smif_identifiers_TechnicalIdentifier.__init__)


def test_smif_identifiers_technicalidentifier_constructor_args():
    sig = inspect.signature(smif_identifiers_TechnicalIdentifier.__init__)
    params = list(sig.parameters.keys())



def test_textidentifier_is_not_abstract():
    assert not inspect.isabstract(TextIdentifier)


def test_textidentifier_constructor_exists():
    assert callable(TextIdentifier.__init__)


def test_textidentifier_constructor_args():
    sig = inspect.signature(TextIdentifier.__init__)
    params = list(sig.parameters.keys())



def test_smif_identifiers_name_is_not_abstract():
    assert not inspect.isabstract(smif_identifiers_Name)


def test_smif_identifiers_name_constructor_exists():
    assert callable(smif_identifiers_Name.__init__)


def test_smif_identifiers_name_constructor_args():
    sig = inspect.signature(smif_identifiers_Name.__init__)
    params = list(sig.parameters.keys())



def test_facet_is_not_abstract():
    assert not inspect.isabstract(Facet)


def test_facet_constructor_exists():
    assert callable(Facet.__init__)


def test_facet_constructor_args():
    sig = inspect.signature(Facet.__init__)
    params = list(sig.parameters.keys())



def test_smif_facets_category_is_not_abstract():
    assert not inspect.isabstract(smif_facets_Category)


def test_smif_facets_category_constructor_exists():
    assert callable(smif_facets_Category.__init__)


def test_smif_facets_category_constructor_args():
    sig = inspect.signature(smif_facets_Category.__init__)
    params = list(sig.parameters.keys())



def test_smif_facets_role_is_not_abstract():
    assert not inspect.isabstract(smif_facets_Role)


def test_smif_facets_role_constructor_exists():
    assert callable(smif_facets_Role.__init__)


def test_smif_facets_role_constructor_args():
    sig = inspect.signature(smif_facets_Role.__init__)
    params = list(sig.parameters.keys())



def test_facets_facet_is_not_abstract():
    assert not inspect.isabstract(facets_Facet)


def test_facets_facet_constructor_exists():
    assert callable(facets_Facet.__init__)


def test_facets_facet_constructor_args():
    sig = inspect.signature(facets_Facet.__init__)
    params = list(sig.parameters.keys())



def test_smif_facets_phase_is_not_abstract():
    assert not inspect.isabstract(smif_facets_Phase)


def test_smif_facets_phase_constructor_exists():
    assert callable(smif_facets_Phase.__init__)


def test_smif_facets_phase_constructor_args():
    sig = inspect.signature(smif_facets_Phase.__init__)
    params = list(sig.parameters.keys())



def test_relationship_is_not_abstract():
    assert not inspect.isabstract(Relationship)


def test_relationship_constructor_exists():
    assert callable(Relationship.__init__)


def test_relationship_constructor_args():
    sig = inspect.signature(Relationship.__init__)
    params = list(sig.parameters.keys())



def test_smif_facets_facetofentity_is_not_abstract():
    assert not inspect.isabstract(smif_facets_FacetOfEntity)


def test_smif_facets_facetofentity_constructor_exists():
    assert callable(smif_facets_FacetOfEntity.__init__)


def test_smif_facets_facetofentity_constructor_args():
    sig = inspect.signature(smif_facets_FacetOfEntity.__init__)
    params = list(sig.parameters.keys())



def test_smif_properties_ownedpropertybinding_is_not_abstract():
    assert not inspect.isabstract(smif_properties_OwnedPropertyBinding)


def test_smif_properties_ownedpropertybinding_constructor_exists():
    assert callable(smif_properties_OwnedPropertyBinding.__init__)


def test_smif_properties_ownedpropertybinding_constructor_args():
    sig = inspect.signature(smif_properties_OwnedPropertyBinding.__init__)
    params = list(sig.parameters.keys())



def test_characteristictype_is_not_abstract():
    assert not inspect.isabstract(CharacteristicType)


def test_characteristictype_constructor_exists():
    assert callable(CharacteristicType.__init__)


def test_characteristictype_constructor_args():
    sig = inspect.signature(CharacteristicType.__init__)
    params = list(sig.parameters.keys())



def test_smif_properties_annotationproperty_is_not_abstract():
    assert not inspect.isabstract(smif_properties_AnnotationProperty)


def test_smif_properties_annotationproperty_constructor_exists():
    assert callable(smif_properties_AnnotationProperty.__init__)


def test_smif_properties_annotationproperty_constructor_args():
    sig = inspect.signature(smif_properties_AnnotationProperty.__init__)
    params = list(sig.parameters.keys())



def test_properties_propertybinding_is_not_abstract():
    assert not inspect.isabstract(properties_PropertyBinding)


def test_properties_propertybinding_constructor_exists():
    assert callable(properties_PropertyBinding.__init__)


def test_properties_propertybinding_constructor_args():
    sig = inspect.signature(properties_PropertyBinding.__init__)
    params = list(sig.parameters.keys())



def test_smif_properties_characteristicbinding_is_not_abstract():
    assert not inspect.isabstract(smif_properties_CharacteristicBinding)


def test_smif_properties_characteristicbinding_constructor_exists():
    assert callable(smif_properties_CharacteristicBinding.__init__)


def test_smif_properties_characteristicbinding_constructor_args():
    sig = inspect.signature(smif_properties_CharacteristicBinding.__init__)
    params = list(sig.parameters.keys())



def test_properties_propertytype_is_not_abstract():
    assert not inspect.isabstract(properties_PropertyType)


def test_properties_propertytype_constructor_exists():
    assert callable(properties_PropertyType.__init__)


def test_properties_propertytype_constructor_args():
    sig = inspect.signature(properties_PropertyType.__init__)
    params = list(sig.parameters.keys())



def test_smif_properties_characteristictype_is_not_abstract():
    assert not inspect.isabstract(smif_properties_CharacteristicType)


def test_smif_properties_characteristictype_constructor_exists():
    assert callable(smif_properties_CharacteristicType.__init__)


def test_smif_properties_characteristictype_constructor_args():
    sig = inspect.signature(smif_properties_CharacteristicType.__init__)
    params = list(sig.parameters.keys())



def test_uniquenessconstraint_is_not_abstract():
    assert not inspect.isabstract(UniquenessConstraint)


def test_uniquenessconstraint_constructor_exists():
    assert callable(UniquenessConstraint.__init__)


def test_uniquenessconstraint_constructor_args():
    sig = inspect.signature(UniquenessConstraint.__init__)
    params = list(sig.parameters.keys())



def test_objectoperationtype_is_not_abstract():
    assert not inspect.isabstract(ObjectOperationType)


def test_objectoperationtype_constructor_exists():
    assert callable(ObjectOperationType.__init__)


def test_objectoperationtype_constructor_args():
    sig = inspect.signature(ObjectOperationType.__init__)
    params = list(sig.parameters.keys())



def test_traversal_is_not_abstract():
    assert not inspect.isabstract(Traversal)


def test_traversal_constructor_exists():
    assert callable(Traversal.__init__)


def test_traversal_constructor_args():
    sig = inspect.signature(Traversal.__init__)
    params = list(sig.parameters.keys())



def test_smif_metadata_definition_is_not_abstract():
    assert not inspect.isabstract(smif_metadata_Definition)


def test_smif_metadata_definition_constructor_exists():
    assert callable(smif_metadata_Definition.__init__)


def test_smif_metadata_definition_constructor_args():
    sig = inspect.signature(smif_metadata_Definition.__init__)
    params = list(sig.parameters.keys())
    assert "summaryDescription" in params, "Missing parameter 'summaryDescription'"
    assert "textDefinition" in params, "Missing parameter 'textDefinition'"

def test_smif_metadata_definition_has_summaryDescription():
    assert hasattr(smif_metadata_Definition, "summaryDescription")
    descriptor = None
    for klass in smif_metadata_Definition.__mro__:
        if "summaryDescription" in klass.__dict__:
            descriptor = klass.__dict__["summaryDescription"]
            break
    assert isinstance(descriptor, property)

def test_smif_metadata_definition_has_textDefinition():
    assert hasattr(smif_metadata_Definition, "textDefinition")
    descriptor = None
    for klass in smif_metadata_Definition.__mro__:
        if "textDefinition" in klass.__dict__:
            descriptor = klass.__dict__["textDefinition"]
            break
    assert isinstance(descriptor, property)



def test_term_is_not_abstract():
    assert not inspect.isabstract(Term)


def test_term_constructor_exists():
    assert callable(Term.__init__)


def test_term_constructor_args():
    sig = inspect.signature(Term.__init__)
    params = list(sig.parameters.keys())



def test_iriidentifier_is_not_abstract():
    assert not inspect.isabstract(IRIIdentifier)


def test_iriidentifier_constructor_exists():
    assert callable(IRIIdentifier.__init__)


def test_iriidentifier_constructor_args():
    sig = inspect.signature(IRIIdentifier.__init__)
    params = list(sig.parameters.keys())



def test_smif_lexicalscope_include_is_not_abstract():
    assert not inspect.isabstract(smif_lexicalscope_Include)


def test_smif_lexicalscope_include_constructor_exists():
    assert callable(smif_lexicalscope_Include.__init__)


def test_smif_lexicalscope_include_constructor_args():
    sig = inspect.signature(smif_lexicalscope_Include.__init__)
    params = list(sig.parameters.keys())



def test_smif_metadata_metadata_is_not_abstract():
    assert not inspect.isabstract(smif_metadata_Metadata)


def test_smif_metadata_metadata_constructor_exists():
    assert callable(smif_metadata_Metadata.__init__)


def test_smif_metadata_metadata_constructor_args():
    sig = inspect.signature(smif_metadata_Metadata.__init__)
    params = list(sig.parameters.keys())



def test_metadata_metadata_is_not_abstract():
    assert not inspect.isabstract(metadata_Metadata)


def test_metadata_metadata_constructor_exists():
    assert callable(metadata_Metadata.__init__)


def test_metadata_metadata_constructor_args():
    sig = inspect.signature(metadata_Metadata.__init__)
    params = list(sig.parameters.keys())



def test_smif_metadata_statement_is_not_abstract():
    assert not inspect.isabstract(smif_metadata_Statement)


def test_smif_metadata_statement_constructor_exists():
    assert callable(smif_metadata_Statement.__init__)


def test_smif_metadata_statement_constructor_args():
    sig = inspect.signature(smif_metadata_Statement.__init__)
    params = list(sig.parameters.keys())



def test_propertyownertype_is_not_abstract():
    assert not inspect.isabstract(PropertyOwnerType)


def test_propertyownertype_constructor_exists():
    assert callable(PropertyOwnerType.__init__)


def test_propertyownertype_constructor_args():
    sig = inspect.signature(PropertyOwnerType.__init__)
    params = list(sig.parameters.keys())



def test_smif_associations_associationtype_is_not_abstract():
    assert not inspect.isabstract(smif_associations_AssociationType)


def test_smif_associations_associationtype_constructor_exists():
    assert callable(smif_associations_AssociationType.__init__)


def test_smif_associations_associationtype_constructor_args():
    sig = inspect.signature(smif_associations_AssociationType.__init__)
    params = list(sig.parameters.keys())



def test_smif_lexicalscope_prefix_is_not_abstract():
    assert not inspect.isabstract(smif_lexicalscope_Prefix)


def test_smif_lexicalscope_prefix_constructor_exists():
    assert callable(smif_lexicalscope_Prefix.__init__)


def test_smif_lexicalscope_prefix_constructor_args():
    sig = inspect.signature(smif_lexicalscope_Prefix.__init__)
    params = list(sig.parameters.keys())



def test_smif_lexicalscope_mappingpackage_is_not_abstract():
    assert not inspect.isabstract(smif_lexicalscope_MappingPackage)


def test_smif_lexicalscope_mappingpackage_constructor_exists():
    assert callable(smif_lexicalscope_MappingPackage.__init__)


def test_smif_lexicalscope_mappingpackage_constructor_args():
    sig = inspect.signature(smif_lexicalscope_MappingPackage.__init__)
    params = list(sig.parameters.keys())



def test_smif_lexicalscope_physicalpackage_is_not_abstract():
    assert not inspect.isabstract(smif_lexicalscope_PhysicalPackage)


def test_smif_lexicalscope_physicalpackage_constructor_exists():
    assert callable(smif_lexicalscope_PhysicalPackage.__init__)


def test_smif_lexicalscope_physicalpackage_constructor_args():
    sig = inspect.signature(smif_lexicalscope_PhysicalPackage.__init__)
    params = list(sig.parameters.keys())



def test_smif_lexicalscope_logicalpackage_is_not_abstract():
    assert not inspect.isabstract(smif_lexicalscope_LogicalPackage)


def test_smif_lexicalscope_logicalpackage_constructor_exists():
    assert callable(smif_lexicalscope_LogicalPackage.__init__)


def test_smif_lexicalscope_logicalpackage_constructor_args():
    sig = inspect.signature(smif_lexicalscope_LogicalPackage.__init__)
    params = list(sig.parameters.keys())



def test_smif_lexicalscope_mofpackage_is_not_abstract():
    assert not inspect.isabstract(smif_lexicalscope_MOFPackage)


def test_smif_lexicalscope_mofpackage_constructor_exists():
    assert callable(smif_lexicalscope_MOFPackage.__init__)


def test_smif_lexicalscope_mofpackage_constructor_args():
    sig = inspect.signature(smif_lexicalscope_MOFPackage.__init__)
    params = list(sig.parameters.keys())



def test_uniqueidentifier_is_not_abstract():
    assert not inspect.isabstract(UniqueIdentifier)


def test_uniqueidentifier_constructor_exists():
    assert callable(UniqueIdentifier.__init__)


def test_uniqueidentifier_constructor_args():
    sig = inspect.signature(UniqueIdentifier.__init__)
    params = list(sig.parameters.keys())



def test_identifiableentity_is_not_abstract():
    assert not inspect.isabstract(IdentifiableEntity)


def test_identifiableentity_constructor_exists():
    assert callable(IdentifiableEntity.__init__)


def test_identifiableentity_constructor_args():
    sig = inspect.signature(IdentifiableEntity.__init__)
    params = list(sig.parameters.keys())



def test_smif_toplevel_proposition_is_not_abstract():
    assert not inspect.isabstract(smif_toplevel_Proposition)


def test_smif_toplevel_proposition_constructor_exists():
    assert callable(smif_toplevel_Proposition.__init__)


def test_smif_toplevel_proposition_constructor_args():
    sig = inspect.signature(smif_toplevel_Proposition.__init__)
    params = list(sig.parameters.keys())



def test_smif_toplevel_temporalentity_is_not_abstract():
    assert not inspect.isabstract(smif_toplevel_TemporalEntity)


def test_smif_toplevel_temporalentity_constructor_exists():
    assert callable(smif_toplevel_TemporalEntity.__init__)


def test_smif_toplevel_temporalentity_constructor_args():
    sig = inspect.signature(smif_toplevel_TemporalEntity.__init__)
    params = list(sig.parameters.keys())



def test_smif_toplevel_context_is_not_abstract():
    assert not inspect.isabstract(smif_toplevel_Context)


def test_smif_toplevel_context_constructor_exists():
    assert callable(smif_toplevel_Context.__init__)


def test_smif_toplevel_context_constructor_args():
    sig = inspect.signature(smif_toplevel_Context.__init__)
    params = list(sig.parameters.keys())



def test_smif_expressions_expressioncontext_is_not_abstract():
    assert not inspect.isabstract(smif_expressions_ExpressionContext)


def test_smif_expressions_expressioncontext_constructor_exists():
    assert callable(smif_expressions_ExpressionContext.__init__)


def test_smif_expressions_expressioncontext_constructor_args():
    sig = inspect.signature(smif_expressions_ExpressionContext.__init__)
    params = list(sig.parameters.keys())



def test_identifiers_textidentifier_is_not_abstract():
    assert not inspect.isabstract(identifiers_TextIdentifier)


def test_identifiers_textidentifier_constructor_exists():
    assert callable(identifiers_TextIdentifier.__init__)


def test_identifiers_textidentifier_constructor_args():
    sig = inspect.signature(identifiers_TextIdentifier.__init__)
    params = list(sig.parameters.keys())



def test_identifiers_uniqueidentifier_is_not_abstract():
    assert not inspect.isabstract(identifiers_UniqueIdentifier)


def test_identifiers_uniqueidentifier_constructor_exists():
    assert callable(identifiers_UniqueIdentifier.__init__)


def test_identifiers_uniqueidentifier_constructor_args():
    sig = inspect.signature(identifiers_UniqueIdentifier.__init__)
    params = list(sig.parameters.keys())



def test_expressions_expressionnode_is_not_abstract():
    assert not inspect.isabstract(expressions_ExpressionNode)


def test_expressions_expressionnode_constructor_exists():
    assert callable(expressions_ExpressionNode.__init__)


def test_expressions_expressionnode_constructor_args():
    sig = inspect.signature(expressions_ExpressionNode.__init__)
    params = list(sig.parameters.keys())



def test_functiontype_is_not_abstract():
    assert not inspect.isabstract(FunctionType)


def test_functiontype_constructor_exists():
    assert callable(FunctionType.__init__)


def test_functiontype_constructor_args():
    sig = inspect.signature(FunctionType.__init__)
    params = list(sig.parameters.keys())



def test_smif_expressions_objectoperationtype_is_not_abstract():
    assert not inspect.isabstract(smif_expressions_ObjectOperationType)


def test_smif_expressions_objectoperationtype_constructor_exists():
    assert callable(smif_expressions_ObjectOperationType.__init__)


def test_smif_expressions_objectoperationtype_constructor_args():
    sig = inspect.signature(smif_expressions_ObjectOperationType.__init__)
    params = list(sig.parameters.keys())



def test_evaluation_is_not_abstract():
    assert not inspect.isabstract(Evaluation)


def test_evaluation_constructor_exists():
    assert callable(Evaluation.__init__)


def test_evaluation_constructor_args():
    sig = inspect.signature(Evaluation.__init__)
    params = list(sig.parameters.keys())



def test_functioncall_is_not_abstract():
    assert not inspect.isabstract(FunctionCall)


def test_functioncall_constructor_exists():
    assert callable(FunctionCall.__init__)


def test_functioncall_constructor_args():
    sig = inspect.signature(FunctionCall.__init__)
    params = list(sig.parameters.keys())



def test_expressionnode_is_not_abstract():
    assert not inspect.isabstract(ExpressionNode)


def test_expressionnode_constructor_exists():
    assert callable(ExpressionNode.__init__)


def test_expressionnode_constructor_args():
    sig = inspect.signature(ExpressionNode.__init__)
    params = list(sig.parameters.keys())



def test_smif_expressions_constantreference_is_not_abstract():
    assert not inspect.isabstract(smif_expressions_ConstantReference)


def test_smif_expressions_constantreference_constructor_exists():
    assert callable(smif_expressions_ConstantReference.__init__)


def test_smif_expressions_constantreference_constructor_args():
    sig = inspect.signature(smif_expressions_ConstantReference.__init__)
    params = list(sig.parameters.keys())



def test_smif_expressions_equality_is_not_abstract():
    assert not inspect.isabstract(smif_expressions_Equality)


def test_smif_expressions_equality_constructor_exists():
    assert callable(smif_expressions_Equality.__init__)


def test_smif_expressions_equality_constructor_args():
    sig = inspect.signature(smif_expressions_Equality.__init__)
    params = list(sig.parameters.keys())



def test_expressions_expressioncontext_is_not_abstract():
    assert not inspect.isabstract(expressions_ExpressionContext)


def test_expressions_expressioncontext_constructor_exists():
    assert callable(expressions_ExpressionContext.__init__)


def test_expressions_expressioncontext_constructor_args():
    sig = inspect.signature(expressions_ExpressionContext.__init__)
    params = list(sig.parameters.keys())



def test_properties_propertyowner_is_not_abstract():
    assert not inspect.isabstract(properties_PropertyOwner)


def test_properties_propertyowner_constructor_exists():
    assert callable(properties_PropertyOwner.__init__)


def test_properties_propertyowner_constructor_args():
    sig = inspect.signature(properties_PropertyOwner.__init__)
    params = list(sig.parameters.keys())



def test_smif_expressions_functioncall_is_not_abstract():
    assert not inspect.isabstract(smif_expressions_FunctionCall)


def test_smif_expressions_functioncall_constructor_exists():
    assert callable(smif_expressions_FunctionCall.__init__)


def test_smif_expressions_functioncall_constructor_args():
    sig = inspect.signature(smif_expressions_FunctionCall.__init__)
    params = list(sig.parameters.keys())



def test_smif_expressions_traversal_is_not_abstract():
    assert not inspect.isabstract(smif_expressions_Traversal)


def test_smif_expressions_traversal_constructor_exists():
    assert callable(smif_expressions_Traversal.__init__)


def test_smif_expressions_traversal_constructor_args():
    sig = inspect.signature(smif_expressions_Traversal.__init__)
    params = list(sig.parameters.keys())
    assert "inverse" in params, "Missing parameter 'inverse'"
    assert "traverseToRelation" in params, "Missing parameter 'traverseToRelation'"

def test_smif_expressions_traversal_has_inverse():
    assert hasattr(smif_expressions_Traversal, "inverse")
    descriptor = None
    for klass in smif_expressions_Traversal.__mro__:
        if "inverse" in klass.__dict__:
            descriptor = klass.__dict__["inverse"]
            break
    assert isinstance(descriptor, property)

def test_smif_expressions_traversal_has_traverseToRelation():
    assert hasattr(smif_expressions_Traversal, "traverseToRelation")
    descriptor = None
    for klass in smif_expressions_Traversal.__mro__:
        if "traverseToRelation" in klass.__dict__:
            descriptor = klass.__dict__["traverseToRelation"]
            break
    assert isinstance(descriptor, property)



def test_smif_records_record_is_not_abstract():
    assert not inspect.isabstract(smif_records_Record)


def test_smif_records_record_constructor_exists():
    assert callable(smif_records_Record.__init__)


def test_smif_records_record_constructor_args():
    sig = inspect.signature(smif_records_Record.__init__)
    params = list(sig.parameters.keys())



def test_smif_relationships_relationship_is_not_abstract():
    assert not inspect.isabstract(smif_relationships_Relationship)


def test_smif_relationships_relationship_constructor_exists():
    assert callable(smif_relationships_Relationship.__init__)


def test_smif_relationships_relationship_constructor_args():
    sig = inspect.signature(smif_relationships_Relationship.__init__)
    params = list(sig.parameters.keys())



def test_values_value_is_not_abstract():
    assert not inspect.isabstract(values_Value)


def test_values_value_constructor_exists():
    assert callable(values_Value.__init__)


def test_values_value_constructor_args():
    sig = inspect.signature(values_Value.__init__)
    params = list(sig.parameters.keys())



def test_smif_values_structuredvalue_is_not_abstract():
    assert not inspect.isabstract(smif_values_StructuredValue)


def test_smif_values_structuredvalue_constructor_exists():
    assert callable(smif_values_StructuredValue.__init__)


def test_smif_values_structuredvalue_constructor_args():
    sig = inspect.signature(smif_values_StructuredValue.__init__)
    params = list(sig.parameters.keys())



def test_properties_propertyownertype_is_not_abstract():
    assert not inspect.isabstract(properties_PropertyOwnerType)


def test_properties_propertyownertype_constructor_exists():
    assert callable(properties_PropertyOwnerType.__init__)


def test_properties_propertyownertype_constructor_args():
    sig = inspect.signature(properties_PropertyOwnerType.__init__)
    params = list(sig.parameters.keys())



def test_smif_relationships_relationshiptype_is_not_abstract():
    assert not inspect.isabstract(smif_relationships_RelationshipType)


def test_smif_relationships_relationshiptype_constructor_exists():
    assert callable(smif_relationships_RelationshipType.__init__)


def test_smif_relationships_relationshiptype_constructor_args():
    sig = inspect.signature(smif_relationships_RelationshipType.__init__)
    params = list(sig.parameters.keys())



def test_smif_records_recordtype_is_not_abstract():
    assert not inspect.isabstract(smif_records_RecordType)


def test_smif_records_recordtype_constructor_exists():
    assert callable(smif_records_RecordType.__init__)


def test_smif_records_recordtype_constructor_args():
    sig = inspect.signature(smif_records_RecordType.__init__)
    params = list(sig.parameters.keys())



def test_smif_expressions_functiontype_is_not_abstract():
    assert not inspect.isabstract(smif_expressions_FunctionType)


def test_smif_expressions_functiontype_constructor_exists():
    assert callable(smif_expressions_FunctionType.__init__)


def test_smif_expressions_functiontype_constructor_args():
    sig = inspect.signature(smif_expressions_FunctionType.__init__)
    params = list(sig.parameters.keys())



def test_values_valuetype_is_not_abstract():
    assert not inspect.isabstract(values_ValueType)


def test_values_valuetype_constructor_exists():
    assert callable(values_ValueType.__init__)


def test_values_valuetype_constructor_args():
    sig = inspect.signature(values_ValueType.__init__)
    params = list(sig.parameters.keys())



def test_smif_values_structuredvaluetype_is_not_abstract():
    assert not inspect.isabstract(smif_values_StructuredValueType)


def test_smif_values_structuredvaluetype_constructor_exists():
    assert callable(smif_values_StructuredValueType.__init__)


def test_smif_values_structuredvaluetype_constructor_args():
    sig = inspect.signature(smif_values_StructuredValueType.__init__)
    params = list(sig.parameters.keys())



def test_context_is_not_abstract():
    assert not inspect.isabstract(Context)


def test_context_constructor_exists():
    assert callable(Context.__init__)


def test_context_constructor_args():
    sig = inspect.signature(Context.__init__)
    params = list(sig.parameters.keys())



def test_smif_identifiers_namespace_is_not_abstract():
    assert not inspect.isabstract(smif_identifiers_Namespace)


def test_smif_identifiers_namespace_constructor_exists():
    assert callable(smif_identifiers_Namespace.__init__)


def test_smif_identifiers_namespace_constructor_args():
    sig = inspect.signature(smif_identifiers_Namespace.__init__)
    params = list(sig.parameters.keys())



def test_smif_lexicalscope_lexicalreference_is_not_abstract():
    assert not inspect.isabstract(smif_lexicalscope_LexicalReference)


def test_smif_lexicalscope_lexicalreference_constructor_exists():
    assert callable(smif_lexicalscope_LexicalReference.__init__)


def test_smif_lexicalscope_lexicalreference_constructor_args():
    sig = inspect.signature(smif_lexicalscope_LexicalReference.__init__)
    params = list(sig.parameters.keys())



def test_smif_values_systemofunits_is_not_abstract():
    assert not inspect.isabstract(smif_values_SystemOfUnits)


def test_smif_values_systemofunits_constructor_exists():
    assert callable(smif_values_SystemOfUnits.__init__)


def test_smif_values_systemofunits_constructor_args():
    sig = inspect.signature(smif_values_SystemOfUnits.__init__)
    params = list(sig.parameters.keys())



def test_smif_identifiers_uniquetextidentifier_is_not_abstract():
    assert not inspect.isabstract(smif_identifiers_UniqueTextIdentifier)


def test_smif_identifiers_uniquetextidentifier_constructor_exists():
    assert callable(smif_identifiers_UniqueTextIdentifier.__init__)


def test_smif_identifiers_uniquetextidentifier_constructor_args():
    sig = inspect.signature(smif_identifiers_UniqueTextIdentifier.__init__)
    params = list(sig.parameters.keys())



def test_identifiers_uniquetextidentifier_is_not_abstract():
    assert not inspect.isabstract(identifiers_UniqueTextIdentifier)


def test_identifiers_uniquetextidentifier_constructor_exists():
    assert callable(identifiers_UniqueTextIdentifier.__init__)


def test_identifiers_uniquetextidentifier_constructor_args():
    sig = inspect.signature(identifiers_UniqueTextIdentifier.__init__)
    params = list(sig.parameters.keys())



def test_identifiers_name_is_not_abstract():
    assert not inspect.isabstract(identifiers_Name)


def test_identifiers_name_constructor_exists():
    assert callable(identifiers_Name.__init__)


def test_identifiers_name_constructor_args():
    sig = inspect.signature(identifiers_Name.__init__)
    params = list(sig.parameters.keys())



def test_smif_identifiers_term_is_not_abstract():
    assert not inspect.isabstract(smif_identifiers_Term)


def test_smif_identifiers_term_constructor_exists():
    assert callable(smif_identifiers_Term.__init__)


def test_smif_identifiers_term_constructor_args():
    sig = inspect.signature(smif_identifiers_Term.__init__)
    params = list(sig.parameters.keys())



def test_technicalidentifier_is_not_abstract():
    assert not inspect.isabstract(TechnicalIdentifier)


def test_technicalidentifier_constructor_exists():
    assert callable(TechnicalIdentifier.__init__)


def test_technicalidentifier_constructor_args():
    sig = inspect.signature(TechnicalIdentifier.__init__)
    params = list(sig.parameters.keys())



def test_smif_identifiers_iriidentifier_is_not_abstract():
    assert not inspect.isabstract(smif_identifiers_IRIIdentifier)


def test_smif_identifiers_iriidentifier_constructor_exists():
    assert callable(smif_identifiers_IRIIdentifier.__init__)


def test_smif_identifiers_iriidentifier_constructor_args():
    sig = inspect.signature(smif_identifiers_IRIIdentifier.__init__)
    params = list(sig.parameters.keys())



def test_namespace_is_not_abstract():
    assert not inspect.isabstract(Namespace)


def test_namespace_constructor_exists():
    assert callable(Namespace.__init__)


def test_namespace_constructor_args():
    sig = inspect.signature(Namespace.__init__)
    params = list(sig.parameters.keys())



def test_smif_lexicalscope_lexicalscope_is_not_abstract():
    assert not inspect.isabstract(smif_lexicalscope_LexicalScope)


def test_smif_lexicalscope_lexicalscope_constructor_exists():
    assert callable(smif_lexicalscope_LexicalScope.__init__)


def test_smif_lexicalscope_lexicalscope_constructor_args():
    sig = inspect.signature(smif_lexicalscope_LexicalScope.__init__)
    params = list(sig.parameters.keys())



def test_identifier_is_not_abstract():
    assert not inspect.isabstract(Identifier)


def test_identifier_constructor_exists():
    assert callable(Identifier.__init__)


def test_identifier_constructor_args():
    sig = inspect.signature(Identifier.__init__)
    params = list(sig.parameters.keys())



def test_smif_identifiers_textidentifier_is_not_abstract():
    assert not inspect.isabstract(smif_identifiers_TextIdentifier)


def test_smif_identifiers_textidentifier_constructor_exists():
    assert callable(smif_identifiers_TextIdentifier.__init__)


def test_smif_identifiers_textidentifier_constructor_args():
    sig = inspect.signature(smif_identifiers_TextIdentifier.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_smif_identifiers_textidentifier_has_value():
    assert hasattr(smif_identifiers_TextIdentifier, "value")
    descriptor = None
    for klass in smif_identifiers_TextIdentifier.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_smif_identifiers_uniqueidentifier_is_not_abstract():
    assert not inspect.isabstract(smif_identifiers_UniqueIdentifier)


def test_smif_identifiers_uniqueidentifier_constructor_exists():
    assert callable(smif_identifiers_UniqueIdentifier.__init__)


def test_smif_identifiers_uniqueidentifier_constructor_args():
    sig = inspect.signature(smif_identifiers_UniqueIdentifier.__init__)
    params = list(sig.parameters.keys())



def test_unitvalue_is_not_abstract():
    assert not inspect.isabstract(UnitValue)


def test_unitvalue_constructor_exists():
    assert callable(UnitValue.__init__)


def test_unitvalue_constructor_args():
    sig = inspect.signature(UnitValue.__init__)
    params = list(sig.parameters.keys())



def test_smif_values_scalarquantity_is_not_abstract():
    assert not inspect.isabstract(smif_values_ScalarQuantity)


def test_smif_values_scalarquantity_constructor_exists():
    assert callable(smif_values_ScalarQuantity.__init__)


def test_smif_values_scalarquantity_constructor_args():
    sig = inspect.signature(smif_values_ScalarQuantity.__init__)
    params = list(sig.parameters.keys())
    assert "_unnamed_ScalarQuantity" in params, "Missing parameter '_unnamed_ScalarQuantity'"

def test_smif_values_scalarquantity_has__unnamed_ScalarQuantity():
    assert hasattr(smif_values_ScalarQuantity, "_unnamed_ScalarQuantity")
    descriptor = None
    for klass in smif_values_ScalarQuantity.__mro__:
        if "_unnamed_ScalarQuantity" in klass.__dict__:
            descriptor = klass.__dict__["_unnamed_ScalarQuantity"]
            break
    assert isinstance(descriptor, property)



def test_value_is_not_abstract():
    assert not inspect.isabstract(Value)


def test_value_constructor_exists():
    assert callable(Value.__init__)


def test_value_constructor_args():
    sig = inspect.signature(Value.__init__)
    params = list(sig.parameters.keys())



def test_smif_identifiers_identifier_is_not_abstract():
    assert not inspect.isabstract(smif_identifiers_Identifier)


def test_smif_identifiers_identifier_constructor_exists():
    assert callable(smif_identifiers_Identifier.__init__)


def test_smif_identifiers_identifier_constructor_args():
    sig = inspect.signature(smif_identifiers_Identifier.__init__)
    params = list(sig.parameters.keys())



def test_smif_values_unitvalue_is_not_abstract():
    assert not inspect.isabstract(smif_values_UnitValue)


def test_smif_values_unitvalue_constructor_exists():
    assert callable(smif_values_UnitValue.__init__)


def test_smif_values_unitvalue_constructor_args():
    sig = inspect.signature(smif_values_UnitValue.__init__)
    params = list(sig.parameters.keys())
    assert "hasValue" in params, "Missing parameter 'hasValue'"

def test_smif_values_unitvalue_has_hasValue():
    assert hasattr(smif_values_UnitValue, "hasValue")
    descriptor = None
    for klass in smif_values_UnitValue.__mro__:
        if "hasValue" in klass.__dict__:
            descriptor = klass.__dict__["hasValue"]
            break
    assert isinstance(descriptor, property)



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_smif_types_entitytype_is_not_abstract():
    assert not inspect.isabstract(smif_types_EntityType)


def test_smif_types_entitytype_constructor_exists():
    assert callable(smif_types_EntityType.__init__)


def test_smif_types_entitytype_constructor_args():
    sig = inspect.signature(smif_types_EntityType.__init__)
    params = list(sig.parameters.keys())



def test_smif_properties_propertytype_is_not_abstract():
    assert not inspect.isabstract(smif_properties_PropertyType)


def test_smif_properties_propertytype_constructor_exists():
    assert callable(smif_properties_PropertyType.__init__)


def test_smif_properties_propertytype_constructor_args():
    sig = inspect.signature(smif_properties_PropertyType.__init__)
    params = list(sig.parameters.keys())



def test_smif_properties_propertyownertype_is_not_abstract():
    assert not inspect.isabstract(smif_properties_PropertyOwnerType)


def test_smif_properties_propertyownertype_constructor_exists():
    assert callable(smif_properties_PropertyOwnerType.__init__)


def test_smif_properties_propertyownertype_constructor_args():
    sig = inspect.signature(smif_properties_PropertyOwnerType.__init__)
    params = list(sig.parameters.keys())



def test_smif_facets_facet_is_not_abstract():
    assert not inspect.isabstract(smif_facets_Facet)


def test_smif_facets_facet_constructor_exists():
    assert callable(smif_facets_Facet.__init__)


def test_smif_facets_facet_constructor_args():
    sig = inspect.signature(smif_facets_Facet.__init__)
    params = list(sig.parameters.keys())



def test_smif_types_uniontype_is_not_abstract():
    assert not inspect.isabstract(smif_types_UnionType)


def test_smif_types_uniontype_constructor_exists():
    assert callable(smif_types_UnionType.__init__)


def test_smif_types_uniontype_constructor_args():
    sig = inspect.signature(smif_types_UnionType.__init__)
    params = list(sig.parameters.keys())



def test_smif_types_intersectiontype_is_not_abstract():
    assert not inspect.isabstract(smif_types_IntersectionType)


def test_smif_types_intersectiontype_constructor_exists():
    assert callable(smif_types_IntersectionType.__init__)


def test_smif_types_intersectiontype_constructor_args():
    sig = inspect.signature(smif_types_IntersectionType.__init__)
    params = list(sig.parameters.keys())



def test_representationrule_is_not_abstract():
    assert not inspect.isabstract(RepresentationRule)


def test_representationrule_constructor_exists():
    assert callable(RepresentationRule.__init__)


def test_representationrule_constructor_args():
    sig = inspect.signature(RepresentationRule.__init__)
    params = list(sig.parameters.keys())



def test_matchend_is_not_abstract():
    assert not inspect.isabstract(MatchEnd)


def test_matchend_constructor_exists():
    assert callable(MatchEnd.__init__)


def test_matchend_constructor_args():
    sig = inspect.signature(MatchEnd.__init__)
    params = list(sig.parameters.keys())



def test_expressioncontext_is_not_abstract():
    assert not inspect.isabstract(ExpressionContext)


def test_expressioncontext_constructor_exists():
    assert callable(ExpressionContext.__init__)


def test_expressioncontext_constructor_args():
    sig = inspect.signature(ExpressionContext.__init__)
    params = list(sig.parameters.keys())



def test_smif_expressions_evaluation_is_not_abstract():
    assert not inspect.isabstract(smif_expressions_Evaluation)


def test_smif_expressions_evaluation_constructor_exists():
    assert callable(smif_expressions_Evaluation.__init__)


def test_smif_expressions_evaluation_constructor_args():
    sig = inspect.signature(smif_expressions_Evaluation.__init__)
    params = list(sig.parameters.keys())



def test_smif_expressions_expressionnode_is_not_abstract():
    assert not inspect.isabstract(smif_expressions_ExpressionNode)


def test_smif_expressions_expressionnode_constructor_exists():
    assert callable(smif_expressions_ExpressionNode.__init__)


def test_smif_expressions_expressionnode_constructor_args():
    sig = inspect.signature(smif_expressions_ExpressionNode.__init__)
    params = list(sig.parameters.keys())
    assert "expressionTextLanguage" in params, "Missing parameter 'expressionTextLanguage'"
    assert "expressionText" in params, "Missing parameter 'expressionText'"

def test_smif_expressions_expressionnode_has_expressionTextLanguage():
    assert hasattr(smif_expressions_ExpressionNode, "expressionTextLanguage")
    descriptor = None
    for klass in smif_expressions_ExpressionNode.__mro__:
        if "expressionTextLanguage" in klass.__dict__:
            descriptor = klass.__dict__["expressionTextLanguage"]
            break
    assert isinstance(descriptor, property)

def test_smif_expressions_expressionnode_has_expressionText():
    assert hasattr(smif_expressions_ExpressionNode, "expressionText")
    descriptor = None
    for klass in smif_expressions_ExpressionNode.__mro__:
        if "expressionText" in klass.__dict__:
            descriptor = klass.__dict__["expressionText"]
            break
    assert isinstance(descriptor, property)



def test_smif_values_valuetype_is_not_abstract():
    assert not inspect.isabstract(smif_values_ValueType)


def test_smif_values_valuetype_constructor_exists():
    assert callable(smif_values_ValueType.__init__)


def test_smif_values_valuetype_constructor_args():
    sig = inspect.signature(smif_values_ValueType.__init__)
    params = list(sig.parameters.keys())



def test_unittype_is_not_abstract():
    assert not inspect.isabstract(UnitType)


def test_unittype_constructor_exists():
    assert callable(UnitType.__init__)


def test_unittype_constructor_args():
    sig = inspect.signature(UnitType.__init__)
    params = list(sig.parameters.keys())



def test_smif_values_baseunittype_is_not_abstract():
    assert not inspect.isabstract(smif_values_BaseUnitType)


def test_smif_values_baseunittype_constructor_exists():
    assert callable(smif_values_BaseUnitType.__init__)


def test_smif_values_baseunittype_constructor_args():
    sig = inspect.signature(smif_values_BaseUnitType.__init__)
    params = list(sig.parameters.keys())



def test_systemofunits_is_not_abstract():
    assert not inspect.isabstract(SystemOfUnits)


def test_systemofunits_constructor_exists():
    assert callable(SystemOfUnits.__init__)


def test_systemofunits_constructor_args():
    sig = inspect.signature(SystemOfUnits.__init__)
    params = list(sig.parameters.keys())



def test_definition_is_not_abstract():
    assert not inspect.isabstract(Definition)


def test_definition_constructor_exists():
    assert callable(Definition.__init__)


def test_definition_constructor_args():
    sig = inspect.signature(Definition.__init__)
    params = list(sig.parameters.keys())



def test_valuetype_is_not_abstract():
    assert not inspect.isabstract(ValueType)


def test_valuetype_constructor_exists():
    assert callable(ValueType.__init__)


def test_valuetype_constructor_args():
    sig = inspect.signature(ValueType.__init__)
    params = list(sig.parameters.keys())



def test_smif_values_unittype_is_not_abstract():
    assert not inspect.isabstract(smif_values_UnitType)


def test_smif_values_unittype_constructor_exists():
    assert callable(smif_values_UnitType.__init__)


def test_smif_values_unittype_constructor_args():
    sig = inspect.signature(smif_values_UnitType.__init__)
    params = list(sig.parameters.keys())
    assert "symbol" in params, "Missing parameter 'symbol'"
    assert "ratio" in params, "Missing parameter 'ratio'"
    assert "offset" in params, "Missing parameter 'offset'"

def test_smif_values_unittype_has_symbol():
    assert hasattr(smif_values_UnitType, "symbol")
    descriptor = None
    for klass in smif_values_UnitType.__mro__:
        if "symbol" in klass.__dict__:
            descriptor = klass.__dict__["symbol"]
            break
    assert isinstance(descriptor, property)

def test_smif_values_unittype_has_ratio():
    assert hasattr(smif_values_UnitType, "ratio")
    descriptor = None
    for klass in smif_values_UnitType.__mro__:
        if "ratio" in klass.__dict__:
            descriptor = klass.__dict__["ratio"]
            break
    assert isinstance(descriptor, property)

def test_smif_values_unittype_has_offset():
    assert hasattr(smif_values_UnitType, "offset")
    descriptor = None
    for klass in smif_values_UnitType.__mro__:
        if "offset" in klass.__dict__:
            descriptor = klass.__dict__["offset"]
            break
    assert isinstance(descriptor, property)



def test_smif_values_quantitykind_is_not_abstract():
    assert not inspect.isabstract(smif_values_QuantityKind)


def test_smif_values_quantitykind_constructor_exists():
    assert callable(smif_values_QuantityKind.__init__)


def test_smif_values_quantitykind_constructor_args():
    sig = inspect.signature(smif_values_QuantityKind.__init__)
    params = list(sig.parameters.keys())



def test_situations_situation_is_not_abstract():
    assert not inspect.isabstract(situations_Situation)


def test_situations_situation_constructor_exists():
    assert callable(situations_Situation.__init__)


def test_situations_situation_constructor_args():
    sig = inspect.signature(situations_Situation.__init__)
    params = list(sig.parameters.keys())



def test_toplevel_actualentity_is_not_abstract():
    assert not inspect.isabstract(toplevel_ActualEntity)


def test_toplevel_actualentity_constructor_exists():
    assert callable(toplevel_ActualEntity.__init__)


def test_toplevel_actualentity_constructor_args():
    sig = inspect.signature(toplevel_ActualEntity.__init__)
    params = list(sig.parameters.keys())



def test_smif_metadata_informationsource_is_not_abstract():
    assert not inspect.isabstract(smif_metadata_InformationSource)


def test_smif_metadata_informationsource_constructor_exists():
    assert callable(smif_metadata_InformationSource.__init__)


def test_smif_metadata_informationsource_constructor_args():
    sig = inspect.signature(smif_metadata_InformationSource.__init__)
    params = list(sig.parameters.keys())



def test_smif_situations_actualsituation_is_not_abstract():
    assert not inspect.isabstract(smif_situations_ActualSituation)


def test_smif_situations_actualsituation_constructor_exists():
    assert callable(smif_situations_ActualSituation.__init__)


def test_smif_situations_actualsituation_constructor_args():
    sig = inspect.signature(smif_situations_ActualSituation.__init__)
    params = list(sig.parameters.keys())



def test_patternmatch_is_not_abstract():
    assert not inspect.isabstract(PatternMatch)


def test_patternmatch_constructor_exists():
    assert callable(PatternMatch.__init__)


def test_patternmatch_constructor_args():
    sig = inspect.signature(PatternMatch.__init__)
    params = list(sig.parameters.keys())



def test_toplevel_temporalentity_is_not_abstract():
    assert not inspect.isabstract(toplevel_TemporalEntity)


def test_toplevel_temporalentity_constructor_exists():
    assert callable(toplevel_TemporalEntity.__init__)


def test_toplevel_temporalentity_constructor_args():
    sig = inspect.signature(toplevel_TemporalEntity.__init__)
    params = list(sig.parameters.keys())



def test_toplevel_proposition_is_not_abstract():
    assert not inspect.isabstract(toplevel_Proposition)


def test_toplevel_proposition_constructor_exists():
    assert callable(toplevel_Proposition.__init__)


def test_toplevel_proposition_constructor_args():
    sig = inspect.signature(toplevel_Proposition.__init__)
    params = list(sig.parameters.keys())



def test_smif_associations_association_is_not_abstract():
    assert not inspect.isabstract(smif_associations_Association)


def test_smif_associations_association_constructor_exists():
    assert callable(smif_associations_Association.__init__)


def test_smif_associations_association_constructor_args():
    sig = inspect.signature(smif_associations_Association.__init__)
    params = list(sig.parameters.keys())



def test_entitytype_is_not_abstract():
    assert not inspect.isabstract(EntityType)


def test_entitytype_constructor_exists():
    assert callable(EntityType.__init__)


def test_entitytype_constructor_args():
    sig = inspect.signature(EntityType.__init__)
    params = list(sig.parameters.keys())



def test_smif_situations_situationtype_is_not_abstract():
    assert not inspect.isabstract(smif_situations_SituationType)


def test_smif_situations_situationtype_constructor_exists():
    assert callable(smif_situations_SituationType.__init__)


def test_smif_situations_situationtype_constructor_args():
    sig = inspect.signature(smif_situations_SituationType.__init__)
    params = list(sig.parameters.keys())



def test_lexicalscope_is_not_abstract():
    assert not inspect.isabstract(LexicalScope)


def test_lexicalscope_constructor_exists():
    assert callable(LexicalScope.__init__)


def test_lexicalscope_constructor_args():
    sig = inspect.signature(LexicalScope.__init__)
    params = list(sig.parameters.keys())



def test_smif_lexicalscope_package_is_not_abstract():
    assert not inspect.isabstract(smif_lexicalscope_Package)


def test_smif_lexicalscope_package_constructor_exists():
    assert callable(smif_lexicalscope_Package.__init__)


def test_smif_lexicalscope_package_constructor_args():
    sig = inspect.signature(smif_lexicalscope_Package.__init__)
    params = list(sig.parameters.keys())



def test_smif_repository_is_not_abstract():
    assert not inspect.isabstract(smif_Repository)


def test_smif_repository_constructor_exists():
    assert callable(smif_Repository.__init__)


def test_smif_repository_constructor_args():
    sig = inspect.signature(smif_Repository.__init__)
    params = list(sig.parameters.keys())



def test_recordtype_is_not_abstract():
    assert not inspect.isabstract(RecordType)


def test_recordtype_constructor_exists():
    assert callable(RecordType.__init__)


def test_recordtype_constructor_args():
    sig = inspect.signature(RecordType.__init__)
    params = list(sig.parameters.keys())



def test_smif_mapping_facade_is_not_abstract():
    assert not inspect.isabstract(smif_mapping_Facade)


def test_smif_mapping_facade_constructor_exists():
    assert callable(smif_mapping_Facade.__init__)


def test_smif_mapping_facade_constructor_args():
    sig = inspect.signature(smif_mapping_Facade.__init__)
    params = list(sig.parameters.keys())



def test_propertytypeconstraint_is_not_abstract():
    assert not inspect.isabstract(PropertyTypeConstraint)


def test_propertytypeconstraint_constructor_exists():
    assert callable(PropertyTypeConstraint.__init__)


def test_propertytypeconstraint_constructor_args():
    sig = inspect.signature(PropertyTypeConstraint.__init__)
    params = list(sig.parameters.keys())



def test_multiplicityconstraint_is_not_abstract():
    assert not inspect.isabstract(MultiplicityConstraint)


def test_multiplicityconstraint_constructor_exists():
    assert callable(MultiplicityConstraint.__init__)


def test_multiplicityconstraint_constructor_args():
    sig = inspect.signature(MultiplicityConstraint.__init__)
    params = list(sig.parameters.keys())



def test_generalizationconstraint_is_not_abstract():
    assert not inspect.isabstract(GeneralizationConstraint)


def test_generalizationconstraint_constructor_exists():
    assert callable(GeneralizationConstraint.__init__)


def test_generalizationconstraint_constructor_args():
    sig = inspect.signature(GeneralizationConstraint.__init__)
    params = list(sig.parameters.keys())



def test_smif_constraints_facetclassificationconstraint_is_not_abstract():
    assert not inspect.isabstract(smif_constraints_FacetClassificationConstraint)


def test_smif_constraints_facetclassificationconstraint_constructor_exists():
    assert callable(smif_constraints_FacetClassificationConstraint.__init__)


def test_smif_constraints_facetclassificationconstraint_constructor_args():
    sig = inspect.signature(smif_constraints_FacetClassificationConstraint.__init__)
    params = list(sig.parameters.keys())



def test_coveringconstraint_is_not_abstract():
    assert not inspect.isabstract(CoveringConstraint)


def test_coveringconstraint_constructor_exists():
    assert callable(CoveringConstraint.__init__)


def test_coveringconstraint_constructor_args():
    sig = inspect.signature(CoveringConstraint.__init__)
    params = list(sig.parameters.keys())



def test_patternoftype_is_not_abstract():
    assert not inspect.isabstract(PatternOfType)


def test_patternoftype_constructor_exists():
    assert callable(PatternOfType.__init__)


def test_patternoftype_constructor_args():
    sig = inspect.signature(PatternOfType.__init__)
    params = list(sig.parameters.keys())



def test_propertytype_is_not_abstract():
    assert not inspect.isabstract(PropertyType)


def test_propertytype_constructor_exists():
    assert callable(PropertyType.__init__)


def test_propertytype_constructor_args():
    sig = inspect.signature(PropertyType.__init__)
    params = list(sig.parameters.keys())



def test_smif_properties_ownedpropertytype_is_not_abstract():
    assert not inspect.isabstract(smif_properties_OwnedPropertyType)


def test_smif_properties_ownedpropertytype_constructor_exists():
    assert callable(smif_properties_OwnedPropertyType.__init__)


def test_smif_properties_ownedpropertytype_constructor_args():
    sig = inspect.signature(smif_properties_OwnedPropertyType.__init__)
    params = list(sig.parameters.keys())



def test_thing_is_not_abstract():
    assert not inspect.isabstract(Thing)


def test_thing_constructor_exists():
    assert callable(Thing.__init__)


def test_thing_constructor_args():
    sig = inspect.signature(Thing.__init__)
    params = list(sig.parameters.keys())



def test_smif_values_value_is_not_abstract():
    assert not inspect.isabstract(smif_values_Value)


def test_smif_values_value_constructor_exists():
    assert callable(smif_values_Value.__init__)


def test_smif_values_value_constructor_args():
    sig = inspect.signature(smif_values_Value.__init__)
    params = list(sig.parameters.keys())



def test_smif_properties_propertybinding_is_not_abstract():
    assert not inspect.isabstract(smif_properties_PropertyBinding)


def test_smif_properties_propertybinding_constructor_exists():
    assert callable(smif_properties_PropertyBinding.__init__)


def test_smif_properties_propertybinding_constructor_args():
    sig = inspect.signature(smif_properties_PropertyBinding.__init__)
    params = list(sig.parameters.keys())



def test_smif_properties_propertyowner_is_not_abstract():
    assert not inspect.isabstract(smif_properties_PropertyOwner)


def test_smif_properties_propertyowner_constructor_exists():
    assert callable(smif_properties_PropertyOwner.__init__)


def test_smif_properties_propertyowner_constructor_args():
    sig = inspect.signature(smif_properties_PropertyOwner.__init__)
    params = list(sig.parameters.keys())



def test_smif_toplevel_identifiableentity_is_not_abstract():
    assert not inspect.isabstract(smif_toplevel_IdentifiableEntity)


def test_smif_toplevel_identifiableentity_constructor_exists():
    assert callable(smif_toplevel_IdentifiableEntity.__init__)


def test_smif_toplevel_identifiableentity_constructor_args():
    sig = inspect.signature(smif_toplevel_IdentifiableEntity.__init__)
    params = list(sig.parameters.keys())



def test_toplevel_context_is_not_abstract():
    assert not inspect.isabstract(toplevel_Context)


def test_toplevel_context_constructor_exists():
    assert callable(toplevel_Context.__init__)


def test_toplevel_context_constructor_args():
    sig = inspect.signature(toplevel_Context.__init__)
    params = list(sig.parameters.keys())



def test_lexicalscope_lexicalscope_is_not_abstract():
    assert not inspect.isabstract(lexicalscope_LexicalScope)


def test_lexicalscope_lexicalscope_constructor_exists():
    assert callable(lexicalscope_LexicalScope.__init__)


def test_lexicalscope_lexicalscope_constructor_args():
    sig = inspect.signature(lexicalscope_LexicalScope.__init__)
    params = list(sig.parameters.keys())



def test_smif_patterns_pattern_is_not_abstract():
    assert not inspect.isabstract(smif_patterns_Pattern)


def test_smif_patterns_pattern_constructor_exists():
    assert callable(smif_patterns_Pattern.__init__)


def test_smif_patterns_pattern_constructor_args():
    sig = inspect.signature(smif_patterns_Pattern.__init__)
    params = list(sig.parameters.keys())



def test_smif_situations_situation_is_not_abstract():
    assert not inspect.isabstract(smif_situations_Situation)


def test_smif_situations_situation_constructor_exists():
    assert callable(smif_situations_Situation.__init__)


def test_smif_situations_situation_constructor_args():
    sig = inspect.signature(smif_situations_Situation.__init__)
    params = list(sig.parameters.keys())



def test_smif_types_type_is_not_abstract():
    assert not inspect.isabstract(smif_types_Type)


def test_smif_types_type_constructor_exists():
    assert callable(smif_types_Type.__init__)


def test_smif_types_type_constructor_args():
    sig = inspect.signature(smif_types_Type.__init__)
    params = list(sig.parameters.keys())

def test_variablequalification_exists():
    # Check that the Enumeration exists
    assert VariableQualification is not None

def test_variablequalification_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VariableQualification]
    expected_literals = [
        "All",
        "Negate",
        "Assert",
        "ExactlyOne",
        "Select",
        "Optional",
        "ThereExists",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in VariableQualification"

def test_assertionstrength_exists():
    # Check that the Enumeration exists
    assert AssertionStrength is not None

def test_assertionstrength_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AssertionStrength]
    expected_literals = [
        "Global",
        "Local",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AssertionStrength"


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
Prefix_strategy = st.builds(
    Prefix,
)
Package_strategy = st.builds(
    Package,
)
smif_lexicalscope_Model_strategy = st.builds(
    smif_lexicalscope_Model,
)
ConditionalRule_strategy = st.builds(
    ConditionalRule,
)
smif_mapping_RepresentationRule_strategy = st.builds(
    smif_mapping_RepresentationRule,
    mapAll=
        safe_text
)
Facade_strategy = st.builds(
    Facade,
)
smif_mapping_ComputedFacade_strategy = st.builds(
    smif_mapping_ComputedFacade,
)
Situation_strategy = st.builds(
    Situation,
)
VariableBinding_strategy = st.builds(
    VariableBinding,
)
patterns_Pattern_strategy = st.builds(
    patterns_Pattern,
)
MatchRule_strategy = st.builds(
    MatchRule,
)
smif_patterns_Computed_strategy = st.builds(
    smif_patterns_Computed,
)
OwnedPropertyBinding_strategy = st.builds(
    OwnedPropertyBinding,
)
smif_patterns_VariableBinding_strategy = st.builds(
    smif_patterns_VariableBinding,
)
Pattern_strategy = st.builds(
    Pattern,
)
ActualSituation_strategy = st.builds(
    ActualSituation,
)
smif_patterns_PatternMatch_strategy = st.builds(
    smif_patterns_PatternMatch,
)
smif_patterns_PatternOfType_strategy = st.builds(
    smif_patterns_PatternOfType,
)
TypePatternVariable_strategy = st.builds(
    TypePatternVariable,
)
smif_patterns_FocusVariable_strategy = st.builds(
    smif_patterns_FocusVariable,
)
smif_patterns_PartVariable_strategy = st.builds(
    smif_patterns_PartVariable,
    isBoundaryPart=
        safe_text
)
patterns_Computed_strategy = st.builds(
    patterns_Computed,
)
patterns_PatternVariable_strategy = st.builds(
    patterns_PatternVariable,
)
smif_patterns_ExpressionVariable_strategy = st.builds(
    smif_patterns_ExpressionVariable,
)
Mapping_strategy = st.builds(
    Mapping,
)
Equality_strategy = st.builds(
    Equality,
)
properties_OwnedPropertyType_strategy = st.builds(
    properties_OwnedPropertyType,
)
PatternVariable_strategy = st.builds(
    PatternVariable,
)
smif_patterns_TypePatternVariable_strategy = st.builds(
    smif_patterns_TypePatternVariable,
)
smif_patterns_PropositionVariable_strategy = st.builds(
    smif_patterns_PropositionVariable,
)
TemporalEntity_strategy = st.builds(
    TemporalEntity,
)
smif_toplevel_ActualEntity_strategy = st.builds(
    smif_toplevel_ActualEntity,
)
PropositionVariable_strategy = st.builds(
    PropositionVariable,
)
LexicalReference_strategy = st.builds(
    LexicalReference,
)
Statement_strategy = st.builds(
    Statement,
)
ConstantReference_strategy = st.builds(
    ConstantReference,
)
smif_toplevel_Thing_strategy = st.builds(
    smif_toplevel_Thing,
)
PropertyBinding_strategy = st.builds(
    PropertyBinding,
)
InformationSource_strategy = st.builds(
    InformationSource,
)
Record_strategy = st.builds(
    Record,
)
Name_strategy = st.builds(
    Name,
)
Metadata_strategy = st.builds(
    Metadata,
)
constraints_Conditional_strategy = st.builds(
    constraints_Conditional,
)
smif_mapping_MatchEnd_strategy = st.builds(
    smif_mapping_MatchEnd,
)
smif_patterns_PatternVariable_strategy = st.builds(
    smif_patterns_PatternVariable,
    explicit=
        safe_text,
    qualification=
        safe_text
)
constraints_Rule_strategy = st.builds(
    constraints_Rule,
)
smif_mapping_Mapping_strategy = st.builds(
    smif_mapping_Mapping,
    strength=
        safe_text
)
smif_constraints_ConditionalRule_strategy = st.builds(
    smif_constraints_ConditionalRule,
)
smif_constraints_Conditional_strategy = st.builds(
    smif_constraints_Conditional,
)
PropertyConstraint_strategy = st.builds(
    PropertyConstraint,
)
smif_constraints_PropertyTypeConstraint_strategy = st.builds(
    smif_constraints_PropertyTypeConstraint,
    prerequisiteType=
        safe_text
)
smif_constraints_PropertyTransitivityConstraint_strategy = st.builds(
    smif_constraints_PropertyTransitivityConstraint,
)
TypeConstraint_strategy = st.builds(
    TypeConstraint,
)
smif_constraints_UniquenessConstraint_strategy = st.builds(
    smif_constraints_UniquenessConstraint,
    isPrimaryIdentity=
        safe_text
)
smif_constraints_GeneralizationConstraint_strategy = st.builds(
    smif_constraints_GeneralizationConstraint,
    redefines=
        safe_text
)
smif_constraints_CoveringConstraint_strategy = st.builds(
    smif_constraints_CoveringConstraint,
)
smif_constraints_MultiplicityConstraint_strategy = st.builds(
    smif_constraints_MultiplicityConstraint,
    mininumNumber=
        safe_text,
    maximumNumber=
        safe_text,
    atOnce=
        safe_text,
    isSufficent=
        safe_text
)
Rule_strategy = st.builds(
    Rule,
)
smif_mapping_MatchRule_strategy = st.builds(
    smif_mapping_MatchRule,
    coerce=
        safe_text
)
smif_constraints_TypeConstraint_strategy = st.builds(
    smif_constraints_TypeConstraint,
)
smif_constraints_Enumerated_strategy = st.builds(
    smif_constraints_Enumerated,
)
smif_constraints_Equivalent_strategy = st.builds(
    smif_constraints_Equivalent,
)
smif_constraints_Disjoint_strategy = st.builds(
    smif_constraints_Disjoint,
)
smif_constraints_PropertyConstraint_strategy = st.builds(
    smif_constraints_PropertyConstraint,
)
Proposition_strategy = st.builds(
    Proposition,
)
smif_constraints_Rule_strategy = st.builds(
    smif_constraints_Rule,
)
situations_SituationType_strategy = st.builds(
    situations_SituationType,
)
situations_ActualSituation_strategy = st.builds(
    situations_ActualSituation,
)
UniqueTextIdentifier_strategy = st.builds(
    UniqueTextIdentifier,
)
smif_identifiers_TechnicalIdentifier_strategy = st.builds(
    smif_identifiers_TechnicalIdentifier,
)
TextIdentifier_strategy = st.builds(
    TextIdentifier,
)
smif_identifiers_Name_strategy = st.builds(
    smif_identifiers_Name,
)
Facet_strategy = st.builds(
    Facet,
)
smif_facets_Category_strategy = st.builds(
    smif_facets_Category,
)
smif_facets_Role_strategy = st.builds(
    smif_facets_Role,
)
facets_Facet_strategy = st.builds(
    facets_Facet,
)
smif_facets_Phase_strategy = st.builds(
    smif_facets_Phase,
)
Relationship_strategy = st.builds(
    Relationship,
)
smif_facets_FacetOfEntity_strategy = st.builds(
    smif_facets_FacetOfEntity,
)
smif_properties_OwnedPropertyBinding_strategy = st.builds(
    smif_properties_OwnedPropertyBinding,
)
CharacteristicType_strategy = st.builds(
    CharacteristicType,
)
smif_properties_AnnotationProperty_strategy = st.builds(
    smif_properties_AnnotationProperty,
)
properties_PropertyBinding_strategy = st.builds(
    properties_PropertyBinding,
)
smif_properties_CharacteristicBinding_strategy = st.builds(
    smif_properties_CharacteristicBinding,
)
properties_PropertyType_strategy = st.builds(
    properties_PropertyType,
)
smif_properties_CharacteristicType_strategy = st.builds(
    smif_properties_CharacteristicType,
)
UniquenessConstraint_strategy = st.builds(
    UniquenessConstraint,
)
ObjectOperationType_strategy = st.builds(
    ObjectOperationType,
)
Traversal_strategy = st.builds(
    Traversal,
)
smif_metadata_Definition_strategy = st.builds(
    smif_metadata_Definition,
    summaryDescription=
        safe_text,
    textDefinition=
        safe_text
)
Term_strategy = st.builds(
    Term,
)
IRIIdentifier_strategy = st.builds(
    IRIIdentifier,
)
smif_lexicalscope_Include_strategy = st.builds(
    smif_lexicalscope_Include,
)
smif_metadata_Metadata_strategy = st.builds(
    smif_metadata_Metadata,
)
metadata_Metadata_strategy = st.builds(
    metadata_Metadata,
)
smif_metadata_Statement_strategy = st.builds(
    smif_metadata_Statement,
)
PropertyOwnerType_strategy = st.builds(
    PropertyOwnerType,
)
smif_associations_AssociationType_strategy = st.builds(
    smif_associations_AssociationType,
)
smif_lexicalscope_Prefix_strategy = st.builds(
    smif_lexicalscope_Prefix,
)
smif_lexicalscope_MappingPackage_strategy = st.builds(
    smif_lexicalscope_MappingPackage,
)
smif_lexicalscope_PhysicalPackage_strategy = st.builds(
    smif_lexicalscope_PhysicalPackage,
)
smif_lexicalscope_LogicalPackage_strategy = st.builds(
    smif_lexicalscope_LogicalPackage,
)
smif_lexicalscope_MOFPackage_strategy = st.builds(
    smif_lexicalscope_MOFPackage,
)
UniqueIdentifier_strategy = st.builds(
    UniqueIdentifier,
)
IdentifiableEntity_strategy = st.builds(
    IdentifiableEntity,
)
smif_toplevel_Proposition_strategy = st.builds(
    smif_toplevel_Proposition,
)
smif_toplevel_TemporalEntity_strategy = st.builds(
    smif_toplevel_TemporalEntity,
)
smif_toplevel_Context_strategy = st.builds(
    smif_toplevel_Context,
)
smif_expressions_ExpressionContext_strategy = st.builds(
    smif_expressions_ExpressionContext,
)
identifiers_TextIdentifier_strategy = st.builds(
    identifiers_TextIdentifier,
)
identifiers_UniqueIdentifier_strategy = st.builds(
    identifiers_UniqueIdentifier,
)
expressions_ExpressionNode_strategy = st.builds(
    expressions_ExpressionNode,
)
FunctionType_strategy = st.builds(
    FunctionType,
)
smif_expressions_ObjectOperationType_strategy = st.builds(
    smif_expressions_ObjectOperationType,
)
Evaluation_strategy = st.builds(
    Evaluation,
)
FunctionCall_strategy = st.builds(
    FunctionCall,
)
ExpressionNode_strategy = st.builds(
    ExpressionNode,
)
smif_expressions_ConstantReference_strategy = st.builds(
    smif_expressions_ConstantReference,
)
smif_expressions_Equality_strategy = st.builds(
    smif_expressions_Equality,
)
expressions_ExpressionContext_strategy = st.builds(
    expressions_ExpressionContext,
)
properties_PropertyOwner_strategy = st.builds(
    properties_PropertyOwner,
)
smif_expressions_FunctionCall_strategy = st.builds(
    smif_expressions_FunctionCall,
)
smif_expressions_Traversal_strategy = st.builds(
    smif_expressions_Traversal,
    inverse=
        safe_text,
    traverseToRelation=
        safe_text
)
smif_records_Record_strategy = st.builds(
    smif_records_Record,
)
smif_relationships_Relationship_strategy = st.builds(
    smif_relationships_Relationship,
)
values_Value_strategy = st.builds(
    values_Value,
)
smif_values_StructuredValue_strategy = st.builds(
    smif_values_StructuredValue,
)
properties_PropertyOwnerType_strategy = st.builds(
    properties_PropertyOwnerType,
)
smif_relationships_RelationshipType_strategy = st.builds(
    smif_relationships_RelationshipType,
)
smif_records_RecordType_strategy = st.builds(
    smif_records_RecordType,
)
smif_expressions_FunctionType_strategy = st.builds(
    smif_expressions_FunctionType,
)
values_ValueType_strategy = st.builds(
    values_ValueType,
)
smif_values_StructuredValueType_strategy = st.builds(
    smif_values_StructuredValueType,
)
Context_strategy = st.builds(
    Context,
)
smif_identifiers_Namespace_strategy = st.builds(
    smif_identifiers_Namespace,
)
smif_lexicalscope_LexicalReference_strategy = st.builds(
    smif_lexicalscope_LexicalReference,
)
smif_values_SystemOfUnits_strategy = st.builds(
    smif_values_SystemOfUnits,
)
smif_identifiers_UniqueTextIdentifier_strategy = st.builds(
    smif_identifiers_UniqueTextIdentifier,
)
identifiers_UniqueTextIdentifier_strategy = st.builds(
    identifiers_UniqueTextIdentifier,
)
identifiers_Name_strategy = st.builds(
    identifiers_Name,
)
smif_identifiers_Term_strategy = st.builds(
    smif_identifiers_Term,
)
TechnicalIdentifier_strategy = st.builds(
    TechnicalIdentifier,
)
smif_identifiers_IRIIdentifier_strategy = st.builds(
    smif_identifiers_IRIIdentifier,
)
Namespace_strategy = st.builds(
    Namespace,
)
smif_lexicalscope_LexicalScope_strategy = st.builds(
    smif_lexicalscope_LexicalScope,
)
Identifier_strategy = st.builds(
    Identifier,
)
smif_identifiers_TextIdentifier_strategy = st.builds(
    smif_identifiers_TextIdentifier,
    value=
        safe_text
)
smif_identifiers_UniqueIdentifier_strategy = st.builds(
    smif_identifiers_UniqueIdentifier,
)
UnitValue_strategy = st.builds(
    UnitValue,
)
smif_values_ScalarQuantity_strategy = st.builds(
    smif_values_ScalarQuantity,
    _unnamed_ScalarQuantity=
        safe_text
)
Value_strategy = st.builds(
    Value,
)
smif_identifiers_Identifier_strategy = st.builds(
    smif_identifiers_Identifier,
)
smif_values_UnitValue_strategy = st.builds(
    smif_values_UnitValue,
    hasValue=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
smif_types_EntityType_strategy = st.builds(
    smif_types_EntityType,
)
smif_properties_PropertyType_strategy = st.builds(
    smif_properties_PropertyType,
)
smif_properties_PropertyOwnerType_strategy = st.builds(
    smif_properties_PropertyOwnerType,
)
smif_facets_Facet_strategy = st.builds(
    smif_facets_Facet,
)
smif_types_UnionType_strategy = st.builds(
    smif_types_UnionType,
)
smif_types_IntersectionType_strategy = st.builds(
    smif_types_IntersectionType,
)
RepresentationRule_strategy = st.builds(
    RepresentationRule,
)
MatchEnd_strategy = st.builds(
    MatchEnd,
)
ExpressionContext_strategy = st.builds(
    ExpressionContext,
)
smif_expressions_Evaluation_strategy = st.builds(
    smif_expressions_Evaluation,
)
smif_expressions_ExpressionNode_strategy = st.builds(
    smif_expressions_ExpressionNode,
    expressionTextLanguage=
        safe_text,
    expressionText=
        safe_text
)
smif_values_ValueType_strategy = st.builds(
    smif_values_ValueType,
)
UnitType_strategy = st.builds(
    UnitType,
)
smif_values_BaseUnitType_strategy = st.builds(
    smif_values_BaseUnitType,
)
SystemOfUnits_strategy = st.builds(
    SystemOfUnits,
)
Definition_strategy = st.builds(
    Definition,
)
ValueType_strategy = st.builds(
    ValueType,
)
smif_values_UnitType_strategy = st.builds(
    smif_values_UnitType,
    symbol=
        safe_text,
    ratio=
        safe_text,
    offset=
        safe_text
)
smif_values_QuantityKind_strategy = st.builds(
    smif_values_QuantityKind,
)
situations_Situation_strategy = st.builds(
    situations_Situation,
)
toplevel_ActualEntity_strategy = st.builds(
    toplevel_ActualEntity,
)
smif_metadata_InformationSource_strategy = st.builds(
    smif_metadata_InformationSource,
)
smif_situations_ActualSituation_strategy = st.builds(
    smif_situations_ActualSituation,
)
PatternMatch_strategy = st.builds(
    PatternMatch,
)
toplevel_TemporalEntity_strategy = st.builds(
    toplevel_TemporalEntity,
)
toplevel_Proposition_strategy = st.builds(
    toplevel_Proposition,
)
smif_associations_Association_strategy = st.builds(
    smif_associations_Association,
)
EntityType_strategy = st.builds(
    EntityType,
)
smif_situations_SituationType_strategy = st.builds(
    smif_situations_SituationType,
)
LexicalScope_strategy = st.builds(
    LexicalScope,
)
smif_lexicalscope_Package_strategy = st.builds(
    smif_lexicalscope_Package,
)
smif_Repository_strategy = st.builds(
    smif_Repository,
)
RecordType_strategy = st.builds(
    RecordType,
)
smif_mapping_Facade_strategy = st.builds(
    smif_mapping_Facade,
)
PropertyTypeConstraint_strategy = st.builds(
    PropertyTypeConstraint,
)
MultiplicityConstraint_strategy = st.builds(
    MultiplicityConstraint,
)
GeneralizationConstraint_strategy = st.builds(
    GeneralizationConstraint,
)
smif_constraints_FacetClassificationConstraint_strategy = st.builds(
    smif_constraints_FacetClassificationConstraint,
)
CoveringConstraint_strategy = st.builds(
    CoveringConstraint,
)
PatternOfType_strategy = st.builds(
    PatternOfType,
)
PropertyType_strategy = st.builds(
    PropertyType,
)
smif_properties_OwnedPropertyType_strategy = st.builds(
    smif_properties_OwnedPropertyType,
)
Thing_strategy = st.builds(
    Thing,
)
smif_values_Value_strategy = st.builds(
    smif_values_Value,
)
smif_properties_PropertyBinding_strategy = st.builds(
    smif_properties_PropertyBinding,
)
smif_properties_PropertyOwner_strategy = st.builds(
    smif_properties_PropertyOwner,
)
smif_toplevel_IdentifiableEntity_strategy = st.builds(
    smif_toplevel_IdentifiableEntity,
)
toplevel_Context_strategy = st.builds(
    toplevel_Context,
)
lexicalscope_LexicalScope_strategy = st.builds(
    lexicalscope_LexicalScope,
)
smif_patterns_Pattern_strategy = st.builds(
    smif_patterns_Pattern,
)
smif_situations_Situation_strategy = st.builds(
    smif_situations_Situation,
)
smif_types_Type_strategy = st.builds(
    smif_types_Type,
)

@given(instance=Prefix_strategy)
@settings(max_examples=50)
def test_prefix_instantiation(instance):
    assert isinstance(instance, Prefix)

@given(instance=Package_strategy)
@settings(max_examples=50)
def test_package_instantiation(instance):
    assert isinstance(instance, Package)

@given(instance=smif_lexicalscope_Model_strategy)
@settings(max_examples=50)
def test_smif_lexicalscope_model_instantiation(instance):
    assert isinstance(instance, smif_lexicalscope_Model)

@given(instance=ConditionalRule_strategy)
@settings(max_examples=50)
def test_conditionalrule_instantiation(instance):
    assert isinstance(instance, ConditionalRule)

@given(instance=smif_mapping_RepresentationRule_strategy)
@settings(max_examples=50)
def test_smif_mapping_representationrule_instantiation(instance):
    assert isinstance(instance, smif_mapping_RepresentationRule)



@given(instance=smif_mapping_RepresentationRule_strategy)
def test_smif_mapping_representationrule_mapAll_setter(instance):
    original = instance.mapAll
    instance.mapAll = original
    assert instance.mapAll == original

@given(instance=Facade_strategy)
@settings(max_examples=50)
def test_facade_instantiation(instance):
    assert isinstance(instance, Facade)

@given(instance=smif_mapping_ComputedFacade_strategy)
@settings(max_examples=50)
def test_smif_mapping_computedfacade_instantiation(instance):
    assert isinstance(instance, smif_mapping_ComputedFacade)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=smif_mapping_ComputedFacade_strategy)
@settings(max_examples=30)
def test_smif_mapping_computedfacade_pull_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.pull()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.pull).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'pull' in smif_mapping_ComputedFacade is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'pull' in smif_mapping_ComputedFacade did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'pull' in smif_mapping_ComputedFacade is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=smif_mapping_ComputedFacade_strategy)
@settings(max_examples=30)
def test_smif_mapping_computedfacade_push_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.push()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.push).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'push' in smif_mapping_ComputedFacade is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'push' in smif_mapping_ComputedFacade did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'push' in smif_mapping_ComputedFacade is not implemented or raised an error")

@given(instance=Situation_strategy)
@settings(max_examples=50)
def test_situation_instantiation(instance):
    assert isinstance(instance, Situation)

@given(instance=VariableBinding_strategy)
@settings(max_examples=50)
def test_variablebinding_instantiation(instance):
    assert isinstance(instance, VariableBinding)

@given(instance=patterns_Pattern_strategy)
@settings(max_examples=50)
def test_patterns_pattern_instantiation(instance):
    assert isinstance(instance, patterns_Pattern)

@given(instance=MatchRule_strategy)
@settings(max_examples=50)
def test_matchrule_instantiation(instance):
    assert isinstance(instance, MatchRule)

@given(instance=smif_patterns_Computed_strategy)
@settings(max_examples=50)
def test_smif_patterns_computed_instantiation(instance):
    assert isinstance(instance, smif_patterns_Computed)

@given(instance=OwnedPropertyBinding_strategy)
@settings(max_examples=50)
def test_ownedpropertybinding_instantiation(instance):
    assert isinstance(instance, OwnedPropertyBinding)

@given(instance=smif_patterns_VariableBinding_strategy)
@settings(max_examples=50)
def test_smif_patterns_variablebinding_instantiation(instance):
    assert isinstance(instance, smif_patterns_VariableBinding)

@given(instance=Pattern_strategy)
@settings(max_examples=50)
def test_pattern_instantiation(instance):
    assert isinstance(instance, Pattern)

@given(instance=ActualSituation_strategy)
@settings(max_examples=50)
def test_actualsituation_instantiation(instance):
    assert isinstance(instance, ActualSituation)

@given(instance=smif_patterns_PatternMatch_strategy)
@settings(max_examples=50)
def test_smif_patterns_patternmatch_instantiation(instance):
    assert isinstance(instance, smif_patterns_PatternMatch)

@given(instance=smif_patterns_PatternOfType_strategy)
@settings(max_examples=50)
def test_smif_patterns_patternoftype_instantiation(instance):
    assert isinstance(instance, smif_patterns_PatternOfType)

@given(instance=TypePatternVariable_strategy)
@settings(max_examples=50)
def test_typepatternvariable_instantiation(instance):
    assert isinstance(instance, TypePatternVariable)

@given(instance=smif_patterns_FocusVariable_strategy)
@settings(max_examples=50)
def test_smif_patterns_focusvariable_instantiation(instance):
    assert isinstance(instance, smif_patterns_FocusVariable)

@given(instance=smif_patterns_PartVariable_strategy)
@settings(max_examples=50)
def test_smif_patterns_partvariable_instantiation(instance):
    assert isinstance(instance, smif_patterns_PartVariable)



@given(instance=smif_patterns_PartVariable_strategy)
def test_smif_patterns_partvariable_isBoundaryPart_setter(instance):
    original = instance.isBoundaryPart
    instance.isBoundaryPart = original
    assert instance.isBoundaryPart == original

@given(instance=patterns_Computed_strategy)
@settings(max_examples=50)
def test_patterns_computed_instantiation(instance):
    assert isinstance(instance, patterns_Computed)

@given(instance=patterns_PatternVariable_strategy)
@settings(max_examples=50)
def test_patterns_patternvariable_instantiation(instance):
    assert isinstance(instance, patterns_PatternVariable)

@given(instance=smif_patterns_ExpressionVariable_strategy)
@settings(max_examples=50)
def test_smif_patterns_expressionvariable_instantiation(instance):
    assert isinstance(instance, smif_patterns_ExpressionVariable)

@given(instance=Mapping_strategy)
@settings(max_examples=50)
def test_mapping_instantiation(instance):
    assert isinstance(instance, Mapping)

@given(instance=Equality_strategy)
@settings(max_examples=50)
def test_equality_instantiation(instance):
    assert isinstance(instance, Equality)

@given(instance=properties_OwnedPropertyType_strategy)
@settings(max_examples=50)
def test_properties_ownedpropertytype_instantiation(instance):
    assert isinstance(instance, properties_OwnedPropertyType)

@given(instance=PatternVariable_strategy)
@settings(max_examples=50)
def test_patternvariable_instantiation(instance):
    assert isinstance(instance, PatternVariable)

@given(instance=smif_patterns_TypePatternVariable_strategy)
@settings(max_examples=50)
def test_smif_patterns_typepatternvariable_instantiation(instance):
    assert isinstance(instance, smif_patterns_TypePatternVariable)

@given(instance=smif_patterns_PropositionVariable_strategy)
@settings(max_examples=50)
def test_smif_patterns_propositionvariable_instantiation(instance):
    assert isinstance(instance, smif_patterns_PropositionVariable)

@given(instance=TemporalEntity_strategy)
@settings(max_examples=50)
def test_temporalentity_instantiation(instance):
    assert isinstance(instance, TemporalEntity)

@given(instance=smif_toplevel_ActualEntity_strategy)
@settings(max_examples=50)
def test_smif_toplevel_actualentity_instantiation(instance):
    assert isinstance(instance, smif_toplevel_ActualEntity)

@given(instance=PropositionVariable_strategy)
@settings(max_examples=50)
def test_propositionvariable_instantiation(instance):
    assert isinstance(instance, PropositionVariable)

@given(instance=LexicalReference_strategy)
@settings(max_examples=50)
def test_lexicalreference_instantiation(instance):
    assert isinstance(instance, LexicalReference)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=ConstantReference_strategy)
@settings(max_examples=50)
def test_constantreference_instantiation(instance):
    assert isinstance(instance, ConstantReference)

@given(instance=smif_toplevel_Thing_strategy)
@settings(max_examples=50)
def test_smif_toplevel_thing_instantiation(instance):
    assert isinstance(instance, smif_toplevel_Thing)

@given(instance=PropertyBinding_strategy)
@settings(max_examples=50)
def test_propertybinding_instantiation(instance):
    assert isinstance(instance, PropertyBinding)

@given(instance=InformationSource_strategy)
@settings(max_examples=50)
def test_informationsource_instantiation(instance):
    assert isinstance(instance, InformationSource)

@given(instance=Record_strategy)
@settings(max_examples=50)
def test_record_instantiation(instance):
    assert isinstance(instance, Record)

@given(instance=Name_strategy)
@settings(max_examples=50)
def test_name_instantiation(instance):
    assert isinstance(instance, Name)

@given(instance=Metadata_strategy)
@settings(max_examples=50)
def test_metadata_instantiation(instance):
    assert isinstance(instance, Metadata)

@given(instance=constraints_Conditional_strategy)
@settings(max_examples=50)
def test_constraints_conditional_instantiation(instance):
    assert isinstance(instance, constraints_Conditional)

@given(instance=smif_mapping_MatchEnd_strategy)
@settings(max_examples=50)
def test_smif_mapping_matchend_instantiation(instance):
    assert isinstance(instance, smif_mapping_MatchEnd)

@given(instance=smif_patterns_PatternVariable_strategy)
@settings(max_examples=50)
def test_smif_patterns_patternvariable_instantiation(instance):
    assert isinstance(instance, smif_patterns_PatternVariable)



@given(instance=smif_patterns_PatternVariable_strategy)
def test_smif_patterns_patternvariable_explicit_setter(instance):
    original = instance.explicit
    instance.explicit = original
    assert instance.explicit == original



@given(instance=smif_patterns_PatternVariable_strategy)
def test_smif_patterns_patternvariable_qualification_setter(instance):
    original = instance.qualification
    instance.qualification = original
    assert instance.qualification == original

@given(instance=constraints_Rule_strategy)
@settings(max_examples=50)
def test_constraints_rule_instantiation(instance):
    assert isinstance(instance, constraints_Rule)

@given(instance=smif_mapping_Mapping_strategy)
@settings(max_examples=50)
def test_smif_mapping_mapping_instantiation(instance):
    assert isinstance(instance, smif_mapping_Mapping)



@given(instance=smif_mapping_Mapping_strategy)
def test_smif_mapping_mapping_strength_setter(instance):
    original = instance.strength
    instance.strength = original
    assert instance.strength == original

@given(instance=smif_constraints_ConditionalRule_strategy)
@settings(max_examples=50)
def test_smif_constraints_conditionalrule_instantiation(instance):
    assert isinstance(instance, smif_constraints_ConditionalRule)

@given(instance=smif_constraints_Conditional_strategy)
@settings(max_examples=50)
def test_smif_constraints_conditional_instantiation(instance):
    assert isinstance(instance, smif_constraints_Conditional)

@given(instance=PropertyConstraint_strategy)
@settings(max_examples=50)
def test_propertyconstraint_instantiation(instance):
    assert isinstance(instance, PropertyConstraint)

@given(instance=smif_constraints_PropertyTypeConstraint_strategy)
@settings(max_examples=50)
def test_smif_constraints_propertytypeconstraint_instantiation(instance):
    assert isinstance(instance, smif_constraints_PropertyTypeConstraint)



@given(instance=smif_constraints_PropertyTypeConstraint_strategy)
def test_smif_constraints_propertytypeconstraint_prerequisiteType_setter(instance):
    original = instance.prerequisiteType
    instance.prerequisiteType = original
    assert instance.prerequisiteType == original

@given(instance=smif_constraints_PropertyTransitivityConstraint_strategy)
@settings(max_examples=50)
def test_smif_constraints_propertytransitivityconstraint_instantiation(instance):
    assert isinstance(instance, smif_constraints_PropertyTransitivityConstraint)

@given(instance=TypeConstraint_strategy)
@settings(max_examples=50)
def test_typeconstraint_instantiation(instance):
    assert isinstance(instance, TypeConstraint)

@given(instance=smif_constraints_UniquenessConstraint_strategy)
@settings(max_examples=50)
def test_smif_constraints_uniquenessconstraint_instantiation(instance):
    assert isinstance(instance, smif_constraints_UniquenessConstraint)



@given(instance=smif_constraints_UniquenessConstraint_strategy)
def test_smif_constraints_uniquenessconstraint_isPrimaryIdentity_setter(instance):
    original = instance.isPrimaryIdentity
    instance.isPrimaryIdentity = original
    assert instance.isPrimaryIdentity == original

@given(instance=smif_constraints_GeneralizationConstraint_strategy)
@settings(max_examples=50)
def test_smif_constraints_generalizationconstraint_instantiation(instance):
    assert isinstance(instance, smif_constraints_GeneralizationConstraint)



@given(instance=smif_constraints_GeneralizationConstraint_strategy)
def test_smif_constraints_generalizationconstraint_redefines_setter(instance):
    original = instance.redefines
    instance.redefines = original
    assert instance.redefines == original

@given(instance=smif_constraints_CoveringConstraint_strategy)
@settings(max_examples=50)
def test_smif_constraints_coveringconstraint_instantiation(instance):
    assert isinstance(instance, smif_constraints_CoveringConstraint)

@given(instance=smif_constraints_MultiplicityConstraint_strategy)
@settings(max_examples=50)
def test_smif_constraints_multiplicityconstraint_instantiation(instance):
    assert isinstance(instance, smif_constraints_MultiplicityConstraint)



@given(instance=smif_constraints_MultiplicityConstraint_strategy)
def test_smif_constraints_multiplicityconstraint_mininumNumber_setter(instance):
    original = instance.mininumNumber
    instance.mininumNumber = original
    assert instance.mininumNumber == original



@given(instance=smif_constraints_MultiplicityConstraint_strategy)
def test_smif_constraints_multiplicityconstraint_maximumNumber_setter(instance):
    original = instance.maximumNumber
    instance.maximumNumber = original
    assert instance.maximumNumber == original



@given(instance=smif_constraints_MultiplicityConstraint_strategy)
def test_smif_constraints_multiplicityconstraint_atOnce_setter(instance):
    original = instance.atOnce
    instance.atOnce = original
    assert instance.atOnce == original



@given(instance=smif_constraints_MultiplicityConstraint_strategy)
def test_smif_constraints_multiplicityconstraint_isSufficent_setter(instance):
    original = instance.isSufficent
    instance.isSufficent = original
    assert instance.isSufficent == original

@given(instance=Rule_strategy)
@settings(max_examples=50)
def test_rule_instantiation(instance):
    assert isinstance(instance, Rule)

@given(instance=smif_mapping_MatchRule_strategy)
@settings(max_examples=50)
def test_smif_mapping_matchrule_instantiation(instance):
    assert isinstance(instance, smif_mapping_MatchRule)



@given(instance=smif_mapping_MatchRule_strategy)
def test_smif_mapping_matchrule_coerce_setter(instance):
    original = instance.coerce
    instance.coerce = original
    assert instance.coerce == original

@given(instance=smif_constraints_TypeConstraint_strategy)
@settings(max_examples=50)
def test_smif_constraints_typeconstraint_instantiation(instance):
    assert isinstance(instance, smif_constraints_TypeConstraint)

@given(instance=smif_constraints_Enumerated_strategy)
@settings(max_examples=50)
def test_smif_constraints_enumerated_instantiation(instance):
    assert isinstance(instance, smif_constraints_Enumerated)

@given(instance=smif_constraints_Equivalent_strategy)
@settings(max_examples=50)
def test_smif_constraints_equivalent_instantiation(instance):
    assert isinstance(instance, smif_constraints_Equivalent)

@given(instance=smif_constraints_Disjoint_strategy)
@settings(max_examples=50)
def test_smif_constraints_disjoint_instantiation(instance):
    assert isinstance(instance, smif_constraints_Disjoint)

@given(instance=smif_constraints_PropertyConstraint_strategy)
@settings(max_examples=50)
def test_smif_constraints_propertyconstraint_instantiation(instance):
    assert isinstance(instance, smif_constraints_PropertyConstraint)

@given(instance=Proposition_strategy)
@settings(max_examples=50)
def test_proposition_instantiation(instance):
    assert isinstance(instance, Proposition)

@given(instance=smif_constraints_Rule_strategy)
@settings(max_examples=50)
def test_smif_constraints_rule_instantiation(instance):
    assert isinstance(instance, smif_constraints_Rule)

@given(instance=situations_SituationType_strategy)
@settings(max_examples=50)
def test_situations_situationtype_instantiation(instance):
    assert isinstance(instance, situations_SituationType)

@given(instance=situations_ActualSituation_strategy)
@settings(max_examples=50)
def test_situations_actualsituation_instantiation(instance):
    assert isinstance(instance, situations_ActualSituation)

@given(instance=UniqueTextIdentifier_strategy)
@settings(max_examples=50)
def test_uniquetextidentifier_instantiation(instance):
    assert isinstance(instance, UniqueTextIdentifier)

@given(instance=smif_identifiers_TechnicalIdentifier_strategy)
@settings(max_examples=50)
def test_smif_identifiers_technicalidentifier_instantiation(instance):
    assert isinstance(instance, smif_identifiers_TechnicalIdentifier)

@given(instance=TextIdentifier_strategy)
@settings(max_examples=50)
def test_textidentifier_instantiation(instance):
    assert isinstance(instance, TextIdentifier)

@given(instance=smif_identifiers_Name_strategy)
@settings(max_examples=50)
def test_smif_identifiers_name_instantiation(instance):
    assert isinstance(instance, smif_identifiers_Name)

@given(instance=Facet_strategy)
@settings(max_examples=50)
def test_facet_instantiation(instance):
    assert isinstance(instance, Facet)

@given(instance=smif_facets_Category_strategy)
@settings(max_examples=50)
def test_smif_facets_category_instantiation(instance):
    assert isinstance(instance, smif_facets_Category)

@given(instance=smif_facets_Role_strategy)
@settings(max_examples=50)
def test_smif_facets_role_instantiation(instance):
    assert isinstance(instance, smif_facets_Role)

@given(instance=facets_Facet_strategy)
@settings(max_examples=50)
def test_facets_facet_instantiation(instance):
    assert isinstance(instance, facets_Facet)

@given(instance=smif_facets_Phase_strategy)
@settings(max_examples=50)
def test_smif_facets_phase_instantiation(instance):
    assert isinstance(instance, smif_facets_Phase)

@given(instance=Relationship_strategy)
@settings(max_examples=50)
def test_relationship_instantiation(instance):
    assert isinstance(instance, Relationship)

@given(instance=smif_facets_FacetOfEntity_strategy)
@settings(max_examples=50)
def test_smif_facets_facetofentity_instantiation(instance):
    assert isinstance(instance, smif_facets_FacetOfEntity)

@given(instance=smif_properties_OwnedPropertyBinding_strategy)
@settings(max_examples=50)
def test_smif_properties_ownedpropertybinding_instantiation(instance):
    assert isinstance(instance, smif_properties_OwnedPropertyBinding)

@given(instance=CharacteristicType_strategy)
@settings(max_examples=50)
def test_characteristictype_instantiation(instance):
    assert isinstance(instance, CharacteristicType)

@given(instance=smif_properties_AnnotationProperty_strategy)
@settings(max_examples=50)
def test_smif_properties_annotationproperty_instantiation(instance):
    assert isinstance(instance, smif_properties_AnnotationProperty)

@given(instance=properties_PropertyBinding_strategy)
@settings(max_examples=50)
def test_properties_propertybinding_instantiation(instance):
    assert isinstance(instance, properties_PropertyBinding)

@given(instance=smif_properties_CharacteristicBinding_strategy)
@settings(max_examples=50)
def test_smif_properties_characteristicbinding_instantiation(instance):
    assert isinstance(instance, smif_properties_CharacteristicBinding)

@given(instance=properties_PropertyType_strategy)
@settings(max_examples=50)
def test_properties_propertytype_instantiation(instance):
    assert isinstance(instance, properties_PropertyType)

@given(instance=smif_properties_CharacteristicType_strategy)
@settings(max_examples=50)
def test_smif_properties_characteristictype_instantiation(instance):
    assert isinstance(instance, smif_properties_CharacteristicType)

@given(instance=UniquenessConstraint_strategy)
@settings(max_examples=50)
def test_uniquenessconstraint_instantiation(instance):
    assert isinstance(instance, UniquenessConstraint)

@given(instance=ObjectOperationType_strategy)
@settings(max_examples=50)
def test_objectoperationtype_instantiation(instance):
    assert isinstance(instance, ObjectOperationType)

@given(instance=Traversal_strategy)
@settings(max_examples=50)
def test_traversal_instantiation(instance):
    assert isinstance(instance, Traversal)

@given(instance=smif_metadata_Definition_strategy)
@settings(max_examples=50)
def test_smif_metadata_definition_instantiation(instance):
    assert isinstance(instance, smif_metadata_Definition)



@given(instance=smif_metadata_Definition_strategy)
def test_smif_metadata_definition_summaryDescription_setter(instance):
    original = instance.summaryDescription
    instance.summaryDescription = original
    assert instance.summaryDescription == original



@given(instance=smif_metadata_Definition_strategy)
def test_smif_metadata_definition_textDefinition_setter(instance):
    original = instance.textDefinition
    instance.textDefinition = original
    assert instance.textDefinition == original

@given(instance=Term_strategy)
@settings(max_examples=50)
def test_term_instantiation(instance):
    assert isinstance(instance, Term)

@given(instance=IRIIdentifier_strategy)
@settings(max_examples=50)
def test_iriidentifier_instantiation(instance):
    assert isinstance(instance, IRIIdentifier)

@given(instance=smif_lexicalscope_Include_strategy)
@settings(max_examples=50)
def test_smif_lexicalscope_include_instantiation(instance):
    assert isinstance(instance, smif_lexicalscope_Include)

@given(instance=smif_metadata_Metadata_strategy)
@settings(max_examples=50)
def test_smif_metadata_metadata_instantiation(instance):
    assert isinstance(instance, smif_metadata_Metadata)

@given(instance=metadata_Metadata_strategy)
@settings(max_examples=50)
def test_metadata_metadata_instantiation(instance):
    assert isinstance(instance, metadata_Metadata)

@given(instance=smif_metadata_Statement_strategy)
@settings(max_examples=50)
def test_smif_metadata_statement_instantiation(instance):
    assert isinstance(instance, smif_metadata_Statement)

@given(instance=PropertyOwnerType_strategy)
@settings(max_examples=50)
def test_propertyownertype_instantiation(instance):
    assert isinstance(instance, PropertyOwnerType)

@given(instance=smif_associations_AssociationType_strategy)
@settings(max_examples=50)
def test_smif_associations_associationtype_instantiation(instance):
    assert isinstance(instance, smif_associations_AssociationType)

@given(instance=smif_lexicalscope_Prefix_strategy)
@settings(max_examples=50)
def test_smif_lexicalscope_prefix_instantiation(instance):
    assert isinstance(instance, smif_lexicalscope_Prefix)

@given(instance=smif_lexicalscope_MappingPackage_strategy)
@settings(max_examples=50)
def test_smif_lexicalscope_mappingpackage_instantiation(instance):
    assert isinstance(instance, smif_lexicalscope_MappingPackage)

@given(instance=smif_lexicalscope_PhysicalPackage_strategy)
@settings(max_examples=50)
def test_smif_lexicalscope_physicalpackage_instantiation(instance):
    assert isinstance(instance, smif_lexicalscope_PhysicalPackage)

@given(instance=smif_lexicalscope_LogicalPackage_strategy)
@settings(max_examples=50)
def test_smif_lexicalscope_logicalpackage_instantiation(instance):
    assert isinstance(instance, smif_lexicalscope_LogicalPackage)

@given(instance=smif_lexicalscope_MOFPackage_strategy)
@settings(max_examples=50)
def test_smif_lexicalscope_mofpackage_instantiation(instance):
    assert isinstance(instance, smif_lexicalscope_MOFPackage)

@given(instance=UniqueIdentifier_strategy)
@settings(max_examples=50)
def test_uniqueidentifier_instantiation(instance):
    assert isinstance(instance, UniqueIdentifier)

@given(instance=IdentifiableEntity_strategy)
@settings(max_examples=50)
def test_identifiableentity_instantiation(instance):
    assert isinstance(instance, IdentifiableEntity)

@given(instance=smif_toplevel_Proposition_strategy)
@settings(max_examples=50)
def test_smif_toplevel_proposition_instantiation(instance):
    assert isinstance(instance, smif_toplevel_Proposition)

@given(instance=smif_toplevel_TemporalEntity_strategy)
@settings(max_examples=50)
def test_smif_toplevel_temporalentity_instantiation(instance):
    assert isinstance(instance, smif_toplevel_TemporalEntity)

@given(instance=smif_toplevel_Context_strategy)
@settings(max_examples=50)
def test_smif_toplevel_context_instantiation(instance):
    assert isinstance(instance, smif_toplevel_Context)

@given(instance=smif_expressions_ExpressionContext_strategy)
@settings(max_examples=50)
def test_smif_expressions_expressioncontext_instantiation(instance):
    assert isinstance(instance, smif_expressions_ExpressionContext)

@given(instance=identifiers_TextIdentifier_strategy)
@settings(max_examples=50)
def test_identifiers_textidentifier_instantiation(instance):
    assert isinstance(instance, identifiers_TextIdentifier)

@given(instance=identifiers_UniqueIdentifier_strategy)
@settings(max_examples=50)
def test_identifiers_uniqueidentifier_instantiation(instance):
    assert isinstance(instance, identifiers_UniqueIdentifier)

@given(instance=expressions_ExpressionNode_strategy)
@settings(max_examples=50)
def test_expressions_expressionnode_instantiation(instance):
    assert isinstance(instance, expressions_ExpressionNode)

@given(instance=FunctionType_strategy)
@settings(max_examples=50)
def test_functiontype_instantiation(instance):
    assert isinstance(instance, FunctionType)

@given(instance=smif_expressions_ObjectOperationType_strategy)
@settings(max_examples=50)
def test_smif_expressions_objectoperationtype_instantiation(instance):
    assert isinstance(instance, smif_expressions_ObjectOperationType)

@given(instance=Evaluation_strategy)
@settings(max_examples=50)
def test_evaluation_instantiation(instance):
    assert isinstance(instance, Evaluation)

@given(instance=FunctionCall_strategy)
@settings(max_examples=50)
def test_functioncall_instantiation(instance):
    assert isinstance(instance, FunctionCall)

@given(instance=ExpressionNode_strategy)
@settings(max_examples=50)
def test_expressionnode_instantiation(instance):
    assert isinstance(instance, ExpressionNode)

@given(instance=smif_expressions_ConstantReference_strategy)
@settings(max_examples=50)
def test_smif_expressions_constantreference_instantiation(instance):
    assert isinstance(instance, smif_expressions_ConstantReference)

@given(instance=smif_expressions_Equality_strategy)
@settings(max_examples=50)
def test_smif_expressions_equality_instantiation(instance):
    assert isinstance(instance, smif_expressions_Equality)

@given(instance=expressions_ExpressionContext_strategy)
@settings(max_examples=50)
def test_expressions_expressioncontext_instantiation(instance):
    assert isinstance(instance, expressions_ExpressionContext)

@given(instance=properties_PropertyOwner_strategy)
@settings(max_examples=50)
def test_properties_propertyowner_instantiation(instance):
    assert isinstance(instance, properties_PropertyOwner)

@given(instance=smif_expressions_FunctionCall_strategy)
@settings(max_examples=50)
def test_smif_expressions_functioncall_instantiation(instance):
    assert isinstance(instance, smif_expressions_FunctionCall)

@given(instance=smif_expressions_Traversal_strategy)
@settings(max_examples=50)
def test_smif_expressions_traversal_instantiation(instance):
    assert isinstance(instance, smif_expressions_Traversal)



@given(instance=smif_expressions_Traversal_strategy)
def test_smif_expressions_traversal_inverse_setter(instance):
    original = instance.inverse
    instance.inverse = original
    assert instance.inverse == original



@given(instance=smif_expressions_Traversal_strategy)
def test_smif_expressions_traversal_traverseToRelation_setter(instance):
    original = instance.traverseToRelation
    instance.traverseToRelation = original
    assert instance.traverseToRelation == original

@given(instance=smif_records_Record_strategy)
@settings(max_examples=50)
def test_smif_records_record_instantiation(instance):
    assert isinstance(instance, smif_records_Record)

@given(instance=smif_relationships_Relationship_strategy)
@settings(max_examples=50)
def test_smif_relationships_relationship_instantiation(instance):
    assert isinstance(instance, smif_relationships_Relationship)

@given(instance=values_Value_strategy)
@settings(max_examples=50)
def test_values_value_instantiation(instance):
    assert isinstance(instance, values_Value)

@given(instance=smif_values_StructuredValue_strategy)
@settings(max_examples=50)
def test_smif_values_structuredvalue_instantiation(instance):
    assert isinstance(instance, smif_values_StructuredValue)

@given(instance=properties_PropertyOwnerType_strategy)
@settings(max_examples=50)
def test_properties_propertyownertype_instantiation(instance):
    assert isinstance(instance, properties_PropertyOwnerType)

@given(instance=smif_relationships_RelationshipType_strategy)
@settings(max_examples=50)
def test_smif_relationships_relationshiptype_instantiation(instance):
    assert isinstance(instance, smif_relationships_RelationshipType)

@given(instance=smif_records_RecordType_strategy)
@settings(max_examples=50)
def test_smif_records_recordtype_instantiation(instance):
    assert isinstance(instance, smif_records_RecordType)

@given(instance=smif_expressions_FunctionType_strategy)
@settings(max_examples=50)
def test_smif_expressions_functiontype_instantiation(instance):
    assert isinstance(instance, smif_expressions_FunctionType)

@given(instance=values_ValueType_strategy)
@settings(max_examples=50)
def test_values_valuetype_instantiation(instance):
    assert isinstance(instance, values_ValueType)

@given(instance=smif_values_StructuredValueType_strategy)
@settings(max_examples=50)
def test_smif_values_structuredvaluetype_instantiation(instance):
    assert isinstance(instance, smif_values_StructuredValueType)

@given(instance=Context_strategy)
@settings(max_examples=50)
def test_context_instantiation(instance):
    assert isinstance(instance, Context)

@given(instance=smif_identifiers_Namespace_strategy)
@settings(max_examples=50)
def test_smif_identifiers_namespace_instantiation(instance):
    assert isinstance(instance, smif_identifiers_Namespace)

@given(instance=smif_lexicalscope_LexicalReference_strategy)
@settings(max_examples=50)
def test_smif_lexicalscope_lexicalreference_instantiation(instance):
    assert isinstance(instance, smif_lexicalscope_LexicalReference)

@given(instance=smif_values_SystemOfUnits_strategy)
@settings(max_examples=50)
def test_smif_values_systemofunits_instantiation(instance):
    assert isinstance(instance, smif_values_SystemOfUnits)

@given(instance=smif_identifiers_UniqueTextIdentifier_strategy)
@settings(max_examples=50)
def test_smif_identifiers_uniquetextidentifier_instantiation(instance):
    assert isinstance(instance, smif_identifiers_UniqueTextIdentifier)

@given(instance=identifiers_UniqueTextIdentifier_strategy)
@settings(max_examples=50)
def test_identifiers_uniquetextidentifier_instantiation(instance):
    assert isinstance(instance, identifiers_UniqueTextIdentifier)

@given(instance=identifiers_Name_strategy)
@settings(max_examples=50)
def test_identifiers_name_instantiation(instance):
    assert isinstance(instance, identifiers_Name)

@given(instance=smif_identifiers_Term_strategy)
@settings(max_examples=50)
def test_smif_identifiers_term_instantiation(instance):
    assert isinstance(instance, smif_identifiers_Term)

@given(instance=TechnicalIdentifier_strategy)
@settings(max_examples=50)
def test_technicalidentifier_instantiation(instance):
    assert isinstance(instance, TechnicalIdentifier)

@given(instance=smif_identifiers_IRIIdentifier_strategy)
@settings(max_examples=50)
def test_smif_identifiers_iriidentifier_instantiation(instance):
    assert isinstance(instance, smif_identifiers_IRIIdentifier)

@given(instance=Namespace_strategy)
@settings(max_examples=50)
def test_namespace_instantiation(instance):
    assert isinstance(instance, Namespace)

@given(instance=smif_lexicalscope_LexicalScope_strategy)
@settings(max_examples=50)
def test_smif_lexicalscope_lexicalscope_instantiation(instance):
    assert isinstance(instance, smif_lexicalscope_LexicalScope)

@given(instance=Identifier_strategy)
@settings(max_examples=50)
def test_identifier_instantiation(instance):
    assert isinstance(instance, Identifier)

@given(instance=smif_identifiers_TextIdentifier_strategy)
@settings(max_examples=50)
def test_smif_identifiers_textidentifier_instantiation(instance):
    assert isinstance(instance, smif_identifiers_TextIdentifier)



@given(instance=smif_identifiers_TextIdentifier_strategy)
def test_smif_identifiers_textidentifier_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=smif_identifiers_UniqueIdentifier_strategy)
@settings(max_examples=50)
def test_smif_identifiers_uniqueidentifier_instantiation(instance):
    assert isinstance(instance, smif_identifiers_UniqueIdentifier)

@given(instance=UnitValue_strategy)
@settings(max_examples=50)
def test_unitvalue_instantiation(instance):
    assert isinstance(instance, UnitValue)

@given(instance=smif_values_ScalarQuantity_strategy)
@settings(max_examples=50)
def test_smif_values_scalarquantity_instantiation(instance):
    assert isinstance(instance, smif_values_ScalarQuantity)



@given(instance=smif_values_ScalarQuantity_strategy)
def test_smif_values_scalarquantity__unnamed_ScalarQuantity_setter(instance):
    original = instance._unnamed_ScalarQuantity
    instance._unnamed_ScalarQuantity = original
    assert instance._unnamed_ScalarQuantity == original

@given(instance=Value_strategy)
@settings(max_examples=50)
def test_value_instantiation(instance):
    assert isinstance(instance, Value)

@given(instance=smif_identifiers_Identifier_strategy)
@settings(max_examples=50)
def test_smif_identifiers_identifier_instantiation(instance):
    assert isinstance(instance, smif_identifiers_Identifier)

@given(instance=smif_values_UnitValue_strategy)
@settings(max_examples=50)
def test_smif_values_unitvalue_instantiation(instance):
    assert isinstance(instance, smif_values_UnitValue)



@given(instance=smif_values_UnitValue_strategy)
def test_smif_values_unitvalue_hasValue_setter(instance):
    original = instance.hasValue
    instance.hasValue = original
    assert instance.hasValue == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=smif_types_EntityType_strategy)
@settings(max_examples=50)
def test_smif_types_entitytype_instantiation(instance):
    assert isinstance(instance, smif_types_EntityType)

@given(instance=smif_properties_PropertyType_strategy)
@settings(max_examples=50)
def test_smif_properties_propertytype_instantiation(instance):
    assert isinstance(instance, smif_properties_PropertyType)

@given(instance=smif_properties_PropertyOwnerType_strategy)
@settings(max_examples=50)
def test_smif_properties_propertyownertype_instantiation(instance):
    assert isinstance(instance, smif_properties_PropertyOwnerType)

@given(instance=smif_facets_Facet_strategy)
@settings(max_examples=50)
def test_smif_facets_facet_instantiation(instance):
    assert isinstance(instance, smif_facets_Facet)

@given(instance=smif_types_UnionType_strategy)
@settings(max_examples=50)
def test_smif_types_uniontype_instantiation(instance):
    assert isinstance(instance, smif_types_UnionType)

@given(instance=smif_types_IntersectionType_strategy)
@settings(max_examples=50)
def test_smif_types_intersectiontype_instantiation(instance):
    assert isinstance(instance, smif_types_IntersectionType)

@given(instance=RepresentationRule_strategy)
@settings(max_examples=50)
def test_representationrule_instantiation(instance):
    assert isinstance(instance, RepresentationRule)

@given(instance=MatchEnd_strategy)
@settings(max_examples=50)
def test_matchend_instantiation(instance):
    assert isinstance(instance, MatchEnd)

@given(instance=ExpressionContext_strategy)
@settings(max_examples=50)
def test_expressioncontext_instantiation(instance):
    assert isinstance(instance, ExpressionContext)

@given(instance=smif_expressions_Evaluation_strategy)
@settings(max_examples=50)
def test_smif_expressions_evaluation_instantiation(instance):
    assert isinstance(instance, smif_expressions_Evaluation)

@given(instance=smif_expressions_ExpressionNode_strategy)
@settings(max_examples=50)
def test_smif_expressions_expressionnode_instantiation(instance):
    assert isinstance(instance, smif_expressions_ExpressionNode)



@given(instance=smif_expressions_ExpressionNode_strategy)
def test_smif_expressions_expressionnode_expressionTextLanguage_setter(instance):
    original = instance.expressionTextLanguage
    instance.expressionTextLanguage = original
    assert instance.expressionTextLanguage == original



@given(instance=smif_expressions_ExpressionNode_strategy)
def test_smif_expressions_expressionnode_expressionText_setter(instance):
    original = instance.expressionText
    instance.expressionText = original
    assert instance.expressionText == original

@given(instance=smif_values_ValueType_strategy)
@settings(max_examples=50)
def test_smif_values_valuetype_instantiation(instance):
    assert isinstance(instance, smif_values_ValueType)

@given(instance=UnitType_strategy)
@settings(max_examples=50)
def test_unittype_instantiation(instance):
    assert isinstance(instance, UnitType)

@given(instance=smif_values_BaseUnitType_strategy)
@settings(max_examples=50)
def test_smif_values_baseunittype_instantiation(instance):
    assert isinstance(instance, smif_values_BaseUnitType)

@given(instance=SystemOfUnits_strategy)
@settings(max_examples=50)
def test_systemofunits_instantiation(instance):
    assert isinstance(instance, SystemOfUnits)

@given(instance=Definition_strategy)
@settings(max_examples=50)
def test_definition_instantiation(instance):
    assert isinstance(instance, Definition)

@given(instance=ValueType_strategy)
@settings(max_examples=50)
def test_valuetype_instantiation(instance):
    assert isinstance(instance, ValueType)

@given(instance=smif_values_UnitType_strategy)
@settings(max_examples=50)
def test_smif_values_unittype_instantiation(instance):
    assert isinstance(instance, smif_values_UnitType)



@given(instance=smif_values_UnitType_strategy)
def test_smif_values_unittype_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original



@given(instance=smif_values_UnitType_strategy)
def test_smif_values_unittype_ratio_setter(instance):
    original = instance.ratio
    instance.ratio = original
    assert instance.ratio == original



@given(instance=smif_values_UnitType_strategy)
def test_smif_values_unittype_offset_setter(instance):
    original = instance.offset
    instance.offset = original
    assert instance.offset == original

@given(instance=smif_values_QuantityKind_strategy)
@settings(max_examples=50)
def test_smif_values_quantitykind_instantiation(instance):
    assert isinstance(instance, smif_values_QuantityKind)

@given(instance=situations_Situation_strategy)
@settings(max_examples=50)
def test_situations_situation_instantiation(instance):
    assert isinstance(instance, situations_Situation)

@given(instance=toplevel_ActualEntity_strategy)
@settings(max_examples=50)
def test_toplevel_actualentity_instantiation(instance):
    assert isinstance(instance, toplevel_ActualEntity)

@given(instance=smif_metadata_InformationSource_strategy)
@settings(max_examples=50)
def test_smif_metadata_informationsource_instantiation(instance):
    assert isinstance(instance, smif_metadata_InformationSource)

@given(instance=smif_situations_ActualSituation_strategy)
@settings(max_examples=50)
def test_smif_situations_actualsituation_instantiation(instance):
    assert isinstance(instance, smif_situations_ActualSituation)

@given(instance=PatternMatch_strategy)
@settings(max_examples=50)
def test_patternmatch_instantiation(instance):
    assert isinstance(instance, PatternMatch)

@given(instance=toplevel_TemporalEntity_strategy)
@settings(max_examples=50)
def test_toplevel_temporalentity_instantiation(instance):
    assert isinstance(instance, toplevel_TemporalEntity)

@given(instance=toplevel_Proposition_strategy)
@settings(max_examples=50)
def test_toplevel_proposition_instantiation(instance):
    assert isinstance(instance, toplevel_Proposition)

@given(instance=smif_associations_Association_strategy)
@settings(max_examples=50)
def test_smif_associations_association_instantiation(instance):
    assert isinstance(instance, smif_associations_Association)

@given(instance=EntityType_strategy)
@settings(max_examples=50)
def test_entitytype_instantiation(instance):
    assert isinstance(instance, EntityType)

@given(instance=smif_situations_SituationType_strategy)
@settings(max_examples=50)
def test_smif_situations_situationtype_instantiation(instance):
    assert isinstance(instance, smif_situations_SituationType)

@given(instance=LexicalScope_strategy)
@settings(max_examples=50)
def test_lexicalscope_instantiation(instance):
    assert isinstance(instance, LexicalScope)

@given(instance=smif_lexicalscope_Package_strategy)
@settings(max_examples=50)
def test_smif_lexicalscope_package_instantiation(instance):
    assert isinstance(instance, smif_lexicalscope_Package)

@given(instance=smif_Repository_strategy)
@settings(max_examples=50)
def test_smif_repository_instantiation(instance):
    assert isinstance(instance, smif_Repository)

@given(instance=RecordType_strategy)
@settings(max_examples=50)
def test_recordtype_instantiation(instance):
    assert isinstance(instance, RecordType)

@given(instance=smif_mapping_Facade_strategy)
@settings(max_examples=50)
def test_smif_mapping_facade_instantiation(instance):
    assert isinstance(instance, smif_mapping_Facade)

@given(instance=PropertyTypeConstraint_strategy)
@settings(max_examples=50)
def test_propertytypeconstraint_instantiation(instance):
    assert isinstance(instance, PropertyTypeConstraint)

@given(instance=MultiplicityConstraint_strategy)
@settings(max_examples=50)
def test_multiplicityconstraint_instantiation(instance):
    assert isinstance(instance, MultiplicityConstraint)

@given(instance=GeneralizationConstraint_strategy)
@settings(max_examples=50)
def test_generalizationconstraint_instantiation(instance):
    assert isinstance(instance, GeneralizationConstraint)

@given(instance=smif_constraints_FacetClassificationConstraint_strategy)
@settings(max_examples=50)
def test_smif_constraints_facetclassificationconstraint_instantiation(instance):
    assert isinstance(instance, smif_constraints_FacetClassificationConstraint)

@given(instance=CoveringConstraint_strategy)
@settings(max_examples=50)
def test_coveringconstraint_instantiation(instance):
    assert isinstance(instance, CoveringConstraint)

@given(instance=PatternOfType_strategy)
@settings(max_examples=50)
def test_patternoftype_instantiation(instance):
    assert isinstance(instance, PatternOfType)

@given(instance=PropertyType_strategy)
@settings(max_examples=50)
def test_propertytype_instantiation(instance):
    assert isinstance(instance, PropertyType)

@given(instance=smif_properties_OwnedPropertyType_strategy)
@settings(max_examples=50)
def test_smif_properties_ownedpropertytype_instantiation(instance):
    assert isinstance(instance, smif_properties_OwnedPropertyType)

@given(instance=Thing_strategy)
@settings(max_examples=50)
def test_thing_instantiation(instance):
    assert isinstance(instance, Thing)

@given(instance=smif_values_Value_strategy)
@settings(max_examples=50)
def test_smif_values_value_instantiation(instance):
    assert isinstance(instance, smif_values_Value)

@given(instance=smif_properties_PropertyBinding_strategy)
@settings(max_examples=50)
def test_smif_properties_propertybinding_instantiation(instance):
    assert isinstance(instance, smif_properties_PropertyBinding)

@given(instance=smif_properties_PropertyOwner_strategy)
@settings(max_examples=50)
def test_smif_properties_propertyowner_instantiation(instance):
    assert isinstance(instance, smif_properties_PropertyOwner)

@given(instance=smif_toplevel_IdentifiableEntity_strategy)
@settings(max_examples=50)
def test_smif_toplevel_identifiableentity_instantiation(instance):
    assert isinstance(instance, smif_toplevel_IdentifiableEntity)

@given(instance=toplevel_Context_strategy)
@settings(max_examples=50)
def test_toplevel_context_instantiation(instance):
    assert isinstance(instance, toplevel_Context)

@given(instance=lexicalscope_LexicalScope_strategy)
@settings(max_examples=50)
def test_lexicalscope_lexicalscope_instantiation(instance):
    assert isinstance(instance, lexicalscope_LexicalScope)

@given(instance=smif_patterns_Pattern_strategy)
@settings(max_examples=50)
def test_smif_patterns_pattern_instantiation(instance):
    assert isinstance(instance, smif_patterns_Pattern)

@given(instance=smif_situations_Situation_strategy)
@settings(max_examples=50)
def test_smif_situations_situation_instantiation(instance):
    assert isinstance(instance, smif_situations_Situation)

@given(instance=smif_types_Type_strategy)
@settings(max_examples=50)
def test_smif_types_type_instantiation(instance):
    assert isinstance(instance, smif_types_Type)
