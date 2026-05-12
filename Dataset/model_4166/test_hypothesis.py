import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    myDsl1_Greeting,
    myDsl1_Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mydsl1_greeting_is_not_abstract():
    assert not inspect.isabstract(myDsl1_Greeting)


def test_mydsl1_greeting_constructor_exists():
    assert callable(myDsl1_Greeting.__init__)


def test_mydsl1_greeting_constructor_args():
    sig = inspect.signature(myDsl1_Greeting.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl1_greeting_has_name():
    assert hasattr(myDsl1_Greeting, "name")
    descriptor = None
    for klass in myDsl1_Greeting.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl1_model_is_not_abstract():
    assert not inspect.isabstract(myDsl1_Model)


def test_mydsl1_model_constructor_exists():
    assert callable(myDsl1_Model.__init__)


def test_mydsl1_model_constructor_args():
    sig = inspect.signature(myDsl1_Model.__init__)
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
myDsl1_Greeting_strategy = st.builds(
    myDsl1_Greeting,
    name=
        safe_text
)
myDsl1_Model_strategy = st.builds(
    myDsl1_Model,
)

@given(instance=myDsl1_Greeting_strategy)
@settings(max_examples=50)
def test_mydsl1_greeting_instantiation(instance):
    assert isinstance(instance, myDsl1_Greeting)



@given(instance=myDsl1_Greeting_strategy)
def test_mydsl1_greeting_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl1_Model_strategy)
@settings(max_examples=50)
def test_mydsl1_model_instantiation(instance):
    assert isinstance(instance, myDsl1_Model)
