import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    household_Member,
    household_Family,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_household_member_is_not_abstract():
    assert not inspect.isabstract(household_Member)


def test_household_member_constructor_exists():
    assert callable(household_Member.__init__)


def test_household_member_constructor_args():
    sig = inspect.signature(household_Member.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_household_member_has_name():
    assert hasattr(household_Member, "name")
    descriptor = None
    for klass in household_Member.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_household_family_is_not_abstract():
    assert not inspect.isabstract(household_Family)


def test_household_family_constructor_exists():
    assert callable(household_Family.__init__)


def test_household_family_constructor_args():
    sig = inspect.signature(household_Family.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_household_family_has_name():
    assert hasattr(household_Family, "name")
    descriptor = None
    for klass in household_Family.__mro__:
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
household_Member_strategy = st.builds(
    household_Member,
    name=
        safe_text
)
household_Family_strategy = st.builds(
    household_Family,
    name=
        safe_text
)

@given(instance=household_Member_strategy)
@settings(max_examples=50)
def test_household_member_instantiation(instance):
    assert isinstance(instance, household_Member)



@given(instance=household_Member_strategy)
def test_household_member_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=household_Family_strategy)
@settings(max_examples=50)
def test_household_family_instantiation(instance):
    assert isinstance(instance, household_Family)



@given(instance=household_Family_strategy)
def test_household_family_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
