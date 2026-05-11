import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    MemberToPerson,
    Families2Persons::Member2Female,
    Families2Persons::Member2Male,
    Families2Persons::Person,
    Families2Persons::Member,
    Families2Persons::MemberToPerson,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_membertoperson_is_not_abstract():
    assert not inspect.isabstract(MemberToPerson)


def test_membertoperson_constructor_exists():
    assert callable(MemberToPerson.__init__)


def test_membertoperson_constructor_args():
    sig = inspect.signature(MemberToPerson.__init__)
    params = list(sig.parameters.keys())



def test_families2persons::member2female_is_not_abstract():
    assert not inspect.isabstract(Families2Persons::Member2Female)


def test_families2persons::member2female_constructor_exists():
    assert callable(Families2Persons::Member2Female.__init__)


def test_families2persons::member2female_constructor_args():
    sig = inspect.signature(Families2Persons::Member2Female.__init__)
    params = list(sig.parameters.keys())



def test_families2persons::member2male_is_not_abstract():
    assert not inspect.isabstract(Families2Persons::Member2Male)


def test_families2persons::member2male_constructor_exists():
    assert callable(Families2Persons::Member2Male.__init__)


def test_families2persons::member2male_constructor_args():
    sig = inspect.signature(Families2Persons::Member2Male.__init__)
    params = list(sig.parameters.keys())



def test_families2persons::person_is_not_abstract():
    assert not inspect.isabstract(Families2Persons::Person)


def test_families2persons::person_constructor_exists():
    assert callable(Families2Persons::Person.__init__)


def test_families2persons::person_constructor_args():
    sig = inspect.signature(Families2Persons::Person.__init__)
    params = list(sig.parameters.keys())



def test_families2persons::member_is_not_abstract():
    assert not inspect.isabstract(Families2Persons::Member)


def test_families2persons::member_constructor_exists():
    assert callable(Families2Persons::Member.__init__)


def test_families2persons::member_constructor_args():
    sig = inspect.signature(Families2Persons::Member.__init__)
    params = list(sig.parameters.keys())



def test_families2persons::membertoperson_is_not_abstract():
    assert not inspect.isabstract(Families2Persons::MemberToPerson)


def test_families2persons::membertoperson_constructor_exists():
    assert callable(Families2Persons::MemberToPerson.__init__)


def test_families2persons::membertoperson_constructor_args():
    sig = inspect.signature(Families2Persons::MemberToPerson.__init__)
    params = list(sig.parameters.keys())
    assert "firstName" in params, "Missing parameter 'firstName'"
    assert "familyName" in params, "Missing parameter 'familyName'"

def test_families2persons::membertoperson_has_firstName():
    assert hasattr(Families2Persons::MemberToPerson, "firstName")
    descriptor = None
    for klass in Families2Persons::MemberToPerson.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)

def test_families2persons::membertoperson_has_familyName():
    assert hasattr(Families2Persons::MemberToPerson, "familyName")
    descriptor = None
    for klass in Families2Persons::MemberToPerson.__mro__:
        if "familyName" in klass.__dict__:
            descriptor = klass.__dict__["familyName"]
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
MemberToPerson_strategy = st.builds(
    MemberToPerson,
)
Families2Persons::Member2Female_strategy = st.builds(
    Families2Persons::Member2Female,
)
Families2Persons::Member2Male_strategy = st.builds(
    Families2Persons::Member2Male,
)
Families2Persons::Person_strategy = st.builds(
    Families2Persons::Person,
)
Families2Persons::Member_strategy = st.builds(
    Families2Persons::Member,
)
Families2Persons::MemberToPerson_strategy = st.builds(
    Families2Persons::MemberToPerson,
    firstName=
        safe_text,
    familyName=
        safe_text
)

@given(instance=MemberToPerson_strategy)
@settings(max_examples=50)
def test_membertoperson_instantiation(instance):
    assert isinstance(instance, MemberToPerson)

@given(instance=Families2Persons::Member2Female_strategy)
@settings(max_examples=50)
def test_families2persons::member2female_instantiation(instance):
    assert isinstance(instance, Families2Persons::Member2Female)

@given(instance=Families2Persons::Member2Male_strategy)
@settings(max_examples=50)
def test_families2persons::member2male_instantiation(instance):
    assert isinstance(instance, Families2Persons::Member2Male)

@given(instance=Families2Persons::Person_strategy)
@settings(max_examples=50)
def test_families2persons::person_instantiation(instance):
    assert isinstance(instance, Families2Persons::Person)

@given(instance=Families2Persons::Member_strategy)
@settings(max_examples=50)
def test_families2persons::member_instantiation(instance):
    assert isinstance(instance, Families2Persons::Member)

@given(instance=Families2Persons::MemberToPerson_strategy)
@settings(max_examples=50)
def test_families2persons::membertoperson_instantiation(instance):
    assert isinstance(instance, Families2Persons::MemberToPerson)

@given(instance=Families2Persons::MemberToPerson_strategy)
def test_families2persons::membertoperson_firstName_type(instance):
    assert isinstance(instance.firstName, str)


@given(instance=Families2Persons::MemberToPerson_strategy)
def test_families2persons::membertoperson_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original

@given(instance=Families2Persons::MemberToPerson_strategy)
def test_families2persons::membertoperson_familyName_type(instance):
    assert isinstance(instance.familyName, str)


@given(instance=Families2Persons::MemberToPerson_strategy)
def test_families2persons::membertoperson_familyName_setter(instance):
    original = instance.familyName
    instance.familyName = original
    assert instance.familyName == original
