import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    helloworld2::GreetingMessage,
    helloworld2::Greeting,
    helloworld2::Person,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_helloworld2::greetingmessage_is_not_abstract():
    assert not inspect.isabstract(helloworld2::GreetingMessage)


def test_helloworld2::greetingmessage_constructor_exists():
    assert callable(helloworld2::GreetingMessage.__init__)


def test_helloworld2::greetingmessage_constructor_args():
    sig = inspect.signature(helloworld2::GreetingMessage.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_helloworld2::greetingmessage_has_text():
    assert hasattr(helloworld2::GreetingMessage, "text")
    descriptor = None
    for klass in helloworld2::GreetingMessage.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_helloworld2::greeting_is_not_abstract():
    assert not inspect.isabstract(helloworld2::Greeting)


def test_helloworld2::greeting_constructor_exists():
    assert callable(helloworld2::Greeting.__init__)


def test_helloworld2::greeting_constructor_args():
    sig = inspect.signature(helloworld2::Greeting.__init__)
    params = list(sig.parameters.keys())



def test_helloworld2::person_is_not_abstract():
    assert not inspect.isabstract(helloworld2::Person)


def test_helloworld2::person_constructor_exists():
    assert callable(helloworld2::Person.__init__)


def test_helloworld2::person_constructor_args():
    sig = inspect.signature(helloworld2::Person.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_helloworld2::person_has_name():
    assert hasattr(helloworld2::Person, "name")
    descriptor = None
    for klass in helloworld2::Person.__mro__:
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
helloworld2::GreetingMessage_strategy = st.builds(
    helloworld2::GreetingMessage,
    text=
        safe_text
)
helloworld2::Greeting_strategy = st.builds(
    helloworld2::Greeting,
)
helloworld2::Person_strategy = st.builds(
    helloworld2::Person,
    name=
        safe_text
)

@given(instance=helloworld2::GreetingMessage_strategy)
@settings(max_examples=50)
def test_helloworld2::greetingmessage_instantiation(instance):
    assert isinstance(instance, helloworld2::GreetingMessage)

@given(instance=helloworld2::GreetingMessage_strategy)
def test_helloworld2::greetingmessage_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=helloworld2::GreetingMessage_strategy)
def test_helloworld2::greetingmessage_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=helloworld2::Greeting_strategy)
@settings(max_examples=50)
def test_helloworld2::greeting_instantiation(instance):
    assert isinstance(instance, helloworld2::Greeting)

@given(instance=helloworld2::Person_strategy)
@settings(max_examples=50)
def test_helloworld2::person_instantiation(instance):
    assert isinstance(instance, helloworld2::Person)

@given(instance=helloworld2::Person_strategy)
def test_helloworld2::person_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=helloworld2::Person_strategy)
def test_helloworld2::person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
