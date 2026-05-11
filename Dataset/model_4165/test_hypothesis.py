import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    noJdt::Greeting,
    noJdt::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_nojdt::greeting_is_not_abstract():
    assert not inspect.isabstract(noJdt::Greeting)


def test_nojdt::greeting_constructor_exists():
    assert callable(noJdt::Greeting.__init__)


def test_nojdt::greeting_constructor_args():
    sig = inspect.signature(noJdt::Greeting.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_nojdt::greeting_has_name():
    assert hasattr(noJdt::Greeting, "name")
    descriptor = None
    for klass in noJdt::Greeting.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_nojdt::model_is_not_abstract():
    assert not inspect.isabstract(noJdt::Model)


def test_nojdt::model_constructor_exists():
    assert callable(noJdt::Model.__init__)


def test_nojdt::model_constructor_args():
    sig = inspect.signature(noJdt::Model.__init__)
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
noJdt::Greeting_strategy = st.builds(
    noJdt::Greeting,
    name=
        safe_text
)
noJdt::Model_strategy = st.builds(
    noJdt::Model,
)

@given(instance=noJdt::Greeting_strategy)
@settings(max_examples=50)
def test_nojdt::greeting_instantiation(instance):
    assert isinstance(instance, noJdt::Greeting)

@given(instance=noJdt::Greeting_strategy)
def test_nojdt::greeting_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=noJdt::Greeting_strategy)
def test_nojdt::greeting_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=noJdt::Model_strategy)
@settings(max_examples=50)
def test_nojdt::model_instantiation(instance):
    assert isinstance(instance, noJdt::Model)
