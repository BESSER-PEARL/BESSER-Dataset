import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Families::Member,
    Families::Family,
    Families::FamilyRegistry,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_families::member_is_not_abstract():
    assert not inspect.isabstract(Families::Member)


def test_families::member_constructor_exists():
    assert callable(Families::Member.__init__)


def test_families::member_constructor_args():
    sig = inspect.signature(Families::Member.__init__)
    params = list(sig.parameters.keys())
    assert "firstName" in params, "Missing parameter 'firstName'"
    assert "age" in params, "Missing parameter 'age'"

def test_families::member_has_firstName():
    assert hasattr(Families::Member, "firstName")
    descriptor = None
    for klass in Families::Member.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)

def test_families::member_has_age():
    assert hasattr(Families::Member, "age")
    descriptor = None
    for klass in Families::Member.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
            break
    assert isinstance(descriptor, property)



def test_families::family_is_not_abstract():
    assert not inspect.isabstract(Families::Family)


def test_families::family_constructor_exists():
    assert callable(Families::Family.__init__)


def test_families::family_constructor_args():
    sig = inspect.signature(Families::Family.__init__)
    params = list(sig.parameters.keys())
    assert "address" in params, "Missing parameter 'address'"
    assert "lastName" in params, "Missing parameter 'lastName'"

def test_families::family_has_address():
    assert hasattr(Families::Family, "address")
    descriptor = None
    for klass in Families::Family.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_families::family_has_lastName():
    assert hasattr(Families::Family, "lastName")
    descriptor = None
    for klass in Families::Family.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)



def test_families::familyregistry_is_not_abstract():
    assert not inspect.isabstract(Families::FamilyRegistry)


def test_families::familyregistry_constructor_exists():
    assert callable(Families::FamilyRegistry.__init__)


def test_families::familyregistry_constructor_args():
    sig = inspect.signature(Families::FamilyRegistry.__init__)
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
Families::Member_strategy = st.builds(
    Families::Member,
    firstName=
        safe_text,
    age=
        st.integers()
)
Families::Family_strategy = st.builds(
    Families::Family,
    address=
        safe_text,
    lastName=
        safe_text
)
Families::FamilyRegistry_strategy = st.builds(
    Families::FamilyRegistry,
)

@given(instance=Families::Member_strategy)
@settings(max_examples=50)
def test_families::member_instantiation(instance):
    assert isinstance(instance, Families::Member)

@given(instance=Families::Member_strategy)
def test_families::member_firstName_type(instance):
    assert isinstance(instance.firstName, str)


@given(instance=Families::Member_strategy)
def test_families::member_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original

@given(instance=Families::Member_strategy)
def test_families::member_age_type(instance):
    assert isinstance(instance.age, int)


@given(instance=Families::Member_strategy)
def test_families::member_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original

@given(instance=Families::Family_strategy)
@settings(max_examples=50)
def test_families::family_instantiation(instance):
    assert isinstance(instance, Families::Family)

@given(instance=Families::Family_strategy)
def test_families::family_address_type(instance):
    assert isinstance(instance.address, str)


@given(instance=Families::Family_strategy)
def test_families::family_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=Families::Family_strategy)
def test_families::family_lastName_type(instance):
    assert isinstance(instance.lastName, str)


@given(instance=Families::Family_strategy)
def test_families::family_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original

@given(instance=Families::FamilyRegistry_strategy)
@settings(max_examples=50)
def test_families::familyregistry_instantiation(instance):
    assert isinstance(instance, Families::FamilyRegistry)
