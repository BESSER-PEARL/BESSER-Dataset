import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    java_Greeting,
    java_Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_java_greeting_is_not_abstract():
    assert not inspect.isabstract(java_Greeting)


def test_java_greeting_constructor_exists():
    assert callable(java_Greeting.__init__)


def test_java_greeting_constructor_args():
    sig = inspect.signature(java_Greeting.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_java_greeting_has_name():
    assert hasattr(java_Greeting, "name")
    descriptor = None
    for klass in java_Greeting.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_java_model_is_not_abstract():
    assert not inspect.isabstract(java_Model)


def test_java_model_constructor_exists():
    assert callable(java_Model.__init__)


def test_java_model_constructor_args():
    sig = inspect.signature(java_Model.__init__)
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
java_Greeting_strategy = st.builds(
    java_Greeting,
    name=
        safe_text
)
java_Model_strategy = st.builds(
    java_Model,
)

@given(instance=java_Greeting_strategy)
@settings(max_examples=50)
def test_java_greeting_instantiation(instance):
    assert isinstance(instance, java_Greeting)



@given(instance=java_Greeting_strategy)
def test_java_greeting_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=java_Model_strategy)
@settings(max_examples=50)
def test_java_model_instantiation(instance):
    assert isinstance(instance, java_Model)
