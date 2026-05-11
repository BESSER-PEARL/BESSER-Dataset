import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    model::IPersonList,
    model::IPerson,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_model::ipersonlist_is_not_abstract():
    assert not inspect.isabstract(model::IPersonList)


def test_model::ipersonlist_constructor_exists():
    assert callable(model::IPersonList.__init__)


def test_model::ipersonlist_constructor_args():
    sig = inspect.signature(model::IPersonList.__init__)
    params = list(sig.parameters.keys())



def test_model::iperson_is_not_abstract():
    assert not inspect.isabstract(model::IPerson)


def test_model::iperson_constructor_exists():
    assert callable(model::IPerson.__init__)


def test_model::iperson_constructor_args():
    sig = inspect.signature(model::IPerson.__init__)
    params = list(sig.parameters.keys())
    assert "firstName" in params, "Missing parameter 'firstName'"

def test_model::iperson_has_firstName():
    assert hasattr(model::IPerson, "firstName")
    descriptor = None
    for klass in model::IPerson.__mro__:
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
model::IPersonList_strategy = st.builds(
    model::IPersonList,
)
model::IPerson_strategy = st.builds(
    model::IPerson,
    firstName=
        safe_text
)

@given(instance=model::IPersonList_strategy)
@settings(max_examples=50)
def test_model::ipersonlist_instantiation(instance):
    assert isinstance(instance, model::IPersonList)

@given(instance=model::IPerson_strategy)
@settings(max_examples=50)
def test_model::iperson_instantiation(instance):
    assert isinstance(instance, model::IPerson)

@given(instance=model::IPerson_strategy)
def test_model::iperson_firstName_type(instance):
    assert isinstance(instance.firstName, str)


@given(instance=model::IPerson_strategy)
def test_model::iperson_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original
