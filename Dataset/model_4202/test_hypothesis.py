import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    helloWorld_KeywordsExample,
    helloWorld_Greeting,
    helloWorld_Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_helloworld_keywordsexample_is_not_abstract():
    assert not inspect.isabstract(helloWorld_KeywordsExample)


def test_helloworld_keywordsexample_constructor_exists():
    assert callable(helloWorld_KeywordsExample.__init__)


def test_helloworld_keywordsexample_constructor_args():
    sig = inspect.signature(helloWorld_KeywordsExample.__init__)
    params = list(sig.parameters.keys())
    assert "option" in params, "Missing parameter 'option'"

def test_helloworld_keywordsexample_has_option():
    assert hasattr(helloWorld_KeywordsExample, "option")
    descriptor = None
    for klass in helloWorld_KeywordsExample.__mro__:
        if "option" in klass.__dict__:
            descriptor = klass.__dict__["option"]
            break
    assert isinstance(descriptor, property)



def test_helloworld_greeting_is_not_abstract():
    assert not inspect.isabstract(helloWorld_Greeting)


def test_helloworld_greeting_constructor_exists():
    assert callable(helloWorld_Greeting.__init__)


def test_helloworld_greeting_constructor_args():
    sig = inspect.signature(helloWorld_Greeting.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_helloworld_greeting_has_name():
    assert hasattr(helloWorld_Greeting, "name")
    descriptor = None
    for klass in helloWorld_Greeting.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_helloworld_model_is_not_abstract():
    assert not inspect.isabstract(helloWorld_Model)


def test_helloworld_model_constructor_exists():
    assert callable(helloWorld_Model.__init__)


def test_helloworld_model_constructor_args():
    sig = inspect.signature(helloWorld_Model.__init__)
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
helloWorld_KeywordsExample_strategy = st.builds(
    helloWorld_KeywordsExample,
    option=
        safe_text
)
helloWorld_Greeting_strategy = st.builds(
    helloWorld_Greeting,
    name=
        safe_text
)
helloWorld_Model_strategy = st.builds(
    helloWorld_Model,
)

@given(instance=helloWorld_KeywordsExample_strategy)
@settings(max_examples=50)
def test_helloworld_keywordsexample_instantiation(instance):
    assert isinstance(instance, helloWorld_KeywordsExample)



@given(instance=helloWorld_KeywordsExample_strategy)
def test_helloworld_keywordsexample_option_setter(instance):
    original = instance.option
    instance.option = original
    assert instance.option == original

@given(instance=helloWorld_Greeting_strategy)
@settings(max_examples=50)
def test_helloworld_greeting_instantiation(instance):
    assert isinstance(instance, helloWorld_Greeting)



@given(instance=helloWorld_Greeting_strategy)
def test_helloworld_greeting_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=helloWorld_Model_strategy)
@settings(max_examples=50)
def test_helloworld_model_instantiation(instance):
    assert isinstance(instance, helloWorld_Model)
