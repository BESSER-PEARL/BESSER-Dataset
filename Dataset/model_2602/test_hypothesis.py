import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    model::Root,
    model::PersonList,
    model::Person,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_model::root_is_not_abstract():
    assert not inspect.isabstract(model::Root)


def test_model::root_constructor_exists():
    assert callable(model::Root.__init__)


def test_model::root_constructor_args():
    sig = inspect.signature(model::Root.__init__)
    params = list(sig.parameters.keys())



def test_model::personlist_is_not_abstract():
    assert not inspect.isabstract(model::PersonList)


def test_model::personlist_constructor_exists():
    assert callable(model::PersonList.__init__)


def test_model::personlist_constructor_args():
    sig = inspect.signature(model::PersonList.__init__)
    params = list(sig.parameters.keys())



def test_model::person_is_not_abstract():
    assert not inspect.isabstract(model::Person)


def test_model::person_constructor_exists():
    assert callable(model::Person.__init__)


def test_model::person_constructor_args():
    sig = inspect.signature(model::Person.__init__)
    params = list(sig.parameters.keys())
    assert "firstName" in params, "Missing parameter 'firstName'"

def test_model::person_has_firstName():
    assert hasattr(model::Person, "firstName")
    descriptor = None
    for klass in model::Person.__mro__:
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
model::Root_strategy = st.builds(
    model::Root,
)
model::PersonList_strategy = st.builds(
    model::PersonList,
)
model::Person_strategy = st.builds(
    model::Person,
    firstName=
        safe_text
)

@given(instance=model::Root_strategy)
@settings(max_examples=50)
def test_model::root_instantiation(instance):
    assert isinstance(instance, model::Root)

@given(instance=model::PersonList_strategy)
@settings(max_examples=50)
def test_model::personlist_instantiation(instance):
    assert isinstance(instance, model::PersonList)

@given(instance=model::Person_strategy)
@settings(max_examples=50)
def test_model::person_instantiation(instance):
    assert isinstance(instance, model::Person)

@given(instance=model::Person_strategy)
def test_model::person_firstName_type(instance):
    assert isinstance(instance.firstName, str)


@given(instance=model::Person_strategy)
def test_model::person_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original
