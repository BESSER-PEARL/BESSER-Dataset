import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    helloworld2_GreetingMessage,
    helloworld2_Greeting,
    helloworld2_Person,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_helloworld2_greetingmessage_is_not_abstract():
    assert not inspect.isabstract(helloworld2_GreetingMessage)


def test_helloworld2_greetingmessage_constructor_exists():
    assert callable(helloworld2_GreetingMessage.__init__)


def test_helloworld2_greetingmessage_constructor_args():
    sig = inspect.signature(helloworld2_GreetingMessage.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_helloworld2_greetingmessage_has_text():
    assert hasattr(helloworld2_GreetingMessage, "text")
    descriptor = None
    for klass in helloworld2_GreetingMessage.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_helloworld2_greeting_is_not_abstract():
    assert not inspect.isabstract(helloworld2_Greeting)


def test_helloworld2_greeting_constructor_exists():
    assert callable(helloworld2_Greeting.__init__)


def test_helloworld2_greeting_constructor_args():
    sig = inspect.signature(helloworld2_Greeting.__init__)
    params = list(sig.parameters.keys())



def test_helloworld2_person_is_not_abstract():
    assert not inspect.isabstract(helloworld2_Person)


def test_helloworld2_person_constructor_exists():
    assert callable(helloworld2_Person.__init__)


def test_helloworld2_person_constructor_args():
    sig = inspect.signature(helloworld2_Person.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_helloworld2_person_has_name():
    assert hasattr(helloworld2_Person, "name")
    descriptor = None
    for klass in helloworld2_Person.__mro__:
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
helloworld2_GreetingMessage_strategy = st.builds(
    helloworld2_GreetingMessage,
    text=
        safe_text
)
helloworld2_Greeting_strategy = st.builds(
    helloworld2_Greeting,
)
helloworld2_Person_strategy = st.builds(
    helloworld2_Person,
    name=
        safe_text
)

@given(instance=helloworld2_GreetingMessage_strategy)
@settings(max_examples=50)
def test_helloworld2_greetingmessage_instantiation(instance):
    assert isinstance(instance, helloworld2_GreetingMessage)



@given(instance=helloworld2_GreetingMessage_strategy)
def test_helloworld2_greetingmessage_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=helloworld2_Greeting_strategy)
@settings(max_examples=50)
def test_helloworld2_greeting_instantiation(instance):
    assert isinstance(instance, helloworld2_Greeting)

@given(instance=helloworld2_Person_strategy)
@settings(max_examples=50)
def test_helloworld2_person_instantiation(instance):
    assert isinstance(instance, helloworld2_Person)



@given(instance=helloworld2_Person_strategy)
def test_helloworld2_person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
