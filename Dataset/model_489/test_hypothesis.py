import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    families::Member,
    families::Family,
    families::FamilyRegister,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_families::member_is_not_abstract():
    assert not inspect.isabstract(families::Member)


def test_families::member_constructor_exists():
    assert callable(families::Member.__init__)


def test_families::member_constructor_args():
    sig = inspect.signature(families::Member.__init__)
    params = list(sig.parameters.keys())
    assert "firstName" in params, "Missing parameter 'firstName'"

def test_families::member_has_firstName():
    assert hasattr(families::Member, "firstName")
    descriptor = None
    for klass in families::Member.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)



def test_families::family_is_not_abstract():
    assert not inspect.isabstract(families::Family)


def test_families::family_constructor_exists():
    assert callable(families::Family.__init__)


def test_families::family_constructor_args():
    sig = inspect.signature(families::Family.__init__)
    params = list(sig.parameters.keys())
    assert "lastName" in params, "Missing parameter 'lastName'"

def test_families::family_has_lastName():
    assert hasattr(families::Family, "lastName")
    descriptor = None
    for klass in families::Family.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)



def test_families::familyregister_is_not_abstract():
    assert not inspect.isabstract(families::FamilyRegister)


def test_families::familyregister_constructor_exists():
    assert callable(families::FamilyRegister.__init__)


def test_families::familyregister_constructor_args():
    sig = inspect.signature(families::FamilyRegister.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_families::familyregister_has_id():
    assert hasattr(families::FamilyRegister, "id")
    descriptor = None
    for klass in families::FamilyRegister.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
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
families::Member_strategy = st.builds(
    families::Member,
    firstName=
        safe_text
)
families::Family_strategy = st.builds(
    families::Family,
    lastName=
        safe_text
)
families::FamilyRegister_strategy = st.builds(
    families::FamilyRegister,
    id=
        safe_text
)

@given(instance=families::Member_strategy)
@settings(max_examples=50)
def test_families::member_instantiation(instance):
    assert isinstance(instance, families::Member)

@given(instance=families::Member_strategy)
def test_families::member_firstName_type(instance):
    assert isinstance(instance.firstName, str)


@given(instance=families::Member_strategy)
def test_families::member_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original

@given(instance=families::Family_strategy)
@settings(max_examples=50)
def test_families::family_instantiation(instance):
    assert isinstance(instance, families::Family)

@given(instance=families::Family_strategy)
def test_families::family_lastName_type(instance):
    assert isinstance(instance.lastName, str)


@given(instance=families::Family_strategy)
def test_families::family_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original

@given(instance=families::FamilyRegister_strategy)
@settings(max_examples=50)
def test_families::familyregister_instantiation(instance):
    assert isinstance(instance, families::FamilyRegister)

@given(instance=families::FamilyRegister_strategy)
def test_families::familyregister_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=families::FamilyRegister_strategy)
def test_families::familyregister_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
