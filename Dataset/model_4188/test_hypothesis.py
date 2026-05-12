import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    anyaBasic_Greeting,
    anyaBasic_Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_anyabasic_greeting_is_not_abstract():
    assert not inspect.isabstract(anyaBasic_Greeting)


def test_anyabasic_greeting_constructor_exists():
    assert callable(anyaBasic_Greeting.__init__)


def test_anyabasic_greeting_constructor_args():
    sig = inspect.signature(anyaBasic_Greeting.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_anyabasic_greeting_has_name():
    assert hasattr(anyaBasic_Greeting, "name")
    descriptor = None
    for klass in anyaBasic_Greeting.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_anyabasic_model_is_not_abstract():
    assert not inspect.isabstract(anyaBasic_Model)


def test_anyabasic_model_constructor_exists():
    assert callable(anyaBasic_Model.__init__)


def test_anyabasic_model_constructor_args():
    sig = inspect.signature(anyaBasic_Model.__init__)
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
anyaBasic_Greeting_strategy = st.builds(
    anyaBasic_Greeting,
    name=
        safe_text
)
anyaBasic_Model_strategy = st.builds(
    anyaBasic_Model,
)

@given(instance=anyaBasic_Greeting_strategy)
@settings(max_examples=50)
def test_anyabasic_greeting_instantiation(instance):
    assert isinstance(instance, anyaBasic_Greeting)



@given(instance=anyaBasic_Greeting_strategy)
def test_anyabasic_greeting_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=anyaBasic_Model_strategy)
@settings(max_examples=50)
def test_anyabasic_model_instantiation(instance):
    assert isinstance(instance, anyaBasic_Model)
