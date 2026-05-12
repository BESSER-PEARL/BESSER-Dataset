import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    scheme_Greeting,
    scheme_Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_scheme_greeting_is_not_abstract():
    assert not inspect.isabstract(scheme_Greeting)


def test_scheme_greeting_constructor_exists():
    assert callable(scheme_Greeting.__init__)


def test_scheme_greeting_constructor_args():
    sig = inspect.signature(scheme_Greeting.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_scheme_greeting_has_name():
    assert hasattr(scheme_Greeting, "name")
    descriptor = None
    for klass in scheme_Greeting.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_scheme_model_is_not_abstract():
    assert not inspect.isabstract(scheme_Model)


def test_scheme_model_constructor_exists():
    assert callable(scheme_Model.__init__)


def test_scheme_model_constructor_args():
    sig = inspect.signature(scheme_Model.__init__)
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
scheme_Greeting_strategy = st.builds(
    scheme_Greeting,
    name=
        safe_text
)
scheme_Model_strategy = st.builds(
    scheme_Model,
)

@given(instance=scheme_Greeting_strategy)
@settings(max_examples=50)
def test_scheme_greeting_instantiation(instance):
    assert isinstance(instance, scheme_Greeting)



@given(instance=scheme_Greeting_strategy)
def test_scheme_greeting_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=scheme_Model_strategy)
@settings(max_examples=50)
def test_scheme_model_instantiation(instance):
    assert isinstance(instance, scheme_Model)
