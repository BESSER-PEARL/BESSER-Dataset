import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Example::Greeting,
    Example::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_example::greeting_is_not_abstract():
    assert not inspect.isabstract(Example::Greeting)


def test_example::greeting_constructor_exists():
    assert callable(Example::Greeting.__init__)


def test_example::greeting_constructor_args():
    sig = inspect.signature(Example::Greeting.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_example::greeting_has_name():
    assert hasattr(Example::Greeting, "name")
    descriptor = None
    for klass in Example::Greeting.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_example::model_is_not_abstract():
    assert not inspect.isabstract(Example::Model)


def test_example::model_constructor_exists():
    assert callable(Example::Model.__init__)


def test_example::model_constructor_args():
    sig = inspect.signature(Example::Model.__init__)
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
Example::Greeting_strategy = st.builds(
    Example::Greeting,
    name=
        safe_text
)
Example::Model_strategy = st.builds(
    Example::Model,
)

@given(instance=Example::Greeting_strategy)
@settings(max_examples=50)
def test_example::greeting_instantiation(instance):
    assert isinstance(instance, Example::Greeting)

@given(instance=Example::Greeting_strategy)
def test_example::greeting_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Example::Greeting_strategy)
def test_example::greeting_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Example::Model_strategy)
@settings(max_examples=50)
def test_example::model_instantiation(instance):
    assert isinstance(instance, Example::Model)
