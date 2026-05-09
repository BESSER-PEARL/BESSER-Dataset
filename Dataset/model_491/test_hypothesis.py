import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Member,
    Families::Family,
    Families::MemberMale,
    Family,
    Families::Member,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



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



def test_families::membermale_is_not_abstract():
    assert not inspect.isabstract(Families::MemberMale)


def test_families::membermale_constructor_exists():
    assert callable(Families::MemberMale.__init__)


def test_families::membermale_constructor_args():
    sig = inspect.signature(Families::MemberMale.__init__)
    params = list(sig.parameters.keys())
    assert "test" in params, "Missing parameter 'test'"

def test_families::membermale_has_test():
    assert hasattr(Families::MemberMale, "test")
    descriptor = None
    for klass in Families::MemberMale.__mro__:
        if "test" in klass.__dict__:
            descriptor = klass.__dict__["test"]
            break
    assert isinstance(descriptor, property)



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
Member_strategy = st.builds(
    Member,
)
Families::Family_strategy = st.builds(
    Families::Family,
    lastName=
        safe_text
)
Families::MemberMale_strategy = st.builds(
    Families::MemberMale,
    test=
        safe_text
)
Family_strategy = st.builds(
    Family,
)
Families::Member_strategy = st.builds(
    Families::Member,
    firstName=
        safe_text
)

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

@given(instance=Families::MemberMale_strategy)
@settings(max_examples=50)
def test_families::membermale_instantiation(instance):
    assert isinstance(instance, Families::MemberMale)

@given(instance=Families::MemberMale_strategy)
def test_families::membermale_test_type(instance):
    assert isinstance(instance.test, str)


@given(instance=Families::MemberMale_strategy)
def test_families::membermale_test_setter(instance):
    original = instance.test
    instance.test = original
    assert instance.test == original

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
