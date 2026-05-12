import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Household_Member,
    Household_Family,
    Household_HouseholdRoot,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_household_member_is_not_abstract():
    assert not inspect.isabstract(Household_Member)


def test_household_member_constructor_exists():
    assert callable(Household_Member.__init__)


def test_household_member_constructor_args():
    sig = inspect.signature(Household_Member.__init__)
    params = list(sig.parameters.keys())
    assert "firstName" in params, "Missing parameter 'firstName'"

def test_household_member_has_firstName():
    assert hasattr(Household_Member, "firstName")
    descriptor = None
    for klass in Household_Member.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)



def test_household_family_is_not_abstract():
    assert not inspect.isabstract(Household_Family)


def test_household_family_constructor_exists():
    assert callable(Household_Family.__init__)


def test_household_family_constructor_args():
    sig = inspect.signature(Household_Family.__init__)
    params = list(sig.parameters.keys())
    assert "lastName" in params, "Missing parameter 'lastName'"

def test_household_family_has_lastName():
    assert hasattr(Household_Family, "lastName")
    descriptor = None
    for klass in Household_Family.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)



def test_household_householdroot_is_not_abstract():
    assert not inspect.isabstract(Household_HouseholdRoot)


def test_household_householdroot_constructor_exists():
    assert callable(Household_HouseholdRoot.__init__)


def test_household_householdroot_constructor_args():
    sig = inspect.signature(Household_HouseholdRoot.__init__)
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
Household_Member_strategy = st.builds(
    Household_Member,
    firstName=
        safe_text
)
Household_Family_strategy = st.builds(
    Household_Family,
    lastName=
        safe_text
)
Household_HouseholdRoot_strategy = st.builds(
    Household_HouseholdRoot,
)

@given(instance=Household_Member_strategy)
@settings(max_examples=50)
def test_household_member_instantiation(instance):
    assert isinstance(instance, Household_Member)



@given(instance=Household_Member_strategy)
def test_household_member_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original

@given(instance=Household_Family_strategy)
@settings(max_examples=50)
def test_household_family_instantiation(instance):
    assert isinstance(instance, Household_Family)



@given(instance=Household_Family_strategy)
def test_household_family_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original

@given(instance=Household_HouseholdRoot_strategy)
@settings(max_examples=50)
def test_household_householdroot_instantiation(instance):
    assert isinstance(instance, Household_HouseholdRoot)
