import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    features::Feature,
    features::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_features::feature_is_not_abstract():
    assert not inspect.isabstract(features::Feature)


def test_features::feature_constructor_exists():
    assert callable(features::Feature.__init__)


def test_features::feature_constructor_args():
    sig = inspect.signature(features::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "short" in params, "Missing parameter 'short'"
    assert "name" in params, "Missing parameter 'name'"
    assert "abstract" in params, "Missing parameter 'abstract'"

def test_features::feature_has_short():
    assert hasattr(features::Feature, "short")
    descriptor = None
    for klass in features::Feature.__mro__:
        if "short" in klass.__dict__:
            descriptor = klass.__dict__["short"]
            break
    assert isinstance(descriptor, property)

def test_features::feature_has_name():
    assert hasattr(features::Feature, "name")
    descriptor = None
    for klass in features::Feature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_features::feature_has_abstract():
    assert hasattr(features::Feature, "abstract")
    descriptor = None
    for klass in features::Feature.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)



def test_features::model_is_not_abstract():
    assert not inspect.isabstract(features::Model)


def test_features::model_constructor_exists():
    assert callable(features::Model.__init__)


def test_features::model_constructor_args():
    sig = inspect.signature(features::Model.__init__)
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
features::Feature_strategy = st.builds(
    features::Feature,
    short=
        safe_text,
    name=
        safe_text,
    abstract=
        st.booleans()
)
features::Model_strategy = st.builds(
    features::Model,
)

@given(instance=features::Feature_strategy)
@settings(max_examples=50)
def test_features::feature_instantiation(instance):
    assert isinstance(instance, features::Feature)

@given(instance=features::Feature_strategy)
def test_features::feature_short_type(instance):
    assert isinstance(instance.short, str)


@given(instance=features::Feature_strategy)
def test_features::feature_short_setter(instance):
    original = instance.short
    instance.short = original
    assert instance.short == original

@given(instance=features::Feature_strategy)
def test_features::feature_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=features::Feature_strategy)
def test_features::feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=features::Feature_strategy)
def test_features::feature_abstract_type(instance):
    assert isinstance(instance.abstract, bool)


@given(instance=features::Feature_strategy)
def test_features::feature_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original

@given(instance=features::Model_strategy)
@settings(max_examples=50)
def test_features::model_instantiation(instance):
    assert isinstance(instance, features::Model)
