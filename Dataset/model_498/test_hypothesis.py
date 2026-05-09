import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Families::LastNameElement,
    Family,
    Member,
    LastNameElement,
    Families::Member,
    Families::Family,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_families::lastnameelement_is_not_abstract():
    assert not inspect.isabstract(Families::LastNameElement)


def test_families::lastnameelement_constructor_exists():
    assert callable(Families::LastNameElement.__init__)


def test_families::lastnameelement_constructor_args():
    sig = inspect.signature(Families::LastNameElement.__init__)
    params = list(sig.parameters.keys())
    assert "lastName" in params, "Missing parameter 'lastName'"

def test_families::lastnameelement_has_lastName():
    assert hasattr(Families::LastNameElement, "lastName")
    descriptor = None
    for klass in Families::LastNameElement.__mro__:
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



def test_families::family_is_not_abstract():
    assert not inspect.isabstract(Families::Family)


def test_families::family_constructor_exists():
    assert callable(Families::Family.__init__)


def test_families::family_constructor_args():
    sig = inspect.signature(Families::Family.__init__)
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
Families::LastNameElement_strategy = st.builds(
    Families::LastNameElement,
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
Families::Member_strategy = st.builds(
    Families::Member,
    firstName=
        safe_text
)
Families::Family_strategy = st.builds(
    Families::Family,
)

@given(instance=Families::LastNameElement_strategy)
@settings(max_examples=50)
def test_families::lastnameelement_instantiation(instance):
    assert isinstance(instance, Families::LastNameElement)

@given(instance=Families::LastNameElement_strategy)
def test_families::lastnameelement_lastName_type(instance):
    assert isinstance(instance.lastName, str)


@given(instance=Families::LastNameElement_strategy)
def test_families::lastnameelement_lastName_setter(instance):
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

@given(instance=Families::Family_strategy)
@settings(max_examples=50)
def test_families::family_instantiation(instance):
    assert isinstance(instance, Families::Family)
