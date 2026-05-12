import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    font_Greeting,
    font_Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_font_greeting_is_not_abstract():
    assert not inspect.isabstract(font_Greeting)


def test_font_greeting_constructor_exists():
    assert callable(font_Greeting.__init__)


def test_font_greeting_constructor_args():
    sig = inspect.signature(font_Greeting.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_font_greeting_has_name():
    assert hasattr(font_Greeting, "name")
    descriptor = None
    for klass in font_Greeting.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_font_model_is_not_abstract():
    assert not inspect.isabstract(font_Model)


def test_font_model_constructor_exists():
    assert callable(font_Model.__init__)


def test_font_model_constructor_args():
    sig = inspect.signature(font_Model.__init__)
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
font_Greeting_strategy = st.builds(
    font_Greeting,
    name=
        safe_text
)
font_Model_strategy = st.builds(
    font_Model,
)

@given(instance=font_Greeting_strategy)
@settings(max_examples=50)
def test_font_greeting_instantiation(instance):
    assert isinstance(instance, font_Greeting)



@given(instance=font_Greeting_strategy)
def test_font_greeting_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=font_Model_strategy)
@settings(max_examples=50)
def test_font_model_instantiation(instance):
    assert isinstance(instance, font_Model)
