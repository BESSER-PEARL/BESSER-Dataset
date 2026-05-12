import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    families_Family,
    families_Member,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_families_family_is_not_abstract():
    assert not inspect.isabstract(families_Family)


def test_families_family_constructor_exists():
    assert callable(families_Family.__init__)


def test_families_family_constructor_args():
    sig = inspect.signature(families_Family.__init__)
    params = list(sig.parameters.keys())
    assert "lastName" in params, "Missing parameter 'lastName'"

def test_families_family_has_lastName():
    assert hasattr(families_Family, "lastName")
    descriptor = None
    for klass in families_Family.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)



def test_families_member_is_not_abstract():
    assert not inspect.isabstract(families_Member)


def test_families_member_constructor_exists():
    assert callable(families_Member.__init__)


def test_families_member_constructor_args():
    sig = inspect.signature(families_Member.__init__)
    params = list(sig.parameters.keys())
    assert "firstName" in params, "Missing parameter 'firstName'"

def test_families_member_has_firstName():
    assert hasattr(families_Member, "firstName")
    descriptor = None
    for klass in families_Member.__mro__:
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
families_Family_strategy = st.builds(
    families_Family,
    lastName=
        safe_text
)
families_Member_strategy = st.builds(
    families_Member,
    firstName=
        safe_text
)

@given(instance=families_Family_strategy)
@settings(max_examples=50)
def test_families_family_instantiation(instance):
    assert isinstance(instance, families_Family)



@given(instance=families_Family_strategy)
def test_families_family_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original

@given(instance=families_Member_strategy)
@settings(max_examples=50)
def test_families_member_instantiation(instance):
    assert isinstance(instance, families_Member)



@given(instance=families_Member_strategy)
def test_families_member_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original
