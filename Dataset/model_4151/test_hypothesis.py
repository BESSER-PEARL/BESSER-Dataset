import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Greeting,
    greetings::RefGreeting,
    greetings::HelloGreeting,
    greetings::Greeting,
    greetings::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_greeting_is_not_abstract():
    assert not inspect.isabstract(Greeting)


def test_greeting_constructor_exists():
    assert callable(Greeting.__init__)


def test_greeting_constructor_args():
    sig = inspect.signature(Greeting.__init__)
    params = list(sig.parameters.keys())



def test_greetings::refgreeting_is_not_abstract():
    assert not inspect.isabstract(greetings::RefGreeting)


def test_greetings::refgreeting_constructor_exists():
    assert callable(greetings::RefGreeting.__init__)


def test_greetings::refgreeting_constructor_args():
    sig = inspect.signature(greetings::RefGreeting.__init__)
    params = list(sig.parameters.keys())



def test_greetings::hellogreeting_is_not_abstract():
    assert not inspect.isabstract(greetings::HelloGreeting)


def test_greetings::hellogreeting_constructor_exists():
    assert callable(greetings::HelloGreeting.__init__)


def test_greetings::hellogreeting_constructor_args():
    sig = inspect.signature(greetings::HelloGreeting.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_greetings::hellogreeting_has_name():
    assert hasattr(greetings::HelloGreeting, "name")
    descriptor = None
    for klass in greetings::HelloGreeting.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_greetings::greeting_is_not_abstract():
    assert not inspect.isabstract(greetings::Greeting)


def test_greetings::greeting_constructor_exists():
    assert callable(greetings::Greeting.__init__)


def test_greetings::greeting_constructor_args():
    sig = inspect.signature(greetings::Greeting.__init__)
    params = list(sig.parameters.keys())



def test_greetings::model_is_not_abstract():
    assert not inspect.isabstract(greetings::Model)


def test_greetings::model_constructor_exists():
    assert callable(greetings::Model.__init__)


def test_greetings::model_constructor_args():
    sig = inspect.signature(greetings::Model.__init__)
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
Greeting_strategy = st.builds(
    Greeting,
)
greetings::RefGreeting_strategy = st.builds(
    greetings::RefGreeting,
)
greetings::HelloGreeting_strategy = st.builds(
    greetings::HelloGreeting,
    name=
        safe_text
)
greetings::Greeting_strategy = st.builds(
    greetings::Greeting,
)
greetings::Model_strategy = st.builds(
    greetings::Model,
)

@given(instance=Greeting_strategy)
@settings(max_examples=50)
def test_greeting_instantiation(instance):
    assert isinstance(instance, Greeting)

@given(instance=greetings::RefGreeting_strategy)
@settings(max_examples=50)
def test_greetings::refgreeting_instantiation(instance):
    assert isinstance(instance, greetings::RefGreeting)

@given(instance=greetings::HelloGreeting_strategy)
@settings(max_examples=50)
def test_greetings::hellogreeting_instantiation(instance):
    assert isinstance(instance, greetings::HelloGreeting)

@given(instance=greetings::HelloGreeting_strategy)
def test_greetings::hellogreeting_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=greetings::HelloGreeting_strategy)
def test_greetings::hellogreeting_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=greetings::Greeting_strategy)
@settings(max_examples=50)
def test_greetings::greeting_instantiation(instance):
    assert isinstance(instance, greetings::Greeting)

@given(instance=greetings::Model_strategy)
@settings(max_examples=50)
def test_greetings::model_instantiation(instance):
    assert isinstance(instance, greetings::Model)
