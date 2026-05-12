import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    model_IPersonList,
    model_IPerson,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_model_ipersonlist_is_not_abstract():
    assert not inspect.isabstract(model_IPersonList)


def test_model_ipersonlist_constructor_exists():
    assert callable(model_IPersonList.__init__)


def test_model_ipersonlist_constructor_args():
    sig = inspect.signature(model_IPersonList.__init__)
    params = list(sig.parameters.keys())



def test_model_iperson_is_not_abstract():
    assert not inspect.isabstract(model_IPerson)


def test_model_iperson_constructor_exists():
    assert callable(model_IPerson.__init__)


def test_model_iperson_constructor_args():
    sig = inspect.signature(model_IPerson.__init__)
    params = list(sig.parameters.keys())
    assert "firstName" in params, "Missing parameter 'firstName'"

def test_model_iperson_has_firstName():
    assert hasattr(model_IPerson, "firstName")
    descriptor = None
    for klass in model_IPerson.__mro__:
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
model_IPersonList_strategy = st.builds(
    model_IPersonList,
)
model_IPerson_strategy = st.builds(
    model_IPerson,
    firstName=
        safe_text
)

@given(instance=model_IPersonList_strategy)
@settings(max_examples=50)
def test_model_ipersonlist_instantiation(instance):
    assert isinstance(instance, model_IPersonList)

@given(instance=model_IPerson_strategy)
@settings(max_examples=50)
def test_model_iperson_instantiation(instance):
    assert isinstance(instance, model_IPerson)



@given(instance=model_IPerson_strategy)
def test_model_iperson_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original
