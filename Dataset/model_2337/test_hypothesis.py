import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    persons::PersonGroup,
    persons::Person,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_persons::persongroup_is_not_abstract():
    assert not inspect.isabstract(persons::PersonGroup)


def test_persons::persongroup_constructor_exists():
    assert callable(persons::PersonGroup.__init__)


def test_persons::persongroup_constructor_args():
    sig = inspect.signature(persons::PersonGroup.__init__)
    params = list(sig.parameters.keys())



def test_persons::person_is_not_abstract():
    assert not inspect.isabstract(persons::Person)


def test_persons::person_constructor_exists():
    assert callable(persons::Person.__init__)


def test_persons::person_constructor_args():
    sig = inspect.signature(persons::Person.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_persons::person_has_name():
    assert hasattr(persons::Person, "name")
    descriptor = None
    for klass in persons::Person.__mro__:
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
persons::PersonGroup_strategy = st.builds(
    persons::PersonGroup,
)
persons::Person_strategy = st.builds(
    persons::Person,
    name=
        safe_text
)

@given(instance=persons::PersonGroup_strategy)
@settings(max_examples=50)
def test_persons::persongroup_instantiation(instance):
    assert isinstance(instance, persons::PersonGroup)

@given(instance=persons::Person_strategy)
@settings(max_examples=50)
def test_persons::person_instantiation(instance):
    assert isinstance(instance, persons::Person)

@given(instance=persons::Person_strategy)
def test_persons::person_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=persons::Person_strategy)
def test_persons::person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
