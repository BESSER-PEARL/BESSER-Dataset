import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    mydsl_Greeting,
    mydsl_Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mydsl_greeting_is_not_abstract():
    assert not inspect.isabstract(mydsl_Greeting)


def test_mydsl_greeting_constructor_exists():
    assert callable(mydsl_Greeting.__init__)


def test_mydsl_greeting_constructor_args():
    sig = inspect.signature(mydsl_Greeting.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl_greeting_has_name():
    assert hasattr(mydsl_Greeting, "name")
    descriptor = None
    for klass in mydsl_Greeting.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_model_is_not_abstract():
    assert not inspect.isabstract(mydsl_Model)


def test_mydsl_model_constructor_exists():
    assert callable(mydsl_Model.__init__)


def test_mydsl_model_constructor_args():
    sig = inspect.signature(mydsl_Model.__init__)
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
mydsl_Greeting_strategy = st.builds(
    mydsl_Greeting,
    name=
        safe_text
)
mydsl_Model_strategy = st.builds(
    mydsl_Model,
)

@given(instance=mydsl_Greeting_strategy)
@settings(max_examples=50)
def test_mydsl_greeting_instantiation(instance):
    assert isinstance(instance, mydsl_Greeting)



@given(instance=mydsl_Greeting_strategy)
def test_mydsl_greeting_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mydsl_Model_strategy)
@settings(max_examples=50)
def test_mydsl_model_instantiation(instance):
    assert isinstance(instance, mydsl_Model)
