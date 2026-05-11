import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    feature::Model,
    feature::Feature,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_feature::model_is_not_abstract():
    assert not inspect.isabstract(feature::Model)


def test_feature::model_constructor_exists():
    assert callable(feature::Model.__init__)


def test_feature::model_constructor_args():
    sig = inspect.signature(feature::Model.__init__)
    params = list(sig.parameters.keys())
    assert "features" in params, "Missing parameter 'features'"

def test_feature::model_has_features():
    assert hasattr(feature::Model, "features")
    descriptor = None
    for klass in feature::Model.__mro__:
        if "features" in klass.__dict__:
            descriptor = klass.__dict__["features"]
            break
    assert isinstance(descriptor, property)



def test_feature::feature_is_not_abstract():
    assert not inspect.isabstract(feature::Feature)


def test_feature::feature_constructor_exists():
    assert callable(feature::Feature.__init__)


def test_feature::feature_constructor_args():
    sig = inspect.signature(feature::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "min" in params, "Missing parameter 'min'"
    assert "name" in params, "Missing parameter 'name'"
    assert "attribute" in params, "Missing parameter 'attribute'"
    assert "isSelected" in params, "Missing parameter 'isSelected'"
    assert "max" in params, "Missing parameter 'max'"

def test_feature::feature_has_min():
    assert hasattr(feature::Feature, "min")
    descriptor = None
    for klass in feature::Feature.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)

def test_feature::feature_has_name():
    assert hasattr(feature::Feature, "name")
    descriptor = None
    for klass in feature::Feature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_feature::feature_has_attribute():
    assert hasattr(feature::Feature, "attribute")
    descriptor = None
    for klass in feature::Feature.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
            break
    assert isinstance(descriptor, property)

def test_feature::feature_has_isSelected():
    assert hasattr(feature::Feature, "isSelected")
    descriptor = None
    for klass in feature::Feature.__mro__:
        if "isSelected" in klass.__dict__:
            descriptor = klass.__dict__["isSelected"]
            break
    assert isinstance(descriptor, property)

def test_feature::feature_has_max():
    assert hasattr(feature::Feature, "max")
    descriptor = None
    for klass in feature::Feature.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
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
feature::Model_strategy = st.builds(
    feature::Model,
    features=
        safe_text
)
feature::Feature_strategy = st.builds(
    feature::Feature,
    min=
        st.integers(),
    name=
        safe_text,
    attribute=
        safe_text,
    isSelected=
        st.booleans(),
    max=
        st.integers()
)

@given(instance=feature::Model_strategy)
@settings(max_examples=50)
def test_feature::model_instantiation(instance):
    assert isinstance(instance, feature::Model)

@given(instance=feature::Model_strategy)
def test_feature::model_features_type(instance):
    assert isinstance(instance.features, str)


@given(instance=feature::Model_strategy)
def test_feature::model_features_setter(instance):
    original = instance.features
    instance.features = original
    assert instance.features == original

@given(instance=feature::Feature_strategy)
@settings(max_examples=50)
def test_feature::feature_instantiation(instance):
    assert isinstance(instance, feature::Feature)

@given(instance=feature::Feature_strategy)
def test_feature::feature_min_type(instance):
    assert isinstance(instance.min, int)


@given(instance=feature::Feature_strategy)
def test_feature::feature_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original

@given(instance=feature::Feature_strategy)
def test_feature::feature_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=feature::Feature_strategy)
def test_feature::feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=feature::Feature_strategy)
def test_feature::feature_attribute_type(instance):
    assert isinstance(instance.attribute, str)


@given(instance=feature::Feature_strategy)
def test_feature::feature_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original

@given(instance=feature::Feature_strategy)
def test_feature::feature_isSelected_type(instance):
    assert isinstance(instance.isSelected, bool)


@given(instance=feature::Feature_strategy)
def test_feature::feature_isSelected_setter(instance):
    original = instance.isSelected
    instance.isSelected = original
    assert instance.isSelected == original

@given(instance=feature::Feature_strategy)
def test_feature::feature_max_type(instance):
    assert isinstance(instance.max, int)


@given(instance=feature::Feature_strategy)
def test_feature::feature_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original
