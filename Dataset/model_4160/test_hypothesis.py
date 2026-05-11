import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    font::Greeting,
    font::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_font::greeting_is_not_abstract():
    assert not inspect.isabstract(font::Greeting)


def test_font::greeting_constructor_exists():
    assert callable(font::Greeting.__init__)


def test_font::greeting_constructor_args():
    sig = inspect.signature(font::Greeting.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_font::greeting_has_name():
    assert hasattr(font::Greeting, "name")
    descriptor = None
    for klass in font::Greeting.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_font::model_is_not_abstract():
    assert not inspect.isabstract(font::Model)


def test_font::model_constructor_exists():
    assert callable(font::Model.__init__)


def test_font::model_constructor_args():
    sig = inspect.signature(font::Model.__init__)
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
font::Greeting_strategy = st.builds(
    font::Greeting,
    name=
        safe_text
)
font::Model_strategy = st.builds(
    font::Model,
)

@given(instance=font::Greeting_strategy)
@settings(max_examples=50)
def test_font::greeting_instantiation(instance):
    assert isinstance(instance, font::Greeting)

@given(instance=font::Greeting_strategy)
def test_font::greeting_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=font::Greeting_strategy)
def test_font::greeting_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=font::Model_strategy)
@settings(max_examples=50)
def test_font::model_instantiation(instance):
    assert isinstance(instance, font::Model)
