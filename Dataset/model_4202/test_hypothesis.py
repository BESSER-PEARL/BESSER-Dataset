import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    helloWorld::KeywordsExample,
    helloWorld::Greeting,
    helloWorld::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_helloworld::keywordsexample_is_not_abstract():
    assert not inspect.isabstract(helloWorld::KeywordsExample)


def test_helloworld::keywordsexample_constructor_exists():
    assert callable(helloWorld::KeywordsExample.__init__)


def test_helloworld::keywordsexample_constructor_args():
    sig = inspect.signature(helloWorld::KeywordsExample.__init__)
    params = list(sig.parameters.keys())
    assert "option" in params, "Missing parameter 'option'"

def test_helloworld::keywordsexample_has_option():
    assert hasattr(helloWorld::KeywordsExample, "option")
    descriptor = None
    for klass in helloWorld::KeywordsExample.__mro__:
        if "option" in klass.__dict__:
            descriptor = klass.__dict__["option"]
            break
    assert isinstance(descriptor, property)



def test_helloworld::greeting_is_not_abstract():
    assert not inspect.isabstract(helloWorld::Greeting)


def test_helloworld::greeting_constructor_exists():
    assert callable(helloWorld::Greeting.__init__)


def test_helloworld::greeting_constructor_args():
    sig = inspect.signature(helloWorld::Greeting.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_helloworld::greeting_has_name():
    assert hasattr(helloWorld::Greeting, "name")
    descriptor = None
    for klass in helloWorld::Greeting.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_helloworld::model_is_not_abstract():
    assert not inspect.isabstract(helloWorld::Model)


def test_helloworld::model_constructor_exists():
    assert callable(helloWorld::Model.__init__)


def test_helloworld::model_constructor_args():
    sig = inspect.signature(helloWorld::Model.__init__)
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
helloWorld::KeywordsExample_strategy = st.builds(
    helloWorld::KeywordsExample,
    option=
        safe_text
)
helloWorld::Greeting_strategy = st.builds(
    helloWorld::Greeting,
    name=
        safe_text
)
helloWorld::Model_strategy = st.builds(
    helloWorld::Model,
)

@given(instance=helloWorld::KeywordsExample_strategy)
@settings(max_examples=50)
def test_helloworld::keywordsexample_instantiation(instance):
    assert isinstance(instance, helloWorld::KeywordsExample)

@given(instance=helloWorld::KeywordsExample_strategy)
def test_helloworld::keywordsexample_option_type(instance):
    assert isinstance(instance.option, str)


@given(instance=helloWorld::KeywordsExample_strategy)
def test_helloworld::keywordsexample_option_setter(instance):
    original = instance.option
    instance.option = original
    assert instance.option == original

@given(instance=helloWorld::Greeting_strategy)
@settings(max_examples=50)
def test_helloworld::greeting_instantiation(instance):
    assert isinstance(instance, helloWorld::Greeting)

@given(instance=helloWorld::Greeting_strategy)
def test_helloworld::greeting_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=helloWorld::Greeting_strategy)
def test_helloworld::greeting_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=helloWorld::Model_strategy)
@settings(max_examples=50)
def test_helloworld::model_instantiation(instance):
    assert isinstance(instance, helloWorld::Model)
