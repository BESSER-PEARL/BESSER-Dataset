import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Families::Family,
    Families::Families,
    Families::Member,
    GenderType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_families::family_is_not_abstract():
    assert not inspect.isabstract(Families::Family)


def test_families::family_constructor_exists():
    assert callable(Families::Family.__init__)


def test_families::family_constructor_args():
    sig = inspect.signature(Families::Family.__init__)
    params = list(sig.parameters.keys())
    assert "lastname" in params, "Missing parameter 'lastname'"

def test_families::family_has_lastname():
    assert hasattr(Families::Family, "lastname")
    descriptor = None
    for klass in Families::Family.__mro__:
        if "lastname" in klass.__dict__:
            descriptor = klass.__dict__["lastname"]
            break
    assert isinstance(descriptor, property)



def test_families::families_is_not_abstract():
    assert not inspect.isabstract(Families::Families)


def test_families::families_constructor_exists():
    assert callable(Families::Families.__init__)


def test_families::families_constructor_args():
    sig = inspect.signature(Families::Families.__init__)
    params = list(sig.parameters.keys())



def test_families::member_is_not_abstract():
    assert not inspect.isabstract(Families::Member)


def test_families::member_constructor_exists():
    assert callable(Families::Member.__init__)


def test_families::member_constructor_args():
    sig = inspect.signature(Families::Member.__init__)
    params = list(sig.parameters.keys())
    assert "firstname" in params, "Missing parameter 'firstname'"
    assert "gender" in params, "Missing parameter 'gender'"

def test_families::member_has_firstname():
    assert hasattr(Families::Member, "firstname")
    descriptor = None
    for klass in Families::Member.__mro__:
        if "firstname" in klass.__dict__:
            descriptor = klass.__dict__["firstname"]
            break
    assert isinstance(descriptor, property)

def test_families::member_has_gender():
    assert hasattr(Families::Member, "gender")
    descriptor = None
    for klass in Families::Member.__mro__:
        if "gender" in klass.__dict__:
            descriptor = klass.__dict__["gender"]
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
Families::Family_strategy = st.builds(
    Families::Family,
    lastname=
        safe_text
)
Families::Families_strategy = st.builds(
    Families::Families,
)
Families::Member_strategy = st.builds(
    Families::Member,
    firstname=
        safe_text,
    gender=
        safe_text
)

@given(instance=Families::Family_strategy)
@settings(max_examples=50)
def test_families::family_instantiation(instance):
    assert isinstance(instance, Families::Family)

@given(instance=Families::Family_strategy)
def test_families::family_lastname_type(instance):
    assert isinstance(instance.lastname, str)


@given(instance=Families::Family_strategy)
def test_families::family_lastname_setter(instance):
    original = instance.lastname
    instance.lastname = original
    assert instance.lastname == original

@given(instance=Families::Families_strategy)
@settings(max_examples=50)
def test_families::families_instantiation(instance):
    assert isinstance(instance, Families::Families)

@given(instance=Families::Member_strategy)
@settings(max_examples=50)
def test_families::member_instantiation(instance):
    assert isinstance(instance, Families::Member)

@given(instance=Families::Member_strategy)
def test_families::member_firstname_type(instance):
    assert isinstance(instance.firstname, str)


@given(instance=Families::Member_strategy)
def test_families::member_firstname_setter(instance):
    original = instance.firstname
    instance.firstname = original
    assert instance.firstname == original

@given(instance=Families::Member_strategy)
def test_families::member_gender_type(instance):
    assert isinstance(instance.gender, str)


@given(instance=Families::Member_strategy)
def test_families::member_gender_setter(instance):
    original = instance.gender
    instance.gender = original
    assert instance.gender == original
