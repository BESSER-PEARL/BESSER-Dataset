import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    family::Family,
    family::Member,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_family::family_is_not_abstract():
    assert not inspect.isabstract(family::Family)


def test_family::family_constructor_exists():
    assert callable(family::Family.__init__)


def test_family::family_constructor_args():
    sig = inspect.signature(family::Family.__init__)
    params = list(sig.parameters.keys())
    assert "lastName" in params, "Missing parameter 'lastName'"

def test_family::family_has_lastName():
    assert hasattr(family::Family, "lastName")
    descriptor = None
    for klass in family::Family.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)



def test_family::member_is_not_abstract():
    assert not inspect.isabstract(family::Member)


def test_family::member_constructor_exists():
    assert callable(family::Member.__init__)


def test_family::member_constructor_args():
    sig = inspect.signature(family::Member.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_family::member_has_name():
    assert hasattr(family::Member, "name")
    descriptor = None
    for klass in family::Member.__mro__:
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
family::Family_strategy = st.builds(
    family::Family,
    lastName=
        safe_text
)
family::Member_strategy = st.builds(
    family::Member,
    name=
        safe_text
)

@given(instance=family::Family_strategy)
@settings(max_examples=50)
def test_family::family_instantiation(instance):
    assert isinstance(instance, family::Family)

@given(instance=family::Family_strategy)
def test_family::family_lastName_type(instance):
    assert isinstance(instance.lastName, str)


@given(instance=family::Family_strategy)
def test_family::family_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original

@given(instance=family::Member_strategy)
@settings(max_examples=50)
def test_family::member_instantiation(instance):
    assert isinstance(instance, family::Member)

@given(instance=family::Member_strategy)
def test_family::member_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=family::Member_strategy)
def test_family::member_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
