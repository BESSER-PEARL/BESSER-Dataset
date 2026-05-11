import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    helloworldext::Greeting,
    helloworldext::Person,
    helloworldext::GreetingMessage,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_helloworldext::greeting_is_not_abstract():
    assert not inspect.isabstract(helloworldext::Greeting)


def test_helloworldext::greeting_constructor_exists():
    assert callable(helloworldext::Greeting.__init__)


def test_helloworldext::greeting_constructor_args():
    sig = inspect.signature(helloworldext::Greeting.__init__)
    params = list(sig.parameters.keys())



def test_helloworldext::person_is_not_abstract():
    assert not inspect.isabstract(helloworldext::Person)


def test_helloworldext::person_constructor_exists():
    assert callable(helloworldext::Person.__init__)


def test_helloworldext::person_constructor_args():
    sig = inspect.signature(helloworldext::Person.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_helloworldext::person_has_name():
    assert hasattr(helloworldext::Person, "name")
    descriptor = None
    for klass in helloworldext::Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_helloworldext::greetingmessage_is_not_abstract():
    assert not inspect.isabstract(helloworldext::GreetingMessage)


def test_helloworldext::greetingmessage_constructor_exists():
    assert callable(helloworldext::GreetingMessage.__init__)


def test_helloworldext::greetingmessage_constructor_args():
    sig = inspect.signature(helloworldext::GreetingMessage.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_helloworldext::greetingmessage_has_text():
    assert hasattr(helloworldext::GreetingMessage, "text")
    descriptor = None
    for klass in helloworldext::GreetingMessage.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
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
helloworldext::Greeting_strategy = st.builds(
    helloworldext::Greeting,
)
helloworldext::Person_strategy = st.builds(
    helloworldext::Person,
    name=
        safe_text
)
helloworldext::GreetingMessage_strategy = st.builds(
    helloworldext::GreetingMessage,
    text=
        safe_text
)

@given(instance=helloworldext::Greeting_strategy)
@settings(max_examples=50)
def test_helloworldext::greeting_instantiation(instance):
    assert isinstance(instance, helloworldext::Greeting)

@given(instance=helloworldext::Person_strategy)
@settings(max_examples=50)
def test_helloworldext::person_instantiation(instance):
    assert isinstance(instance, helloworldext::Person)

@given(instance=helloworldext::Person_strategy)
def test_helloworldext::person_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=helloworldext::Person_strategy)
def test_helloworldext::person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=helloworldext::GreetingMessage_strategy)
@settings(max_examples=50)
def test_helloworldext::greetingmessage_instantiation(instance):
    assert isinstance(instance, helloworldext::GreetingMessage)

@given(instance=helloworldext::GreetingMessage_strategy)
def test_helloworldext::greetingmessage_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=helloworldext::GreetingMessage_strategy)
def test_helloworldext::greetingmessage_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original
