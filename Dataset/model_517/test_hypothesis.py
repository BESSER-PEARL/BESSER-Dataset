import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Families_Family,
    Families_Families,
    Families_Member,
    GenderType,
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



def test_families_families_is_not_abstract():
    assert not inspect.isabstract(Families_Families)


def test_families_families_constructor_exists():
    assert callable(Families_Families.__init__)


def test_families_families_constructor_args():
    sig = inspect.signature(Families_Families.__init__)
    params = list(sig.parameters.keys())



def test_families_member_is_not_abstract():
    assert not inspect.isabstract(Families_Member)


def test_families_member_constructor_exists():
    assert callable(Families_Member.__init__)


def test_families_member_constructor_args():
    sig = inspect.signature(Families_Member.__init__)
    params = list(sig.parameters.keys())
    assert "gender" in params, "Missing parameter 'gender'"
    assert "firstname" in params, "Missing parameter 'firstname'"

def test_families_member_has_gender():
    assert hasattr(Families_Member, "gender")
    descriptor = None
    for klass in Families_Member.__mro__:
        if "gender" in klass.__dict__:
            descriptor = klass.__dict__["gender"]
            break
    assert isinstance(descriptor, property)

def test_families_member_has_firstname():
    assert hasattr(Families_Member, "firstname")
    descriptor = None
    for klass in Families_Member.__mro__:
        if "firstname" in klass.__dict__:
            descriptor = klass.__dict__["firstname"]
            break
    assert isinstance(descriptor, property)

def test_gendertype_exists():
    # Check that the Enumeration exists
    assert GenderType is not None

def test_gendertype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in GenderType]
    expected_literals = [
        "female",
        "male",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in GenderType"


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
Families_Families_strategy = st.builds(
    Families_Families,
)
Families_Member_strategy = st.builds(
    Families_Member,
    gender=
        safe_text,
    firstname=
        safe_text
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

@given(instance=Families_Families_strategy)
@settings(max_examples=50)
def test_families_families_instantiation(instance):
    assert isinstance(instance, Families_Families)

@given(instance=Families_Member_strategy)
@settings(max_examples=50)
def test_families_member_instantiation(instance):
    assert isinstance(instance, Families_Member)



@given(instance=Families_Member_strategy)
def test_families_member_gender_setter(instance):
    original = instance.gender
    instance.gender = original
    assert instance.gender == original



@given(instance=Families_Member_strategy)
def test_families_member_firstname_setter(instance):
    original = instance.firstname
    instance.firstname = original
    assert instance.firstname == original
