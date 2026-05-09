import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    family::ecore::Family,
    family::ecore::Person,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_family::ecore::family_is_not_abstract():
    assert not inspect.isabstract(family::ecore::Family)


def test_family::ecore::family_constructor_exists():
    assert callable(family::ecore::Family.__init__)


def test_family::ecore::family_constructor_args():
    sig = inspect.signature(family::ecore::Family.__init__)
    params = list(sig.parameters.keys())



def test_family::ecore::person_is_not_abstract():
    assert not inspect.isabstract(family::ecore::Person)


def test_family::ecore::person_constructor_exists():
    assert callable(family::ecore::Person.__init__)


def test_family::ecore::person_constructor_args():
    sig = inspect.signature(family::ecore::Person.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "age" in params, "Missing parameter 'age'"

def test_family::ecore::person_has_name():
    assert hasattr(family::ecore::Person, "name")
    descriptor = None
    for klass in family::ecore::Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_family::ecore::person_has_age():
    assert hasattr(family::ecore::Person, "age")
    descriptor = None
    for klass in family::ecore::Person.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
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
family::ecore::Family_strategy = st.builds(
    family::ecore::Family,
)
family::ecore::Person_strategy = st.builds(
    family::ecore::Person,
    name=
        safe_text,
    age=
        st.integers()
)

@given(instance=family::ecore::Family_strategy)
@settings(max_examples=50)
def test_family::ecore::family_instantiation(instance):
    assert isinstance(instance, family::ecore::Family)

@given(instance=family::ecore::Person_strategy)
@settings(max_examples=50)
def test_family::ecore::person_instantiation(instance):
    assert isinstance(instance, family::ecore::Person)

@given(instance=family::ecore::Person_strategy)
def test_family::ecore::person_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=family::ecore::Person_strategy)
def test_family::ecore::person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=family::ecore::Person_strategy)
def test_family::ecore::person_age_type(instance):
    assert isinstance(instance.age, int)


@given(instance=family::ecore::Person_strategy)
def test_family::ecore::person_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original
