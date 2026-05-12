import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    features_Feature,
    features_Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_features_feature_is_not_abstract():
    assert not inspect.isabstract(features_Feature)


def test_features_feature_constructor_exists():
    assert callable(features_Feature.__init__)


def test_features_feature_constructor_args():
    sig = inspect.signature(features_Feature.__init__)
    params = list(sig.parameters.keys())
    assert "short" in params, "Missing parameter 'short'"
    assert "abstract" in params, "Missing parameter 'abstract'"
    assert "name" in params, "Missing parameter 'name'"

def test_features_feature_has_short():
    assert hasattr(features_Feature, "short")
    descriptor = None
    for klass in features_Feature.__mro__:
        if "short" in klass.__dict__:
            descriptor = klass.__dict__["short"]
            break
    assert isinstance(descriptor, property)

def test_features_feature_has_abstract():
    assert hasattr(features_Feature, "abstract")
    descriptor = None
    for klass in features_Feature.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)

def test_features_feature_has_name():
    assert hasattr(features_Feature, "name")
    descriptor = None
    for klass in features_Feature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_features_model_is_not_abstract():
    assert not inspect.isabstract(features_Model)


def test_features_model_constructor_exists():
    assert callable(features_Model.__init__)


def test_features_model_constructor_args():
    sig = inspect.signature(features_Model.__init__)
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
features_Feature_strategy = st.builds(
    features_Feature,
    short=
        safe_text,
    abstract=
        st.booleans(),
    name=
        safe_text
)
features_Model_strategy = st.builds(
    features_Model,
)

@given(instance=features_Feature_strategy)
@settings(max_examples=50)
def test_features_feature_instantiation(instance):
    assert isinstance(instance, features_Feature)



@given(instance=features_Feature_strategy)
def test_features_feature_short_setter(instance):
    original = instance.short
    instance.short = original
    assert instance.short == original



@given(instance=features_Feature_strategy)
def test_features_feature_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original



@given(instance=features_Feature_strategy)
def test_features_feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=features_Model_strategy)
@settings(max_examples=50)
def test_features_model_instantiation(instance):
    assert isinstance(instance, features_Model)
