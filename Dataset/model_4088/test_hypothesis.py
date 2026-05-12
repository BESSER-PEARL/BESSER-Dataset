import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    simpleuml_Classifier,
    Classifier,
    simpleuml_Class,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_simpleuml_classifier_is_not_abstract():
    assert not inspect.isabstract(simpleuml_Classifier)


def test_simpleuml_classifier_constructor_exists():
    assert callable(simpleuml_Classifier.__init__)


def test_simpleuml_classifier_constructor_args():
    sig = inspect.signature(simpleuml_Classifier.__init__)
    params = list(sig.parameters.keys())



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_simpleuml_class_is_not_abstract():
    assert not inspect.isabstract(simpleuml_Class)


def test_simpleuml_class_constructor_exists():
    assert callable(simpleuml_Class.__init__)


def test_simpleuml_class_constructor_args():
    sig = inspect.signature(simpleuml_Class.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simpleuml_class_has_name():
    assert hasattr(simpleuml_Class, "name")
    descriptor = None
    for klass in simpleuml_Class.__mro__:
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
simpleuml_Classifier_strategy = st.builds(
    simpleuml_Classifier,
)
Classifier_strategy = st.builds(
    Classifier,
)
simpleuml_Class_strategy = st.builds(
    simpleuml_Class,
    name=
        safe_text
)

@given(instance=simpleuml_Classifier_strategy)
@settings(max_examples=50)
def test_simpleuml_classifier_instantiation(instance):
    assert isinstance(instance, simpleuml_Classifier)

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=simpleuml_Class_strategy)
@settings(max_examples=50)
def test_simpleuml_class_instantiation(instance):
    assert isinstance(instance, simpleuml_Class)



@given(instance=simpleuml_Class_strategy)
def test_simpleuml_class_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
