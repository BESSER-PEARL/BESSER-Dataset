import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    family::Person,
    family::Family,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_family::person_is_not_abstract():
    assert not inspect.isabstract(family::Person)


def test_family::person_constructor_exists():
    assert callable(family::Person.__init__)


def test_family::person_constructor_args():
    sig = inspect.signature(family::Person.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "male" in params, "Missing parameter 'male'"

def test_family::person_has_name():
    assert hasattr(family::Person, "name")
    descriptor = None
    for klass in family::Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_family::person_has_male():
    assert hasattr(family::Person, "male")
    descriptor = None
    for klass in family::Person.__mro__:
        if "male" in klass.__dict__:
            descriptor = klass.__dict__["male"]
            break
    assert isinstance(descriptor, property)



def test_family::family_is_not_abstract():
    assert not inspect.isabstract(family::Family)


def test_family::family_constructor_exists():
    assert callable(family::Family.__init__)


def test_family::family_constructor_args():
    sig = inspect.signature(family::Family.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_family::family_has_name():
    assert hasattr(family::Family, "name")
    descriptor = None
    for klass in family::Family.__mro__:
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
family::Person_strategy = st.builds(
    family::Person,
    name=
        safe_text,
    male=
        st.booleans()
)
family::Family_strategy = st.builds(
    family::Family,
    name=
        safe_text
)

@given(instance=family::Person_strategy)
@settings(max_examples=50)
def test_family::person_instantiation(instance):
    assert isinstance(instance, family::Person)

@given(instance=family::Person_strategy)
def test_family::person_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=family::Person_strategy)
def test_family::person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=family::Person_strategy)
def test_family::person_male_type(instance):
    assert isinstance(instance.male, bool)


@given(instance=family::Person_strategy)
def test_family::person_male_setter(instance):
    original = instance.male
    instance.male = original
    assert instance.male == original

@given(instance=family::Family_strategy)
@settings(max_examples=50)
def test_family::family_instantiation(instance):
    assert isinstance(instance, family::Family)

@given(instance=family::Family_strategy)
def test_family::family_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=family::Family_strategy)
def test_family::family_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
