import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    featureDiagram::FeatureDiagram,
    Constraint,
    featureDiagram::Mutex,
    featureDiagram::Require,
    featureDiagram::Operator,
    featureDiagram::ConstraintEdge,
    Operator,
    featureDiagram::And,
    featureDiagram::Or,
    featureDiagram::Xor,
    featureDiagram::Card,
    featureDiagram::Opt,
    featureDiagram::Constraint,
    Feature,
    featureDiagram::PrimitiveFeature,
    featureDiagram::Model,
    featureDiagram::Feature,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_featurediagram::featurediagram_is_not_abstract():
    assert not inspect.isabstract(featureDiagram::FeatureDiagram)


def test_featurediagram::featurediagram_constructor_exists():
    assert callable(featureDiagram::FeatureDiagram.__init__)


def test_featurediagram::featurediagram_constructor_args():
    sig = inspect.signature(featureDiagram::FeatureDiagram.__init__)
    params = list(sig.parameters.keys())
    assert "graphTypeTree" in params, "Missing parameter 'graphTypeTree'"

def test_featurediagram::featurediagram_has_graphTypeTree():
    assert hasattr(featureDiagram::FeatureDiagram, "graphTypeTree")
    descriptor = None
    for klass in featureDiagram::FeatureDiagram.__mro__:
        if "graphTypeTree" in klass.__dict__:
            descriptor = klass.__dict__["graphTypeTree"]
            break
    assert isinstance(descriptor, property)



def test_constraint_is_not_abstract():
    assert not inspect.isabstract(Constraint)


def test_constraint_constructor_exists():
    assert callable(Constraint.__init__)


def test_constraint_constructor_args():
    sig = inspect.signature(Constraint.__init__)
    params = list(sig.parameters.keys())



def test_featurediagram::mutex_is_not_abstract():
    assert not inspect.isabstract(featureDiagram::Mutex)


def test_featurediagram::mutex_constructor_exists():
    assert callable(featureDiagram::Mutex.__init__)


def test_featurediagram::mutex_constructor_args():
    sig = inspect.signature(featureDiagram::Mutex.__init__)
    params = list(sig.parameters.keys())



def test_featurediagram::require_is_not_abstract():
    assert not inspect.isabstract(featureDiagram::Require)


def test_featurediagram::require_constructor_exists():
    assert callable(featureDiagram::Require.__init__)


def test_featurediagram::require_constructor_args():
    sig = inspect.signature(featureDiagram::Require.__init__)
    params = list(sig.parameters.keys())



def test_featurediagram::operator_is_not_abstract():
    assert not inspect.isabstract(featureDiagram::Operator)


def test_featurediagram::operator_constructor_exists():
    assert callable(featureDiagram::Operator.__init__)


def test_featurediagram::operator_constructor_args():
    sig = inspect.signature(featureDiagram::Operator.__init__)
    params = list(sig.parameters.keys())



def test_featurediagram::constraintedge_is_not_abstract():
    assert not inspect.isabstract(featureDiagram::ConstraintEdge)


def test_featurediagram::constraintedge_constructor_exists():
    assert callable(featureDiagram::ConstraintEdge.__init__)


def test_featurediagram::constraintedge_constructor_args():
    sig = inspect.signature(featureDiagram::ConstraintEdge.__init__)
    params = list(sig.parameters.keys())



def test_operator_is_not_abstract():
    assert not inspect.isabstract(Operator)


def test_operator_constructor_exists():
    assert callable(Operator.__init__)


def test_operator_constructor_args():
    sig = inspect.signature(Operator.__init__)
    params = list(sig.parameters.keys())



def test_featurediagram::and_is_not_abstract():
    assert not inspect.isabstract(featureDiagram::And)


def test_featurediagram::and_constructor_exists():
    assert callable(featureDiagram::And.__init__)


def test_featurediagram::and_constructor_args():
    sig = inspect.signature(featureDiagram::And.__init__)
    params = list(sig.parameters.keys())



def test_featurediagram::or_is_not_abstract():
    assert not inspect.isabstract(featureDiagram::Or)


def test_featurediagram::or_constructor_exists():
    assert callable(featureDiagram::Or.__init__)


def test_featurediagram::or_constructor_args():
    sig = inspect.signature(featureDiagram::Or.__init__)
    params = list(sig.parameters.keys())



def test_featurediagram::xor_is_not_abstract():
    assert not inspect.isabstract(featureDiagram::Xor)


def test_featurediagram::xor_constructor_exists():
    assert callable(featureDiagram::Xor.__init__)


def test_featurediagram::xor_constructor_args():
    sig = inspect.signature(featureDiagram::Xor.__init__)
    params = list(sig.parameters.keys())



def test_featurediagram::card_is_not_abstract():
    assert not inspect.isabstract(featureDiagram::Card)


def test_featurediagram::card_constructor_exists():
    assert callable(featureDiagram::Card.__init__)


def test_featurediagram::card_constructor_args():
    sig = inspect.signature(featureDiagram::Card.__init__)
    params = list(sig.parameters.keys())



def test_featurediagram::opt_is_not_abstract():
    assert not inspect.isabstract(featureDiagram::Opt)


def test_featurediagram::opt_constructor_exists():
    assert callable(featureDiagram::Opt.__init__)


def test_featurediagram::opt_constructor_args():
    sig = inspect.signature(featureDiagram::Opt.__init__)
    params = list(sig.parameters.keys())



def test_featurediagram::constraint_is_not_abstract():
    assert not inspect.isabstract(featureDiagram::Constraint)


def test_featurediagram::constraint_constructor_exists():
    assert callable(featureDiagram::Constraint.__init__)


def test_featurediagram::constraint_constructor_args():
    sig = inspect.signature(featureDiagram::Constraint.__init__)
    params = list(sig.parameters.keys())



def test_feature_is_not_abstract():
    assert not inspect.isabstract(Feature)


def test_feature_constructor_exists():
    assert callable(Feature.__init__)


def test_feature_constructor_args():
    sig = inspect.signature(Feature.__init__)
    params = list(sig.parameters.keys())



def test_featurediagram::primitivefeature_is_not_abstract():
    assert not inspect.isabstract(featureDiagram::PrimitiveFeature)


def test_featurediagram::primitivefeature_constructor_exists():
    assert callable(featureDiagram::PrimitiveFeature.__init__)


def test_featurediagram::primitivefeature_constructor_args():
    sig = inspect.signature(featureDiagram::PrimitiveFeature.__init__)
    params = list(sig.parameters.keys())



def test_featurediagram::model_is_not_abstract():
    assert not inspect.isabstract(featureDiagram::Model)


def test_featurediagram::model_constructor_exists():
    assert callable(featureDiagram::Model.__init__)


def test_featurediagram::model_constructor_args():
    sig = inspect.signature(featureDiagram::Model.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_featurediagram::model_has_name():
    assert hasattr(featureDiagram::Model, "name")
    descriptor = None
    for klass in featureDiagram::Model.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_featurediagram::feature_is_not_abstract():
    assert not inspect.isabstract(featureDiagram::Feature)


def test_featurediagram::feature_constructor_exists():
    assert callable(featureDiagram::Feature.__init__)


def test_featurediagram::feature_constructor_args():
    sig = inspect.signature(featureDiagram::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "selected" in params, "Missing parameter 'selected'"
    assert "optional" in params, "Missing parameter 'optional'"

def test_featurediagram::feature_has_name():
    assert hasattr(featureDiagram::Feature, "name")
    descriptor = None
    for klass in featureDiagram::Feature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_featurediagram::feature_has_selected():
    assert hasattr(featureDiagram::Feature, "selected")
    descriptor = None
    for klass in featureDiagram::Feature.__mro__:
        if "selected" in klass.__dict__:
            descriptor = klass.__dict__["selected"]
            break
    assert isinstance(descriptor, property)

def test_featurediagram::feature_has_optional():
    assert hasattr(featureDiagram::Feature, "optional")
    descriptor = None
    for klass in featureDiagram::Feature.__mro__:
        if "optional" in klass.__dict__:
            descriptor = klass.__dict__["optional"]
            break
    assert isinstance(descriptor, property)


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
featureDiagram::FeatureDiagram_strategy = st.builds(
    featureDiagram::FeatureDiagram,
    graphTypeTree=
        safe_text
)
Constraint_strategy = st.builds(
    Constraint,
)
featureDiagram::Mutex_strategy = st.builds(
    featureDiagram::Mutex,
)
featureDiagram::Require_strategy = st.builds(
    featureDiagram::Require,
)
featureDiagram::Operator_strategy = st.builds(
    featureDiagram::Operator,
)
featureDiagram::ConstraintEdge_strategy = st.builds(
    featureDiagram::ConstraintEdge,
)
Operator_strategy = st.builds(
    Operator,
)
featureDiagram::And_strategy = st.builds(
    featureDiagram::And,
)
featureDiagram::Or_strategy = st.builds(
    featureDiagram::Or,
)
featureDiagram::Xor_strategy = st.builds(
    featureDiagram::Xor,
)
featureDiagram::Card_strategy = st.builds(
    featureDiagram::Card,
)
featureDiagram::Opt_strategy = st.builds(
    featureDiagram::Opt,
)
featureDiagram::Constraint_strategy = st.builds(
    featureDiagram::Constraint,
)
Feature_strategy = st.builds(
    Feature,
)
featureDiagram::PrimitiveFeature_strategy = st.builds(
    featureDiagram::PrimitiveFeature,
)
featureDiagram::Model_strategy = st.builds(
    featureDiagram::Model,
    name=
        safe_text
)
featureDiagram::Feature_strategy = st.builds(
    featureDiagram::Feature,
    name=
        safe_text,
    selected=
        safe_text,
    optional=
        safe_text
)

@given(instance=featureDiagram::FeatureDiagram_strategy)
@settings(max_examples=50)
def test_featurediagram::featurediagram_instantiation(instance):
    assert isinstance(instance, featureDiagram::FeatureDiagram)

@given(instance=featureDiagram::FeatureDiagram_strategy)
def test_featurediagram::featurediagram_graphTypeTree_type(instance):
    assert isinstance(instance.graphTypeTree, str)


@given(instance=featureDiagram::FeatureDiagram_strategy)
def test_featurediagram::featurediagram_graphTypeTree_setter(instance):
    original = instance.graphTypeTree
    instance.graphTypeTree = original
    assert instance.graphTypeTree == original

@given(instance=Constraint_strategy)
@settings(max_examples=50)
def test_constraint_instantiation(instance):
    assert isinstance(instance, Constraint)

@given(instance=featureDiagram::Mutex_strategy)
@settings(max_examples=50)
def test_featurediagram::mutex_instantiation(instance):
    assert isinstance(instance, featureDiagram::Mutex)

@given(instance=featureDiagram::Require_strategy)
@settings(max_examples=50)
def test_featurediagram::require_instantiation(instance):
    assert isinstance(instance, featureDiagram::Require)

@given(instance=featureDiagram::Operator_strategy)
@settings(max_examples=50)
def test_featurediagram::operator_instantiation(instance):
    assert isinstance(instance, featureDiagram::Operator)

@given(instance=featureDiagram::ConstraintEdge_strategy)
@settings(max_examples=50)
def test_featurediagram::constraintedge_instantiation(instance):
    assert isinstance(instance, featureDiagram::ConstraintEdge)

@given(instance=Operator_strategy)
@settings(max_examples=50)
def test_operator_instantiation(instance):
    assert isinstance(instance, Operator)

@given(instance=featureDiagram::And_strategy)
@settings(max_examples=50)
def test_featurediagram::and_instantiation(instance):
    assert isinstance(instance, featureDiagram::And)

@given(instance=featureDiagram::Or_strategy)
@settings(max_examples=50)
def test_featurediagram::or_instantiation(instance):
    assert isinstance(instance, featureDiagram::Or)

@given(instance=featureDiagram::Xor_strategy)
@settings(max_examples=50)
def test_featurediagram::xor_instantiation(instance):
    assert isinstance(instance, featureDiagram::Xor)

@given(instance=featureDiagram::Card_strategy)
@settings(max_examples=50)
def test_featurediagram::card_instantiation(instance):
    assert isinstance(instance, featureDiagram::Card)

@given(instance=featureDiagram::Opt_strategy)
@settings(max_examples=50)
def test_featurediagram::opt_instantiation(instance):
    assert isinstance(instance, featureDiagram::Opt)

@given(instance=featureDiagram::Constraint_strategy)
@settings(max_examples=50)
def test_featurediagram::constraint_instantiation(instance):
    assert isinstance(instance, featureDiagram::Constraint)

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=featureDiagram::PrimitiveFeature_strategy)
@settings(max_examples=50)
def test_featurediagram::primitivefeature_instantiation(instance):
    assert isinstance(instance, featureDiagram::PrimitiveFeature)

@given(instance=featureDiagram::Model_strategy)
@settings(max_examples=50)
def test_featurediagram::model_instantiation(instance):
    assert isinstance(instance, featureDiagram::Model)

@given(instance=featureDiagram::Model_strategy)
def test_featurediagram::model_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=featureDiagram::Model_strategy)
def test_featurediagram::model_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=featureDiagram::Feature_strategy)
@settings(max_examples=50)
def test_featurediagram::feature_instantiation(instance):
    assert isinstance(instance, featureDiagram::Feature)

@given(instance=featureDiagram::Feature_strategy)
def test_featurediagram::feature_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=featureDiagram::Feature_strategy)
def test_featurediagram::feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=featureDiagram::Feature_strategy)
def test_featurediagram::feature_selected_type(instance):
    assert isinstance(instance.selected, str)


@given(instance=featureDiagram::Feature_strategy)
def test_featurediagram::feature_selected_setter(instance):
    original = instance.selected
    instance.selected = original
    assert instance.selected == original

@given(instance=featureDiagram::Feature_strategy)
def test_featurediagram::feature_optional_type(instance):
    assert isinstance(instance.optional, str)


@given(instance=featureDiagram::Feature_strategy)
def test_featurediagram::feature_optional_setter(instance):
    original = instance.optional
    instance.optional = original
    assert instance.optional == original
