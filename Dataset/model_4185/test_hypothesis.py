import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    kobold::Greeting,
    kobold::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_kobold::greeting_is_not_abstract():
    assert not inspect.isabstract(kobold::Greeting)


def test_kobold::greeting_constructor_exists():
    assert callable(kobold::Greeting.__init__)


def test_kobold::greeting_constructor_args():
    sig = inspect.signature(kobold::Greeting.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_kobold::greeting_has_name():
    assert hasattr(kobold::Greeting, "name")
    descriptor = None
    for klass in kobold::Greeting.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_kobold::model_is_not_abstract():
    assert not inspect.isabstract(kobold::Model)


def test_kobold::model_constructor_exists():
    assert callable(kobold::Model.__init__)


def test_kobold::model_constructor_args():
    sig = inspect.signature(kobold::Model.__init__)
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
kobold::Greeting_strategy = st.builds(
    kobold::Greeting,
    name=
        safe_text
)
kobold::Model_strategy = st.builds(
    kobold::Model,
)

@given(instance=kobold::Greeting_strategy)
@settings(max_examples=50)
def test_kobold::greeting_instantiation(instance):
    assert isinstance(instance, kobold::Greeting)

@given(instance=kobold::Greeting_strategy)
def test_kobold::greeting_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=kobold::Greeting_strategy)
def test_kobold::greeting_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=kobold::Model_strategy)
@settings(max_examples=50)
def test_kobold::model_instantiation(instance):
    assert isinstance(instance, kobold::Model)
