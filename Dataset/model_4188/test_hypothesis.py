import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    anyaBasic::Greeting,
    anyaBasic::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_anyabasic::greeting_is_not_abstract():
    assert not inspect.isabstract(anyaBasic::Greeting)


def test_anyabasic::greeting_constructor_exists():
    assert callable(anyaBasic::Greeting.__init__)


def test_anyabasic::greeting_constructor_args():
    sig = inspect.signature(anyaBasic::Greeting.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_anyabasic::greeting_has_name():
    assert hasattr(anyaBasic::Greeting, "name")
    descriptor = None
    for klass in anyaBasic::Greeting.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_anyabasic::model_is_not_abstract():
    assert not inspect.isabstract(anyaBasic::Model)


def test_anyabasic::model_constructor_exists():
    assert callable(anyaBasic::Model.__init__)


def test_anyabasic::model_constructor_args():
    sig = inspect.signature(anyaBasic::Model.__init__)
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
anyaBasic::Greeting_strategy = st.builds(
    anyaBasic::Greeting,
    name=
        safe_text
)
anyaBasic::Model_strategy = st.builds(
    anyaBasic::Model,
)

@given(instance=anyaBasic::Greeting_strategy)
@settings(max_examples=50)
def test_anyabasic::greeting_instantiation(instance):
    assert isinstance(instance, anyaBasic::Greeting)

@given(instance=anyaBasic::Greeting_strategy)
def test_anyabasic::greeting_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=anyaBasic::Greeting_strategy)
def test_anyabasic::greeting_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=anyaBasic::Model_strategy)
@settings(max_examples=50)
def test_anyabasic::model_instantiation(instance):
    assert isinstance(instance, anyaBasic::Model)
