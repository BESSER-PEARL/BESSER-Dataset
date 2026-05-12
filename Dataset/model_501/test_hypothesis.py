import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Families_Member,
    Families_Family,
    Member,
    Families_Mother,
    Families_Daughter,
    Families_Son,
    Families_Father,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



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



def test_member_is_not_abstract():
    assert not inspect.isabstract(Member)


def test_member_constructor_exists():
    assert callable(Member.__init__)


def test_member_constructor_args():
    sig = inspect.signature(Member.__init__)
    params = list(sig.parameters.keys())



def test_families_mother_is_not_abstract():
    assert not inspect.isabstract(Families_Mother)


def test_families_mother_constructor_exists():
    assert callable(Families_Mother.__init__)


def test_families_mother_constructor_args():
    sig = inspect.signature(Families_Mother.__init__)
    params = list(sig.parameters.keys())



def test_families_daughter_is_not_abstract():
    assert not inspect.isabstract(Families_Daughter)


def test_families_daughter_constructor_exists():
    assert callable(Families_Daughter.__init__)


def test_families_daughter_constructor_args():
    sig = inspect.signature(Families_Daughter.__init__)
    params = list(sig.parameters.keys())



def test_families_son_is_not_abstract():
    assert not inspect.isabstract(Families_Son)


def test_families_son_constructor_exists():
    assert callable(Families_Son.__init__)


def test_families_son_constructor_args():
    sig = inspect.signature(Families_Son.__init__)
    params = list(sig.parameters.keys())



def test_families_father_is_not_abstract():
    assert not inspect.isabstract(Families_Father)


def test_families_father_constructor_exists():
    assert callable(Families_Father.__init__)


def test_families_father_constructor_args():
    sig = inspect.signature(Families_Father.__init__)
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
Families_Member_strategy = st.builds(
    Families_Member,
    firstName=
        safe_text
)
Families_Family_strategy = st.builds(
    Families_Family,
    lastName=
        safe_text
)
Member_strategy = st.builds(
    Member,
)
Families_Mother_strategy = st.builds(
    Families_Mother,
)
Families_Daughter_strategy = st.builds(
    Families_Daughter,
)
Families_Son_strategy = st.builds(
    Families_Son,
)
Families_Father_strategy = st.builds(
    Families_Father,
)

@given(instance=Families_Member_strategy)
@settings(max_examples=50)
def test_families_member_instantiation(instance):
    assert isinstance(instance, Families_Member)



@given(instance=Families_Member_strategy)
def test_families_member_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original

@given(instance=Families_Family_strategy)
@settings(max_examples=50)
def test_families_family_instantiation(instance):
    assert isinstance(instance, Families_Family)



@given(instance=Families_Family_strategy)
def test_families_family_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original

@given(instance=Member_strategy)
@settings(max_examples=50)
def test_member_instantiation(instance):
    assert isinstance(instance, Member)

@given(instance=Families_Mother_strategy)
@settings(max_examples=50)
def test_families_mother_instantiation(instance):
    assert isinstance(instance, Families_Mother)

@given(instance=Families_Daughter_strategy)
@settings(max_examples=50)
def test_families_daughter_instantiation(instance):
    assert isinstance(instance, Families_Daughter)

@given(instance=Families_Son_strategy)
@settings(max_examples=50)
def test_families_son_instantiation(instance):
    assert isinstance(instance, Families_Son)

@given(instance=Families_Father_strategy)
@settings(max_examples=50)
def test_families_father_instantiation(instance):
    assert isinstance(instance, Families_Father)
