import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Household::Member,
    Household::Family,
    Household::HouseholdRoot,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_household::member_is_not_abstract():
    assert not inspect.isabstract(Household::Member)


def test_household::member_constructor_exists():
    assert callable(Household::Member.__init__)


def test_household::member_constructor_args():
    sig = inspect.signature(Household::Member.__init__)
    params = list(sig.parameters.keys())
    assert "firstName" in params, "Missing parameter 'firstName'"

def test_household::member_has_firstName():
    assert hasattr(Household::Member, "firstName")
    descriptor = None
    for klass in Household::Member.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)



def test_household::family_is_not_abstract():
    assert not inspect.isabstract(Household::Family)


def test_household::family_constructor_exists():
    assert callable(Household::Family.__init__)


def test_household::family_constructor_args():
    sig = inspect.signature(Household::Family.__init__)
    params = list(sig.parameters.keys())
    assert "lastName" in params, "Missing parameter 'lastName'"

def test_household::family_has_lastName():
    assert hasattr(Household::Family, "lastName")
    descriptor = None
    for klass in Household::Family.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)



def test_household::householdroot_is_not_abstract():
    assert not inspect.isabstract(Household::HouseholdRoot)


def test_household::householdroot_constructor_exists():
    assert callable(Household::HouseholdRoot.__init__)


def test_household::householdroot_constructor_args():
    sig = inspect.signature(Household::HouseholdRoot.__init__)
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
Household::Member_strategy = st.builds(
    Household::Member,
    firstName=
        safe_text
)
Household::Family_strategy = st.builds(
    Household::Family,
    lastName=
        safe_text
)
Household::HouseholdRoot_strategy = st.builds(
    Household::HouseholdRoot,
)

@given(instance=Household::Member_strategy)
@settings(max_examples=50)
def test_household::member_instantiation(instance):
    assert isinstance(instance, Household::Member)

@given(instance=Household::Member_strategy)
def test_household::member_firstName_type(instance):
    assert isinstance(instance.firstName, str)


@given(instance=Household::Member_strategy)
def test_household::member_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original

@given(instance=Household::Family_strategy)
@settings(max_examples=50)
def test_household::family_instantiation(instance):
    assert isinstance(instance, Household::Family)

@given(instance=Household::Family_strategy)
def test_household::family_lastName_type(instance):
    assert isinstance(instance.lastName, str)


@given(instance=Household::Family_strategy)
def test_household::family_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original

@given(instance=Household::HouseholdRoot_strategy)
@settings(max_examples=50)
def test_household::householdroot_instantiation(instance):
    assert isinstance(instance, Household::HouseholdRoot)
