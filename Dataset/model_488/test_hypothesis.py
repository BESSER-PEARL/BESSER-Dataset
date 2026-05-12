import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Family,
    Families_FamElem,
    Member,
    FamElem,
    Families_Member,
    Families_Family,
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



def test_families_famelem_is_not_abstract():
    assert not inspect.isabstract(Families_FamElem)


def test_families_famelem_constructor_exists():
    assert callable(Families_FamElem.__init__)


def test_families_famelem_constructor_args():
    sig = inspect.signature(Families_FamElem.__init__)
    params = list(sig.parameters.keys())



def test_member_is_not_abstract():
    assert not inspect.isabstract(Member)


def test_member_constructor_exists():
    assert callable(Member.__init__)


def test_member_constructor_args():
    sig = inspect.signature(Member.__init__)
    params = list(sig.parameters.keys())



def test_famelem_is_not_abstract():
    assert not inspect.isabstract(FamElem)


def test_famelem_constructor_exists():
    assert callable(FamElem.__init__)


def test_famelem_constructor_args():
    sig = inspect.signature(FamElem.__init__)
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
Families_FamElem_strategy = st.builds(
    Families_FamElem,
)
Member_strategy = st.builds(
    Member,
)
FamElem_strategy = st.builds(
    FamElem,
)
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

@given(instance=Family_strategy)
@settings(max_examples=50)
def test_family_instantiation(instance):
    assert isinstance(instance, Family)

@given(instance=Families_FamElem_strategy)
@settings(max_examples=50)
def test_families_famelem_instantiation(instance):
    assert isinstance(instance, Families_FamElem)

@given(instance=Member_strategy)
@settings(max_examples=50)
def test_member_instantiation(instance):
    assert isinstance(instance, Member)

@given(instance=FamElem_strategy)
@settings(max_examples=50)
def test_famelem_instantiation(instance):
    assert isinstance(instance, FamElem)

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
