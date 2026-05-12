import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    comp_Greeting,
    comp_Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_comp_greeting_is_not_abstract():
    assert not inspect.isabstract(comp_Greeting)


def test_comp_greeting_constructor_exists():
    assert callable(comp_Greeting.__init__)


def test_comp_greeting_constructor_args():
    sig = inspect.signature(comp_Greeting.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_comp_greeting_has_name():
    assert hasattr(comp_Greeting, "name")
    descriptor = None
    for klass in comp_Greeting.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_comp_model_is_not_abstract():
    assert not inspect.isabstract(comp_Model)


def test_comp_model_constructor_exists():
    assert callable(comp_Model.__init__)


def test_comp_model_constructor_args():
    sig = inspect.signature(comp_Model.__init__)
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
comp_Greeting_strategy = st.builds(
    comp_Greeting,
    name=
        safe_text
)
comp_Model_strategy = st.builds(
    comp_Model,
)

@given(instance=comp_Greeting_strategy)
@settings(max_examples=50)
def test_comp_greeting_instantiation(instance):
    assert isinstance(instance, comp_Greeting)



@given(instance=comp_Greeting_strategy)
def test_comp_greeting_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=comp_Model_strategy)
@settings(max_examples=50)
def test_comp_model_instantiation(instance):
    assert isinstance(instance, comp_Model)
