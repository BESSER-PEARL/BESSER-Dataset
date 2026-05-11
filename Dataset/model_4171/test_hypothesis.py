import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    pascal::Greeting,
    pascal::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_pascal::greeting_is_not_abstract():
    assert not inspect.isabstract(pascal::Greeting)


def test_pascal::greeting_constructor_exists():
    assert callable(pascal::Greeting.__init__)


def test_pascal::greeting_constructor_args():
    sig = inspect.signature(pascal::Greeting.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_pascal::greeting_has_name():
    assert hasattr(pascal::Greeting, "name")
    descriptor = None
    for klass in pascal::Greeting.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_pascal::model_is_not_abstract():
    assert not inspect.isabstract(pascal::Model)


def test_pascal::model_constructor_exists():
    assert callable(pascal::Model.__init__)


def test_pascal::model_constructor_args():
    sig = inspect.signature(pascal::Model.__init__)
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
pascal::Greeting_strategy = st.builds(
    pascal::Greeting,
    name=
        safe_text
)
pascal::Model_strategy = st.builds(
    pascal::Model,
)

@given(instance=pascal::Greeting_strategy)
@settings(max_examples=50)
def test_pascal::greeting_instantiation(instance):
    assert isinstance(instance, pascal::Greeting)

@given(instance=pascal::Greeting_strategy)
def test_pascal::greeting_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=pascal::Greeting_strategy)
def test_pascal::greeting_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=pascal::Model_strategy)
@settings(max_examples=50)
def test_pascal::model_instantiation(instance):
    assert isinstance(instance, pascal::Model)
