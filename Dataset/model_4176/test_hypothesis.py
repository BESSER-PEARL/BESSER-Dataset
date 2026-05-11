import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    activator::Greeting,
    activator::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_activator::greeting_is_not_abstract():
    assert not inspect.isabstract(activator::Greeting)


def test_activator::greeting_constructor_exists():
    assert callable(activator::Greeting.__init__)


def test_activator::greeting_constructor_args():
    sig = inspect.signature(activator::Greeting.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_activator::greeting_has_name():
    assert hasattr(activator::Greeting, "name")
    descriptor = None
    for klass in activator::Greeting.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_activator::model_is_not_abstract():
    assert not inspect.isabstract(activator::Model)


def test_activator::model_constructor_exists():
    assert callable(activator::Model.__init__)


def test_activator::model_constructor_args():
    sig = inspect.signature(activator::Model.__init__)
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
activator::Greeting_strategy = st.builds(
    activator::Greeting,
    name=
        safe_text
)
activator::Model_strategy = st.builds(
    activator::Model,
)

@given(instance=activator::Greeting_strategy)
@settings(max_examples=50)
def test_activator::greeting_instantiation(instance):
    assert isinstance(instance, activator::Greeting)

@given(instance=activator::Greeting_strategy)
def test_activator::greeting_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=activator::Greeting_strategy)
def test_activator::greeting_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=activator::Model_strategy)
@settings(max_examples=50)
def test_activator::model_instantiation(instance):
    assert isinstance(instance, activator::Model)
