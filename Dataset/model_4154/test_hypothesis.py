import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    mydsl::Greeting,
    mydsl::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mydsl::greeting_is_not_abstract():
    assert not inspect.isabstract(mydsl::Greeting)


def test_mydsl::greeting_constructor_exists():
    assert callable(mydsl::Greeting.__init__)


def test_mydsl::greeting_constructor_args():
    sig = inspect.signature(mydsl::Greeting.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::greeting_has_name():
    assert hasattr(mydsl::Greeting, "name")
    descriptor = None
    for klass in mydsl::Greeting.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::model_is_not_abstract():
    assert not inspect.isabstract(mydsl::Model)


def test_mydsl::model_constructor_exists():
    assert callable(mydsl::Model.__init__)


def test_mydsl::model_constructor_args():
    sig = inspect.signature(mydsl::Model.__init__)
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
mydsl::Greeting_strategy = st.builds(
    mydsl::Greeting,
    name=
        safe_text
)
mydsl::Model_strategy = st.builds(
    mydsl::Model,
)

@given(instance=mydsl::Greeting_strategy)
@settings(max_examples=50)
def test_mydsl::greeting_instantiation(instance):
    assert isinstance(instance, mydsl::Greeting)

@given(instance=mydsl::Greeting_strategy)
def test_mydsl::greeting_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mydsl::Greeting_strategy)
def test_mydsl::greeting_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mydsl::Model_strategy)
@settings(max_examples=50)
def test_mydsl::model_instantiation(instance):
    assert isinstance(instance, mydsl::Model)
