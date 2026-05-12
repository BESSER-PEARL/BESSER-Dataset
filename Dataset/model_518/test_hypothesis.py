import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Families_Family,
    Member,
    Families_Female,
    Families_Male,
    Families_Member,
    Families_Families,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_families_family_is_not_abstract():
    assert not inspect.isabstract(Families_Family)


def test_families_family_constructor_exists():
    assert callable(Families_Family.__init__)


def test_families_family_constructor_args():
    sig = inspect.signature(Families_Family.__init__)
    params = list(sig.parameters.keys())
    assert "lastname" in params, "Missing parameter 'lastname'"

def test_families_family_has_lastname():
    assert hasattr(Families_Family, "lastname")
    descriptor = None
    for klass in Families_Family.__mro__:
        if "lastname" in klass.__dict__:
            descriptor = klass.__dict__["lastname"]
            break
    assert isinstance(descriptor, property)



def test_member_is_not_abstract():
    assert not inspect.isabstract(Member)


def test_member_constructor_exists():
    assert callable(Member.__init__)


def test_member_constructor_args():
    sig = inspect.signature(Member.__init__)
    params = list(sig.parameters.keys())



def test_families_female_is_not_abstract():
    assert not inspect.isabstract(Families_Female)


def test_families_female_constructor_exists():
    assert callable(Families_Female.__init__)


def test_families_female_constructor_args():
    sig = inspect.signature(Families_Female.__init__)
    params = list(sig.parameters.keys())



def test_families_male_is_not_abstract():
    assert not inspect.isabstract(Families_Male)


def test_families_male_constructor_exists():
    assert callable(Families_Male.__init__)


def test_families_male_constructor_args():
    sig = inspect.signature(Families_Male.__init__)
    params = list(sig.parameters.keys())



def test_families_member_is_not_abstract():
    assert not inspect.isabstract(Families_Member)


def test_families_member_constructor_exists():
    assert callable(Families_Member.__init__)


def test_families_member_constructor_args():
    sig = inspect.signature(Families_Member.__init__)
    params = list(sig.parameters.keys())
    assert "firstname" in params, "Missing parameter 'firstname'"

def test_families_member_has_firstname():
    assert hasattr(Families_Member, "firstname")
    descriptor = None
    for klass in Families_Member.__mro__:
        if "firstname" in klass.__dict__:
            descriptor = klass.__dict__["firstname"]
            break
    assert isinstance(descriptor, property)



def test_families_families_is_not_abstract():
    assert not inspect.isabstract(Families_Families)


def test_families_families_constructor_exists():
    assert callable(Families_Families.__init__)


def test_families_families_constructor_args():
    sig = inspect.signature(Families_Families.__init__)
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
Families_Family_strategy = st.builds(
    Families_Family,
    lastname=
        safe_text
)
Member_strategy = st.builds(
    Member,
)
Families_Female_strategy = st.builds(
    Families_Female,
)
Families_Male_strategy = st.builds(
    Families_Male,
)
Families_Member_strategy = st.builds(
    Families_Member,
    firstname=
        safe_text
)
Families_Families_strategy = st.builds(
    Families_Families,
)

@given(instance=Families_Family_strategy)
@settings(max_examples=50)
def test_families_family_instantiation(instance):
    assert isinstance(instance, Families_Family)



@given(instance=Families_Family_strategy)
def test_families_family_lastname_setter(instance):
    original = instance.lastname
    instance.lastname = original
    assert instance.lastname == original

@given(instance=Member_strategy)
@settings(max_examples=50)
def test_member_instantiation(instance):
    assert isinstance(instance, Member)

@given(instance=Families_Female_strategy)
@settings(max_examples=50)
def test_families_female_instantiation(instance):
    assert isinstance(instance, Families_Female)

@given(instance=Families_Male_strategy)
@settings(max_examples=50)
def test_families_male_instantiation(instance):
    assert isinstance(instance, Families_Male)

@given(instance=Families_Member_strategy)
@settings(max_examples=50)
def test_families_member_instantiation(instance):
    assert isinstance(instance, Families_Member)



@given(instance=Families_Member_strategy)
def test_families_member_firstname_setter(instance):
    original = instance.firstname
    instance.firstname = original
    assert instance.firstname == original

@given(instance=Families_Families_strategy)
@settings(max_examples=50)
def test_families_families_instantiation(instance):
    assert isinstance(instance, Families_Families)
