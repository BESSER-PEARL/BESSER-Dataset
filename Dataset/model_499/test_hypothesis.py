import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    families::FamilyModel,
    families::Member,
    families::Family,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_families::familymodel_is_not_abstract():
    assert not inspect.isabstract(families::FamilyModel)


def test_families::familymodel_constructor_exists():
    assert callable(families::FamilyModel.__init__)


def test_families::familymodel_constructor_args():
    sig = inspect.signature(families::FamilyModel.__init__)
    params = list(sig.parameters.keys())



def test_families::member_is_not_abstract():
    assert not inspect.isabstract(families::Member)


def test_families::member_constructor_exists():
    assert callable(families::Member.__init__)


def test_families::member_constructor_args():
    sig = inspect.signature(families::Member.__init__)
    params = list(sig.parameters.keys())
    assert "age" in params, "Missing parameter 'age'"
    assert "firstName" in params, "Missing parameter 'firstName'"

def test_families::member_has_age():
    assert hasattr(families::Member, "age")
    descriptor = None
    for klass in families::Member.__mro__:
        if "age" in klass.__dict__:
            descriptor = klass.__dict__["age"]
            break
    assert isinstance(descriptor, property)

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
    assert "town" in params, "Missing parameter 'town'"
    assert "lastName" in params, "Missing parameter 'lastName'"
    assert "street" in params, "Missing parameter 'street'"

def test_families::family_has_town():
    assert hasattr(families::Family, "town")
    descriptor = None
    for klass in families::Family.__mro__:
        if "town" in klass.__dict__:
            descriptor = klass.__dict__["town"]
            break
    assert isinstance(descriptor, property)

def test_families::family_has_lastName():
    assert hasattr(families::Family, "lastName")
    descriptor = None
    for klass in families::Family.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)

def test_families::family_has_street():
    assert hasattr(families::Family, "street")
    descriptor = None
    for klass in families::Family.__mro__:
        if "street" in klass.__dict__:
            descriptor = klass.__dict__["street"]
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
families::FamilyModel_strategy = st.builds(
    families::FamilyModel,
)
families::Member_strategy = st.builds(
    families::Member,
    age=
        st.integers(),
    firstName=
        safe_text
)
families::Family_strategy = st.builds(
    families::Family,
    town=
        safe_text,
    lastName=
        safe_text,
    street=
        safe_text
)

@given(instance=families::FamilyModel_strategy)
@settings(max_examples=50)
def test_families::familymodel_instantiation(instance):
    assert isinstance(instance, families::FamilyModel)

@given(instance=families::Member_strategy)
@settings(max_examples=50)
def test_families::member_instantiation(instance):
    assert isinstance(instance, families::Member)

@given(instance=families::Member_strategy)
def test_families::member_age_type(instance):
    assert isinstance(instance.age, int)


@given(instance=families::Member_strategy)
def test_families::member_age_setter(instance):
    original = instance.age
    instance.age = original
    assert instance.age == original

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
def test_families::family_town_type(instance):
    assert isinstance(instance.town, str)


@given(instance=families::Family_strategy)
def test_families::family_town_setter(instance):
    original = instance.town
    instance.town = original
    assert instance.town == original

@given(instance=families::Family_strategy)
def test_families::family_lastName_type(instance):
    assert isinstance(instance.lastName, str)


@given(instance=families::Family_strategy)
def test_families::family_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original

@given(instance=families::Family_strategy)
def test_families::family_street_type(instance):
    assert isinstance(instance.street, str)


@given(instance=families::Family_strategy)
def test_families::family_street_setter(instance):
    original = instance.street
    instance.street = original
    assert instance.street == original
