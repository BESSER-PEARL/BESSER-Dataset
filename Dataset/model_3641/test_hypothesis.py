import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    detachelist::Person,
    detachelist::Contacts,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_detachelist::person_is_not_abstract():
    assert not inspect.isabstract(detachelist::Person)


def test_detachelist::person_constructor_exists():
    assert callable(detachelist::Person.__init__)


def test_detachelist::person_constructor_args():
    sig = inspect.signature(detachelist::Person.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_detachelist::person_has_name():
    assert hasattr(detachelist::Person, "name")
    descriptor = None
    for klass in detachelist::Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_detachelist::contacts_is_not_abstract():
    assert not inspect.isabstract(detachelist::Contacts)


def test_detachelist::contacts_constructor_exists():
    assert callable(detachelist::Contacts.__init__)


def test_detachelist::contacts_constructor_args():
    sig = inspect.signature(detachelist::Contacts.__init__)
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
detachelist::Person_strategy = st.builds(
    detachelist::Person,
    name=
        safe_text
)
detachelist::Contacts_strategy = st.builds(
    detachelist::Contacts,
)

@given(instance=detachelist::Person_strategy)
@settings(max_examples=50)
def test_detachelist::person_instantiation(instance):
    assert isinstance(instance, detachelist::Person)

@given(instance=detachelist::Person_strategy)
def test_detachelist::person_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=detachelist::Person_strategy)
def test_detachelist::person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=detachelist::Contacts_strategy)
@settings(max_examples=50)
def test_detachelist::contacts_instantiation(instance):
    assert isinstance(instance, detachelist::Contacts)
