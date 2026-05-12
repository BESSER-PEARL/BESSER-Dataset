import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    cherry1to2_Greeting,
    cherry1to2_Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_cherry1to2_greeting_is_not_abstract():
    assert not inspect.isabstract(cherry1to2_Greeting)


def test_cherry1to2_greeting_constructor_exists():
    assert callable(cherry1to2_Greeting.__init__)


def test_cherry1to2_greeting_constructor_args():
    sig = inspect.signature(cherry1to2_Greeting.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cherry1to2_greeting_has_name():
    assert hasattr(cherry1to2_Greeting, "name")
    descriptor = None
    for klass in cherry1to2_Greeting.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cherry1to2_model_is_not_abstract():
    assert not inspect.isabstract(cherry1to2_Model)


def test_cherry1to2_model_constructor_exists():
    assert callable(cherry1to2_Model.__init__)


def test_cherry1to2_model_constructor_args():
    sig = inspect.signature(cherry1to2_Model.__init__)
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
cherry1to2_Greeting_strategy = st.builds(
    cherry1to2_Greeting,
    name=
        safe_text
)
cherry1to2_Model_strategy = st.builds(
    cherry1to2_Model,
)

@given(instance=cherry1to2_Greeting_strategy)
@settings(max_examples=50)
def test_cherry1to2_greeting_instantiation(instance):
    assert isinstance(instance, cherry1to2_Greeting)



@given(instance=cherry1to2_Greeting_strategy)
def test_cherry1to2_greeting_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cherry1to2_Model_strategy)
@settings(max_examples=50)
def test_cherry1to2_model_instantiation(instance):
    assert isinstance(instance, cherry1to2_Model)
