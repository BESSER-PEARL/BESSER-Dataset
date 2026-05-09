import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Family,
    Families::Member,
    Member,
    Families::Family,
    Person,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_family_is_not_abstract():
    assert not inspect.isabstract(Family)


def test_family_constructor_exists():
    assert callable(Family.__init__)


def test_family_constructor_args():
    sig = inspect.signature(Family.__init__)
    params = list(sig.parameters.keys())



def test_families::member_is_not_abstract():
    assert not inspect.isabstract(Families::Member)


def test_families::member_constructor_exists():
    assert callable(Families::Member.__init__)


def test_families::member_constructor_args():
    sig = inspect.signature(Families::Member.__init__)
    params = list(sig.parameters.keys())
    assert "firstName" in params, "Missing parameter 'firstName'"

def test_families::member_has_firstName():
    assert hasattr(Families::Member, "firstName")
    descriptor = None
    for klass in Families::Member.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)



def test_member_is_not_abstract():
    assert not inspect.isabstract(Member)


def test_member_constructor_exists():
    assert callable(Member.__init__)


def test_member_constructor_args():
    sig = inspect.signature(Member.__init__)
    params = list(sig.parameters.keys())



def test_families::family_is_not_abstract():
    assert not inspect.isabstract(Families::Family)


def test_families::family_constructor_exists():
    assert callable(Families::Family.__init__)


def test_families::family_constructor_args():
    sig = inspect.signature(Families::Family.__init__)
    params = list(sig.parameters.keys())
    assert "lastName" in params, "Missing parameter 'lastName'"

def test_families::family_has_lastName():
    assert hasattr(Families::Family, "lastName")
    descriptor = None
    for klass in Families::Family.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)



def test_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_person_constructor_exists():
    assert callable(Person.__init__)


def test_person_constructor_args():
    sig = inspect.signature(Person.__init__)
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
Family_strategy = st.builds(
    Family,
)
Families::Member_strategy = st.builds(
    Families::Member,
    firstName=
        safe_text
)
Member_strategy = st.builds(
    Member,
)
Families::Family_strategy = st.builds(
    Families::Family,
    lastName=
        safe_text
)
Person_strategy = st.builds(
    Person,
)

@given(instance=Family_strategy)
@settings(max_examples=50)
def test_family_instantiation(instance):
    assert isinstance(instance, Family)

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

@given(instance=Member_strategy)
@settings(max_examples=50)
def test_member_instantiation(instance):
    assert isinstance(instance, Member)

@given(instance=Families::Family_strategy)
@settings(max_examples=50)
def test_families::family_instantiation(instance):
    assert isinstance(instance, Families::Family)

@given(instance=Families::Family_strategy)
def test_families::family_lastName_type(instance):
    assert isinstance(instance.lastName, str)


@given(instance=Families::Family_strategy)
def test_families::family_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)
