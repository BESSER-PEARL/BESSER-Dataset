import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    family_Person,
    family_Family,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_family_person_is_not_abstract():
    assert not inspect.isabstract(family_Person)


def test_family_person_constructor_exists():
    assert callable(family_Person.__init__)


def test_family_person_constructor_args():
    sig = inspect.signature(family_Person.__init__)
    params = list(sig.parameters.keys())
    assert "age" in params, "Missing parameter 'age'"

def test_family_person_has_age():
    assert hasattr(family_Person, "age")
    descriptor = None
    for klass in family_Person.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
            break
    assert isinstance(descriptor, property)



def test_family_family_is_not_abstract():
    assert not inspect.isabstract(family_Family)


def test_family_family_constructor_exists():
    assert callable(family_Family.__init__)


def test_family_family_constructor_args():
    sig = inspect.signature(family_Family.__init__)
    params = list(sig.parameters.keys())
    assert "memberCount" in params, "Missing parameter 'memberCount'"
    assert "averageAge" in params, "Missing parameter 'averageAge'"

def test_family_family_has_memberCount():
    assert hasattr(family_Family, "memberCount")
    descriptor = None
    for klass in family_Family.__mro__:
        if "memberCount" in klass.__dict__:
            descriptor = klass.__dict__["memberCount"]
            break
    assert isinstance(descriptor, property)

def test_family_family_has_averageAge():
    assert hasattr(family_Family, "averageAge")
    descriptor = None
    for klass in family_Family.__mro__:
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
family_Person_strategy = st.builds(
    family_Person,
    age=
        st.integers()
)
family_Family_strategy = st.builds(
    family_Family,
    memberCount=
        st.integers(),
    averageAge=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)

@given(instance=family_Person_strategy)
@settings(max_examples=50)
def test_family_person_instantiation(instance):
    assert isinstance(instance, family_Person)



@given(instance=family_Person_strategy)
def test_family_person_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original

@given(instance=family_Family_strategy)
@settings(max_examples=50)
def test_family_family_instantiation(instance):
    assert isinstance(instance, family_Family)



@given(instance=family_Family_strategy)
def test_family_family_memberCount_setter(instance):
    original = instance.memberCount
    instance.memberCount = original
    assert instance.memberCount == original



@given(instance=family_Family_strategy)
def test_family_family_averageAge_setter(instance):
    original = instance.averageAge
    instance.averageAge = original
    assert instance.averageAge == original
