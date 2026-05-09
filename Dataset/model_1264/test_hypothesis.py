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
    assert "age" in params, "Missing parameter 'age'"

def test_family::person_has_age():
    assert hasattr(family::Person, "age")
    descriptor = None
    for klass in family::Person.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
            break
    assert isinstance(descriptor, property)



def test_family::family_is_not_abstract():
    assert not inspect.isabstract(family::Family)


def test_family::family_constructor_exists():
    assert callable(family::Family.__init__)


def test_family::family_constructor_args():
    sig = inspect.signature(family::Family.__init__)
    params = list(sig.parameters.keys())
    assert "memberCount" in params, "Missing parameter 'memberCount'"
    assert "averageAge" in params, "Missing parameter 'averageAge'"

def test_family::family_has_memberCount():
    assert hasattr(family::Family, "memberCount")
    descriptor = None
    for klass in family::Family.__mro__:
        if "memberCount" in klass.__dict__:
            descriptor = klass.__dict__["memberCount"]
            break
    assert isinstance(descriptor, property)

def test_family::family_has_averageAge():
    assert hasattr(family::Family, "averageAge")
    descriptor = None
    for klass in family::Family.__mro__:
        if "averageAge" in klass.__dict__:
            descriptor = klass.__dict__["averageAge"]
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
    age=
        st.integers()
)
family::Family_strategy = st.builds(
    family::Family,
    memberCount=
        st.integers(),
    averageAge=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)

@given(instance=family::Person_strategy)
@settings(max_examples=50)
def test_family::person_instantiation(instance):
    assert isinstance(instance, family::Person)

@given(instance=family::Person_strategy)
def test_family::person_age_type(instance):
    assert isinstance(instance.age, int)


@given(instance=family::Person_strategy)
def test_family::person_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original

@given(instance=family::Family_strategy)
@settings(max_examples=50)
def test_family::family_instantiation(instance):
    assert isinstance(instance, family::Family)

@given(instance=family::Family_strategy)
def test_family::family_memberCount_type(instance):
    assert isinstance(instance.memberCount, int)


@given(instance=family::Family_strategy)
def test_family::family_memberCount_setter(instance):
    original = instance.memberCount
    instance.memberCount = original
    assert instance.memberCount == original

@given(instance=family::Family_strategy)
def test_family::family_averageAge_type(instance):
    assert isinstance(instance.averageAge, float)


@given(instance=family::Family_strategy)
def test_family::family_averageAge_setter(instance):
    original = instance.averageAge
    instance.averageAge = original
    assert instance.averageAge == original
