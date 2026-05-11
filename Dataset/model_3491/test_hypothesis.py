import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Feature,
    featureDiagram::PrimitiveFeature,
    featureDiagram::EObject,
    featureDiagram::FeatureElement,
    Constraint,
    featureDiagram::Mutex,
    featureDiagram::Require,
    Operator,
    featureDiagram::Alternative,
    featureDiagram::Mandatory,
    featureDiagram::Card,
    featureDiagram::Or,
    featureDiagram::Opt,
    FeatureElement,
    featureDiagram::Attribute,
    featureDiagram::Operator,
    featureDiagram::ConstraintEdge,
    featureDiagram::Constraint,
    featureDiagram::Feature,
    featureDiagram::FeatureDiagram,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



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



def test_featurediagram::eobject_is_not_abstract():
    assert not inspect.isabstract(featureDiagram::EObject)


def test_featurediagram::eobject_constructor_exists():
    assert callable(featureDiagram::EObject.__init__)


def test_featurediagram::eobject_constructor_args():
    sig = inspect.signature(featureDiagram::EObject.__init__)
    params = list(sig.parameters.keys())



def test_featurediagram::featureelement_is_not_abstract():
    assert not inspect.isabstract(featureDiagram::FeatureElement)


def test_featurediagram::featureelement_constructor_exists():
    assert callable(featureDiagram::FeatureElement.__init__)


def test_featurediagram::featureelement_constructor_args():
    sig = inspect.signature(featureDiagram::FeatureElement.__init__)
    params = list(sig.parameters.keys())



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



def test_operator_is_not_abstract():
    assert not inspect.isabstract(Operator)


def test_operator_constructor_exists():
    assert callable(Operator.__init__)


def test_operator_constructor_args():
    sig = inspect.signature(Operator.__init__)
    params = list(sig.parameters.keys())



def test_featurediagram::alternative_is_not_abstract():
    assert not inspect.isabstract(featureDiagram::Alternative)


def test_featurediagram::alternative_constructor_exists():
    assert callable(featureDiagram::Alternative.__init__)


def test_featurediagram::alternative_constructor_args():
    sig = inspect.signature(featureDiagram::Alternative.__init__)
    params = list(sig.parameters.keys())



def test_featurediagram::mandatory_is_not_abstract():
    assert not inspect.isabstract(featureDiagram::Mandatory)


def test_featurediagram::mandatory_constructor_exists():
    assert callable(featureDiagram::Mandatory.__init__)


def test_featurediagram::mandatory_constructor_args():
    sig = inspect.signature(featureDiagram::Mandatory.__init__)
    params = list(sig.parameters.keys())



def test_featurediagram::card_is_not_abstract():
    assert not inspect.isabstract(featureDiagram::Card)


def test_featurediagram::card_constructor_exists():
    assert callable(featureDiagram::Card.__init__)


def test_featurediagram::card_constructor_args():
    sig = inspect.signature(featureDiagram::Card.__init__)
    params = list(sig.parameters.keys())
    assert "min" in params, "Missing parameter 'min'"
    assert "max" in params, "Missing parameter 'max'"

def test_featurediagram::card_has_min():
    assert hasattr(featureDiagram::Card, "min")
    descriptor = None
    for klass in featureDiagram::Card.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)

def test_featurediagram::card_has_max():
    assert hasattr(featureDiagram::Card, "max")
    descriptor = None
    for klass in featureDiagram::Card.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
            break
    assert isinstance(descriptor, property)



def test_featurediagram::or_is_not_abstract():
    assert not inspect.isabstract(featureDiagram::Or)


def test_featurediagram::or_constructor_exists():
    assert callable(featureDiagram::Or.__init__)


def test_featurediagram::or_constructor_args():
    sig = inspect.signature(featureDiagram::Or.__init__)
    params = list(sig.parameters.keys())



def test_featurediagram::opt_is_not_abstract():
    assert not inspect.isabstract(featureDiagram::Opt)


def test_featurediagram::opt_constructor_exists():
    assert callable(featureDiagram::Opt.__init__)


def test_featurediagram::opt_constructor_args():
    sig = inspect.signature(featureDiagram::Opt.__init__)
    params = list(sig.parameters.keys())



def test_featureelement_is_not_abstract():
    assert not inspect.isabstract(FeatureElement)


def test_featureelement_constructor_exists():
    assert callable(FeatureElement.__init__)


def test_featureelement_constructor_args():
    sig = inspect.signature(FeatureElement.__init__)
    params = list(sig.parameters.keys())



def test_featurediagram::attribute_is_not_abstract():
    assert not inspect.isabstract(featureDiagram::Attribute)


def test_featurediagram::attribute_constructor_exists():
    assert callable(featureDiagram::Attribute.__init__)


def test_featurediagram::attribute_constructor_args():
    sig = inspect.signature(featureDiagram::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"
    assert "type" in params, "Missing parameter 'type'"

def test_featurediagram::attribute_has_name():
    assert hasattr(featureDiagram::Attribute, "name")
    descriptor = None
    for klass in featureDiagram::Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_featurediagram::attribute_has_value():
    assert hasattr(featureDiagram::Attribute, "value")
    descriptor = None
    for klass in featureDiagram::Attribute.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_featurediagram::attribute_has_type():
    assert hasattr(featureDiagram::Attribute, "type")
    descriptor = None
    for klass in featureDiagram::Attribute.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_featurediagram::operator_is_not_abstract():
    assert not inspect.isabstract(featureDiagram::Operator)


def test_featurediagram::operator_constructor_exists():
    assert callable(featureDiagram::Operator.__init__)


def test_featurediagram::operator_constructor_args():
    sig = inspect.signature(featureDiagram::Operator.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_featurediagram::operator_has_name():
    assert hasattr(featureDiagram::Operator, "name")
    descriptor = None
    for klass in featureDiagram::Operator.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_featurediagram::constraintedge_is_not_abstract():
    assert not inspect.isabstract(featureDiagram::ConstraintEdge)


def test_featurediagram::constraintedge_constructor_exists():
    assert callable(featureDiagram::ConstraintEdge.__init__)


def test_featurediagram::constraintedge_constructor_args():
    sig = inspect.signature(featureDiagram::ConstraintEdge.__init__)
    params = list(sig.parameters.keys())



def test_featurediagram::constraint_is_not_abstract():
    assert not inspect.isabstract(featureDiagram::Constraint)


def test_featurediagram::constraint_constructor_exists():
    assert callable(featureDiagram::Constraint.__init__)


def test_featurediagram::constraint_constructor_args():
    sig = inspect.signature(featureDiagram::Constraint.__init__)
    params = list(sig.parameters.keys())



def test_featurediagram::feature_is_not_abstract():
    assert not inspect.isabstract(featureDiagram::Feature)


def test_featurediagram::feature_constructor_exists():
    assert callable(featureDiagram::Feature.__init__)


def test_featurediagram::feature_constructor_args():
    sig = inspect.signature(featureDiagram::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "selected" in params, "Missing parameter 'selected'"
    assert "name" in params, "Missing parameter 'name'"

def test_featurediagram::feature_has_selected():
    assert hasattr(featureDiagram::Feature, "selected")
    descriptor = None
    for klass in featureDiagram::Feature.__mro__:
        if "selected" in klass.__dict__:
            descriptor = klass.__dict__["selected"]
            break
    assert isinstance(descriptor, property)

def test_featurediagram::feature_has_name():
    assert hasattr(featureDiagram::Feature, "name")
    descriptor = None
    for klass in featureDiagram::Feature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



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
Feature_strategy = st.builds(
    Feature,
)
featureDiagram::PrimitiveFeature_strategy = st.builds(
    featureDiagram::PrimitiveFeature,
)
featureDiagram::EObject_strategy = st.builds(
    featureDiagram::EObject,
)
featureDiagram::FeatureElement_strategy = st.builds(
    featureDiagram::FeatureElement,
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
Operator_strategy = st.builds(
    Operator,
)
featureDiagram::Alternative_strategy = st.builds(
    featureDiagram::Alternative,
)
featureDiagram::Mandatory_strategy = st.builds(
    featureDiagram::Mandatory,
)
featureDiagram::Card_strategy = st.builds(
    featureDiagram::Card,
    min=
        st.integers(),
    max=
        st.integers()
)
featureDiagram::Or_strategy = st.builds(
    featureDiagram::Or,
)
featureDiagram::Opt_strategy = st.builds(
    featureDiagram::Opt,
)
FeatureElement_strategy = st.builds(
    FeatureElement,
)
featureDiagram::Attribute_strategy = st.builds(
    featureDiagram::Attribute,
    name=
        safe_text,
    value=
        safe_text,
    type=
        safe_text
)
featureDiagram::Operator_strategy = st.builds(
    featureDiagram::Operator,
    name=
        safe_text
)
featureDiagram::ConstraintEdge_strategy = st.builds(
    featureDiagram::ConstraintEdge,
)
featureDiagram::Constraint_strategy = st.builds(
    featureDiagram::Constraint,
)
featureDiagram::Feature_strategy = st.builds(
    featureDiagram::Feature,
    selected=
        st.booleans(),
    name=
        safe_text
)
featureDiagram::FeatureDiagram_strategy = st.builds(
    featureDiagram::FeatureDiagram,
    graphTypeTree=
        st.booleans()
)

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=featureDiagram::PrimitiveFeature_strategy)
@settings(max_examples=50)
def test_featurediagram::primitivefeature_instantiation(instance):
    assert isinstance(instance, featureDiagram::PrimitiveFeature)

@given(instance=featureDiagram::EObject_strategy)
@settings(max_examples=50)
def test_featurediagram::eobject_instantiation(instance):
    assert isinstance(instance, featureDiagram::EObject)

@given(instance=featureDiagram::FeatureElement_strategy)
@settings(max_examples=50)
def test_featurediagram::featureelement_instantiation(instance):
    assert isinstance(instance, featureDiagram::FeatureElement)

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

@given(instance=Operator_strategy)
@settings(max_examples=50)
def test_operator_instantiation(instance):
    assert isinstance(instance, Operator)

@given(instance=featureDiagram::Alternative_strategy)
@settings(max_examples=50)
def test_featurediagram::alternative_instantiation(instance):
    assert isinstance(instance, featureDiagram::Alternative)

@given(instance=featureDiagram::Mandatory_strategy)
@settings(max_examples=50)
def test_featurediagram::mandatory_instantiation(instance):
    assert isinstance(instance, featureDiagram::Mandatory)

@given(instance=featureDiagram::Card_strategy)
@settings(max_examples=50)
def test_featurediagram::card_instantiation(instance):
    assert isinstance(instance, featureDiagram::Card)

@given(instance=featureDiagram::Card_strategy)
def test_featurediagram::card_min_type(instance):
    assert isinstance(instance.min, int)


@given(instance=featureDiagram::Card_strategy)
def test_featurediagram::card_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original

@given(instance=featureDiagram::Card_strategy)
def test_featurediagram::card_max_type(instance):
    assert isinstance(instance.max, int)


@given(instance=featureDiagram::Card_strategy)
def test_featurediagram::card_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original

@given(instance=featureDiagram::Or_strategy)
@settings(max_examples=50)
def test_featurediagram::or_instantiation(instance):
    assert isinstance(instance, featureDiagram::Or)

@given(instance=featureDiagram::Opt_strategy)
@settings(max_examples=50)
def test_featurediagram::opt_instantiation(instance):
    assert isinstance(instance, featureDiagram::Opt)

@given(instance=FeatureElement_strategy)
@settings(max_examples=50)
def test_featureelement_instantiation(instance):
    assert isinstance(instance, FeatureElement)

@given(instance=featureDiagram::Attribute_strategy)
@settings(max_examples=50)
def test_featurediagram::attribute_instantiation(instance):
    assert isinstance(instance, featureDiagram::Attribute)

@given(instance=featureDiagram::Attribute_strategy)
def test_featurediagram::attribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=featureDiagram::Attribute_strategy)
def test_featurediagram::attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=featureDiagram::Attribute_strategy)
def test_featurediagram::attribute_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=featureDiagram::Attribute_strategy)
def test_featurediagram::attribute_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=featureDiagram::Attribute_strategy)
def test_featurediagram::attribute_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=featureDiagram::Attribute_strategy)
def test_featurediagram::attribute_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=featureDiagram::Operator_strategy)
@settings(max_examples=50)
def test_featurediagram::operator_instantiation(instance):
    assert isinstance(instance, featureDiagram::Operator)

@given(instance=featureDiagram::Operator_strategy)
def test_featurediagram::operator_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=featureDiagram::Operator_strategy)
def test_featurediagram::operator_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=featureDiagram::ConstraintEdge_strategy)
@settings(max_examples=50)
def test_featurediagram::constraintedge_instantiation(instance):
    assert isinstance(instance, featureDiagram::ConstraintEdge)

@given(instance=featureDiagram::Constraint_strategy)
@settings(max_examples=50)
def test_featurediagram::constraint_instantiation(instance):
    assert isinstance(instance, featureDiagram::Constraint)

@given(instance=featureDiagram::Feature_strategy)
@settings(max_examples=50)
def test_featurediagram::feature_instantiation(instance):
    assert isinstance(instance, featureDiagram::Feature)

@given(instance=featureDiagram::Feature_strategy)
def test_featurediagram::feature_selected_type(instance):
    assert isinstance(instance.selected, bool)


@given(instance=featureDiagram::Feature_strategy)
def test_featurediagram::feature_selected_setter(instance):
    original = instance.selected
    instance.selected = original
    assert instance.selected == original

@given(instance=featureDiagram::Feature_strategy)
def test_featurediagram::feature_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=featureDiagram::Feature_strategy)
def test_featurediagram::feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=featureDiagram::FeatureDiagram_strategy)
@settings(max_examples=50)
def test_featurediagram::featurediagram_instantiation(instance):
    assert isinstance(instance, featureDiagram::FeatureDiagram)

@given(instance=featureDiagram::FeatureDiagram_strategy)
def test_featurediagram::featurediagram_graphTypeTree_type(instance):
    assert isinstance(instance.graphTypeTree, bool)


@given(instance=featureDiagram::FeatureDiagram_strategy)
def test_featurediagram::featurediagram_graphTypeTree_setter(instance):
    original = instance.graphTypeTree
    instance.graphTypeTree = original
    assert instance.graphTypeTree == original
