import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    scheme::Greeting,
    scheme::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_scheme::greeting_is_not_abstract():
    assert not inspect.isabstract(scheme::Greeting)


def test_scheme::greeting_constructor_exists():
    assert callable(scheme::Greeting.__init__)


def test_scheme::greeting_constructor_args():
    sig = inspect.signature(scheme::Greeting.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_scheme::greeting_has_name():
    assert hasattr(scheme::Greeting, "name")
    descriptor = None
    for klass in scheme::Greeting.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_scheme::model_is_not_abstract():
    assert not inspect.isabstract(scheme::Model)


def test_scheme::model_constructor_exists():
    assert callable(scheme::Model.__init__)


def test_scheme::model_constructor_args():
    sig = inspect.signature(scheme::Model.__init__)
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
scheme::Greeting_strategy = st.builds(
    scheme::Greeting,
    name=
        safe_text
)
scheme::Model_strategy = st.builds(
    scheme::Model,
)

@given(instance=scheme::Greeting_strategy)
@settings(max_examples=50)
def test_scheme::greeting_instantiation(instance):
    assert isinstance(instance, scheme::Greeting)

@given(instance=scheme::Greeting_strategy)
def test_scheme::greeting_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=scheme::Greeting_strategy)
def test_scheme::greeting_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=scheme::Model_strategy)
@settings(max_examples=50)
def test_scheme::model_instantiation(instance):
    assert isinstance(instance, scheme::Model)
