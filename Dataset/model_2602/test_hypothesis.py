import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    model_Root,
    model_PersonList,
    model_Person,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_model_root_is_not_abstract():
    assert not inspect.isabstract(model_Root)


def test_model_root_constructor_exists():
    assert callable(model_Root.__init__)


def test_model_root_constructor_args():
    sig = inspect.signature(model_Root.__init__)
    params = list(sig.parameters.keys())



def test_model_personlist_is_not_abstract():
    assert not inspect.isabstract(model_PersonList)


def test_model_personlist_constructor_exists():
    assert callable(model_PersonList.__init__)


def test_model_personlist_constructor_args():
    sig = inspect.signature(model_PersonList.__init__)
    params = list(sig.parameters.keys())



def test_model_person_is_not_abstract():
    assert not inspect.isabstract(model_Person)


def test_model_person_constructor_exists():
    assert callable(model_Person.__init__)


def test_model_person_constructor_args():
    sig = inspect.signature(model_Person.__init__)
    params = list(sig.parameters.keys())
    assert "firstName" in params, "Missing parameter 'firstName'"

def test_model_person_has_firstName():
    assert hasattr(model_Person, "firstName")
    descriptor = None
    for klass in model_Person.__mro__:
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
model_Root_strategy = st.builds(
    model_Root,
)
model_PersonList_strategy = st.builds(
    model_PersonList,
)
model_Person_strategy = st.builds(
    model_Person,
    firstName=
        safe_text
)

@given(instance=model_Root_strategy)
@settings(max_examples=50)
def test_model_root_instantiation(instance):
    assert isinstance(instance, model_Root)

@given(instance=model_PersonList_strategy)
@settings(max_examples=50)
def test_model_personlist_instantiation(instance):
    assert isinstance(instance, model_PersonList)

@given(instance=model_Person_strategy)
@settings(max_examples=50)
def test_model_person_instantiation(instance):
    assert isinstance(instance, model_Person)



@given(instance=model_Person_strategy)
def test_model_person_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original
