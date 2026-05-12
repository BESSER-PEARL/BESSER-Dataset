import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Greeting,
    greetings_RefGreeting,
    greetings_HelloGreeting,
    greetings_Greeting,
    greetings_Model,
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



def test_greetings_refgreeting_is_not_abstract():
    assert not inspect.isabstract(greetings_RefGreeting)


def test_greetings_refgreeting_constructor_exists():
    assert callable(greetings_RefGreeting.__init__)


def test_greetings_refgreeting_constructor_args():
    sig = inspect.signature(greetings_RefGreeting.__init__)
    params = list(sig.parameters.keys())



def test_greetings_hellogreeting_is_not_abstract():
    assert not inspect.isabstract(greetings_HelloGreeting)


def test_greetings_hellogreeting_constructor_exists():
    assert callable(greetings_HelloGreeting.__init__)


def test_greetings_hellogreeting_constructor_args():
    sig = inspect.signature(greetings_HelloGreeting.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_greetings_hellogreeting_has_name():
    assert hasattr(greetings_HelloGreeting, "name")
    descriptor = None
    for klass in greetings_HelloGreeting.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_greetings_greeting_is_not_abstract():
    assert not inspect.isabstract(greetings_Greeting)


def test_greetings_greeting_constructor_exists():
    assert callable(greetings_Greeting.__init__)


def test_greetings_greeting_constructor_args():
    sig = inspect.signature(greetings_Greeting.__init__)
    params = list(sig.parameters.keys())



def test_greetings_model_is_not_abstract():
    assert not inspect.isabstract(greetings_Model)


def test_greetings_model_constructor_exists():
    assert callable(greetings_Model.__init__)


def test_greetings_model_constructor_args():
    sig = inspect.signature(greetings_Model.__init__)
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
greetings_RefGreeting_strategy = st.builds(
    greetings_RefGreeting,
)
greetings_HelloGreeting_strategy = st.builds(
    greetings_HelloGreeting,
    name=
        safe_text
)
greetings_Greeting_strategy = st.builds(
    greetings_Greeting,
)
greetings_Model_strategy = st.builds(
    greetings_Model,
)

@given(instance=Greeting_strategy)
@settings(max_examples=50)
def test_greeting_instantiation(instance):
    assert isinstance(instance, Greeting)

@given(instance=greetings_RefGreeting_strategy)
@settings(max_examples=50)
def test_greetings_refgreeting_instantiation(instance):
    assert isinstance(instance, greetings_RefGreeting)

@given(instance=greetings_HelloGreeting_strategy)
@settings(max_examples=50)
def test_greetings_hellogreeting_instantiation(instance):
    assert isinstance(instance, greetings_HelloGreeting)



@given(instance=greetings_HelloGreeting_strategy)
def test_greetings_hellogreeting_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=greetings_Greeting_strategy)
@settings(max_examples=50)
def test_greetings_greeting_instantiation(instance):
    assert isinstance(instance, greetings_Greeting)

@given(instance=greetings_Model_strategy)
@settings(max_examples=50)
def test_greetings_model_instantiation(instance):
    assert isinstance(instance, greetings_Model)
