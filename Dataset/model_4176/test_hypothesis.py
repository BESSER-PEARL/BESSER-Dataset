import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    activator_Greeting,
    activator_Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_activator_greeting_is_not_abstract():
    assert not inspect.isabstract(activator_Greeting)


def test_activator_greeting_constructor_exists():
    assert callable(activator_Greeting.__init__)


def test_activator_greeting_constructor_args():
    sig = inspect.signature(activator_Greeting.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_activator_greeting_has_name():
    assert hasattr(activator_Greeting, "name")
    descriptor = None
    for klass in activator_Greeting.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_activator_model_is_not_abstract():
    assert not inspect.isabstract(activator_Model)


def test_activator_model_constructor_exists():
    assert callable(activator_Model.__init__)


def test_activator_model_constructor_args():
    sig = inspect.signature(activator_Model.__init__)
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
activator_Greeting_strategy = st.builds(
    activator_Greeting,
    name=
        safe_text
)
activator_Model_strategy = st.builds(
    activator_Model,
)

@given(instance=activator_Greeting_strategy)
@settings(max_examples=50)
def test_activator_greeting_instantiation(instance):
    assert isinstance(instance, activator_Greeting)



@given(instance=activator_Greeting_strategy)
def test_activator_greeting_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=activator_Model_strategy)
@settings(max_examples=50)
def test_activator_model_instantiation(instance):
    assert isinstance(instance, activator_Model)
