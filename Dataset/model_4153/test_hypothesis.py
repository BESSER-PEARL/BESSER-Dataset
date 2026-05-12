import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Example_Greeting,
    Example_Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_example_greeting_is_not_abstract():
    assert not inspect.isabstract(Example_Greeting)


def test_example_greeting_constructor_exists():
    assert callable(Example_Greeting.__init__)


def test_example_greeting_constructor_args():
    sig = inspect.signature(Example_Greeting.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_example_greeting_has_name():
    assert hasattr(Example_Greeting, "name")
    descriptor = None
    for klass in Example_Greeting.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_example_model_is_not_abstract():
    assert not inspect.isabstract(Example_Model)


def test_example_model_constructor_exists():
    assert callable(Example_Model.__init__)


def test_example_model_constructor_args():
    sig = inspect.signature(Example_Model.__init__)
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
Example_Greeting_strategy = st.builds(
    Example_Greeting,
    name=
        safe_text
)
Example_Model_strategy = st.builds(
    Example_Model,
)

@given(instance=Example_Greeting_strategy)
@settings(max_examples=50)
def test_example_greeting_instantiation(instance):
    assert isinstance(instance, Example_Greeting)



@given(instance=Example_Greeting_strategy)
def test_example_greeting_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Example_Model_strategy)
@settings(max_examples=50)
def test_example_model_instantiation(instance):
    assert isinstance(instance, Example_Model)
