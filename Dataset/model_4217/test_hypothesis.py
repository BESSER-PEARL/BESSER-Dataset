import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    helloworldext_Greeting,
    helloworldext_Person,
    helloworldext_GreetingMessage,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_helloworldext_greeting_is_not_abstract():
    assert not inspect.isabstract(helloworldext_Greeting)


def test_helloworldext_greeting_constructor_exists():
    assert callable(helloworldext_Greeting.__init__)


def test_helloworldext_greeting_constructor_args():
    sig = inspect.signature(helloworldext_Greeting.__init__)
    params = list(sig.parameters.keys())



def test_helloworldext_person_is_not_abstract():
    assert not inspect.isabstract(helloworldext_Person)


def test_helloworldext_person_constructor_exists():
    assert callable(helloworldext_Person.__init__)


def test_helloworldext_person_constructor_args():
    sig = inspect.signature(helloworldext_Person.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_helloworldext_person_has_name():
    assert hasattr(helloworldext_Person, "name")
    descriptor = None
    for klass in helloworldext_Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_helloworldext_greetingmessage_is_not_abstract():
    assert not inspect.isabstract(helloworldext_GreetingMessage)


def test_helloworldext_greetingmessage_constructor_exists():
    assert callable(helloworldext_GreetingMessage.__init__)


def test_helloworldext_greetingmessage_constructor_args():
    sig = inspect.signature(helloworldext_GreetingMessage.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_helloworldext_greetingmessage_has_text():
    assert hasattr(helloworldext_GreetingMessage, "text")
    descriptor = None
    for klass in helloworldext_GreetingMessage.__mro__:
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
helloworldext_Greeting_strategy = st.builds(
    helloworldext_Greeting,
)
helloworldext_Person_strategy = st.builds(
    helloworldext_Person,
    name=
        safe_text
)
helloworldext_GreetingMessage_strategy = st.builds(
    helloworldext_GreetingMessage,
    text=
        safe_text
)

@given(instance=helloworldext_Greeting_strategy)
@settings(max_examples=50)
def test_helloworldext_greeting_instantiation(instance):
    assert isinstance(instance, helloworldext_Greeting)

@given(instance=helloworldext_Person_strategy)
@settings(max_examples=50)
def test_helloworldext_person_instantiation(instance):
    assert isinstance(instance, helloworldext_Person)



@given(instance=helloworldext_Person_strategy)
def test_helloworldext_person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=helloworldext_GreetingMessage_strategy)
@settings(max_examples=50)
def test_helloworldext_greetingmessage_instantiation(instance):
    assert isinstance(instance, helloworldext_GreetingMessage)



@given(instance=helloworldext_GreetingMessage_strategy)
def test_helloworldext_greetingmessage_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original
