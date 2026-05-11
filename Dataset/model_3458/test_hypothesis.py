import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    featureModel::Value,
    Alternative,
    featureModel::Exclusive,
    VariabilityElement,
    featureModel::Attribute,
    featureModel::Feature,
    featureModel::FMConstraint,
    featureModel::FeatureModel,
    featureModel::VariabilityElement,
    featureModel::IntValue,
    Feature,
    featureModel::Alternative,
    featureModel::Action,
    featureModel::Condition,
    BooleanConstraint,
    featureModel::Excludes,
    featureModel::Implies,
    FMConstraint,
    featureModel::AdaptationRule,
    featureModel::BooleanConstraint,
    ComparisonOperator,
    SelectionOperator,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_featuremodel::value_is_not_abstract():
    assert not inspect.isabstract(featureModel::Value)


def test_featuremodel::value_constructor_exists():
    assert callable(featureModel::Value.__init__)


def test_featuremodel::value_constructor_args():
    sig = inspect.signature(featureModel::Value.__init__)
    params = list(sig.parameters.keys())



def test_alternative_is_not_abstract():
    assert not inspect.isabstract(Alternative)


def test_alternative_constructor_exists():
    assert callable(Alternative.__init__)


def test_alternative_constructor_args():
    sig = inspect.signature(Alternative.__init__)
    params = list(sig.parameters.keys())



def test_featuremodel::exclusive_is_not_abstract():
    assert not inspect.isabstract(featureModel::Exclusive)


def test_featuremodel::exclusive_constructor_exists():
    assert callable(featureModel::Exclusive.__init__)


def test_featuremodel::exclusive_constructor_args():
    sig = inspect.signature(featureModel::Exclusive.__init__)
    params = list(sig.parameters.keys())



def test_variabilityelement_is_not_abstract():
    assert not inspect.isabstract(VariabilityElement)


def test_variabilityelement_constructor_exists():
    assert callable(VariabilityElement.__init__)


def test_variabilityelement_constructor_args():
    sig = inspect.signature(VariabilityElement.__init__)
    params = list(sig.parameters.keys())



def test_featuremodel::attribute_is_not_abstract():
    assert not inspect.isabstract(featureModel::Attribute)


def test_featuremodel::attribute_constructor_exists():
    assert callable(featureModel::Attribute.__init__)


def test_featuremodel::attribute_constructor_args():
    sig = inspect.signature(featureModel::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "runtime" in params, "Missing parameter 'runtime'"
    assert "name" in params, "Missing parameter 'name'"

def test_featuremodel::attribute_has_runtime():
    assert hasattr(featureModel::Attribute, "runtime")
    descriptor = None
    for klass in featureModel::Attribute.__mro__:
        if "runtime" in klass.__dict__:
            descriptor = klass.__dict__["runtime"]
            break
    assert isinstance(descriptor, property)

def test_featuremodel::attribute_has_name():
    assert hasattr(featureModel::Attribute, "name")
    descriptor = None
    for klass in featureModel::Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_featuremodel::feature_is_not_abstract():
    assert not inspect.isabstract(featureModel::Feature)


def test_featuremodel::feature_constructor_exists():
    assert callable(featureModel::Feature.__init__)


def test_featuremodel::feature_constructor_args():
    sig = inspect.signature(featureModel::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "unselected" in params, "Missing parameter 'unselected'"
    assert "mandatory" in params, "Missing parameter 'mandatory'"
    assert "name" in params, "Missing parameter 'name'"
    assert "selected" in params, "Missing parameter 'selected'"

def test_featuremodel::feature_has_unselected():
    assert hasattr(featureModel::Feature, "unselected")
    descriptor = None
    for klass in featureModel::Feature.__mro__:
        if "unselected" in klass.__dict__:
            descriptor = klass.__dict__["unselected"]
            break
    assert isinstance(descriptor, property)

def test_featuremodel::feature_has_mandatory():
    assert hasattr(featureModel::Feature, "mandatory")
    descriptor = None
    for klass in featureModel::Feature.__mro__:
        if "mandatory" in klass.__dict__:
            descriptor = klass.__dict__["mandatory"]
            break
    assert isinstance(descriptor, property)

def test_featuremodel::feature_has_name():
    assert hasattr(featureModel::Feature, "name")
    descriptor = None
    for klass in featureModel::Feature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_featuremodel::feature_has_selected():
    assert hasattr(featureModel::Feature, "selected")
    descriptor = None
    for klass in featureModel::Feature.__mro__:
        if "selected" in klass.__dict__:
            descriptor = klass.__dict__["selected"]
            break
    assert isinstance(descriptor, property)



def test_featuremodel::fmconstraint_is_not_abstract():
    assert not inspect.isabstract(featureModel::FMConstraint)


def test_featuremodel::fmconstraint_constructor_exists():
    assert callable(featureModel::FMConstraint.__init__)


def test_featuremodel::fmconstraint_constructor_args():
    sig = inspect.signature(featureModel::FMConstraint.__init__)
    params = list(sig.parameters.keys())



def test_featuremodel::featuremodel_is_not_abstract():
    assert not inspect.isabstract(featureModel::FeatureModel)


def test_featuremodel::featuremodel_constructor_exists():
    assert callable(featureModel::FeatureModel.__init__)


def test_featuremodel::featuremodel_constructor_args():
    sig = inspect.signature(featureModel::FeatureModel.__init__)
    params = list(sig.parameters.keys())



def test_featuremodel::variabilityelement_is_not_abstract():
    assert not inspect.isabstract(featureModel::VariabilityElement)


def test_featuremodel::variabilityelement_constructor_exists():
    assert callable(featureModel::VariabilityElement.__init__)


def test_featuremodel::variabilityelement_constructor_args():
    sig = inspect.signature(featureModel::VariabilityElement.__init__)
    params = list(sig.parameters.keys())



def test_featuremodel::intvalue_is_not_abstract():
    assert not inspect.isabstract(featureModel::IntValue)


def test_featuremodel::intvalue_constructor_exists():
    assert callable(featureModel::IntValue.__init__)


def test_featuremodel::intvalue_constructor_args():
    sig = inspect.signature(featureModel::IntValue.__init__)
    params = list(sig.parameters.keys())



def test_feature_is_not_abstract():
    assert not inspect.isabstract(Feature)


def test_feature_constructor_exists():
    assert callable(Feature.__init__)


def test_feature_constructor_args():
    sig = inspect.signature(Feature.__init__)
    params = list(sig.parameters.keys())



def test_featuremodel::alternative_is_not_abstract():
    assert not inspect.isabstract(featureModel::Alternative)


def test_featuremodel::alternative_constructor_exists():
    assert callable(featureModel::Alternative.__init__)


def test_featuremodel::alternative_constructor_args():
    sig = inspect.signature(featureModel::Alternative.__init__)
    params = list(sig.parameters.keys())



def test_featuremodel::action_is_not_abstract():
    assert not inspect.isabstract(featureModel::Action)


def test_featuremodel::action_constructor_exists():
    assert callable(featureModel::Action.__init__)


def test_featuremodel::action_constructor_args():
    sig = inspect.signature(featureModel::Action.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_featuremodel::action_has_type():
    assert hasattr(featureModel::Action, "type")
    descriptor = None
    for klass in featureModel::Action.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_featuremodel::condition_is_not_abstract():
    assert not inspect.isabstract(featureModel::Condition)


def test_featuremodel::condition_constructor_exists():
    assert callable(featureModel::Condition.__init__)


def test_featuremodel::condition_constructor_args():
    sig = inspect.signature(featureModel::Condition.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_featuremodel::condition_has_type():
    assert hasattr(featureModel::Condition, "type")
    descriptor = None
    for klass in featureModel::Condition.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_booleanconstraint_is_not_abstract():
    assert not inspect.isabstract(BooleanConstraint)


def test_booleanconstraint_constructor_exists():
    assert callable(BooleanConstraint.__init__)


def test_booleanconstraint_constructor_args():
    sig = inspect.signature(BooleanConstraint.__init__)
    params = list(sig.parameters.keys())



def test_featuremodel::excludes_is_not_abstract():
    assert not inspect.isabstract(featureModel::Excludes)


def test_featuremodel::excludes_constructor_exists():
    assert callable(featureModel::Excludes.__init__)


def test_featuremodel::excludes_constructor_args():
    sig = inspect.signature(featureModel::Excludes.__init__)
    params = list(sig.parameters.keys())



def test_featuremodel::implies_is_not_abstract():
    assert not inspect.isabstract(featureModel::Implies)


def test_featuremodel::implies_constructor_exists():
    assert callable(featureModel::Implies.__init__)


def test_featuremodel::implies_constructor_args():
    sig = inspect.signature(featureModel::Implies.__init__)
    params = list(sig.parameters.keys())



def test_fmconstraint_is_not_abstract():
    assert not inspect.isabstract(FMConstraint)


def test_fmconstraint_constructor_exists():
    assert callable(FMConstraint.__init__)


def test_fmconstraint_constructor_args():
    sig = inspect.signature(FMConstraint.__init__)
    params = list(sig.parameters.keys())



def test_featuremodel::adaptationrule_is_not_abstract():
    assert not inspect.isabstract(featureModel::AdaptationRule)


def test_featuremodel::adaptationrule_constructor_exists():
    assert callable(featureModel::AdaptationRule.__init__)


def test_featuremodel::adaptationrule_constructor_args():
    sig = inspect.signature(featureModel::AdaptationRule.__init__)
    params = list(sig.parameters.keys())



def test_featuremodel::booleanconstraint_is_not_abstract():
    assert not inspect.isabstract(featureModel::BooleanConstraint)


def test_featuremodel::booleanconstraint_constructor_exists():
    assert callable(featureModel::BooleanConstraint.__init__)


def test_featuremodel::booleanconstraint_constructor_args():
    sig = inspect.signature(featureModel::BooleanConstraint.__init__)
    params = list(sig.parameters.keys())

def test_comparisonoperator_exists():
    # Check that the Enumeration exists
    assert ComparisonOperator is not None

def test_comparisonoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ComparisonOperator]
    expected_literals = [
        "leq",
        "lt",
        "geq",
        "equal",
        "gt",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ComparisonOperator"

def test_selectionoperator_exists():
    # Check that the Enumeration exists
    assert SelectionOperator is not None

def test_selectionoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SelectionOperator]
    expected_literals = [
        "select",
        "deselect",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SelectionOperator"


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
featureModel::Value_strategy = st.builds(
    featureModel::Value,
)
Alternative_strategy = st.builds(
    Alternative,
)
featureModel::Exclusive_strategy = st.builds(
    featureModel::Exclusive,
)
VariabilityElement_strategy = st.builds(
    VariabilityElement,
)
featureModel::Attribute_strategy = st.builds(
    featureModel::Attribute,
    runtime=
        st.booleans(),
    name=
        safe_text
)
featureModel::Feature_strategy = st.builds(
    featureModel::Feature,
    unselected=
        st.booleans(),
    mandatory=
        st.booleans(),
    name=
        safe_text,
    selected=
        st.booleans()
)
featureModel::FMConstraint_strategy = st.builds(
    featureModel::FMConstraint,
)
featureModel::FeatureModel_strategy = st.builds(
    featureModel::FeatureModel,
)
featureModel::VariabilityElement_strategy = st.builds(
    featureModel::VariabilityElement,
)
featureModel::IntValue_strategy = st.builds(
    featureModel::IntValue,
)
Feature_strategy = st.builds(
    Feature,
)
featureModel::Alternative_strategy = st.builds(
    featureModel::Alternative,
)
featureModel::Action_strategy = st.builds(
    featureModel::Action,
    type=
        safe_text
)
featureModel::Condition_strategy = st.builds(
    featureModel::Condition,
    type=
        safe_text
)
BooleanConstraint_strategy = st.builds(
    BooleanConstraint,
)
featureModel::Excludes_strategy = st.builds(
    featureModel::Excludes,
)
featureModel::Implies_strategy = st.builds(
    featureModel::Implies,
)
FMConstraint_strategy = st.builds(
    FMConstraint,
)
featureModel::AdaptationRule_strategy = st.builds(
    featureModel::AdaptationRule,
)
featureModel::BooleanConstraint_strategy = st.builds(
    featureModel::BooleanConstraint,
)

@given(instance=featureModel::Value_strategy)
@settings(max_examples=50)
def test_featuremodel::value_instantiation(instance):
    assert isinstance(instance, featureModel::Value)

@given(instance=Alternative_strategy)
@settings(max_examples=50)
def test_alternative_instantiation(instance):
    assert isinstance(instance, Alternative)

@given(instance=featureModel::Exclusive_strategy)
@settings(max_examples=50)
def test_featuremodel::exclusive_instantiation(instance):
    assert isinstance(instance, featureModel::Exclusive)

@given(instance=VariabilityElement_strategy)
@settings(max_examples=50)
def test_variabilityelement_instantiation(instance):
    assert isinstance(instance, VariabilityElement)

@given(instance=featureModel::Attribute_strategy)
@settings(max_examples=50)
def test_featuremodel::attribute_instantiation(instance):
    assert isinstance(instance, featureModel::Attribute)

@given(instance=featureModel::Attribute_strategy)
def test_featuremodel::attribute_runtime_type(instance):
    assert isinstance(instance.runtime, bool)


@given(instance=featureModel::Attribute_strategy)
def test_featuremodel::attribute_runtime_setter(instance):
    original = instance.runtime
    instance.runtime = original
    assert instance.runtime == original

@given(instance=featureModel::Attribute_strategy)
def test_featuremodel::attribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=featureModel::Attribute_strategy)
def test_featuremodel::attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=featureModel::Feature_strategy)
@settings(max_examples=50)
def test_featuremodel::feature_instantiation(instance):
    assert isinstance(instance, featureModel::Feature)

@given(instance=featureModel::Feature_strategy)
def test_featuremodel::feature_unselected_type(instance):
    assert isinstance(instance.unselected, bool)


@given(instance=featureModel::Feature_strategy)
def test_featuremodel::feature_unselected_setter(instance):
    original = instance.unselected
    instance.unselected = original
    assert instance.unselected == original

@given(instance=featureModel::Feature_strategy)
def test_featuremodel::feature_mandatory_type(instance):
    assert isinstance(instance.mandatory, bool)


@given(instance=featureModel::Feature_strategy)
def test_featuremodel::feature_mandatory_setter(instance):
    original = instance.mandatory
    instance.mandatory = original
    assert instance.mandatory == original

@given(instance=featureModel::Feature_strategy)
def test_featuremodel::feature_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=featureModel::Feature_strategy)
def test_featuremodel::feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=featureModel::Feature_strategy)
def test_featuremodel::feature_selected_type(instance):
    assert isinstance(instance.selected, bool)


@given(instance=featureModel::Feature_strategy)
def test_featuremodel::feature_selected_setter(instance):
    original = instance.selected
    instance.selected = original
    assert instance.selected == original

@given(instance=featureModel::FMConstraint_strategy)
@settings(max_examples=50)
def test_featuremodel::fmconstraint_instantiation(instance):
    assert isinstance(instance, featureModel::FMConstraint)

@given(instance=featureModel::FeatureModel_strategy)
@settings(max_examples=50)
def test_featuremodel::featuremodel_instantiation(instance):
    assert isinstance(instance, featureModel::FeatureModel)

@given(instance=featureModel::VariabilityElement_strategy)
@settings(max_examples=50)
def test_featuremodel::variabilityelement_instantiation(instance):
    assert isinstance(instance, featureModel::VariabilityElement)

@given(instance=featureModel::IntValue_strategy)
@settings(max_examples=50)
def test_featuremodel::intvalue_instantiation(instance):
    assert isinstance(instance, featureModel::IntValue)

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=featureModel::Alternative_strategy)
@settings(max_examples=50)
def test_featuremodel::alternative_instantiation(instance):
    assert isinstance(instance, featureModel::Alternative)

@given(instance=featureModel::Action_strategy)
@settings(max_examples=50)
def test_featuremodel::action_instantiation(instance):
    assert isinstance(instance, featureModel::Action)

@given(instance=featureModel::Action_strategy)
def test_featuremodel::action_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=featureModel::Action_strategy)
def test_featuremodel::action_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=featureModel::Condition_strategy)
@settings(max_examples=50)
def test_featuremodel::condition_instantiation(instance):
    assert isinstance(instance, featureModel::Condition)

@given(instance=featureModel::Condition_strategy)
def test_featuremodel::condition_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=featureModel::Condition_strategy)
def test_featuremodel::condition_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=BooleanConstraint_strategy)
@settings(max_examples=50)
def test_booleanconstraint_instantiation(instance):
    assert isinstance(instance, BooleanConstraint)

@given(instance=featureModel::Excludes_strategy)
@settings(max_examples=50)
def test_featuremodel::excludes_instantiation(instance):
    assert isinstance(instance, featureModel::Excludes)

@given(instance=featureModel::Implies_strategy)
@settings(max_examples=50)
def test_featuremodel::implies_instantiation(instance):
    assert isinstance(instance, featureModel::Implies)

@given(instance=FMConstraint_strategy)
@settings(max_examples=50)
def test_fmconstraint_instantiation(instance):
    assert isinstance(instance, FMConstraint)

@given(instance=featureModel::AdaptationRule_strategy)
@settings(max_examples=50)
def test_featuremodel::adaptationrule_instantiation(instance):
    assert isinstance(instance, featureModel::AdaptationRule)

@given(instance=featureModel::BooleanConstraint_strategy)
@settings(max_examples=50)
def test_featuremodel::booleanconstraint_instantiation(instance):
    assert isinstance(instance, featureModel::BooleanConstraint)
