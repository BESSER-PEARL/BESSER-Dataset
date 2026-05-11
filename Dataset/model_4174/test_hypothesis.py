import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    hello::Greeting,
    hello::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hello::greeting_is_not_abstract():
    assert not inspect.isabstract(hello::Greeting)


def test_hello::greeting_constructor_exists():
    assert callable(hello::Greeting.__init__)


def test_hello::greeting_constructor_args():
    sig = inspect.signature(hello::Greeting.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_hello::greeting_has_name():
    assert hasattr(hello::Greeting, "name")
    descriptor = None
    for klass in hello::Greeting.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_hello::model_is_not_abstract():
    assert not inspect.isabstract(hello::Model)


def test_hello::model_constructor_exists():
    assert callable(hello::Model.__init__)


def test_hello::model_constructor_args():
    sig = inspect.signature(hello::Model.__init__)
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
hello::Greeting_strategy = st.builds(
    hello::Greeting,
    name=
        safe_text
)
hello::Model_strategy = st.builds(
    hello::Model,
)

@given(instance=hello::Greeting_strategy)
@settings(max_examples=50)
def test_hello::greeting_instantiation(instance):
    assert isinstance(instance, hello::Greeting)

@given(instance=hello::Greeting_strategy)
def test_hello::greeting_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=hello::Greeting_strategy)
def test_hello::greeting_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=hello::Model_strategy)
@settings(max_examples=50)
def test_hello::model_instantiation(instance):
    assert isinstance(instance, hello::Model)
