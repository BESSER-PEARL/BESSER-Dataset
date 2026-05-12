import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    family_Family,
    family_Member,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_family_family_is_not_abstract():
    assert not inspect.isabstract(family_Family)


def test_family_family_constructor_exists():
    assert callable(family_Family.__init__)


def test_family_family_constructor_args():
    sig = inspect.signature(family_Family.__init__)
    params = list(sig.parameters.keys())
    assert "lastName" in params, "Missing parameter 'lastName'"

def test_family_family_has_lastName():
    assert hasattr(family_Family, "lastName")
    descriptor = None
    for klass in family_Family.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)



def test_family_member_is_not_abstract():
    assert not inspect.isabstract(family_Member)


def test_family_member_constructor_exists():
    assert callable(family_Member.__init__)


def test_family_member_constructor_args():
    sig = inspect.signature(family_Member.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_family_member_has_name():
    assert hasattr(family_Member, "name")
    descriptor = None
    for klass in family_Member.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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
family_Family_strategy = st.builds(
    family_Family,
    lastName=
        safe_text
)
family_Member_strategy = st.builds(
    family_Member,
    name=
        safe_text
)

@given(instance=family_Family_strategy)
@settings(max_examples=50)
def test_family_family_instantiation(instance):
    assert isinstance(instance, family_Family)



@given(instance=family_Family_strategy)
def test_family_family_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original

@given(instance=family_Member_strategy)
@settings(max_examples=50)
def test_family_member_instantiation(instance):
    assert isinstance(instance, family_Member)



@given(instance=family_Member_strategy)
def test_family_member_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
