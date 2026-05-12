import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Families_Member,
    Families_Family,
    Families_FamilyRegistry,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_families_member_is_not_abstract():
    assert not inspect.isabstract(Families_Member)


def test_families_member_constructor_exists():
    assert callable(Families_Member.__init__)


def test_families_member_constructor_args():
    sig = inspect.signature(Families_Member.__init__)
    params = list(sig.parameters.keys())
    assert "age" in params, "Missing parameter 'age'"
    assert "firstName" in params, "Missing parameter 'firstName'"

def test_families_member_has_age():
    assert hasattr(Families_Member, "age")
    descriptor = None
    for klass in Families_Member.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
            break
    assert isinstance(descriptor, property)

def test_families_member_has_firstName():
    assert hasattr(Families_Member, "firstName")
    descriptor = None
    for klass in Families_Member.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)



def test_families_family_is_not_abstract():
    assert not inspect.isabstract(Families_Family)


def test_families_family_constructor_exists():
    assert callable(Families_Family.__init__)


def test_families_family_constructor_args():
    sig = inspect.signature(Families_Family.__init__)
    params = list(sig.parameters.keys())
    assert "lastName" in params, "Missing parameter 'lastName'"
    assert "address" in params, "Missing parameter 'address'"

def test_families_family_has_lastName():
    assert hasattr(Families_Family, "lastName")
    descriptor = None
    for klass in Families_Family.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)

def test_families_family_has_address():
    assert hasattr(Families_Family, "address")
    descriptor = None
    for klass in Families_Family.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)



def test_families_familyregistry_is_not_abstract():
    assert not inspect.isabstract(Families_FamilyRegistry)


def test_families_familyregistry_constructor_exists():
    assert callable(Families_FamilyRegistry.__init__)


def test_families_familyregistry_constructor_args():
    sig = inspect.signature(Families_FamilyRegistry.__init__)
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
Families_Member_strategy = st.builds(
    Families_Member,
    age=
        st.integers(),
    firstName=
        safe_text
)
Families_Family_strategy = st.builds(
    Families_Family,
    lastName=
        safe_text,
    address=
        safe_text
)
Families_FamilyRegistry_strategy = st.builds(
    Families_FamilyRegistry,
)

@given(instance=Families_Member_strategy)
@settings(max_examples=50)
def test_families_member_instantiation(instance):
    assert isinstance(instance, Families_Member)



@given(instance=Families_Member_strategy)
def test_families_member_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original



@given(instance=Families_Member_strategy)
def test_families_member_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original

@given(instance=Families_Family_strategy)
@settings(max_examples=50)
def test_families_family_instantiation(instance):
    assert isinstance(instance, Families_Family)



@given(instance=Families_Family_strategy)
def test_families_family_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original



@given(instance=Families_Family_strategy)
def test_families_family_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=Families_FamilyRegistry_strategy)
@settings(max_examples=50)
def test_families_familyregistry_instantiation(instance):
    assert isinstance(instance, Families_FamilyRegistry)
