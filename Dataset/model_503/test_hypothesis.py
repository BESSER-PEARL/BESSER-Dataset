import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Member,
    Families::Member,
    Families::Daughter,
    Families::Son,
    Families::Mother,
    Families::Father,
    Families::Family,
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



def test_families::daughter_is_not_abstract():
    assert not inspect.isabstract(Families::Daughter)


def test_families::daughter_constructor_exists():
    assert callable(Families::Daughter.__init__)


def test_families::daughter_constructor_args():
    sig = inspect.signature(Families::Daughter.__init__)
    params = list(sig.parameters.keys())



def test_families::son_is_not_abstract():
    assert not inspect.isabstract(Families::Son)


def test_families::son_constructor_exists():
    assert callable(Families::Son.__init__)


def test_families::son_constructor_args():
    sig = inspect.signature(Families::Son.__init__)
    params = list(sig.parameters.keys())



def test_families::mother_is_not_abstract():
    assert not inspect.isabstract(Families::Mother)


def test_families::mother_constructor_exists():
    assert callable(Families::Mother.__init__)


def test_families::mother_constructor_args():
    sig = inspect.signature(Families::Mother.__init__)
    params = list(sig.parameters.keys())



def test_families::father_is_not_abstract():
    assert not inspect.isabstract(Families::Father)


def test_families::father_constructor_exists():
    assert callable(Families::Father.__init__)


def test_families::father_constructor_args():
    sig = inspect.signature(Families::Father.__init__)
    params = list(sig.parameters.keys())



def test_families::family_is_not_abstract():
    assert not inspect.isabstract(Families::Family)


def test_families::family_constructor_exists():
    assert callable(Families::Family.__init__)


def test_families::family_constructor_args():
    sig = inspect.signature(Families::Family.__init__)
    params = list(sig.parameters.keys())
    assert "lastName" in params, "Missing parameter 'lastName'"

def test_families::family_has_lastName():
    assert hasattr(Families::Family, "lastName")
    descriptor = None
    for klass in Families::Family.__mro__:
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
Member_strategy = st.builds(
    Member,
)
Families::Member_strategy = st.builds(
    Families::Member,
    firstName=
        safe_text
)
Families::Daughter_strategy = st.builds(
    Families::Daughter,
)
Families::Son_strategy = st.builds(
    Families::Son,
)
Families::Mother_strategy = st.builds(
    Families::Mother,
)
Families::Father_strategy = st.builds(
    Families::Father,
)
Families::Family_strategy = st.builds(
    Families::Family,
    lastName=
        safe_text
)

@given(instance=Member_strategy)
@settings(max_examples=50)
def test_member_instantiation(instance):
    assert isinstance(instance, Member)

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

@given(instance=Families::Daughter_strategy)
@settings(max_examples=50)
def test_families::daughter_instantiation(instance):
    assert isinstance(instance, Families::Daughter)

@given(instance=Families::Son_strategy)
@settings(max_examples=50)
def test_families::son_instantiation(instance):
    assert isinstance(instance, Families::Son)

@given(instance=Families::Mother_strategy)
@settings(max_examples=50)
def test_families::mother_instantiation(instance):
    assert isinstance(instance, Families::Mother)

@given(instance=Families::Father_strategy)
@settings(max_examples=50)
def test_families::father_instantiation(instance):
    assert isinstance(instance, Families::Father)

@given(instance=Families::Family_strategy)
@settings(max_examples=50)
def test_families::family_instantiation(instance):
    assert isinstance(instance, Families::Family)

@given(instance=Families::Family_strategy)
def test_families::family_lastName_type(instance):
    assert isinstance(instance.lastName, str)


@given(instance=Families::Family_strategy)
def test_families::family_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original
