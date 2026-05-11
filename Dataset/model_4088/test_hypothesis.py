import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    simpleuml::Classifier,
    Classifier,
    simpleuml::Class,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_simpleuml::classifier_is_not_abstract():
    assert not inspect.isabstract(simpleuml::Classifier)


def test_simpleuml::classifier_constructor_exists():
    assert callable(simpleuml::Classifier.__init__)


def test_simpleuml::classifier_constructor_args():
    sig = inspect.signature(simpleuml::Classifier.__init__)
    params = list(sig.parameters.keys())



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_simpleuml::class_is_not_abstract():
    assert not inspect.isabstract(simpleuml::Class)


def test_simpleuml::class_constructor_exists():
    assert callable(simpleuml::Class.__init__)


def test_simpleuml::class_constructor_args():
    sig = inspect.signature(simpleuml::Class.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simpleuml::class_has_name():
    assert hasattr(simpleuml::Class, "name")
    descriptor = None
    for klass in simpleuml::Class.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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
simpleuml::Classifier_strategy = st.builds(
    simpleuml::Classifier,
)
Classifier_strategy = st.builds(
    Classifier,
)
simpleuml::Class_strategy = st.builds(
    simpleuml::Class,
    name=
        safe_text
)

@given(instance=simpleuml::Classifier_strategy)
@settings(max_examples=50)
def test_simpleuml::classifier_instantiation(instance):
    assert isinstance(instance, simpleuml::Classifier)

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=simpleuml::Class_strategy)
@settings(max_examples=50)
def test_simpleuml::class_instantiation(instance):
    assert isinstance(instance, simpleuml::Class)

@given(instance=simpleuml::Class_strategy)
def test_simpleuml::class_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simpleuml::Class_strategy)
def test_simpleuml::class_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
