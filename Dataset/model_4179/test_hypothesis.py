import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    prolog::Greeting,
    prolog::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_prolog::greeting_is_not_abstract():
    assert not inspect.isabstract(prolog::Greeting)


def test_prolog::greeting_constructor_exists():
    assert callable(prolog::Greeting.__init__)


def test_prolog::greeting_constructor_args():
    sig = inspect.signature(prolog::Greeting.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_prolog::greeting_has_name():
    assert hasattr(prolog::Greeting, "name")
    descriptor = None
    for klass in prolog::Greeting.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_prolog::model_is_not_abstract():
    assert not inspect.isabstract(prolog::Model)


def test_prolog::model_constructor_exists():
    assert callable(prolog::Model.__init__)


def test_prolog::model_constructor_args():
    sig = inspect.signature(prolog::Model.__init__)
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
prolog::Greeting_strategy = st.builds(
    prolog::Greeting,
    name=
        safe_text
)
prolog::Model_strategy = st.builds(
    prolog::Model,
)

@given(instance=prolog::Greeting_strategy)
@settings(max_examples=50)
def test_prolog::greeting_instantiation(instance):
    assert isinstance(instance, prolog::Greeting)

@given(instance=prolog::Greeting_strategy)
def test_prolog::greeting_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=prolog::Greeting_strategy)
def test_prolog::greeting_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=prolog::Model_strategy)
@settings(max_examples=50)
def test_prolog::model_instantiation(instance):
    assert isinstance(instance, prolog::Model)
