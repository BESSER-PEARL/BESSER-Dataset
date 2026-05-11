import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    dsl::Greeting,
    dsl::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_dsl::greeting_is_not_abstract():
    assert not inspect.isabstract(dsl::Greeting)


def test_dsl::greeting_constructor_exists():
    assert callable(dsl::Greeting.__init__)


def test_dsl::greeting_constructor_args():
    sig = inspect.signature(dsl::Greeting.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dsl::greeting_has_name():
    assert hasattr(dsl::Greeting, "name")
    descriptor = None
    for klass in dsl::Greeting.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dsl::model_is_not_abstract():
    assert not inspect.isabstract(dsl::Model)


def test_dsl::model_constructor_exists():
    assert callable(dsl::Model.__init__)


def test_dsl::model_constructor_args():
    sig = inspect.signature(dsl::Model.__init__)
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
dsl::Greeting_strategy = st.builds(
    dsl::Greeting,
    name=
        safe_text
)
dsl::Model_strategy = st.builds(
    dsl::Model,
)

@given(instance=dsl::Greeting_strategy)
@settings(max_examples=50)
def test_dsl::greeting_instantiation(instance):
    assert isinstance(instance, dsl::Greeting)

@given(instance=dsl::Greeting_strategy)
def test_dsl::greeting_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dsl::Greeting_strategy)
def test_dsl::greeting_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dsl::Model_strategy)
@settings(max_examples=50)
def test_dsl::model_instantiation(instance):
    assert isinstance(instance, dsl::Model)
