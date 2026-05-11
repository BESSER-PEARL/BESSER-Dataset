import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    datavault::Greeting,
    datavault::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_datavault::greeting_is_not_abstract():
    assert not inspect.isabstract(datavault::Greeting)


def test_datavault::greeting_constructor_exists():
    assert callable(datavault::Greeting.__init__)


def test_datavault::greeting_constructor_args():
    sig = inspect.signature(datavault::Greeting.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_datavault::greeting_has_name():
    assert hasattr(datavault::Greeting, "name")
    descriptor = None
    for klass in datavault::Greeting.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_datavault::model_is_not_abstract():
    assert not inspect.isabstract(datavault::Model)


def test_datavault::model_constructor_exists():
    assert callable(datavault::Model.__init__)


def test_datavault::model_constructor_args():
    sig = inspect.signature(datavault::Model.__init__)
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
datavault::Greeting_strategy = st.builds(
    datavault::Greeting,
    name=
        safe_text
)
datavault::Model_strategy = st.builds(
    datavault::Model,
)

@given(instance=datavault::Greeting_strategy)
@settings(max_examples=50)
def test_datavault::greeting_instantiation(instance):
    assert isinstance(instance, datavault::Greeting)

@given(instance=datavault::Greeting_strategy)
def test_datavault::greeting_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=datavault::Greeting_strategy)
def test_datavault::greeting_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=datavault::Model_strategy)
@settings(max_examples=50)
def test_datavault::model_instantiation(instance):
    assert isinstance(instance, datavault::Model)
