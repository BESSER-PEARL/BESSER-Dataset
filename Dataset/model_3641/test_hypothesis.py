import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    detachelist_Person,
    detachelist_Contacts,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_detachelist_person_is_not_abstract():
    assert not inspect.isabstract(detachelist_Person)


def test_detachelist_person_constructor_exists():
    assert callable(detachelist_Person.__init__)


def test_detachelist_person_constructor_args():
    sig = inspect.signature(detachelist_Person.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_detachelist_person_has_name():
    assert hasattr(detachelist_Person, "name")
    descriptor = None
    for klass in detachelist_Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_detachelist_contacts_is_not_abstract():
    assert not inspect.isabstract(detachelist_Contacts)


def test_detachelist_contacts_constructor_exists():
    assert callable(detachelist_Contacts.__init__)


def test_detachelist_contacts_constructor_args():
    sig = inspect.signature(detachelist_Contacts.__init__)
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
detachelist_Person_strategy = st.builds(
    detachelist_Person,
    name=
        safe_text
)
detachelist_Contacts_strategy = st.builds(
    detachelist_Contacts,
)

@given(instance=detachelist_Person_strategy)
@settings(max_examples=50)
def test_detachelist_person_instantiation(instance):
    assert isinstance(instance, detachelist_Person)



@given(instance=detachelist_Person_strategy)
def test_detachelist_person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=detachelist_Contacts_strategy)
@settings(max_examples=50)
def test_detachelist_contacts_instantiation(instance):
    assert isinstance(instance, detachelist_Contacts)
