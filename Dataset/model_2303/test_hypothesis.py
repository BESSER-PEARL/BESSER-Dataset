import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    MemberToPerson,
    Families2Persons_Member2Female,
    Families2Persons_Member2Male,
    Families2Persons_Person,
    Families2Persons_Member,
    Families2Persons_MemberToPerson,
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



def test_families2persons_member2female_is_not_abstract():
    assert not inspect.isabstract(Families2Persons_Member2Female)


def test_families2persons_member2female_constructor_exists():
    assert callable(Families2Persons_Member2Female.__init__)


def test_families2persons_member2female_constructor_args():
    sig = inspect.signature(Families2Persons_Member2Female.__init__)
    params = list(sig.parameters.keys())



def test_families2persons_member2male_is_not_abstract():
    assert not inspect.isabstract(Families2Persons_Member2Male)


def test_families2persons_member2male_constructor_exists():
    assert callable(Families2Persons_Member2Male.__init__)


def test_families2persons_member2male_constructor_args():
    sig = inspect.signature(Families2Persons_Member2Male.__init__)
    params = list(sig.parameters.keys())



def test_families2persons_person_is_not_abstract():
    assert not inspect.isabstract(Families2Persons_Person)


def test_families2persons_person_constructor_exists():
    assert callable(Families2Persons_Person.__init__)


def test_families2persons_person_constructor_args():
    sig = inspect.signature(Families2Persons_Person.__init__)
    params = list(sig.parameters.keys())



def test_families2persons_member_is_not_abstract():
    assert not inspect.isabstract(Families2Persons_Member)


def test_families2persons_member_constructor_exists():
    assert callable(Families2Persons_Member.__init__)


def test_families2persons_member_constructor_args():
    sig = inspect.signature(Families2Persons_Member.__init__)
    params = list(sig.parameters.keys())



def test_families2persons_membertoperson_is_not_abstract():
    assert not inspect.isabstract(Families2Persons_MemberToPerson)


def test_families2persons_membertoperson_constructor_exists():
    assert callable(Families2Persons_MemberToPerson.__init__)


def test_families2persons_membertoperson_constructor_args():
    sig = inspect.signature(Families2Persons_MemberToPerson.__init__)
    params = list(sig.parameters.keys())
    assert "familyName" in params, "Missing parameter 'familyName'"
    assert "firstName" in params, "Missing parameter 'firstName'"

def test_families2persons_membertoperson_has_familyName():
    assert hasattr(Families2Persons_MemberToPerson, "familyName")
    descriptor = None
    for klass in Families2Persons_MemberToPerson.__mro__:
        if "familyName" in klass.__dict__:
            descriptor = klass.__dict__["familyName"]
            break
    assert isinstance(descriptor, property)

def test_families2persons_membertoperson_has_firstName():
    assert hasattr(Families2Persons_MemberToPerson, "firstName")
    descriptor = None
    for klass in Families2Persons_MemberToPerson.__mro__:
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
MemberToPerson_strategy = st.builds(
    MemberToPerson,
)
Families2Persons_Member2Female_strategy = st.builds(
    Families2Persons_Member2Female,
)
Families2Persons_Member2Male_strategy = st.builds(
    Families2Persons_Member2Male,
)
Families2Persons_Person_strategy = st.builds(
    Families2Persons_Person,
)
Families2Persons_Member_strategy = st.builds(
    Families2Persons_Member,
)
Families2Persons_MemberToPerson_strategy = st.builds(
    Families2Persons_MemberToPerson,
    familyName=
        safe_text,
    firstName=
        safe_text
)

@given(instance=MemberToPerson_strategy)
@settings(max_examples=50)
def test_membertoperson_instantiation(instance):
    assert isinstance(instance, MemberToPerson)

@given(instance=Families2Persons_Member2Female_strategy)
@settings(max_examples=50)
def test_families2persons_member2female_instantiation(instance):
    assert isinstance(instance, Families2Persons_Member2Female)

@given(instance=Families2Persons_Member2Male_strategy)
@settings(max_examples=50)
def test_families2persons_member2male_instantiation(instance):
    assert isinstance(instance, Families2Persons_Member2Male)

@given(instance=Families2Persons_Person_strategy)
@settings(max_examples=50)
def test_families2persons_person_instantiation(instance):
    assert isinstance(instance, Families2Persons_Person)

@given(instance=Families2Persons_Member_strategy)
@settings(max_examples=50)
def test_families2persons_member_instantiation(instance):
    assert isinstance(instance, Families2Persons_Member)

@given(instance=Families2Persons_MemberToPerson_strategy)
@settings(max_examples=50)
def test_families2persons_membertoperson_instantiation(instance):
    assert isinstance(instance, Families2Persons_MemberToPerson)



@given(instance=Families2Persons_MemberToPerson_strategy)
def test_families2persons_membertoperson_familyName_setter(instance):
    original = instance.familyName
    instance.familyName = original
    assert instance.familyName == original



@given(instance=Families2Persons_MemberToPerson_strategy)
def test_families2persons_membertoperson_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original
