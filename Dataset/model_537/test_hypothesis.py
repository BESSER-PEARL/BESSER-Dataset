import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    household::Member,
    household::Family,
    household::HouseholdRoot,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_household::member_is_not_abstract():
    assert not inspect.isabstract(household::Member)


def test_household::member_constructor_exists():
    assert callable(household::Member.__init__)


def test_household::member_constructor_args():
    sig = inspect.signature(household::Member.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_household::member_has_name():
    assert hasattr(household::Member, "name")
    descriptor = None
    for klass in household::Member.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_household::family_is_not_abstract():
    assert not inspect.isabstract(household::Family)


def test_household::family_constructor_exists():
    assert callable(household::Family.__init__)


def test_household::family_constructor_args():
    sig = inspect.signature(household::Family.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_household::family_has_name():
    assert hasattr(household::Family, "name")
    descriptor = None
    for klass in household::Family.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_household::householdroot_is_not_abstract():
    assert not inspect.isabstract(household::HouseholdRoot)


def test_household::householdroot_constructor_exists():
    assert callable(household::HouseholdRoot.__init__)


def test_household::householdroot_constructor_args():
    sig = inspect.signature(household::HouseholdRoot.__init__)
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
household::Member_strategy = st.builds(
    household::Member,
    name=
        safe_text
)
household::Family_strategy = st.builds(
    household::Family,
    name=
        safe_text
)
household::HouseholdRoot_strategy = st.builds(
    household::HouseholdRoot,
)

@given(instance=household::Member_strategy)
@settings(max_examples=50)
def test_household::member_instantiation(instance):
    assert isinstance(instance, household::Member)

@given(instance=household::Member_strategy)
def test_household::member_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=household::Member_strategy)
def test_household::member_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=household::Family_strategy)
@settings(max_examples=50)
def test_household::family_instantiation(instance):
    assert isinstance(instance, household::Family)

@given(instance=household::Family_strategy)
def test_household::family_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=household::Family_strategy)
def test_household::family_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=household::HouseholdRoot_strategy)
@settings(max_examples=50)
def test_household::householdroot_instantiation(instance):
    assert isinstance(instance, household::HouseholdRoot)
