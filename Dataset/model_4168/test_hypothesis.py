import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    comp::Model,
    comp::Greeting,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_comp::model_is_not_abstract():
    assert not inspect.isabstract(comp::Model)


def test_comp::model_constructor_exists():
    assert callable(comp::Model.__init__)


def test_comp::model_constructor_args():
    sig = inspect.signature(comp::Model.__init__)
    params = list(sig.parameters.keys())



def test_comp::greeting_is_not_abstract():
    assert not inspect.isabstract(comp::Greeting)


def test_comp::greeting_constructor_exists():
    assert callable(comp::Greeting.__init__)


def test_comp::greeting_constructor_args():
    sig = inspect.signature(comp::Greeting.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_comp::greeting_has_name():
    assert hasattr(comp::Greeting, "name")
    descriptor = None
    for klass in comp::Greeting.__mro__:
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
comp::Model_strategy = st.builds(
    comp::Model,
)
comp::Greeting_strategy = st.builds(
    comp::Greeting,
    name=
        safe_text
)

@given(instance=comp::Model_strategy)
@settings(max_examples=50)
def test_comp::model_instantiation(instance):
    assert isinstance(instance, comp::Model)

@given(instance=comp::Greeting_strategy)
@settings(max_examples=50)
def test_comp::greeting_instantiation(instance):
    assert isinstance(instance, comp::Greeting)

@given(instance=comp::Greeting_strategy)
def test_comp::greeting_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=comp::Greeting_strategy)
def test_comp::greeting_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
