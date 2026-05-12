import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Member,
    Families_Family,
    Families_MemberMale,
    Family,
    Families_Member,
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



def test_families_family_is_not_abstract():
    assert not inspect.isabstract(Families_Family)


def test_families_family_constructor_exists():
    assert callable(Families_Family.__init__)


def test_families_family_constructor_args():
    sig = inspect.signature(Families_Family.__init__)
    params = list(sig.parameters.keys())
    assert "lastName" in params, "Missing parameter 'lastName'"

def test_families_family_has_lastName():
    assert hasattr(Families_Family, "lastName")
    descriptor = None
    for klass in Families_Family.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)



def test_families_membermale_is_not_abstract():
    assert not inspect.isabstract(Families_MemberMale)


def test_families_membermale_constructor_exists():
    assert callable(Families_MemberMale.__init__)


def test_families_membermale_constructor_args():
    sig = inspect.signature(Families_MemberMale.__init__)
    params = list(sig.parameters.keys())
    assert "test" in params, "Missing parameter 'test'"

def test_families_membermale_has_test():
    assert hasattr(Families_MemberMale, "test")
    descriptor = None
    for klass in Families_MemberMale.__mro__:
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



def test_families_member_is_not_abstract():
    assert not inspect.isabstract(Families_Member)


def test_families_member_constructor_exists():
    assert callable(Families_Member.__init__)


def test_families_member_constructor_args():
    sig = inspect.signature(Families_Member.__init__)
    params = list(sig.parameters.keys())
    assert "firstName" in params, "Missing parameter 'firstName'"

def test_families_member_has_firstName():
    assert hasattr(Families_Member, "firstName")
    descriptor = None
    for klass in Families_Member.__mro__:
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
Families_Family_strategy = st.builds(
    Families_Family,
    lastName=
        safe_text
)
Families_MemberMale_strategy = st.builds(
    Families_MemberMale,
    test=
        safe_text
)
Family_strategy = st.builds(
    Family,
)
Families_Member_strategy = st.builds(
    Families_Member,
    firstName=
        safe_text
)

@given(instance=Member_strategy)
@settings(max_examples=50)
def test_member_instantiation(instance):
    assert isinstance(instance, Member)

@given(instance=Families_Family_strategy)
@settings(max_examples=50)
def test_families_family_instantiation(instance):
    assert isinstance(instance, Families_Family)



@given(instance=Families_Family_strategy)
def test_families_family_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original

@given(instance=Families_MemberMale_strategy)
@settings(max_examples=50)
def test_families_membermale_instantiation(instance):
    assert isinstance(instance, Families_MemberMale)



@given(instance=Families_MemberMale_strategy)
def test_families_membermale_test_setter(instance):
    original = instance.test
    instance.test = original
    assert instance.test == original

@given(instance=Family_strategy)
@settings(max_examples=50)
def test_family_instantiation(instance):
    assert isinstance(instance, Family)

@given(instance=Families_Member_strategy)
@settings(max_examples=50)
def test_families_member_instantiation(instance):
    assert isinstance(instance, Families_Member)



@given(instance=Families_Member_strategy)
def test_families_member_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original
