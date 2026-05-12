import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    datavault_Greeting,
    datavault_Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_datavault_greeting_is_not_abstract():
    assert not inspect.isabstract(datavault_Greeting)


def test_datavault_greeting_constructor_exists():
    assert callable(datavault_Greeting.__init__)


def test_datavault_greeting_constructor_args():
    sig = inspect.signature(datavault_Greeting.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_datavault_greeting_has_name():
    assert hasattr(datavault_Greeting, "name")
    descriptor = None
    for klass in datavault_Greeting.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_datavault_model_is_not_abstract():
    assert not inspect.isabstract(datavault_Model)


def test_datavault_model_constructor_exists():
    assert callable(datavault_Model.__init__)


def test_datavault_model_constructor_args():
    sig = inspect.signature(datavault_Model.__init__)
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
datavault_Greeting_strategy = st.builds(
    datavault_Greeting,
    name=
        safe_text
)
datavault_Model_strategy = st.builds(
    datavault_Model,
)

@given(instance=datavault_Greeting_strategy)
@settings(max_examples=50)
def test_datavault_greeting_instantiation(instance):
    assert isinstance(instance, datavault_Greeting)



@given(instance=datavault_Greeting_strategy)
def test_datavault_greeting_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=datavault_Model_strategy)
@settings(max_examples=50)
def test_datavault_model_instantiation(instance):
    assert isinstance(instance, datavault_Model)
