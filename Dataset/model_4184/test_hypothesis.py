import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    hello_Greeting,
    hello_Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hello_greeting_is_not_abstract():
    assert not inspect.isabstract(hello_Greeting)


def test_hello_greeting_constructor_exists():
    assert callable(hello_Greeting.__init__)


def test_hello_greeting_constructor_args():
    sig = inspect.signature(hello_Greeting.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_hello_greeting_has_name():
    assert hasattr(hello_Greeting, "name")
    descriptor = None
    for klass in hello_Greeting.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_hello_model_is_not_abstract():
    assert not inspect.isabstract(hello_Model)


def test_hello_model_constructor_exists():
    assert callable(hello_Model.__init__)


def test_hello_model_constructor_args():
    sig = inspect.signature(hello_Model.__init__)
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
hello_Greeting_strategy = st.builds(
    hello_Greeting,
    name=
        safe_text
)
hello_Model_strategy = st.builds(
    hello_Model,
)

@given(instance=hello_Greeting_strategy)
@settings(max_examples=50)
def test_hello_greeting_instantiation(instance):
    assert isinstance(instance, hello_Greeting)



@given(instance=hello_Greeting_strategy)
def test_hello_greeting_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=hello_Model_strategy)
@settings(max_examples=50)
def test_hello_model_instantiation(instance):
    assert isinstance(instance, hello_Model)
