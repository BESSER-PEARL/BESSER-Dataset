import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    prolog_Greeting,
    prolog_Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_prolog_greeting_is_not_abstract():
    assert not inspect.isabstract(prolog_Greeting)


def test_prolog_greeting_constructor_exists():
    assert callable(prolog_Greeting.__init__)


def test_prolog_greeting_constructor_args():
    sig = inspect.signature(prolog_Greeting.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_prolog_greeting_has_name():
    assert hasattr(prolog_Greeting, "name")
    descriptor = None
    for klass in prolog_Greeting.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_prolog_model_is_not_abstract():
    assert not inspect.isabstract(prolog_Model)


def test_prolog_model_constructor_exists():
    assert callable(prolog_Model.__init__)


def test_prolog_model_constructor_args():
    sig = inspect.signature(prolog_Model.__init__)
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
prolog_Greeting_strategy = st.builds(
    prolog_Greeting,
    name=
        safe_text
)
prolog_Model_strategy = st.builds(
    prolog_Model,
)

@given(instance=prolog_Greeting_strategy)
@settings(max_examples=50)
def test_prolog_greeting_instantiation(instance):
    assert isinstance(instance, prolog_Greeting)



@given(instance=prolog_Greeting_strategy)
def test_prolog_greeting_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=prolog_Model_strategy)
@settings(max_examples=50)
def test_prolog_model_instantiation(instance):
    assert isinstance(instance, prolog_Model)
