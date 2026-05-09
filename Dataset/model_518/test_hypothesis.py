import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Families::Family,
    Member,
    Families::Female,
    Families::Male,
    Families::Member,
    Families::Families,
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



def test_member_is_not_abstract():
    assert not inspect.isabstract(Member)


def test_member_constructor_exists():
    assert callable(Member.__init__)


def test_member_constructor_args():
    sig = inspect.signature(Member.__init__)
    params = list(sig.parameters.keys())



def test_families::female_is_not_abstract():
    assert not inspect.isabstract(Families::Female)


def test_families::female_constructor_exists():
    assert callable(Families::Female.__init__)


def test_families::female_constructor_args():
    sig = inspect.signature(Families::Female.__init__)
    params = list(sig.parameters.keys())



def test_families::male_is_not_abstract():
    assert not inspect.isabstract(Families::Male)


def test_families::male_constructor_exists():
    assert callable(Families::Male.__init__)


def test_families::male_constructor_args():
    sig = inspect.signature(Families::Male.__init__)
    params = list(sig.parameters.keys())



def test_families::member_is_not_abstract():
    assert not inspect.isabstract(Families::Member)


def test_families::member_constructor_exists():
    assert callable(Families::Member.__init__)


def test_families::member_constructor_args():
    sig = inspect.signature(Families::Member.__init__)
    params = list(sig.parameters.keys())
    assert "firstname" in params, "Missing parameter 'firstname'"

def test_families::member_has_firstname():
    assert hasattr(Families::Member, "firstname")
    descriptor = None
    for klass in Families::Member.__mro__:
        if "firstname" in klass.__dict__:
            descriptor = klass.__dict__["firstname"]
            break
    assert isinstance(descriptor, property)



def test_families::families_is_not_abstract():
    assert not inspect.isabstract(Families::Families)


def test_families::families_constructor_exists():
    assert callable(Families::Families.__init__)


def test_families::families_constructor_args():
    sig = inspect.signature(Families::Families.__init__)
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
Families::Family_strategy = st.builds(
    Families::Family,
    lastname=
        safe_text
)
Member_strategy = st.builds(
    Member,
)
Families::Female_strategy = st.builds(
    Families::Female,
)
Families::Male_strategy = st.builds(
    Families::Male,
)
Families::Member_strategy = st.builds(
    Families::Member,
    firstname=
        safe_text
)
Families::Families_strategy = st.builds(
    Families::Families,
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

@given(instance=Member_strategy)
@settings(max_examples=50)
def test_member_instantiation(instance):
    assert isinstance(instance, Member)

@given(instance=Families::Female_strategy)
@settings(max_examples=50)
def test_families::female_instantiation(instance):
    assert isinstance(instance, Families::Female)

@given(instance=Families::Male_strategy)
@settings(max_examples=50)
def test_families::male_instantiation(instance):
    assert isinstance(instance, Families::Male)

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

@given(instance=Families::Families_strategy)
@settings(max_examples=50)
def test_families::families_instantiation(instance):
    assert isinstance(instance, Families::Families)
