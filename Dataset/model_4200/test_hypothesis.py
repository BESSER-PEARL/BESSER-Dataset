import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    a_Greeting,
    a_PackageDeclaration,
    a_Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_a_greeting_is_not_abstract():
    assert not inspect.isabstract(a_Greeting)


def test_a_greeting_constructor_exists():
    assert callable(a_Greeting.__init__)


def test_a_greeting_constructor_args():
    sig = inspect.signature(a_Greeting.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_a_greeting_has_name():
    assert hasattr(a_Greeting, "name")
    descriptor = None
    for klass in a_Greeting.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_a_packagedeclaration_is_not_abstract():
    assert not inspect.isabstract(a_PackageDeclaration)


def test_a_packagedeclaration_constructor_exists():
    assert callable(a_PackageDeclaration.__init__)


def test_a_packagedeclaration_constructor_args():
    sig = inspect.signature(a_PackageDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_a_packagedeclaration_has_name():
    assert hasattr(a_PackageDeclaration, "name")
    descriptor = None
    for klass in a_PackageDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_a_model_is_not_abstract():
    assert not inspect.isabstract(a_Model)


def test_a_model_constructor_exists():
    assert callable(a_Model.__init__)


def test_a_model_constructor_args():
    sig = inspect.signature(a_Model.__init__)
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
a_Greeting_strategy = st.builds(
    a_Greeting,
    name=
        safe_text
)
a_PackageDeclaration_strategy = st.builds(
    a_PackageDeclaration,
    name=
        safe_text
)
a_Model_strategy = st.builds(
    a_Model,
)

@given(instance=a_Greeting_strategy)
@settings(max_examples=50)
def test_a_greeting_instantiation(instance):
    assert isinstance(instance, a_Greeting)



@given(instance=a_Greeting_strategy)
def test_a_greeting_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=a_PackageDeclaration_strategy)
@settings(max_examples=50)
def test_a_packagedeclaration_instantiation(instance):
    assert isinstance(instance, a_PackageDeclaration)



@given(instance=a_PackageDeclaration_strategy)
def test_a_packagedeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=a_Model_strategy)
@settings(max_examples=50)
def test_a_model_instantiation(instance):
    assert isinstance(instance, a_Model)
