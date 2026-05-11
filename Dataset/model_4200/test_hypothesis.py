import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    a::Greeting,
    a::PackageDeclaration,
    a::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_a::greeting_is_not_abstract():
    assert not inspect.isabstract(a::Greeting)


def test_a::greeting_constructor_exists():
    assert callable(a::Greeting.__init__)


def test_a::greeting_constructor_args():
    sig = inspect.signature(a::Greeting.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_a::greeting_has_name():
    assert hasattr(a::Greeting, "name")
    descriptor = None
    for klass in a::Greeting.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_a::packagedeclaration_is_not_abstract():
    assert not inspect.isabstract(a::PackageDeclaration)


def test_a::packagedeclaration_constructor_exists():
    assert callable(a::PackageDeclaration.__init__)


def test_a::packagedeclaration_constructor_args():
    sig = inspect.signature(a::PackageDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_a::packagedeclaration_has_name():
    assert hasattr(a::PackageDeclaration, "name")
    descriptor = None
    for klass in a::PackageDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_a::model_is_not_abstract():
    assert not inspect.isabstract(a::Model)


def test_a::model_constructor_exists():
    assert callable(a::Model.__init__)


def test_a::model_constructor_args():
    sig = inspect.signature(a::Model.__init__)
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
a::Greeting_strategy = st.builds(
    a::Greeting,
    name=
        safe_text
)
a::PackageDeclaration_strategy = st.builds(
    a::PackageDeclaration,
    name=
        safe_text
)
a::Model_strategy = st.builds(
    a::Model,
)

@given(instance=a::Greeting_strategy)
@settings(max_examples=50)
def test_a::greeting_instantiation(instance):
    assert isinstance(instance, a::Greeting)

@given(instance=a::Greeting_strategy)
def test_a::greeting_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=a::Greeting_strategy)
def test_a::greeting_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=a::PackageDeclaration_strategy)
@settings(max_examples=50)
def test_a::packagedeclaration_instantiation(instance):
    assert isinstance(instance, a::PackageDeclaration)

@given(instance=a::PackageDeclaration_strategy)
def test_a::packagedeclaration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=a::PackageDeclaration_strategy)
def test_a::packagedeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=a::Model_strategy)
@settings(max_examples=50)
def test_a::model_instantiation(instance):
    assert isinstance(instance, a::Model)
