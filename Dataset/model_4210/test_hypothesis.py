import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    myDsl::Greeting,
    myDsl::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mydsl::greeting_is_not_abstract():
    assert not inspect.isabstract(myDsl::Greeting)


def test_mydsl::greeting_constructor_exists():
    assert callable(myDsl::Greeting.__init__)


def test_mydsl::greeting_constructor_args():
    sig = inspect.signature(myDsl::Greeting.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::greeting_has_name():
    assert hasattr(myDsl::Greeting, "name")
    descriptor = None
    for klass in myDsl::Greeting.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::model_is_not_abstract():
    assert not inspect.isabstract(myDsl::Model)


def test_mydsl::model_constructor_exists():
    assert callable(myDsl::Model.__init__)


def test_mydsl::model_constructor_args():
    sig = inspect.signature(myDsl::Model.__init__)
    params = list(sig.parameters.keys())
    assert "greetings" in params, "Missing parameter 'greetings'"

def test_mydsl::model_has_greetings():
    assert hasattr(myDsl::Model, "greetings")
    descriptor = None
    for klass in myDsl::Model.__mro__:
        if "greetings" in klass.__dict__:
            descriptor = klass.__dict__["greetings"]
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
myDsl::Greeting_strategy = st.builds(
    myDsl::Greeting,
    name=
        safe_text
)
myDsl::Model_strategy = st.builds(
    myDsl::Model,
    greetings=
        safe_text
)

@given(instance=myDsl::Greeting_strategy)
@settings(max_examples=50)
def test_mydsl::greeting_instantiation(instance):
    assert isinstance(instance, myDsl::Greeting)

@given(instance=myDsl::Greeting_strategy)
def test_mydsl::greeting_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::Greeting_strategy)
def test_mydsl::greeting_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl::Model_strategy)
@settings(max_examples=50)
def test_mydsl::model_instantiation(instance):
    assert isinstance(instance, myDsl::Model)

@given(instance=myDsl::Model_strategy)
def test_mydsl::model_greetings_type(instance):
    assert isinstance(instance.greetings, str)


@given(instance=myDsl::Model_strategy)
def test_mydsl::model_greetings_setter(instance):
    original = instance.greetings
    instance.greetings = original
    assert instance.greetings == original
