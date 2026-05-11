import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    lexertrace::Model,
    lexertrace::Greeting,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_lexertrace::model_is_not_abstract():
    assert not inspect.isabstract(lexertrace::Model)


def test_lexertrace::model_constructor_exists():
    assert callable(lexertrace::Model.__init__)


def test_lexertrace::model_constructor_args():
    sig = inspect.signature(lexertrace::Model.__init__)
    params = list(sig.parameters.keys())



def test_lexertrace::greeting_is_not_abstract():
    assert not inspect.isabstract(lexertrace::Greeting)


def test_lexertrace::greeting_constructor_exists():
    assert callable(lexertrace::Greeting.__init__)


def test_lexertrace::greeting_constructor_args():
    sig = inspect.signature(lexertrace::Greeting.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_lexertrace::greeting_has_name():
    assert hasattr(lexertrace::Greeting, "name")
    descriptor = None
    for klass in lexertrace::Greeting.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)


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
lexertrace::Model_strategy = st.builds(
    lexertrace::Model,
)
lexertrace::Greeting_strategy = st.builds(
    lexertrace::Greeting,
    name=
        safe_text
)

@given(instance=lexertrace::Model_strategy)
@settings(max_examples=50)
def test_lexertrace::model_instantiation(instance):
    assert isinstance(instance, lexertrace::Model)

@given(instance=lexertrace::Greeting_strategy)
@settings(max_examples=50)
def test_lexertrace::greeting_instantiation(instance):
    assert isinstance(instance, lexertrace::Greeting)

@given(instance=lexertrace::Greeting_strategy)
def test_lexertrace::greeting_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=lexertrace::Greeting_strategy)
def test_lexertrace::greeting_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
