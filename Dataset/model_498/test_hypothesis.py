import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Families_LastNameElement,
    Family,
    Member,
    LastNameElement,
    Families_Member,
    Families_Family,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_families_lastnameelement_is_not_abstract():
    assert not inspect.isabstract(Families_LastNameElement)


def test_families_lastnameelement_constructor_exists():
    assert callable(Families_LastNameElement.__init__)


def test_families_lastnameelement_constructor_args():
    sig = inspect.signature(Families_LastNameElement.__init__)
    params = list(sig.parameters.keys())
    assert "lastName" in params, "Missing parameter 'lastName'"

def test_families_lastnameelement_has_lastName():
    assert hasattr(Families_LastNameElement, "lastName")
    descriptor = None
    for klass in Families_LastNameElement.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)



def test_family_is_not_abstract():
    assert not inspect.isabstract(Family)


def test_family_constructor_exists():
    assert callable(Family.__init__)


def test_family_constructor_args():
    sig = inspect.signature(Family.__init__)
    params = list(sig.parameters.keys())



def test_member_is_not_abstract():
    assert not inspect.isabstract(Member)


def test_member_constructor_exists():
    assert callable(Member.__init__)


def test_member_constructor_args():
    sig = inspect.signature(Member.__init__)
    params = list(sig.parameters.keys())



def test_lastnameelement_is_not_abstract():
    assert not inspect.isabstract(LastNameElement)


def test_lastnameelement_constructor_exists():
    assert callable(LastNameElement.__init__)


def test_lastnameelement_constructor_args():
    sig = inspect.signature(LastNameElement.__init__)
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
Families_LastNameElement_strategy = st.builds(
    Families_LastNameElement,
    lastName=
        safe_text
)
Family_strategy = st.builds(
    Family,
)
Member_strategy = st.builds(
    Member,
)
LastNameElement_strategy = st.builds(
    LastNameElement,
)
Families_Member_strategy = st.builds(
    Families_Member,
    firstName=
        safe_text
)
Families_Family_strategy = st.builds(
    Families_Family,
)

@given(instance=Families_LastNameElement_strategy)
@settings(max_examples=50)
def test_families_lastnameelement_instantiation(instance):
    assert isinstance(instance, Families_LastNameElement)



@given(instance=Families_LastNameElement_strategy)
def test_families_lastnameelement_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original

@given(instance=Family_strategy)
@settings(max_examples=50)
def test_family_instantiation(instance):
    assert isinstance(instance, Family)

@given(instance=Member_strategy)
@settings(max_examples=50)
def test_member_instantiation(instance):
    assert isinstance(instance, Member)

@given(instance=LastNameElement_strategy)
@settings(max_examples=50)
def test_lastnameelement_instantiation(instance):
    assert isinstance(instance, LastNameElement)

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
