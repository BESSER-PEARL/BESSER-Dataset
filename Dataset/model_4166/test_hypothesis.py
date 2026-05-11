import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    myDsl1::Greeting,
    myDsl1::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mydsl1::greeting_is_not_abstract():
    assert not inspect.isabstract(myDsl1::Greeting)


def test_mydsl1::greeting_constructor_exists():
    assert callable(myDsl1::Greeting.__init__)


def test_mydsl1::greeting_constructor_args():
    sig = inspect.signature(myDsl1::Greeting.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl1::greeting_has_name():
    assert hasattr(myDsl1::Greeting, "name")
    descriptor = None
    for klass in myDsl1::Greeting.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl1::model_is_not_abstract():
    assert not inspect.isabstract(myDsl1::Model)


def test_mydsl1::model_constructor_exists():
    assert callable(myDsl1::Model.__init__)


def test_mydsl1::model_constructor_args():
    sig = inspect.signature(myDsl1::Model.__init__)
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
myDsl1::Greeting_strategy = st.builds(
    myDsl1::Greeting,
    name=
        safe_text
)
myDsl1::Model_strategy = st.builds(
    myDsl1::Model,
)

@given(instance=myDsl1::Greeting_strategy)
@settings(max_examples=50)
def test_mydsl1::greeting_instantiation(instance):
    assert isinstance(instance, myDsl1::Greeting)

@given(instance=myDsl1::Greeting_strategy)
def test_mydsl1::greeting_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl1::Greeting_strategy)
def test_mydsl1::greeting_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl1::Model_strategy)
@settings(max_examples=50)
def test_mydsl1::model_instantiation(instance):
    assert isinstance(instance, myDsl1::Model)
