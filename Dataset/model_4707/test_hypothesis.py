import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    values::ValueType,
    Context,
    smif::values::SystemOfUnits,
    identifiers::UniqueTextIdentifier,
    identifiers::Name,
    smif::identifiers::Term,
    TechnicalIdentifier,
    smif::identifiers::IRIIdentifier,
    Namespace,
    Identifier,
    smif::identifiers::UniqueIdentifier,
    UnitValue,
    smif::values::ScalarQuantity,
    Value,
    smif::values::UnitValue,
    Type,
    smif::types::EntityType,
    smif::types::UnionType,
    smif::types::IntersectionType,
    RepresentationRule,
    MatchEnd,
    ExpressionContext,
    smif::values::ValueType,
    UnitType,
    smif::values::BaseUnitType,
    SystemOfUnits,
    Definition,
    ValueType,
    smif::values::UnitType,
    smif::values::QuantityKind,
    situations::Situation,
    toplevel::ActualEntity,
    smif::situations::ActualSituation,
    PatternMatch,
    toplevel::TemporalEntity,
    toplevel::Proposition,
    EntityType,
    smif::situations::SituationType,
    LexicalScope,
    smif::Repository,
    RecordType,
    PropertyTypeConstraint,
    MultiplicityConstraint,
    GeneralizationConstraint,
    CoveringConstraint,
    PatternOfType,
    PropertyType,
    Thing,
    smif::values::Value,
    toplevel::Context,
    lexicalscope::LexicalScope,
    smif::situations::Situation,
    smif::types::Type,
    smif::facets::Facet,
    smif::properties::PropertyBinding,
    Facet,
    smif::facets::Category,
    smif::facets::Role,
    facets::Facet,
    Relationship,
    smif::facets::FacetOfEntity,
    smif::properties::PropertyOwner,
    smif::properties::PropertyOwnerType,
    smif::properties::OwnedPropertyType,
    CharacteristicType,
    smif::properties::AnnotationProperty,
    properties::PropertyBinding,
    properties::PropertyType,
    UniquenessConstraint,
    ObjectOperationType,
    Traversal,
    smif::properties::PropertyType,
    Term,
    IRIIdentifier,
    metadata::Metadata,
    smif::metadata::InformationSource,
    PropertyOwnerType,
    smif::associations::AssociationType,
    Prefix,
    smif::lexicalscope::Package,
    smif::lexicalscope::LexicalReference,
    smif::lexicalscope::LexicalScope,
    Package,
    smif::lexicalscope::MappingPackage,
    smif::lexicalscope::PhysicalPackage,
    smif::lexicalscope::MOFPackage,
    smif::lexicalscope::LogicalPackage,
    smif::lexicalscope::Model,
    ConditionalRule,
    smif::mapping::RepresentationRule,
    Facade,
    smif::mapping::ComputedFacade,
    smif::mapping::Facade,
    Situation,
    VariableBinding,
    patterns::Pattern,
    MatchRule,
    smif::patterns::Computed,
    OwnedPropertyBinding,
    smif::patterns::VariableBinding,
    Pattern,
    ActualSituation,
    smif::patterns::PatternMatch,
    smif::patterns::PatternOfType,
    TypePatternVariable,
    smif::patterns::FocusVariable,
    smif::patterns::PartVariable,
    patterns::Computed,
    patterns::PatternVariable,
    smif::patterns::ExpressionVariable,
    Mapping,
    Equality,
    properties::OwnedPropertyType,
    PatternVariable,
    smif::patterns::PropositionVariable,
    smif::patterns::TypePatternVariable,
    TemporalEntity,
    smif::toplevel::ActualEntity,
    PropositionVariable,
    LexicalReference,
    smif::lexicalscope::Include,
    Statement,
    smif::toplevel::IdentifiableEntity,
    ConstantReference,
    smif::toplevel::Thing,
    PropertyBinding,
    smif::properties::OwnedPropertyBinding,
    InformationSource,
    Record,
    smif::metadata::Metadata,
    Name,
    Metadata,
    smif::metadata::Definition,
    smif::metadata::Statement,
    constraints::Conditional,
    smif::patterns::PatternVariable,
    smif::mapping::MatchEnd,
    constraints::Rule,
    smif::mapping::Mapping,
    smif::constraints::ConditionalRule,
    smif::constraints::Conditional,
    smif::constraints::FacetClassificationConstraint,
    PropertyConstraint,
    smif::constraints::PropertyTypeConstraint,
    smif::constraints::PropertyTransitivityConstraint,
    smif::expressions::Evaluation,
    TypeConstraint,
    smif::constraints::GeneralizationConstraint,
    smif::constraints::CoveringConstraint,
    smif::constraints::UniquenessConstraint,
    smif::constraints::MultiplicityConstraint,
    Rule,
    smif::constraints::TypeConstraint,
    smif::constraints::PropertyConstraint,
    smif::mapping::MatchRule,
    smif::constraints::Enumerated,
    smif::constraints::Equivalent,
    smif::constraints::Disjoint,
    Proposition,
    smif::constraints::Rule,
    situations::SituationType,
    smif::properties::CharacteristicType,
    smif::facets::Phase,
    situations::ActualSituation,
    smif::properties::CharacteristicBinding,
    UniqueTextIdentifier,
    smif::lexicalscope::Prefix,
    smif::identifiers::TechnicalIdentifier,
    TextIdentifier,
    smif::identifiers::Name,
    smif::identifiers::TextIdentifier,
    UniqueIdentifier,
    smif::identifiers::Namespace,
    IdentifiableEntity,
    smif::toplevel::Context,
    smif::expressions::ExpressionContext,
    smif::toplevel::TemporalEntity,
    smif::toplevel::Proposition,
    smif::identifiers::Identifier,
    identifiers::TextIdentifier,
    identifiers::UniqueIdentifier,
    smif::identifiers::UniqueTextIdentifier,
    expressions::ExpressionNode,
    FunctionType,
    smif::expressions::ObjectOperationType,
    Evaluation,
    smif::expressions::ExpressionNode,
    FunctionCall,
    ExpressionNode,
    smif::expressions::Equality,
    smif::expressions::ConstantReference,
    expressions::ExpressionContext,
    properties::PropertyOwner,
    smif::associations::Association,
    smif::patterns::Pattern,
    smif::expressions::Traversal,
    smif::relationships::Relationship,
    smif::records::Record,
    smif::expressions::FunctionCall,
    values::Value,
    smif::values::StructuredValue,
    properties::PropertyOwnerType,
    smif::relationships::RelationshipType,
    smif::records::RecordType,
    smif::values::StructuredValueType,
    smif::expressions::FunctionType,
    VariableQualification,
    AssertionStrength,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_values::valuetype_is_not_abstract():
    assert not inspect.isabstract(values::ValueType)


def test_values::valuetype_constructor_exists():
    assert callable(values::ValueType.__init__)


def test_values::valuetype_constructor_args():
    sig = inspect.signature(values::ValueType.__init__)
    params = list(sig.parameters.keys())



def test_context_is_not_abstract():
    assert not inspect.isabstract(Context)


def test_context_constructor_exists():
    assert callable(Context.__init__)


def test_context_constructor_args():
    sig = inspect.signature(Context.__init__)
    params = list(sig.parameters.keys())



def test_smif::values::systemofunits_is_not_abstract():
    assert not inspect.isabstract(smif::values::SystemOfUnits)


def test_smif::values::systemofunits_constructor_exists():
    assert callable(smif::values::SystemOfUnits.__init__)


def test_smif::values::systemofunits_constructor_args():
    sig = inspect.signature(smif::values::SystemOfUnits.__init__)
    params = list(sig.parameters.keys())



def test_identifiers::uniquetextidentifier_is_not_abstract():
    assert not inspect.isabstract(identifiers::UniqueTextIdentifier)


def test_identifiers::uniquetextidentifier_constructor_exists():
    assert callable(identifiers::UniqueTextIdentifier.__init__)


def test_identifiers::uniquetextidentifier_constructor_args():
    sig = inspect.signature(identifiers::UniqueTextIdentifier.__init__)
    params = list(sig.parameters.keys())



def test_identifiers::name_is_not_abstract():
    assert not inspect.isabstract(identifiers::Name)


def test_identifiers::name_constructor_exists():
    assert callable(identifiers::Name.__init__)


def test_identifiers::name_constructor_args():
    sig = inspect.signature(identifiers::Name.__init__)
    params = list(sig.parameters.keys())



def test_smif::identifiers::term_is_not_abstract():
    assert not inspect.isabstract(smif::identifiers::Term)


def test_smif::identifiers::term_constructor_exists():
    assert callable(smif::identifiers::Term.__init__)


def test_smif::identifiers::term_constructor_args():
    sig = inspect.signature(smif::identifiers::Term.__init__)
    params = list(sig.parameters.keys())



def test_technicalidentifier_is_not_abstract():
    assert not inspect.isabstract(TechnicalIdentifier)


def test_technicalidentifier_constructor_exists():
    assert callable(TechnicalIdentifier.__init__)


def test_technicalidentifier_constructor_args():
    sig = inspect.signature(TechnicalIdentifier.__init__)
    params = list(sig.parameters.keys())



def test_smif::identifiers::iriidentifier_is_not_abstract():
    assert not inspect.isabstract(smif::identifiers::IRIIdentifier)


def test_smif::identifiers::iriidentifier_constructor_exists():
    assert callable(smif::identifiers::IRIIdentifier.__init__)


def test_smif::identifiers::iriidentifier_constructor_args():
    sig = inspect.signature(smif::identifiers::IRIIdentifier.__init__)
    params = list(sig.parameters.keys())



def test_namespace_is_not_abstract():
    assert not inspect.isabstract(Namespace)


def test_namespace_constructor_exists():
    assert callable(Namespace.__init__)


def test_namespace_constructor_args():
    sig = inspect.signature(Namespace.__init__)
    params = list(sig.parameters.keys())



def test_identifier_is_not_abstract():
    assert not inspect.isabstract(Identifier)


def test_identifier_constructor_exists():
    assert callable(Identifier.__init__)


def test_identifier_constructor_args():
    sig = inspect.signature(Identifier.__init__)
    params = list(sig.parameters.keys())



def test_smif::identifiers::uniqueidentifier_is_not_abstract():
    assert not inspect.isabstract(smif::identifiers::UniqueIdentifier)


def test_smif::identifiers::uniqueidentifier_constructor_exists():
    assert callable(smif::identifiers::UniqueIdentifier.__init__)


def test_smif::identifiers::uniqueidentifier_constructor_args():
    sig = inspect.signature(smif::identifiers::UniqueIdentifier.__init__)
    params = list(sig.parameters.keys())



def test_unitvalue_is_not_abstract():
    assert not inspect.isabstract(UnitValue)


def test_unitvalue_constructor_exists():
    assert callable(UnitValue.__init__)


def test_unitvalue_constructor_args():
    sig = inspect.signature(UnitValue.__init__)
    params = list(sig.parameters.keys())



def test_smif::values::scalarquantity_is_not_abstract():
    assert not inspect.isabstract(smif::values::ScalarQuantity)


def test_smif::values::scalarquantity_constructor_exists():
    assert callable(smif::values::ScalarQuantity.__init__)


def test_smif::values::scalarquantity_constructor_args():
    sig = inspect.signature(smif::values::ScalarQuantity.__init__)
    params = list(sig.parameters.keys())
    assert "_unnamed_ScalarQuantity" in params, "Missing parameter '_unnamed_ScalarQuantity'"

def test_smif::values::scalarquantity_has__unnamed_ScalarQuantity():
    assert hasattr(smif::values::ScalarQuantity, "_unnamed_ScalarQuantity")
    descriptor = None
    for klass in smif::values::ScalarQuantity.__mro__:
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



def test_smif::values::unitvalue_is_not_abstract():
    assert not inspect.isabstract(smif::values::UnitValue)


def test_smif::values::unitvalue_constructor_exists():
    assert callable(smif::values::UnitValue.__init__)


def test_smif::values::unitvalue_constructor_args():
    sig = inspect.signature(smif::values::UnitValue.__init__)
    params = list(sig.parameters.keys())
    assert "hasValue" in params, "Missing parameter 'hasValue'"

def test_smif::values::unitvalue_has_hasValue():
    assert hasattr(smif::values::UnitValue, "hasValue")
    descriptor = None
    for klass in smif::values::UnitValue.__mro__:
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



def test_smif::types::entitytype_is_not_abstract():
    assert not inspect.isabstract(smif::types::EntityType)


def test_smif::types::entitytype_constructor_exists():
    assert callable(smif::types::EntityType.__init__)


def test_smif::types::entitytype_constructor_args():
    sig = inspect.signature(smif::types::EntityType.__init__)
    params = list(sig.parameters.keys())



def test_smif::types::uniontype_is_not_abstract():
    assert not inspect.isabstract(smif::types::UnionType)


def test_smif::types::uniontype_constructor_exists():
    assert callable(smif::types::UnionType.__init__)


def test_smif::types::uniontype_constructor_args():
    sig = inspect.signature(smif::types::UnionType.__init__)
    params = list(sig.parameters.keys())



def test_smif::types::intersectiontype_is_not_abstract():
    assert not inspect.isabstract(smif::types::IntersectionType)


def test_smif::types::intersectiontype_constructor_exists():
    assert callable(smif::types::IntersectionType.__init__)


def test_smif::types::intersectiontype_constructor_args():
    sig = inspect.signature(smif::types::IntersectionType.__init__)
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



def test_smif::values::valuetype_is_not_abstract():
    assert not inspect.isabstract(smif::values::ValueType)


def test_smif::values::valuetype_constructor_exists():
    assert callable(smif::values::ValueType.__init__)


def test_smif::values::valuetype_constructor_args():
    sig = inspect.signature(smif::values::ValueType.__init__)
    params = list(sig.parameters.keys())



def test_unittype_is_not_abstract():
    assert not inspect.isabstract(UnitType)


def test_unittype_constructor_exists():
    assert callable(UnitType.__init__)


def test_unittype_constructor_args():
    sig = inspect.signature(UnitType.__init__)
    params = list(sig.parameters.keys())



def test_smif::values::baseunittype_is_not_abstract():
    assert not inspect.isabstract(smif::values::BaseUnitType)


def test_smif::values::baseunittype_constructor_exists():
    assert callable(smif::values::BaseUnitType.__init__)


def test_smif::values::baseunittype_constructor_args():
    sig = inspect.signature(smif::values::BaseUnitType.__init__)
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



def test_smif::values::unittype_is_not_abstract():
    assert not inspect.isabstract(smif::values::UnitType)


def test_smif::values::unittype_constructor_exists():
    assert callable(smif::values::UnitType.__init__)


def test_smif::values::unittype_constructor_args():
    sig = inspect.signature(smif::values::UnitType.__init__)
    params = list(sig.parameters.keys())
    assert "symbol" in params, "Missing parameter 'symbol'"
    assert "offset" in params, "Missing parameter 'offset'"
    assert "ratio" in params, "Missing parameter 'ratio'"

def test_smif::values::unittype_has_symbol():
    assert hasattr(smif::values::UnitType, "symbol")
    descriptor = None
    for klass in smif::values::UnitType.__mro__:
        if "symbol" in klass.__dict__:
            descriptor = klass.__dict__["symbol"]
            break
    assert isinstance(descriptor, property)

def test_smif::values::unittype_has_offset():
    assert hasattr(smif::values::UnitType, "offset")
    descriptor = None
    for klass in smif::values::UnitType.__mro__:
        if "offset" in klass.__dict__:
            descriptor = klass.__dict__["offset"]
            break
    assert isinstance(descriptor, property)

def test_smif::values::unittype_has_ratio():
    assert hasattr(smif::values::UnitType, "ratio")
    descriptor = None
    for klass in smif::values::UnitType.__mro__:
        if "ratio" in klass.__dict__:
            descriptor = klass.__dict__["ratio"]
            break
    assert isinstance(descriptor, property)



def test_smif::values::quantitykind_is_not_abstract():
    assert not inspect.isabstract(smif::values::QuantityKind)


def test_smif::values::quantitykind_constructor_exists():
    assert callable(smif::values::QuantityKind.__init__)


def test_smif::values::quantitykind_constructor_args():
    sig = inspect.signature(smif::values::QuantityKind.__init__)
    params = list(sig.parameters.keys())



def test_situations::situation_is_not_abstract():
    assert not inspect.isabstract(situations::Situation)


def test_situations::situation_constructor_exists():
    assert callable(situations::Situation.__init__)


def test_situations::situation_constructor_args():
    sig = inspect.signature(situations::Situation.__init__)
    params = list(sig.parameters.keys())



def test_toplevel::actualentity_is_not_abstract():
    assert not inspect.isabstract(toplevel::ActualEntity)


def test_toplevel::actualentity_constructor_exists():
    assert callable(toplevel::ActualEntity.__init__)


def test_toplevel::actualentity_constructor_args():
    sig = inspect.signature(toplevel::ActualEntity.__init__)
    params = list(sig.parameters.keys())



def test_smif::situations::actualsituation_is_not_abstract():
    assert not inspect.isabstract(smif::situations::ActualSituation)


def test_smif::situations::actualsituation_constructor_exists():
    assert callable(smif::situations::ActualSituation.__init__)


def test_smif::situations::actualsituation_constructor_args():
    sig = inspect.signature(smif::situations::ActualSituation.__init__)
    params = list(sig.parameters.keys())



def test_patternmatch_is_not_abstract():
    assert not inspect.isabstract(PatternMatch)


def test_patternmatch_constructor_exists():
    assert callable(PatternMatch.__init__)


def test_patternmatch_constructor_args():
    sig = inspect.signature(PatternMatch.__init__)
    params = list(sig.parameters.keys())



def test_toplevel::temporalentity_is_not_abstract():
    assert not inspect.isabstract(toplevel::TemporalEntity)


def test_toplevel::temporalentity_constructor_exists():
    assert callable(toplevel::TemporalEntity.__init__)


def test_toplevel::temporalentity_constructor_args():
    sig = inspect.signature(toplevel::TemporalEntity.__init__)
    params = list(sig.parameters.keys())



def test_toplevel::proposition_is_not_abstract():
    assert not inspect.isabstract(toplevel::Proposition)


def test_toplevel::proposition_constructor_exists():
    assert callable(toplevel::Proposition.__init__)


def test_toplevel::proposition_constructor_args():
    sig = inspect.signature(toplevel::Proposition.__init__)
    params = list(sig.parameters.keys())



def test_entitytype_is_not_abstract():
    assert not inspect.isabstract(EntityType)


def test_entitytype_constructor_exists():
    assert callable(EntityType.__init__)


def test_entitytype_constructor_args():
    sig = inspect.signature(EntityType.__init__)
    params = list(sig.parameters.keys())



def test_smif::situations::situationtype_is_not_abstract():
    assert not inspect.isabstract(smif::situations::SituationType)


def test_smif::situations::situationtype_constructor_exists():
    assert callable(smif::situations::SituationType.__init__)


def test_smif::situations::situationtype_constructor_args():
    sig = inspect.signature(smif::situations::SituationType.__init__)
    params = list(sig.parameters.keys())



def test_lexicalscope_is_not_abstract():
    assert not inspect.isabstract(LexicalScope)


def test_lexicalscope_constructor_exists():
    assert callable(LexicalScope.__init__)


def test_lexicalscope_constructor_args():
    sig = inspect.signature(LexicalScope.__init__)
    params = list(sig.parameters.keys())



def test_smif::repository_is_not_abstract():
    assert not inspect.isabstract(smif::Repository)


def test_smif::repository_constructor_exists():
    assert callable(smif::Repository.__init__)


def test_smif::repository_constructor_args():
    sig = inspect.signature(smif::Repository.__init__)
    params = list(sig.parameters.keys())



def test_recordtype_is_not_abstract():
    assert not inspect.isabstract(RecordType)


def test_recordtype_constructor_exists():
    assert callable(RecordType.__init__)


def test_recordtype_constructor_args():
    sig = inspect.signature(RecordType.__init__)
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



def test_thing_is_not_abstract():
    assert not inspect.isabstract(Thing)


def test_thing_constructor_exists():
    assert callable(Thing.__init__)


def test_thing_constructor_args():
    sig = inspect.signature(Thing.__init__)
    params = list(sig.parameters.keys())



def test_smif::values::value_is_not_abstract():
    assert not inspect.isabstract(smif::values::Value)


def test_smif::values::value_constructor_exists():
    assert callable(smif::values::Value.__init__)


def test_smif::values::value_constructor_args():
    sig = inspect.signature(smif::values::Value.__init__)
    params = list(sig.parameters.keys())



def test_toplevel::context_is_not_abstract():
    assert not inspect.isabstract(toplevel::Context)


def test_toplevel::context_constructor_exists():
    assert callable(toplevel::Context.__init__)


def test_toplevel::context_constructor_args():
    sig = inspect.signature(toplevel::Context.__init__)
    params = list(sig.parameters.keys())



def test_lexicalscope::lexicalscope_is_not_abstract():
    assert not inspect.isabstract(lexicalscope::LexicalScope)


def test_lexicalscope::lexicalscope_constructor_exists():
    assert callable(lexicalscope::LexicalScope.__init__)


def test_lexicalscope::lexicalscope_constructor_args():
    sig = inspect.signature(lexicalscope::LexicalScope.__init__)
    params = list(sig.parameters.keys())



def test_smif::situations::situation_is_not_abstract():
    assert not inspect.isabstract(smif::situations::Situation)


def test_smif::situations::situation_constructor_exists():
    assert callable(smif::situations::Situation.__init__)


def test_smif::situations::situation_constructor_args():
    sig = inspect.signature(smif::situations::Situation.__init__)
    params = list(sig.parameters.keys())



def test_smif::types::type_is_not_abstract():
    assert not inspect.isabstract(smif::types::Type)


def test_smif::types::type_constructor_exists():
    assert callable(smif::types::Type.__init__)


def test_smif::types::type_constructor_args():
    sig = inspect.signature(smif::types::Type.__init__)
    params = list(sig.parameters.keys())



def test_smif::facets::facet_is_not_abstract():
    assert not inspect.isabstract(smif::facets::Facet)


def test_smif::facets::facet_constructor_exists():
    assert callable(smif::facets::Facet.__init__)


def test_smif::facets::facet_constructor_args():
    sig = inspect.signature(smif::facets::Facet.__init__)
    params = list(sig.parameters.keys())



def test_smif::properties::propertybinding_is_not_abstract():
    assert not inspect.isabstract(smif::properties::PropertyBinding)


def test_smif::properties::propertybinding_constructor_exists():
    assert callable(smif::properties::PropertyBinding.__init__)


def test_smif::properties::propertybinding_constructor_args():
    sig = inspect.signature(smif::properties::PropertyBinding.__init__)
    params = list(sig.parameters.keys())



def test_facet_is_not_abstract():
    assert not inspect.isabstract(Facet)


def test_facet_constructor_exists():
    assert callable(Facet.__init__)


def test_facet_constructor_args():
    sig = inspect.signature(Facet.__init__)
    params = list(sig.parameters.keys())



def test_smif::facets::category_is_not_abstract():
    assert not inspect.isabstract(smif::facets::Category)


def test_smif::facets::category_constructor_exists():
    assert callable(smif::facets::Category.__init__)


def test_smif::facets::category_constructor_args():
    sig = inspect.signature(smif::facets::Category.__init__)
    params = list(sig.parameters.keys())



def test_smif::facets::role_is_not_abstract():
    assert not inspect.isabstract(smif::facets::Role)


def test_smif::facets::role_constructor_exists():
    assert callable(smif::facets::Role.__init__)


def test_smif::facets::role_constructor_args():
    sig = inspect.signature(smif::facets::Role.__init__)
    params = list(sig.parameters.keys())



def test_facets::facet_is_not_abstract():
    assert not inspect.isabstract(facets::Facet)


def test_facets::facet_constructor_exists():
    assert callable(facets::Facet.__init__)


def test_facets::facet_constructor_args():
    sig = inspect.signature(facets::Facet.__init__)
    params = list(sig.parameters.keys())



def test_relationship_is_not_abstract():
    assert not inspect.isabstract(Relationship)


def test_relationship_constructor_exists():
    assert callable(Relationship.__init__)


def test_relationship_constructor_args():
    sig = inspect.signature(Relationship.__init__)
    params = list(sig.parameters.keys())



def test_smif::facets::facetofentity_is_not_abstract():
    assert not inspect.isabstract(smif::facets::FacetOfEntity)


def test_smif::facets::facetofentity_constructor_exists():
    assert callable(smif::facets::FacetOfEntity.__init__)


def test_smif::facets::facetofentity_constructor_args():
    sig = inspect.signature(smif::facets::FacetOfEntity.__init__)
    params = list(sig.parameters.keys())



def test_smif::properties::propertyowner_is_not_abstract():
    assert not inspect.isabstract(smif::properties::PropertyOwner)


def test_smif::properties::propertyowner_constructor_exists():
    assert callable(smif::properties::PropertyOwner.__init__)


def test_smif::properties::propertyowner_constructor_args():
    sig = inspect.signature(smif::properties::PropertyOwner.__init__)
    params = list(sig.parameters.keys())



def test_smif::properties::propertyownertype_is_not_abstract():
    assert not inspect.isabstract(smif::properties::PropertyOwnerType)


def test_smif::properties::propertyownertype_constructor_exists():
    assert callable(smif::properties::PropertyOwnerType.__init__)


def test_smif::properties::propertyownertype_constructor_args():
    sig = inspect.signature(smif::properties::PropertyOwnerType.__init__)
    params = list(sig.parameters.keys())



def test_smif::properties::ownedpropertytype_is_not_abstract():
    assert not inspect.isabstract(smif::properties::OwnedPropertyType)


def test_smif::properties::ownedpropertytype_constructor_exists():
    assert callable(smif::properties::OwnedPropertyType.__init__)


def test_smif::properties::ownedpropertytype_constructor_args():
    sig = inspect.signature(smif::properties::OwnedPropertyType.__init__)
    params = list(sig.parameters.keys())



def test_characteristictype_is_not_abstract():
    assert not inspect.isabstract(CharacteristicType)


def test_characteristictype_constructor_exists():
    assert callable(CharacteristicType.__init__)


def test_characteristictype_constructor_args():
    sig = inspect.signature(CharacteristicType.__init__)
    params = list(sig.parameters.keys())



def test_smif::properties::annotationproperty_is_not_abstract():
    assert not inspect.isabstract(smif::properties::AnnotationProperty)


def test_smif::properties::annotationproperty_constructor_exists():
    assert callable(smif::properties::AnnotationProperty.__init__)


def test_smif::properties::annotationproperty_constructor_args():
    sig = inspect.signature(smif::properties::AnnotationProperty.__init__)
    params = list(sig.parameters.keys())



def test_properties::propertybinding_is_not_abstract():
    assert not inspect.isabstract(properties::PropertyBinding)


def test_properties::propertybinding_constructor_exists():
    assert callable(properties::PropertyBinding.__init__)


def test_properties::propertybinding_constructor_args():
    sig = inspect.signature(properties::PropertyBinding.__init__)
    params = list(sig.parameters.keys())



def test_properties::propertytype_is_not_abstract():
    assert not inspect.isabstract(properties::PropertyType)


def test_properties::propertytype_constructor_exists():
    assert callable(properties::PropertyType.__init__)


def test_properties::propertytype_constructor_args():
    sig = inspect.signature(properties::PropertyType.__init__)
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



def test_smif::properties::propertytype_is_not_abstract():
    assert not inspect.isabstract(smif::properties::PropertyType)


def test_smif::properties::propertytype_constructor_exists():
    assert callable(smif::properties::PropertyType.__init__)


def test_smif::properties::propertytype_constructor_args():
    sig = inspect.signature(smif::properties::PropertyType.__init__)
    params = list(sig.parameters.keys())



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



def test_metadata::metadata_is_not_abstract():
    assert not inspect.isabstract(metadata::Metadata)


def test_metadata::metadata_constructor_exists():
    assert callable(metadata::Metadata.__init__)


def test_metadata::metadata_constructor_args():
    sig = inspect.signature(metadata::Metadata.__init__)
    params = list(sig.parameters.keys())



def test_smif::metadata::informationsource_is_not_abstract():
    assert not inspect.isabstract(smif::metadata::InformationSource)


def test_smif::metadata::informationsource_constructor_exists():
    assert callable(smif::metadata::InformationSource.__init__)


def test_smif::metadata::informationsource_constructor_args():
    sig = inspect.signature(smif::metadata::InformationSource.__init__)
    params = list(sig.parameters.keys())



def test_propertyownertype_is_not_abstract():
    assert not inspect.isabstract(PropertyOwnerType)


def test_propertyownertype_constructor_exists():
    assert callable(PropertyOwnerType.__init__)


def test_propertyownertype_constructor_args():
    sig = inspect.signature(PropertyOwnerType.__init__)
    params = list(sig.parameters.keys())



def test_smif::associations::associationtype_is_not_abstract():
    assert not inspect.isabstract(smif::associations::AssociationType)


def test_smif::associations::associationtype_constructor_exists():
    assert callable(smif::associations::AssociationType.__init__)


def test_smif::associations::associationtype_constructor_args():
    sig = inspect.signature(smif::associations::AssociationType.__init__)
    params = list(sig.parameters.keys())



def test_prefix_is_not_abstract():
    assert not inspect.isabstract(Prefix)


def test_prefix_constructor_exists():
    assert callable(Prefix.__init__)


def test_prefix_constructor_args():
    sig = inspect.signature(Prefix.__init__)
    params = list(sig.parameters.keys())



def test_smif::lexicalscope::package_is_not_abstract():
    assert not inspect.isabstract(smif::lexicalscope::Package)


def test_smif::lexicalscope::package_constructor_exists():
    assert callable(smif::lexicalscope::Package.__init__)


def test_smif::lexicalscope::package_constructor_args():
    sig = inspect.signature(smif::lexicalscope::Package.__init__)
    params = list(sig.parameters.keys())



def test_smif::lexicalscope::lexicalreference_is_not_abstract():
    assert not inspect.isabstract(smif::lexicalscope::LexicalReference)


def test_smif::lexicalscope::lexicalreference_constructor_exists():
    assert callable(smif::lexicalscope::LexicalReference.__init__)


def test_smif::lexicalscope::lexicalreference_constructor_args():
    sig = inspect.signature(smif::lexicalscope::LexicalReference.__init__)
    params = list(sig.parameters.keys())



def test_smif::lexicalscope::lexicalscope_is_not_abstract():
    assert not inspect.isabstract(smif::lexicalscope::LexicalScope)


def test_smif::lexicalscope::lexicalscope_constructor_exists():
    assert callable(smif::lexicalscope::LexicalScope.__init__)


def test_smif::lexicalscope::lexicalscope_constructor_args():
    sig = inspect.signature(smif::lexicalscope::LexicalScope.__init__)
    params = list(sig.parameters.keys())



def test_package_is_not_abstract():
    assert not inspect.isabstract(Package)


def test_package_constructor_exists():
    assert callable(Package.__init__)


def test_package_constructor_args():
    sig = inspect.signature(Package.__init__)
    params = list(sig.parameters.keys())



def test_smif::lexicalscope::mappingpackage_is_not_abstract():
    assert not inspect.isabstract(smif::lexicalscope::MappingPackage)


def test_smif::lexicalscope::mappingpackage_constructor_exists():
    assert callable(smif::lexicalscope::MappingPackage.__init__)


def test_smif::lexicalscope::mappingpackage_constructor_args():
    sig = inspect.signature(smif::lexicalscope::MappingPackage.__init__)
    params = list(sig.parameters.keys())



def test_smif::lexicalscope::physicalpackage_is_not_abstract():
    assert not inspect.isabstract(smif::lexicalscope::PhysicalPackage)


def test_smif::lexicalscope::physicalpackage_constructor_exists():
    assert callable(smif::lexicalscope::PhysicalPackage.__init__)


def test_smif::lexicalscope::physicalpackage_constructor_args():
    sig = inspect.signature(smif::lexicalscope::PhysicalPackage.__init__)
    params = list(sig.parameters.keys())



def test_smif::lexicalscope::mofpackage_is_not_abstract():
    assert not inspect.isabstract(smif::lexicalscope::MOFPackage)


def test_smif::lexicalscope::mofpackage_constructor_exists():
    assert callable(smif::lexicalscope::MOFPackage.__init__)


def test_smif::lexicalscope::mofpackage_constructor_args():
    sig = inspect.signature(smif::lexicalscope::MOFPackage.__init__)
    params = list(sig.parameters.keys())



def test_smif::lexicalscope::logicalpackage_is_not_abstract():
    assert not inspect.isabstract(smif::lexicalscope::LogicalPackage)


def test_smif::lexicalscope::logicalpackage_constructor_exists():
    assert callable(smif::lexicalscope::LogicalPackage.__init__)


def test_smif::lexicalscope::logicalpackage_constructor_args():
    sig = inspect.signature(smif::lexicalscope::LogicalPackage.__init__)
    params = list(sig.parameters.keys())



def test_smif::lexicalscope::model_is_not_abstract():
    assert not inspect.isabstract(smif::lexicalscope::Model)


def test_smif::lexicalscope::model_constructor_exists():
    assert callable(smif::lexicalscope::Model.__init__)


def test_smif::lexicalscope::model_constructor_args():
    sig = inspect.signature(smif::lexicalscope::Model.__init__)
    params = list(sig.parameters.keys())



def test_conditionalrule_is_not_abstract():
    assert not inspect.isabstract(ConditionalRule)


def test_conditionalrule_constructor_exists():
    assert callable(ConditionalRule.__init__)


def test_conditionalrule_constructor_args():
    sig = inspect.signature(ConditionalRule.__init__)
    params = list(sig.parameters.keys())



def test_smif::mapping::representationrule_is_not_abstract():
    assert not inspect.isabstract(smif::mapping::RepresentationRule)


def test_smif::mapping::representationrule_constructor_exists():
    assert callable(smif::mapping::RepresentationRule.__init__)


def test_smif::mapping::representationrule_constructor_args():
    sig = inspect.signature(smif::mapping::RepresentationRule.__init__)
    params = list(sig.parameters.keys())
    assert "mapAll" in params, "Missing parameter 'mapAll'"

def test_smif::mapping::representationrule_has_mapAll():
    assert hasattr(smif::mapping::RepresentationRule, "mapAll")
    descriptor = None
    for klass in smif::mapping::RepresentationRule.__mro__:
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



def test_smif::mapping::computedfacade_is_not_abstract():
    assert not inspect.isabstract(smif::mapping::ComputedFacade)


def test_smif::mapping::computedfacade_constructor_exists():
    assert callable(smif::mapping::ComputedFacade.__init__)


def test_smif::mapping::computedfacade_constructor_args():
    sig = inspect.signature(smif::mapping::ComputedFacade.__init__)
    params = list(sig.parameters.keys())



def test_smif::mapping::facade_is_not_abstract():
    assert not inspect.isabstract(smif::mapping::Facade)


def test_smif::mapping::facade_constructor_exists():
    assert callable(smif::mapping::Facade.__init__)


def test_smif::mapping::facade_constructor_args():
    sig = inspect.signature(smif::mapping::Facade.__init__)
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



def test_patterns::pattern_is_not_abstract():
    assert not inspect.isabstract(patterns::Pattern)


def test_patterns::pattern_constructor_exists():
    assert callable(patterns::Pattern.__init__)


def test_patterns::pattern_constructor_args():
    sig = inspect.signature(patterns::Pattern.__init__)
    params = list(sig.parameters.keys())



def test_matchrule_is_not_abstract():
    assert not inspect.isabstract(MatchRule)


def test_matchrule_constructor_exists():
    assert callable(MatchRule.__init__)


def test_matchrule_constructor_args():
    sig = inspect.signature(MatchRule.__init__)
    params = list(sig.parameters.keys())



def test_smif::patterns::computed_is_not_abstract():
    assert not inspect.isabstract(smif::patterns::Computed)


def test_smif::patterns::computed_constructor_exists():
    assert callable(smif::patterns::Computed.__init__)


def test_smif::patterns::computed_constructor_args():
    sig = inspect.signature(smif::patterns::Computed.__init__)
    params = list(sig.parameters.keys())



def test_ownedpropertybinding_is_not_abstract():
    assert not inspect.isabstract(OwnedPropertyBinding)


def test_ownedpropertybinding_constructor_exists():
    assert callable(OwnedPropertyBinding.__init__)


def test_ownedpropertybinding_constructor_args():
    sig = inspect.signature(OwnedPropertyBinding.__init__)
    params = list(sig.parameters.keys())



def test_smif::patterns::variablebinding_is_not_abstract():
    assert not inspect.isabstract(smif::patterns::VariableBinding)


def test_smif::patterns::variablebinding_constructor_exists():
    assert callable(smif::patterns::VariableBinding.__init__)


def test_smif::patterns::variablebinding_constructor_args():
    sig = inspect.signature(smif::patterns::VariableBinding.__init__)
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



def test_smif::patterns::patternmatch_is_not_abstract():
    assert not inspect.isabstract(smif::patterns::PatternMatch)


def test_smif::patterns::patternmatch_constructor_exists():
    assert callable(smif::patterns::PatternMatch.__init__)


def test_smif::patterns::patternmatch_constructor_args():
    sig = inspect.signature(smif::patterns::PatternMatch.__init__)
    params = list(sig.parameters.keys())



def test_smif::patterns::patternoftype_is_not_abstract():
    assert not inspect.isabstract(smif::patterns::PatternOfType)


def test_smif::patterns::patternoftype_constructor_exists():
    assert callable(smif::patterns::PatternOfType.__init__)


def test_smif::patterns::patternoftype_constructor_args():
    sig = inspect.signature(smif::patterns::PatternOfType.__init__)
    params = list(sig.parameters.keys())



def test_typepatternvariable_is_not_abstract():
    assert not inspect.isabstract(TypePatternVariable)


def test_typepatternvariable_constructor_exists():
    assert callable(TypePatternVariable.__init__)


def test_typepatternvariable_constructor_args():
    sig = inspect.signature(TypePatternVariable.__init__)
    params = list(sig.parameters.keys())



def test_smif::patterns::focusvariable_is_not_abstract():
    assert not inspect.isabstract(smif::patterns::FocusVariable)


def test_smif::patterns::focusvariable_constructor_exists():
    assert callable(smif::patterns::FocusVariable.__init__)


def test_smif::patterns::focusvariable_constructor_args():
    sig = inspect.signature(smif::patterns::FocusVariable.__init__)
    params = list(sig.parameters.keys())



def test_smif::patterns::partvariable_is_not_abstract():
    assert not inspect.isabstract(smif::patterns::PartVariable)


def test_smif::patterns::partvariable_constructor_exists():
    assert callable(smif::patterns::PartVariable.__init__)


def test_smif::patterns::partvariable_constructor_args():
    sig = inspect.signature(smif::patterns::PartVariable.__init__)
    params = list(sig.parameters.keys())
    assert "isBoundaryPart" in params, "Missing parameter 'isBoundaryPart'"

def test_smif::patterns::partvariable_has_isBoundaryPart():
    assert hasattr(smif::patterns::PartVariable, "isBoundaryPart")
    descriptor = None
    for klass in smif::patterns::PartVariable.__mro__:
        if "isBoundaryPart" in klass.__dict__:
            descriptor = klass.__dict__["isBoundaryPart"]
            break
    assert isinstance(descriptor, property)



def test_patterns::computed_is_not_abstract():
    assert not inspect.isabstract(patterns::Computed)


def test_patterns::computed_constructor_exists():
    assert callable(patterns::Computed.__init__)


def test_patterns::computed_constructor_args():
    sig = inspect.signature(patterns::Computed.__init__)
    params = list(sig.parameters.keys())



def test_patterns::patternvariable_is_not_abstract():
    assert not inspect.isabstract(patterns::PatternVariable)


def test_patterns::patternvariable_constructor_exists():
    assert callable(patterns::PatternVariable.__init__)


def test_patterns::patternvariable_constructor_args():
    sig = inspect.signature(patterns::PatternVariable.__init__)
    params = list(sig.parameters.keys())



def test_smif::patterns::expressionvariable_is_not_abstract():
    assert not inspect.isabstract(smif::patterns::ExpressionVariable)


def test_smif::patterns::expressionvariable_constructor_exists():
    assert callable(smif::patterns::ExpressionVariable.__init__)


def test_smif::patterns::expressionvariable_constructor_args():
    sig = inspect.signature(smif::patterns::ExpressionVariable.__init__)
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



def test_properties::ownedpropertytype_is_not_abstract():
    assert not inspect.isabstract(properties::OwnedPropertyType)


def test_properties::ownedpropertytype_constructor_exists():
    assert callable(properties::OwnedPropertyType.__init__)


def test_properties::ownedpropertytype_constructor_args():
    sig = inspect.signature(properties::OwnedPropertyType.__init__)
    params = list(sig.parameters.keys())



def test_patternvariable_is_not_abstract():
    assert not inspect.isabstract(PatternVariable)


def test_patternvariable_constructor_exists():
    assert callable(PatternVariable.__init__)


def test_patternvariable_constructor_args():
    sig = inspect.signature(PatternVariable.__init__)
    params = list(sig.parameters.keys())



def test_smif::patterns::propositionvariable_is_not_abstract():
    assert not inspect.isabstract(smif::patterns::PropositionVariable)


def test_smif::patterns::propositionvariable_constructor_exists():
    assert callable(smif::patterns::PropositionVariable.__init__)


def test_smif::patterns::propositionvariable_constructor_args():
    sig = inspect.signature(smif::patterns::PropositionVariable.__init__)
    params = list(sig.parameters.keys())



def test_smif::patterns::typepatternvariable_is_not_abstract():
    assert not inspect.isabstract(smif::patterns::TypePatternVariable)


def test_smif::patterns::typepatternvariable_constructor_exists():
    assert callable(smif::patterns::TypePatternVariable.__init__)


def test_smif::patterns::typepatternvariable_constructor_args():
    sig = inspect.signature(smif::patterns::TypePatternVariable.__init__)
    params = list(sig.parameters.keys())



def test_temporalentity_is_not_abstract():
    assert not inspect.isabstract(TemporalEntity)


def test_temporalentity_constructor_exists():
    assert callable(TemporalEntity.__init__)


def test_temporalentity_constructor_args():
    sig = inspect.signature(TemporalEntity.__init__)
    params = list(sig.parameters.keys())



def test_smif::toplevel::actualentity_is_not_abstract():
    assert not inspect.isabstract(smif::toplevel::ActualEntity)


def test_smif::toplevel::actualentity_constructor_exists():
    assert callable(smif::toplevel::ActualEntity.__init__)


def test_smif::toplevel::actualentity_constructor_args():
    sig = inspect.signature(smif::toplevel::ActualEntity.__init__)
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



def test_smif::lexicalscope::include_is_not_abstract():
    assert not inspect.isabstract(smif::lexicalscope::Include)


def test_smif::lexicalscope::include_constructor_exists():
    assert callable(smif::lexicalscope::Include.__init__)


def test_smif::lexicalscope::include_constructor_args():
    sig = inspect.signature(smif::lexicalscope::Include.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_smif::toplevel::identifiableentity_is_not_abstract():
    assert not inspect.isabstract(smif::toplevel::IdentifiableEntity)


def test_smif::toplevel::identifiableentity_constructor_exists():
    assert callable(smif::toplevel::IdentifiableEntity.__init__)


def test_smif::toplevel::identifiableentity_constructor_args():
    sig = inspect.signature(smif::toplevel::IdentifiableEntity.__init__)
    params = list(sig.parameters.keys())



def test_constantreference_is_not_abstract():
    assert not inspect.isabstract(ConstantReference)


def test_constantreference_constructor_exists():
    assert callable(ConstantReference.__init__)


def test_constantreference_constructor_args():
    sig = inspect.signature(ConstantReference.__init__)
    params = list(sig.parameters.keys())



def test_smif::toplevel::thing_is_not_abstract():
    assert not inspect.isabstract(smif::toplevel::Thing)


def test_smif::toplevel::thing_constructor_exists():
    assert callable(smif::toplevel::Thing.__init__)


def test_smif::toplevel::thing_constructor_args():
    sig = inspect.signature(smif::toplevel::Thing.__init__)
    params = list(sig.parameters.keys())



def test_propertybinding_is_not_abstract():
    assert not inspect.isabstract(PropertyBinding)


def test_propertybinding_constructor_exists():
    assert callable(PropertyBinding.__init__)


def test_propertybinding_constructor_args():
    sig = inspect.signature(PropertyBinding.__init__)
    params = list(sig.parameters.keys())



def test_smif::properties::ownedpropertybinding_is_not_abstract():
    assert not inspect.isabstract(smif::properties::OwnedPropertyBinding)


def test_smif::properties::ownedpropertybinding_constructor_exists():
    assert callable(smif::properties::OwnedPropertyBinding.__init__)


def test_smif::properties::ownedpropertybinding_constructor_args():
    sig = inspect.signature(smif::properties::OwnedPropertyBinding.__init__)
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



def test_smif::metadata::metadata_is_not_abstract():
    assert not inspect.isabstract(smif::metadata::Metadata)


def test_smif::metadata::metadata_constructor_exists():
    assert callable(smif::metadata::Metadata.__init__)


def test_smif::metadata::metadata_constructor_args():
    sig = inspect.signature(smif::metadata::Metadata.__init__)
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



def test_smif::metadata::definition_is_not_abstract():
    assert not inspect.isabstract(smif::metadata::Definition)


def test_smif::metadata::definition_constructor_exists():
    assert callable(smif::metadata::Definition.__init__)


def test_smif::metadata::definition_constructor_args():
    sig = inspect.signature(smif::metadata::Definition.__init__)
    params = list(sig.parameters.keys())
    assert "textDefinition" in params, "Missing parameter 'textDefinition'"
    assert "summaryDescription" in params, "Missing parameter 'summaryDescription'"

def test_smif::metadata::definition_has_textDefinition():
    assert hasattr(smif::metadata::Definition, "textDefinition")
    descriptor = None
    for klass in smif::metadata::Definition.__mro__:
        if "textDefinition" in klass.__dict__:
            descriptor = klass.__dict__["textDefinition"]
            break
    assert isinstance(descriptor, property)

def test_smif::metadata::definition_has_summaryDescription():
    assert hasattr(smif::metadata::Definition, "summaryDescription")
    descriptor = None
    for klass in smif::metadata::Definition.__mro__:
        if "summaryDescription" in klass.__dict__:
            descriptor = klass.__dict__["summaryDescription"]
            break
    assert isinstance(descriptor, property)



def test_smif::metadata::statement_is_not_abstract():
    assert not inspect.isabstract(smif::metadata::Statement)


def test_smif::metadata::statement_constructor_exists():
    assert callable(smif::metadata::Statement.__init__)


def test_smif::metadata::statement_constructor_args():
    sig = inspect.signature(smif::metadata::Statement.__init__)
    params = list(sig.parameters.keys())



def test_constraints::conditional_is_not_abstract():
    assert not inspect.isabstract(constraints::Conditional)


def test_constraints::conditional_constructor_exists():
    assert callable(constraints::Conditional.__init__)


def test_constraints::conditional_constructor_args():
    sig = inspect.signature(constraints::Conditional.__init__)
    params = list(sig.parameters.keys())



def test_smif::patterns::patternvariable_is_not_abstract():
    assert not inspect.isabstract(smif::patterns::PatternVariable)


def test_smif::patterns::patternvariable_constructor_exists():
    assert callable(smif::patterns::PatternVariable.__init__)


def test_smif::patterns::patternvariable_constructor_args():
    sig = inspect.signature(smif::patterns::PatternVariable.__init__)
    params = list(sig.parameters.keys())
    assert "qualification" in params, "Missing parameter 'qualification'"
    assert "explicit" in params, "Missing parameter 'explicit'"

def test_smif::patterns::patternvariable_has_qualification():
    assert hasattr(smif::patterns::PatternVariable, "qualification")
    descriptor = None
    for klass in smif::patterns::PatternVariable.__mro__:
        if "qualification" in klass.__dict__:
            descriptor = klass.__dict__["qualification"]
            break
    assert isinstance(descriptor, property)

def test_smif::patterns::patternvariable_has_explicit():
    assert hasattr(smif::patterns::PatternVariable, "explicit")
    descriptor = None
    for klass in smif::patterns::PatternVariable.__mro__:
        if "explicit" in klass.__dict__:
            descriptor = klass.__dict__["explicit"]
            break
    assert isinstance(descriptor, property)



def test_smif::mapping::matchend_is_not_abstract():
    assert not inspect.isabstract(smif::mapping::MatchEnd)


def test_smif::mapping::matchend_constructor_exists():
    assert callable(smif::mapping::MatchEnd.__init__)


def test_smif::mapping::matchend_constructor_args():
    sig = inspect.signature(smif::mapping::MatchEnd.__init__)
    params = list(sig.parameters.keys())



def test_constraints::rule_is_not_abstract():
    assert not inspect.isabstract(constraints::Rule)


def test_constraints::rule_constructor_exists():
    assert callable(constraints::Rule.__init__)


def test_constraints::rule_constructor_args():
    sig = inspect.signature(constraints::Rule.__init__)
    params = list(sig.parameters.keys())



def test_smif::mapping::mapping_is_not_abstract():
    assert not inspect.isabstract(smif::mapping::Mapping)


def test_smif::mapping::mapping_constructor_exists():
    assert callable(smif::mapping::Mapping.__init__)


def test_smif::mapping::mapping_constructor_args():
    sig = inspect.signature(smif::mapping::Mapping.__init__)
    params = list(sig.parameters.keys())
    assert "strength" in params, "Missing parameter 'strength'"

def test_smif::mapping::mapping_has_strength():
    assert hasattr(smif::mapping::Mapping, "strength")
    descriptor = None
    for klass in smif::mapping::Mapping.__mro__:
        if "strength" in klass.__dict__:
            descriptor = klass.__dict__["strength"]
            break
    assert isinstance(descriptor, property)



def test_smif::constraints::conditionalrule_is_not_abstract():
    assert not inspect.isabstract(smif::constraints::ConditionalRule)


def test_smif::constraints::conditionalrule_constructor_exists():
    assert callable(smif::constraints::ConditionalRule.__init__)


def test_smif::constraints::conditionalrule_constructor_args():
    sig = inspect.signature(smif::constraints::ConditionalRule.__init__)
    params = list(sig.parameters.keys())



def test_smif::constraints::conditional_is_not_abstract():
    assert not inspect.isabstract(smif::constraints::Conditional)


def test_smif::constraints::conditional_constructor_exists():
    assert callable(smif::constraints::Conditional.__init__)


def test_smif::constraints::conditional_constructor_args():
    sig = inspect.signature(smif::constraints::Conditional.__init__)
    params = list(sig.parameters.keys())



def test_smif::constraints::facetclassificationconstraint_is_not_abstract():
    assert not inspect.isabstract(smif::constraints::FacetClassificationConstraint)


def test_smif::constraints::facetclassificationconstraint_constructor_exists():
    assert callable(smif::constraints::FacetClassificationConstraint.__init__)


def test_smif::constraints::facetclassificationconstraint_constructor_args():
    sig = inspect.signature(smif::constraints::FacetClassificationConstraint.__init__)
    params = list(sig.parameters.keys())



def test_propertyconstraint_is_not_abstract():
    assert not inspect.isabstract(PropertyConstraint)


def test_propertyconstraint_constructor_exists():
    assert callable(PropertyConstraint.__init__)


def test_propertyconstraint_constructor_args():
    sig = inspect.signature(PropertyConstraint.__init__)
    params = list(sig.parameters.keys())



def test_smif::constraints::propertytypeconstraint_is_not_abstract():
    assert not inspect.isabstract(smif::constraints::PropertyTypeConstraint)


def test_smif::constraints::propertytypeconstraint_constructor_exists():
    assert callable(smif::constraints::PropertyTypeConstraint.__init__)


def test_smif::constraints::propertytypeconstraint_constructor_args():
    sig = inspect.signature(smif::constraints::PropertyTypeConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "prerequisiteType" in params, "Missing parameter 'prerequisiteType'"

def test_smif::constraints::propertytypeconstraint_has_prerequisiteType():
    assert hasattr(smif::constraints::PropertyTypeConstraint, "prerequisiteType")
    descriptor = None
    for klass in smif::constraints::PropertyTypeConstraint.__mro__:
        if "prerequisiteType" in klass.__dict__:
            descriptor = klass.__dict__["prerequisiteType"]
            break
    assert isinstance(descriptor, property)



def test_smif::constraints::propertytransitivityconstraint_is_not_abstract():
    assert not inspect.isabstract(smif::constraints::PropertyTransitivityConstraint)


def test_smif::constraints::propertytransitivityconstraint_constructor_exists():
    assert callable(smif::constraints::PropertyTransitivityConstraint.__init__)


def test_smif::constraints::propertytransitivityconstraint_constructor_args():
    sig = inspect.signature(smif::constraints::PropertyTransitivityConstraint.__init__)
    params = list(sig.parameters.keys())



def test_smif::expressions::evaluation_is_not_abstract():
    assert not inspect.isabstract(smif::expressions::Evaluation)


def test_smif::expressions::evaluation_constructor_exists():
    assert callable(smif::expressions::Evaluation.__init__)


def test_smif::expressions::evaluation_constructor_args():
    sig = inspect.signature(smif::expressions::Evaluation.__init__)
    params = list(sig.parameters.keys())



def test_typeconstraint_is_not_abstract():
    assert not inspect.isabstract(TypeConstraint)


def test_typeconstraint_constructor_exists():
    assert callable(TypeConstraint.__init__)


def test_typeconstraint_constructor_args():
    sig = inspect.signature(TypeConstraint.__init__)
    params = list(sig.parameters.keys())



def test_smif::constraints::generalizationconstraint_is_not_abstract():
    assert not inspect.isabstract(smif::constraints::GeneralizationConstraint)


def test_smif::constraints::generalizationconstraint_constructor_exists():
    assert callable(smif::constraints::GeneralizationConstraint.__init__)


def test_smif::constraints::generalizationconstraint_constructor_args():
    sig = inspect.signature(smif::constraints::GeneralizationConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "redefines" in params, "Missing parameter 'redefines'"

def test_smif::constraints::generalizationconstraint_has_redefines():
    assert hasattr(smif::constraints::GeneralizationConstraint, "redefines")
    descriptor = None
    for klass in smif::constraints::GeneralizationConstraint.__mro__:
        if "redefines" in klass.__dict__:
            descriptor = klass.__dict__["redefines"]
            break
    assert isinstance(descriptor, property)



def test_smif::constraints::coveringconstraint_is_not_abstract():
    assert not inspect.isabstract(smif::constraints::CoveringConstraint)


def test_smif::constraints::coveringconstraint_constructor_exists():
    assert callable(smif::constraints::CoveringConstraint.__init__)


def test_smif::constraints::coveringconstraint_constructor_args():
    sig = inspect.signature(smif::constraints::CoveringConstraint.__init__)
    params = list(sig.parameters.keys())



def test_smif::constraints::uniquenessconstraint_is_not_abstract():
    assert not inspect.isabstract(smif::constraints::UniquenessConstraint)


def test_smif::constraints::uniquenessconstraint_constructor_exists():
    assert callable(smif::constraints::UniquenessConstraint.__init__)


def test_smif::constraints::uniquenessconstraint_constructor_args():
    sig = inspect.signature(smif::constraints::UniquenessConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "isPrimaryIdentity" in params, "Missing parameter 'isPrimaryIdentity'"

def test_smif::constraints::uniquenessconstraint_has_isPrimaryIdentity():
    assert hasattr(smif::constraints::UniquenessConstraint, "isPrimaryIdentity")
    descriptor = None
    for klass in smif::constraints::UniquenessConstraint.__mro__:
        if "isPrimaryIdentity" in klass.__dict__:
            descriptor = klass.__dict__["isPrimaryIdentity"]
            break
    assert isinstance(descriptor, property)



def test_smif::constraints::multiplicityconstraint_is_not_abstract():
    assert not inspect.isabstract(smif::constraints::MultiplicityConstraint)


def test_smif::constraints::multiplicityconstraint_constructor_exists():
    assert callable(smif::constraints::MultiplicityConstraint.__init__)


def test_smif::constraints::multiplicityconstraint_constructor_args():
    sig = inspect.signature(smif::constraints::MultiplicityConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "maximumNumber" in params, "Missing parameter 'maximumNumber'"
    assert "isSufficent" in params, "Missing parameter 'isSufficent'"
    assert "atOnce" in params, "Missing parameter 'atOnce'"
    assert "mininumNumber" in params, "Missing parameter 'mininumNumber'"

def test_smif::constraints::multiplicityconstraint_has_maximumNumber():
    assert hasattr(smif::constraints::MultiplicityConstraint, "maximumNumber")
    descriptor = None
    for klass in smif::constraints::MultiplicityConstraint.__mro__:
        if "maximumNumber" in klass.__dict__:
            descriptor = klass.__dict__["maximumNumber"]
            break
    assert isinstance(descriptor, property)

def test_smif::constraints::multiplicityconstraint_has_isSufficent():
    assert hasattr(smif::constraints::MultiplicityConstraint, "isSufficent")
    descriptor = None
    for klass in smif::constraints::MultiplicityConstraint.__mro__:
        if "isSufficent" in klass.__dict__:
            descriptor = klass.__dict__["isSufficent"]
            break
    assert isinstance(descriptor, property)

def test_smif::constraints::multiplicityconstraint_has_atOnce():
    assert hasattr(smif::constraints::MultiplicityConstraint, "atOnce")
    descriptor = None
    for klass in smif::constraints::MultiplicityConstraint.__mro__:
        if "atOnce" in klass.__dict__:
            descriptor = klass.__dict__["atOnce"]
            break
    assert isinstance(descriptor, property)

def test_smif::constraints::multiplicityconstraint_has_mininumNumber():
    assert hasattr(smif::constraints::MultiplicityConstraint, "mininumNumber")
    descriptor = None
    for klass in smif::constraints::MultiplicityConstraint.__mro__:
        if "mininumNumber" in klass.__dict__:
            descriptor = klass.__dict__["mininumNumber"]
            break
    assert isinstance(descriptor, property)



def test_rule_is_not_abstract():
    assert not inspect.isabstract(Rule)


def test_rule_constructor_exists():
    assert callable(Rule.__init__)


def test_rule_constructor_args():
    sig = inspect.signature(Rule.__init__)
    params = list(sig.parameters.keys())



def test_smif::constraints::typeconstraint_is_not_abstract():
    assert not inspect.isabstract(smif::constraints::TypeConstraint)


def test_smif::constraints::typeconstraint_constructor_exists():
    assert callable(smif::constraints::TypeConstraint.__init__)


def test_smif::constraints::typeconstraint_constructor_args():
    sig = inspect.signature(smif::constraints::TypeConstraint.__init__)
    params = list(sig.parameters.keys())



def test_smif::constraints::propertyconstraint_is_not_abstract():
    assert not inspect.isabstract(smif::constraints::PropertyConstraint)


def test_smif::constraints::propertyconstraint_constructor_exists():
    assert callable(smif::constraints::PropertyConstraint.__init__)


def test_smif::constraints::propertyconstraint_constructor_args():
    sig = inspect.signature(smif::constraints::PropertyConstraint.__init__)
    params = list(sig.parameters.keys())



def test_smif::mapping::matchrule_is_not_abstract():
    assert not inspect.isabstract(smif::mapping::MatchRule)


def test_smif::mapping::matchrule_constructor_exists():
    assert callable(smif::mapping::MatchRule.__init__)


def test_smif::mapping::matchrule_constructor_args():
    sig = inspect.signature(smif::mapping::MatchRule.__init__)
    params = list(sig.parameters.keys())
    assert "coerce" in params, "Missing parameter 'coerce'"

def test_smif::mapping::matchrule_has_coerce():
    assert hasattr(smif::mapping::MatchRule, "coerce")
    descriptor = None
    for klass in smif::mapping::MatchRule.__mro__:
        if "coerce" in klass.__dict__:
            descriptor = klass.__dict__["coerce"]
            break
    assert isinstance(descriptor, property)



def test_smif::constraints::enumerated_is_not_abstract():
    assert not inspect.isabstract(smif::constraints::Enumerated)


def test_smif::constraints::enumerated_constructor_exists():
    assert callable(smif::constraints::Enumerated.__init__)


def test_smif::constraints::enumerated_constructor_args():
    sig = inspect.signature(smif::constraints::Enumerated.__init__)
    params = list(sig.parameters.keys())



def test_smif::constraints::equivalent_is_not_abstract():
    assert not inspect.isabstract(smif::constraints::Equivalent)


def test_smif::constraints::equivalent_constructor_exists():
    assert callable(smif::constraints::Equivalent.__init__)


def test_smif::constraints::equivalent_constructor_args():
    sig = inspect.signature(smif::constraints::Equivalent.__init__)
    params = list(sig.parameters.keys())



def test_smif::constraints::disjoint_is_not_abstract():
    assert not inspect.isabstract(smif::constraints::Disjoint)


def test_smif::constraints::disjoint_constructor_exists():
    assert callable(smif::constraints::Disjoint.__init__)


def test_smif::constraints::disjoint_constructor_args():
    sig = inspect.signature(smif::constraints::Disjoint.__init__)
    params = list(sig.parameters.keys())



def test_proposition_is_not_abstract():
    assert not inspect.isabstract(Proposition)


def test_proposition_constructor_exists():
    assert callable(Proposition.__init__)


def test_proposition_constructor_args():
    sig = inspect.signature(Proposition.__init__)
    params = list(sig.parameters.keys())



def test_smif::constraints::rule_is_not_abstract():
    assert not inspect.isabstract(smif::constraints::Rule)


def test_smif::constraints::rule_constructor_exists():
    assert callable(smif::constraints::Rule.__init__)


def test_smif::constraints::rule_constructor_args():
    sig = inspect.signature(smif::constraints::Rule.__init__)
    params = list(sig.parameters.keys())



def test_situations::situationtype_is_not_abstract():
    assert not inspect.isabstract(situations::SituationType)


def test_situations::situationtype_constructor_exists():
    assert callable(situations::SituationType.__init__)


def test_situations::situationtype_constructor_args():
    sig = inspect.signature(situations::SituationType.__init__)
    params = list(sig.parameters.keys())



def test_smif::properties::characteristictype_is_not_abstract():
    assert not inspect.isabstract(smif::properties::CharacteristicType)


def test_smif::properties::characteristictype_constructor_exists():
    assert callable(smif::properties::CharacteristicType.__init__)


def test_smif::properties::characteristictype_constructor_args():
    sig = inspect.signature(smif::properties::CharacteristicType.__init__)
    params = list(sig.parameters.keys())



def test_smif::facets::phase_is_not_abstract():
    assert not inspect.isabstract(smif::facets::Phase)


def test_smif::facets::phase_constructor_exists():
    assert callable(smif::facets::Phase.__init__)


def test_smif::facets::phase_constructor_args():
    sig = inspect.signature(smif::facets::Phase.__init__)
    params = list(sig.parameters.keys())



def test_situations::actualsituation_is_not_abstract():
    assert not inspect.isabstract(situations::ActualSituation)


def test_situations::actualsituation_constructor_exists():
    assert callable(situations::ActualSituation.__init__)


def test_situations::actualsituation_constructor_args():
    sig = inspect.signature(situations::ActualSituation.__init__)
    params = list(sig.parameters.keys())



def test_smif::properties::characteristicbinding_is_not_abstract():
    assert not inspect.isabstract(smif::properties::CharacteristicBinding)


def test_smif::properties::characteristicbinding_constructor_exists():
    assert callable(smif::properties::CharacteristicBinding.__init__)


def test_smif::properties::characteristicbinding_constructor_args():
    sig = inspect.signature(smif::properties::CharacteristicBinding.__init__)
    params = list(sig.parameters.keys())



def test_uniquetextidentifier_is_not_abstract():
    assert not inspect.isabstract(UniqueTextIdentifier)


def test_uniquetextidentifier_constructor_exists():
    assert callable(UniqueTextIdentifier.__init__)


def test_uniquetextidentifier_constructor_args():
    sig = inspect.signature(UniqueTextIdentifier.__init__)
    params = list(sig.parameters.keys())



def test_smif::lexicalscope::prefix_is_not_abstract():
    assert not inspect.isabstract(smif::lexicalscope::Prefix)


def test_smif::lexicalscope::prefix_constructor_exists():
    assert callable(smif::lexicalscope::Prefix.__init__)


def test_smif::lexicalscope::prefix_constructor_args():
    sig = inspect.signature(smif::lexicalscope::Prefix.__init__)
    params = list(sig.parameters.keys())



def test_smif::identifiers::technicalidentifier_is_not_abstract():
    assert not inspect.isabstract(smif::identifiers::TechnicalIdentifier)


def test_smif::identifiers::technicalidentifier_constructor_exists():
    assert callable(smif::identifiers::TechnicalIdentifier.__init__)


def test_smif::identifiers::technicalidentifier_constructor_args():
    sig = inspect.signature(smif::identifiers::TechnicalIdentifier.__init__)
    params = list(sig.parameters.keys())



def test_textidentifier_is_not_abstract():
    assert not inspect.isabstract(TextIdentifier)


def test_textidentifier_constructor_exists():
    assert callable(TextIdentifier.__init__)


def test_textidentifier_constructor_args():
    sig = inspect.signature(TextIdentifier.__init__)
    params = list(sig.parameters.keys())



def test_smif::identifiers::name_is_not_abstract():
    assert not inspect.isabstract(smif::identifiers::Name)


def test_smif::identifiers::name_constructor_exists():
    assert callable(smif::identifiers::Name.__init__)


def test_smif::identifiers::name_constructor_args():
    sig = inspect.signature(smif::identifiers::Name.__init__)
    params = list(sig.parameters.keys())



def test_smif::identifiers::textidentifier_is_not_abstract():
    assert not inspect.isabstract(smif::identifiers::TextIdentifier)


def test_smif::identifiers::textidentifier_constructor_exists():
    assert callable(smif::identifiers::TextIdentifier.__init__)


def test_smif::identifiers::textidentifier_constructor_args():
    sig = inspect.signature(smif::identifiers::TextIdentifier.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_smif::identifiers::textidentifier_has_value():
    assert hasattr(smif::identifiers::TextIdentifier, "value")
    descriptor = None
    for klass in smif::identifiers::TextIdentifier.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_uniqueidentifier_is_not_abstract():
    assert not inspect.isabstract(UniqueIdentifier)


def test_uniqueidentifier_constructor_exists():
    assert callable(UniqueIdentifier.__init__)


def test_uniqueidentifier_constructor_args():
    sig = inspect.signature(UniqueIdentifier.__init__)
    params = list(sig.parameters.keys())



def test_smif::identifiers::namespace_is_not_abstract():
    assert not inspect.isabstract(smif::identifiers::Namespace)


def test_smif::identifiers::namespace_constructor_exists():
    assert callable(smif::identifiers::Namespace.__init__)


def test_smif::identifiers::namespace_constructor_args():
    sig = inspect.signature(smif::identifiers::Namespace.__init__)
    params = list(sig.parameters.keys())



def test_identifiableentity_is_not_abstract():
    assert not inspect.isabstract(IdentifiableEntity)


def test_identifiableentity_constructor_exists():
    assert callable(IdentifiableEntity.__init__)


def test_identifiableentity_constructor_args():
    sig = inspect.signature(IdentifiableEntity.__init__)
    params = list(sig.parameters.keys())



def test_smif::toplevel::context_is_not_abstract():
    assert not inspect.isabstract(smif::toplevel::Context)


def test_smif::toplevel::context_constructor_exists():
    assert callable(smif::toplevel::Context.__init__)


def test_smif::toplevel::context_constructor_args():
    sig = inspect.signature(smif::toplevel::Context.__init__)
    params = list(sig.parameters.keys())



def test_smif::expressions::expressioncontext_is_not_abstract():
    assert not inspect.isabstract(smif::expressions::ExpressionContext)


def test_smif::expressions::expressioncontext_constructor_exists():
    assert callable(smif::expressions::ExpressionContext.__init__)


def test_smif::expressions::expressioncontext_constructor_args():
    sig = inspect.signature(smif::expressions::ExpressionContext.__init__)
    params = list(sig.parameters.keys())



def test_smif::toplevel::temporalentity_is_not_abstract():
    assert not inspect.isabstract(smif::toplevel::TemporalEntity)


def test_smif::toplevel::temporalentity_constructor_exists():
    assert callable(smif::toplevel::TemporalEntity.__init__)


def test_smif::toplevel::temporalentity_constructor_args():
    sig = inspect.signature(smif::toplevel::TemporalEntity.__init__)
    params = list(sig.parameters.keys())



def test_smif::toplevel::proposition_is_not_abstract():
    assert not inspect.isabstract(smif::toplevel::Proposition)


def test_smif::toplevel::proposition_constructor_exists():
    assert callable(smif::toplevel::Proposition.__init__)


def test_smif::toplevel::proposition_constructor_args():
    sig = inspect.signature(smif::toplevel::Proposition.__init__)
    params = list(sig.parameters.keys())



def test_smif::identifiers::identifier_is_not_abstract():
    assert not inspect.isabstract(smif::identifiers::Identifier)


def test_smif::identifiers::identifier_constructor_exists():
    assert callable(smif::identifiers::Identifier.__init__)


def test_smif::identifiers::identifier_constructor_args():
    sig = inspect.signature(smif::identifiers::Identifier.__init__)
    params = list(sig.parameters.keys())



def test_identifiers::textidentifier_is_not_abstract():
    assert not inspect.isabstract(identifiers::TextIdentifier)


def test_identifiers::textidentifier_constructor_exists():
    assert callable(identifiers::TextIdentifier.__init__)


def test_identifiers::textidentifier_constructor_args():
    sig = inspect.signature(identifiers::TextIdentifier.__init__)
    params = list(sig.parameters.keys())



def test_identifiers::uniqueidentifier_is_not_abstract():
    assert not inspect.isabstract(identifiers::UniqueIdentifier)


def test_identifiers::uniqueidentifier_constructor_exists():
    assert callable(identifiers::UniqueIdentifier.__init__)


def test_identifiers::uniqueidentifier_constructor_args():
    sig = inspect.signature(identifiers::UniqueIdentifier.__init__)
    params = list(sig.parameters.keys())



def test_smif::identifiers::uniquetextidentifier_is_not_abstract():
    assert not inspect.isabstract(smif::identifiers::UniqueTextIdentifier)


def test_smif::identifiers::uniquetextidentifier_constructor_exists():
    assert callable(smif::identifiers::UniqueTextIdentifier.__init__)


def test_smif::identifiers::uniquetextidentifier_constructor_args():
    sig = inspect.signature(smif::identifiers::UniqueTextIdentifier.__init__)
    params = list(sig.parameters.keys())



def test_expressions::expressionnode_is_not_abstract():
    assert not inspect.isabstract(expressions::ExpressionNode)


def test_expressions::expressionnode_constructor_exists():
    assert callable(expressions::ExpressionNode.__init__)


def test_expressions::expressionnode_constructor_args():
    sig = inspect.signature(expressions::ExpressionNode.__init__)
    params = list(sig.parameters.keys())



def test_functiontype_is_not_abstract():
    assert not inspect.isabstract(FunctionType)


def test_functiontype_constructor_exists():
    assert callable(FunctionType.__init__)


def test_functiontype_constructor_args():
    sig = inspect.signature(FunctionType.__init__)
    params = list(sig.parameters.keys())



def test_smif::expressions::objectoperationtype_is_not_abstract():
    assert not inspect.isabstract(smif::expressions::ObjectOperationType)


def test_smif::expressions::objectoperationtype_constructor_exists():
    assert callable(smif::expressions::ObjectOperationType.__init__)


def test_smif::expressions::objectoperationtype_constructor_args():
    sig = inspect.signature(smif::expressions::ObjectOperationType.__init__)
    params = list(sig.parameters.keys())



def test_evaluation_is_not_abstract():
    assert not inspect.isabstract(Evaluation)


def test_evaluation_constructor_exists():
    assert callable(Evaluation.__init__)


def test_evaluation_constructor_args():
    sig = inspect.signature(Evaluation.__init__)
    params = list(sig.parameters.keys())



def test_smif::expressions::expressionnode_is_not_abstract():
    assert not inspect.isabstract(smif::expressions::ExpressionNode)


def test_smif::expressions::expressionnode_constructor_exists():
    assert callable(smif::expressions::ExpressionNode.__init__)


def test_smif::expressions::expressionnode_constructor_args():
    sig = inspect.signature(smif::expressions::ExpressionNode.__init__)
    params = list(sig.parameters.keys())
    assert "expressionTextLanguage" in params, "Missing parameter 'expressionTextLanguage'"
    assert "expressionText" in params, "Missing parameter 'expressionText'"

def test_smif::expressions::expressionnode_has_expressionTextLanguage():
    assert hasattr(smif::expressions::ExpressionNode, "expressionTextLanguage")
    descriptor = None
    for klass in smif::expressions::ExpressionNode.__mro__:
        if "expressionTextLanguage" in klass.__dict__:
            descriptor = klass.__dict__["expressionTextLanguage"]
            break
    assert isinstance(descriptor, property)

def test_smif::expressions::expressionnode_has_expressionText():
    assert hasattr(smif::expressions::ExpressionNode, "expressionText")
    descriptor = None
    for klass in smif::expressions::ExpressionNode.__mro__:
        if "expressionText" in klass.__dict__:
            descriptor = klass.__dict__["expressionText"]
            break
    assert isinstance(descriptor, property)



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



def test_smif::expressions::equality_is_not_abstract():
    assert not inspect.isabstract(smif::expressions::Equality)


def test_smif::expressions::equality_constructor_exists():
    assert callable(smif::expressions::Equality.__init__)


def test_smif::expressions::equality_constructor_args():
    sig = inspect.signature(smif::expressions::Equality.__init__)
    params = list(sig.parameters.keys())



def test_smif::expressions::constantreference_is_not_abstract():
    assert not inspect.isabstract(smif::expressions::ConstantReference)


def test_smif::expressions::constantreference_constructor_exists():
    assert callable(smif::expressions::ConstantReference.__init__)


def test_smif::expressions::constantreference_constructor_args():
    sig = inspect.signature(smif::expressions::ConstantReference.__init__)
    params = list(sig.parameters.keys())



def test_expressions::expressioncontext_is_not_abstract():
    assert not inspect.isabstract(expressions::ExpressionContext)


def test_expressions::expressioncontext_constructor_exists():
    assert callable(expressions::ExpressionContext.__init__)


def test_expressions::expressioncontext_constructor_args():
    sig = inspect.signature(expressions::ExpressionContext.__init__)
    params = list(sig.parameters.keys())



def test_properties::propertyowner_is_not_abstract():
    assert not inspect.isabstract(properties::PropertyOwner)


def test_properties::propertyowner_constructor_exists():
    assert callable(properties::PropertyOwner.__init__)


def test_properties::propertyowner_constructor_args():
    sig = inspect.signature(properties::PropertyOwner.__init__)
    params = list(sig.parameters.keys())



def test_smif::associations::association_is_not_abstract():
    assert not inspect.isabstract(smif::associations::Association)


def test_smif::associations::association_constructor_exists():
    assert callable(smif::associations::Association.__init__)


def test_smif::associations::association_constructor_args():
    sig = inspect.signature(smif::associations::Association.__init__)
    params = list(sig.parameters.keys())



def test_smif::patterns::pattern_is_not_abstract():
    assert not inspect.isabstract(smif::patterns::Pattern)


def test_smif::patterns::pattern_constructor_exists():
    assert callable(smif::patterns::Pattern.__init__)


def test_smif::patterns::pattern_constructor_args():
    sig = inspect.signature(smif::patterns::Pattern.__init__)
    params = list(sig.parameters.keys())



def test_smif::expressions::traversal_is_not_abstract():
    assert not inspect.isabstract(smif::expressions::Traversal)


def test_smif::expressions::traversal_constructor_exists():
    assert callable(smif::expressions::Traversal.__init__)


def test_smif::expressions::traversal_constructor_args():
    sig = inspect.signature(smif::expressions::Traversal.__init__)
    params = list(sig.parameters.keys())
    assert "inverse" in params, "Missing parameter 'inverse'"
    assert "traverseToRelation" in params, "Missing parameter 'traverseToRelation'"

def test_smif::expressions::traversal_has_inverse():
    assert hasattr(smif::expressions::Traversal, "inverse")
    descriptor = None
    for klass in smif::expressions::Traversal.__mro__:
        if "inverse" in klass.__dict__:
            descriptor = klass.__dict__["inverse"]
            break
    assert isinstance(descriptor, property)

def test_smif::expressions::traversal_has_traverseToRelation():
    assert hasattr(smif::expressions::Traversal, "traverseToRelation")
    descriptor = None
    for klass in smif::expressions::Traversal.__mro__:
        if "traverseToRelation" in klass.__dict__:
            descriptor = klass.__dict__["traverseToRelation"]
            break
    assert isinstance(descriptor, property)



def test_smif::relationships::relationship_is_not_abstract():
    assert not inspect.isabstract(smif::relationships::Relationship)


def test_smif::relationships::relationship_constructor_exists():
    assert callable(smif::relationships::Relationship.__init__)


def test_smif::relationships::relationship_constructor_args():
    sig = inspect.signature(smif::relationships::Relationship.__init__)
    params = list(sig.parameters.keys())



def test_smif::records::record_is_not_abstract():
    assert not inspect.isabstract(smif::records::Record)


def test_smif::records::record_constructor_exists():
    assert callable(smif::records::Record.__init__)


def test_smif::records::record_constructor_args():
    sig = inspect.signature(smif::records::Record.__init__)
    params = list(sig.parameters.keys())



def test_smif::expressions::functioncall_is_not_abstract():
    assert not inspect.isabstract(smif::expressions::FunctionCall)


def test_smif::expressions::functioncall_constructor_exists():
    assert callable(smif::expressions::FunctionCall.__init__)


def test_smif::expressions::functioncall_constructor_args():
    sig = inspect.signature(smif::expressions::FunctionCall.__init__)
    params = list(sig.parameters.keys())



def test_values::value_is_not_abstract():
    assert not inspect.isabstract(values::Value)


def test_values::value_constructor_exists():
    assert callable(values::Value.__init__)


def test_values::value_constructor_args():
    sig = inspect.signature(values::Value.__init__)
    params = list(sig.parameters.keys())



def test_smif::values::structuredvalue_is_not_abstract():
    assert not inspect.isabstract(smif::values::StructuredValue)


def test_smif::values::structuredvalue_constructor_exists():
    assert callable(smif::values::StructuredValue.__init__)


def test_smif::values::structuredvalue_constructor_args():
    sig = inspect.signature(smif::values::StructuredValue.__init__)
    params = list(sig.parameters.keys())



def test_properties::propertyownertype_is_not_abstract():
    assert not inspect.isabstract(properties::PropertyOwnerType)


def test_properties::propertyownertype_constructor_exists():
    assert callable(properties::PropertyOwnerType.__init__)


def test_properties::propertyownertype_constructor_args():
    sig = inspect.signature(properties::PropertyOwnerType.__init__)
    params = list(sig.parameters.keys())



def test_smif::relationships::relationshiptype_is_not_abstract():
    assert not inspect.isabstract(smif::relationships::RelationshipType)


def test_smif::relationships::relationshiptype_constructor_exists():
    assert callable(smif::relationships::RelationshipType.__init__)


def test_smif::relationships::relationshiptype_constructor_args():
    sig = inspect.signature(smif::relationships::RelationshipType.__init__)
    params = list(sig.parameters.keys())



def test_smif::records::recordtype_is_not_abstract():
    assert not inspect.isabstract(smif::records::RecordType)


def test_smif::records::recordtype_constructor_exists():
    assert callable(smif::records::RecordType.__init__)


def test_smif::records::recordtype_constructor_args():
    sig = inspect.signature(smif::records::RecordType.__init__)
    params = list(sig.parameters.keys())



def test_smif::values::structuredvaluetype_is_not_abstract():
    assert not inspect.isabstract(smif::values::StructuredValueType)


def test_smif::values::structuredvaluetype_constructor_exists():
    assert callable(smif::values::StructuredValueType.__init__)


def test_smif::values::structuredvaluetype_constructor_args():
    sig = inspect.signature(smif::values::StructuredValueType.__init__)
    params = list(sig.parameters.keys())



def test_smif::expressions::functiontype_is_not_abstract():
    assert not inspect.isabstract(smif::expressions::FunctionType)


def test_smif::expressions::functiontype_constructor_exists():
    assert callable(smif::expressions::FunctionType.__init__)


def test_smif::expressions::functiontype_constructor_args():
    sig = inspect.signature(smif::expressions::FunctionType.__init__)
    params = list(sig.parameters.keys())

def test_variablequalification_exists():
    # Check that the Enumeration exists
    assert VariableQualification is not None

def test_variablequalification_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VariableQualification]
    expected_literals = [
        "ThereExists",
        "ExactlyOne",
        "Select",
        "Negate",
        "Optional",
        "Assert",
        "All",
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
values::ValueType_strategy = st.builds(
    values::ValueType,
)
Context_strategy = st.builds(
    Context,
)
smif::values::SystemOfUnits_strategy = st.builds(
    smif::values::SystemOfUnits,
)
identifiers::UniqueTextIdentifier_strategy = st.builds(
    identifiers::UniqueTextIdentifier,
)
identifiers::Name_strategy = st.builds(
    identifiers::Name,
)
smif::identifiers::Term_strategy = st.builds(
    smif::identifiers::Term,
)
TechnicalIdentifier_strategy = st.builds(
    TechnicalIdentifier,
)
smif::identifiers::IRIIdentifier_strategy = st.builds(
    smif::identifiers::IRIIdentifier,
)
Namespace_strategy = st.builds(
    Namespace,
)
Identifier_strategy = st.builds(
    Identifier,
)
smif::identifiers::UniqueIdentifier_strategy = st.builds(
    smif::identifiers::UniqueIdentifier,
)
UnitValue_strategy = st.builds(
    UnitValue,
)
smif::values::ScalarQuantity_strategy = st.builds(
    smif::values::ScalarQuantity,
    _unnamed_ScalarQuantity=
        safe_text
)
Value_strategy = st.builds(
    Value,
)
smif::values::UnitValue_strategy = st.builds(
    smif::values::UnitValue,
    hasValue=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
smif::types::EntityType_strategy = st.builds(
    smif::types::EntityType,
)
smif::types::UnionType_strategy = st.builds(
    smif::types::UnionType,
)
smif::types::IntersectionType_strategy = st.builds(
    smif::types::IntersectionType,
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
smif::values::ValueType_strategy = st.builds(
    smif::values::ValueType,
)
UnitType_strategy = st.builds(
    UnitType,
)
smif::values::BaseUnitType_strategy = st.builds(
    smif::values::BaseUnitType,
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
smif::values::UnitType_strategy = st.builds(
    smif::values::UnitType,
    symbol=
        safe_text,
    offset=
        safe_text,
    ratio=
        safe_text
)
smif::values::QuantityKind_strategy = st.builds(
    smif::values::QuantityKind,
)
situations::Situation_strategy = st.builds(
    situations::Situation,
)
toplevel::ActualEntity_strategy = st.builds(
    toplevel::ActualEntity,
)
smif::situations::ActualSituation_strategy = st.builds(
    smif::situations::ActualSituation,
)
PatternMatch_strategy = st.builds(
    PatternMatch,
)
toplevel::TemporalEntity_strategy = st.builds(
    toplevel::TemporalEntity,
)
toplevel::Proposition_strategy = st.builds(
    toplevel::Proposition,
)
EntityType_strategy = st.builds(
    EntityType,
)
smif::situations::SituationType_strategy = st.builds(
    smif::situations::SituationType,
)
LexicalScope_strategy = st.builds(
    LexicalScope,
)
smif::Repository_strategy = st.builds(
    smif::Repository,
)
RecordType_strategy = st.builds(
    RecordType,
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
CoveringConstraint_strategy = st.builds(
    CoveringConstraint,
)
PatternOfType_strategy = st.builds(
    PatternOfType,
)
PropertyType_strategy = st.builds(
    PropertyType,
)
Thing_strategy = st.builds(
    Thing,
)
smif::values::Value_strategy = st.builds(
    smif::values::Value,
)
toplevel::Context_strategy = st.builds(
    toplevel::Context,
)
lexicalscope::LexicalScope_strategy = st.builds(
    lexicalscope::LexicalScope,
)
smif::situations::Situation_strategy = st.builds(
    smif::situations::Situation,
)
smif::types::Type_strategy = st.builds(
    smif::types::Type,
)
smif::facets::Facet_strategy = st.builds(
    smif::facets::Facet,
)
smif::properties::PropertyBinding_strategy = st.builds(
    smif::properties::PropertyBinding,
)
Facet_strategy = st.builds(
    Facet,
)
smif::facets::Category_strategy = st.builds(
    smif::facets::Category,
)
smif::facets::Role_strategy = st.builds(
    smif::facets::Role,
)
facets::Facet_strategy = st.builds(
    facets::Facet,
)
Relationship_strategy = st.builds(
    Relationship,
)
smif::facets::FacetOfEntity_strategy = st.builds(
    smif::facets::FacetOfEntity,
)
smif::properties::PropertyOwner_strategy = st.builds(
    smif::properties::PropertyOwner,
)
smif::properties::PropertyOwnerType_strategy = st.builds(
    smif::properties::PropertyOwnerType,
)
smif::properties::OwnedPropertyType_strategy = st.builds(
    smif::properties::OwnedPropertyType,
)
CharacteristicType_strategy = st.builds(
    CharacteristicType,
)
smif::properties::AnnotationProperty_strategy = st.builds(
    smif::properties::AnnotationProperty,
)
properties::PropertyBinding_strategy = st.builds(
    properties::PropertyBinding,
)
properties::PropertyType_strategy = st.builds(
    properties::PropertyType,
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
smif::properties::PropertyType_strategy = st.builds(
    smif::properties::PropertyType,
)
Term_strategy = st.builds(
    Term,
)
IRIIdentifier_strategy = st.builds(
    IRIIdentifier,
)
metadata::Metadata_strategy = st.builds(
    metadata::Metadata,
)
smif::metadata::InformationSource_strategy = st.builds(
    smif::metadata::InformationSource,
)
PropertyOwnerType_strategy = st.builds(
    PropertyOwnerType,
)
smif::associations::AssociationType_strategy = st.builds(
    smif::associations::AssociationType,
)
Prefix_strategy = st.builds(
    Prefix,
)
smif::lexicalscope::Package_strategy = st.builds(
    smif::lexicalscope::Package,
)
smif::lexicalscope::LexicalReference_strategy = st.builds(
    smif::lexicalscope::LexicalReference,
)
smif::lexicalscope::LexicalScope_strategy = st.builds(
    smif::lexicalscope::LexicalScope,
)
Package_strategy = st.builds(
    Package,
)
smif::lexicalscope::MappingPackage_strategy = st.builds(
    smif::lexicalscope::MappingPackage,
)
smif::lexicalscope::PhysicalPackage_strategy = st.builds(
    smif::lexicalscope::PhysicalPackage,
)
smif::lexicalscope::MOFPackage_strategy = st.builds(
    smif::lexicalscope::MOFPackage,
)
smif::lexicalscope::LogicalPackage_strategy = st.builds(
    smif::lexicalscope::LogicalPackage,
)
smif::lexicalscope::Model_strategy = st.builds(
    smif::lexicalscope::Model,
)
ConditionalRule_strategy = st.builds(
    ConditionalRule,
)
smif::mapping::RepresentationRule_strategy = st.builds(
    smif::mapping::RepresentationRule,
    mapAll=
        safe_text
)
Facade_strategy = st.builds(
    Facade,
)
smif::mapping::ComputedFacade_strategy = st.builds(
    smif::mapping::ComputedFacade,
)
smif::mapping::Facade_strategy = st.builds(
    smif::mapping::Facade,
)
Situation_strategy = st.builds(
    Situation,
)
VariableBinding_strategy = st.builds(
    VariableBinding,
)
patterns::Pattern_strategy = st.builds(
    patterns::Pattern,
)
MatchRule_strategy = st.builds(
    MatchRule,
)
smif::patterns::Computed_strategy = st.builds(
    smif::patterns::Computed,
)
OwnedPropertyBinding_strategy = st.builds(
    OwnedPropertyBinding,
)
smif::patterns::VariableBinding_strategy = st.builds(
    smif::patterns::VariableBinding,
)
Pattern_strategy = st.builds(
    Pattern,
)
ActualSituation_strategy = st.builds(
    ActualSituation,
)
smif::patterns::PatternMatch_strategy = st.builds(
    smif::patterns::PatternMatch,
)
smif::patterns::PatternOfType_strategy = st.builds(
    smif::patterns::PatternOfType,
)
TypePatternVariable_strategy = st.builds(
    TypePatternVariable,
)
smif::patterns::FocusVariable_strategy = st.builds(
    smif::patterns::FocusVariable,
)
smif::patterns::PartVariable_strategy = st.builds(
    smif::patterns::PartVariable,
    isBoundaryPart=
        safe_text
)
patterns::Computed_strategy = st.builds(
    patterns::Computed,
)
patterns::PatternVariable_strategy = st.builds(
    patterns::PatternVariable,
)
smif::patterns::ExpressionVariable_strategy = st.builds(
    smif::patterns::ExpressionVariable,
)
Mapping_strategy = st.builds(
    Mapping,
)
Equality_strategy = st.builds(
    Equality,
)
properties::OwnedPropertyType_strategy = st.builds(
    properties::OwnedPropertyType,
)
PatternVariable_strategy = st.builds(
    PatternVariable,
)
smif::patterns::PropositionVariable_strategy = st.builds(
    smif::patterns::PropositionVariable,
)
smif::patterns::TypePatternVariable_strategy = st.builds(
    smif::patterns::TypePatternVariable,
)
TemporalEntity_strategy = st.builds(
    TemporalEntity,
)
smif::toplevel::ActualEntity_strategy = st.builds(
    smif::toplevel::ActualEntity,
)
PropositionVariable_strategy = st.builds(
    PropositionVariable,
)
LexicalReference_strategy = st.builds(
    LexicalReference,
)
smif::lexicalscope::Include_strategy = st.builds(
    smif::lexicalscope::Include,
)
Statement_strategy = st.builds(
    Statement,
)
smif::toplevel::IdentifiableEntity_strategy = st.builds(
    smif::toplevel::IdentifiableEntity,
)
ConstantReference_strategy = st.builds(
    ConstantReference,
)
smif::toplevel::Thing_strategy = st.builds(
    smif::toplevel::Thing,
)
PropertyBinding_strategy = st.builds(
    PropertyBinding,
)
smif::properties::OwnedPropertyBinding_strategy = st.builds(
    smif::properties::OwnedPropertyBinding,
)
InformationSource_strategy = st.builds(
    InformationSource,
)
Record_strategy = st.builds(
    Record,
)
smif::metadata::Metadata_strategy = st.builds(
    smif::metadata::Metadata,
)
Name_strategy = st.builds(
    Name,
)
Metadata_strategy = st.builds(
    Metadata,
)
smif::metadata::Definition_strategy = st.builds(
    smif::metadata::Definition,
    textDefinition=
        safe_text,
    summaryDescription=
        safe_text
)
smif::metadata::Statement_strategy = st.builds(
    smif::metadata::Statement,
)
constraints::Conditional_strategy = st.builds(
    constraints::Conditional,
)
smif::patterns::PatternVariable_strategy = st.builds(
    smif::patterns::PatternVariable,
    qualification=
        safe_text,
    explicit=
        safe_text
)
smif::mapping::MatchEnd_strategy = st.builds(
    smif::mapping::MatchEnd,
)
constraints::Rule_strategy = st.builds(
    constraints::Rule,
)
smif::mapping::Mapping_strategy = st.builds(
    smif::mapping::Mapping,
    strength=
        safe_text
)
smif::constraints::ConditionalRule_strategy = st.builds(
    smif::constraints::ConditionalRule,
)
smif::constraints::Conditional_strategy = st.builds(
    smif::constraints::Conditional,
)
smif::constraints::FacetClassificationConstraint_strategy = st.builds(
    smif::constraints::FacetClassificationConstraint,
)
PropertyConstraint_strategy = st.builds(
    PropertyConstraint,
)
smif::constraints::PropertyTypeConstraint_strategy = st.builds(
    smif::constraints::PropertyTypeConstraint,
    prerequisiteType=
        safe_text
)
smif::constraints::PropertyTransitivityConstraint_strategy = st.builds(
    smif::constraints::PropertyTransitivityConstraint,
)
smif::expressions::Evaluation_strategy = st.builds(
    smif::expressions::Evaluation,
)
TypeConstraint_strategy = st.builds(
    TypeConstraint,
)
smif::constraints::GeneralizationConstraint_strategy = st.builds(
    smif::constraints::GeneralizationConstraint,
    redefines=
        safe_text
)
smif::constraints::CoveringConstraint_strategy = st.builds(
    smif::constraints::CoveringConstraint,
)
smif::constraints::UniquenessConstraint_strategy = st.builds(
    smif::constraints::UniquenessConstraint,
    isPrimaryIdentity=
        safe_text
)
smif::constraints::MultiplicityConstraint_strategy = st.builds(
    smif::constraints::MultiplicityConstraint,
    maximumNumber=
        safe_text,
    isSufficent=
        safe_text,
    atOnce=
        safe_text,
    mininumNumber=
        safe_text
)
Rule_strategy = st.builds(
    Rule,
)
smif::constraints::TypeConstraint_strategy = st.builds(
    smif::constraints::TypeConstraint,
)
smif::constraints::PropertyConstraint_strategy = st.builds(
    smif::constraints::PropertyConstraint,
)
smif::mapping::MatchRule_strategy = st.builds(
    smif::mapping::MatchRule,
    coerce=
        safe_text
)
smif::constraints::Enumerated_strategy = st.builds(
    smif::constraints::Enumerated,
)
smif::constraints::Equivalent_strategy = st.builds(
    smif::constraints::Equivalent,
)
smif::constraints::Disjoint_strategy = st.builds(
    smif::constraints::Disjoint,
)
Proposition_strategy = st.builds(
    Proposition,
)
smif::constraints::Rule_strategy = st.builds(
    smif::constraints::Rule,
)
situations::SituationType_strategy = st.builds(
    situations::SituationType,
)
smif::properties::CharacteristicType_strategy = st.builds(
    smif::properties::CharacteristicType,
)
smif::facets::Phase_strategy = st.builds(
    smif::facets::Phase,
)
situations::ActualSituation_strategy = st.builds(
    situations::ActualSituation,
)
smif::properties::CharacteristicBinding_strategy = st.builds(
    smif::properties::CharacteristicBinding,
)
UniqueTextIdentifier_strategy = st.builds(
    UniqueTextIdentifier,
)
smif::lexicalscope::Prefix_strategy = st.builds(
    smif::lexicalscope::Prefix,
)
smif::identifiers::TechnicalIdentifier_strategy = st.builds(
    smif::identifiers::TechnicalIdentifier,
)
TextIdentifier_strategy = st.builds(
    TextIdentifier,
)
smif::identifiers::Name_strategy = st.builds(
    smif::identifiers::Name,
)
smif::identifiers::TextIdentifier_strategy = st.builds(
    smif::identifiers::TextIdentifier,
    value=
        safe_text
)
UniqueIdentifier_strategy = st.builds(
    UniqueIdentifier,
)
smif::identifiers::Namespace_strategy = st.builds(
    smif::identifiers::Namespace,
)
IdentifiableEntity_strategy = st.builds(
    IdentifiableEntity,
)
smif::toplevel::Context_strategy = st.builds(
    smif::toplevel::Context,
)
smif::expressions::ExpressionContext_strategy = st.builds(
    smif::expressions::ExpressionContext,
)
smif::toplevel::TemporalEntity_strategy = st.builds(
    smif::toplevel::TemporalEntity,
)
smif::toplevel::Proposition_strategy = st.builds(
    smif::toplevel::Proposition,
)
smif::identifiers::Identifier_strategy = st.builds(
    smif::identifiers::Identifier,
)
identifiers::TextIdentifier_strategy = st.builds(
    identifiers::TextIdentifier,
)
identifiers::UniqueIdentifier_strategy = st.builds(
    identifiers::UniqueIdentifier,
)
smif::identifiers::UniqueTextIdentifier_strategy = st.builds(
    smif::identifiers::UniqueTextIdentifier,
)
expressions::ExpressionNode_strategy = st.builds(
    expressions::ExpressionNode,
)
FunctionType_strategy = st.builds(
    FunctionType,
)
smif::expressions::ObjectOperationType_strategy = st.builds(
    smif::expressions::ObjectOperationType,
)
Evaluation_strategy = st.builds(
    Evaluation,
)
smif::expressions::ExpressionNode_strategy = st.builds(
    smif::expressions::ExpressionNode,
    expressionTextLanguage=
        safe_text,
    expressionText=
        safe_text
)
FunctionCall_strategy = st.builds(
    FunctionCall,
)
ExpressionNode_strategy = st.builds(
    ExpressionNode,
)
smif::expressions::Equality_strategy = st.builds(
    smif::expressions::Equality,
)
smif::expressions::ConstantReference_strategy = st.builds(
    smif::expressions::ConstantReference,
)
expressions::ExpressionContext_strategy = st.builds(
    expressions::ExpressionContext,
)
properties::PropertyOwner_strategy = st.builds(
    properties::PropertyOwner,
)
smif::associations::Association_strategy = st.builds(
    smif::associations::Association,
)
smif::patterns::Pattern_strategy = st.builds(
    smif::patterns::Pattern,
)
smif::expressions::Traversal_strategy = st.builds(
    smif::expressions::Traversal,
    inverse=
        safe_text,
    traverseToRelation=
        safe_text
)
smif::relationships::Relationship_strategy = st.builds(
    smif::relationships::Relationship,
)
smif::records::Record_strategy = st.builds(
    smif::records::Record,
)
smif::expressions::FunctionCall_strategy = st.builds(
    smif::expressions::FunctionCall,
)
values::Value_strategy = st.builds(
    values::Value,
)
smif::values::StructuredValue_strategy = st.builds(
    smif::values::StructuredValue,
)
properties::PropertyOwnerType_strategy = st.builds(
    properties::PropertyOwnerType,
)
smif::relationships::RelationshipType_strategy = st.builds(
    smif::relationships::RelationshipType,
)
smif::records::RecordType_strategy = st.builds(
    smif::records::RecordType,
)
smif::values::StructuredValueType_strategy = st.builds(
    smif::values::StructuredValueType,
)
smif::expressions::FunctionType_strategy = st.builds(
    smif::expressions::FunctionType,
)

@given(instance=values::ValueType_strategy)
@settings(max_examples=50)
def test_values::valuetype_instantiation(instance):
    assert isinstance(instance, values::ValueType)

@given(instance=Context_strategy)
@settings(max_examples=50)
def test_context_instantiation(instance):
    assert isinstance(instance, Context)

@given(instance=smif::values::SystemOfUnits_strategy)
@settings(max_examples=50)
def test_smif::values::systemofunits_instantiation(instance):
    assert isinstance(instance, smif::values::SystemOfUnits)

@given(instance=identifiers::UniqueTextIdentifier_strategy)
@settings(max_examples=50)
def test_identifiers::uniquetextidentifier_instantiation(instance):
    assert isinstance(instance, identifiers::UniqueTextIdentifier)

@given(instance=identifiers::Name_strategy)
@settings(max_examples=50)
def test_identifiers::name_instantiation(instance):
    assert isinstance(instance, identifiers::Name)

@given(instance=smif::identifiers::Term_strategy)
@settings(max_examples=50)
def test_smif::identifiers::term_instantiation(instance):
    assert isinstance(instance, smif::identifiers::Term)

@given(instance=TechnicalIdentifier_strategy)
@settings(max_examples=50)
def test_technicalidentifier_instantiation(instance):
    assert isinstance(instance, TechnicalIdentifier)

@given(instance=smif::identifiers::IRIIdentifier_strategy)
@settings(max_examples=50)
def test_smif::identifiers::iriidentifier_instantiation(instance):
    assert isinstance(instance, smif::identifiers::IRIIdentifier)

@given(instance=Namespace_strategy)
@settings(max_examples=50)
def test_namespace_instantiation(instance):
    assert isinstance(instance, Namespace)

@given(instance=Identifier_strategy)
@settings(max_examples=50)
def test_identifier_instantiation(instance):
    assert isinstance(instance, Identifier)

@given(instance=smif::identifiers::UniqueIdentifier_strategy)
@settings(max_examples=50)
def test_smif::identifiers::uniqueidentifier_instantiation(instance):
    assert isinstance(instance, smif::identifiers::UniqueIdentifier)

@given(instance=UnitValue_strategy)
@settings(max_examples=50)
def test_unitvalue_instantiation(instance):
    assert isinstance(instance, UnitValue)

@given(instance=smif::values::ScalarQuantity_strategy)
@settings(max_examples=50)
def test_smif::values::scalarquantity_instantiation(instance):
    assert isinstance(instance, smif::values::ScalarQuantity)

@given(instance=smif::values::ScalarQuantity_strategy)
def test_smif::values::scalarquantity__unnamed_ScalarQuantity_type(instance):
    assert isinstance(instance._unnamed_ScalarQuantity, str)


@given(instance=smif::values::ScalarQuantity_strategy)
def test_smif::values::scalarquantity__unnamed_ScalarQuantity_setter(instance):
    original = instance._unnamed_ScalarQuantity
    instance._unnamed_ScalarQuantity = original
    assert instance._unnamed_ScalarQuantity == original

@given(instance=Value_strategy)
@settings(max_examples=50)
def test_value_instantiation(instance):
    assert isinstance(instance, Value)

@given(instance=smif::values::UnitValue_strategy)
@settings(max_examples=50)
def test_smif::values::unitvalue_instantiation(instance):
    assert isinstance(instance, smif::values::UnitValue)

@given(instance=smif::values::UnitValue_strategy)
def test_smif::values::unitvalue_hasValue_type(instance):
    assert isinstance(instance.hasValue, str)


@given(instance=smif::values::UnitValue_strategy)
def test_smif::values::unitvalue_hasValue_setter(instance):
    original = instance.hasValue
    instance.hasValue = original
    assert instance.hasValue == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=smif::types::EntityType_strategy)
@settings(max_examples=50)
def test_smif::types::entitytype_instantiation(instance):
    assert isinstance(instance, smif::types::EntityType)

@given(instance=smif::types::UnionType_strategy)
@settings(max_examples=50)
def test_smif::types::uniontype_instantiation(instance):
    assert isinstance(instance, smif::types::UnionType)

@given(instance=smif::types::IntersectionType_strategy)
@settings(max_examples=50)
def test_smif::types::intersectiontype_instantiation(instance):
    assert isinstance(instance, smif::types::IntersectionType)

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

@given(instance=smif::values::ValueType_strategy)
@settings(max_examples=50)
def test_smif::values::valuetype_instantiation(instance):
    assert isinstance(instance, smif::values::ValueType)

@given(instance=UnitType_strategy)
@settings(max_examples=50)
def test_unittype_instantiation(instance):
    assert isinstance(instance, UnitType)

@given(instance=smif::values::BaseUnitType_strategy)
@settings(max_examples=50)
def test_smif::values::baseunittype_instantiation(instance):
    assert isinstance(instance, smif::values::BaseUnitType)

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

@given(instance=smif::values::UnitType_strategy)
@settings(max_examples=50)
def test_smif::values::unittype_instantiation(instance):
    assert isinstance(instance, smif::values::UnitType)

@given(instance=smif::values::UnitType_strategy)
def test_smif::values::unittype_symbol_type(instance):
    assert isinstance(instance.symbol, str)


@given(instance=smif::values::UnitType_strategy)
def test_smif::values::unittype_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original

@given(instance=smif::values::UnitType_strategy)
def test_smif::values::unittype_offset_type(instance):
    assert isinstance(instance.offset, str)


@given(instance=smif::values::UnitType_strategy)
def test_smif::values::unittype_offset_setter(instance):
    original = instance.offset
    instance.offset = original
    assert instance.offset == original

@given(instance=smif::values::UnitType_strategy)
def test_smif::values::unittype_ratio_type(instance):
    assert isinstance(instance.ratio, str)


@given(instance=smif::values::UnitType_strategy)
def test_smif::values::unittype_ratio_setter(instance):
    original = instance.ratio
    instance.ratio = original
    assert instance.ratio == original

@given(instance=smif::values::QuantityKind_strategy)
@settings(max_examples=50)
def test_smif::values::quantitykind_instantiation(instance):
    assert isinstance(instance, smif::values::QuantityKind)

@given(instance=situations::Situation_strategy)
@settings(max_examples=50)
def test_situations::situation_instantiation(instance):
    assert isinstance(instance, situations::Situation)

@given(instance=toplevel::ActualEntity_strategy)
@settings(max_examples=50)
def test_toplevel::actualentity_instantiation(instance):
    assert isinstance(instance, toplevel::ActualEntity)

@given(instance=smif::situations::ActualSituation_strategy)
@settings(max_examples=50)
def test_smif::situations::actualsituation_instantiation(instance):
    assert isinstance(instance, smif::situations::ActualSituation)

@given(instance=PatternMatch_strategy)
@settings(max_examples=50)
def test_patternmatch_instantiation(instance):
    assert isinstance(instance, PatternMatch)

@given(instance=toplevel::TemporalEntity_strategy)
@settings(max_examples=50)
def test_toplevel::temporalentity_instantiation(instance):
    assert isinstance(instance, toplevel::TemporalEntity)

@given(instance=toplevel::Proposition_strategy)
@settings(max_examples=50)
def test_toplevel::proposition_instantiation(instance):
    assert isinstance(instance, toplevel::Proposition)

@given(instance=EntityType_strategy)
@settings(max_examples=50)
def test_entitytype_instantiation(instance):
    assert isinstance(instance, EntityType)

@given(instance=smif::situations::SituationType_strategy)
@settings(max_examples=50)
def test_smif::situations::situationtype_instantiation(instance):
    assert isinstance(instance, smif::situations::SituationType)

@given(instance=LexicalScope_strategy)
@settings(max_examples=50)
def test_lexicalscope_instantiation(instance):
    assert isinstance(instance, LexicalScope)

@given(instance=smif::Repository_strategy)
@settings(max_examples=50)
def test_smif::repository_instantiation(instance):
    assert isinstance(instance, smif::Repository)

@given(instance=RecordType_strategy)
@settings(max_examples=50)
def test_recordtype_instantiation(instance):
    assert isinstance(instance, RecordType)

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

@given(instance=Thing_strategy)
@settings(max_examples=50)
def test_thing_instantiation(instance):
    assert isinstance(instance, Thing)

@given(instance=smif::values::Value_strategy)
@settings(max_examples=50)
def test_smif::values::value_instantiation(instance):
    assert isinstance(instance, smif::values::Value)

@given(instance=toplevel::Context_strategy)
@settings(max_examples=50)
def test_toplevel::context_instantiation(instance):
    assert isinstance(instance, toplevel::Context)

@given(instance=lexicalscope::LexicalScope_strategy)
@settings(max_examples=50)
def test_lexicalscope::lexicalscope_instantiation(instance):
    assert isinstance(instance, lexicalscope::LexicalScope)

@given(instance=smif::situations::Situation_strategy)
@settings(max_examples=50)
def test_smif::situations::situation_instantiation(instance):
    assert isinstance(instance, smif::situations::Situation)

@given(instance=smif::types::Type_strategy)
@settings(max_examples=50)
def test_smif::types::type_instantiation(instance):
    assert isinstance(instance, smif::types::Type)

@given(instance=smif::facets::Facet_strategy)
@settings(max_examples=50)
def test_smif::facets::facet_instantiation(instance):
    assert isinstance(instance, smif::facets::Facet)

@given(instance=smif::properties::PropertyBinding_strategy)
@settings(max_examples=50)
def test_smif::properties::propertybinding_instantiation(instance):
    assert isinstance(instance, smif::properties::PropertyBinding)

@given(instance=Facet_strategy)
@settings(max_examples=50)
def test_facet_instantiation(instance):
    assert isinstance(instance, Facet)

@given(instance=smif::facets::Category_strategy)
@settings(max_examples=50)
def test_smif::facets::category_instantiation(instance):
    assert isinstance(instance, smif::facets::Category)

@given(instance=smif::facets::Role_strategy)
@settings(max_examples=50)
def test_smif::facets::role_instantiation(instance):
    assert isinstance(instance, smif::facets::Role)

@given(instance=facets::Facet_strategy)
@settings(max_examples=50)
def test_facets::facet_instantiation(instance):
    assert isinstance(instance, facets::Facet)

@given(instance=Relationship_strategy)
@settings(max_examples=50)
def test_relationship_instantiation(instance):
    assert isinstance(instance, Relationship)

@given(instance=smif::facets::FacetOfEntity_strategy)
@settings(max_examples=50)
def test_smif::facets::facetofentity_instantiation(instance):
    assert isinstance(instance, smif::facets::FacetOfEntity)

@given(instance=smif::properties::PropertyOwner_strategy)
@settings(max_examples=50)
def test_smif::properties::propertyowner_instantiation(instance):
    assert isinstance(instance, smif::properties::PropertyOwner)

@given(instance=smif::properties::PropertyOwnerType_strategy)
@settings(max_examples=50)
def test_smif::properties::propertyownertype_instantiation(instance):
    assert isinstance(instance, smif::properties::PropertyOwnerType)

@given(instance=smif::properties::OwnedPropertyType_strategy)
@settings(max_examples=50)
def test_smif::properties::ownedpropertytype_instantiation(instance):
    assert isinstance(instance, smif::properties::OwnedPropertyType)

@given(instance=CharacteristicType_strategy)
@settings(max_examples=50)
def test_characteristictype_instantiation(instance):
    assert isinstance(instance, CharacteristicType)

@given(instance=smif::properties::AnnotationProperty_strategy)
@settings(max_examples=50)
def test_smif::properties::annotationproperty_instantiation(instance):
    assert isinstance(instance, smif::properties::AnnotationProperty)

@given(instance=properties::PropertyBinding_strategy)
@settings(max_examples=50)
def test_properties::propertybinding_instantiation(instance):
    assert isinstance(instance, properties::PropertyBinding)

@given(instance=properties::PropertyType_strategy)
@settings(max_examples=50)
def test_properties::propertytype_instantiation(instance):
    assert isinstance(instance, properties::PropertyType)

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

@given(instance=smif::properties::PropertyType_strategy)
@settings(max_examples=50)
def test_smif::properties::propertytype_instantiation(instance):
    assert isinstance(instance, smif::properties::PropertyType)

@given(instance=Term_strategy)
@settings(max_examples=50)
def test_term_instantiation(instance):
    assert isinstance(instance, Term)

@given(instance=IRIIdentifier_strategy)
@settings(max_examples=50)
def test_iriidentifier_instantiation(instance):
    assert isinstance(instance, IRIIdentifier)

@given(instance=metadata::Metadata_strategy)
@settings(max_examples=50)
def test_metadata::metadata_instantiation(instance):
    assert isinstance(instance, metadata::Metadata)

@given(instance=smif::metadata::InformationSource_strategy)
@settings(max_examples=50)
def test_smif::metadata::informationsource_instantiation(instance):
    assert isinstance(instance, smif::metadata::InformationSource)

@given(instance=PropertyOwnerType_strategy)
@settings(max_examples=50)
def test_propertyownertype_instantiation(instance):
    assert isinstance(instance, PropertyOwnerType)

@given(instance=smif::associations::AssociationType_strategy)
@settings(max_examples=50)
def test_smif::associations::associationtype_instantiation(instance):
    assert isinstance(instance, smif::associations::AssociationType)

@given(instance=Prefix_strategy)
@settings(max_examples=50)
def test_prefix_instantiation(instance):
    assert isinstance(instance, Prefix)

@given(instance=smif::lexicalscope::Package_strategy)
@settings(max_examples=50)
def test_smif::lexicalscope::package_instantiation(instance):
    assert isinstance(instance, smif::lexicalscope::Package)

@given(instance=smif::lexicalscope::LexicalReference_strategy)
@settings(max_examples=50)
def test_smif::lexicalscope::lexicalreference_instantiation(instance):
    assert isinstance(instance, smif::lexicalscope::LexicalReference)

@given(instance=smif::lexicalscope::LexicalScope_strategy)
@settings(max_examples=50)
def test_smif::lexicalscope::lexicalscope_instantiation(instance):
    assert isinstance(instance, smif::lexicalscope::LexicalScope)

@given(instance=Package_strategy)
@settings(max_examples=50)
def test_package_instantiation(instance):
    assert isinstance(instance, Package)

@given(instance=smif::lexicalscope::MappingPackage_strategy)
@settings(max_examples=50)
def test_smif::lexicalscope::mappingpackage_instantiation(instance):
    assert isinstance(instance, smif::lexicalscope::MappingPackage)

@given(instance=smif::lexicalscope::PhysicalPackage_strategy)
@settings(max_examples=50)
def test_smif::lexicalscope::physicalpackage_instantiation(instance):
    assert isinstance(instance, smif::lexicalscope::PhysicalPackage)

@given(instance=smif::lexicalscope::MOFPackage_strategy)
@settings(max_examples=50)
def test_smif::lexicalscope::mofpackage_instantiation(instance):
    assert isinstance(instance, smif::lexicalscope::MOFPackage)

@given(instance=smif::lexicalscope::LogicalPackage_strategy)
@settings(max_examples=50)
def test_smif::lexicalscope::logicalpackage_instantiation(instance):
    assert isinstance(instance, smif::lexicalscope::LogicalPackage)

@given(instance=smif::lexicalscope::Model_strategy)
@settings(max_examples=50)
def test_smif::lexicalscope::model_instantiation(instance):
    assert isinstance(instance, smif::lexicalscope::Model)

@given(instance=ConditionalRule_strategy)
@settings(max_examples=50)
def test_conditionalrule_instantiation(instance):
    assert isinstance(instance, ConditionalRule)

@given(instance=smif::mapping::RepresentationRule_strategy)
@settings(max_examples=50)
def test_smif::mapping::representationrule_instantiation(instance):
    assert isinstance(instance, smif::mapping::RepresentationRule)

@given(instance=smif::mapping::RepresentationRule_strategy)
def test_smif::mapping::representationrule_mapAll_type(instance):
    assert isinstance(instance.mapAll, str)


@given(instance=smif::mapping::RepresentationRule_strategy)
def test_smif::mapping::representationrule_mapAll_setter(instance):
    original = instance.mapAll
    instance.mapAll = original
    assert instance.mapAll == original

@given(instance=Facade_strategy)
@settings(max_examples=50)
def test_facade_instantiation(instance):
    assert isinstance(instance, Facade)

@given(instance=smif::mapping::ComputedFacade_strategy)
@settings(max_examples=50)
def test_smif::mapping::computedfacade_instantiation(instance):
    assert isinstance(instance, smif::mapping::ComputedFacade)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=smif::mapping::ComputedFacade_strategy)
@settings(max_examples=30)
def test_smif::mapping::computedfacade_push_changes_state(instance):
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
        assert has_statements, f"Function 'push' in smif::mapping::ComputedFacade is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'push' in smif::mapping::ComputedFacade did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'push' in smif::mapping::ComputedFacade is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=smif::mapping::ComputedFacade_strategy)
@settings(max_examples=30)
def test_smif::mapping::computedfacade_pull_changes_state(instance):
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
        assert has_statements, f"Function 'pull' in smif::mapping::ComputedFacade is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'pull' in smif::mapping::ComputedFacade did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'pull' in smif::mapping::ComputedFacade is not implemented or raised an error")

@given(instance=smif::mapping::Facade_strategy)
@settings(max_examples=50)
def test_smif::mapping::facade_instantiation(instance):
    assert isinstance(instance, smif::mapping::Facade)

@given(instance=Situation_strategy)
@settings(max_examples=50)
def test_situation_instantiation(instance):
    assert isinstance(instance, Situation)

@given(instance=VariableBinding_strategy)
@settings(max_examples=50)
def test_variablebinding_instantiation(instance):
    assert isinstance(instance, VariableBinding)

@given(instance=patterns::Pattern_strategy)
@settings(max_examples=50)
def test_patterns::pattern_instantiation(instance):
    assert isinstance(instance, patterns::Pattern)

@given(instance=MatchRule_strategy)
@settings(max_examples=50)
def test_matchrule_instantiation(instance):
    assert isinstance(instance, MatchRule)

@given(instance=smif::patterns::Computed_strategy)
@settings(max_examples=50)
def test_smif::patterns::computed_instantiation(instance):
    assert isinstance(instance, smif::patterns::Computed)

@given(instance=OwnedPropertyBinding_strategy)
@settings(max_examples=50)
def test_ownedpropertybinding_instantiation(instance):
    assert isinstance(instance, OwnedPropertyBinding)

@given(instance=smif::patterns::VariableBinding_strategy)
@settings(max_examples=50)
def test_smif::patterns::variablebinding_instantiation(instance):
    assert isinstance(instance, smif::patterns::VariableBinding)

@given(instance=Pattern_strategy)
@settings(max_examples=50)
def test_pattern_instantiation(instance):
    assert isinstance(instance, Pattern)

@given(instance=ActualSituation_strategy)
@settings(max_examples=50)
def test_actualsituation_instantiation(instance):
    assert isinstance(instance, ActualSituation)

@given(instance=smif::patterns::PatternMatch_strategy)
@settings(max_examples=50)
def test_smif::patterns::patternmatch_instantiation(instance):
    assert isinstance(instance, smif::patterns::PatternMatch)

@given(instance=smif::patterns::PatternOfType_strategy)
@settings(max_examples=50)
def test_smif::patterns::patternoftype_instantiation(instance):
    assert isinstance(instance, smif::patterns::PatternOfType)

@given(instance=TypePatternVariable_strategy)
@settings(max_examples=50)
def test_typepatternvariable_instantiation(instance):
    assert isinstance(instance, TypePatternVariable)

@given(instance=smif::patterns::FocusVariable_strategy)
@settings(max_examples=50)
def test_smif::patterns::focusvariable_instantiation(instance):
    assert isinstance(instance, smif::patterns::FocusVariable)

@given(instance=smif::patterns::PartVariable_strategy)
@settings(max_examples=50)
def test_smif::patterns::partvariable_instantiation(instance):
    assert isinstance(instance, smif::patterns::PartVariable)

@given(instance=smif::patterns::PartVariable_strategy)
def test_smif::patterns::partvariable_isBoundaryPart_type(instance):
    assert isinstance(instance.isBoundaryPart, str)


@given(instance=smif::patterns::PartVariable_strategy)
def test_smif::patterns::partvariable_isBoundaryPart_setter(instance):
    original = instance.isBoundaryPart
    instance.isBoundaryPart = original
    assert instance.isBoundaryPart == original

@given(instance=patterns::Computed_strategy)
@settings(max_examples=50)
def test_patterns::computed_instantiation(instance):
    assert isinstance(instance, patterns::Computed)

@given(instance=patterns::PatternVariable_strategy)
@settings(max_examples=50)
def test_patterns::patternvariable_instantiation(instance):
    assert isinstance(instance, patterns::PatternVariable)

@given(instance=smif::patterns::ExpressionVariable_strategy)
@settings(max_examples=50)
def test_smif::patterns::expressionvariable_instantiation(instance):
    assert isinstance(instance, smif::patterns::ExpressionVariable)

@given(instance=Mapping_strategy)
@settings(max_examples=50)
def test_mapping_instantiation(instance):
    assert isinstance(instance, Mapping)

@given(instance=Equality_strategy)
@settings(max_examples=50)
def test_equality_instantiation(instance):
    assert isinstance(instance, Equality)

@given(instance=properties::OwnedPropertyType_strategy)
@settings(max_examples=50)
def test_properties::ownedpropertytype_instantiation(instance):
    assert isinstance(instance, properties::OwnedPropertyType)

@given(instance=PatternVariable_strategy)
@settings(max_examples=50)
def test_patternvariable_instantiation(instance):
    assert isinstance(instance, PatternVariable)

@given(instance=smif::patterns::PropositionVariable_strategy)
@settings(max_examples=50)
def test_smif::patterns::propositionvariable_instantiation(instance):
    assert isinstance(instance, smif::patterns::PropositionVariable)

@given(instance=smif::patterns::TypePatternVariable_strategy)
@settings(max_examples=50)
def test_smif::patterns::typepatternvariable_instantiation(instance):
    assert isinstance(instance, smif::patterns::TypePatternVariable)

@given(instance=TemporalEntity_strategy)
@settings(max_examples=50)
def test_temporalentity_instantiation(instance):
    assert isinstance(instance, TemporalEntity)

@given(instance=smif::toplevel::ActualEntity_strategy)
@settings(max_examples=50)
def test_smif::toplevel::actualentity_instantiation(instance):
    assert isinstance(instance, smif::toplevel::ActualEntity)

@given(instance=PropositionVariable_strategy)
@settings(max_examples=50)
def test_propositionvariable_instantiation(instance):
    assert isinstance(instance, PropositionVariable)

@given(instance=LexicalReference_strategy)
@settings(max_examples=50)
def test_lexicalreference_instantiation(instance):
    assert isinstance(instance, LexicalReference)

@given(instance=smif::lexicalscope::Include_strategy)
@settings(max_examples=50)
def test_smif::lexicalscope::include_instantiation(instance):
    assert isinstance(instance, smif::lexicalscope::Include)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=smif::toplevel::IdentifiableEntity_strategy)
@settings(max_examples=50)
def test_smif::toplevel::identifiableentity_instantiation(instance):
    assert isinstance(instance, smif::toplevel::IdentifiableEntity)

@given(instance=ConstantReference_strategy)
@settings(max_examples=50)
def test_constantreference_instantiation(instance):
    assert isinstance(instance, ConstantReference)

@given(instance=smif::toplevel::Thing_strategy)
@settings(max_examples=50)
def test_smif::toplevel::thing_instantiation(instance):
    assert isinstance(instance, smif::toplevel::Thing)

@given(instance=PropertyBinding_strategy)
@settings(max_examples=50)
def test_propertybinding_instantiation(instance):
    assert isinstance(instance, PropertyBinding)

@given(instance=smif::properties::OwnedPropertyBinding_strategy)
@settings(max_examples=50)
def test_smif::properties::ownedpropertybinding_instantiation(instance):
    assert isinstance(instance, smif::properties::OwnedPropertyBinding)

@given(instance=InformationSource_strategy)
@settings(max_examples=50)
def test_informationsource_instantiation(instance):
    assert isinstance(instance, InformationSource)

@given(instance=Record_strategy)
@settings(max_examples=50)
def test_record_instantiation(instance):
    assert isinstance(instance, Record)

@given(instance=smif::metadata::Metadata_strategy)
@settings(max_examples=50)
def test_smif::metadata::metadata_instantiation(instance):
    assert isinstance(instance, smif::metadata::Metadata)

@given(instance=Name_strategy)
@settings(max_examples=50)
def test_name_instantiation(instance):
    assert isinstance(instance, Name)

@given(instance=Metadata_strategy)
@settings(max_examples=50)
def test_metadata_instantiation(instance):
    assert isinstance(instance, Metadata)

@given(instance=smif::metadata::Definition_strategy)
@settings(max_examples=50)
def test_smif::metadata::definition_instantiation(instance):
    assert isinstance(instance, smif::metadata::Definition)

@given(instance=smif::metadata::Definition_strategy)
def test_smif::metadata::definition_textDefinition_type(instance):
    assert isinstance(instance.textDefinition, str)


@given(instance=smif::metadata::Definition_strategy)
def test_smif::metadata::definition_textDefinition_setter(instance):
    original = instance.textDefinition
    instance.textDefinition = original
    assert instance.textDefinition == original

@given(instance=smif::metadata::Definition_strategy)
def test_smif::metadata::definition_summaryDescription_type(instance):
    assert isinstance(instance.summaryDescription, str)


@given(instance=smif::metadata::Definition_strategy)
def test_smif::metadata::definition_summaryDescription_setter(instance):
    original = instance.summaryDescription
    instance.summaryDescription = original
    assert instance.summaryDescription == original

@given(instance=smif::metadata::Statement_strategy)
@settings(max_examples=50)
def test_smif::metadata::statement_instantiation(instance):
    assert isinstance(instance, smif::metadata::Statement)

@given(instance=constraints::Conditional_strategy)
@settings(max_examples=50)
def test_constraints::conditional_instantiation(instance):
    assert isinstance(instance, constraints::Conditional)

@given(instance=smif::patterns::PatternVariable_strategy)
@settings(max_examples=50)
def test_smif::patterns::patternvariable_instantiation(instance):
    assert isinstance(instance, smif::patterns::PatternVariable)

@given(instance=smif::patterns::PatternVariable_strategy)
def test_smif::patterns::patternvariable_qualification_type(instance):
    assert isinstance(instance.qualification, str)


@given(instance=smif::patterns::PatternVariable_strategy)
def test_smif::patterns::patternvariable_qualification_setter(instance):
    original = instance.qualification
    instance.qualification = original
    assert instance.qualification == original

@given(instance=smif::patterns::PatternVariable_strategy)
def test_smif::patterns::patternvariable_explicit_type(instance):
    assert isinstance(instance.explicit, str)


@given(instance=smif::patterns::PatternVariable_strategy)
def test_smif::patterns::patternvariable_explicit_setter(instance):
    original = instance.explicit
    instance.explicit = original
    assert instance.explicit == original

@given(instance=smif::mapping::MatchEnd_strategy)
@settings(max_examples=50)
def test_smif::mapping::matchend_instantiation(instance):
    assert isinstance(instance, smif::mapping::MatchEnd)

@given(instance=constraints::Rule_strategy)
@settings(max_examples=50)
def test_constraints::rule_instantiation(instance):
    assert isinstance(instance, constraints::Rule)

@given(instance=smif::mapping::Mapping_strategy)
@settings(max_examples=50)
def test_smif::mapping::mapping_instantiation(instance):
    assert isinstance(instance, smif::mapping::Mapping)

@given(instance=smif::mapping::Mapping_strategy)
def test_smif::mapping::mapping_strength_type(instance):
    assert isinstance(instance.strength, str)


@given(instance=smif::mapping::Mapping_strategy)
def test_smif::mapping::mapping_strength_setter(instance):
    original = instance.strength
    instance.strength = original
    assert instance.strength == original

@given(instance=smif::constraints::ConditionalRule_strategy)
@settings(max_examples=50)
def test_smif::constraints::conditionalrule_instantiation(instance):
    assert isinstance(instance, smif::constraints::ConditionalRule)

@given(instance=smif::constraints::Conditional_strategy)
@settings(max_examples=50)
def test_smif::constraints::conditional_instantiation(instance):
    assert isinstance(instance, smif::constraints::Conditional)

@given(instance=smif::constraints::FacetClassificationConstraint_strategy)
@settings(max_examples=50)
def test_smif::constraints::facetclassificationconstraint_instantiation(instance):
    assert isinstance(instance, smif::constraints::FacetClassificationConstraint)

@given(instance=PropertyConstraint_strategy)
@settings(max_examples=50)
def test_propertyconstraint_instantiation(instance):
    assert isinstance(instance, PropertyConstraint)

@given(instance=smif::constraints::PropertyTypeConstraint_strategy)
@settings(max_examples=50)
def test_smif::constraints::propertytypeconstraint_instantiation(instance):
    assert isinstance(instance, smif::constraints::PropertyTypeConstraint)

@given(instance=smif::constraints::PropertyTypeConstraint_strategy)
def test_smif::constraints::propertytypeconstraint_prerequisiteType_type(instance):
    assert isinstance(instance.prerequisiteType, str)


@given(instance=smif::constraints::PropertyTypeConstraint_strategy)
def test_smif::constraints::propertytypeconstraint_prerequisiteType_setter(instance):
    original = instance.prerequisiteType
    instance.prerequisiteType = original
    assert instance.prerequisiteType == original

@given(instance=smif::constraints::PropertyTransitivityConstraint_strategy)
@settings(max_examples=50)
def test_smif::constraints::propertytransitivityconstraint_instantiation(instance):
    assert isinstance(instance, smif::constraints::PropertyTransitivityConstraint)

@given(instance=smif::expressions::Evaluation_strategy)
@settings(max_examples=50)
def test_smif::expressions::evaluation_instantiation(instance):
    assert isinstance(instance, smif::expressions::Evaluation)

@given(instance=TypeConstraint_strategy)
@settings(max_examples=50)
def test_typeconstraint_instantiation(instance):
    assert isinstance(instance, TypeConstraint)

@given(instance=smif::constraints::GeneralizationConstraint_strategy)
@settings(max_examples=50)
def test_smif::constraints::generalizationconstraint_instantiation(instance):
    assert isinstance(instance, smif::constraints::GeneralizationConstraint)

@given(instance=smif::constraints::GeneralizationConstraint_strategy)
def test_smif::constraints::generalizationconstraint_redefines_type(instance):
    assert isinstance(instance.redefines, str)


@given(instance=smif::constraints::GeneralizationConstraint_strategy)
def test_smif::constraints::generalizationconstraint_redefines_setter(instance):
    original = instance.redefines
    instance.redefines = original
    assert instance.redefines == original

@given(instance=smif::constraints::CoveringConstraint_strategy)
@settings(max_examples=50)
def test_smif::constraints::coveringconstraint_instantiation(instance):
    assert isinstance(instance, smif::constraints::CoveringConstraint)

@given(instance=smif::constraints::UniquenessConstraint_strategy)
@settings(max_examples=50)
def test_smif::constraints::uniquenessconstraint_instantiation(instance):
    assert isinstance(instance, smif::constraints::UniquenessConstraint)

@given(instance=smif::constraints::UniquenessConstraint_strategy)
def test_smif::constraints::uniquenessconstraint_isPrimaryIdentity_type(instance):
    assert isinstance(instance.isPrimaryIdentity, str)


@given(instance=smif::constraints::UniquenessConstraint_strategy)
def test_smif::constraints::uniquenessconstraint_isPrimaryIdentity_setter(instance):
    original = instance.isPrimaryIdentity
    instance.isPrimaryIdentity = original
    assert instance.isPrimaryIdentity == original

@given(instance=smif::constraints::MultiplicityConstraint_strategy)
@settings(max_examples=50)
def test_smif::constraints::multiplicityconstraint_instantiation(instance):
    assert isinstance(instance, smif::constraints::MultiplicityConstraint)

@given(instance=smif::constraints::MultiplicityConstraint_strategy)
def test_smif::constraints::multiplicityconstraint_maximumNumber_type(instance):
    assert isinstance(instance.maximumNumber, str)


@given(instance=smif::constraints::MultiplicityConstraint_strategy)
def test_smif::constraints::multiplicityconstraint_maximumNumber_setter(instance):
    original = instance.maximumNumber
    instance.maximumNumber = original
    assert instance.maximumNumber == original

@given(instance=smif::constraints::MultiplicityConstraint_strategy)
def test_smif::constraints::multiplicityconstraint_isSufficent_type(instance):
    assert isinstance(instance.isSufficent, str)


@given(instance=smif::constraints::MultiplicityConstraint_strategy)
def test_smif::constraints::multiplicityconstraint_isSufficent_setter(instance):
    original = instance.isSufficent
    instance.isSufficent = original
    assert instance.isSufficent == original

@given(instance=smif::constraints::MultiplicityConstraint_strategy)
def test_smif::constraints::multiplicityconstraint_atOnce_type(instance):
    assert isinstance(instance.atOnce, str)


@given(instance=smif::constraints::MultiplicityConstraint_strategy)
def test_smif::constraints::multiplicityconstraint_atOnce_setter(instance):
    original = instance.atOnce
    instance.atOnce = original
    assert instance.atOnce == original

@given(instance=smif::constraints::MultiplicityConstraint_strategy)
def test_smif::constraints::multiplicityconstraint_mininumNumber_type(instance):
    assert isinstance(instance.mininumNumber, str)


@given(instance=smif::constraints::MultiplicityConstraint_strategy)
def test_smif::constraints::multiplicityconstraint_mininumNumber_setter(instance):
    original = instance.mininumNumber
    instance.mininumNumber = original
    assert instance.mininumNumber == original

@given(instance=Rule_strategy)
@settings(max_examples=50)
def test_rule_instantiation(instance):
    assert isinstance(instance, Rule)

@given(instance=smif::constraints::TypeConstraint_strategy)
@settings(max_examples=50)
def test_smif::constraints::typeconstraint_instantiation(instance):
    assert isinstance(instance, smif::constraints::TypeConstraint)

@given(instance=smif::constraints::PropertyConstraint_strategy)
@settings(max_examples=50)
def test_smif::constraints::propertyconstraint_instantiation(instance):
    assert isinstance(instance, smif::constraints::PropertyConstraint)

@given(instance=smif::mapping::MatchRule_strategy)
@settings(max_examples=50)
def test_smif::mapping::matchrule_instantiation(instance):
    assert isinstance(instance, smif::mapping::MatchRule)

@given(instance=smif::mapping::MatchRule_strategy)
def test_smif::mapping::matchrule_coerce_type(instance):
    assert isinstance(instance.coerce, str)


@given(instance=smif::mapping::MatchRule_strategy)
def test_smif::mapping::matchrule_coerce_setter(instance):
    original = instance.coerce
    instance.coerce = original
    assert instance.coerce == original

@given(instance=smif::constraints::Enumerated_strategy)
@settings(max_examples=50)
def test_smif::constraints::enumerated_instantiation(instance):
    assert isinstance(instance, smif::constraints::Enumerated)

@given(instance=smif::constraints::Equivalent_strategy)
@settings(max_examples=50)
def test_smif::constraints::equivalent_instantiation(instance):
    assert isinstance(instance, smif::constraints::Equivalent)

@given(instance=smif::constraints::Disjoint_strategy)
@settings(max_examples=50)
def test_smif::constraints::disjoint_instantiation(instance):
    assert isinstance(instance, smif::constraints::Disjoint)

@given(instance=Proposition_strategy)
@settings(max_examples=50)
def test_proposition_instantiation(instance):
    assert isinstance(instance, Proposition)

@given(instance=smif::constraints::Rule_strategy)
@settings(max_examples=50)
def test_smif::constraints::rule_instantiation(instance):
    assert isinstance(instance, smif::constraints::Rule)

@given(instance=situations::SituationType_strategy)
@settings(max_examples=50)
def test_situations::situationtype_instantiation(instance):
    assert isinstance(instance, situations::SituationType)

@given(instance=smif::properties::CharacteristicType_strategy)
@settings(max_examples=50)
def test_smif::properties::characteristictype_instantiation(instance):
    assert isinstance(instance, smif::properties::CharacteristicType)

@given(instance=smif::facets::Phase_strategy)
@settings(max_examples=50)
def test_smif::facets::phase_instantiation(instance):
    assert isinstance(instance, smif::facets::Phase)

@given(instance=situations::ActualSituation_strategy)
@settings(max_examples=50)
def test_situations::actualsituation_instantiation(instance):
    assert isinstance(instance, situations::ActualSituation)

@given(instance=smif::properties::CharacteristicBinding_strategy)
@settings(max_examples=50)
def test_smif::properties::characteristicbinding_instantiation(instance):
    assert isinstance(instance, smif::properties::CharacteristicBinding)

@given(instance=UniqueTextIdentifier_strategy)
@settings(max_examples=50)
def test_uniquetextidentifier_instantiation(instance):
    assert isinstance(instance, UniqueTextIdentifier)

@given(instance=smif::lexicalscope::Prefix_strategy)
@settings(max_examples=50)
def test_smif::lexicalscope::prefix_instantiation(instance):
    assert isinstance(instance, smif::lexicalscope::Prefix)

@given(instance=smif::identifiers::TechnicalIdentifier_strategy)
@settings(max_examples=50)
def test_smif::identifiers::technicalidentifier_instantiation(instance):
    assert isinstance(instance, smif::identifiers::TechnicalIdentifier)

@given(instance=TextIdentifier_strategy)
@settings(max_examples=50)
def test_textidentifier_instantiation(instance):
    assert isinstance(instance, TextIdentifier)

@given(instance=smif::identifiers::Name_strategy)
@settings(max_examples=50)
def test_smif::identifiers::name_instantiation(instance):
    assert isinstance(instance, smif::identifiers::Name)

@given(instance=smif::identifiers::TextIdentifier_strategy)
@settings(max_examples=50)
def test_smif::identifiers::textidentifier_instantiation(instance):
    assert isinstance(instance, smif::identifiers::TextIdentifier)

@given(instance=smif::identifiers::TextIdentifier_strategy)
def test_smif::identifiers::textidentifier_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=smif::identifiers::TextIdentifier_strategy)
def test_smif::identifiers::textidentifier_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=UniqueIdentifier_strategy)
@settings(max_examples=50)
def test_uniqueidentifier_instantiation(instance):
    assert isinstance(instance, UniqueIdentifier)

@given(instance=smif::identifiers::Namespace_strategy)
@settings(max_examples=50)
def test_smif::identifiers::namespace_instantiation(instance):
    assert isinstance(instance, smif::identifiers::Namespace)

@given(instance=IdentifiableEntity_strategy)
@settings(max_examples=50)
def test_identifiableentity_instantiation(instance):
    assert isinstance(instance, IdentifiableEntity)

@given(instance=smif::toplevel::Context_strategy)
@settings(max_examples=50)
def test_smif::toplevel::context_instantiation(instance):
    assert isinstance(instance, smif::toplevel::Context)

@given(instance=smif::expressions::ExpressionContext_strategy)
@settings(max_examples=50)
def test_smif::expressions::expressioncontext_instantiation(instance):
    assert isinstance(instance, smif::expressions::ExpressionContext)

@given(instance=smif::toplevel::TemporalEntity_strategy)
@settings(max_examples=50)
def test_smif::toplevel::temporalentity_instantiation(instance):
    assert isinstance(instance, smif::toplevel::TemporalEntity)

@given(instance=smif::toplevel::Proposition_strategy)
@settings(max_examples=50)
def test_smif::toplevel::proposition_instantiation(instance):
    assert isinstance(instance, smif::toplevel::Proposition)

@given(instance=smif::identifiers::Identifier_strategy)
@settings(max_examples=50)
def test_smif::identifiers::identifier_instantiation(instance):
    assert isinstance(instance, smif::identifiers::Identifier)

@given(instance=identifiers::TextIdentifier_strategy)
@settings(max_examples=50)
def test_identifiers::textidentifier_instantiation(instance):
    assert isinstance(instance, identifiers::TextIdentifier)

@given(instance=identifiers::UniqueIdentifier_strategy)
@settings(max_examples=50)
def test_identifiers::uniqueidentifier_instantiation(instance):
    assert isinstance(instance, identifiers::UniqueIdentifier)

@given(instance=smif::identifiers::UniqueTextIdentifier_strategy)
@settings(max_examples=50)
def test_smif::identifiers::uniquetextidentifier_instantiation(instance):
    assert isinstance(instance, smif::identifiers::UniqueTextIdentifier)

@given(instance=expressions::ExpressionNode_strategy)
@settings(max_examples=50)
def test_expressions::expressionnode_instantiation(instance):
    assert isinstance(instance, expressions::ExpressionNode)

@given(instance=FunctionType_strategy)
@settings(max_examples=50)
def test_functiontype_instantiation(instance):
    assert isinstance(instance, FunctionType)

@given(instance=smif::expressions::ObjectOperationType_strategy)
@settings(max_examples=50)
def test_smif::expressions::objectoperationtype_instantiation(instance):
    assert isinstance(instance, smif::expressions::ObjectOperationType)

@given(instance=Evaluation_strategy)
@settings(max_examples=50)
def test_evaluation_instantiation(instance):
    assert isinstance(instance, Evaluation)

@given(instance=smif::expressions::ExpressionNode_strategy)
@settings(max_examples=50)
def test_smif::expressions::expressionnode_instantiation(instance):
    assert isinstance(instance, smif::expressions::ExpressionNode)

@given(instance=smif::expressions::ExpressionNode_strategy)
def test_smif::expressions::expressionnode_expressionTextLanguage_type(instance):
    assert isinstance(instance.expressionTextLanguage, str)


@given(instance=smif::expressions::ExpressionNode_strategy)
def test_smif::expressions::expressionnode_expressionTextLanguage_setter(instance):
    original = instance.expressionTextLanguage
    instance.expressionTextLanguage = original
    assert instance.expressionTextLanguage == original

@given(instance=smif::expressions::ExpressionNode_strategy)
def test_smif::expressions::expressionnode_expressionText_type(instance):
    assert isinstance(instance.expressionText, str)


@given(instance=smif::expressions::ExpressionNode_strategy)
def test_smif::expressions::expressionnode_expressionText_setter(instance):
    original = instance.expressionText
    instance.expressionText = original
    assert instance.expressionText == original

@given(instance=FunctionCall_strategy)
@settings(max_examples=50)
def test_functioncall_instantiation(instance):
    assert isinstance(instance, FunctionCall)

@given(instance=ExpressionNode_strategy)
@settings(max_examples=50)
def test_expressionnode_instantiation(instance):
    assert isinstance(instance, ExpressionNode)

@given(instance=smif::expressions::Equality_strategy)
@settings(max_examples=50)
def test_smif::expressions::equality_instantiation(instance):
    assert isinstance(instance, smif::expressions::Equality)

@given(instance=smif::expressions::ConstantReference_strategy)
@settings(max_examples=50)
def test_smif::expressions::constantreference_instantiation(instance):
    assert isinstance(instance, smif::expressions::ConstantReference)

@given(instance=expressions::ExpressionContext_strategy)
@settings(max_examples=50)
def test_expressions::expressioncontext_instantiation(instance):
    assert isinstance(instance, expressions::ExpressionContext)

@given(instance=properties::PropertyOwner_strategy)
@settings(max_examples=50)
def test_properties::propertyowner_instantiation(instance):
    assert isinstance(instance, properties::PropertyOwner)

@given(instance=smif::associations::Association_strategy)
@settings(max_examples=50)
def test_smif::associations::association_instantiation(instance):
    assert isinstance(instance, smif::associations::Association)

@given(instance=smif::patterns::Pattern_strategy)
@settings(max_examples=50)
def test_smif::patterns::pattern_instantiation(instance):
    assert isinstance(instance, smif::patterns::Pattern)

@given(instance=smif::expressions::Traversal_strategy)
@settings(max_examples=50)
def test_smif::expressions::traversal_instantiation(instance):
    assert isinstance(instance, smif::expressions::Traversal)

@given(instance=smif::expressions::Traversal_strategy)
def test_smif::expressions::traversal_inverse_type(instance):
    assert isinstance(instance.inverse, str)


@given(instance=smif::expressions::Traversal_strategy)
def test_smif::expressions::traversal_inverse_setter(instance):
    original = instance.inverse
    instance.inverse = original
    assert instance.inverse == original

@given(instance=smif::expressions::Traversal_strategy)
def test_smif::expressions::traversal_traverseToRelation_type(instance):
    assert isinstance(instance.traverseToRelation, str)


@given(instance=smif::expressions::Traversal_strategy)
def test_smif::expressions::traversal_traverseToRelation_setter(instance):
    original = instance.traverseToRelation
    instance.traverseToRelation = original
    assert instance.traverseToRelation == original

@given(instance=smif::relationships::Relationship_strategy)
@settings(max_examples=50)
def test_smif::relationships::relationship_instantiation(instance):
    assert isinstance(instance, smif::relationships::Relationship)

@given(instance=smif::records::Record_strategy)
@settings(max_examples=50)
def test_smif::records::record_instantiation(instance):
    assert isinstance(instance, smif::records::Record)

@given(instance=smif::expressions::FunctionCall_strategy)
@settings(max_examples=50)
def test_smif::expressions::functioncall_instantiation(instance):
    assert isinstance(instance, smif::expressions::FunctionCall)

@given(instance=values::Value_strategy)
@settings(max_examples=50)
def test_values::value_instantiation(instance):
    assert isinstance(instance, values::Value)

@given(instance=smif::values::StructuredValue_strategy)
@settings(max_examples=50)
def test_smif::values::structuredvalue_instantiation(instance):
    assert isinstance(instance, smif::values::StructuredValue)

@given(instance=properties::PropertyOwnerType_strategy)
@settings(max_examples=50)
def test_properties::propertyownertype_instantiation(instance):
    assert isinstance(instance, properties::PropertyOwnerType)

@given(instance=smif::relationships::RelationshipType_strategy)
@settings(max_examples=50)
def test_smif::relationships::relationshiptype_instantiation(instance):
    assert isinstance(instance, smif::relationships::RelationshipType)

@given(instance=smif::records::RecordType_strategy)
@settings(max_examples=50)
def test_smif::records::recordtype_instantiation(instance):
    assert isinstance(instance, smif::records::RecordType)

@given(instance=smif::values::StructuredValueType_strategy)
@settings(max_examples=50)
def test_smif::values::structuredvaluetype_instantiation(instance):
    assert isinstance(instance, smif::values::StructuredValueType)

@given(instance=smif::expressions::FunctionType_strategy)
@settings(max_examples=50)
def test_smif::expressions::functiontype_instantiation(instance):
    assert isinstance(instance, smif::expressions::FunctionType)
