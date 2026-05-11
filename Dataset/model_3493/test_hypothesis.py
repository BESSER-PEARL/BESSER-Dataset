import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Abstract::ATT::ID,
    vM::PairFeatureReal,
    vM::PairFeatureInteger,
    TableBasedValuationByAttribute,
    vM::TableBasedValuationByAttributeForReal,
    vM::TableBasedValuationByAttributeForInteger,
    vM::PairAttributeValue,
    vM::TableBasedValuationByFeatureAndClone,
    vM::TableBasedValuationByAttribute,
    vM::TableBasedValuationByFeature,
    BasicAttrValuation,
    vM::BooleanAttrValuation,
    vM::StringAttrValuation,
    vM::IntegerAttrValuation,
    vM::RealAttrValuation,
    ExtendedValuation,
    vM::AdvancedAttrValuation,
    vM::ExtendedValuation,
    vM::BooleanValuation,
    vM::Configuration,
    vM::ObjectiveExpression,
    vM::Objective,
    vM::NumericExpression::List,
    vM::BooleanExpression::List,
    vM::AttHead,
    Expression,
    vM::StringExpression,
    vM::BooleanExpression,
    vM::BrackedExpression,
    vM::PrimitiveExpression,
    vM::NumericExpression,
    vM::SpecialExpression,
    ComplexExpression,
    vM::LeftImplication,
    vM::Inequality,
    vM::Plus,
    vM::RightImplication,
    vM::Or,
    vM::Less,
    vM::Excludes,
    vM::Equality,
    vM::Lessequal,
    vM::BiImplication,
    vM::Greater,
    vM::Minus,
    vM::Greaterequal,
    vM::Requires,
    vM::Multiplication,
    vM::Division,
    vM::If,
    vM::And,
    vM::Expression,
    vM::ComplexExpression,
    vM::Constraint,
    vM::Abstract::ATT::ID,
    vM::AttributeDescription,
    vM::FeatureDescription,
    vM::IntegerAttrDefComplement,
    vM::Enum::Real::ATT::ID,
    vM::Enum::Integer::ATT::ID,
    vM::Enum::String::ATT::ID,
    EnumAttrDef,
    vM::EnumIntegerDef,
    vM::EnumRealDef,
    vM::EnumStringDef,
    vM::RealDeltaDef,
    vM::RealAttrDefComplement,
    RealAttrDef,
    vM::RealAttrDefUnbounded,
    vM::RealAttrDefBounded,
    vM::RealDefaultDef,
    vM::Real::ATT::ID,
    vM::IntegerDeltaDef,
    vM::FeatureDefinition,
    IntegerAttrDef,
    vM::IntegerAttrDefUnbounded,
    vM::IntegerAttrDefBounded,
    vM::IntegerDefaultDef,
    vM::Integer::ATT::ID,
    vM::StringDefaultDef,
    vM::String::ATT::ID,
    vM::BoolDefaultDef,
    vM::Boolean::ATT::ID,
    BasicAttrDef,
    vM::StringAttrDef,
    vM::RealAttrDef,
    vM::IntegerAttrDef,
    vM::BooleanAttrDef,
    vM::EnumAttrDef,
    vM::BasicAttrDef,
    vM::BasicAttrValuation,
    vM::AttrDef,
    FeaturesGroup,
    vM::CardinalityBased,
    vM::Orgroup,
    vM::Xorgroup,
    FeatureDefinition,
    vM::FeaturesGroup,
    vM::Feature,
    vM::FeatureHierarchy,
    vM::Email,
    vM::Version,
    VmBlock,
    vM::Attributes,
    vM::Objectives,
    vM::ImportDeclaration,
    vM::Configurations,
    vM::Relationships,
    vM::Descriptions,
    vM::MetaDataDeclaration,
    vM::Constraints,
    vM::PackageDeclaration,
    vM::VmBlock,
    vM::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_abstract::att::id_is_not_abstract():
    assert not inspect.isabstract(Abstract::ATT::ID)


def test_abstract::att::id_constructor_exists():
    assert callable(Abstract::ATT::ID.__init__)


def test_abstract::att::id_constructor_args():
    sig = inspect.signature(Abstract::ATT::ID.__init__)
    params = list(sig.parameters.keys())



def test_vm::pairfeaturereal_is_not_abstract():
    assert not inspect.isabstract(vM::PairFeatureReal)


def test_vm::pairfeaturereal_constructor_exists():
    assert callable(vM::PairFeatureReal.__init__)


def test_vm::pairfeaturereal_constructor_args():
    sig = inspect.signature(vM::PairFeatureReal.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_vm::pairfeaturereal_has_value():
    assert hasattr(vM::PairFeatureReal, "value")
    descriptor = None
    for klass in vM::PairFeatureReal.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_vm::pairfeatureinteger_is_not_abstract():
    assert not inspect.isabstract(vM::PairFeatureInteger)


def test_vm::pairfeatureinteger_constructor_exists():
    assert callable(vM::PairFeatureInteger.__init__)


def test_vm::pairfeatureinteger_constructor_args():
    sig = inspect.signature(vM::PairFeatureInteger.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_vm::pairfeatureinteger_has_value():
    assert hasattr(vM::PairFeatureInteger, "value")
    descriptor = None
    for klass in vM::PairFeatureInteger.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_tablebasedvaluationbyattribute_is_not_abstract():
    assert not inspect.isabstract(TableBasedValuationByAttribute)


def test_tablebasedvaluationbyattribute_constructor_exists():
    assert callable(TableBasedValuationByAttribute.__init__)


def test_tablebasedvaluationbyattribute_constructor_args():
    sig = inspect.signature(TableBasedValuationByAttribute.__init__)
    params = list(sig.parameters.keys())



def test_vm::tablebasedvaluationbyattributeforreal_is_not_abstract():
    assert not inspect.isabstract(vM::TableBasedValuationByAttributeForReal)


def test_vm::tablebasedvaluationbyattributeforreal_constructor_exists():
    assert callable(vM::TableBasedValuationByAttributeForReal.__init__)


def test_vm::tablebasedvaluationbyattributeforreal_constructor_args():
    sig = inspect.signature(vM::TableBasedValuationByAttributeForReal.__init__)
    params = list(sig.parameters.keys())



def test_vm::tablebasedvaluationbyattributeforinteger_is_not_abstract():
    assert not inspect.isabstract(vM::TableBasedValuationByAttributeForInteger)


def test_vm::tablebasedvaluationbyattributeforinteger_constructor_exists():
    assert callable(vM::TableBasedValuationByAttributeForInteger.__init__)


def test_vm::tablebasedvaluationbyattributeforinteger_constructor_args():
    sig = inspect.signature(vM::TableBasedValuationByAttributeForInteger.__init__)
    params = list(sig.parameters.keys())



def test_vm::pairattributevalue_is_not_abstract():
    assert not inspect.isabstract(vM::PairAttributeValue)


def test_vm::pairattributevalue_constructor_exists():
    assert callable(vM::PairAttributeValue.__init__)


def test_vm::pairattributevalue_constructor_args():
    sig = inspect.signature(vM::PairAttributeValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_vm::pairattributevalue_has_value():
    assert hasattr(vM::PairAttributeValue, "value")
    descriptor = None
    for klass in vM::PairAttributeValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_vm::tablebasedvaluationbyfeatureandclone_is_not_abstract():
    assert not inspect.isabstract(vM::TableBasedValuationByFeatureAndClone)


def test_vm::tablebasedvaluationbyfeatureandclone_constructor_exists():
    assert callable(vM::TableBasedValuationByFeatureAndClone.__init__)


def test_vm::tablebasedvaluationbyfeatureandclone_constructor_args():
    sig = inspect.signature(vM::TableBasedValuationByFeatureAndClone.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_vm::tablebasedvaluationbyfeatureandclone_has_name():
    assert hasattr(vM::TableBasedValuationByFeatureAndClone, "name")
    descriptor = None
    for klass in vM::TableBasedValuationByFeatureAndClone.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_vm::tablebasedvaluationbyattribute_is_not_abstract():
    assert not inspect.isabstract(vM::TableBasedValuationByAttribute)


def test_vm::tablebasedvaluationbyattribute_constructor_exists():
    assert callable(vM::TableBasedValuationByAttribute.__init__)


def test_vm::tablebasedvaluationbyattribute_constructor_args():
    sig = inspect.signature(vM::TableBasedValuationByAttribute.__init__)
    params = list(sig.parameters.keys())



def test_vm::tablebasedvaluationbyfeature_is_not_abstract():
    assert not inspect.isabstract(vM::TableBasedValuationByFeature)


def test_vm::tablebasedvaluationbyfeature_constructor_exists():
    assert callable(vM::TableBasedValuationByFeature.__init__)


def test_vm::tablebasedvaluationbyfeature_constructor_args():
    sig = inspect.signature(vM::TableBasedValuationByFeature.__init__)
    params = list(sig.parameters.keys())



def test_basicattrvaluation_is_not_abstract():
    assert not inspect.isabstract(BasicAttrValuation)


def test_basicattrvaluation_constructor_exists():
    assert callable(BasicAttrValuation.__init__)


def test_basicattrvaluation_constructor_args():
    sig = inspect.signature(BasicAttrValuation.__init__)
    params = list(sig.parameters.keys())



def test_vm::booleanattrvaluation_is_not_abstract():
    assert not inspect.isabstract(vM::BooleanAttrValuation)


def test_vm::booleanattrvaluation_constructor_exists():
    assert callable(vM::BooleanAttrValuation.__init__)


def test_vm::booleanattrvaluation_constructor_args():
    sig = inspect.signature(vM::BooleanAttrValuation.__init__)
    params = list(sig.parameters.keys())



def test_vm::stringattrvaluation_is_not_abstract():
    assert not inspect.isabstract(vM::StringAttrValuation)


def test_vm::stringattrvaluation_constructor_exists():
    assert callable(vM::StringAttrValuation.__init__)


def test_vm::stringattrvaluation_constructor_args():
    sig = inspect.signature(vM::StringAttrValuation.__init__)
    params = list(sig.parameters.keys())



def test_vm::integerattrvaluation_is_not_abstract():
    assert not inspect.isabstract(vM::IntegerAttrValuation)


def test_vm::integerattrvaluation_constructor_exists():
    assert callable(vM::IntegerAttrValuation.__init__)


def test_vm::integerattrvaluation_constructor_args():
    sig = inspect.signature(vM::IntegerAttrValuation.__init__)
    params = list(sig.parameters.keys())



def test_vm::realattrvaluation_is_not_abstract():
    assert not inspect.isabstract(vM::RealAttrValuation)


def test_vm::realattrvaluation_constructor_exists():
    assert callable(vM::RealAttrValuation.__init__)


def test_vm::realattrvaluation_constructor_args():
    sig = inspect.signature(vM::RealAttrValuation.__init__)
    params = list(sig.parameters.keys())



def test_extendedvaluation_is_not_abstract():
    assert not inspect.isabstract(ExtendedValuation)


def test_extendedvaluation_constructor_exists():
    assert callable(ExtendedValuation.__init__)


def test_extendedvaluation_constructor_args():
    sig = inspect.signature(ExtendedValuation.__init__)
    params = list(sig.parameters.keys())



def test_vm::advancedattrvaluation_is_not_abstract():
    assert not inspect.isabstract(vM::AdvancedAttrValuation)


def test_vm::advancedattrvaluation_constructor_exists():
    assert callable(vM::AdvancedAttrValuation.__init__)


def test_vm::advancedattrvaluation_constructor_args():
    sig = inspect.signature(vM::AdvancedAttrValuation.__init__)
    params = list(sig.parameters.keys())



def test_vm::extendedvaluation_is_not_abstract():
    assert not inspect.isabstract(vM::ExtendedValuation)


def test_vm::extendedvaluation_constructor_exists():
    assert callable(vM::ExtendedValuation.__init__)


def test_vm::extendedvaluation_constructor_args():
    sig = inspect.signature(vM::ExtendedValuation.__init__)
    params = list(sig.parameters.keys())



def test_vm::booleanvaluation_is_not_abstract():
    assert not inspect.isabstract(vM::BooleanValuation)


def test_vm::booleanvaluation_constructor_exists():
    assert callable(vM::BooleanValuation.__init__)


def test_vm::booleanvaluation_constructor_args():
    sig = inspect.signature(vM::BooleanValuation.__init__)
    params = list(sig.parameters.keys())
    assert "notSelected" in params, "Missing parameter 'notSelected'"

def test_vm::booleanvaluation_has_notSelected():
    assert hasattr(vM::BooleanValuation, "notSelected")
    descriptor = None
    for klass in vM::BooleanValuation.__mro__:
        if "notSelected" in klass.__dict__:
            descriptor = klass.__dict__["notSelected"]
            break
    assert isinstance(descriptor, property)



def test_vm::configuration_is_not_abstract():
    assert not inspect.isabstract(vM::Configuration)


def test_vm::configuration_constructor_exists():
    assert callable(vM::Configuration.__init__)


def test_vm::configuration_constructor_args():
    sig = inspect.signature(vM::Configuration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_vm::configuration_has_name():
    assert hasattr(vM::Configuration, "name")
    descriptor = None
    for klass in vM::Configuration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_vm::objectiveexpression_is_not_abstract():
    assert not inspect.isabstract(vM::ObjectiveExpression)


def test_vm::objectiveexpression_constructor_exists():
    assert callable(vM::ObjectiveExpression.__init__)


def test_vm::objectiveexpression_constructor_args():
    sig = inspect.signature(vM::ObjectiveExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_vm::objectiveexpression_has_op():
    assert hasattr(vM::ObjectiveExpression, "op")
    descriptor = None
    for klass in vM::ObjectiveExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_vm::objective_is_not_abstract():
    assert not inspect.isabstract(vM::Objective)


def test_vm::objective_constructor_exists():
    assert callable(vM::Objective.__init__)


def test_vm::objective_constructor_args():
    sig = inspect.signature(vM::Objective.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "op" in params, "Missing parameter 'op'"

def test_vm::objective_has_name():
    assert hasattr(vM::Objective, "name")
    descriptor = None
    for klass in vM::Objective.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_vm::objective_has_op():
    assert hasattr(vM::Objective, "op")
    descriptor = None
    for klass in vM::Objective.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_vm::numericexpression::list_is_not_abstract():
    assert not inspect.isabstract(vM::NumericExpression::List)


def test_vm::numericexpression::list_constructor_exists():
    assert callable(vM::NumericExpression::List.__init__)


def test_vm::numericexpression::list_constructor_args():
    sig = inspect.signature(vM::NumericExpression::List.__init__)
    params = list(sig.parameters.keys())



def test_vm::booleanexpression::list_is_not_abstract():
    assert not inspect.isabstract(vM::BooleanExpression::List)


def test_vm::booleanexpression::list_constructor_exists():
    assert callable(vM::BooleanExpression::List.__init__)


def test_vm::booleanexpression::list_constructor_args():
    sig = inspect.signature(vM::BooleanExpression::List.__init__)
    params = list(sig.parameters.keys())



def test_vm::atthead_is_not_abstract():
    assert not inspect.isabstract(vM::AttHead)


def test_vm::atthead_constructor_exists():
    assert callable(vM::AttHead.__init__)


def test_vm::atthead_constructor_args():
    sig = inspect.signature(vM::AttHead.__init__)
    params = list(sig.parameters.keys())
    assert "forAllFeatures" in params, "Missing parameter 'forAllFeatures'"

def test_vm::atthead_has_forAllFeatures():
    assert hasattr(vM::AttHead, "forAllFeatures")
    descriptor = None
    for klass in vM::AttHead.__mro__:
        if "forAllFeatures" in klass.__dict__:
            descriptor = klass.__dict__["forAllFeatures"]
            break
    assert isinstance(descriptor, property)



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_vm::stringexpression_is_not_abstract():
    assert not inspect.isabstract(vM::StringExpression)


def test_vm::stringexpression_constructor_exists():
    assert callable(vM::StringExpression.__init__)


def test_vm::stringexpression_constructor_args():
    sig = inspect.signature(vM::StringExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_vm::stringexpression_has_value():
    assert hasattr(vM::StringExpression, "value")
    descriptor = None
    for klass in vM::StringExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_vm::booleanexpression_is_not_abstract():
    assert not inspect.isabstract(vM::BooleanExpression)


def test_vm::booleanexpression_constructor_exists():
    assert callable(vM::BooleanExpression.__init__)


def test_vm::booleanexpression_constructor_args():
    sig = inspect.signature(vM::BooleanExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "op" in params, "Missing parameter 'op'"

def test_vm::booleanexpression_has_value():
    assert hasattr(vM::BooleanExpression, "value")
    descriptor = None
    for klass in vM::BooleanExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_vm::booleanexpression_has_op():
    assert hasattr(vM::BooleanExpression, "op")
    descriptor = None
    for klass in vM::BooleanExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_vm::brackedexpression_is_not_abstract():
    assert not inspect.isabstract(vM::BrackedExpression)


def test_vm::brackedexpression_constructor_exists():
    assert callable(vM::BrackedExpression.__init__)


def test_vm::brackedexpression_constructor_args():
    sig = inspect.signature(vM::BrackedExpression.__init__)
    params = list(sig.parameters.keys())



def test_vm::primitiveexpression_is_not_abstract():
    assert not inspect.isabstract(vM::PrimitiveExpression)


def test_vm::primitiveexpression_constructor_exists():
    assert callable(vM::PrimitiveExpression.__init__)


def test_vm::primitiveexpression_constructor_args():
    sig = inspect.signature(vM::PrimitiveExpression.__init__)
    params = list(sig.parameters.keys())



def test_vm::numericexpression_is_not_abstract():
    assert not inspect.isabstract(vM::NumericExpression)


def test_vm::numericexpression_constructor_exists():
    assert callable(vM::NumericExpression.__init__)


def test_vm::numericexpression_constructor_args():
    sig = inspect.signature(vM::NumericExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "op" in params, "Missing parameter 'op'"

def test_vm::numericexpression_has_value():
    assert hasattr(vM::NumericExpression, "value")
    descriptor = None
    for klass in vM::NumericExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_vm::numericexpression_has_op():
    assert hasattr(vM::NumericExpression, "op")
    descriptor = None
    for klass in vM::NumericExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_vm::specialexpression_is_not_abstract():
    assert not inspect.isabstract(vM::SpecialExpression)


def test_vm::specialexpression_constructor_exists():
    assert callable(vM::SpecialExpression.__init__)


def test_vm::specialexpression_constructor_args():
    sig = inspect.signature(vM::SpecialExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_vm::specialexpression_has_op():
    assert hasattr(vM::SpecialExpression, "op")
    descriptor = None
    for klass in vM::SpecialExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_complexexpression_is_not_abstract():
    assert not inspect.isabstract(ComplexExpression)


def test_complexexpression_constructor_exists():
    assert callable(ComplexExpression.__init__)


def test_complexexpression_constructor_args():
    sig = inspect.signature(ComplexExpression.__init__)
    params = list(sig.parameters.keys())



def test_vm::leftimplication_is_not_abstract():
    assert not inspect.isabstract(vM::LeftImplication)


def test_vm::leftimplication_constructor_exists():
    assert callable(vM::LeftImplication.__init__)


def test_vm::leftimplication_constructor_args():
    sig = inspect.signature(vM::LeftImplication.__init__)
    params = list(sig.parameters.keys())



def test_vm::inequality_is_not_abstract():
    assert not inspect.isabstract(vM::Inequality)


def test_vm::inequality_constructor_exists():
    assert callable(vM::Inequality.__init__)


def test_vm::inequality_constructor_args():
    sig = inspect.signature(vM::Inequality.__init__)
    params = list(sig.parameters.keys())



def test_vm::plus_is_not_abstract():
    assert not inspect.isabstract(vM::Plus)


def test_vm::plus_constructor_exists():
    assert callable(vM::Plus.__init__)


def test_vm::plus_constructor_args():
    sig = inspect.signature(vM::Plus.__init__)
    params = list(sig.parameters.keys())



def test_vm::rightimplication_is_not_abstract():
    assert not inspect.isabstract(vM::RightImplication)


def test_vm::rightimplication_constructor_exists():
    assert callable(vM::RightImplication.__init__)


def test_vm::rightimplication_constructor_args():
    sig = inspect.signature(vM::RightImplication.__init__)
    params = list(sig.parameters.keys())



def test_vm::or_is_not_abstract():
    assert not inspect.isabstract(vM::Or)


def test_vm::or_constructor_exists():
    assert callable(vM::Or.__init__)


def test_vm::or_constructor_args():
    sig = inspect.signature(vM::Or.__init__)
    params = list(sig.parameters.keys())



def test_vm::less_is_not_abstract():
    assert not inspect.isabstract(vM::Less)


def test_vm::less_constructor_exists():
    assert callable(vM::Less.__init__)


def test_vm::less_constructor_args():
    sig = inspect.signature(vM::Less.__init__)
    params = list(sig.parameters.keys())



def test_vm::excludes_is_not_abstract():
    assert not inspect.isabstract(vM::Excludes)


def test_vm::excludes_constructor_exists():
    assert callable(vM::Excludes.__init__)


def test_vm::excludes_constructor_args():
    sig = inspect.signature(vM::Excludes.__init__)
    params = list(sig.parameters.keys())



def test_vm::equality_is_not_abstract():
    assert not inspect.isabstract(vM::Equality)


def test_vm::equality_constructor_exists():
    assert callable(vM::Equality.__init__)


def test_vm::equality_constructor_args():
    sig = inspect.signature(vM::Equality.__init__)
    params = list(sig.parameters.keys())



def test_vm::lessequal_is_not_abstract():
    assert not inspect.isabstract(vM::Lessequal)


def test_vm::lessequal_constructor_exists():
    assert callable(vM::Lessequal.__init__)


def test_vm::lessequal_constructor_args():
    sig = inspect.signature(vM::Lessequal.__init__)
    params = list(sig.parameters.keys())



def test_vm::biimplication_is_not_abstract():
    assert not inspect.isabstract(vM::BiImplication)


def test_vm::biimplication_constructor_exists():
    assert callable(vM::BiImplication.__init__)


def test_vm::biimplication_constructor_args():
    sig = inspect.signature(vM::BiImplication.__init__)
    params = list(sig.parameters.keys())



def test_vm::greater_is_not_abstract():
    assert not inspect.isabstract(vM::Greater)


def test_vm::greater_constructor_exists():
    assert callable(vM::Greater.__init__)


def test_vm::greater_constructor_args():
    sig = inspect.signature(vM::Greater.__init__)
    params = list(sig.parameters.keys())



def test_vm::minus_is_not_abstract():
    assert not inspect.isabstract(vM::Minus)


def test_vm::minus_constructor_exists():
    assert callable(vM::Minus.__init__)


def test_vm::minus_constructor_args():
    sig = inspect.signature(vM::Minus.__init__)
    params = list(sig.parameters.keys())



def test_vm::greaterequal_is_not_abstract():
    assert not inspect.isabstract(vM::Greaterequal)


def test_vm::greaterequal_constructor_exists():
    assert callable(vM::Greaterequal.__init__)


def test_vm::greaterequal_constructor_args():
    sig = inspect.signature(vM::Greaterequal.__init__)
    params = list(sig.parameters.keys())



def test_vm::requires_is_not_abstract():
    assert not inspect.isabstract(vM::Requires)


def test_vm::requires_constructor_exists():
    assert callable(vM::Requires.__init__)


def test_vm::requires_constructor_args():
    sig = inspect.signature(vM::Requires.__init__)
    params = list(sig.parameters.keys())



def test_vm::multiplication_is_not_abstract():
    assert not inspect.isabstract(vM::Multiplication)


def test_vm::multiplication_constructor_exists():
    assert callable(vM::Multiplication.__init__)


def test_vm::multiplication_constructor_args():
    sig = inspect.signature(vM::Multiplication.__init__)
    params = list(sig.parameters.keys())



def test_vm::division_is_not_abstract():
    assert not inspect.isabstract(vM::Division)


def test_vm::division_constructor_exists():
    assert callable(vM::Division.__init__)


def test_vm::division_constructor_args():
    sig = inspect.signature(vM::Division.__init__)
    params = list(sig.parameters.keys())



def test_vm::if_is_not_abstract():
    assert not inspect.isabstract(vM::If)


def test_vm::if_constructor_exists():
    assert callable(vM::If.__init__)


def test_vm::if_constructor_args():
    sig = inspect.signature(vM::If.__init__)
    params = list(sig.parameters.keys())



def test_vm::and_is_not_abstract():
    assert not inspect.isabstract(vM::And)


def test_vm::and_constructor_exists():
    assert callable(vM::And.__init__)


def test_vm::and_constructor_args():
    sig = inspect.signature(vM::And.__init__)
    params = list(sig.parameters.keys())



def test_vm::expression_is_not_abstract():
    assert not inspect.isabstract(vM::Expression)


def test_vm::expression_constructor_exists():
    assert callable(vM::Expression.__init__)


def test_vm::expression_constructor_args():
    sig = inspect.signature(vM::Expression.__init__)
    params = list(sig.parameters.keys())



def test_vm::complexexpression_is_not_abstract():
    assert not inspect.isabstract(vM::ComplexExpression)


def test_vm::complexexpression_constructor_exists():
    assert callable(vM::ComplexExpression.__init__)


def test_vm::complexexpression_constructor_args():
    sig = inspect.signature(vM::ComplexExpression.__init__)
    params = list(sig.parameters.keys())



def test_vm::constraint_is_not_abstract():
    assert not inspect.isabstract(vM::Constraint)


def test_vm::constraint_constructor_exists():
    assert callable(vM::Constraint.__init__)


def test_vm::constraint_constructor_args():
    sig = inspect.signature(vM::Constraint.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_vm::constraint_has_name():
    assert hasattr(vM::Constraint, "name")
    descriptor = None
    for klass in vM::Constraint.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_vm::abstract::att::id_is_not_abstract():
    assert not inspect.isabstract(vM::Abstract::ATT::ID)


def test_vm::abstract::att::id_constructor_exists():
    assert callable(vM::Abstract::ATT::ID.__init__)


def test_vm::abstract::att::id_constructor_args():
    sig = inspect.signature(vM::Abstract::ATT::ID.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_vm::abstract::att::id_has_name():
    assert hasattr(vM::Abstract::ATT::ID, "name")
    descriptor = None
    for klass in vM::Abstract::ATT::ID.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_vm::attributedescription_is_not_abstract():
    assert not inspect.isabstract(vM::AttributeDescription)


def test_vm::attributedescription_constructor_exists():
    assert callable(vM::AttributeDescription.__init__)


def test_vm::attributedescription_constructor_args():
    sig = inspect.signature(vM::AttributeDescription.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_vm::attributedescription_has_description():
    assert hasattr(vM::AttributeDescription, "description")
    descriptor = None
    for klass in vM::AttributeDescription.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_vm::featuredescription_is_not_abstract():
    assert not inspect.isabstract(vM::FeatureDescription)


def test_vm::featuredescription_constructor_exists():
    assert callable(vM::FeatureDescription.__init__)


def test_vm::featuredescription_constructor_args():
    sig = inspect.signature(vM::FeatureDescription.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_vm::featuredescription_has_description():
    assert hasattr(vM::FeatureDescription, "description")
    descriptor = None
    for klass in vM::FeatureDescription.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_vm::integerattrdefcomplement_is_not_abstract():
    assert not inspect.isabstract(vM::IntegerAttrDefComplement)


def test_vm::integerattrdefcomplement_constructor_exists():
    assert callable(vM::IntegerAttrDefComplement.__init__)


def test_vm::integerattrdefcomplement_constructor_args():
    sig = inspect.signature(vM::IntegerAttrDefComplement.__init__)
    params = list(sig.parameters.keys())
    assert "min" in params, "Missing parameter 'min'"
    assert "max" in params, "Missing parameter 'max'"

def test_vm::integerattrdefcomplement_has_min():
    assert hasattr(vM::IntegerAttrDefComplement, "min")
    descriptor = None
    for klass in vM::IntegerAttrDefComplement.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)

def test_vm::integerattrdefcomplement_has_max():
    assert hasattr(vM::IntegerAttrDefComplement, "max")
    descriptor = None
    for klass in vM::IntegerAttrDefComplement.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
            break
    assert isinstance(descriptor, property)



def test_vm::enum::real::att::id_is_not_abstract():
    assert not inspect.isabstract(vM::Enum::Real::ATT::ID)


def test_vm::enum::real::att::id_constructor_exists():
    assert callable(vM::Enum::Real::ATT::ID.__init__)


def test_vm::enum::real::att::id_constructor_args():
    sig = inspect.signature(vM::Enum::Real::ATT::ID.__init__)
    params = list(sig.parameters.keys())



def test_vm::enum::integer::att::id_is_not_abstract():
    assert not inspect.isabstract(vM::Enum::Integer::ATT::ID)


def test_vm::enum::integer::att::id_constructor_exists():
    assert callable(vM::Enum::Integer::ATT::ID.__init__)


def test_vm::enum::integer::att::id_constructor_args():
    sig = inspect.signature(vM::Enum::Integer::ATT::ID.__init__)
    params = list(sig.parameters.keys())



def test_vm::enum::string::att::id_is_not_abstract():
    assert not inspect.isabstract(vM::Enum::String::ATT::ID)


def test_vm::enum::string::att::id_constructor_exists():
    assert callable(vM::Enum::String::ATT::ID.__init__)


def test_vm::enum::string::att::id_constructor_args():
    sig = inspect.signature(vM::Enum::String::ATT::ID.__init__)
    params = list(sig.parameters.keys())



def test_enumattrdef_is_not_abstract():
    assert not inspect.isabstract(EnumAttrDef)


def test_enumattrdef_constructor_exists():
    assert callable(EnumAttrDef.__init__)


def test_enumattrdef_constructor_args():
    sig = inspect.signature(EnumAttrDef.__init__)
    params = list(sig.parameters.keys())



def test_vm::enumintegerdef_is_not_abstract():
    assert not inspect.isabstract(vM::EnumIntegerDef)


def test_vm::enumintegerdef_constructor_exists():
    assert callable(vM::EnumIntegerDef.__init__)


def test_vm::enumintegerdef_constructor_args():
    sig = inspect.signature(vM::EnumIntegerDef.__init__)
    params = list(sig.parameters.keys())



def test_vm::enumrealdef_is_not_abstract():
    assert not inspect.isabstract(vM::EnumRealDef)


def test_vm::enumrealdef_constructor_exists():
    assert callable(vM::EnumRealDef.__init__)


def test_vm::enumrealdef_constructor_args():
    sig = inspect.signature(vM::EnumRealDef.__init__)
    params = list(sig.parameters.keys())



def test_vm::enumstringdef_is_not_abstract():
    assert not inspect.isabstract(vM::EnumStringDef)


def test_vm::enumstringdef_constructor_exists():
    assert callable(vM::EnumStringDef.__init__)


def test_vm::enumstringdef_constructor_args():
    sig = inspect.signature(vM::EnumStringDef.__init__)
    params = list(sig.parameters.keys())



def test_vm::realdeltadef_is_not_abstract():
    assert not inspect.isabstract(vM::RealDeltaDef)


def test_vm::realdeltadef_constructor_exists():
    assert callable(vM::RealDeltaDef.__init__)


def test_vm::realdeltadef_constructor_args():
    sig = inspect.signature(vM::RealDeltaDef.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_vm::realdeltadef_has_value():
    assert hasattr(vM::RealDeltaDef, "value")
    descriptor = None
    for klass in vM::RealDeltaDef.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_vm::realattrdefcomplement_is_not_abstract():
    assert not inspect.isabstract(vM::RealAttrDefComplement)


def test_vm::realattrdefcomplement_constructor_exists():
    assert callable(vM::RealAttrDefComplement.__init__)


def test_vm::realattrdefcomplement_constructor_args():
    sig = inspect.signature(vM::RealAttrDefComplement.__init__)
    params = list(sig.parameters.keys())
    assert "max" in params, "Missing parameter 'max'"
    assert "min" in params, "Missing parameter 'min'"

def test_vm::realattrdefcomplement_has_max():
    assert hasattr(vM::RealAttrDefComplement, "max")
    descriptor = None
    for klass in vM::RealAttrDefComplement.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
            break
    assert isinstance(descriptor, property)

def test_vm::realattrdefcomplement_has_min():
    assert hasattr(vM::RealAttrDefComplement, "min")
    descriptor = None
    for klass in vM::RealAttrDefComplement.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)



def test_realattrdef_is_not_abstract():
    assert not inspect.isabstract(RealAttrDef)


def test_realattrdef_constructor_exists():
    assert callable(RealAttrDef.__init__)


def test_realattrdef_constructor_args():
    sig = inspect.signature(RealAttrDef.__init__)
    params = list(sig.parameters.keys())



def test_vm::realattrdefunbounded_is_not_abstract():
    assert not inspect.isabstract(vM::RealAttrDefUnbounded)


def test_vm::realattrdefunbounded_constructor_exists():
    assert callable(vM::RealAttrDefUnbounded.__init__)


def test_vm::realattrdefunbounded_constructor_args():
    sig = inspect.signature(vM::RealAttrDefUnbounded.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_vm::realattrdefunbounded_has_value():
    assert hasattr(vM::RealAttrDefUnbounded, "value")
    descriptor = None
    for klass in vM::RealAttrDefUnbounded.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_vm::realattrdefbounded_is_not_abstract():
    assert not inspect.isabstract(vM::RealAttrDefBounded)


def test_vm::realattrdefbounded_constructor_exists():
    assert callable(vM::RealAttrDefBounded.__init__)


def test_vm::realattrdefbounded_constructor_args():
    sig = inspect.signature(vM::RealAttrDefBounded.__init__)
    params = list(sig.parameters.keys())



def test_vm::realdefaultdef_is_not_abstract():
    assert not inspect.isabstract(vM::RealDefaultDef)


def test_vm::realdefaultdef_constructor_exists():
    assert callable(vM::RealDefaultDef.__init__)


def test_vm::realdefaultdef_constructor_args():
    sig = inspect.signature(vM::RealDefaultDef.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_vm::realdefaultdef_has_value():
    assert hasattr(vM::RealDefaultDef, "value")
    descriptor = None
    for klass in vM::RealDefaultDef.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_vm::real::att::id_is_not_abstract():
    assert not inspect.isabstract(vM::Real::ATT::ID)


def test_vm::real::att::id_constructor_exists():
    assert callable(vM::Real::ATT::ID.__init__)


def test_vm::real::att::id_constructor_args():
    sig = inspect.signature(vM::Real::ATT::ID.__init__)
    params = list(sig.parameters.keys())



def test_vm::integerdeltadef_is_not_abstract():
    assert not inspect.isabstract(vM::IntegerDeltaDef)


def test_vm::integerdeltadef_constructor_exists():
    assert callable(vM::IntegerDeltaDef.__init__)


def test_vm::integerdeltadef_constructor_args():
    sig = inspect.signature(vM::IntegerDeltaDef.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_vm::integerdeltadef_has_value():
    assert hasattr(vM::IntegerDeltaDef, "value")
    descriptor = None
    for klass in vM::IntegerDeltaDef.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_vm::featuredefinition_is_not_abstract():
    assert not inspect.isabstract(vM::FeatureDefinition)


def test_vm::featuredefinition_constructor_exists():
    assert callable(vM::FeatureDefinition.__init__)


def test_vm::featuredefinition_constructor_args():
    sig = inspect.signature(vM::FeatureDefinition.__init__)
    params = list(sig.parameters.keys())



def test_integerattrdef_is_not_abstract():
    assert not inspect.isabstract(IntegerAttrDef)


def test_integerattrdef_constructor_exists():
    assert callable(IntegerAttrDef.__init__)


def test_integerattrdef_constructor_args():
    sig = inspect.signature(IntegerAttrDef.__init__)
    params = list(sig.parameters.keys())



def test_vm::integerattrdefunbounded_is_not_abstract():
    assert not inspect.isabstract(vM::IntegerAttrDefUnbounded)


def test_vm::integerattrdefunbounded_constructor_exists():
    assert callable(vM::IntegerAttrDefUnbounded.__init__)


def test_vm::integerattrdefunbounded_constructor_args():
    sig = inspect.signature(vM::IntegerAttrDefUnbounded.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_vm::integerattrdefunbounded_has_value():
    assert hasattr(vM::IntegerAttrDefUnbounded, "value")
    descriptor = None
    for klass in vM::IntegerAttrDefUnbounded.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_vm::integerattrdefbounded_is_not_abstract():
    assert not inspect.isabstract(vM::IntegerAttrDefBounded)


def test_vm::integerattrdefbounded_constructor_exists():
    assert callable(vM::IntegerAttrDefBounded.__init__)


def test_vm::integerattrdefbounded_constructor_args():
    sig = inspect.signature(vM::IntegerAttrDefBounded.__init__)
    params = list(sig.parameters.keys())



def test_vm::integerdefaultdef_is_not_abstract():
    assert not inspect.isabstract(vM::IntegerDefaultDef)


def test_vm::integerdefaultdef_constructor_exists():
    assert callable(vM::IntegerDefaultDef.__init__)


def test_vm::integerdefaultdef_constructor_args():
    sig = inspect.signature(vM::IntegerDefaultDef.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_vm::integerdefaultdef_has_value():
    assert hasattr(vM::IntegerDefaultDef, "value")
    descriptor = None
    for klass in vM::IntegerDefaultDef.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_vm::integer::att::id_is_not_abstract():
    assert not inspect.isabstract(vM::Integer::ATT::ID)


def test_vm::integer::att::id_constructor_exists():
    assert callable(vM::Integer::ATT::ID.__init__)


def test_vm::integer::att::id_constructor_args():
    sig = inspect.signature(vM::Integer::ATT::ID.__init__)
    params = list(sig.parameters.keys())



def test_vm::stringdefaultdef_is_not_abstract():
    assert not inspect.isabstract(vM::StringDefaultDef)


def test_vm::stringdefaultdef_constructor_exists():
    assert callable(vM::StringDefaultDef.__init__)


def test_vm::stringdefaultdef_constructor_args():
    sig = inspect.signature(vM::StringDefaultDef.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_vm::stringdefaultdef_has_value():
    assert hasattr(vM::StringDefaultDef, "value")
    descriptor = None
    for klass in vM::StringDefaultDef.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_vm::string::att::id_is_not_abstract():
    assert not inspect.isabstract(vM::String::ATT::ID)


def test_vm::string::att::id_constructor_exists():
    assert callable(vM::String::ATT::ID.__init__)


def test_vm::string::att::id_constructor_args():
    sig = inspect.signature(vM::String::ATT::ID.__init__)
    params = list(sig.parameters.keys())



def test_vm::booldefaultdef_is_not_abstract():
    assert not inspect.isabstract(vM::BoolDefaultDef)


def test_vm::booldefaultdef_constructor_exists():
    assert callable(vM::BoolDefaultDef.__init__)


def test_vm::booldefaultdef_constructor_args():
    sig = inspect.signature(vM::BoolDefaultDef.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_vm::booldefaultdef_has_value():
    assert hasattr(vM::BoolDefaultDef, "value")
    descriptor = None
    for klass in vM::BoolDefaultDef.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_vm::boolean::att::id_is_not_abstract():
    assert not inspect.isabstract(vM::Boolean::ATT::ID)


def test_vm::boolean::att::id_constructor_exists():
    assert callable(vM::Boolean::ATT::ID.__init__)


def test_vm::boolean::att::id_constructor_args():
    sig = inspect.signature(vM::Boolean::ATT::ID.__init__)
    params = list(sig.parameters.keys())



def test_basicattrdef_is_not_abstract():
    assert not inspect.isabstract(BasicAttrDef)


def test_basicattrdef_constructor_exists():
    assert callable(BasicAttrDef.__init__)


def test_basicattrdef_constructor_args():
    sig = inspect.signature(BasicAttrDef.__init__)
    params = list(sig.parameters.keys())



def test_vm::stringattrdef_is_not_abstract():
    assert not inspect.isabstract(vM::StringAttrDef)


def test_vm::stringattrdef_constructor_exists():
    assert callable(vM::StringAttrDef.__init__)


def test_vm::stringattrdef_constructor_args():
    sig = inspect.signature(vM::StringAttrDef.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_vm::stringattrdef_has_value():
    assert hasattr(vM::StringAttrDef, "value")
    descriptor = None
    for klass in vM::StringAttrDef.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_vm::realattrdef_is_not_abstract():
    assert not inspect.isabstract(vM::RealAttrDef)


def test_vm::realattrdef_constructor_exists():
    assert callable(vM::RealAttrDef.__init__)


def test_vm::realattrdef_constructor_args():
    sig = inspect.signature(vM::RealAttrDef.__init__)
    params = list(sig.parameters.keys())



def test_vm::integerattrdef_is_not_abstract():
    assert not inspect.isabstract(vM::IntegerAttrDef)


def test_vm::integerattrdef_constructor_exists():
    assert callable(vM::IntegerAttrDef.__init__)


def test_vm::integerattrdef_constructor_args():
    sig = inspect.signature(vM::IntegerAttrDef.__init__)
    params = list(sig.parameters.keys())



def test_vm::booleanattrdef_is_not_abstract():
    assert not inspect.isabstract(vM::BooleanAttrDef)


def test_vm::booleanattrdef_constructor_exists():
    assert callable(vM::BooleanAttrDef.__init__)


def test_vm::booleanattrdef_constructor_args():
    sig = inspect.signature(vM::BooleanAttrDef.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_vm::booleanattrdef_has_value():
    assert hasattr(vM::BooleanAttrDef, "value")
    descriptor = None
    for klass in vM::BooleanAttrDef.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_vm::enumattrdef_is_not_abstract():
    assert not inspect.isabstract(vM::EnumAttrDef)


def test_vm::enumattrdef_constructor_exists():
    assert callable(vM::EnumAttrDef.__init__)


def test_vm::enumattrdef_constructor_args():
    sig = inspect.signature(vM::EnumAttrDef.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_vm::enumattrdef_has_value():
    assert hasattr(vM::EnumAttrDef, "value")
    descriptor = None
    for klass in vM::EnumAttrDef.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_vm::basicattrdef_is_not_abstract():
    assert not inspect.isabstract(vM::BasicAttrDef)


def test_vm::basicattrdef_constructor_exists():
    assert callable(vM::BasicAttrDef.__init__)


def test_vm::basicattrdef_constructor_args():
    sig = inspect.signature(vM::BasicAttrDef.__init__)
    params = list(sig.parameters.keys())



def test_vm::basicattrvaluation_is_not_abstract():
    assert not inspect.isabstract(vM::BasicAttrValuation)


def test_vm::basicattrvaluation_constructor_exists():
    assert callable(vM::BasicAttrValuation.__init__)


def test_vm::basicattrvaluation_constructor_args():
    sig = inspect.signature(vM::BasicAttrValuation.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_vm::basicattrvaluation_has_value():
    assert hasattr(vM::BasicAttrValuation, "value")
    descriptor = None
    for klass in vM::BasicAttrValuation.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_vm::attrdef_is_not_abstract():
    assert not inspect.isabstract(vM::AttrDef)


def test_vm::attrdef_constructor_exists():
    assert callable(vM::AttrDef.__init__)


def test_vm::attrdef_constructor_args():
    sig = inspect.signature(vM::AttrDef.__init__)
    params = list(sig.parameters.keys())
    assert "notTranslatable" in params, "Missing parameter 'notTranslatable'"
    assert "notDecidable" in params, "Missing parameter 'notDecidable'"
    assert "runTime" in params, "Missing parameter 'runTime'"

def test_vm::attrdef_has_notTranslatable():
    assert hasattr(vM::AttrDef, "notTranslatable")
    descriptor = None
    for klass in vM::AttrDef.__mro__:
        if "notTranslatable" in klass.__dict__:
            descriptor = klass.__dict__["notTranslatable"]
            break
    assert isinstance(descriptor, property)

def test_vm::attrdef_has_notDecidable():
    assert hasattr(vM::AttrDef, "notDecidable")
    descriptor = None
    for klass in vM::AttrDef.__mro__:
        if "notDecidable" in klass.__dict__:
            descriptor = klass.__dict__["notDecidable"]
            break
    assert isinstance(descriptor, property)

def test_vm::attrdef_has_runTime():
    assert hasattr(vM::AttrDef, "runTime")
    descriptor = None
    for klass in vM::AttrDef.__mro__:
        if "runTime" in klass.__dict__:
            descriptor = klass.__dict__["runTime"]
            break
    assert isinstance(descriptor, property)



def test_featuresgroup_is_not_abstract():
    assert not inspect.isabstract(FeaturesGroup)


def test_featuresgroup_constructor_exists():
    assert callable(FeaturesGroup.__init__)


def test_featuresgroup_constructor_args():
    sig = inspect.signature(FeaturesGroup.__init__)
    params = list(sig.parameters.keys())



def test_vm::cardinalitybased_is_not_abstract():
    assert not inspect.isabstract(vM::CardinalityBased)


def test_vm::cardinalitybased_constructor_exists():
    assert callable(vM::CardinalityBased.__init__)


def test_vm::cardinalitybased_constructor_args():
    sig = inspect.signature(vM::CardinalityBased.__init__)
    params = list(sig.parameters.keys())
    assert "min" in params, "Missing parameter 'min'"
    assert "all" in params, "Missing parameter 'all'"
    assert "max" in params, "Missing parameter 'max'"

def test_vm::cardinalitybased_has_min():
    assert hasattr(vM::CardinalityBased, "min")
    descriptor = None
    for klass in vM::CardinalityBased.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)

def test_vm::cardinalitybased_has_all():
    assert hasattr(vM::CardinalityBased, "all")
    descriptor = None
    for klass in vM::CardinalityBased.__mro__:
        if "all" in klass.__dict__:
            descriptor = klass.__dict__["all"]
            break
    assert isinstance(descriptor, property)

def test_vm::cardinalitybased_has_max():
    assert hasattr(vM::CardinalityBased, "max")
    descriptor = None
    for klass in vM::CardinalityBased.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
            break
    assert isinstance(descriptor, property)



def test_vm::orgroup_is_not_abstract():
    assert not inspect.isabstract(vM::Orgroup)


def test_vm::orgroup_constructor_exists():
    assert callable(vM::Orgroup.__init__)


def test_vm::orgroup_constructor_args():
    sig = inspect.signature(vM::Orgroup.__init__)
    params = list(sig.parameters.keys())



def test_vm::xorgroup_is_not_abstract():
    assert not inspect.isabstract(vM::Xorgroup)


def test_vm::xorgroup_constructor_exists():
    assert callable(vM::Xorgroup.__init__)


def test_vm::xorgroup_constructor_args():
    sig = inspect.signature(vM::Xorgroup.__init__)
    params = list(sig.parameters.keys())



def test_featuredefinition_is_not_abstract():
    assert not inspect.isabstract(FeatureDefinition)


def test_featuredefinition_constructor_exists():
    assert callable(FeatureDefinition.__init__)


def test_featuredefinition_constructor_args():
    sig = inspect.signature(FeatureDefinition.__init__)
    params = list(sig.parameters.keys())



def test_vm::featuresgroup_is_not_abstract():
    assert not inspect.isabstract(vM::FeaturesGroup)


def test_vm::featuresgroup_constructor_exists():
    assert callable(vM::FeaturesGroup.__init__)


def test_vm::featuresgroup_constructor_args():
    sig = inspect.signature(vM::FeaturesGroup.__init__)
    params = list(sig.parameters.keys())



def test_vm::feature_is_not_abstract():
    assert not inspect.isabstract(vM::Feature)


def test_vm::feature_constructor_exists():
    assert callable(vM::Feature.__init__)


def test_vm::feature_constructor_args():
    sig = inspect.signature(vM::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "optional" in params, "Missing parameter 'optional'"
    assert "max" in params, "Missing parameter 'max'"
    assert "notTranslatable" in params, "Missing parameter 'notTranslatable'"
    assert "notDecidable" in params, "Missing parameter 'notDecidable'"
    assert "runTime" in params, "Missing parameter 'runTime'"
    assert "name" in params, "Missing parameter 'name'"
    assert "min" in params, "Missing parameter 'min'"

def test_vm::feature_has_optional():
    assert hasattr(vM::Feature, "optional")
    descriptor = None
    for klass in vM::Feature.__mro__:
        if "optional" in klass.__dict__:
            descriptor = klass.__dict__["optional"]
            break
    assert isinstance(descriptor, property)

def test_vm::feature_has_max():
    assert hasattr(vM::Feature, "max")
    descriptor = None
    for klass in vM::Feature.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
            break
    assert isinstance(descriptor, property)

def test_vm::feature_has_notTranslatable():
    assert hasattr(vM::Feature, "notTranslatable")
    descriptor = None
    for klass in vM::Feature.__mro__:
        if "notTranslatable" in klass.__dict__:
            descriptor = klass.__dict__["notTranslatable"]
            break
    assert isinstance(descriptor, property)

def test_vm::feature_has_notDecidable():
    assert hasattr(vM::Feature, "notDecidable")
    descriptor = None
    for klass in vM::Feature.__mro__:
        if "notDecidable" in klass.__dict__:
            descriptor = klass.__dict__["notDecidable"]
            break
    assert isinstance(descriptor, property)

def test_vm::feature_has_runTime():
    assert hasattr(vM::Feature, "runTime")
    descriptor = None
    for klass in vM::Feature.__mro__:
        if "runTime" in klass.__dict__:
            descriptor = klass.__dict__["runTime"]
            break
    assert isinstance(descriptor, property)

def test_vm::feature_has_name():
    assert hasattr(vM::Feature, "name")
    descriptor = None
    for klass in vM::Feature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_vm::feature_has_min():
    assert hasattr(vM::Feature, "min")
    descriptor = None
    for klass in vM::Feature.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)



def test_vm::featurehierarchy_is_not_abstract():
    assert not inspect.isabstract(vM::FeatureHierarchy)


def test_vm::featurehierarchy_constructor_exists():
    assert callable(vM::FeatureHierarchy.__init__)


def test_vm::featurehierarchy_constructor_args():
    sig = inspect.signature(vM::FeatureHierarchy.__init__)
    params = list(sig.parameters.keys())



def test_vm::email_is_not_abstract():
    assert not inspect.isabstract(vM::Email)


def test_vm::email_constructor_exists():
    assert callable(vM::Email.__init__)


def test_vm::email_constructor_args():
    sig = inspect.signature(vM::Email.__init__)
    params = list(sig.parameters.keys())
    assert "username" in params, "Missing parameter 'username'"
    assert "domain" in params, "Missing parameter 'domain'"

def test_vm::email_has_username():
    assert hasattr(vM::Email, "username")
    descriptor = None
    for klass in vM::Email.__mro__:
        if "username" in klass.__dict__:
            descriptor = klass.__dict__["username"]
            break
    assert isinstance(descriptor, property)

def test_vm::email_has_domain():
    assert hasattr(vM::Email, "domain")
    descriptor = None
    for klass in vM::Email.__mro__:
        if "domain" in klass.__dict__:
            descriptor = klass.__dict__["domain"]
            break
    assert isinstance(descriptor, property)



def test_vm::version_is_not_abstract():
    assert not inspect.isabstract(vM::Version)


def test_vm::version_constructor_exists():
    assert callable(vM::Version.__init__)


def test_vm::version_constructor_args():
    sig = inspect.signature(vM::Version.__init__)
    params = list(sig.parameters.keys())
    assert "tail" in params, "Missing parameter 'tail'"
    assert "main" in params, "Missing parameter 'main'"

def test_vm::version_has_tail():
    assert hasattr(vM::Version, "tail")
    descriptor = None
    for klass in vM::Version.__mro__:
        if "tail" in klass.__dict__:
            descriptor = klass.__dict__["tail"]
            break
    assert isinstance(descriptor, property)

def test_vm::version_has_main():
    assert hasattr(vM::Version, "main")
    descriptor = None
    for klass in vM::Version.__mro__:
        if "main" in klass.__dict__:
            descriptor = klass.__dict__["main"]
            break
    assert isinstance(descriptor, property)



def test_vmblock_is_not_abstract():
    assert not inspect.isabstract(VmBlock)


def test_vmblock_constructor_exists():
    assert callable(VmBlock.__init__)


def test_vmblock_constructor_args():
    sig = inspect.signature(VmBlock.__init__)
    params = list(sig.parameters.keys())



def test_vm::attributes_is_not_abstract():
    assert not inspect.isabstract(vM::Attributes)


def test_vm::attributes_constructor_exists():
    assert callable(vM::Attributes.__init__)


def test_vm::attributes_constructor_args():
    sig = inspect.signature(vM::Attributes.__init__)
    params = list(sig.parameters.keys())



def test_vm::objectives_is_not_abstract():
    assert not inspect.isabstract(vM::Objectives)


def test_vm::objectives_constructor_exists():
    assert callable(vM::Objectives.__init__)


def test_vm::objectives_constructor_args():
    sig = inspect.signature(vM::Objectives.__init__)
    params = list(sig.parameters.keys())



def test_vm::importdeclaration_is_not_abstract():
    assert not inspect.isabstract(vM::ImportDeclaration)


def test_vm::importdeclaration_constructor_exists():
    assert callable(vM::ImportDeclaration.__init__)


def test_vm::importdeclaration_constructor_args():
    sig = inspect.signature(vM::ImportDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "importedNamespace" in params, "Missing parameter 'importedNamespace'"

def test_vm::importdeclaration_has_importedNamespace():
    assert hasattr(vM::ImportDeclaration, "importedNamespace")
    descriptor = None
    for klass in vM::ImportDeclaration.__mro__:
        if "importedNamespace" in klass.__dict__:
            descriptor = klass.__dict__["importedNamespace"]
            break
    assert isinstance(descriptor, property)



def test_vm::configurations_is_not_abstract():
    assert not inspect.isabstract(vM::Configurations)


def test_vm::configurations_constructor_exists():
    assert callable(vM::Configurations.__init__)


def test_vm::configurations_constructor_args():
    sig = inspect.signature(vM::Configurations.__init__)
    params = list(sig.parameters.keys())



def test_vm::relationships_is_not_abstract():
    assert not inspect.isabstract(vM::Relationships)


def test_vm::relationships_constructor_exists():
    assert callable(vM::Relationships.__init__)


def test_vm::relationships_constructor_args():
    sig = inspect.signature(vM::Relationships.__init__)
    params = list(sig.parameters.keys())



def test_vm::descriptions_is_not_abstract():
    assert not inspect.isabstract(vM::Descriptions)


def test_vm::descriptions_constructor_exists():
    assert callable(vM::Descriptions.__init__)


def test_vm::descriptions_constructor_args():
    sig = inspect.signature(vM::Descriptions.__init__)
    params = list(sig.parameters.keys())



def test_vm::metadatadeclaration_is_not_abstract():
    assert not inspect.isabstract(vM::MetaDataDeclaration)


def test_vm::metadatadeclaration_constructor_exists():
    assert callable(vM::MetaDataDeclaration.__init__)


def test_vm::metadatadeclaration_constructor_args():
    sig = inspect.signature(vM::MetaDataDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "organization" in params, "Missing parameter 'organization'"
    assert "date" in params, "Missing parameter 'date'"
    assert "description" in params, "Missing parameter 'description'"
    assert "author" in params, "Missing parameter 'author'"
    assert "publication" in params, "Missing parameter 'publication'"

def test_vm::metadatadeclaration_has_name():
    assert hasattr(vM::MetaDataDeclaration, "name")
    descriptor = None
    for klass in vM::MetaDataDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_vm::metadatadeclaration_has_organization():
    assert hasattr(vM::MetaDataDeclaration, "organization")
    descriptor = None
    for klass in vM::MetaDataDeclaration.__mro__:
        if "organization" in klass.__dict__:
            descriptor = klass.__dict__["organization"]
            break
    assert isinstance(descriptor, property)

def test_vm::metadatadeclaration_has_date():
    assert hasattr(vM::MetaDataDeclaration, "date")
    descriptor = None
    for klass in vM::MetaDataDeclaration.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_vm::metadatadeclaration_has_description():
    assert hasattr(vM::MetaDataDeclaration, "description")
    descriptor = None
    for klass in vM::MetaDataDeclaration.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_vm::metadatadeclaration_has_author():
    assert hasattr(vM::MetaDataDeclaration, "author")
    descriptor = None
    for klass in vM::MetaDataDeclaration.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_vm::metadatadeclaration_has_publication():
    assert hasattr(vM::MetaDataDeclaration, "publication")
    descriptor = None
    for klass in vM::MetaDataDeclaration.__mro__:
        if "publication" in klass.__dict__:
            descriptor = klass.__dict__["publication"]
            break
    assert isinstance(descriptor, property)



def test_vm::constraints_is_not_abstract():
    assert not inspect.isabstract(vM::Constraints)


def test_vm::constraints_constructor_exists():
    assert callable(vM::Constraints.__init__)


def test_vm::constraints_constructor_args():
    sig = inspect.signature(vM::Constraints.__init__)
    params = list(sig.parameters.keys())



def test_vm::packagedeclaration_is_not_abstract():
    assert not inspect.isabstract(vM::PackageDeclaration)


def test_vm::packagedeclaration_constructor_exists():
    assert callable(vM::PackageDeclaration.__init__)


def test_vm::packagedeclaration_constructor_args():
    sig = inspect.signature(vM::PackageDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_vm::packagedeclaration_has_name():
    assert hasattr(vM::PackageDeclaration, "name")
    descriptor = None
    for klass in vM::PackageDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_vm::vmblock_is_not_abstract():
    assert not inspect.isabstract(vM::VmBlock)


def test_vm::vmblock_constructor_exists():
    assert callable(vM::VmBlock.__init__)


def test_vm::vmblock_constructor_args():
    sig = inspect.signature(vM::VmBlock.__init__)
    params = list(sig.parameters.keys())



def test_vm::model_is_not_abstract():
    assert not inspect.isabstract(vM::Model)


def test_vm::model_constructor_exists():
    assert callable(vM::Model.__init__)


def test_vm::model_constructor_args():
    sig = inspect.signature(vM::Model.__init__)
    params = list(sig.parameters.keys())


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
Abstract::ATT::ID_strategy = st.builds(
    Abstract::ATT::ID,
)
vM::PairFeatureReal_strategy = st.builds(
    vM::PairFeatureReal,
    value=
        safe_text
)
vM::PairFeatureInteger_strategy = st.builds(
    vM::PairFeatureInteger,
    value=
        safe_text
)
TableBasedValuationByAttribute_strategy = st.builds(
    TableBasedValuationByAttribute,
)
vM::TableBasedValuationByAttributeForReal_strategy = st.builds(
    vM::TableBasedValuationByAttributeForReal,
)
vM::TableBasedValuationByAttributeForInteger_strategy = st.builds(
    vM::TableBasedValuationByAttributeForInteger,
)
vM::PairAttributeValue_strategy = st.builds(
    vM::PairAttributeValue,
    value=
        safe_text
)
vM::TableBasedValuationByFeatureAndClone_strategy = st.builds(
    vM::TableBasedValuationByFeatureAndClone,
    name=
        safe_text
)
vM::TableBasedValuationByAttribute_strategy = st.builds(
    vM::TableBasedValuationByAttribute,
)
vM::TableBasedValuationByFeature_strategy = st.builds(
    vM::TableBasedValuationByFeature,
)
BasicAttrValuation_strategy = st.builds(
    BasicAttrValuation,
)
vM::BooleanAttrValuation_strategy = st.builds(
    vM::BooleanAttrValuation,
)
vM::StringAttrValuation_strategy = st.builds(
    vM::StringAttrValuation,
)
vM::IntegerAttrValuation_strategy = st.builds(
    vM::IntegerAttrValuation,
)
vM::RealAttrValuation_strategy = st.builds(
    vM::RealAttrValuation,
)
ExtendedValuation_strategy = st.builds(
    ExtendedValuation,
)
vM::AdvancedAttrValuation_strategy = st.builds(
    vM::AdvancedAttrValuation,
)
vM::ExtendedValuation_strategy = st.builds(
    vM::ExtendedValuation,
)
vM::BooleanValuation_strategy = st.builds(
    vM::BooleanValuation,
    notSelected=
        st.booleans()
)
vM::Configuration_strategy = st.builds(
    vM::Configuration,
    name=
        safe_text
)
vM::ObjectiveExpression_strategy = st.builds(
    vM::ObjectiveExpression,
    op=
        safe_text
)
vM::Objective_strategy = st.builds(
    vM::Objective,
    name=
        safe_text,
    op=
        safe_text
)
vM::NumericExpression::List_strategy = st.builds(
    vM::NumericExpression::List,
)
vM::BooleanExpression::List_strategy = st.builds(
    vM::BooleanExpression::List,
)
vM::AttHead_strategy = st.builds(
    vM::AttHead,
    forAllFeatures=
        st.booleans()
)
Expression_strategy = st.builds(
    Expression,
)
vM::StringExpression_strategy = st.builds(
    vM::StringExpression,
    value=
        safe_text
)
vM::BooleanExpression_strategy = st.builds(
    vM::BooleanExpression,
    value=
        safe_text,
    op=
        safe_text
)
vM::BrackedExpression_strategy = st.builds(
    vM::BrackedExpression,
)
vM::PrimitiveExpression_strategy = st.builds(
    vM::PrimitiveExpression,
)
vM::NumericExpression_strategy = st.builds(
    vM::NumericExpression,
    value=
        safe_text,
    op=
        safe_text
)
vM::SpecialExpression_strategy = st.builds(
    vM::SpecialExpression,
    op=
        safe_text
)
ComplexExpression_strategy = st.builds(
    ComplexExpression,
)
vM::LeftImplication_strategy = st.builds(
    vM::LeftImplication,
)
vM::Inequality_strategy = st.builds(
    vM::Inequality,
)
vM::Plus_strategy = st.builds(
    vM::Plus,
)
vM::RightImplication_strategy = st.builds(
    vM::RightImplication,
)
vM::Or_strategy = st.builds(
    vM::Or,
)
vM::Less_strategy = st.builds(
    vM::Less,
)
vM::Excludes_strategy = st.builds(
    vM::Excludes,
)
vM::Equality_strategy = st.builds(
    vM::Equality,
)
vM::Lessequal_strategy = st.builds(
    vM::Lessequal,
)
vM::BiImplication_strategy = st.builds(
    vM::BiImplication,
)
vM::Greater_strategy = st.builds(
    vM::Greater,
)
vM::Minus_strategy = st.builds(
    vM::Minus,
)
vM::Greaterequal_strategy = st.builds(
    vM::Greaterequal,
)
vM::Requires_strategy = st.builds(
    vM::Requires,
)
vM::Multiplication_strategy = st.builds(
    vM::Multiplication,
)
vM::Division_strategy = st.builds(
    vM::Division,
)
vM::If_strategy = st.builds(
    vM::If,
)
vM::And_strategy = st.builds(
    vM::And,
)
vM::Expression_strategy = st.builds(
    vM::Expression,
)
vM::ComplexExpression_strategy = st.builds(
    vM::ComplexExpression,
)
vM::Constraint_strategy = st.builds(
    vM::Constraint,
    name=
        safe_text
)
vM::Abstract::ATT::ID_strategy = st.builds(
    vM::Abstract::ATT::ID,
    name=
        safe_text
)
vM::AttributeDescription_strategy = st.builds(
    vM::AttributeDescription,
    description=
        safe_text
)
vM::FeatureDescription_strategy = st.builds(
    vM::FeatureDescription,
    description=
        safe_text
)
vM::IntegerAttrDefComplement_strategy = st.builds(
    vM::IntegerAttrDefComplement,
    min=
        safe_text,
    max=
        safe_text
)
vM::Enum::Real::ATT::ID_strategy = st.builds(
    vM::Enum::Real::ATT::ID,
)
vM::Enum::Integer::ATT::ID_strategy = st.builds(
    vM::Enum::Integer::ATT::ID,
)
vM::Enum::String::ATT::ID_strategy = st.builds(
    vM::Enum::String::ATT::ID,
)
EnumAttrDef_strategy = st.builds(
    EnumAttrDef,
)
vM::EnumIntegerDef_strategy = st.builds(
    vM::EnumIntegerDef,
)
vM::EnumRealDef_strategy = st.builds(
    vM::EnumRealDef,
)
vM::EnumStringDef_strategy = st.builds(
    vM::EnumStringDef,
)
vM::RealDeltaDef_strategy = st.builds(
    vM::RealDeltaDef,
    value=
        safe_text
)
vM::RealAttrDefComplement_strategy = st.builds(
    vM::RealAttrDefComplement,
    max=
        safe_text,
    min=
        safe_text
)
RealAttrDef_strategy = st.builds(
    RealAttrDef,
)
vM::RealAttrDefUnbounded_strategy = st.builds(
    vM::RealAttrDefUnbounded,
    value=
        safe_text
)
vM::RealAttrDefBounded_strategy = st.builds(
    vM::RealAttrDefBounded,
)
vM::RealDefaultDef_strategy = st.builds(
    vM::RealDefaultDef,
    value=
        safe_text
)
vM::Real::ATT::ID_strategy = st.builds(
    vM::Real::ATT::ID,
)
vM::IntegerDeltaDef_strategy = st.builds(
    vM::IntegerDeltaDef,
    value=
        st.integers()
)
vM::FeatureDefinition_strategy = st.builds(
    vM::FeatureDefinition,
)
IntegerAttrDef_strategy = st.builds(
    IntegerAttrDef,
)
vM::IntegerAttrDefUnbounded_strategy = st.builds(
    vM::IntegerAttrDefUnbounded,
    value=
        safe_text
)
vM::IntegerAttrDefBounded_strategy = st.builds(
    vM::IntegerAttrDefBounded,
)
vM::IntegerDefaultDef_strategy = st.builds(
    vM::IntegerDefaultDef,
    value=
        st.integers()
)
vM::Integer::ATT::ID_strategy = st.builds(
    vM::Integer::ATT::ID,
)
vM::StringDefaultDef_strategy = st.builds(
    vM::StringDefaultDef,
    value=
        safe_text
)
vM::String::ATT::ID_strategy = st.builds(
    vM::String::ATT::ID,
)
vM::BoolDefaultDef_strategy = st.builds(
    vM::BoolDefaultDef,
    value=
        safe_text
)
vM::Boolean::ATT::ID_strategy = st.builds(
    vM::Boolean::ATT::ID,
)
BasicAttrDef_strategy = st.builds(
    BasicAttrDef,
)
vM::StringAttrDef_strategy = st.builds(
    vM::StringAttrDef,
    value=
        safe_text
)
vM::RealAttrDef_strategy = st.builds(
    vM::RealAttrDef,
)
vM::IntegerAttrDef_strategy = st.builds(
    vM::IntegerAttrDef,
)
vM::BooleanAttrDef_strategy = st.builds(
    vM::BooleanAttrDef,
    value=
        safe_text
)
vM::EnumAttrDef_strategy = st.builds(
    vM::EnumAttrDef,
    value=
        safe_text
)
vM::BasicAttrDef_strategy = st.builds(
    vM::BasicAttrDef,
)
vM::BasicAttrValuation_strategy = st.builds(
    vM::BasicAttrValuation,
    value=
        safe_text
)
vM::AttrDef_strategy = st.builds(
    vM::AttrDef,
    notTranslatable=
        st.booleans(),
    notDecidable=
        st.booleans(),
    runTime=
        st.booleans()
)
FeaturesGroup_strategy = st.builds(
    FeaturesGroup,
)
vM::CardinalityBased_strategy = st.builds(
    vM::CardinalityBased,
    min=
        safe_text,
    all=
        st.booleans(),
    max=
        safe_text
)
vM::Orgroup_strategy = st.builds(
    vM::Orgroup,
)
vM::Xorgroup_strategy = st.builds(
    vM::Xorgroup,
)
FeatureDefinition_strategy = st.builds(
    FeatureDefinition,
)
vM::FeaturesGroup_strategy = st.builds(
    vM::FeaturesGroup,
)
vM::Feature_strategy = st.builds(
    vM::Feature,
    optional=
        st.booleans(),
    max=
        safe_text,
    notTranslatable=
        st.booleans(),
    notDecidable=
        st.booleans(),
    runTime=
        st.booleans(),
    name=
        safe_text,
    min=
        safe_text
)
vM::FeatureHierarchy_strategy = st.builds(
    vM::FeatureHierarchy,
)
vM::Email_strategy = st.builds(
    vM::Email,
    username=
        safe_text,
    domain=
        safe_text
)
vM::Version_strategy = st.builds(
    vM::Version,
    tail=
        st.integers(),
    main=
        st.integers()
)
VmBlock_strategy = st.builds(
    VmBlock,
)
vM::Attributes_strategy = st.builds(
    vM::Attributes,
)
vM::Objectives_strategy = st.builds(
    vM::Objectives,
)
vM::ImportDeclaration_strategy = st.builds(
    vM::ImportDeclaration,
    importedNamespace=
        safe_text
)
vM::Configurations_strategy = st.builds(
    vM::Configurations,
)
vM::Relationships_strategy = st.builds(
    vM::Relationships,
)
vM::Descriptions_strategy = st.builds(
    vM::Descriptions,
)
vM::MetaDataDeclaration_strategy = st.builds(
    vM::MetaDataDeclaration,
    name=
        safe_text,
    organization=
        safe_text,
    date=
        safe_text,
    description=
        safe_text,
    author=
        safe_text,
    publication=
        safe_text
)
vM::Constraints_strategy = st.builds(
    vM::Constraints,
)
vM::PackageDeclaration_strategy = st.builds(
    vM::PackageDeclaration,
    name=
        safe_text
)
vM::VmBlock_strategy = st.builds(
    vM::VmBlock,
)
vM::Model_strategy = st.builds(
    vM::Model,
)

@given(instance=Abstract::ATT::ID_strategy)
@settings(max_examples=50)
def test_abstract::att::id_instantiation(instance):
    assert isinstance(instance, Abstract::ATT::ID)

@given(instance=vM::PairFeatureReal_strategy)
@settings(max_examples=50)
def test_vm::pairfeaturereal_instantiation(instance):
    assert isinstance(instance, vM::PairFeatureReal)

@given(instance=vM::PairFeatureReal_strategy)
def test_vm::pairfeaturereal_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=vM::PairFeatureReal_strategy)
def test_vm::pairfeaturereal_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=vM::PairFeatureInteger_strategy)
@settings(max_examples=50)
def test_vm::pairfeatureinteger_instantiation(instance):
    assert isinstance(instance, vM::PairFeatureInteger)

@given(instance=vM::PairFeatureInteger_strategy)
def test_vm::pairfeatureinteger_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=vM::PairFeatureInteger_strategy)
def test_vm::pairfeatureinteger_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=TableBasedValuationByAttribute_strategy)
@settings(max_examples=50)
def test_tablebasedvaluationbyattribute_instantiation(instance):
    assert isinstance(instance, TableBasedValuationByAttribute)

@given(instance=vM::TableBasedValuationByAttributeForReal_strategy)
@settings(max_examples=50)
def test_vm::tablebasedvaluationbyattributeforreal_instantiation(instance):
    assert isinstance(instance, vM::TableBasedValuationByAttributeForReal)

@given(instance=vM::TableBasedValuationByAttributeForInteger_strategy)
@settings(max_examples=50)
def test_vm::tablebasedvaluationbyattributeforinteger_instantiation(instance):
    assert isinstance(instance, vM::TableBasedValuationByAttributeForInteger)

@given(instance=vM::PairAttributeValue_strategy)
@settings(max_examples=50)
def test_vm::pairattributevalue_instantiation(instance):
    assert isinstance(instance, vM::PairAttributeValue)

@given(instance=vM::PairAttributeValue_strategy)
def test_vm::pairattributevalue_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=vM::PairAttributeValue_strategy)
def test_vm::pairattributevalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=vM::TableBasedValuationByFeatureAndClone_strategy)
@settings(max_examples=50)
def test_vm::tablebasedvaluationbyfeatureandclone_instantiation(instance):
    assert isinstance(instance, vM::TableBasedValuationByFeatureAndClone)

@given(instance=vM::TableBasedValuationByFeatureAndClone_strategy)
def test_vm::tablebasedvaluationbyfeatureandclone_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=vM::TableBasedValuationByFeatureAndClone_strategy)
def test_vm::tablebasedvaluationbyfeatureandclone_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=vM::TableBasedValuationByAttribute_strategy)
@settings(max_examples=50)
def test_vm::tablebasedvaluationbyattribute_instantiation(instance):
    assert isinstance(instance, vM::TableBasedValuationByAttribute)

@given(instance=vM::TableBasedValuationByFeature_strategy)
@settings(max_examples=50)
def test_vm::tablebasedvaluationbyfeature_instantiation(instance):
    assert isinstance(instance, vM::TableBasedValuationByFeature)

@given(instance=BasicAttrValuation_strategy)
@settings(max_examples=50)
def test_basicattrvaluation_instantiation(instance):
    assert isinstance(instance, BasicAttrValuation)

@given(instance=vM::BooleanAttrValuation_strategy)
@settings(max_examples=50)
def test_vm::booleanattrvaluation_instantiation(instance):
    assert isinstance(instance, vM::BooleanAttrValuation)

@given(instance=vM::StringAttrValuation_strategy)
@settings(max_examples=50)
def test_vm::stringattrvaluation_instantiation(instance):
    assert isinstance(instance, vM::StringAttrValuation)

@given(instance=vM::IntegerAttrValuation_strategy)
@settings(max_examples=50)
def test_vm::integerattrvaluation_instantiation(instance):
    assert isinstance(instance, vM::IntegerAttrValuation)

@given(instance=vM::RealAttrValuation_strategy)
@settings(max_examples=50)
def test_vm::realattrvaluation_instantiation(instance):
    assert isinstance(instance, vM::RealAttrValuation)

@given(instance=ExtendedValuation_strategy)
@settings(max_examples=50)
def test_extendedvaluation_instantiation(instance):
    assert isinstance(instance, ExtendedValuation)

@given(instance=vM::AdvancedAttrValuation_strategy)
@settings(max_examples=50)
def test_vm::advancedattrvaluation_instantiation(instance):
    assert isinstance(instance, vM::AdvancedAttrValuation)

@given(instance=vM::ExtendedValuation_strategy)
@settings(max_examples=50)
def test_vm::extendedvaluation_instantiation(instance):
    assert isinstance(instance, vM::ExtendedValuation)

@given(instance=vM::BooleanValuation_strategy)
@settings(max_examples=50)
def test_vm::booleanvaluation_instantiation(instance):
    assert isinstance(instance, vM::BooleanValuation)

@given(instance=vM::BooleanValuation_strategy)
def test_vm::booleanvaluation_notSelected_type(instance):
    assert isinstance(instance.notSelected, bool)


@given(instance=vM::BooleanValuation_strategy)
def test_vm::booleanvaluation_notSelected_setter(instance):
    original = instance.notSelected
    instance.notSelected = original
    assert instance.notSelected == original

@given(instance=vM::Configuration_strategy)
@settings(max_examples=50)
def test_vm::configuration_instantiation(instance):
    assert isinstance(instance, vM::Configuration)

@given(instance=vM::Configuration_strategy)
def test_vm::configuration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=vM::Configuration_strategy)
def test_vm::configuration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=vM::ObjectiveExpression_strategy)
@settings(max_examples=50)
def test_vm::objectiveexpression_instantiation(instance):
    assert isinstance(instance, vM::ObjectiveExpression)

@given(instance=vM::ObjectiveExpression_strategy)
def test_vm::objectiveexpression_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=vM::ObjectiveExpression_strategy)
def test_vm::objectiveexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=vM::Objective_strategy)
@settings(max_examples=50)
def test_vm::objective_instantiation(instance):
    assert isinstance(instance, vM::Objective)

@given(instance=vM::Objective_strategy)
def test_vm::objective_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=vM::Objective_strategy)
def test_vm::objective_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=vM::Objective_strategy)
def test_vm::objective_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=vM::Objective_strategy)
def test_vm::objective_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=vM::NumericExpression::List_strategy)
@settings(max_examples=50)
def test_vm::numericexpression::list_instantiation(instance):
    assert isinstance(instance, vM::NumericExpression::List)

@given(instance=vM::BooleanExpression::List_strategy)
@settings(max_examples=50)
def test_vm::booleanexpression::list_instantiation(instance):
    assert isinstance(instance, vM::BooleanExpression::List)

@given(instance=vM::AttHead_strategy)
@settings(max_examples=50)
def test_vm::atthead_instantiation(instance):
    assert isinstance(instance, vM::AttHead)

@given(instance=vM::AttHead_strategy)
def test_vm::atthead_forAllFeatures_type(instance):
    assert isinstance(instance.forAllFeatures, bool)


@given(instance=vM::AttHead_strategy)
def test_vm::atthead_forAllFeatures_setter(instance):
    original = instance.forAllFeatures
    instance.forAllFeatures = original
    assert instance.forAllFeatures == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=vM::StringExpression_strategy)
@settings(max_examples=50)
def test_vm::stringexpression_instantiation(instance):
    assert isinstance(instance, vM::StringExpression)

@given(instance=vM::StringExpression_strategy)
def test_vm::stringexpression_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=vM::StringExpression_strategy)
def test_vm::stringexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=vM::BooleanExpression_strategy)
@settings(max_examples=50)
def test_vm::booleanexpression_instantiation(instance):
    assert isinstance(instance, vM::BooleanExpression)

@given(instance=vM::BooleanExpression_strategy)
def test_vm::booleanexpression_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=vM::BooleanExpression_strategy)
def test_vm::booleanexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=vM::BooleanExpression_strategy)
def test_vm::booleanexpression_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=vM::BooleanExpression_strategy)
def test_vm::booleanexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=vM::BrackedExpression_strategy)
@settings(max_examples=50)
def test_vm::brackedexpression_instantiation(instance):
    assert isinstance(instance, vM::BrackedExpression)

@given(instance=vM::PrimitiveExpression_strategy)
@settings(max_examples=50)
def test_vm::primitiveexpression_instantiation(instance):
    assert isinstance(instance, vM::PrimitiveExpression)

@given(instance=vM::NumericExpression_strategy)
@settings(max_examples=50)
def test_vm::numericexpression_instantiation(instance):
    assert isinstance(instance, vM::NumericExpression)

@given(instance=vM::NumericExpression_strategy)
def test_vm::numericexpression_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=vM::NumericExpression_strategy)
def test_vm::numericexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=vM::NumericExpression_strategy)
def test_vm::numericexpression_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=vM::NumericExpression_strategy)
def test_vm::numericexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=vM::SpecialExpression_strategy)
@settings(max_examples=50)
def test_vm::specialexpression_instantiation(instance):
    assert isinstance(instance, vM::SpecialExpression)

@given(instance=vM::SpecialExpression_strategy)
def test_vm::specialexpression_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=vM::SpecialExpression_strategy)
def test_vm::specialexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=ComplexExpression_strategy)
@settings(max_examples=50)
def test_complexexpression_instantiation(instance):
    assert isinstance(instance, ComplexExpression)

@given(instance=vM::LeftImplication_strategy)
@settings(max_examples=50)
def test_vm::leftimplication_instantiation(instance):
    assert isinstance(instance, vM::LeftImplication)

@given(instance=vM::Inequality_strategy)
@settings(max_examples=50)
def test_vm::inequality_instantiation(instance):
    assert isinstance(instance, vM::Inequality)

@given(instance=vM::Plus_strategy)
@settings(max_examples=50)
def test_vm::plus_instantiation(instance):
    assert isinstance(instance, vM::Plus)

@given(instance=vM::RightImplication_strategy)
@settings(max_examples=50)
def test_vm::rightimplication_instantiation(instance):
    assert isinstance(instance, vM::RightImplication)

@given(instance=vM::Or_strategy)
@settings(max_examples=50)
def test_vm::or_instantiation(instance):
    assert isinstance(instance, vM::Or)

@given(instance=vM::Less_strategy)
@settings(max_examples=50)
def test_vm::less_instantiation(instance):
    assert isinstance(instance, vM::Less)

@given(instance=vM::Excludes_strategy)
@settings(max_examples=50)
def test_vm::excludes_instantiation(instance):
    assert isinstance(instance, vM::Excludes)

@given(instance=vM::Equality_strategy)
@settings(max_examples=50)
def test_vm::equality_instantiation(instance):
    assert isinstance(instance, vM::Equality)

@given(instance=vM::Lessequal_strategy)
@settings(max_examples=50)
def test_vm::lessequal_instantiation(instance):
    assert isinstance(instance, vM::Lessequal)

@given(instance=vM::BiImplication_strategy)
@settings(max_examples=50)
def test_vm::biimplication_instantiation(instance):
    assert isinstance(instance, vM::BiImplication)

@given(instance=vM::Greater_strategy)
@settings(max_examples=50)
def test_vm::greater_instantiation(instance):
    assert isinstance(instance, vM::Greater)

@given(instance=vM::Minus_strategy)
@settings(max_examples=50)
def test_vm::minus_instantiation(instance):
    assert isinstance(instance, vM::Minus)

@given(instance=vM::Greaterequal_strategy)
@settings(max_examples=50)
def test_vm::greaterequal_instantiation(instance):
    assert isinstance(instance, vM::Greaterequal)

@given(instance=vM::Requires_strategy)
@settings(max_examples=50)
def test_vm::requires_instantiation(instance):
    assert isinstance(instance, vM::Requires)

@given(instance=vM::Multiplication_strategy)
@settings(max_examples=50)
def test_vm::multiplication_instantiation(instance):
    assert isinstance(instance, vM::Multiplication)

@given(instance=vM::Division_strategy)
@settings(max_examples=50)
def test_vm::division_instantiation(instance):
    assert isinstance(instance, vM::Division)

@given(instance=vM::If_strategy)
@settings(max_examples=50)
def test_vm::if_instantiation(instance):
    assert isinstance(instance, vM::If)

@given(instance=vM::And_strategy)
@settings(max_examples=50)
def test_vm::and_instantiation(instance):
    assert isinstance(instance, vM::And)

@given(instance=vM::Expression_strategy)
@settings(max_examples=50)
def test_vm::expression_instantiation(instance):
    assert isinstance(instance, vM::Expression)

@given(instance=vM::ComplexExpression_strategy)
@settings(max_examples=50)
def test_vm::complexexpression_instantiation(instance):
    assert isinstance(instance, vM::ComplexExpression)

@given(instance=vM::Constraint_strategy)
@settings(max_examples=50)
def test_vm::constraint_instantiation(instance):
    assert isinstance(instance, vM::Constraint)

@given(instance=vM::Constraint_strategy)
def test_vm::constraint_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=vM::Constraint_strategy)
def test_vm::constraint_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=vM::Abstract::ATT::ID_strategy)
@settings(max_examples=50)
def test_vm::abstract::att::id_instantiation(instance):
    assert isinstance(instance, vM::Abstract::ATT::ID)

@given(instance=vM::Abstract::ATT::ID_strategy)
def test_vm::abstract::att::id_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=vM::Abstract::ATT::ID_strategy)
def test_vm::abstract::att::id_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=vM::AttributeDescription_strategy)
@settings(max_examples=50)
def test_vm::attributedescription_instantiation(instance):
    assert isinstance(instance, vM::AttributeDescription)

@given(instance=vM::AttributeDescription_strategy)
def test_vm::attributedescription_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=vM::AttributeDescription_strategy)
def test_vm::attributedescription_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=vM::FeatureDescription_strategy)
@settings(max_examples=50)
def test_vm::featuredescription_instantiation(instance):
    assert isinstance(instance, vM::FeatureDescription)

@given(instance=vM::FeatureDescription_strategy)
def test_vm::featuredescription_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=vM::FeatureDescription_strategy)
def test_vm::featuredescription_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=vM::IntegerAttrDefComplement_strategy)
@settings(max_examples=50)
def test_vm::integerattrdefcomplement_instantiation(instance):
    assert isinstance(instance, vM::IntegerAttrDefComplement)

@given(instance=vM::IntegerAttrDefComplement_strategy)
def test_vm::integerattrdefcomplement_min_type(instance):
    assert isinstance(instance.min, str)


@given(instance=vM::IntegerAttrDefComplement_strategy)
def test_vm::integerattrdefcomplement_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original

@given(instance=vM::IntegerAttrDefComplement_strategy)
def test_vm::integerattrdefcomplement_max_type(instance):
    assert isinstance(instance.max, str)


@given(instance=vM::IntegerAttrDefComplement_strategy)
def test_vm::integerattrdefcomplement_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original

@given(instance=vM::Enum::Real::ATT::ID_strategy)
@settings(max_examples=50)
def test_vm::enum::real::att::id_instantiation(instance):
    assert isinstance(instance, vM::Enum::Real::ATT::ID)

@given(instance=vM::Enum::Integer::ATT::ID_strategy)
@settings(max_examples=50)
def test_vm::enum::integer::att::id_instantiation(instance):
    assert isinstance(instance, vM::Enum::Integer::ATT::ID)

@given(instance=vM::Enum::String::ATT::ID_strategy)
@settings(max_examples=50)
def test_vm::enum::string::att::id_instantiation(instance):
    assert isinstance(instance, vM::Enum::String::ATT::ID)

@given(instance=EnumAttrDef_strategy)
@settings(max_examples=50)
def test_enumattrdef_instantiation(instance):
    assert isinstance(instance, EnumAttrDef)

@given(instance=vM::EnumIntegerDef_strategy)
@settings(max_examples=50)
def test_vm::enumintegerdef_instantiation(instance):
    assert isinstance(instance, vM::EnumIntegerDef)

@given(instance=vM::EnumRealDef_strategy)
@settings(max_examples=50)
def test_vm::enumrealdef_instantiation(instance):
    assert isinstance(instance, vM::EnumRealDef)

@given(instance=vM::EnumStringDef_strategy)
@settings(max_examples=50)
def test_vm::enumstringdef_instantiation(instance):
    assert isinstance(instance, vM::EnumStringDef)

@given(instance=vM::RealDeltaDef_strategy)
@settings(max_examples=50)
def test_vm::realdeltadef_instantiation(instance):
    assert isinstance(instance, vM::RealDeltaDef)

@given(instance=vM::RealDeltaDef_strategy)
def test_vm::realdeltadef_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=vM::RealDeltaDef_strategy)
def test_vm::realdeltadef_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=vM::RealAttrDefComplement_strategy)
@settings(max_examples=50)
def test_vm::realattrdefcomplement_instantiation(instance):
    assert isinstance(instance, vM::RealAttrDefComplement)

@given(instance=vM::RealAttrDefComplement_strategy)
def test_vm::realattrdefcomplement_max_type(instance):
    assert isinstance(instance.max, str)


@given(instance=vM::RealAttrDefComplement_strategy)
def test_vm::realattrdefcomplement_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original

@given(instance=vM::RealAttrDefComplement_strategy)
def test_vm::realattrdefcomplement_min_type(instance):
    assert isinstance(instance.min, str)


@given(instance=vM::RealAttrDefComplement_strategy)
def test_vm::realattrdefcomplement_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original

@given(instance=RealAttrDef_strategy)
@settings(max_examples=50)
def test_realattrdef_instantiation(instance):
    assert isinstance(instance, RealAttrDef)

@given(instance=vM::RealAttrDefUnbounded_strategy)
@settings(max_examples=50)
def test_vm::realattrdefunbounded_instantiation(instance):
    assert isinstance(instance, vM::RealAttrDefUnbounded)

@given(instance=vM::RealAttrDefUnbounded_strategy)
def test_vm::realattrdefunbounded_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=vM::RealAttrDefUnbounded_strategy)
def test_vm::realattrdefunbounded_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=vM::RealAttrDefBounded_strategy)
@settings(max_examples=50)
def test_vm::realattrdefbounded_instantiation(instance):
    assert isinstance(instance, vM::RealAttrDefBounded)

@given(instance=vM::RealDefaultDef_strategy)
@settings(max_examples=50)
def test_vm::realdefaultdef_instantiation(instance):
    assert isinstance(instance, vM::RealDefaultDef)

@given(instance=vM::RealDefaultDef_strategy)
def test_vm::realdefaultdef_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=vM::RealDefaultDef_strategy)
def test_vm::realdefaultdef_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=vM::Real::ATT::ID_strategy)
@settings(max_examples=50)
def test_vm::real::att::id_instantiation(instance):
    assert isinstance(instance, vM::Real::ATT::ID)

@given(instance=vM::IntegerDeltaDef_strategy)
@settings(max_examples=50)
def test_vm::integerdeltadef_instantiation(instance):
    assert isinstance(instance, vM::IntegerDeltaDef)

@given(instance=vM::IntegerDeltaDef_strategy)
def test_vm::integerdeltadef_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=vM::IntegerDeltaDef_strategy)
def test_vm::integerdeltadef_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=vM::FeatureDefinition_strategy)
@settings(max_examples=50)
def test_vm::featuredefinition_instantiation(instance):
    assert isinstance(instance, vM::FeatureDefinition)

@given(instance=IntegerAttrDef_strategy)
@settings(max_examples=50)
def test_integerattrdef_instantiation(instance):
    assert isinstance(instance, IntegerAttrDef)

@given(instance=vM::IntegerAttrDefUnbounded_strategy)
@settings(max_examples=50)
def test_vm::integerattrdefunbounded_instantiation(instance):
    assert isinstance(instance, vM::IntegerAttrDefUnbounded)

@given(instance=vM::IntegerAttrDefUnbounded_strategy)
def test_vm::integerattrdefunbounded_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=vM::IntegerAttrDefUnbounded_strategy)
def test_vm::integerattrdefunbounded_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=vM::IntegerAttrDefBounded_strategy)
@settings(max_examples=50)
def test_vm::integerattrdefbounded_instantiation(instance):
    assert isinstance(instance, vM::IntegerAttrDefBounded)

@given(instance=vM::IntegerDefaultDef_strategy)
@settings(max_examples=50)
def test_vm::integerdefaultdef_instantiation(instance):
    assert isinstance(instance, vM::IntegerDefaultDef)

@given(instance=vM::IntegerDefaultDef_strategy)
def test_vm::integerdefaultdef_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=vM::IntegerDefaultDef_strategy)
def test_vm::integerdefaultdef_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=vM::Integer::ATT::ID_strategy)
@settings(max_examples=50)
def test_vm::integer::att::id_instantiation(instance):
    assert isinstance(instance, vM::Integer::ATT::ID)

@given(instance=vM::StringDefaultDef_strategy)
@settings(max_examples=50)
def test_vm::stringdefaultdef_instantiation(instance):
    assert isinstance(instance, vM::StringDefaultDef)

@given(instance=vM::StringDefaultDef_strategy)
def test_vm::stringdefaultdef_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=vM::StringDefaultDef_strategy)
def test_vm::stringdefaultdef_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=vM::String::ATT::ID_strategy)
@settings(max_examples=50)
def test_vm::string::att::id_instantiation(instance):
    assert isinstance(instance, vM::String::ATT::ID)

@given(instance=vM::BoolDefaultDef_strategy)
@settings(max_examples=50)
def test_vm::booldefaultdef_instantiation(instance):
    assert isinstance(instance, vM::BoolDefaultDef)

@given(instance=vM::BoolDefaultDef_strategy)
def test_vm::booldefaultdef_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=vM::BoolDefaultDef_strategy)
def test_vm::booldefaultdef_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=vM::Boolean::ATT::ID_strategy)
@settings(max_examples=50)
def test_vm::boolean::att::id_instantiation(instance):
    assert isinstance(instance, vM::Boolean::ATT::ID)

@given(instance=BasicAttrDef_strategy)
@settings(max_examples=50)
def test_basicattrdef_instantiation(instance):
    assert isinstance(instance, BasicAttrDef)

@given(instance=vM::StringAttrDef_strategy)
@settings(max_examples=50)
def test_vm::stringattrdef_instantiation(instance):
    assert isinstance(instance, vM::StringAttrDef)

@given(instance=vM::StringAttrDef_strategy)
def test_vm::stringattrdef_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=vM::StringAttrDef_strategy)
def test_vm::stringattrdef_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=vM::RealAttrDef_strategy)
@settings(max_examples=50)
def test_vm::realattrdef_instantiation(instance):
    assert isinstance(instance, vM::RealAttrDef)

@given(instance=vM::IntegerAttrDef_strategy)
@settings(max_examples=50)
def test_vm::integerattrdef_instantiation(instance):
    assert isinstance(instance, vM::IntegerAttrDef)

@given(instance=vM::BooleanAttrDef_strategy)
@settings(max_examples=50)
def test_vm::booleanattrdef_instantiation(instance):
    assert isinstance(instance, vM::BooleanAttrDef)

@given(instance=vM::BooleanAttrDef_strategy)
def test_vm::booleanattrdef_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=vM::BooleanAttrDef_strategy)
def test_vm::booleanattrdef_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=vM::EnumAttrDef_strategy)
@settings(max_examples=50)
def test_vm::enumattrdef_instantiation(instance):
    assert isinstance(instance, vM::EnumAttrDef)

@given(instance=vM::EnumAttrDef_strategy)
def test_vm::enumattrdef_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=vM::EnumAttrDef_strategy)
def test_vm::enumattrdef_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=vM::BasicAttrDef_strategy)
@settings(max_examples=50)
def test_vm::basicattrdef_instantiation(instance):
    assert isinstance(instance, vM::BasicAttrDef)

@given(instance=vM::BasicAttrValuation_strategy)
@settings(max_examples=50)
def test_vm::basicattrvaluation_instantiation(instance):
    assert isinstance(instance, vM::BasicAttrValuation)

@given(instance=vM::BasicAttrValuation_strategy)
def test_vm::basicattrvaluation_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=vM::BasicAttrValuation_strategy)
def test_vm::basicattrvaluation_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=vM::AttrDef_strategy)
@settings(max_examples=50)
def test_vm::attrdef_instantiation(instance):
    assert isinstance(instance, vM::AttrDef)

@given(instance=vM::AttrDef_strategy)
def test_vm::attrdef_notTranslatable_type(instance):
    assert isinstance(instance.notTranslatable, bool)


@given(instance=vM::AttrDef_strategy)
def test_vm::attrdef_notTranslatable_setter(instance):
    original = instance.notTranslatable
    instance.notTranslatable = original
    assert instance.notTranslatable == original

@given(instance=vM::AttrDef_strategy)
def test_vm::attrdef_notDecidable_type(instance):
    assert isinstance(instance.notDecidable, bool)


@given(instance=vM::AttrDef_strategy)
def test_vm::attrdef_notDecidable_setter(instance):
    original = instance.notDecidable
    instance.notDecidable = original
    assert instance.notDecidable == original

@given(instance=vM::AttrDef_strategy)
def test_vm::attrdef_runTime_type(instance):
    assert isinstance(instance.runTime, bool)


@given(instance=vM::AttrDef_strategy)
def test_vm::attrdef_runTime_setter(instance):
    original = instance.runTime
    instance.runTime = original
    assert instance.runTime == original

@given(instance=FeaturesGroup_strategy)
@settings(max_examples=50)
def test_featuresgroup_instantiation(instance):
    assert isinstance(instance, FeaturesGroup)

@given(instance=vM::CardinalityBased_strategy)
@settings(max_examples=50)
def test_vm::cardinalitybased_instantiation(instance):
    assert isinstance(instance, vM::CardinalityBased)

@given(instance=vM::CardinalityBased_strategy)
def test_vm::cardinalitybased_min_type(instance):
    assert isinstance(instance.min, str)


@given(instance=vM::CardinalityBased_strategy)
def test_vm::cardinalitybased_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original

@given(instance=vM::CardinalityBased_strategy)
def test_vm::cardinalitybased_all_type(instance):
    assert isinstance(instance.all, bool)


@given(instance=vM::CardinalityBased_strategy)
def test_vm::cardinalitybased_all_setter(instance):
    original = instance.all
    instance.all = original
    assert instance.all == original

@given(instance=vM::CardinalityBased_strategy)
def test_vm::cardinalitybased_max_type(instance):
    assert isinstance(instance.max, str)


@given(instance=vM::CardinalityBased_strategy)
def test_vm::cardinalitybased_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original

@given(instance=vM::Orgroup_strategy)
@settings(max_examples=50)
def test_vm::orgroup_instantiation(instance):
    assert isinstance(instance, vM::Orgroup)

@given(instance=vM::Xorgroup_strategy)
@settings(max_examples=50)
def test_vm::xorgroup_instantiation(instance):
    assert isinstance(instance, vM::Xorgroup)

@given(instance=FeatureDefinition_strategy)
@settings(max_examples=50)
def test_featuredefinition_instantiation(instance):
    assert isinstance(instance, FeatureDefinition)

@given(instance=vM::FeaturesGroup_strategy)
@settings(max_examples=50)
def test_vm::featuresgroup_instantiation(instance):
    assert isinstance(instance, vM::FeaturesGroup)

@given(instance=vM::Feature_strategy)
@settings(max_examples=50)
def test_vm::feature_instantiation(instance):
    assert isinstance(instance, vM::Feature)

@given(instance=vM::Feature_strategy)
def test_vm::feature_optional_type(instance):
    assert isinstance(instance.optional, bool)


@given(instance=vM::Feature_strategy)
def test_vm::feature_optional_setter(instance):
    original = instance.optional
    instance.optional = original
    assert instance.optional == original

@given(instance=vM::Feature_strategy)
def test_vm::feature_max_type(instance):
    assert isinstance(instance.max, str)


@given(instance=vM::Feature_strategy)
def test_vm::feature_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original

@given(instance=vM::Feature_strategy)
def test_vm::feature_notTranslatable_type(instance):
    assert isinstance(instance.notTranslatable, bool)


@given(instance=vM::Feature_strategy)
def test_vm::feature_notTranslatable_setter(instance):
    original = instance.notTranslatable
    instance.notTranslatable = original
    assert instance.notTranslatable == original

@given(instance=vM::Feature_strategy)
def test_vm::feature_notDecidable_type(instance):
    assert isinstance(instance.notDecidable, bool)


@given(instance=vM::Feature_strategy)
def test_vm::feature_notDecidable_setter(instance):
    original = instance.notDecidable
    instance.notDecidable = original
    assert instance.notDecidable == original

@given(instance=vM::Feature_strategy)
def test_vm::feature_runTime_type(instance):
    assert isinstance(instance.runTime, bool)


@given(instance=vM::Feature_strategy)
def test_vm::feature_runTime_setter(instance):
    original = instance.runTime
    instance.runTime = original
    assert instance.runTime == original

@given(instance=vM::Feature_strategy)
def test_vm::feature_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=vM::Feature_strategy)
def test_vm::feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=vM::Feature_strategy)
def test_vm::feature_min_type(instance):
    assert isinstance(instance.min, str)


@given(instance=vM::Feature_strategy)
def test_vm::feature_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original

@given(instance=vM::FeatureHierarchy_strategy)
@settings(max_examples=50)
def test_vm::featurehierarchy_instantiation(instance):
    assert isinstance(instance, vM::FeatureHierarchy)

@given(instance=vM::Email_strategy)
@settings(max_examples=50)
def test_vm::email_instantiation(instance):
    assert isinstance(instance, vM::Email)

@given(instance=vM::Email_strategy)
def test_vm::email_username_type(instance):
    assert isinstance(instance.username, str)


@given(instance=vM::Email_strategy)
def test_vm::email_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original

@given(instance=vM::Email_strategy)
def test_vm::email_domain_type(instance):
    assert isinstance(instance.domain, str)


@given(instance=vM::Email_strategy)
def test_vm::email_domain_setter(instance):
    original = instance.domain
    instance.domain = original
    assert instance.domain == original

@given(instance=vM::Version_strategy)
@settings(max_examples=50)
def test_vm::version_instantiation(instance):
    assert isinstance(instance, vM::Version)

@given(instance=vM::Version_strategy)
def test_vm::version_tail_type(instance):
    assert isinstance(instance.tail, int)


@given(instance=vM::Version_strategy)
def test_vm::version_tail_setter(instance):
    original = instance.tail
    instance.tail = original
    assert instance.tail == original

@given(instance=vM::Version_strategy)
def test_vm::version_main_type(instance):
    assert isinstance(instance.main, int)


@given(instance=vM::Version_strategy)
def test_vm::version_main_setter(instance):
    original = instance.main
    instance.main = original
    assert instance.main == original

@given(instance=VmBlock_strategy)
@settings(max_examples=50)
def test_vmblock_instantiation(instance):
    assert isinstance(instance, VmBlock)

@given(instance=vM::Attributes_strategy)
@settings(max_examples=50)
def test_vm::attributes_instantiation(instance):
    assert isinstance(instance, vM::Attributes)

@given(instance=vM::Objectives_strategy)
@settings(max_examples=50)
def test_vm::objectives_instantiation(instance):
    assert isinstance(instance, vM::Objectives)

@given(instance=vM::ImportDeclaration_strategy)
@settings(max_examples=50)
def test_vm::importdeclaration_instantiation(instance):
    assert isinstance(instance, vM::ImportDeclaration)

@given(instance=vM::ImportDeclaration_strategy)
def test_vm::importdeclaration_importedNamespace_type(instance):
    assert isinstance(instance.importedNamespace, str)


@given(instance=vM::ImportDeclaration_strategy)
def test_vm::importdeclaration_importedNamespace_setter(instance):
    original = instance.importedNamespace
    instance.importedNamespace = original
    assert instance.importedNamespace == original

@given(instance=vM::Configurations_strategy)
@settings(max_examples=50)
def test_vm::configurations_instantiation(instance):
    assert isinstance(instance, vM::Configurations)

@given(instance=vM::Relationships_strategy)
@settings(max_examples=50)
def test_vm::relationships_instantiation(instance):
    assert isinstance(instance, vM::Relationships)

@given(instance=vM::Descriptions_strategy)
@settings(max_examples=50)
def test_vm::descriptions_instantiation(instance):
    assert isinstance(instance, vM::Descriptions)

@given(instance=vM::MetaDataDeclaration_strategy)
@settings(max_examples=50)
def test_vm::metadatadeclaration_instantiation(instance):
    assert isinstance(instance, vM::MetaDataDeclaration)

@given(instance=vM::MetaDataDeclaration_strategy)
def test_vm::metadatadeclaration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=vM::MetaDataDeclaration_strategy)
def test_vm::metadatadeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=vM::MetaDataDeclaration_strategy)
def test_vm::metadatadeclaration_organization_type(instance):
    assert isinstance(instance.organization, str)


@given(instance=vM::MetaDataDeclaration_strategy)
def test_vm::metadatadeclaration_organization_setter(instance):
    original = instance.organization
    instance.organization = original
    assert instance.organization == original

@given(instance=vM::MetaDataDeclaration_strategy)
def test_vm::metadatadeclaration_date_type(instance):
    assert isinstance(instance.date, str)


@given(instance=vM::MetaDataDeclaration_strategy)
def test_vm::metadatadeclaration_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original

@given(instance=vM::MetaDataDeclaration_strategy)
def test_vm::metadatadeclaration_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=vM::MetaDataDeclaration_strategy)
def test_vm::metadatadeclaration_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=vM::MetaDataDeclaration_strategy)
def test_vm::metadatadeclaration_author_type(instance):
    assert isinstance(instance.author, str)


@given(instance=vM::MetaDataDeclaration_strategy)
def test_vm::metadatadeclaration_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original

@given(instance=vM::MetaDataDeclaration_strategy)
def test_vm::metadatadeclaration_publication_type(instance):
    assert isinstance(instance.publication, str)


@given(instance=vM::MetaDataDeclaration_strategy)
def test_vm::metadatadeclaration_publication_setter(instance):
    original = instance.publication
    instance.publication = original
    assert instance.publication == original

@given(instance=vM::Constraints_strategy)
@settings(max_examples=50)
def test_vm::constraints_instantiation(instance):
    assert isinstance(instance, vM::Constraints)

@given(instance=vM::PackageDeclaration_strategy)
@settings(max_examples=50)
def test_vm::packagedeclaration_instantiation(instance):
    assert isinstance(instance, vM::PackageDeclaration)

@given(instance=vM::PackageDeclaration_strategy)
def test_vm::packagedeclaration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=vM::PackageDeclaration_strategy)
def test_vm::packagedeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=vM::VmBlock_strategy)
@settings(max_examples=50)
def test_vm::vmblock_instantiation(instance):
    assert isinstance(instance, vM::VmBlock)

@given(instance=vM::Model_strategy)
@settings(max_examples=50)
def test_vm::model_instantiation(instance):
    assert isinstance(instance, vM::Model)
