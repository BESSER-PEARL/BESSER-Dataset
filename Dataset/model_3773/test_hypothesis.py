import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    feature_Model,
    feature_Feature,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_feature_model_is_not_abstract():
    assert not inspect.isabstract(feature_Model)


def test_feature_model_constructor_exists():
    assert callable(feature_Model.__init__)


def test_feature_model_constructor_args():
    sig = inspect.signature(feature_Model.__init__)
    params = list(sig.parameters.keys())
    assert "features" in params, "Missing parameter 'features'"

def test_feature_model_has_features():
    assert hasattr(feature_Model, "features")
    descriptor = None
    for klass in feature_Model.__mro__:
        if "features" in klass.__dict__:
            descriptor = klass.__dict__["features"]
            break
    assert isinstance(descriptor, property)



def test_feature_feature_is_not_abstract():
    assert not inspect.isabstract(feature_Feature)


def test_feature_feature_constructor_exists():
    assert callable(feature_Feature.__init__)


def test_feature_feature_constructor_args():
    sig = inspect.signature(feature_Feature.__init__)
    params = list(sig.parameters.keys())
    assert "min" in params, "Missing parameter 'min'"
    assert "attribute" in params, "Missing parameter 'attribute'"
    assert "max" in params, "Missing parameter 'max'"
    assert "name" in params, "Missing parameter 'name'"
    assert "isSelected" in params, "Missing parameter 'isSelected'"

def test_feature_feature_has_min():
    assert hasattr(feature_Feature, "min")
    descriptor = None
    for klass in feature_Feature.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)

def test_feature_feature_has_attribute():
    assert hasattr(feature_Feature, "attribute")
    descriptor = None
    for klass in feature_Feature.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
            break
    assert isinstance(descriptor, property)

def test_feature_feature_has_max():
    assert hasattr(feature_Feature, "max")
    descriptor = None
    for klass in feature_Feature.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
            break
    assert isinstance(descriptor, property)

def test_feature_feature_has_name():
    assert hasattr(feature_Feature, "name")
    descriptor = None
    for klass in feature_Feature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_feature_feature_has_isSelected():
    assert hasattr(feature_Feature, "isSelected")
    descriptor = None
    for klass in feature_Feature.__mro__:
        if "isSelected" in klass.__dict__:
            descriptor = klass.__dict__["isSelected"]
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
feature_Model_strategy = st.builds(
    feature_Model,
    features=
        safe_text
)
feature_Feature_strategy = st.builds(
    feature_Feature,
    min=
        st.integers(),
    attribute=
        safe_text,
    max=
        st.integers(),
    name=
        safe_text,
    isSelected=
        st.booleans()
)

@given(instance=feature_Model_strategy)
@settings(max_examples=50)
def test_feature_model_instantiation(instance):
    assert isinstance(instance, feature_Model)



@given(instance=feature_Model_strategy)
def test_feature_model_features_setter(instance):
    original = instance.features
    instance.features = original
    assert instance.features == original

@given(instance=feature_Feature_strategy)
@settings(max_examples=50)
def test_feature_feature_instantiation(instance):
    assert isinstance(instance, feature_Feature)



@given(instance=feature_Feature_strategy)
def test_feature_feature_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original



@given(instance=feature_Feature_strategy)
def test_feature_feature_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original



@given(instance=feature_Feature_strategy)
def test_feature_feature_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original



@given(instance=feature_Feature_strategy)
def test_feature_feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=feature_Feature_strategy)
def test_feature_feature_isSelected_setter(instance):
    original = instance.isSelected
    instance.isSelected = original
    assert instance.isSelected == original
